from flask import Blueprint
from flask import render_template
import flask
order_bp = Blueprint('order_bp',
                    __name__,
                    template_folder="templates",
                    static_folder="static")

@order_bp.route('/')
def order():
    if 'username' in flask.session:
        return render_template("IndexOrders.html", username=flask.session['username'])
    else:
        return render_template("IndexOrders.html")
