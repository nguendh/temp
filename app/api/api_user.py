from flask import request, make_response, jsonify
from flask_restful import Resource

from app import db
from app.models import User


class GetUser(Resource):
    def get(self):
        users = User.query.all()
        users_list = []
        for us in users:
            us_data = {'Id': us.id, 'Username': us.username, 'Password': us.password,
                       'FullName': us.full_name, 'Address': us.address, 'Phone': us.phone}
            users_list.append(us_data)
        return {"Users": users_list}, 200


class AddUser(Resource):
    def post(self):
        if request.is_json:
            us = User(username=request.json['Username'],
                      password=request.json['Password'],
                      full_name=request.json['FullName'],
                      address=request.json['Address'],
                      phone=request.json['Phone'])
            db.session.add(us)
            db.session.commit()
            return make_response(jsonify({'Id': us.id, 'Username': us.username, 'Password': us.password,
                                          'FullName': us.full_name, 'Address': us.address, 'Phone': us.phone}), 201)
        else:
            return {'error': 'Request must be JSON'}, 400


class UpdateUser(Resource):
    def put(self, id):
        if request.is_json:
            us = User.query.get(id)
            if us is None:
                return {'error': 'not found'}, 404
            else:
                us.username = request.json['Username']
                us.password = request.json['Password']
                us.full_name = request.json['FullName']
                us.address = request.json['Address']
                us.phone = request.json['Phone']
                db.session.commit()
                return 'Updated', 200


class DeleteUser(Resource):
    def delete(self, id):
        us = User.query.get(id)
        if us is None:
            return {'error': 'not found'}, 404
        db.session.delete(us)
        db.session.commit()
        return f'{id} is deleted', 200
