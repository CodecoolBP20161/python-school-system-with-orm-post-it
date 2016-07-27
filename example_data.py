# This script can generate example data for "City" and "InterviewSlot" models.
import random
import datetime
from models import *
from application_code import generator


# ccbudapest = School.create(school='Budapest school')
# ccmiskolc = School.create(school='Miskolc school')
# cckrakow = School.create(school='Krakow school')


schools = [{'school': 'Budapest school'},
           {'school': 'Miskolc school'},
           {'school': 'Krakow school'}]

for school in schools:
    s = School(**school)
    s.save()

applicants = [{
    'first_name': "Levente",
    'last_name': "Csanyi",
    'hometown': "Pecs",
    'application_code': generator(),
    'status': 'new',
    'application_time': datetime.date(1988, 12, 1)},
    {
        'first_name': "Lvnt",
        'last_name': "Cny",
        'hometown': "Pecs",
        'application_code': generator(),
        'status': 'new',
        'application_time': datetime.date(1928, 12, 1)}
]

for applicant in applicants:
    a = Applicant(**applicant)
    a.save()

city = [{'city': 'Budapest'}]

for c in city:
    ct = City(**c)
    ct.save()



