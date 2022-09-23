from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "qbnb",
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)


# Transactions class to create fields in the database
class Transactions(db.Document):
    """
    Description for each field:
    reference: call base user class for user info
    ^to be changed later when user class is fully implemented^
    bookingID: ID of booking made in booking class
    date = date of transaction made
    time = time of transaction made
    amount = amount paid at transaction
    trans_start = start of transaction process
    trans_end = end of transaction process
    """
    reference = db.ReferenceField(user)
    bookingID = db.StringField(required=True)
    date = db.StringField(required=True)
    time = db.StringField(required=True)
    amount = db.IntField(min_value=0, max_value=None, required=True)
    trans_start = StringField(required=True)
    trans_end = StringField(required=True)

    # Function for representating the start and end to the transaction
    def __repr__(self):
        return f"transaction_start: {self.trans_start} \
            transaction_end: {self.trans_end}"
