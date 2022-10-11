from qbnb import app 
from qbnb.models import *
from mongoengine import *
db = MongoEngine(app)

def create_listing(name, price, owner, description, last_modified_date):
    listing = Listing(
        name=name, price=price,
        owner=owner, description=description,
        last_modified_date=last_modified_date
    )
    try:
        listing.check()
        listing.save()
        return True
    except ValidationError as e:
        print(e.message)
        return False
