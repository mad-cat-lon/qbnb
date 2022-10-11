"""
Test cases for the file models.py
"""
from flask_mongoengine import BaseQuerySet
from flask_mongoengine import QuerySet
from mongoengine import *
from flask_mongoengine import MongoEngine
from qbnb import app
from qbnb.models import login, update_user, User


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
