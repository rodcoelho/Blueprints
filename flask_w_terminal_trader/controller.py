#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def homepage():
    if request.method == 'GET':
        title = 'Terminal Trader'
        return render_template('index.html',title=title)
    else:
        submitted_username = request.form['username']
        submitted_password = request.form['password']
        if submitted_username:
            if submitted_password:
                if submitted_username == 'rod':
                    if submitted_password == 'swordfish':
                        return redirect(url_for('dashboardpage'))

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