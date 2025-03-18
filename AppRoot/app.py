from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .Home.routes import home_bp
from .Dashboard.routes import dashboard_bp
from .Login.routes import login_bp



app = Flask("bööö")

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite://db.sqlite'

from . import database
db = database.initDb(app)
from .Login import models

def testAdduser():
    email = "dooner@dooner.ch"
    name = "testAdduser"
    pw = "anothersafepassword"
    models.User(email=email,name=name,password=pw)

app.register_blueprint(home_bp,url_prefix='/',name="home-red")
app.register_blueprint(home_bp,url_prefix='/home')
app.register_blueprint(login_bp,url_prefix="/login")
app.register_blueprint(dashboard_bp,url_prefix='/dashboard')

testAdduser()
if __name__ == '__main__':
    app.run(debug=True)




