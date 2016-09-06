from flask import *
from models import *
from datetime import *


app = Flask(__name__)
db.connect()


@app.route('/')
def main_page():
    return render_template('home_page.html')


# @app.route('/applicants')
# def app_list():
#     applicants = Applicant.select()
#     return render_template('VALAMI.HTML', applicants=applicants)

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        new_applicant = Applicant.create(first_name = request.form["first_name"], last_name= request.form["last_name"], hometown= request.form["hometown"],
                            status= ["In Progress"], application_time = datetime.now())
        #flash("Registration Successful!")
        new_applicant.save()
        Applicant.assign_app_code()
        Applicant.assign_school()
        return redirect(url_for('suprise_boda'))
    else:
        return render_template('application_form.html')

@app.route('/successful')
def suprise_boda():
    return render_template('supriseboda.html')


if __name__ == '__main__':
    #create_tables()
    app.run(debug=True)
