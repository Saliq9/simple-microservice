#Basic REST mivcroservice example
import re

from flask import Flask, jsonify, request
from userdata import users

app = Flask(__name__)

#Message when service is up
@app.route('/', methods=['GET'])
def index():
    return 'Hello! This is a microservice example.'

#Get the list of users
# Get a list of resources
@app.route('/users', methods=['GET'])
def display_users():
    return jsonify(list(users.values()))

# Get a single resource
@app.route('/users/<user_id>', methods=['GET'])
def display_single_user(user_id):
    if user_id not in users:
        return 'User Not Found', 404
    return jsonify(users[user_id])

if __name__=='__main__':
    app.run(port=5000, debug=True)
