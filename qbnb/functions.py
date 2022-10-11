from qbnb import app 
from qbnb.models import *
from mongoengine import *
db = MongoEngine(app)

def create_listing(name, price, owner, description, last_modified_date):
    '''
    Takes in name, price, owner, description and last_modified_date as
    input and attempts to save it to MongoDB. If the provided input is 
    valid, then it will save it and return True. If there are any 
    ValidationErrors, it will return False.
    '''
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
