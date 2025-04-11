#here We define the structure of the infos in the userDb using sqlitealchemy
from __future__ import annotations
from typing import List

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from ..database import db as userDb
from AppRoot.Order.models import Order

class User(userDb.Model):
    __tablename__ = "user_table"

    uid = userDb.Column(userDb.Integer,primary_key=True)
    email = userDb.Column(userDb.String(100))
    password = userDb.Column(userDb.String(100))
    username = userDb.Column(userDb.String(100),unique=True)
    firstname = userDb.Column(userDb.String(100))
    lastname = userDb.Column(userDb.String(100))
    orders: Mapped[List["Order"]] = relationship()
