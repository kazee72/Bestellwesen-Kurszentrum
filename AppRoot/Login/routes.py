from flask import Blueprint
from flask import render_template

login_bp = Blueprint('login_bp',
                     __name__,
                     template_folder="templates",
                     static_folder="static")

@login_bp.route("/")
def login():
    return render_template("LoginPage.html")
