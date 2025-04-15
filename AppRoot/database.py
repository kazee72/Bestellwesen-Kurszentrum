from flask_sqlalchemy import SQLAlchemy
from AppRoot.Login import models

def initDb():
    db = SQLAlchemy()
    return db
db = initDb()

