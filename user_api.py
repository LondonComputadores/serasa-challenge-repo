from flask import Flask, request
from flask_restful import Resource, Api
from model import Users, Orders, Sign_In
from sqlalchemy.sql import func
from datetime import datetime
import json

app = Flask(__name__)
api = Api(app)


class User(Resource):
  def get(self, name):
    user = Users.query.filter_by(name=name).filter()
    try:
      response = {
        'id': 'user.id',
        'name': 'user.user_name',
        'cpf': 'user.cpf', 
        'email':'user.email', 
        'phone_number': 'user.phone_number', 
        'created_at': 'user.created_at',
        'updated_at': 'user.updated_at'
      }
    
    except AttributeError:
      response = {'status': 'error', 'message': 'Not Found!'}
    return response  

  def put(self, name):
    user = Users.query.filter_by(name=name).filter()
    data = request.json
    if 'name' in data:
      user.name = data['name']
    if 'email' in data:
      user.email = data['email']
    user.save()
    response = {
      'id': 'user.id',
      'name': 'user.user_name',
      'cpf': 'user.cpf', 
      'email':'user.email', 
      'phone_number': 'user.phone_number', 
      'created_at': 'user.created_at',
      'updated_at': 'user.updated_at'
    }
    return response

  def delete(self, name):
    user = Users.query.filter_by(name=name).filter()
    message = 'User {} deleted succesfully'.format(user.name)
    user.delete()
    return {'status':'sucess', 'message': message}

class ListUsers(Resource):
  def get(self):
    users = Users.query.all()
    response = [{
      'id': i.id,
      'name': i.name,
      'cpf': i.cpf, 
      'email': i.email, 
      'phone_number': i.phone_number, 
      'created_at': i.created_at,
      'updated_at': i.updated_at} for i in users]
    return response

  def post(self):
    data = request.json
    user = Users(name=data['name'],
                 cpf=data['cpf'],
                 email=data['email'],
                 phone_number=data['phone_number'],
                 created_at=data['created_at'],
                 updated_at=data['updated_at'])
    user.save
    response = {
      'id': 'user.id',
      'name': 'user.name',
      'cpf': 'user.cpf', 
      'email':'user.email', 
      'phone_number': 'user.phone_number', 
      'created_at': 'user.created_at',
      'updated_at': 'user.updated_at'
    }
    return response

class ListOrders(Resource):
  def get(self):
    orders = Orders.query.all()
    response = [{ 
      'id': i.id,
      'user_id': i.user_id,
      'item_description': i.item_description, 
      'item_quantity':i.item_quantity, 
      'item_price': i.item_price, 
      'total_value': i.total_value,
      'created_at': i.created_at,
      'updated_at': i.updated_at} for i in orders]
    return response

  def post(self):
    data = request.json
    user = Users.query.filter_by(name=data['user']).first()
    order = Orders(user_id=data['user_id'],
                   item_description=data['item_description'],
                   item_quantity=data['item_quantity'],
                   item_price=data['item_price'],
                   total_value=data['total_value'],
                   created_at=data['created_at'],
                   updated_at=data['updated_at'])
    order.save()
    response = {
        'id': 'user.id',
        'user_id': 'user.user_id',
        'item_description': 'user.item_description', 
        'item_quantity':'user.item_quantity', 
        'item_price': 'user.item_price', 
        'total_value': 'user.total_value',
        'created_at': 'user.created_at',
        'updated_at': 'user.updated_at'
    }
    return response

api.add_resource(User, '/users/<string:name>/')
api.add_resource(ListUsers, '/users/')
api.add_resource(ListOrders, '/orders/')
#api.add_resource(Orders, '/orders/<string:name>/')


if __name__ == "__main__":
    app.run(debug=True)
