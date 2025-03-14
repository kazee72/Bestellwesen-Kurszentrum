from flask import Flask
from Home.routes import home_bp
from Dashboard.routes import dashboard_bp

app = Flask("bööö")

app.register_blueprint(home_bp,url_prefix='/',name="home-red")
app.register_blueprint(home_bp,url_prefix='/home')

app.register_blueprint(dashboard_bp,url_prefix='/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
