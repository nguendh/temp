from flask import request, make_response, jsonify

from app import db
from flask_restful import Resource


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<User {}, {}, {}>'.format(self.username, self.full_name, self.address)


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    inventory = db.Column(db.Integer)

    def __repr__(self):
        return '<Item {}, {}>'.format(self.name, self.price)


class ItemsInOrder(db.Model):
    __tablename__ = "items_in_order"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column("item_id", db.Integer, db.ForeignKey("items.id"))
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("orders.id"))
    quantity = db.Column(db.Integer)

    item = db.relationship("Item")
    order = db.relationship("OrderModel", back_populates="items")


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(15), nullable=True)

    items = db.relationship("ItemsInOrder", back_populates="order")


