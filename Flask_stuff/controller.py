# Flask basics
    # need templates dir for CSS and JS files
    # need static dir for HTML
# also need the following:
from flask import Flask, render_template
# anything that is in this file (__name__) run it in Flask
api = Flask(__name__)



# @api - is the decorator - allows us to call functions from Flask object
@api.route('/', methods = ["GET"])

def show_home():
    return render_template('view_structure.html')

if __name__ == '__main__':
    api.run(host='127.0.0.1', port = 5000, debug = True)