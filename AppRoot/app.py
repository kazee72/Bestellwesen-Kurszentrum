import sys
from dotenv import dotenv_values, load_dotenv

from flask import Flask
from flask_migrate import Migrate

from AppRoot.Home.routes import home_bp
from AppRoot.Dashboard.routes import dashboard_bp
from AppRoot.Login.routes import login_bp

from . import database
from .Login import models

import logging
logging.basicConfig(stream=sys.stdout,level=logging.INFO)
logger = logging.getLogger(__name__)

config = dotenv_values(".env")

app = Flask("bööö")

try:
    app.secret_key = config["FLASK_SECRET_KEY"]
except Exception as e:
    raise ValueError("FLASK_SECRET_KEY is not defined in the .env",e)  

app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{app.root_path}/db.sqlite'
database.db.init_app(app)

migrate = Migrate(app,database.db)

app.register_blueprint(home_bp,url_prefix='/',name="home-red")
app.register_blueprint(home_bp,url_prefix='/home')
app.register_blueprint(login_bp,url_prefix="/login")
app.register_blueprint(dashboard_bp,url_prefix='/dashboard')

if __name__ == '__main__':
    app.run(debug=True)

