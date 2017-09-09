from flask import Flask, render_template, request, redirect, session, flash
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d') #searches for a upper case followed by a number and the |(or operator) looks for a number then a upper case
NAME_REGEX = re.compile(r'\W.*[A-Za-z]|[A-Za-z]\.*\W|\d.*[A-Za-z]|[A-Za-z].*\d')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    count = 0
    present = datetime.now()
    # present = datetime.datetime(present.year, present.month, present.day)
    if len(request.form['email']) < 1:
        flash("Email is blank!", "email")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "email")
    else:
        count += 1
    if len(request.form['birthday']) < 1:
        flash("Birthday is blank!", "birthday")
    elif request.form['birthday'] == present:
        print str(request.form['birthday'])
        print present
    # elif request.form['birthday'] < present:
    #     flash("The date must be before today's date!")

    if len(request.form['first_name']) <1:
        flash("First name is blank!", "first_name")
    elif NAME_REGEX.search(request.form['first_name']):
        flash("Invalid First Name!", "first_name")
    else:
        count += 1
    if len(request.form['last_name']) <1:
        flash("Last name is blank!", "last_name")
    elif NAME_REGEX.search(request.form['last_name']):
        flash("Invalid Last Name!", "last_name")
    else:
        count += 1
    if len(request.form['password']) <1:
        flash("Password is blank!", "password")
    elif len(request.form['password']) > 0 and len(request.form['password']) < 9:
        flash("Password is shorter than 8 characters!", "password")
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Password needs at least 1 Upper case and 1 number", "password")
    else:
        count += 1
    if len(request.form['confirm_password']) <1:
        flash("Password Confirmation is blank!", "confirm_password")
    elif request.form['confirm_password'] != request.form['password']:
        flash("Password and confirmation password do not match!", "pw_match")
    else:
        count += 1

    if count == 5:
        flash("Thanks for submitting your information.")
    return redirect('/')

app.run(debug=True)