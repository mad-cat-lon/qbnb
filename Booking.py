import json
from operator import truediv
from mongoengine import *
from flask_mongoengine import BaseQuerySet

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
