from venv import create
from qbnb.models import *
from qbnb.functions import *
import requests
from mongoengine import *


def test_r4_1_listing_create():
    '''
    Testing R4-1 in listing creation
    Requirement: the title of the product has to be
    alphanumeric only, and spaces are only allowed as prefixes and suffixes
    '''
    test_cases = {
        " ": False,
        " ABCD123": False,
        "ABCD123 ": False,
        " ABCD123 ": False,
        " ABCD 123 ": False,
        ".": False,
        " . . ": False,
        "ABCD .123": False,
        "ABCD 123": True,
        "ABCD  123": True,
        "ABCD123": True
    }
    for key, value in test_cases.items(): 
        print(key, value)
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        ret = create_listing(
            title=key,
            price=100,
            owner=owner,
            description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            last_modified_date="2022-03-09"
        )
        if value is True:
            assert ret is True
        if value is False:
            assert ret is False
        # Delete our objects
        listing = Listing.objects(title=key)
        listing.delete()
        owner = User.objects(username="abcd123")
        owner.delete()


def test_r4_2_listing_create():
    '''
    Testing R4-2 in listing creation
    Requirement: the title of the listing can be no longer than 80 characters
    '''
    test_cases = {
        "A" * 81: False,
        "AAAAAAAA": True
    }
    for key, value in test_cases.items(): 
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        ret = create_listing(
            title=key,
            price=100,
            owner=owner,
            description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            last_modified_date="2022-03-09"
        )
        if value is True:
            assert ret is True
        if value is False:
            assert ret is False
        # Delete our objects
        listing = Listing.objects(title=key)
        listing.delete()
        owner = User.objects(username="abcd123")
        owner.delete()


def test_r4_3_listing_create():
    '''
    Testing R4-3 in listing creation
    Requirement: the description of the product can be arbitrary characters,
    with a minimum length of 20 characters and a maximum of 2000
    '''
    test_cases = {
        "": False,
        "ABCD123": False,
        "*" * 2001: False,
        "*" * 1999: True
    }
    for key, value in test_cases.items(): 
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        ret = create_listing(
            title="ABCD 123",
            price=100.0,
            owner=owner,
            description=key,
            last_modified_date="2022-03-09"
        )
        if value is True:
            assert ret is True
        if value is False:
            assert ret is False
        # Delete our objects
        listing = Listing.objects(description=key)
        listing.delete()
        owner = User.objects(username="abcd123")
        owner.delete()


def test_r4_4_listing_create():
    '''
    Testing R4-4 in listing creation
    Requirement: the description has to be longer than the product's title
    '''
    test_cases = {
        ("A" * 20, "ABCD 123"): True,
        ("A" * 20, "A" * 21): False
    }
    for key, value in test_cases.items():
        name = key[1]
        description = key[0]
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        ret = create_listing(
            title=name,
            price=100.0,
            owner=owner,
            description=description,
            last_modified_date="2022-03-09"
        )
        if value is True:
            assert ret is True
        if value is False:
            assert ret is False
        # Delete our objects
        listing = Listing.objects(title=key)
        listing.delete()
        owner = User.objects(username="abcd123")
        owner.delete()


def test_r4_5_listing_create():
    '''
    Testing R4-5 in listing creation
    Requirement: the price has to be within the range 10, 10000
    '''
    test_cases = {
        0: False, 9.999: False, 10000.1: False,
        10: True, 99: True, 10000: True
    }
    for key, value in test_cases.items(): 
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        ret = create_listing(
            title="ABCD 123",
            price=key,
            owner=owner,
            description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            last_modified_date="2022-03-09"
        )
        if value is True:
            assert ret is True
        if value is False:
            assert ret is False
        # Delete our objects
        listing = Listing.objects(title="ABCD 123")
        listing.delete()
        owner = User.objects(username="abcd123")
        owner.delete()


def test_r4_6_listing_create():
    '''
    Testing R4-6 in listing creation
    Requirement: last_modified_date has to be after 2021-01-02 and
    before 2025-01-02
    '''
    test_cases = {
        "1970-01-01": False, "2025-01-03": False,
        "2021-01-02": True, "2022-01-01": True
    }
    for key, value in test_cases.items(): 
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        ret = create_listing(
            title="ABCD 123",
            price=100.0,
            owner=owner,
            description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            last_modified_date=key
        )
        if value is True:
            assert ret is True
        if value is False:
            assert ret is False
        # Delete our objects
        listing = Listing.objects(title="ABCD 123")
        listing.delete()
        owner = User.objects(username="abcd123")
        owner.delete()


def test_r4_7_listing_create():
    '''
    Testing R4-7 in listing creation
    Requirement: owner of the created listing must exist
    '''
    # Test case 1
    owner = User(
        id=1,
        username="abcd123",
        email="abcd@email.com",
        balance=100.0
    )
    owner.save()
    ret = create_listing(
        title="ABCD 123",
        price=100.0,
        owner=owner,
        description="ABCDEFGHIJKLMNOPQRSTUVQWXYZ",
        last_modified_date="2022-03-09"
    )
    assert ret is True 
    listing = Listing.objects(title="ABCD 123")
    listing.delete()
    

def test_r4_8_listing_create():
    '''
    Testing R4-8 in listing creation
    Requirement: users cannot create products that have the same title
    '''
    owner = User(
        id=1,
        username="abcd123",
        email="abcd@email.com",
        balance=100.0
    )
    owner.save()
    # Test case 1
    ret = create_listing(
        title="ABCD 123",
        price=100.0,
        owner=owner,
        description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        last_modified_date="2022-03-09"
    )
    assert ret is True
    # Test case 2
    ret = create_listing(
        title="ABCD 123",
        price=100.0,
        owner=owner.id,
        description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        last_modified_date="2022-03-09"
    )
    assert ret is False
    # Test case 3
    ret = create_listing(
        title="ABCD123",
        price=100.0,
        owner=owner,
        description="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        last_modified_date="2022-03-09"
    )
    assert ret is True
    # Delete all objects after we are done
    listing = Listing.objects(title="ABCD 123")
    listing.delete()
    listing = Listing.objects(title="ABCD123")
    listing.delete()
    owner = User.objects(username="abcd123")
    owner.delete()

