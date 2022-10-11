from qbnb import app
import re
from mongoengine import *
from flask_mongoengine import BaseQuerySet
from flask_mongoengine import MongoEngine
db = MongoEngine(app)

"""
Base Booking class
user_id: id of the user booking the place
listing_id: id of the listing being booked
price: Price of listing
date: Date of the booking
"""


class Booking(Document):
    user_id = IntField(required=True)
    listing_id = IntField(required=True)
    price = FloatField(required=True)
    date = IntField(required=True)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of booking
    def __repr__(self):
        return f"booking_start: {self.booking_start} \
            booking_end: {self.booking_end}"


"""
Base User class (data model)
email: Email of the user
password: Password of the user
user_name: Name of the user
billing_address: Billing address of the user
postal_code: Postal code of user
balance: Account balance of the user
"""


class User(db.Document):
    email = EmailField(required=True)
    password = StringField(required=True)
    user_name = StringField(required=True)
    billing_address = StringField(required=True)
    postal_code = StringField(required=True)
    balance = FloatField(required=True)

    def __repr__(self):
        return f"username: {self.username} email: {self.email}"


"""
user registration function: Creates user in MongoDB.

Parameters
_email: User's email
_password: User's password
_user_name: User's username
_balance: Preset to 100

On initialization of flask, two user's are created 
After this no it returns to normal
"""


def user_register(_email, _password, _user_name, _balance=100):
    special_characters = set('`~!@#$%^&*()_-=+\{\}\\|;:\'\",./?')
    regex_email_5322 = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    regex_spaces = r"^\S$|^\S[ \S]*\S$"
    regex_alphanumeric = r"^[a-zA-Z0-9 ]*$"
    if _email == '' or _password == '':
        return

    if not (re.fullmatch(regex_email_5322, _email)):
        return

    if (len(_password) < 6):
        return

    if (_password.lower() == _password):
        return
    
    if (_password.upper() == _password):
        return

    if not special_characters.intersection(_password):
        return

    if _user_name == '':
        return
    
    if not (re.fullmatch(regex_alphanumeric, _user_name)):
        return
    
    if not (re.fullmatch(regex_spaces, _user_name)):
        return

    if not len(_user_name) > 2 or not len(_user_name) < 20:
        return

    if (User.objects(email=_email)):
        return
    
    user = User(email=_email, password=_password, user_name=_user_name,
                billing_address='', postal_code='', balance=_balance)

    user.save()
    return user


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


class Transaction(Document):
    reference = ReferenceField(User)
    bookingID = StringField(required=True)
    date = StringField(required=True)
    time = StringField(required=True)
    amount = IntField(min_value=0, max_value=None, required=True)
    trans_start = StringField(required=True)
    trans_end = StringField(required=True)

    # Function for representating the start and end to the transaction
    def __repr__(self):
        return f"transaction_start: {self.trans_start} \
            transaction_end: {self.trans_end}"


"""
Base Listing class
title: Name of listing
description: Description of listing
price: Price of Listing
owner_id: id of the owner
"""


class Listing(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    price = FloatField(required=True)
    last_modified_date = IntField(required=True)
    owner_id = IntField(required=True)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of Listing
    def __repr__(self):
        return f"name: {self.name} price: {self.price}"


"""
Base Listing class
user_id: id of the user who gave the review
listing_id: id of the listing being reviewed
review_text: Content of review
date: Date of the review
"""


class Review(Document):
    user_id = IntField(required=True)
    listing_id = IntField(required=True)
    review_text = StringField(required=True)
    date = IntField(required=True)

    def __repr__(self):
        return f"user: {self.user_id} reviewed listing: {self.listing_id}"
