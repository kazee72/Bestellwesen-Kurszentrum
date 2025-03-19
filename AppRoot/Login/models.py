#here We define the structure of the infos in the db using sqlitealchemy
from ..app import db
class User(db.Model):
    uid = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    prename = db.Column(db.String(100))
