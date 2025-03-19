#here We define the structure of the infos in the userDb using sqlitealchemy
from ..database import db as userDb

class User(userDb.Model):
    uid = userDb.Column(userDb.Integer,primary_key=True)
    email = userDb.Column(userDb.String(100))
    password = userDb.Column(userDb.String(100))
    username = userDb.Column(userDb.String(100),unique=True)
    firstname = userDb.Column(userDb.String(100))
    lastname = userDb.Column(userDb.String(100))
