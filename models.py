from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('krs', user='krs')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    hometown = CharField()
    application_code = CharField(null=False)
    status = CharField()
    closest_school = ForeignKeyField(School)
    application_time = DateField()



class City(BaseModel):
    city = CharField()
    # closest_school = ForeignKeyField(School)



class School(BaseModel):
    school = CharField()
