from peewee import *
from application_code import generator
import random

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
dbname = input("Please enter the database name and user (should be your username on your laptop): ")
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
        for row in cls.select().where(cls.closest_school >> None):
            row.closest_school = row.get_closest_school_id()
            row.save()

    @classmethod
    def assign_app_code(cls):
        for row in cls.select().where(cls.application_code >> None):
            row.application_code = generator()
            row.save()

# Story 2


class Mentor(BaseModel):
    first_name = TextField()
    last_name = TextField()
    school = ForeignKeyField(School)
    # available = DateField()


class Interview(BaseModel):
    mentor = ForeignKeyField(Mentor)
    applicant = ForeignKeyField(Applicant)
    # interview_time = ForeignKeyField(InterviewSlot)


    def make_interview(self):
        print(
        random.choice(InterviewSlot\
        .select()\
        .join(Mentor)\
        .join(Applicant)\
        .where(Mentor.school_id == self.closest_school_id and InterviewSlot.interview_id >> None)).slot)


    @classmethod
    def find_applicant_without_interview(cls):
        for row in cls.select().join(Applicant, join_type=JOIN_LEFT_OUTER).where(cls.applicant >> None):
            row.make_interview()
            row.save()



class InterviewSlot(BaseModel):
    interview_id = ForeignKeyField(Interview, null=True)
    slot = DateTimeField()
    available_mentor = ForeignKeyField(Mentor)
