from flask import Flask
from models import *

app = Flask(__name__)
db.connect()

@app.route('/')
def starting_page():
    q = Applicant.select(Applicant.first_name).get()
    return q.first_name





if __name__ == '__main__':
    #create_tables()
    app.run(debug=True)




