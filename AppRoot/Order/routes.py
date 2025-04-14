import flask
from AppRoot.Order import models
from AppRoot.app import logger
from flask import render_template, Blueprint

order_bp = flask.Blueprint("order_bp",
                           __name__,
                           template_folder="templates",
                           static_folder="static")

@order_bp.route('/')
def order():
    if 'username' in flask.session:
        return render_template("IndexOrders.html", username=flask.session['username'])
    else:
        return render_template("IndexOrders.html")

@order_bp.route("/addOrder",methods=["GET","POST"])
def addOrder():
#check User login rights
    itemlist = []
    try:
        itemList = models.ItemStore.query.all()
    except Exception as e:
        logger.error("Eerror at db call for itemstore:\n",e)
    return flask.render_template(template_name_or_list="AddOrder.html",items=itemList)
