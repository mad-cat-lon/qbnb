from qbnb.models import *
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
