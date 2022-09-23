import json
from flask import Flask
from flask import request
from flask import jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

"""Setting name of database, host, and port
for the time being we are running the data models on our local machines
"""
app.config['MONGODB_SETTINGS'] = {
    'db': 'qbnb',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

"""Base User class (data model)
id: Identification number associated with user profile
username: Username of user
email: Email associated with user
balance: Money in user's account
"""
class User(db.Document):
    id = db.IntField(required=True)
    username = db.StringField(required=True)
    email = db.StringField(required=True)
    balance = db.FloatField(required=True)
    
    def __repr__(self):
        return f"username: (self.username) email: {self.email}"
