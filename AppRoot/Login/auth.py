from flask import redirect, request, flash, url_for
from werkzeug.security import generate_password_hash
#from ..app import app
#from ..app import logger
#from ..app import db
from .. import app
from sqlalchemy import exc
from . import models

def login():
    #login logic here
    return "here is login logic"

def signUp():
    #signUp logic here

    username = request.form.get('username')
    password = request.form.get('password')
    repeatPassword = request.form.get('repeatPassword')

    user = models.User.query.filter_by(username=username).first()
    if user:
       flash("this username is already taken")
       return redirect(url_for('auth.login'))
    else:
        if password == repeatPassword and len(password) > 10:
            newUser = models.User(username=username,
                                  password=generate_password_hash(password,method="sha256"))
            with app.context():
                db.session.add(newUser)
                try:
                    db.session.commit()
                except exc.IntegrityError as e:
                    logger.info("User already exist in db:"+ str(e))
                    flash("Error adding user!, please contact your sysadmin")
                    db.session.rollback()
                else:
                    flash("User successfull added")
        else:
           flash("password is invalid")
           return redirect(url_for('auth.login'))

        return "some response"
