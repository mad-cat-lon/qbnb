"""
Testing for listing updates and its requiremetns
"""

import subprocess
import sys
from os import popen
from pathlib import Path

from qbnb import models
from qbnb import functions

"""
Requirements for update listing:
R5-1: One can update all attributes of the listing, except owner_id and
        last_modified_date.
R5-2: Price can be only increased but cannot be decreased :)
R5-3: last_modified_date should be updated when the update operation is
        successful.
R5-4: When updating an attribute, one has to make sure that it follows the
        same requirements as above.
"""

# get expected input/output file
current_folder = Path(__file__).parent

# input test cases
expected_in_r5_1 = open(current_folder.joinpath(
    'test_r5_1.in'))
expected_in_r5_2_valid = open(current_folder.joinpath(
    'test_r5_2.in'))
expected_in_r5_2_invalid = open(current_folder.joinpath(
    'test_r5_2_invalid.in'))
"""
r5_3 will not be tested here since it is tested in the backend and the last
modified date is not visible to the user on the frontend CLI.
"""
expected_in_r5_4_valid = open(current_folder.joinpath(
    'test_r5_4.in'))
expected_in_r5_4_invalid_title = open(current_folder.joinpath(
    'test_r5_4_invalid_title.in'))
expected_in_r5_4_invalid_description = open(current_folder.joinpath(
    'test_r5_4_invalid_description.in'))
expected_in_r5_4_invalid_price = open(current_folder.joinpath(
    'test_r5_4_invalid_price.in'))

# expected outputs
expected_out_valid = open(current_folder.joinpath(
    'test_update_listing_valid.out')).read()
expected_out_invalid = open(current_folder.joinpath(
    'test_update_listing_invalid.out')).read()


def test_r5_1_valid():
    """
    Input partition test for input with invalid attributes of the listing
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_1,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()


def test_r5_2_valid():
    """
    Input partition test for valid price change
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_2_valid,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()


def test_r5_2_invalid():
    """
    Input partition test for invalid price change
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_2_invalid,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()


def test_r5_4_valid():
    """
    Input partition test for valid attribute change
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_4_valid,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_valid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()


def test_r5_4_invalid_title():
    """
    Input partition test for invalid attribute change
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_4_invalid_title,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()


def test_r5_4_invalid_description():
    """
    Input partition test for invalid attribute change
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_4_invalid_description,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()


def test_r5_4_invalid_price():
    """
    Input partition test for invalid attribute change
    """
    user = models.User.objects(email="tester@email.com")
    if len(user) == 0:
        user = models.User(
            email='tester@email.com',
            password='Tester@12345',
            user_name='tester',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]

    Listing = models.Listing.objects(title="test listing")
    if len(Listing) == 0:
        Listing = models.Listing(
            title="test listing",
            price=1000,
            owner=user,
            description="test listing description",
            last_modified_date='2020-12-01'
        )
        Listing.save()

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r5_4_invalid_price,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_out_invalid.replace('\r', '')

    assert output.strip() == expected.strip()

    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(
        email='tester@email.com', password='Tester@12345').delete()
