import json
from operator import truediv
from flask_mongoengine import BaseQuerySet
from mongoengine import *
from Booking import Booking

class Listing(Document): 
    name = StringField(required=True) 
    #images = EmbeddedDocumentListField()
    price = FloatField(required=True)
    #host = ReferenceField(User)
    #reviews = ListField(ReferenceField(Review))
    booked = BooleanField(default=False)
    requested_bookings = ListField(ReferenceField(Booking))
    current_booking = ReferenceField(Booking)
    meta = {"queryset_class" : BaseQuerySet}

    def __repr__(self): 
        return f"name: {self.name} price: {self.price}"
