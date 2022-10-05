from flask_mongoengine import BaseQuerySet
from mongoengine import *

"""
Base Booking class
guest: User associated with the booking
booking_start: Start of booking period
booking_end: End of booking period
"""


class Booking(Document):
    # guest = ReferenceField(User)
    # Host must confirm booking before it is registered
    confirmed = BooleanField(default=False)
    booking_start = StringField(required=True)
    booking_end = StringField(required=True)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of booking
    def __repr__(self):
        return f"booking_start: {self.booking_start} \
            booking_end: {self.booking_end}"


"""Base User class (data model)
id: Identification number associated with user profile
username: Username of user
email: Email associated with user
balance: Money in user's account
"""


class User(Document):
    id = IntField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
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
name: Name of the listing
images: Array of embedded images
price: Price of the listing
host: User object representing the host
reviews: Array of Review objects
booked: Boolean value representing if the listing
        is booked
requested_bookings: Array of requested Booking
        objects
current_booking: the current booking
"""


class Listing(Document):
    name = StringField(required=True)
    # images = EmbeddedDocumentListField()
    price = FloatField(required=True)
    # host = ReferenceField(User)
    # reviews = ListField(ReferenceField(Review))
    description = StringField(required=True)
    booked = BooleanField(default=False)
    requested_bookings = ListField(ReferenceField(Booking))
    current_booking = ReferenceField(Booking)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of Listing
    def __repr__(self):
        return f"name: {self.name} price: {self.price}"
