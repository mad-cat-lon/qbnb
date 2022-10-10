from qbnb.models import *
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
    url = "http://127.0.0.1:5000/listings/"
    for key, value in test_cases.items():
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0
        )
        owner.save()
        body = {
            "name": key,
            "description": "R4-1: ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
        }
        req = requests.post(url, json=body)
        # Delete objects we created
        owner = User.objects(username="abcd123")
        owner.delete()
        listing = Listing.objects(name=key)
        listing.delete()
        print(key, value)
        if req.status_code == 500:
            assert value is False
        elif req.status_code == 200:
            assert value is True

def test_r4_2_listing_create():
    '''
    Testing R4-2 in listing creation
    Requirement: the title of the listing can be no longer than 80 characters
    '''
    test_cases = {
        "A"*81: False,
        "AAAAAAAA": True
    }
    url = "http://127.0.0.1:5000/listings/"
    for key, value in test_cases.items():
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0)
        owner.save()
        body = {
            "name": key,
            "description": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
        }
        req = requests.post(url, json=body)
        # Delete objects we created
        owner = User.objects(username="abcd123")
        owner.delete()
        listing = Listing.objects(name=key)
        listing.delete()
        if req.status_code == 500:
            assert value is False
        elif req.status_code == 200:
            assert value is True
        

def test_r4_3_listing_create():
    '''
    Testing R4-3 in listing creation
    Requirement: the description of the product can be arbitrary characters,
    with a minimum length of 20 characters and a maximum of 2000
    '''
    test_cases = {
        "": False,
        "ABCD123": False,
        "*"*2001: False,
        "*"*1999: True
        }
    url = "http://127.0.0.1:5000/listings/"
    for key, value in test_cases.items():
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0)
        owner.save()
        body = {
            "name": "ABCD 123",
            "description": key,
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
        }
        req = requests.post(url, json=body)
        # Delete objects we created
        owner = User.objects(username="abcd123")
        owner.delete()
        listing = Listing.objects(name="ABCD 123")
        listing.delete()
        if req.status_code == 500:
            assert value is False
        elif req.status_code == 200:
            assert value is True


def test_r4_4_listing_create():
    '''
    Testing R4-4 in listing creation
    Requirement: the description has to be longer than the product's title
    '''
    test_cases = {
        ("A"*20, "ABCD 123"): True,
        ("A"*20, "A"*21): False
    }
    url = "http://127.0.0.1:5000/listings/"
    for key, value in test_cases.items():
        #print(key, value)
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0)
        owner.save()
        description = key[0]
        name = key[1]
        body = {
            "name": name,
            "description": description,
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
        }
        req = requests.post(url, json=body)
        # Delete objects we created
        owner = User.objects(username="abcd123")
        owner.delete()
        listing = Listing.objects(name=name)
        listing.delete()
        if req.status_code == 500:
            assert value is False
        elif req.status_code == 200:
            assert value is True


def test_r4_5_listing_create():
    '''
    Testing R4-5 in listing creation
    Requirement: the price has to be within the range 10, 10000
    '''
    test_cases = {
        0: False, 9.999: False, 10000.1: False,
        10: True, 99: True, 10000: True
    }
    url = "http://127.0.0.1:5000/listings/"
    for key, value in test_cases.items():
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0)
        owner.save()
        body = {
            "name": "ABCD 123",
            "description": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": key,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
        }
        req = requests.post(url, json=body)
        # Delete objects we created
        owner = User.objects(username="abcd123")
        owner.delete()
        listing = Listing.objects(name="ABCD 123")
        listing.delete()
        if req.status_code == 500:
            assert value is False
        elif req.status_code == 200:
            assert value is True


def test_r4_6_listing_create():
    '''
    Testing R4-6 in listing creation
    Requirement: last_modified_date has to be after 2021-01-02 and
    before 2025-01-02
    '''
    test_cases = {
        "1970-01-01": False, "2025-01-03": False,
        "2021-01-02": True, "2022-01-01": True}
    url = "http://127.0.0.1:5000/listings/"
    for key, value in test_cases.items():
        owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0)
        owner.save()
        body = {
            "name": "ABCD 123",
            "description": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": 100,
            "last_modified_date": key,
            "owner": owner.id
        }
        req = requests.post(url, json=body)
        # Delete objects we created
        owner = User.objects(username="abcd123")
        owner.delete()
        listing = Listing.objects(name="ABCD 123")
        listing.delete()
        if req.status_code == 500:
            assert value is False
        elif req.status_code == 200:
            assert value is True

def test_r4_7_listing_create():
    '''
    Testing R4-7 in listing creation
    Requirement: owner of the created listing must exist
    '''
    url = "http://127.0.0.1:5000/listings/"
    # Test case 1
    owner = User(
            id=1,
            username="abcd123",
            email="abcd@email.com",
            balance=100.0)
    owner.save()
    body = {
            "name": "ABCD 123",
            "description": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
    }
    req = requests.post(url, json=body)
    assert req.status_code == 200
    owner = User.objects(username="abcd123")
    owner.delete()
    listing = Listing.objects(name="ABCD 123")
    listing.delete()
    # Test case 2
    req = requests.post(url, json=body)
    listing = Listing.objects(name="ABCD 123")
    listing.delete()
    assert req.status_code == 500
    

def test_r4_8_listing_create():
    '''
    Testing R4-8 in listing creation
    Requirement: users cannot create products that have the same title
    '''
    url = "http://127.0.0.1:5000/listings/"
    owner = User(
                id=1,
                username="abcd123",
                email="abcd@email.com",
                balance=100.0)
    owner.save()
    # Test case 1
    body = {
            "name": "ABCD 123",
            "description": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
    }
    req = requests.post(url, json=body)
    assert req.status_code == 200
    # Test case 2
    req = requests.post(url, json=body)
    assert req.status_code == 500
    # Test case 3
    body = {
            "name": "ABCD123",
            "description": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "price": 100,
            "last_modified_date": "2022-03-09",
            "owner": owner.id
    }
    req = requests.post(url, json=body)
    assert req.status_code == 200
    # Delete all objects after we are done
    listing = Listing.objects(name="ABCD 123")
    listing.delete()
    listing = Listing.objects(name="ABCD123")
    listing.delete()
    owner = User.objects(username="abcd123")
    owner.delete()