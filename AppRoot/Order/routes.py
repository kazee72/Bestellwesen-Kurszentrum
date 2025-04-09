import flask

order_bp = flask.Blueprint("order_bp",
                           __name__,
                           template_folder="templates",
                           static_folder="static")

@order_bp.route("/",methods=["GET"])
def index():
    return flask.render_template("IndexOrders.html")
