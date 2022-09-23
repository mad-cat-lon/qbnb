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
        firstname: First name of client
        surname: Last/family name of client
        email: Email address of client
        phone: Primary phone number of client
        date: Date of transaction
        price: Amount paid at transaction
        roomID: Room/Suite selected by client
        cardNum: Credit/Debit card number used for transaction
    """
    firstname = db.StringField(required=True)
    surname = db.StringField(required=True)
    email = db.StringField(max_length=100, min_length=None, required=True)
    phone = db.StringField(max_length=30, min_length=None, required=True)
    date = db.StringField(required=True)
    price = db.IntField(min_value=0, max_value=None, required=True)
    roomID = db.IntField(required=True)
    cardNum = db.IntField(min_value=0, max_value=30, required=True)

    # Function for representating the start and end to the transaction
    def __repr__(self):
        return f"transaction_start: {self.trans_start} \
            transaction_end: {self.trans_end}"
