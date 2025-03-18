import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_migrate import Migrate

from .Home.routes import home_bp
from .Dashboard.routes import dashboard_bp
from .Login.routes import login_bp

import logging
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask("bööö")
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{app.root_path}/db.sqlite'

from . import database
db = database.initDb(app)
from .Login import models

migrate = Migrate(app,db)

def testAdduser():
    with app.app_context():
        email = "dooner@dooner.ch"
        name = "testAdduser"
        prename = "sdfa"
        pw = "anothersafepassword"
        user = models.User(email=email,name=name,prename=prename,password=pw)
        db.session.add(user)
        try:
            db.session.commit()
        except exc.IntegrityError as e:
            logger.info("User already exist in db:"+ str(e))
            db.session.rollback()

app.register_blueprint(home_bp,url_prefix='/',name="home-red")
app.register_blueprint(home_bp,url_prefix='/home')
app.register_blueprint(login_bp,url_prefix="/login")
app.register_blueprint(dashboard_bp,url_prefix='/dashboard')

testAdduser()
if __name__ == '__main__':
    app.run(debug=True)




