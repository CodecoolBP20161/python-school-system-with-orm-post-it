from models import *
import build
import example_data
from app import  *

app.run()
db.connect()

# # for testing purposes drop and recreate the database
# build.start_over_database()

# # fill database with example data
# example_data.fill_all_ex()

# Applicant.assign_app_code()
# Applicant.assign_school()
# Applicant.assign_interview()
