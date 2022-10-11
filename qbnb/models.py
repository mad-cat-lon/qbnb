from flask_mongoengine import BaseQuerySet
from mongoengine import *
from flask_mongoengine import MongoEngine
from qbnb import app
import re
import datetime
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


class User(db.Document):
    email = EmailField(required=True)
    password = StringField(required=True)
    user_name = StringField(required=True)
    billing_address = StringField()
    postal_code = StringField()
    balance = FloatField(required=True)

    def __init__(self, id, username, email, balance):
        self.id = id
        self.username = username
        self.email = email
        self.balance = balance

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


class Transaction(db.Document):
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


class Listing(db.Document):
    title = StringField(required=True)
    description = StringField(required=True)
    price = FloatField(required=True)
    last_modified_date = IntField(required=True)
    owner_id = IntField(required=True)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of Listing
    def __repr__(self):
        return f"name: {self.title} price: {self.price}"


"""
Base Listing class
user_id: id of the user who gave the review
listing_id: id of the listing being reviewed
review_text: Content of review
date: Date of the review
"""


class Review(db.Document):
    user_id = IntField(required=True)
    listing_id = IntField(required=True)
    review_text = StringField(required=True)
    date = IntField(required=True)

    def __repr__(self):
        return f"user: {self.user_id} reviewed listing: {self.listing_id}"


def update_listing(title, new_title, description, price, new_price,
                   last_modified_date):
    """
    --Description--
    Function for updating all attributes of a listing, except owner_id and
    last_modified_date. If parameter is None, then it is not changed.

    --Parameters--
    title: string, name of listing to be updated.
    new_title: string, updated name of listing.
    description: string, description of listing to be updated.
    price: float, price of listing to be updated, can only be increased.
    new_price: float, new price, can be None.
    last_modified_date: integer, last modified date of listing, should be
    updated once operation is successful.

    """
    listing = Listing.objects(title=title)
    if len(listing) != 1:
        return False
    else:
        listing = listing[0]
    
    if new_title is not None:
        if len(new_title) > 80:
            return False
        if new_title[0] == ' ' or new_title[-1] == ' ':
            return False
        for i in new_title:
            if not (i.isalnum() or i == ' '):
                return False
        listing.update(new_title=new_title)
        listing.reload()

    if description is not None:
        if len(description) < 20 or len(description) > 2000:
            return False
        if len(description) <= len(new_title):
            return False
        listing.update(description=description)
        listing.reload()

    if new_price is not None:
        if float(new_price) < float(price):
            return False
        if float(new_price) < 10 or float(new_price) > 10000:
            return False
        listing.update(price=new_price)
        listing.reload()

    if last_modified_date is not None:
        if int(last_modified_date) < 20210102 or\
                int(last_modified_date) > 20250102:
            return False
    
    """
    if update_listing(
            title, description, price, new_price, last_modified_date) is True:
        listing.update(last_modified_date=last_modified_date)
    """
    return True
