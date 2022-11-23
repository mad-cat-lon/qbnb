"""
NoSql injection test for register function. The injection payload
used for testing is not the file provided in the assignment, because
our project uses non relational database instead of sql.
"""
from pathlib import Path
from qbnb.models import User, user_register
from qbnb import db
current_folder = Path(__file__).parent


def test_register_injection_email():
    """
    test case for injection in register function
    tested parameter: email
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    for text in input_file:
        try:
            user_register(text, "A123456a!", "test0user")
        except Exception as e:
            assert False
    user = User.objects(user_name='test0user')
    for i in user:
        i.delete()
    input_file.close()


def test_register_injection_password():
    """
    test case for injection in register function
    tested parameter: password
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    for text in input_file:
        try:
            user_register('test@test.com', text, "test0user")
        except Exception as e:
            assert False
    user = User.objects(user_name='test0user')
    for i in user:
        i.delete()
    input_file.close()


def test_register_injection_user_name():
    """
    test case for injection in register function
    tested parameter: user_name
    """
    input_file = open(current_folder.joinpath(
        "input.txt"))
    for text in input_file:
        try:
            user_register('test@test.com', "A123456!a", text)
        except Exception as e:
            assert False
    user = User.objects(password="A123456!a")
    for i in user:
        i.delete()
    input_file.close()