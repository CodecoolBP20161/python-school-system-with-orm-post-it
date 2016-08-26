from peewee import *
from application_code import generator

with open('login.txt', 'r') as f:
    dbname = f.readline().strip()
db = PostgresqlDatabase(dbname, user=dbname)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class School(BaseModel):
    school_name = CharField()


class City(BaseModel):
    city_name = CharField()
    closest_school_id = ForeignKeyField(School)


class Mentor(BaseModel):
    first_name = TextField()
    last_name = TextField()
    school = ForeignKeyField(School, related_name='mentors')
    # available = DateField()


class InterviewSlot(BaseModel):
    slot = DateTimeField()
    mentor = ForeignKeyField(Mentor, related_name='interview_slots')
    free = BooleanField()


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    hometown = CharField()
    application_code = CharField(null=True)
    status = CharField()
    closest_school = ForeignKeyField(School, null=True)
    application_time = DateField()

    def get_closest_school_id(self):
        return City.select(
            City.closest_school_id
        ).join(
            Applicant, on=(Applicant.hometown == City.city_name)
        ).where(Applicant.id == self.id)

    @classmethod
    def assign_school(cls):
        for row in cls.select().where(cls.closest_school >> None).execute():
            row.closest_school = row.get_closest_school_id()
            row.save()

    @classmethod
    def assign_app_code(cls):
        for row in cls.select().where(cls.application_code >> None):
            row.application_code = generator()
            row.save()

    def available_slot(self):
        available = InterviewSlot.select(
            InterviewSlot.slot
        ).join(
            Mentor
        ).where(
            InterviewSlot.free == True,
            self.closest_school.id == Mentor.school
        ).group_by(
            InterviewSlot.slot
        ).having(
            fn.Count(InterviewSlot.mentor) > 1
        ).get()
        return available.slot

    @classmethod
    def assign_interview(cls):
        students = cls.select().join(
            Interview, join_type=JOIN_LEFT_OUTER
        ).where(Interview.applicant_id >> None)

        for row in students:
            # find a suitable interview slot
            slot_to_reserve = row.available_slot()
            # update Interview table with slot and applicant
            new_interview = Interview.insert(slot=slot_to_reserve, applicant_id=row.id).execute()
            #
            av_mentors = InterviewSlot.select().where(InterviewSlot.slot == slot_to_reserve).limit(2).execute()
            for av_mentor in av_mentors:
                av_mentor.free = False
                av_mentor.save()
                MentorInterview.insert(mentor_id=av_mentor.mentor.id, interview_id=new_interview).execute()


class Interview(BaseModel):
    slot = DateTimeField()
    applicant_id = ForeignKeyField(Applicant, related_name='interview')


class MentorInterview(BaseModel):
    mentor_id = ForeignKeyField(Mentor)
    interview_id = ForeignKeyField(Interview)
