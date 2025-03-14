from flask import Blueprint

home_bp = Blueprint('home_b',
                    __name__,
                    template_folder="templates",
                    static_folder="static")

@home_bp.route('/')
def home():
    return "home page hello"
