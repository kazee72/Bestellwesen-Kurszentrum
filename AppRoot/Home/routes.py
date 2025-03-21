from flask import Blueprint
from flask import render_template
import flask
home_bp = Blueprint('home_bp',
                    __name__,
                    template_folder="templates",
                    static_folder="static")

@home_bp.route('/')
def home():
    if 'username' in flask.session:
        return render_template("frontpage.html",username=flask.session['username'])
    else:
        return render_template("frontpage.html")
