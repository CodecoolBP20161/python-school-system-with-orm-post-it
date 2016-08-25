from peewee import *
from application_code import generator
import random

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop

with open('login.txt', 'r') as f:
    dbname = f.readline().strip()
db = PostgresqlDatabase(dbname, user=dbname)  # , password='TheTibi87', host='localhost')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class School(BaseModel):
    school_name = CharField()


class City(BaseModel):
    city_name = CharField()
    closest_school_id = ForeignKeyField(School)


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
        # fixme: should check only mentors from the same school
        available = InterviewSlot.select(InterviewSlot.slot
        ).where(
            InterviewSlot.free == True  # , self.closest_school == InterviewSlot.mentor
        ).group_by(
            InterviewSlot.slot
        ).having(
            fn.Count(InterviewSlot.mentor) > 1
        ).get()
        return available.slot

    @classmethod
    def assign_interview(cls):
        students = cls.select(cls.id).join(
            Interview, join_type=JOIN_LEFT_OUTER
        ).where(Interview.applicant_id >> None).execute()

        for row in students:
            # find a suitable interview slot
            slot_to_reserve = Applicant.available_slot(row)
            # update Interview table with slot and applicant
            new_interview = Interview.insert(slot=slot_to_reserve, applicant_id=row.id).execute()
            #
            av_mentors = InterviewSlot.select().where(InterviewSlot.slot == slot_to_reserve).limit(2).execute()
            for av_mentor in av_mentors:
                InterviewSlot.update(free=False).where(InterviewSlot.mentor == 1).execute()
                MentorInterview.insert(mentor_id=1, interview_id=new_interview).execute()
            # Interview.create(slot=slot_to_reserve, applicant_id=row.id)
            # todo: choose two mentors from the selected slot


# Story 2


class Mentor(BaseModel):
    first_name = TextField()
    last_name = TextField()
    school = ForeignKeyField(School, related_name='mentors')
    # available = DateField()


class Interview(BaseModel):
    slot = DateTimeField()
    applicant_id = ForeignKeyField(Applicant, related_name='interview')


class InterviewSlot(BaseModel):
    slot = DateTimeField()
    mentor = ForeignKeyField(Mentor, related_name='interview_slots')
    free = BooleanField()


class MentorInterview(BaseModel):
    mentor_id = ForeignKeyField(Mentor)
    interview_id = ForeignKeyField(Interview)
