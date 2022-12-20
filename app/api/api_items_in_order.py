from flask import request, make_response, jsonify
from flask_restful import Resource

from app import db
from app.models import ItemsInOrder


class GetItemsInOrder(Resource):
    def get(self):
        items = ItemsInOrder.query.all()
        items_list = []
        for it in items:
            it_data = {'Id': it.id, 'ItemId': it.item_id, 'OrderId': it.order_id,
                       'Quantity': it.quantity}
            items_list.append(it_data)
        return {"ItemsInOrder": items_list}, 200


class AddItemsInOrder(Resource):
    def post(self):
        if request.is_json:
            it = ItemsInOrder(item_id=request.json['ItemId'],
                              order_id=request.json['OrderId'],
                              quantity=request.json['Quantity'])
            db.session.add(it)
            db.session.commit()
            return make_response(jsonify({'Id': it.id, 'ItemId': it.item_id, 'OrderId': it.order_id,
                                          'Quantity': it.quantity}), 201)
        else:
            return {'error': 'Request must be JSON'}, 400


class UpdateItemsInOrder(Resource):
    def put(self, id):
        if request.is_json:
            it = ItemsInOrder.query.get(id)
            if it is None:
                return {'error': 'not found'}, 404
            else:
                it.item_id = request.json['ItemId'],
                it.order_id = request.json['OrderId'],
                it.quantity = request.json['Quantity']
                db.session.commit()
                return 'Updated', 200


class DeleteItemsInOrder(Resource):
    def delete(self, id):
        it = ItemsInOrder.query.get(id)
        if it is None:
            return {'error': 'not found'}, 404
        db.session.delete(it)
        db.session.commit()
        return f'{id} is deleted', 200
