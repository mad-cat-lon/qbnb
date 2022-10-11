from flask_mongoengine import BaseQuerySet
from mongoengine import *
from flask_mongoengine import MongoEngine
from qbnb import app
import re
db = MongoEngine(app)
"""
Base Booking class
user_id: id of the user booking the place
listing_id: id of the listing being booked
price: Price of listing
date: Date of the booking
"""


class Booking(db.Document):
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


class User(Document):
    email = EmailField(required=True)
    password = StringField(required=True)
    user_name = StringField(required=True)
    billing_address = StringField()
    postal_code = StringField()
    balance = FloatField(required=True)

    def __repr__(self):
        return f"username: {self.username} email: {self.email}"


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


def login(email, password):
    """
    Function for user login, allow user to login using
    email and pass word.

    Parameter:
    email: string, email of user
    password: string pass owrd of user

    Return:
    user object if succeed, False other wise

    """
    # regular expression to check email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email == '' or password == '':
        return False

    if not (re.fullmatch(regex, email)):
        return False

    if len(password) < 6:
        return False

    if len(re.findall('[^A-Za-z0-9]', password)) != 0:
        return False

    if re.search('[A-Z]', password) is None:
        return False

    if re.search('[a-z]', password) is None:
        return False

    valid = User.objects(email=email, password=password)
    if valid is None:
        return False

    if len(valid) != 1:
        return False

    return valid[0]


def update_user(org_email, user_name, new_email,
                billing_address, postal_code):
    """
    Function for updating user profile. The user with the org_email will 
    be updated. If parameter is None, then it is not changed

    Parameter
    org_email: string, email of the user being updated
    user_name: string, new user name, can be None
    new_email: string, new email address, can be None
    billling_address: string, new billing address, can be None
    postal_code: string, new postal code, can be None

    """
    user = User.objects(email=org_email)
    if len(user) != 1:
        return False
    else:
        user = user[0]

    if user_name is not None:
        if len(user_name) > 20 or len(user_name) < 2:
            return False
        if user_name[0] == ' ' or user_name[-1] == ' ':
            return False
        for i in user_name:
            if not (i.isalnum() or i == ' '):
                return False
        user.update(user_name=user_name)
        user.reload()

    if postal_code is not None:
        postal_reg = r'[A-Z]{1}[0-9]{1}[A-Z]{1}\s{1}[0-9]{1}[A-Z]{1}[0-9]{1}'
        postal_code = postal_code.upper()
        if len(postal_code) != 7:
            return False
        if len(re.findall(postal_reg, postal_code)) != 1:
            return False
        user.update(postal_code=postal_code)
        user.reload()

    if new_email is not None:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, new_email)):
            return False
        unique = User.objects(email=new_email)
        if len(unique) != 0:
            return False
        user.update(email=new_email)
        user.reload()

    if billing_address is not None:
        user.update(billing_address=billing_address)
        user.reload()

    return True
