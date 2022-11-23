from pathlib import Path
from qbnb.models import Listing
from qbnb.models import User
from mongoengine import ValidationError
from mongoengine import NotRegistered
from mongoengine import InvalidDocumentError
from mongoengine import LookUpError
from mongoengine import DoesNotExist
from mongoengine import MultipleObjectsReturned
from mongoengine import InvalidQueryError
from mongoengine import OperationError
from mongoengine import NotUniqueError
from mongoengine import BulkWriteError
from mongoengine import FieldDoesNotExist
from mongoengine import SaveConditionError
from pytest import raises
current_folder = Path(__file__).parent


def test_create_injection_title():
    """
    Test cases for listing creation NoSQL injection
    tested parameter: title
    """
    user = User.objects(email="create_inject@test.com")
    if len(user) == 0:
        user = User(
            email='create_inject@test.com',
            password='A123456a',
            user_name='create_inject',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    test_cases = open(current_folder.joinpath("test_title.txt"))
    for test_case in test_cases:
        # Should always return a ValidationError since all injections
        # will contain illegal characters
        with raises(
            ValidationError,
            match="Title of listing can only contain alphanumeric characters "
            "and spaces"
        ):
            listing = Listing(
                title=test_case,
                description="Default description for listing",
                price=100,
                owner=user,
                last_modified_date="2022-01-02"
            )
            listing.check()
            listing.save()
    listings = Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    User.objects(email='create_inject@test.com', password='A123456a').delete()


def test_create_injection_description():
    """
    Test cases for listing creation NoSQL injection
    tested parameter: description
    """
    user = User.objects(email="create_inject@test.com")
    if len(user) == 0:
        user = User(
            email='create_inject@test.com',
            password='A123456a',
            user_name='create_inject',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    test_cases = open(current_folder.joinpath("test_description.txt"))
    for test_case in test_cases:
        # Can contain arbitrary characters, so handle the following:
        # ValidationError, description too short
        # ValidationError, description too Long
        # MongoEngineException, description was executed as a command
        try:
            listing = Listing(
                title="Default title for listing",
                description=test_case,
                price=100,
                owner=user,
                last_modified_date="2022-01-02"
            )
            listing.check()
            listing.save()
        except Exception as e:
            # If any of these exceptions are thrown, we know that
            # the injection succeeded
            assert type(e) != NotRegistered
            assert type(e) != LookUpError
            assert type(e) != DoesNotExist
            assert type(e) != MultipleObjectsReturned
            assert type(e) != InvalidQueryError
            assert type(e) != OperationError
            assert type(e) != NotUniqueError
            assert type(e) != BulkWriteError
            assert type(e) != FieldDoesNotExist
            assert type(e) != SaveConditionError
            assert type(e) == ValidationError
    listings = Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    User.objects(email='create_inject@test.com', password='A123456a').delete()


def test_create_injection_price():
    """
    Test cases for listing creation NoSQL injection
    tested parameter: price
    """
    user = User.objects(email="create_inject@test.com")
    if len(user) == 0:
        user = User(
            email='create_inject@test.com',
            password='A123456a',
            user_name='create_inject',
            postal_code='',
            billing_address='',
            balance=100,
        )
        user.save()
    else:
        user = user[0]
    test_cases = open(current_folder.joinpath("test_price.txt"))
    for test_case in test_cases:
        # Should only return TypeError, as price is a FloatField()
        with raises(TypeError):
            listing = Listing(
                title="Default title for listing",
                description="Default description for listing",
                price=test_case,
                owner=user,
                last_modified_date="2022-01-02"
            )
            listing.check()
            listing.save()
    listings = Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    User.objects(email='create_inject@test.com', password='A123456a').delete()


def test_create_injection_last_modified_date():
    """
    Test cases for listing creation NoSQL injection
    tested parameter: last_modified_date
    """
    user = User.objects(email="create_inject@test.com")
    if len(user) == 0:
        user = User(
            email='create_inject@test.com',
            password='A123456a',
            user_name='create_inject',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    test_cases = open(current_folder.joinpath("test_last_modified_date.txt"))
    for test_case in test_cases:
        with raises(Exception) as e:
            listing = Listing(
                title="Default title for listing",
                description="Default description for listing",
                price=100,
                owner=user,
                last_modified_date=test_case
            )
            listing.check()
            listing.save()
        assert type(e) != NotRegistered
        assert type(e) != LookUpError
        assert type(e) != DoesNotExist
        assert type(e) != MultipleObjectsReturned
        assert type(e) != InvalidQueryError
        assert type(e) != OperationError
        assert type(e) != NotUniqueError
        assert type(e) != BulkWriteError
        assert type(e) != FieldDoesNotExist
        assert type(e) != SaveConditionError
    listings = Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    User.objects(email='create_inject@test.com', password='A123456a').delete()
