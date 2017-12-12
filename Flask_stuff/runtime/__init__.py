#!/usr/bin/env python3

import os
import sys

from flask import Flask, render_template


forest = Flask(__name__)

def keymaker(forest,filename='secret_key'):
    filename=os.path.join(forest.instance_path,filename)
    try:
        forest.config['SECRET_KEY']=open(filename,"rb").read()
    except IOError:
        # print("\nHey! You don't have secret key! Run these commands to make one!\n")
        full_path=os.path.dirname(filename)
        if not os.path.isdir(full_path):
            os.system("mkdir -p {filename}".format(filename=full_path))
        os.system('head -c 24 /dev/urandom > {filename}\n'.format(filename=filename))
        sys.exit(1)

keymaker(forest)

@forest.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from runtime.app.books import tree1 as tree1_blueprint
forest.register_blueprint(tree1_blueprint)
# from runtime.app.electronics import tree2 as tree2_blueprint
# forest.register_blueprint(tree2_blueprint)