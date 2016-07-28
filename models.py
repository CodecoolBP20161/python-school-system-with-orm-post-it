from peewee import *
from application_code import generator

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
        # if self.closest_school is None:
        return City.select(City.closest_school_id).where(City.city_name == self.hometown)

    @classmethod
    def assign_app_code(cls):
        for row in cls.select().where(cls.application_code >> None):
            row.application_code = generator()
            row.save()
