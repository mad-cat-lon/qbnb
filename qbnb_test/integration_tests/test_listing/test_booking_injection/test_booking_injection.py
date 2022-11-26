from pathlib import Path
from qbnb.models import Listing
from qbnb.models import User
from qbnb.functions import create_booking, create_listing
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
from datetime import datetime
from pytest import raises
current_folder = Path(__file__).parent


def test_injection_guest():
    """
    Injection for the parameter guest
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    user = User(user_name='user0', email='test@test.com', 
                password='A123456a!')
    user.save()
    user = User.objects(email='test@test.com')
    
    create_listing("title", 10, user[0], 
                   "This is a listing for testing",  
                   datetime.now().strftime("%Y-%m-%d")
                   )
    listing = Listing.objects(title='title')
    
    for text in input_file:
        try:
            create_booking(text, "2022-10-10", "2022-10-15", listing[0])
        except Exception as e:
            assert type(e) != NotRegistered
            assert type(e) != LookUpError
            assert type(e) != MultipleObjectsReturned
            assert type(e) != InvalidQueryError
            assert type(e) != OperationError
            assert type(e) != NotUniqueError
            assert type(e) != BulkWriteError
            assert type(e) != FieldDoesNotExist
            assert type(e) != SaveConditionError
    user[0].delete()
    listing[0].delete()


def test_injection_start_date():
    """
    Injection for the parameter start_date
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    user = User(user_name='user0', email='test@test.com', password='A123456a!')
    user.save()
    user = User.objects(email='test@test.com')
    
    guest = User(user_name='user0', email='test@test1.com', 
                 password='A123456a!')
    guest.save()
    guest = User.objects(email='test@test1.com')
    
    create_listing("title", 10, user[0], 
                   "This is a listing for testing", 
                   datetime.now().strftime("%Y-%m-%d")
                   )
    listing = Listing.objects(title='title')
    
    for text in input_file:
        try:
            create_booking(guest[0], text, "2022-10-15", listing[0])
        except Exception as e:
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

    user[0].delete()
    listing[0].delete()
    guest[0].delete()


def test_injection_end_date():
    """
    Injection for the parameter end_date
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    user = User(user_name='user0', email='test@test.com', 
                password='A123456a!')
    user.save()
    user = User.objects(email='test@test.com')
    
    guest = User(user_name='user0', email='test@test1.com', 
                 password='A123456a!')
    guest.save()
    guest = User.objects(email='test@test1.com')
    
    create_listing("title", 10, user[0], 
                   "This is a listing for testing", 
                   datetime.now().strftime("%Y-%m-%d")
                   )

    listing = Listing.objects(title='title')
    
    for text in input_file:
        try:
            create_booking(guest[0], "2022-10-10", text, listing[0])
        except Exception as e:
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

    user[0].delete()
    listing[0].delete()
    guest[0].delete()
    

def test_injection_listing():
    """
    Injection for the parameter listing
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    
    guest = User(user_name='user0', email='test@test1.com', 
                 password='A123456a!')
    guest.save()
    guest = User.objects(email='test@test1.com')
    
    for text in input_file:
        try:
            create_booking(guest[0], "2022-10-10", "2022-10-14", text)
        except Exception as e:
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

    guest[0].delete()