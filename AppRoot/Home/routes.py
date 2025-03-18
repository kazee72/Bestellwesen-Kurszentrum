from flask import Blueprint
from flask import render_template

home_bp = Blueprint('home_b',
                    __name__,
                    template_folder="templates",
                    static_folder="static")

@home_bp.route('/')
def home():
    return render_template("frontpage.html")
