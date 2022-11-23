"""
init file for qbnb
"""
from flask import Flask
from flask_mongoengine import MongoEngine
import os

app = Flask(__name__)

db_string = os.getenv('db_string')
if db_string:
    app.config['MONGODB_SETTINGS'] = db_string
else:
    app.config['MONGODB_SETTINGS'] = 'mongodb://localhost:27017/qbnb'
app.app_context().push()

app.config["MONGODB_SETTINGS"] = {
    "db": "qbnb",
    "host": "localhost",
    "port": 27017
}
app.config["SECRET_KEY"] = "SECRET_KEY"
db = MongoEngine(app)
