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


mentors = [{'first_name' : 'Tamas',
            'last_name': 'Tompa',
            'school' : '1'}]

for mentor in mentors:
    m = Mentor(**mentor)
    m.save()

slots = [{'interview_id': None,
          'slot': datetime.datetime(2016, 8, 22, 13),
          'available_mentor': 1},
         {'interview_id': None,
          'slot': datetime.datetime(2016, 8, 25, 17),
          'available_mentor': 1},
         {'interview_id': None,
          'slot': datetime.datetime(2016, 8, 21, 13),
          'available_mentor': 1},
         {'interview_id': None,
          'slot': datetime.datetime(2016, 8, 29, 13),
          'available_mentor': 1}
         ]

for slot in slots:
    s = Interview(**slot)
    s.save()

Applicant.assign_app_code()
Applicant.school_to_applicant()
Interview.find_applicant_without_interview()