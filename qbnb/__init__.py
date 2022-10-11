from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "qbnb",
    "host": "localhost",
    "port": 27017
}
app.config["SECRET_KEY"] = "SECRET_KEY"
db = MongoEngine(app)
