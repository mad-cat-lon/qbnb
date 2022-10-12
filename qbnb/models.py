from qbnb import app
import re
from mongoengine import *
from flask_mongoengine import BaseQuerySet
from flask_mongoengine import MongoEngine
from mongoengine import Document
from mongoengine import ReferenceField
from mongoengine import BooleanField
from mongoengine import DateTimeField
from mongoengine import StringField
from mongoengine import FloatField
from mongoengine import IntField
from mongoengine import ValidationError
from mongoengine import ListField
import re
import datetime
from qbnb import app
db = MongoEngine(app)

"""
Base Booking class
user_id: id of the user booking the place
listing_id: id of the listing being booked
price: Price of listing
date: Date of the booking
"""


class Booking(db.Document):
    user_id = IntField(required=True)
    listing_id = IntField(required=True)
    price = FloatField(required=True)
    date = IntField(required=True)
    meta = {"queryset_class": BaseQuerySet}

    # String representation of booking
    def __repr__(self):
        return f"booking_start: {self.booking_start} \
            booking_end: {self.booking_end}"


"""
Base User class (data model)
email: Email of the user
password: Password of the user
user_name: Name of the user
billing_address: Billing address of the user
postal_code: Postal code of user
balance: Account balance of the user
"""


class User(db.Document):
    email = EmailField(required=True)
    password = StringField(required=True, primary_key=True)
    user_name = StringField(required=True)
    billing_address = StringField(required=True)
    postal_code = StringField(required=True)
    balance = FloatField(required=True)
   
    def __repr__(self):
        return f"username: {self.username} email: {self.email}"


"""
user registration function: Creates user in MongoDB.

Parameters
_email: User's email
_password: User's password
_user_name: User's username
_balance: Preset to 100

On initialization of flask, two user's are created 
After this no it returns to normal
"""


def user_register(_email, _password, _user_name, _balance=100):
    # Regex predefined for email format, spaces at start and end,
    # as well as an alphanumeric string
    special_characters = set('`~!@#$%^&*()_-=+\{\}\\|;:\'\",./?')
    regex_email_5322 = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    regex_spaces = r"^\S$|^\S[ \S]*\S$"
    regex_alphanumeric = r"^[a-zA-Z0-9 ]*$"
    if _email == '' or _password == '':
        return

    if not (re.fullmatch(regex_email_5322, _email)):
        return

    if (len(_password) < 6):
        return

    if (_password.lower() == _password):
        return
    
    if (_password.upper() == _password):
        return

    if not special_characters.intersection(_password):
        return

    if _user_name == '':
        return
    
    if not (re.fullmatch(regex_alphanumeric, _user_name)):
        return
    
    if not (re.fullmatch(regex_spaces, _user_name)):
        return

    if not len(_user_name) > 2 or not len(_user_name) < 20:
        return

    if (User.objects(email=_email)):
        return
    
    user = User(email=_email, password=_password, user_name=_user_name,
                billing_address='', postal_code='', balance=_balance)

    user.save()
    return user


"""
Description for each field:
reference: call base user class for user info
^to be changed later when user class is fully implemented^
bookingID: ID of booking made in booking class
date = date of transaction made
time = time of transaction made
amount = amount paid at transaction
trans_start = start of transaction process
trans_end = end of transaction process
"""


class Transaction(Document):
    reference = ReferenceField(User)
    bookingID = StringField(required=True)
    date = StringField(required=True)
    time = StringField(required=True)
    amount = IntField(min_value=0, max_value=None, required=True)
    trans_start = StringField(required=True)
    trans_end = StringField(required=True)

    # Function for representating the start and end to the transaction
    def __repr__(self):
        return f"transaction_start: {self.trans_start} \
            transaction_end: {self.trans_end}"


"""
Base Listing class
title: Name of the listing
images: Array of embedded images
price: Price of the listing
host: User object representing the host
reviews: Array of Review objects
booked: Boolean value representing if the listing
        is booked
requested_bookings: Array of requested Booking
        objects
current_booking: the current booking
"""


class Listing(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    price = FloatField(required=True)
    last_modified_date = IntField(required=True)
    owner_id = IntField(required=True)
    meta = {"queryset_class": BaseQuerySet}

    def check(self):
        '''
        Checks to see if created Listing object conforms to requirements
        and raises a ValidationError if it does not
        '''
        # R4-1
        valid_title_regex = "^[1-9A-Za-z][1-9A-Za-z ]*[1-9A-Za-z]$"
        if re.search(valid_title_regex, self.title) is None:
            raise ValidationError(
                "Name of listing can only contain"
                "alphanumeric characters and spaces")
                             
        # R4-2
        if len(self.title) > 80:
            raise ValidationError("Name of listing is too long")

        # R4-3
        if len(self.description) < 20 or len(self.description) > 2000:
            raise ValidationError(
                "Description must be between 20 to"
                "2000 characters")

        # R4-4
        if len(self.description) < len(self.title):
            raise ValidationError("Description must be longer than title")
       
        # R4-5
        if self.price < 10 or self.price > 10000:
            raise ValidationError("Price must be between 10 and 10000")

        # R4-6
        last_modified_date = datetime.datetime.strptime(
            self.last_modified_date, "%Y-%m-%d").date()
        if (last_modified_date < datetime.date(2021, 1, 2) or
                last_modified_date > datetime.date(2025, 1, 2)):
            raise ValidationError("Invalid modification date")

        # R4-7
        if self.owner is None:
            raise ValidationError("Cannot create listing without owner")
       
        # R4-8
        listings = Listing.objects(title=self.title, owner=self.owner.id)
        print(listings)
        if len(listings) != 0:
            raise ValidationError("Cannot create listing with same title")
               
    # String representation of Listing
    def __repr__(self):
        return f"title: {self.title} price: {self.price}"


"""
Base Listing class
user_id: id of the user who gave the review
listing_id: id of the listing being reviewed
review_text: Content of review
date: Date of the review
"""


class Review(Document):
    user_id = IntField(required=True)
    listing_id = IntField(required=True)
    review_text = StringField(required=True)
    date = IntField(required=True)

    def __repr__(self):
        return f"user: {self.user_id} reviewed listing: {self.listing_id}"


def login(email, password):
    """
    Function for user login, allow user to login using
    email and pass word.

    Parameter:
    email: string, email of user
    password: string pass owrd of user

    Return:
    user object if succeed, False other wise

    """
    # regular expression to check email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email == '' or password == '':
        return False

    if not (re.fullmatch(regex, email)):
        return False

    if len(password) < 6:
        return False

    if len(re.findall('[^A-Za-z0-9]', password)) != 0:
        return False

    if re.search('[A-Z]', password) is None:
        return False

    if re.search('[a-z]', password) is None:
        return False

    valid = User.objects(email=email, password=password)
    if valid is None:
        return False

    if len(valid) != 1:
        return False

    return valid[0]


def update_user(org_email, user_name, new_email,
                billing_address, postal_code):
    """
    Function for updating user profile. The user with the org_email will 
    be updated. If parameter is None, then it is not changed

    Parameter
    org_email: string, email of the user being updated
    user_name: string, new user name, can be None
    new_email: string, new email address, can be None
    billling_address: string, new billing address, can be None
    postal_code: string, new postal code, can be None

    """
    user = User.objects(email=org_email)
    if len(user) != 1:
        return False
    else:
        user = user[0]

    if user_name is not None:
        if len(user_name) > 20 or len(user_name) < 2:
            return False
        if user_name[0] == ' ' or user_name[-1] == ' ':
            return False
        for i in user_name:
            if not (i.isalnum() or i == ' '):
                return False
        user.update(user_name=user_name)
        user.reload()

    if postal_code is not None:
        postal_reg = r'[A-Z]{1}[0-9]{1}[A-Z]{1}\s{1}[0-9]{1}[A-Z]{1}[0-9]{1}'
        postal_code = postal_code.upper()
        if len(postal_code) != 7:
            return False
        if len(re.findall(postal_reg, postal_code)) != 1:
            return False
        user.update(postal_code=postal_code)
        user.reload()

    if new_email is not None:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, new_email)):
            return False
        unique = User.objects(email=new_email)
        if len(unique) != 0:
            return False
        user.update(email=new_email)
        user.reload()

    if billing_address is not None:
        user.update(billing_address=billing_address)
        user.reload()

    return True


"""
Base Listing class
user_id: id of the user who gave the review
listing_id: id of the listing being reviewed
review_text: Content of review
date: Date of the review
"""


class Review(Document):
    user_id = IntField(required=True)
    listing_id = IntField(required=True)
    review_text = StringField(required=True)
    date = IntField(required=True)

    def __repr__(self):
        return f"user: {self.user_id} reviewed listing: {self.listing_id}"


def login(email, password):
    """
    Function for user login, allow user to login using
    email and pass word.

    Parameter:
    email: string, email of user
    password: string pass owrd of user

    Return:
    user object if succeed, False other wise

    """
    # regular expression to check email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if email == '' or password == '':
        return False

    if not (re.fullmatch(regex, email)):
        return False

    if len(password) < 6:
        return False

    if len(re.findall('[^A-Za-z0-9]', password)) != 0:
        return False

    if re.search('[A-Z]', password) is None:
        return False

    if re.search('[a-z]', password) is None:
        return False

    valid = User.objects(email=email, password=password)
    if valid is None:
        return False

    if len(valid) != 1:
        return False

    return valid[0]


def update_user(org_email, user_name, new_email,
                billing_address, postal_code):
    """
    Function for updating user profile. The user with the org_email will 
    be updated. If parameter is None, then it is not changed

    Parameter
    org_email: string, email of the user being updated
    user_name: string, new user name, can be None
    new_email: string, new email address, can be None
    billling_address: string, new billing address, can be None
    postal_code: string, new postal code, can be None

    """
    user = User.objects(email=org_email)
    if len(user) != 1:
        return False
    else:
        user = user[0]

    if user_name is not None:
        if len(user_name) > 20 or len(user_name) < 2:
            return False
        if user_name[0] == ' ' or user_name[-1] == ' ':
            return False
        for i in user_name:
            if not (i.isalnum() or i == ' '):
                return False
        user.update(user_name=user_name)
        user.reload()

    if postal_code is not None:
        postal_reg = r'[A-Z]{1}[0-9]{1}[A-Z]{1}\s{1}[0-9]{1}[A-Z]{1}[0-9]{1}'
        postal_code = postal_code.upper()
        if len(postal_code) != 7:
            return False
        if len(re.findall(postal_reg, postal_code)) != 1:
            return False
        user.update(postal_code=postal_code)
        user.reload()

    if new_email is not None:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, new_email)):
            return False
        unique = User.objects(email=new_email)
        if len(unique) != 0:
            return False
        user.update(email=new_email)
        user.reload()

    if billing_address is not None:
        user.update(billing_address=billing_address)
        user.reload()

    return True
