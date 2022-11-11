from qbnb import models
from pathlib import Path
import subprocess


def test_r4_1_listing_create():
    """
    Input partitioning for R4-1
    test1 - Invalid empty title
    test2 - Invalid title with space as prefix
    test3 - Invalid title with space as suffix
    test4 - Invalid title with non-alphanumeric chararacters
    test5 - Valid title that conforms to r4-1
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
    test_dir = current_folder / "r4_1"
    expected_in_files = [x for x in test_dir.glob("*.in")]
    expected_out_files = [x for x in test_dir.glob("*.out")]
    test_cases = dict(zip(expected_in_files, expected_out_files))
    failures = []
    for in_file, out_file in test_cases.items():
        expected_in = open(in_file)
        expected_out = open(out_file).read()
        output = subprocess.run(
            ["python", "-m", "qbnb"],
            stdin=expected_in,
            capture_output=True,
            text=True
        ).stdout
        # Delete created listing
        listing = models.Listing.objects(owner=user)
        listing.delete()
        if output.strip() != expected_out.strip():
            failures.append(in_file.name)
    assert failures == []
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_2_listing_create():
    """
    Input partitioning for R4-2
    test1 - Invalid title longer than 80 characters
    test2 - Valid title less than 80 characters
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
    test_dir = current_folder / "r4_2"
    expected_in_files = [x for x in test_dir.glob("*.in")]
    expected_out_files = [x for x in test_dir.glob("*.out")]
    test_cases = dict(zip(expected_in_files, expected_out_files))
    failures = []
    for in_file, out_file in test_cases.items():
        expected_in = open(in_file)
        expected_out = open(out_file).read()
        output = subprocess.run(
            ["python", "-m", "qbnb"],
            stdin=expected_in,
            capture_output=True,
            text=True
        ).stdout
        # Delete created listing
        listing = models.Listing.objects(owner=user)
        listing.delete()
        if output.strip() != expected_out.strip():
            failures.append(in_file.name)
    assert failures == []
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
    test_dir = current_folder / "r4_3"
    expected_in_files = [x for x in test_dir.glob("*.in")]
    expected_out_files = [x for x in test_dir.glob("*.out")]
    test_cases = dict(zip(expected_in_files, expected_out_files))
    failures = []
    for in_file, out_file in test_cases.items():
        expected_in = open(in_file)
        expected_out = open(out_file).read()
        output = subprocess.run(
            ["python", "-m", "qbnb"],
            stdin=expected_in,
            capture_output=True,
            text=True
        ).stdout
        # Delete created listing
        listing = models.Listing.objects(owner=user)
        listing.delete()
        if output.strip() != expected_out.strip():
            failures.append(in_file.name)
    assert failures == []
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_4_liting_create():
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
    test_dir = current_folder / "r4_4"
    expected_in_files = [x for x in test_dir.glob("*.in")]
    expected_out_files = [x for x in test_dir.glob("*.out")]
    test_cases = dict(zip(expected_in_files, expected_out_files))
    failures = []
    for in_file, out_file in test_cases.items():
        expected_in = open(in_file)
        expected_out = open(out_file).read()
        output = subprocess.run(
            ["python", "-m", "qbnb"],
            stdin=expected_in,
            capture_output=True,
            text=True
        ).stdout
        # Delete created listing
        listing = models.Listing.objects(owner=user)
        listing.delete()
        if output.strip() != expected_out.strip():
            failures.append(in_file.name)
    assert failures == []
    models.User.objects(email='r4@test.com', password='A123456a').delete()


def test_r4_5_listing_create():
    """
    Boundary testing for R4-5
    test1 - Invalid price of 9.99
    test2 - Invalid price of 10000.1
    test3 - Valid price of 10.0
    test4 - Valid price of 10000.0
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
    test_dir = current_folder / "r4_5"
    expected_in_files = [x for x in test_dir.glob("*.in")]
    expected_out_files = [x for x in test_dir.glob("*.out")]
    test_cases = dict(zip(expected_in_files, expected_out_files))
    failures = []
    for in_file, out_file in test_cases.items():
        expected_in = open(in_file)
        expected_out = open(out_file).read()
        output = subprocess.run(
            ["python", "-m", "qbnb"],
            stdin=expected_in,
            capture_output=True,
            text=True
        ).stdout
        # Delete created listing
        listing = models.Listing.objects(owner=user)
        listing.delete()
        if output.strip() != expected_out.strip():
            failures.append(in_file.name)
    assert failures == []
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
    test_dir = current_folder / "r4_8"
    expected_in_files = [x for x in test_dir.glob("*.in")]
    expected_out_files = [x for x in test_dir.glob("*.out")]
    test_cases = dict(zip(expected_in_files, expected_out_files))
    failures = []
    for in_file, out_file in test_cases.items():
        expected_in = open(in_file)
        expected_out = open(out_file).read()
        output = subprocess.run(
            ["python", "-m", "qbnb"],
            stdin=expected_in,
            capture_output=True,
            text=True
        ).stdout
        if output.strip() != expected_out.strip():
            failures.append(in_file.name)
    # Delete created listing in first case
    listing = models.Listing.objects(owner=user)
    listing.delete()
    assert failures == []
    models.User.objects(email='r4@test.com', password='A123456a').delete()
