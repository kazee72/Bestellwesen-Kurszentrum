from flask import Blueprint, request, redirect, url_for
from flask import render_template
import flask
from AppRoot.Login import auth

login_bp = Blueprint('login_bp',
                     __name__,
                     template_folder="templates",
                     static_folder="static")

@login_bp.route("/",methods=['GET','POST'])
def loginPage():
    if request.method == 'POST':
        return auth.login()
    elif request.method == 'GET':
        if 'username' in flask.session:
            return render_template("LoginPage.html",
                               username=flask.session['username'])
        else:
            return render_template("LoginPage.html")

@login_bp.route("/signUp",methods = ['POST','GET']) #remove the get here!!!
def signUpPage():
    if request.method == 'POST':
        return auth.signUp()
    if request.method == 'GET':
        return render_template("SignUpPage.html")

@login_bp.route("/logout",methods=['GET'])
def logout():
    flask.session.clear()
    flask.flash("User logged out")
    return redirect("/")
