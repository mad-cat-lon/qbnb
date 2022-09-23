import json
from operator import truediv
from flask_mongoengine import BaseQuerySet
from mongoengine import *
from Booking import Booking

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
    booked = BooleanField(default=False)
    requested_bookings = ListField(ReferenceField(Booking))
    current_booking = ReferenceField(Booking)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of Listing
    def __repr__(self):
        return f"name: {self.name} price: {self.price}"
