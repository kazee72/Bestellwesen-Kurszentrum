from flask import Blueprint, render_template
import flask

dashboard_bp = Blueprint('dashboard_bp',
                         __name__,
                         template_folder="templates",
                         static_folder="static")

@dashboard_bp.route('/')
def main_dashboard():
    if 'username' in flask.session:
        return render_template('dashboard_main.html', username=flask.session['username'])
    else:
        return render_template('dashboard_main.html')
