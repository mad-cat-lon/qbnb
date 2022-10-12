from qbnb.models import *
from mongoengine import *
from qbnb.models import *
from qbnb.functions import *
from mongoengine import *

def test_r1_1_user_register():
    '''
    Testing R1-1: Email cannot be empty. Password Cannot be empty.
    '''
    user0 = user_register("user11@gmail.com", "Password1!", "user1")
    user1 = user_register("", "", "user1")

    assert user0 is not None
    assert user1 is None
    
    user0.delete()


def test_r1_2_user_register():
    '''
    Testing R1-2: A user is uniquely identified by his/her 
    user id - automatically generated.
    '''
    user = user_register("user111S@gmail.com", "Password1!", "user1")

    assert user.id is not None
    user.delete()


def test_r1_3_user_register():
    '''
    Testing R1-3: The email has to follow addr-spec defined in 
    RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a 
    human-friendly explanation). You can use external libraries/imports.
    '''
    user0 = user_register("user000email", "Password1!", "user0")
    user1 = user_register("user1213@gmail.com", "Password1!", "user2")
    assert user0 is None
    assert user1 is not None

    user1.delete()


def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity: 
    minimum length 6, at least one upper case, at least one lower 
    case, and at least one special character.
    '''
    user0 = user_register("user031@email.comn", "Password1!", "user0")
    user1 = user_register("user112@gmail.com", "Pswd", "user1")
    user2 = user_register("user532@email.com", "password1!", "user2")
    user3 = user_register("user313@email.com", "PASSWORD1!", "user3")
    user4 = user_register("user24@gmail.com", "Password1", "user4")

    assert user0 is not None
    assert user1 is None
    assert user2 is None
    assert user3 is None
    assert user4 is None

    user0.delete()


def test_r1_5_user_register():
    '''
    Testing R1-5: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    '''
    user0 = user_register("user0412@email.com", "Password1!", "user0")
    user1 = user_register("user114@gmail.com", "Password1!", "user2!")
    user2 = user_register("user232@email.com", "Password1!", " user0")
    user3 = user_register("user353@gmail.com", "Password1!", "user2 ")

    assert user0 is not None
    assert user1 is None
    assert user2 is None
    assert user3 is None
    
    user0.delete()


def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.
    '''
    user0 = user_register("user140@email.com", "Password1!", "user0")
    user1 = user_register("user1124@gmail.com", "Password1!", "u")
    user2 = user_register(
        "u2142@email.com",
        "Password1!", 
        "usernamedextendedtwo2")

    assert user0 is not None
    assert user1 is None
    assert user2 is None

    user0.delete()


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''
    user0 = user_register('user0@gmail.com', 'Password1!', 'user0')
    user1 = user_register('user1@gmail.com', 'Password1!', 'user0')
    user2 = user_register('user0@gmail.com', 'Password1!', 'user1')

    assert user0 is not None
    assert user1 is not None
    assert user2 is None

    user0.delete()
    user1.delete()


def test_r1_8_user_register():
    '''
    Testing R1-8: Shipping address is empty at the time of registration.
    '''
    user0 = user_register("user55@email.com", "Password1!", "user0")

    assert user0.billing_address == ""

    user0.delete()


def test_r1_9_user_register():
    '''
    Testing R1-9: Postal code is empty at the time of registration.
    '''
    user0 = user_register("user66@email.com", "Password1!", "user0")

    assert user0.postal_code == ""

    user0.delete()


def test_r1_10_user_register():
    '''
    Testing R1-10: Balance should be initialized as 100 at the 
    time of registration. (free $100 dollar signup bonus).
    '''
    user0 = user_register("user255@email.com", "Password1!", "user0")

    assert user0.balance == 100

    user0.delete()


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

