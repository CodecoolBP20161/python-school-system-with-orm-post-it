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
          {'city_name': 'Boldog', 'closest_school_id': 1},
          {'city_name': 'Salgotarjan', 'closest_school_id': 2},
          {'city_name': 'Gyor', 'closest_school_id': 1},
          {'city_name': 'Sopron', 'closest_school_id': 1},
          {'city_name': 'Budapest', 'closest_school_id': 1},
          {'city_name': 'Eger', 'closest_school_id': 2},
          {'city_name': 'Vac', 'closest_school_id': 1},
          {'city_name': 'Debrecen', 'closest_school_id': 2},
          {'city_name': 'Hatvan', 'closest_school_id': 1},
          {'city_name': 'Krakko', 'closest_school_id': 3},
          {'city_name': 'Warsaw', 'closest_school_id': 3}
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
               'application_time': datetime.date(1991, 2, 12)
               },
              {'first_name': "Tom",
               'last_name': "Araya",
               'hometown': "Debrecen",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1978, 2, 21)
               },
              {'first_name': "Korda",
               'last_name': "Gyorgy",
               'hometown': "Vac",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 2, 1)
               },
              {'first_name': "Bernd",
               'last_name': "Storck",
               'hometown': "Eger",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1967, 4, 14)
               },
              {'first_name': "David",
               'last_name': "Beckham",
               'hometown': "Salgotarjan",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 12, 1)
               },
              {'first_name': "Steven",
               'last_name': "Gerrard",
               'hometown': "Debrecen",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1975, 1, 21)
               },
              {'first_name': "John",
               'last_name': "Lennon",
               'hometown': "Boldog",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 1, 11)
               },
              {'first_name': "Kenny",
               'last_name': "Dalglish",
               'hometown': "Gyor",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1944, 9, 1)
               },
              {'first_name': "Method",
               'last_name': "Man",
               'hometown': "Sopron",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1998, 2, 1)
               },
              {'first_name': "Miles",
               'last_name': "Davis",
               'hometown': "Gyor",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1980, 6, 15)
               },
              {'first_name': "Santa",
               'last_name': "Claus",
               'hometown': "Pecs",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1945, 12, 6)
               },
              {'first_name': "John",
               'last_name': "Coltrane",
               'hometown': "Eger",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1966, 2, 21)
               },
              {'first_name': "Zinedine",
               'last_name': "Zidane",
               'hometown': "Krakko",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1988, 1, 1)
               },
              {'first_name': "Csanyi",
               'last_name': "Sandor",
               'hometown': "Hatvan",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1955, 12, 10)
               },
              {'first_name': "Frederic",
               'last_name': "Chopin",
               'hometown': "Warsaw",
               'application_code': None,
               'status': 'new',
               'closest_school_id': None,
               'application_time': datetime.date(1976, 12, 1)
               }
              ]

for applicant in applicants:
    a = Applicant(**applicant)
    a.save()


mentors = [{'first_name' : 'Tamas',
            'last_name': 'Tompa',
            'school' : '1'},
           {'first_name': 'Miklos',
            'last_name': 'Beothy',
            'school': '1'},
           {'first_name': 'Daniel',
            'last_name': 'Salamon',
            'school': '1'},
           {'first_name': 'Miskolci',
            'last_name': 'Mentor',
            'school': '2'},
           {'first_name': 'Miskolci2',
            'last_name': 'Mentor2',
            'school': '2'},
           {'first_name': 'Miskolci3',
            'last_name': 'Mentor3',
            'school': '2'},
           {'first_name': 'Robert',
            'last_name': 'Lewandowsky',
            'school': '3'},
           {'first_name': 'Lukas',
            'last_name': 'Podolski',
            'school': '3'}
           ]

for mentor in mentors:
    m = Mentor(**mentor)
    m.save()

slots = [{'slot': datetime.datetime(2016, 8, 22, 13),
          'mentor': 1,
          'availability': True},
         {'slot': datetime.datetime(2016, 8, 22, 10),
          'mentor': 1,
          'availability': True},
         {'slot': datetime.datetime(2016, 8, 22, 11),
           'mentor': 1,
           'availability': True},
         {'slot': datetime.datetime(2016, 8, 22, 12),
            'mentor': 1,
            'availability': True},
         {'slot': datetime.datetime(2016, 8, 22, 15),
             'mentor': 1,
             'availability': True},
         {'slot': datetime.datetime(2016, 8, 22, 9),
              'mentor': 1,
              'availability': True},

             {'slot': datetime.datetime(2016, 8, 24, 10),
              'mentor': 1,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 24, 11),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 22, 13),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 22, 12),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 22, 14),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 13),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 14),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 9),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 11),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 12),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 15),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 16),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 8),
              'mentor': 2,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 22, 13),
              'mentor': 3,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 22, 14),
              'mentor': 3,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 13),
              'mentor': 3,
              'availability': True},
             {'slot': datetime.datetime(2016, 8, 23, 13),
              'mentor': 3,
              'availability': True}
             {'slot': datetime.datetime(2016, 8, 22, 10),
              'mentor': 2,
              'availability': True}
             {'slot': datetime.datetime(2016, 8, 22, 15),
              'mentor': 2,
              'availability': True}
             {'slot': datetime.datetime(2016, 8, 22, 9),
              'mentor': 2,
              'availability': True}
             {'slot': datetime.datetime(2016, 8, 24, 12),
              'mentor': 2,
              'availability': True}
             ]

    for slot in slots:
        s = InterviewSlot(**slot)
        s.save()


for slot in slots:
    s = InterviewSlot(**slot)
    s.save()

Applicant.assign_app_code()
# Applicant.school_to_applicant()
# Applicant.find_applicant_without_interview()
