import flask
import json
from typing import List

from sqlalchemy.sql.functions import user

from AppRoot.Order import models
from AppRoot.app import logger
from AppRoot.Login import auth
from AppRoot.Order import models as itemModels

management_bp: flask.Blueprint = flask.Blueprint(name="management_bp",
                                                 import_name= __name__,
                                                 template_folder="templates",
                                                 static_folder="static")

@management_bp.route(rule="/items",methods=["GET","POST"])
def mgmtItems():
    items: List[itemModels.ItemStore]
    userLogin = auth.checkUser()

    if flask.request.method == 'GET':
        if userLogin.loggedIn and userLogin.user.accessType == "admin":
            items = itemModels.ItemStore.query.all()
            return flask.render_template("index.html",items=items)
        else:
            return flask.Response("You have no access rights",401)
    elif flask.request.method == 'POST':
        if userLogin.loggedIn and userLogin.user.accessType == "admin":
            bodyJson = flask.request.get_json()
            logger.debug("request: %s",bodyJson)

            try:
                if bodyJson['operation'] == 'ChangeEntity':
                    pass

            items = itemModels.ItemStore.query.all()
            return flask.render_template("index.html",items=items)
        else:
            return flask.Response("You have no access rights",401)

