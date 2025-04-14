from flask import redirect, request, flash, url_for
import flask
from werkzeug.security import check_password_hash, generate_password_hash
from AppRoot import app
from sqlalchemy import exc
from AppRoot.Login import models
from AppRoot import database
from AppRoot.Utils import limits

def login():
    #login logic here
    username = request.form.get('username')
    password = request.form.get('password')
    
    #maybe we should sanitize the input to protect from XSS-Attacks
    #But it seems the ORM itself takes care of the sanitizing, but im not sure yet!!!
    if limits.checkLen(username,limits.USERNAME_LEN) \
            and limits.checkLen(password,limits.PASSWORD_LEN):
        userDb = models.User.query.filter_by(username=username).first()
        if userDb:
            if check_password_hash(userDb.password,password):
                flask.session['id'] = userDb.uid #here we store a encrypted session cookie
                flask.session['username'] = username           
                flask.flash("user " + username +  " logged in")
            else:
                flask.flash("user " + username + "not logged in")
        else:
            flask.flash("user " + username + "not logged in")
    else:
        flash("Exceding lenght in Login-credentials")
    return redirect("/")

def signUp():
    username = request.form.get('username')
    password = request.form.get('password')
    repeatPassword = request.form.get('repeatPassword')

    if limits.checkLen(username,limits.USERNAME_LEN) \
            and limits.checkLen(password,limits.PASSWORD_LEN) \
            and limits.checkLen(repeatPassword,limits.PASSWORD_LEN):
        user = models.User.query.filter_by(username=username).first()
        if user:
           flash("this username is already taken")
           return redirect(url_for('login_bp.signUpPage'))
        else:
            if password == repeatPassword and len(password) > 10:
                newUser = models.User(username=username, \
                                      password=generate_password_hash(password,method="scrypt"),_type="Guest")
                with app.app.app_context():
                    database.db.session.add(newUser)
                    try:
                        database.db.session.commit()
                    except exc.IntegrityError as e:
                        app.logger.info("User already exist in db:"+ str(e))
                        flash("Error adding user!, please contact your sysadmin")
                        database.db.session.rollback()
                    else:
                        flash("User successfull added")
            else:
               flash("password is invalid")
               return redirect(url_for('login_bp.signUpPage'))
    else:
        flash("Exceding lenght in Login-credentials")
    return redirect("/login")
