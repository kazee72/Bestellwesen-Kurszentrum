#structure of db for order for sqlitealchemy
from functools import total_ordering
from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm import Mapped
from AppRoot.database import db

class ItemStore(db.Model):
    __tablename__ = "item_store_table"
    uid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    describtion: Mapped[str]
    totalAmountOfKind: Mapped[int]
    reservedAmountOfKind: Mapped[int]
    takenAmountOfKind: Mapped[int]

class ItemOrder(db.Model):
    __tablename__ = "item_order"
    parentOrder: Mapped[int] = mapped_column(ForeignKey("order_table.orderNumber"))
    orderItemId: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int] # the order amount
    state: Mapped[str] # is the order given, in progress, finished, or canceled?
    
class Order(db.Model):
    __tablename__ = "order_table"
    ownerid: Mapped[int] = mapped_column(ForeignKey("user_table.uid"))
    orderName: Mapped[Optional[str]]
    orderNumber = db.Column(db.Integer,primary_key=True)
    items: Mapped[List["ItemOrder"]] = relationship() #list of ItemOrder
