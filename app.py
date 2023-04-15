'''
    This is an application to show off Bootstrap 5 forms and create a template
    that can be reused for some of my applications.
'''

from flask import Flask, render_template, request
# from flask_recaptcha import ReCaptcha
# import cred
import hashlib
from database import get_db
import os

app = Flask(__name__)

# some app setup
app.config['SECRET_KEY'] = os.urandom(24)
# if using ReCaptcha (google) use this code.
# app.config['RECAPTCHA_SITE_KEY'] = cred.recaptcha_site_key
# app.config['RECAPTCHA_SECRET_KEY'] = cred.recaptcha_secret_key


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    output = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        output = f"your email is {email} and your password is {password}"

    return render_template('login.html', output=output)

@app.route('/login2', methods=['GET','POST'])
def login2():
    output = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        output = f"your email is {email} and your password is {password}"

    return render_template('login2.html', output=output)

@app.route('/login3', methods=['GET','POST'])
def login3():
    output = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        output = f"your email is {email} and your password is {password}"

    return render_template('login3.html', output=output)

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/blocktest')
def blocktest():
    return render_template('blocktest.html')

@app.route('/dform')
def dform():
    return render_template('dform.html')

@app.route('/bform')
def bform():
    return render_template('bform.html')

@app.route('/cform')
def cform():
    return render_template('cform.html')

@app.route('/fform')
def fform():
    return render_template('fform.html')

@app.route('/fform2')
def fform2():
    return render_template('fform2.html')

@app.route('/fform3')
def fform3():
    return render_template('fform3.html')

@app.route('/eform')
def eform():
    return render_template('eform.html')

@app.route('/formcheck')
def formcheck():
    return render_template('formcheck.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
