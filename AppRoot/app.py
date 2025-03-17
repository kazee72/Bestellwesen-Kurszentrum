from flask import Flask
from Home.routes import home_bp
from Dashboard.routes import dashboard_bp
from Login.routes import login_bp
from flask 

app = Flask("bööö")

app.register_blueprint(home_bp,url_prefix='/',name="home-red")
app.register_blueprint(home_bp,url_prefix='/home')
app.register_blueprint(login_bp,url_prefix="/login")
app.register_blueprint(dashboard_bp,url_prefix='/dashboard')

db = SQLAl

if __name__ == '__main__':
    app.run(debug=True)
