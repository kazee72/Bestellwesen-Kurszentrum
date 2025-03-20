from flask import redirect, request, flash, url_for
from werkzeug.security import generate_password_hash
from AppRoot import app
from sqlalchemy import exc
from AppRoot.Login import models
from AppRoot import database

def login():
    #login logic here
    return "here is login logic"

def signUp():
    username = request.form.get('username')
    password = request.form.get('password')
    repeatPassword = request.form.get('repeatPassword')

    user = models.User.query.filter_by(username=username).first()
    if user:
       flash("this username is already taken")
       return redirect(url_for('login_bp.signUpPage'))
    else:
        if password == repeatPassword and len(password) > 10:
            newUser = models.User(username=username,
                                  password=generate_password_hash(password,method="scrypt"))
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

        return "some response"
