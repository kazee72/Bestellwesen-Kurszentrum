from flask import Blueprint, request
from flask import render_template

login_bp = Blueprint('login_bp',
                     __name__,
                     template_folder="templates",
                     static_folder="static")

@login_bp.route("/",methods=['GET','POST'])
def loginPage():
    if request.method == 'POST':
        #user login logic goes here
        pass
    elif request.method == 'GET':
        return render_template("LoginPage.html")

@login_bp.route("/signUp",methods = ['POST'])
def signUpPage():
    if request.method == 'POST':
        #user creation logic here

        pass

    return render_template("SignUpPage.html")
