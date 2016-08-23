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


applicants = [{'first_name': "Jimi",
               'last_name': "Hendrix",
               'hometown': "Pecs",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 12, 1)
               },
              {'first_name': "Tom",
               'last_name': "Araya",
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
            'school' : '1'},
           {'first_name': 'Miskolci',
            'last_name': 'Mentor',
            'school': '2'},
           {'first_name': 'Miskolci',
            'last_name': 'Mentor',
            'school': '2'},
           {'first_name': 'Miskolci',
            'last_name': 'Mentor',
            'school': '2'},
           {'first_name': 'Miskolci',
            'last_name': 'Mentor',
            'school': '2'}
           ]

for mentor in mentors:
    m = Mentor(**mentor)
    m.save()

slots = [{'slot': datetime.datetime(2016, 8, 22, 13),
          'mentor': 1,
          'availability': True},
         {'slot': datetime.datetime(2016, 8, 22, 13),
          'mentor': 1,
          'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
           'mentor': 1,
           'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
            'mentor': 1,
            'availability': True}, {'slot': datetime.datetime(2016, 8, 22, 13),
             'mentor': 1,
             'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
              'mentor': 1,
              'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
               'mentor': 1,
               'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                'mentor': 1,
                'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                 'mentor': 1,
                 'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                  'mentor': 1,
                  'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                   'mentor': 1,
                   'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                    'mentor': 1,
                    'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                     'mentor': 1,
                     'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                      'mentor': 1,
                      'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                       'mentor': 1,
                       'availability': True},{'slot': datetime.datetime(2016, 8, 22, 13),
                        'mentor': 1,
                        'availability': True}
         ]

for slot in slots:
    s = InterviewSlot(**slot)
    s.save()

Applicant.assign_app_code()
# Applicant.school_to_applicant()
# Applicant.find_applicant_without_interview()
