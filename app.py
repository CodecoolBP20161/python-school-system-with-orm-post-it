from flask import *
from models import *
from datetime import *



app = Flask(__name__)
app.secret_key = 'nfNWEOFKWEFMEFKm'
db.connect()


@app.route('/')
def main_page():
    # return redirect(url_for('list_applicants'))
    return render_template('home_page.html')


@app.route('/applicant/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_page.html')
    try:
        login_applicant = Applicant.get(Applicant.email == request.form["username"])

        if login_applicant:
            if request.form["application_code"] == login_applicant.application_code:
                session['username'] = request.form['application_code']
                return redirect(url_for('list_applicants'))

            else:
                return "Invalid username/password combination"
    except:
        return "Wrong e-mail address, please sign up!"


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        new_applicant = Applicant.create(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            hometown=request.form["hometown"],
            email=request.form["email"],
            status="In Progress",
            application_time=datetime.now()
        )
        # flash("Registration Successful!")
        new_applicant.save()
        Applicant.assign_app_code()
        Applicant.assign_school()
        return render_template('supriseboda.html')
    return render_template('application_form.html')

# @app.route('/successful/')
# def suprise_boda():
#     return render_template('supriseboda.html')






@app.route('/list/', methods=['POST', 'GET'])
def list_applicants():
    if request.method == 'GET':
        applicants = Applicant.select()
        return render_template('list.html', applicants=applicants)
    if request.form["filter_option"] == 'closest_school':
        x = Applicant.select().join(School).where(request.form["search_string"] == School.school_name).execute()
        return render_template('list.html', applicants=x)
    filtered_applicants = Applicant.select().\
        where(getattr(Applicant, request.form["filter_option"]) == request.form["search_string"]).execute()
    return render_template('list.html', applicants=filtered_applicants)


@app.before_request
def before_req():
    db.connect()


@app.after_request
def close_db(respond):
    db.close()
    return respond

if __name__ == '__main__':
    # create_tables()
    app.run(debug=True)
