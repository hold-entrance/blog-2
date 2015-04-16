# blog.py - controller


# imports
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import redirect
from flask import url_for
from flask import g
import sqlite3

# configuration 
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in app configuration by looking up UPPERCASE variables
app.config.from_object(__name__)

# function used for connection to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
		request.form['password'] != app.config['PASSWORD']:
            error = 'INVALID CREDENTIALS. Please try again.'
        else:
            session['logged in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))
	
@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
