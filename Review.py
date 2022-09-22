# Base class for reviews.
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'qbnb',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)


class Review(db.Document):
    """
    Base Review Class
    username: Name of user giving the review
    listing: Name of the property being reviewed
    comment: Review comment
    ratiing: Numerical rating
    date: Time of review
    id: Review id
    """
    username = db.StringField(required=True)
    listing = db.StringField(required=True)
    comment = db.StringField(max_length=1000, required=True)
    rating = db.IntField(default=0, max_value=5, min_value=0, required=True)
    date = db.IntField(required=True)
    id = db.IntField(required=True)

    def __repr__(self):
        return f'Review(User={self.username}, Listing={self.listing})'
