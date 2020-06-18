from flask import Flask, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api
from model import Users, Orders, Sign_In
from sqlalchemy.sql import func
from datetime import datetime
import json
import redis

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

cache = redis.Redis(host='redis', port=6379)

@auth.verify_password
def acknowledge(login, password):
  """
      Esse método verifica login do usuário
  """
    # if not (login, password):
    #     return False
    # return Sign_In.query.filter_by(login=login, password=password).first()


class User(Resource):
  #@auth.login_required #Precisa comentar essa linha para rodar o docker
  def get(self, name):
    #Lista usuário pelo nome e caso não encontrado retorna mensagem de erro.
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

  @auth.login_required
  def put(self, name):
    #Altera dados do usuário
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

  @auth.login_required
  def delete(self, name):
    #Exclui um usuário e retorna messagem de confirmação
    user = Users.query.filter_by(name=name).filter()
    message = 'User {} deleted succesfully'.format(user.name)
    user.delete()
    return {'status':'sucess', 'message': message}

class ListUsers(Resource):
  #Lista todos os usuários
  #@auth.login_required #Precisa comentar essa linha para rodar o docker
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

  @auth.login_required
  def post(self):
    #Cria um novo usuário
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
  @auth.login_required
  def get(self):
    #Lista os pedidos e retorna junto com as informações do usuário
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

  @auth.login_required
  def post(self):
    #Cria novo pedido com id do usuário e habilita consulta pelo nome
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
#api.add_resource(Orders, '/orders/<string:name>/') #need a bug fix


if __name__ == "__main__":
    app.run(debug=True)
