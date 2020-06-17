from flask import Flask

appi = Flask('appi')

@appi.route('/users/<string:name>')
def get_user(name):
    return '0k', 200