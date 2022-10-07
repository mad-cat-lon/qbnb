import sys
sys.path.insert(1, "C:\\Users\\adlai\\Desktop\\CISC327\\qbnb\\qbnb\\")
from qbnb.models import user_register
from models import *
import requests
from mongoengine import *

def test_r1_1_user_register():
    '''
    Testing R1-1: Email cannot be empty. Password Cannot be empty.
    '''
    user0 = user_register("user1@gmail.com", "Password1!", "user1")
    user1 = user_register("", "", "user1")
    
    assert user0 is True
    assert user1 is False


def test_r1_2_user_register():
    '''
    Testing R1-2: A user is uniquely identified by his/her 
    user id - automatically generated.
    '''
    user = user_register("user1@gmail.com", "Password1", "user1")
    assert user._id is not None


def test_r1_3_user_register():
    '''
    Testing R1-3: The email has to follow addr-spec defined in 
    RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a 
    human-friendly explanation). You can use external libraries/imports.
    '''
    assert user_register("user0email", "Password1!", "user0") is False
    assert user_register("user1@gmail.com", "Password1!", "user2") is True


def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity: 
    minimum length 6, at least one upper case, at least one lower 
    case, and at least one special character.
    '''
    assert user_register("user0@email.comn", "Password1!", "user0") is True
    assert user_register("user1@gmail.com", "Pswd", "user1") is False
    assert user_register("user2@email.com", "password1!", "user2") is False
    assert user_register("user3@email.com", "PASSWORD1!", "user3") is False
    assert user_register("user4@gmail.com", "Password1", "user4") is False


def test_r1_5_user_register():
    '''
    Testing R1-5: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    '''
    assert user_register("user0@email", "Password1!", "user0") is True
    assert user_register("user1@gmail.com", "Password1!", "user2!") is False
    assert user_register("user2@email", "Password1!", " user0") is False
    assert user_register("user3@gmail.com", "Password1!", "user2 ") is False


def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.
    '''
    assert user_register("user0@email", "Password1!", "user0") is True
    assert user_register("user1@gmail.com", "Password1!", "u") is False
    assert user_register("user2@email", "Password1!", "usernamedextendedtwo2") is False


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''
    assert user_register('user0', 'user0@gmail.com', 'user0') is True
    assert user_register('user0', 'user1@gmail.com', 'user0') is True
    assert user_register('user1', 'user0@gmail.com', 'user0') is False


def test_r1_8_user_register():
    '''
    Testing R1-8: Shipping address is empty at the time of registration.
    '''
    user0 = user_register("user0@email", "Password1!", "user0")

    assert user0.billing_address == ""


def test_r1_9_user_register():
    '''
    Testing R1-9: Postal code is empty at the time of registration.
    '''
    user0 = user_register("user0@email", "Password1!", "user0")

    assert user0.postal_code == ""

def test_r1_10_user_register():
    '''
    Testing R1-10: Balance should be initialized as 100 at the 
    time of registration. (free $100 dollar signup bonus).
    '''
    user0 = user_register("user0@email", "Password1!", "user0")

    assert user0.balance == 100
