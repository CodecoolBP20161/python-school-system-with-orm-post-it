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
        Applicant.create(first_name = request.form["frist_name"], last_name= request.form["last_name"], hometown= request.form["hometown"], application_code= request.form["application_code"],
                            status= "In Progress", application_time = datetime.now())
        return redirect(url_for('homepage'))
    else:
        render_template('application_form.html')




if __name__ == '__main__':
    #create_tables()
    app.run(debug=True)
