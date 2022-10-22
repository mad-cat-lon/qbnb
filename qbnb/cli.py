from qbnb import models
from qbnb.models import update_listing
from datetime import datetime


def listing_update_page(listing):
    new_title = input('Please enter new title: ')
    new_description = input('Please enter new description: ')
    new_price = float(input('Please enter new price: '))
    if new_title == "":
        new_title = None
    if new_description == "":
        new_description = None
    if new_price == 0:
        new_price = None
    push = update_listing(
        title=listing.title,
        new_title=new_title,
        description=new_description,
        price=listing.price,
        new_price=new_price,
        last_modified_date=datetime.now().strftime("%Y-%m-%d")
    )
    if push is True:
        print('Listing updated.')
