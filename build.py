# This script can create the database tables based on your models

from models import *

db.connect()


def start_over_database():
    db.drop_tables([Applicant, School, City, Mentor, Interview, InterviewSlot, MentorInterview], cascade=True)
    make_tables()


def make_tables():
    db.create_tables([Applicant, School, City, Mentor, Interview, InterviewSlot, MentorInterview], safe=True)
