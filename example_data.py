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


cities = [{'city_name': 'Pecs', 'closest_school_id': 1},
          {'city_name': 'Debrecen', 'closest_school_id': 2}
          ]

for city in cities:
    c = City(**city)
    c.save()



applicants = [{'first_name': "Levente",
               'last_name': "Csanyi",
               'hometown': "Pecs",
               'application_code': generator(),
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 12, 1)
               },
              {'first_name': "Lvnt",
               'last_name': "Cny",
               'hometown': "Debrecen",
               'application_code': generator(),
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1928, 12, 1)
               }
              ]

for applicant in applicants:
    a = Applicant(**applicant)
    a.closest_school_id = a.get_closest_school_id()
    a.save()

