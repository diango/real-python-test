from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g

import sqlite3

# Configuration
DATABASE = 'blog.py'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'rM\xb1\xdc\x12o\xd6i\xff+9$T\x8e\xec\x00\x13\x82.*\x16TG\xbd'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variable
app.config.from_object(__name__)

# function used to connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route("/", methods = ['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again!!'
            status_code = 401
        else:
            session['loged_in'] = True
            return redirect(url_for('main'))
    
    return render_template('login.html', error = error), status_code

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    flash('You were logged out!')
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
