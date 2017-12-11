# Flask basics
    # need templates dir for CSS and JS files
    # need static dir for HTML
# also need the following imports

from flask import Flask, render_template, request
import sqlite3

print("Starting application...")

# anything that is in this file (__name__) run it in Flask
api = Flask(__name__)

connection  = sqlite3.connect('master.db', check_same_thread= False)
cursor      = connection.cursor()


# @api - is the decorator - allows us to call functions from Flask object
# here we are creating 'pages' on our website

# home page
@api.route('/', methods = ["GET"])
def show_home():
    return render_template('view_structure.html')

# login/authenticate page
@api.route('/authenticate',methods = ["POST"])
def authenticate():
    submitted_username = request.form['username']
    submitted_password = request.form['password']
    cursor.execute("SELECT username FROM users WHERE username = '{}';".format(submitted_username))
    stored_username = cursor.fetchall()
    cursor.execute("SELECT password FROM users WHERE username = '{}';".format(submitted_username))
    stored_password = cursor.fetchall()
    if len(stored_username) > 0:
        if len(stored_password) > 0:
            if submitted_username == stored_username[0][0]:
                if submitted_password == stored_password[0][0]:
                    print('Log: Access: User {} has logged into their account'.format(submitted_username))
                    return render_template('view_dashboard.html', username=submitted_username)
                else:
                    error_message = 'Wrong username/password submission'
                    return render_template('view_structure.html', message = error_message)
            else:
                error_message = 'Error'
                return render_template('view_structure.html', message = error_message)
        else:
            error_message = 'Error'
            return render_template('view_structure.html', message=error_message)
    else:
        error_message = 'Error'
        return render_template('view_structure.html', message=error_message)

if __name__ == '__main__':
    api.run(host='127.0.0.1', port = 5000, debug = True)