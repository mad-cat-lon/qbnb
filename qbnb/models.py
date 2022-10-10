from flask_mongoengine import BaseQuerySet
from flask_mongoengine import MongoEngine
from mongoengine import Document
from mongoengine import ReferenceField
from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import StringField
from mongoengine import FloatField
from mongoengine import IntField
from mongoengine import ValidationError
from mongoengine import ListField
import re
import datetime
from qbnb import app
db = MongoEngine(app)

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
    id = IntField(required=True, primary_key=True)
    username = StringField(required=True)
    email = StringField(required=True)
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


class Listing(db.Document):
    name = StringField()
    # images = EmbeddedDocumentListField()
    price = FloatField()
    owner = ReferenceField(User)
    # reviews = ListField(ReferenceField(Review))
    last_modified_date = DateTimeField()
    description = StringField()
    booked = BooleanField(default=False)
    requested_bookings = ListField(ReferenceField(Booking))
    current_booking = ReferenceField(Booking)
    meta = {"queryset_class": BaseQuerySet}

    def check(self):
        '''
        Checks to see if created Listing object conforms to requirements
        and raises a ValidationError if it does not
        '''
        # R4-1
        valid_name_regex = "^[1-9A-Za-z][1-9A-Za-z ]*[1-9A-Za-z]$"
        if re.search(valid_name_regex, self.name) is None:
            raise ValidationError(
                "Name of listing can only contain"
                "alphanumeric characters and spaces")
                             
        # R4-2
        if len(self.name) > 80:
            raise ValidationError("Name of listing is too long")

        # R4-3
        if len(self.description) < 20 or len(self.description) > 2000:
            raise ValidationError(
                "Description must be between 20 to"
                "2000 characters")

        # R4-4
        if len(self.description) < len(self.name):
            raise ValidationError("Description must be longer than title")
       
        # R4-5
        if self.price < 10 or self.price > 10000:
            raise ValidationError("Price must be between 10 and 10000")

        # R4-6
        last_modified_date = datetime.datetime.strptime(
            self.last_modified_date, "%Y-%m-%d").date()
        if (last_modified_date < datetime.date(2021, 1, 2) or
                last_modified_date > datetime.date(2025, 1, 2)):
            raise ValidationError("Invalid modification date")

        # R4-7
        if self.owner is None:
            raise ValidationError("Cannot create listing without owner")
       
        # R4-8
        listings = Listing.objects(name=self.name, owner=self.owner.id)
        print(listings)
        if len(listings) != 0:
            raise ValidationError("Cannot create listing with same name")
               
    # String representation of Listing
    def __repr__(self):
        return f"name: {self.name} price: {self.price}"
