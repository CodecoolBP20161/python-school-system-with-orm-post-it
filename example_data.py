# This script can generate example data for "City" and "InterviewSlot" models.
import datetime
from models import *
from application_code import generator


schools = [{'school_name': 'CC Budapest'},
           {'school_name': 'CC Miskolc'},
           {'school_name': 'CC Krakow'}]

for school in schools:
    s = School(**school)
    s.save()

applicants = [{'first_name': "Levente",
               'last_name': "Csanyi",
               'hometown': "Pecs",
               'application_code': generator(),
               'status': 'new',
               'closest_school_id': 1,
               'application_time': datetime.date(1988, 12, 1)
               },
              {'first_name': "Lvnt",
               'last_name': "Cny",
               'hometown': "Pecs",
               'application_code': generator(),
               'status': 'new',
               'closest_school_id': 1,
               'application_time': datetime.date(1928, 12, 1)
               }
              ]

for applicant in applicants:
    a = Applicant(**applicant)
    a.save()

cities = [{'city_name': 'Budapest', 'closest_school_id': 1}]

for city in cities:
    c = City(**city)
    c.save()
