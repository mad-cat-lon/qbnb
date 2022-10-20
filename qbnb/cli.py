from qbnb.models import login, update_user, User


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

    org_email = user.email
    result = update_user(org_email, user_name, email, billing_address,
                         postal_code)

    if result is True:
        if email is not None:
            user = User.objects(email=email)
            user = user[0]     
        else:
            user = User.objects(email=org_email)
            user = user[0]   
        print("User profile updated.\n")
        return user
    else:
        print("Update failed.\n")
