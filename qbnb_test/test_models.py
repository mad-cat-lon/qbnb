"""
Test cases for the file models.py
"""
from flask_mongoengine import BaseQuerySet
from flask_mongoengine import QuerySet
from mongoengine import *
from flask_mongoengine import MongoEngine
from qbnb import app
from qbnb.models import update_listing, Listing


def test_r5_1_update_listing():
    """
    Testing for R5-1: admin is able to update all attributes
        of the listing, except owner_id and last_modified_date.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view, \
            king bed, spa included.', price=2000, last_modified_date=20220928,
              owner_id=1234)
    listing.save()
    result = update_listing('Beverly Hills Inn', 'Beverly Hills Mansion',
                            'Luxury suite with sea view, king bed, spa\
                                 included.', 2000, 2000, 20220928)
    listing = Listing.objects(title='Beverly Hills Mansion')
    assert result is not False
    listing = listing[0]
    assert listing.price == 2000
    assert listing.title == 'Beverly Hills Mansion'
    assert listing.description == 'Luxury suite with sea view, \
            king bed, breakfast and dinner included.'
    assert listing.last_modified_date == 20220928
    listing.delete()


'''
def test_r5_2_update_listing():
    """
    Testing for R5-2: admin is only able to increase price.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view, \
            king bed, spa included.', price=2000, last_modified_date=20220928)
    listing.save()
    listing = Listing.objects(price=2300)
    result = update_listing('Beverly Hills Inn', 'Luxury suite with\
         sea view, king bed, spa included.', 2000, 2300, 20220928)
    invalid_result = update_listing('Beverly Hills Inn', 'Luxury suite with\
         sea view, king bed, spa included.', 2000, 1900, 20220928)
    assert result is True
    assert invalid_result is False
    assert listing[0].price == 2000
    listing[0].delete()


def test_r5_3_update_listing():
    """
    Testing for R5-3: last_modified_date can only be updated\
         when the update operation is successful.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view, \
            king bed, spa included.', price=2000, last_modified_date=20220928)
    listing.save()
    listing = Listing.objects(price=2000)
    result = update_listing('Beverly Hills Inn', 'Luxury suite with\
         sea view, king bed, spa included.', 2000, 2300, 20220928)
    invalid_result = update_listing('Beverly Hills Inn', 'Luxury suite with\
         sea view, king bed, spa included.', 2000, 1900, 20221010)
    assert result is True
    assert invalid_result is False
    assert listing.last_modified_date == 20221010
    listing[0].delete()


def test_r5_4_update_listing():
    """
    Testing for R5-4: test for whether attributes follow the same\
        requirements.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view, \
            king bed, spa included.', price=2000, last_modified_date=20220928)
    listing.save()
    listing = Listing.objects(price=2000)
    result = update_listing(title, description, price, new_price,
                            last_modified_date)('Beverly Hills Inn\
                                ', '', None, 2000, None)
    invalid_result_1 = update_listing('Beverly Hills Inn', 'nice', 2000,
                                      2300, 20220928)
    invalid_result_2 = update_listing('Beverly Hills Inn',
                                      'Luxury suite with sea view, \
                                        king bed, spa included.',
                                      2000, 0, 20200928)
    assert result is True
    assert listing[0].title == 'Beverly Hills Inn'
    assert invalid_result_1 is False
    assert invalid_result_2 is False
    assert listing[0].title == 'Beverly Hills Inn'
    listing[0].delete()
'''
