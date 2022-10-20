from qbnb.functions import create_listing
from datetime import datetime


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
