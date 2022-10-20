from qbnb.models import login, update_user


def login_page():
    """
    Function for the user login page. Allow user to login
    to their account using email and password
    """
    email = input('Please enter email: ')
    password = input('Please enter password: ')
    return login(email, password)


def update_user_page(user):
    """
    Function for the user profile update page. Allow user to update their
    profile using command line input.

    Parameter: user, User object, curret loggedin user
    """
    print('Enter the updated user profile, press enter if no change is needed')
    user_name = input("Enter new user name: ")
    email = input("Enter new email: ")
    billing_address = input("Enter new billing address: ")
    postal_code = input("Enter new postal code:")

    if user_name == '':
        user_name = None
    if email == '':
        email = None
    if billing_address == '':
        billing_address = None
    if postal_code == '':
        postal_code = None

    result = update_user(user.email, user_name, email, billing_address, postal_code)
    if result == True:
        print("User profile updated.")
    else:
        print("Update failed.")
