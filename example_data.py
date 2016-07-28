# This script can generate example data for "City" and "InterviewSlot" models.
import datetime
from models import *

schools = [{'school_name': 'CC Budapest'},
           {'school_name': 'CC Miskolc'},
           {'school_name': 'CC Krakow'}]

for school in schools:
    s = School(**school)
    s.save()


cities = [{'city_name': 'Pecs', 'closest_school_id': 1},
          {'city_name': 'Debrecen', 'closest_school_id': 2},
          {'city_name': 'Miskolc', 'closest_school_id': 2}
          ]

for city in cities:
    c = City(**city)
    c.save()


applicants = [{'first_name': "Levente",
               'last_name': "Csanyi",
               'hometown': "Pecs",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 12, 1)
               },
              {'first_name': "Lvnt",
               'last_name': "Cny",
               'hometown': "Debrecen",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1928, 12, 1)
               }
              ]

for applicant in applicants:
    a = Applicant(**applicant)
    a.save()
