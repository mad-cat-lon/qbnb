from qbnb.models import user_register
from qbnb.functions import create_listing
from datetime import datetime
from qbnb.models import login, update_user, User


def user_home_page(user):
    """
    Displays user home page
    """
    print(f"{'='*10} USER HOME PAGE {'='*10}")
    print(
        "1. Update profile information\n\
         2. Create listing\n\
         3. Update listing\n\
         4. Exit"
    )
    while True:
        choice = input("Enter choice: ")
        if choice == "1":
            pass
        elif choice == "2":
            create_listing_page(user)
        elif choice == "3":
            pass
        elif choice == "4":
            break


def create_listing_page(user):
    """
    Creates listing given user input
    """
    print(f"{'='*10} CREATE A LISTING {'='*10}")
    while True:
        title = input("Enter title of listing: ")
        price = float(input("Enter price of listing: "))
        description = input("Enter description of listing: ")
        ret = create_listing(
            title=title,
            price=price,
            owner=user,
            description=description,
            last_modified_date=datetime.now().strftime("%Y-%m-%d")
        )
        if ret is True:
            print("Listing saved.")
            break

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
            updated_user = User.objects(email=email)
            updated_user = updated_user[0]     
        else:
            updated_user = User.objects(email=org_email)
            updated_user = updated_user[0]   
        print("User profile updated.\n")
        return updated_user
    else:
        print("Update failed.\n")
