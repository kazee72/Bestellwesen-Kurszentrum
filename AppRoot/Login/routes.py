from flask import Blueprint, request, redirect, url_for
from flask import render_template
from . import auth

login_bp = Blueprint('login_bp',
                     __name__,
                     template_folder="templates",
                     static_folder="static")

@login_bp.route("/",methods=['GET','POST'])
def loginPage():
    if request.method == 'POST':
        return auth.login()
    elif request.method == 'GET':
        return render_template("LoginPage.html")

@login_bp.route("/signUp",methods = ['POST'])
def signUpPage():
    if request.method == 'POST':
        return redirect(url_for("auth.signUp"))
    return render_template("SignUpPage.html")
