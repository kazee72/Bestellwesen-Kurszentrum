from flask_sqlalchemy import SQLAlchemy

def initDb():
    db = SQLAlchemy()
    return db
db = initDb()

