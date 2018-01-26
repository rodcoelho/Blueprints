#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, request, url_for, redirect
import orm
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def homepage():
    if request.method == 'GET':
        title = 'Terminal Trader'
        return render_template('index.html', title=title)
    else:
        submitted_username = request.form['username']
        submitted_password = request.form['password']
        fetch = orm.check_username_password(submitted_username, submitted_password)
        if fetch == "ERROR":
            redirect(url_for('homepage'))
        else:
            username_from_db, password_from_db, balance = fetch[0][0], fetch[0][1], fetch[0][2]
            if balance is not False:
                if submitted_username == username_from_db:
                    if submitted_password == password_from_db:
                        return redirect(url_for('dashboardpage'))
                    else:
                        redirect(url_for('homepage'))

@app.route('/dashboard',methods=["GET"])
def dashboardpage():
    title = 'Dashboard'
    return render_template('dashboard.html',title=title)

@app.route('/account',methods = ["GET", "POST"])
def accountpage():
    title = 'Accounts Page'
    return render_template('accounts.html',title=title)

if __name__ == '__main__':
    app.run(debug=True)