from qbnb.models import user_register


def register_page():
    email = input('Please enter your email: ')
    user_name = input('Please enter your username: ')
    password = input('Please enter your password: ')
    password_verify = input('Please confirm your password: ')

    if password != password_verify:
        print("Please ensure both passwords are the same")
    elif user_register(email, password, user_name):
        print('User Registered')
    else:
        print('User registration failed.')
