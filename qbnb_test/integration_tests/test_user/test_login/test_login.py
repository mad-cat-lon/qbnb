"""
Testing for login function and its requirement
"""

from os import popen
import sys
from pathlib import Path
import subprocess
from qbnb.models import user_register
from qbnb.models import User
# get expected input/output file
current_folder = Path(__file__).parent


# read expected in/out
expected_in_both_invalid = open(current_folder.joinpath(
    'test_login_invalid_email_password.in'))
expected_in_invalid_email = open(current_folder.joinpath(
    'test_login_invalid_email.in'))
expected_in_invalid_password = open(current_folder.joinpath(
    'test_login_invalid_password.in'))
expected_in_valid = open(current_folder.joinpath(
    'test_login_valid.in'))

expected_out_invalid = open(current_folder.joinpath(
    'test_login_invalid.out')).read()
expected_out_valid = open(current_folder.joinpath(
    'test_login_valid.out')).read()


"""
    The below test case uses input partitioning method.
    It will cover the login requirement  R2-1 and R2-2.
    The input are divided into four part:
    1. invalid email,valid password
    2. valid email, invalid password
    3. valid email, valid passwrod
    4. invalid email, invalid password
"""


def test_login_invalid_email_password():
    """
    Input partition test for input with both invalid
    passowrd and email
    """

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_both_invalid,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    
    assert output.strip() == expected.strip()

  
def test_login_invalid_email():
    """
    Input partition test for input with only 
    invalid email and valid password
    """
    
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_invalid_email,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')

    assert output.strip() == expected.strip()
    
    user = User.objects(email='test0@test.com')
    user[0].delete()


def test_login_invalid_password():
    """
    Input partition test for input that has invalid
    password and valid email
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_invalid_password,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    
    assert output.strip() == expected.strip()

    user = User.objects(email='test0@test.com')
    user[0].delete()


def test_login_valid():
    """
    Input partition test for valid input.
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_valid,
        capture_output=True,
    ).stdout.decode()
    
    user = User.objects(email='test0@test.com')
    user[0].delete()
    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')

    assert output.strip() == expected.strip()


"""
The following test cases uses output partition to
test the login function. 
There are two possible output. The first happens when login
success. The second happens when login fails
"""


def test_login_output_valid():
    """
    Output partition method
    This test case cover output when login success
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    expected_in_valid = open(current_folder.joinpath(
        'test_login_valid.in'))
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_valid,
        capture_output=True,
    ).stdout.decode()
    
    user = User.objects(email='test0@test.com')
    user[0].delete()
    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')

    assert output.strip() == expected.strip()
    

def test_login_output_invalid():
    """
    Output partition method
    This test case cover output when login fail
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    expected_in_invalid_password = open(current_folder.joinpath(
        'test_login_invalid_password.in'))
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_invalid_password,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    
    assert output.strip() == expected.strip()

    user = User.objects(email='test0@test.com')
    user[0].delete()
