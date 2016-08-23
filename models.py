from peewee import *
from application_code import generator
import random

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
dbname = 'tiborkiss'  # input("Please enter the database name and user (should be your username on your laptop): ")
db = PostgresqlDatabase(dbname, user=dbname, password='TheTibi87', host='localhost')


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
        return City.select(City.closest_school_id).where(City.city_name == self.hometown)

    @classmethod
    def school_to_applicant(cls):
        q = cls.select().where(cls.closest_school >> None).execute()
        for row in q:
            row.closest_school = row.get_closest_school_id()
            row.save()

    @classmethod
    def assign_app_code(cls):
        for row in cls.select().where(cls.application_code >> None):
            row.application_code = generator()
            row.save()

    def make_interview(self):
        print('hey')
        q = Mentor.select().join(Applicant, on=Mentor.school == Applicant.closest_school)\
                .where(Applicant.id == self.id).execute()
        for i in q:
            print(q.__dict__)




    @classmethod
    def find_applicant_without_interview(cls):
        q = cls.select().join(Interview, join_type=JOIN_LEFT_OUTER).where(Interview.applicant_id >> None).execute()

        for row in q:
            # print(row.__dict__)
            row.make_interview()
            # row.save()



# Story 2


class Mentor(BaseModel):
    first_name = TextField()
    last_name = TextField()
    school = ForeignKeyField(School)
    # available = DateField()




class Interview(BaseModel):
    slot = DateTimeField()
    applicant_id = ForeignKeyField(Applicant)


class InterviewSlot(BaseModel):
    slot = DateTimeField()
    mentor = ForeignKeyField(Mentor)
    availability = BooleanField()


class MentorInterview(BaseModel):
    mentor_id = ForeignKeyField(Mentor)
    interview_id = ForeignKeyField(Interview)
