from flask import Blueprint

dashboard_bp = Blueprint('dashboard_bp',
                         __name__,
                         template_folder="templates",
                         static_folder="static")

@dashboard_bp.route('/')
def main_dashboard():
    return "here will be the dashboard"
