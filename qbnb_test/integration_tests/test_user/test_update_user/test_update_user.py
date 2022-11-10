"""
Test cases for update user function frontend
"""
from os import popen
import sys
from pathlib import Path
import subprocess
from qbnb.models import user_register
from qbnb.models import User

# get expected input/output file
current_folder = Path(__file__).parent

expected_in_r3_1 = open(current_folder.joinpath(
    'test_update_user_r3_1.in'))

expected_in_r3_2_empty = open(current_folder.joinpath(
    'test_update_user_r3_2_empty.in'))

expected_in_r3_2_invalid = open(current_folder.joinpath(
    'test_update_user_r3_2_invalid.in'))

expected_in_r3_3 = open(current_folder.joinpath(
    'test_update_user_r3_3.in'))

expected_in_r3_4_empty = open(current_folder.joinpath(
    'test_update_user_r3_4_empty.in'))

expected_in_r3_4_invalid_char = open(current_folder.joinpath(
    'test_update_user_r3_4_invalid_char.in'))

expected_in_r3_4_invalid_length = open(current_folder.joinpath(
    'test_update_user_r3_4_invalid_length.in'))

expected_out_valid = open(current_folder.joinpath(
    'test_update_user_valid.out')).read()

expected_out_invalid = open(current_folder.joinpath(
    'test_update_user_invalid.out')).read()

"""
The below test cases uses requirement partition method
The test cases are made to cover each requirement specified for
the update_user function in Sprint 2. Some requirement are further
divided to test for different input.
"""


def test_r3_1_update_user():
    """
    Requirement partition
    This function test the requirement R3-1
    Assert password and balance are not changed
    Assert other attributes are changed
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_1,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')
    
    assert output.strip() == expected.strip()
    
    user = User.objects(email='newemail@test.com')
    user = user[0]
    
    assert user.password == 'Aa123456!'
    assert user.balance == 100.0
    assert user.postal_code == 'C1A 4A4'
    assert user.user_name == 'newTestName'
    assert user.billing_address == 'newaddress'
    user.delete()


def test_r3_2_empty_postal_update_user():
    """
    Requirement partition
    This function test the requirement R3-2 where postal code is empty
    The positive test case where the input is valid is covered in r3_1
    
    """ 
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    user = User.objects(email='test0@test.com')
    user = user[0]
    user.update(postal_code='C1A 4A4') 
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_2_empty,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')
    
    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')
    user = User.objects(email='test0@test.com')
    user = user[0]
    
    assert user.postal_code == 'C1A 4A4'
    assert output.strip() == expected.strip()
    user.delete()
    
    
def test_r3_2_invalid_postal_update_user():
    """
    Requirement partition
    This function test the requirement R3-2 where postal code 
    contain special character.
    The positive test case where the input is valid is covered in r3_1
    
    """ 
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    user = User.objects(email='test0@test.com')
    user = user[0]
    user.update(postal_code='C1A 4A4') 
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_2_invalid,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    user = User.objects(email='test0@test.com')
    user = user[0]

    assert user.postal_code == 'C1A 4A4'
    assert output.strip() == expected.strip()
    
    user.delete()


def test_r3_3_update_user():
    """    
    Requirement partition
    This function test the requirement R3-3 where postal code 
    should be a valid Canadian postal code
    The positive test case where the input is valid is covered in r3_1
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    user = User.objects(email='test0@test.com')
    user = user[0]
    user.update(postal_code='C1A 4A4') 
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_3,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    
    user = User.objects(email='test0@test.com')
    user = user[0]
    
    assert user.postal_code == 'C1A 4A4'
    assert output.strip() == expected.strip()
    
    user.delete()


def test_r3_4_update_user_empty():
    """
    Requirement partition
    This function test the requirement R3-4 where user name follow the 
    same requirement above. This function specificlly test for empty
    user name, and also user name with length<2
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_4_empty,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')
    
    user = User.objects(email='newemail@test.com')
    user = user[0]
    
    assert user.user_name == 'testuser'
    assert output.strip() == expected.strip()
    user.delete()


def test_r3_4_update_user_invalid_char():
    """
    Requirement partition
    This function test the requirement R3-4 where user name follow the 
    same requirement above. This function specificlly test for 
    user name with special character or spaces
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_4_invalid_char,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    
    user = User.objects(email='test0@test.com')
    user = user[0]
    
    assert user.user_name == 'testuser'
    assert output.strip() == expected.strip()
    user.delete()
    

def test_r3_4_update_user_invalid_len():
    """
    Requirement partition
    This function test the requirement R3-4 where user name follow the 
    same requirement above. This function specificlly test for 
    user name with length>20
    """
    user_register('test0@test.com', 'Aa123456!', 'testuser')
    
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r3_4_invalid_length,
        capture_output=True,
    ).stdout.decode()
    
    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')
    
    user = User.objects(email='test0@test.com')
    user = user[0]
    
    assert user.user_name == 'testuser'
    assert output.strip() == expected.strip()
    user.delete()