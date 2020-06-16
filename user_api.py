from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class User(Resource):
  def get(self, id):
    try:
      response = users[id]
    except IndexError:
      message = 'User with id:{} do not exist.'.format(id)
      response = {'status': 'error', 'message': message}
    except Exception:
      message = 'Unknown error.'
      response = {'status': 'error', 'message': message}
    return response  

  def put(self, id):
    data = json.loads(request.data)
    users[id] = data
    return data

  def delete(self, id):
    users.pop(id)
    return {'status':'sucess', 'message': 'Data Deleted'}

class ListUsers(Resource):
  def get(self):
    return users

  def post(self):
    data = json.loads(request.data)
    position = len(users)
    data['id'] = position
    users.append(data)
    return users[position]

api.add_resource(User, '/users/<int:id>/')
api.add_resource(ListUsers, '/users/')

if __name__ == "__main__":
    app.run(debug=True)