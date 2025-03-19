from flask_sqlalchemy import SQLAlchemy

def initDb(app):
    db = SQLAlchemy(app)
    return db


