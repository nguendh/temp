from flask import request, make_response, jsonify
from flask_restful import Resource

from app import db
from app.models import Item


class GetItem(Resource):
    def get(self):
        items = Item.query.all()
        items_list = []
        for it in items:
            it_data = {'Id': it.id, 'ItemName': it.name, 'Price': it.price,
                       'Inventory': it.inventory}
            items_list.append(it_data)
        return {"Items": items_list}, 200


class AddItem(Resource):
    def post(self):
        if request.is_json:
            it = Item(name=request.json['ItemName'],
                      price=request.json['Price'],
                      inventory=request.json['Inventory'])
            db.session.add(it)
            db.session.commit()
            return make_response(jsonify({'Id': it.id, 'ItemName': it.name, 'Price': it.price,
                                          'Inventory': it.inventory}), 201)
        else:
            return {'error': 'Request must be JSON'}, 400


class UpdateItem(Resource):
    def put(self, id):
        if request.is_json:
            it = Item.query.get(id)
            if it is None:
                return {'error': 'not found'}, 404
            else:
                it.name = request.json['ItemName'],
                it.price = request.json['Price'],
                it.inventory = request.json['Inventory']
                db.session.commit()
                return 'Updated', 200


class DeleteItem(Resource):
    def delete(self, id):
        it = Item.query.get(id)
        if it is None:
            return {'error': 'not found'}, 404
        db.session.delete(it)
        db.session.commit()
        return f'{id} is deleted', 200
