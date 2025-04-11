from flask import Blueprint, request, redirect, url_for
from flask import render_template
import flask
from AppRoot.Login import auth

signup_bp = Blueprint('signup_bp',
                     __name__,
                     template_folder="templates",
                     static_folder="static")



@signup_bp.route("/",methods = ['POST','GET'])
def signUpPage():
    if request.method == 'POST':
        return auth.signUp()
    if request.method == 'GET':
        return render_template("signup.html")


