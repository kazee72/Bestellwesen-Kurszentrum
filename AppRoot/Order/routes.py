import flask
from AppRoot.Order import models
from AppRoot.app import logger
from AppRoot.Login import auth

order_bp = flask.Blueprint("order_bp",
                           __name__,
                           template_folder="templates",
                           static_folder="static")

@order_bp.route("/",methods=["GET"])
def index():
    return flask.render_template("IndexOrders.html")

@order_bp.route("/addOrder",methods=["GET","POST"])
def addOrder():
#check User login rights
    loginCheck = auth.checkUser()
    itemList = []
    if loginCheck.loggedIn == True:
        try:
            itemList = models.ItemStore.query.all()
        except Exception as e:
            logger.error("Eerror at db call for itemstore:\n",e)
        return flask.render_template(template_name_or_list="AddOrder.html",items=itemList)
    return flask.Response("you dont seem to be logged in",401)
