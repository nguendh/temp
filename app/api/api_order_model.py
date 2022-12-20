from flask import request, make_response, jsonify
from flask_restful import Resource

from app import db
from app.models import OrderModel


class GetOrderModel(Resource):
    def get(self):
        orders = OrderModel.query.all()
        orders_list = []
        for od in orders:
            od_data = {'Id': od.id, 'Status': od.status, 'Items': od.iems}
            orders_list.append(od_data)
        return {"OrderModel": orders_list}, 200


class AddOrderModel(Resource):
    def post(self):
        if request.is_json:
            od = OrderModel(status=request.json['Status'], items=request.json['Items'])
            db.session.add(od)
            db.session.commit()
            return make_response(jsonify({'Id': od.id, 'Status': od.status, 'Items': od.iems}), 201)
        else:
            return {'error': 'Request must be JSON'}, 400


class UpdateOrderModel(Resource):
    def put(self, id):
        if request.is_json:
            od = OrderModel.query.get(id)
            if od is None:
                return {'error': 'not found'}, 404
            else:
                od.status = request.json['Status'],
                od.items = request.json['Items']
                od.db.session.commit()
                return 'Updated', 200


class DeleteOrderModel(Resource):
    def delete(self, id):
        od = OrderModel.query.get(id)
        if od is None:
            return {'error': 'not found'}, 404
        db.session.delete(od)
        db.session.commit()
        return f'{id} is deleted', 200
