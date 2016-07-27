# This script can generate example data for "City" and "InterviewSlot" models.
import random
import datetime
from models import *


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
    'application_code': 'SCRD4',
    'status': 'new',
    'application_time': datetime.date(1988, 12, 1)},
    {
        'first_name': "Lvnt",
        'last_name': "Cny",
        'application_code': random.randint(0,4555),
        'status': 'new',
        'application_time': datetime.date(1928, 12, 1)}
]

for applicant in applicants:
    a = Applicant(**applicant)
    a.save()
#
# cities = [{'':}]

