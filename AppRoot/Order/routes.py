import flask
from AppRoot.Order import models
from AppRoot.app import logger

order_bp = flask.Blueprint("order_bp",
                           __name__,
                           template_folder="templates",
                           static_folder="static")

@order_bp.route("/",methods=["GET"])
def index():
    return flask.render_template("IndexOrders.html")

@order_bp.route("/addOrder",methods=["GET","POST"])
def addOrder():
    try:
        itemList = models.ItemStore.query.all()
    except Exception as e:
        logger.error("Eerror at db call for itemstore:\n",e)
    return flask.render_template(template_name_or_list="AddOrder.html",items=itemList)
