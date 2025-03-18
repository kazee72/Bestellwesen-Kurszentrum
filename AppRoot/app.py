import sys
from flask import Flask
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

app.register_blueprint(home_bp,url_prefix='/',name="home-red")
app.register_blueprint(home_bp,url_prefix='/home')
app.register_blueprint(login_bp,url_prefix="/login")
app.register_blueprint(dashboard_bp,url_prefix='/dashboard')

if __name__ == '__main__':
    app.run(debug=True)




