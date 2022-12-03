from qbnb import app
from qbnb.models import Listing
from qbnb.models import Booking
from qbnb.models import User
from qbnb.models import MongoEngine
from mongoengine import ValidationError
db = MongoEngine(app)


def create_listing(title, price, owner, description, last_modified_date):
    '''
    Takes in name, price, owner, description and last_modified_date as
    input and attempts to save it to MongoDB. If the provided input is
    valid, then it will save it and return True. If there are any
    ValidationErrors, it will return False.
    '''
    listing = Listing(
        title=title, price=price,
        owner=owner, description=description,
        last_modified_date=last_modified_date
    )
    try:
        listing.check()
        listing.save(cascade=True)
        return True
    except ValidationError as e:
        print(e.message)
        return False


def create_booking(guest, start_date, end_date, listing):
    """
    Takes in a guest (User object), start and end dates,
    and the parent listing (Listing object) and attempts
    to create a booking in the specified listing.
    Returns False if a ValidationError is raised
    """
    booking = Booking(
        guest=guest,
        start_date=start_date,
        end_date=end_date
    )
    try:
        # Can the booking be added?
        listing.check_booking(booking)
        # Update listing document in MongoDB and
        # update our own representation as well
        Listing.objects(id=listing.id).update_one(
            push__bookings=booking
        )
        listing.reload()
        # Deduct listing price from guest balance
        User.objects(id=guest.id).update_one(
            dec__balance=listing.price
        )
        # Add listing price to owner balance
        User.objects(id=listing.owner.id).update_one(
            inc__balance=listing.price
        )
        guest.balance -= listing.price
        guest.reload()
        return True
    except ValidationError as e:
        print(e.message)
        return False
