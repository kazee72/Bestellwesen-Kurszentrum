from flask import Flask
from Home.routes import home_bp

app = Flask("bööö")

app.register_blueprint(home_bp,url_prefix='/',name="home2")
app.register_blueprint(home_bp,url_prefix='/home')

if __name__ == '__main__':
    app.run(debug=True)
