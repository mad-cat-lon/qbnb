from qbnb import models
from pathlib import Path
import subprocess


def test_r4_1_listing_create():
    """
    Input partitioning for R4-1
    test 1 - Invalid empty title
    test 2 - Invalid title with space as prefix
    test 3 - Invalid title with space as suffix
    test 4 - Invalid title with non-alphanumeric chararacters
    test 5 - Valid title with letters, numbers and spaces
    test 6 - Valid title with letters, numbers and consecutive inner spaces
    test 7 - Valid title with only numbers
    test 8 - Valid title with only letters
    """
    # Check if the test user has been created, stops one failed
    # test from making the next ones fail
    user = models.User.objects(email="r4@test.com")
    if len(user) == 0:
        user = models.User(
            email='r4@test.com',
            password='A123456a',
            user_name='r4',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    current_folder = Path(__file__).parent
    expected_in = open(current_folder / "test_r4_1.in")
    expected_out = open(current_folder / "test_r4_1.out").read()
    output = subprocess.run(
        ["python", "-m", "qbnb"],
        stdin=expected_in,
        capture_output=True,
        text=True
    ).stdout
    assert output.strip() == expected_out.strip()
    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_2_listing_create():
    """
    Input partitioning for R4-2
    test1 - Invalid title longer than 80 characters
    test2 - Valid title less than 80 characters
    test3 - Valid title with exactly 80 characters
    """
    # Check if the test user has been created, stops one failed
    # test from making the next ones fail
    user = models.User.objects(email="r4@test.com")
    if len(user) == 0:
        user = models.User(
            email='r4@test.com',
            password='A123456a',
            user_name='r4',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    current_folder = Path(__file__).parent
    expected_in = open(current_folder / "test_r4_2.in")
    expected_out = open(current_folder / "test_r4_2.out").read()
    output = subprocess.run(
        ["python", "-m", "qbnb"],
        stdin=expected_in,
        capture_output=True,
        text=True
    ).stdout
    assert output.strip() == expected_out.strip()
    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_3_listing_create():
    """
    Boundary testing for R4-3
    test1 - Invalid description less than 20 characters
    test2 - Invalid description more than 2000 characters
    test3 - Valid description with 20 characters
    test4 - Valid description with 2000 characters
    """
    # Check if the test user has been created, stops one failed
    # test from making the next ones fail
    user = models.User.objects(email="r4@test.com")
    if len(user) == 0:
        user = models.User(
            email='r4@test.com',
            password='A123456a',
            user_name='r4',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    current_folder = Path(__file__).parent
    expected_in = open(current_folder / "test_r4_3.in")
    expected_out = open(current_folder / "test_r4_3.out").read()
    output = subprocess.run(
        ["python", "-m", "qbnb"],
        stdin=expected_in,
        capture_output=True,
        text=True
    ).stdout
    assert output.strip() == expected_out.strip()
    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_4_listing_create():
    """
    Input partitioning for R4-4
    test1 - Invalid description is shorter than title
    test2 - Valid description is equal length to title
    test3 - Valid description is longer than title
    """
    # Check if the test user has been created, stops one failed
    # test from making the next ones fail
    user = models.User.objects(email="r4@test.com")
    if len(user) == 0:
        user = models.User(
            email='r4@test.com',
            password='A123456a',
            user_name='r4',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    current_folder = Path(__file__).parent
    expected_in = open(current_folder / "test_r4_4.in")
    expected_out = open(current_folder / "test_r4_4.out").read()
    output = subprocess.run(
        ["python", "-m", "qbnb"],
        stdin=expected_in,
        capture_output=True,
        text=True
    ).stdout
    assert output.strip() == expected_out.strip()
    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_5_listing_create():
    """
    Boundary testing for R4-5
    test1 - Invalid price of 9.99
    test2 - Invalid price of 10000.1
    test3 - Valid price of 10.0
    test4 - Valid price of 10000.0
    test5 - Valid price of 10.1
    test6 - Valid price of 9999.9
    """
    # Check if the test user has been created, stops one failed
    # test from making the next ones fail
    user = models.User.objects(email="r4@test.com")
    if len(user) == 0:
        user = models.User(
            email='r4@test.com',
            password='A123456a',
            user_name='r4',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    current_folder = Path(__file__).parent
    expected_in = open(current_folder / "test_r4_5.in")
    expected_out = open(current_folder / "test_r4_5.out").read()
    output = subprocess.run(
        ["python", "-m", "qbnb"],
        stdin=expected_in,
        capture_output=True,
        text=True
    ).stdout
    assert output.strip() == expected_out.strip()
    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_8_listing_create():
    """
    Output partitioning for R4-8
    test1 - Valid creation of listing
    test2 - Invalid creation of listing with same title
    """
    # Check if the test user has been created, stops one failed
    # test from making the next ones fail
    user = models.User.objects(email="r4@test.com")
    if len(user) == 0:
        user = models.User(
            email='r4@test.com',
            password='A123456a',
            user_name='r4',
            postal_code='',
            billing_address='',
            balance=100
        )
        user.save()
    else:
        user = user[0]
    current_folder = Path(__file__).parent
    expected_in = open(current_folder / "test_r4_8.in")
    expected_out = open(current_folder / "test_r4_8.out").read()
    output = subprocess.run(
        ["python", "-m", "qbnb"],
        stdin=expected_in,
        capture_output=True,
        text=True
    ).stdout
    assert output.strip() == expected_out.strip()
    listings = models.Listing.objects(owner=user)
    for listing in listings:
        listing.delete()
    models.User.objects(email='r4@test.com', password='A123456a').delete()
