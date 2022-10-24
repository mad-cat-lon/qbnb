from qbnb.models import user_register
from qbnb.functions import create_listing
from datetime import datetime
from qbnb.models import login, update_user, User, Listing
from qbnb.models import update_listing


def user_home_page(user):
    """
    Displays user home page
    """
    print(f"{'='*10} USER HOME PAGE {'='*10}")
    print("1. Update profile information\n2. Create listing")
    print("3. Update listing\n4. Exit")
    while True:
        choice = input("Enter choice: ")
        if choice == "1":
            user = update_user_page(user)
        elif choice == "2":
            create_listing_page(user)
        elif choice == "3":
            listing_update_page(user)
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


def listing_update_page(user):
    listings = Listing.objects(owner=user)
    for index, listing in enumerate(listings):
        print(f"{index+1}. {listing.title}")
    choice = int(input("Please pick which listing you would like to edit: "))
    listing = None
    if choice < 1 or choice > len(listings):
        print("Invalid choice.")
        exit()
    else:
        listing = listings[choice - 1]
    new_title = input('Please enter new title: ')
    new_description = input('Please enter new description: ')
    new_price = float(input('Please enter new price: '))
    if new_title == "":
        new_title = None
    if new_description == "":
        new_description = None
    if new_price == 0:
        new_price = None
    push = update_listing(
        title=listing.title,
        new_title=new_title,
        description=new_description,
        price=listing.price,
        new_price=new_price,
        last_modified_date=datetime.now().strftime("%Y-%m-%d")
    )
    if push is True:
        print('Listing updated.')
    else:
        print("Could not update listing")
