from qbnb.models import *
from mongoengine import *
from qbnb.models import *
from qbnb.functions import *
from mongoengine import *
from mongoengine import *
from qbnb import app
from qbnb.models import update_listing, Listing
import datetime


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


def test_r2_1_login():
    """
    Testing R2-1: A user can log in using her/his email address 
      and the password.

    """
    user = User(email='test0@test.com', password='A123456a',
                user_name='u0', postal_code='',
                billing_address='', balance=100)
    user.save()
    user = login('test0@test.com', 'A123456a')
    dne_user = login('test@test.com', '123456Aa')
    assert user is not False
    assert user.email == "test0@test.com"
    assert dne_user is False
    user.delete()


def test_r2_2_login():
    """
    Testing for R2-2:The login function should check if the
    supplied inputs meet the same email/ password requirements
    as above, before checking the database. 
    """
    user = User(email='test0@test.com', password='A123456a',
                user_name='u0', postal_code='',
                billing_address='', balance=100)
    user.save()
    user = login('test0@test.com', '123456a')
    # if login does not check before the search, it would return True
    assert user is False
    User.objects(email='test0@test.com', password='A123456a').delete()


def test_r3_1_update_user():
    """
    Testing for R3-1:TA user is only able to update his/her 
    user name, user email, billing address, and postal code.
    """
    user = User(email='test0@test.com', password='A123456a',
                user_name='u0', postal_code='',
                billing_address='', balance=100)
    user.save()
    result = update_user('test0@test.com', 'newname', 'newemail@test.com',
                         'address', 'C1A 5A4')
    user = User.objects(email='newemail@test.com')
    user = user[0]
    assert result is not False
    assert user.email == "newemail@test.com"
    assert user.user_name == 'newname'
    assert user.billing_address == 'address'
    assert user.postal_code == 'C1A 5A4'
    assert user.password == 'A123456a'
    assert user.balance == 100
    user.delete()


def test_r3_2_update_user():
    """
    Testing for R3-2: postal code should be non-empty,
    alphanumeric-only, and no special characters such as !.
    """
    user = User(email='test0@test.com', password='A123456a',
                user_name='u0', postal_code='',
                billing_address='', balance=100)
    user.save()
    user = User.objects(email='test0@test.com')
    result = update_user('test0@test.com', None, None, None, 'C1A 5A4')
    invalid_result_1 = update_user('test0@test.com', None, None, None, '')
    invalid_result_2 = update_user('test0@test.com', None, None,
                                   None, 'C/A 4!5')
    assert result is True
    assert invalid_result_1 is False
    assert invalid_result_2 is False
    assert user[0].postal_code == 'C1A 5A4'
    user[0].delete()


def test_r3_3_update_user():
    """
    Test for R3-3: Postal code has to be a valid Canadian postal code.
    """
    user = User(email='test0@test.com', password='A123456a',
                user_name='u0', postal_code='',
                billing_address='', balance=100)
    user.save()
    user = User.objects(email='test0@test.com')
    result = update_user('test0@test.com', None, None, None, 'C1A 5A4')
    invalid_result_1 = update_user('test0@test.com', None,
                                   None, None, 'C11 5Aa')
    assert result is True
    assert invalid_result_1 is False
    assert user[0].postal_code == 'C1A 5A4'
    user[0].delete()


def test_r3_4_update_user():
    """
    Test for user name following the guideline
    """
    user = User(email='test0@test.com', password='A123456a',
                user_name='u0', postal_code='',
                billing_address='', balance=100)
    user.save()
    user = User.objects(email='test0@test.com')
    result = update_user('test0@test.com', 'test User1', None, None, None)
    invalid_result_1 = update_user('test0@test.com', '', None, None, None)
    invalid_result_2 = update_user('test0@test.com', 'a1-', None, None, None)
    invalid_result_3 = update_user('test0@test.com', ' a', None, None, None)
    invalid_result_4 = update_user('test0@test.com', 'a ', None, None, None)
    assert result is True
    assert user[0].user_name == 'test User1'
    assert invalid_result_1 is False
    assert invalid_result_2 is False
    assert invalid_result_3 is False
    assert invalid_result_4 is False
    assert user[0].user_name == 'test User1'
    user[0].delete()

    
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
            user_name="abcd123",
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
        owner = User.objects(user_name="abcd123")
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
            user_name="abcd123",
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
        owner = User.objects(user_name="abcd123")
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
            user_name="abcd123",
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
        owner = User.objects(user_name="abcd123")
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
            user_name="abcd123",
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
        owner = User.objects(user_name="abcd123")
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
            user_name="abcd123",
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
        owner = User.objects(user_name="abcd123")
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
            user_name="abcd123",
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
        owner = User.objects(user_name="abcd123")
        owner.delete()


def test_r4_7_listing_create():
    '''
    Testing R4-7 in listing creation
    Requirement: owner of the created listing must exist
    '''
    # Test case 1
    owner = User(
        user_name="abcd123",
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
    owner = User.objects(user_name="abcd123")
    owner.delete()
    

def test_r4_8_listing_create():
    '''
    Testing R4-8 in listing creation
    Requirement: users cannot create products that have the same title
    '''
    owner = User(
        user_name="abcd123",
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
    owner = User.objects(user_name="abcd123")
    owner.delete()


def test_r5_1_update_listing():
    """
    Testing for R5-1: admin is able to update all attributes
        of the listing, except owner_id and last_modified_date.
    """
    listing = Listing(title='Beverly Hills Inn',
                      description='Luxury suite with sea view.',
                      price=2000,
                      last_modified_date="2022-03-09",
                      owner_id=1234)
    listing.save()
    result = update_listing('Beverly Hills Inn', 'Beverly Hills Mansion',
                            'Luxury suite with sea view. Test', 2000, 2000,
                            "2022-03-08")
    listing = Listing.objects(title='Beverly Hills Mansion')
    assert result is not False
    listing = listing[0]
    assert listing.price == 2000
    assert listing.title == 'Beverly Hills Mansion'
    assert listing.description == 'Luxury suite with sea view. Test'
    time = datetime.datetime.strptime("2022-03-08", "%Y-%m-%d").date()
    assert listing.last_modified_date.date() == time
    listing.delete()


def test_r5_2_update_listing():
    """
    Testing for R5-2: admin is only able to increase price.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view.',
        price=2000, last_modified_date="2022-03-09", owner_id=123)
    listing.save()
    listing = Listing.objects(title='Beverly Hills Inn')
    result = update_listing('Beverly Hills Inn', None,
                            'Luxury suite with sea view.',
                            2000, 2300, None)
    invalid_result = update_listing('Beverly Hills Inn', None,
                                    'Luxury suite with sea view.',
                                    2000, 1900, None)
    assert result is True
    assert invalid_result is False
    assert listing[0].price == 2300
    listing[0].delete()


def test_r5_3_update_listing():
    """
    Testing for R5-3: last_modified_date can only be updated\
         when the update operation is successful.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view.',
        price=2000, last_modified_date="2022-03-09", owner_id=123)
    listing.save()
    listing = Listing.objects(title='Beverly Hills Inn')
    result = update_listing('Beverly Hills Inn', None,
                            'Luxury suite with sea view.',
                            2000, 2300, "2022-03-10")
    invalid_result = update_listing('Beverly Hills Inn', None,
                                    'Luxury suite with sea view.',
                                    2000, 1900, "2022-03-11")
    assert result is True
    assert invalid_result is False
    time = datetime.datetime.strptime("2022-03-10", "%Y-%m-%d").date()
    assert listing[0].last_modified_date.date() == time
    listing[0].delete()


def test_r5_4_update_listing():
    """
    Testing for R5-4: test for whether attributes follow the same\
        requirements.
    """
    listing = Listing(
        title='Beverly Hills Inn', description='Luxury suite with sea view.',
        price=2000, last_modified_date="2022-03-10", owner_id=123)
    listing.save()
    result = update_listing('Beverly Hills Inn', 'Beverly Hills Mansion',
                            'Luxury suite with sea view. Test', 2000, 2300,
                            "2022-03-11")
    invalid_result_1 = update_listing('Beverly Hills Inn', None, 'nice', 2000,
                                      2300, None)
    invalid_result_2 = update_listing('Beverly! Hills Inn',
                                      'Beverly Hills Mansion',
                                      'Luxury suite with sea view. Test',
                                      2000, 2300, None)
    listing = Listing.objects(title='Beverly Hills Mansion')
    listing = listing[0]
    assert result is True
    assert invalid_result_1 is False
    assert invalid_result_2 is False
    assert listing.title == 'Beverly Hills Mansion'
    listing.delete()