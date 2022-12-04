from os import popen
from pathlib import Path
import subprocess
from qbnb.models import User, Listing

# get expected input/output file
current_folder = Path(__file__).parent

# expected outputs
expected_output_valid = open(current_folder.joinpath(
    'expected_output_valid.out')).read()
expected_output_no_listing = open(current_folder.joinpath(
    'expected_output_no_listing.out')).read()
expected_output_own_listing = open(current_folder.joinpath(
    'expected_output_own_listing.out')).read() 
expected_output_balance = open(current_folder.joinpath(
    'expected_output_balance.out')).read()
expected_output_overlapped = open(current_folder.joinpath(
    'expected_output_overlapped.out')).read()


# Output Partition Testing inputs
expected_input_valid = open(current_folder.joinpath(
    'expected_input_valid.in'))
expected_input_no_listing = open(current_folder.joinpath(
    'expected_input_no_listing.in'))
expected_input_own_listing = open(current_folder.joinpath(
    'expected_input_own_listing.in'))
expected_input_balance = open(current_folder.joinpath(
    'expected_input_balance.in'))
expected_input_overlapped = open(current_folder.joinpath(
    'expected_input_overlapped.in'))
expected_input_defaults = open(current_folder.joinpath(
    'create_users_and_listing_for_tests.in'))


"""
Output partition testing
Testing book function for base valid and invalid cases.
Valid: Booking successful
Invalid: Booking unsuccessful
"""


def test_output_no_listings():
    """
    Output Partition
    Testing output for booking listing when no listings are available
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_no_listing,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_no_listing.replace('\r', '')

    assert output.strip() == expected.strip()


# create users and listing for testing
    subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_defaults,
        capture_output=True,
    ).stdout.decode()


def test_book_own_listing():
    """
    Output Partition
    Testing output for when the listing attempting to be booked is owned
    by the user
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_own_listing,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_own_listing.replace('\r', '')

    assert output.strip() == expected.strip()


def test_book_listing_output_valid():
    """
    Output Partition
    Testing output for successfully booked listing
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_valid,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_valid.replace('\r', '')

    assert output.strip() == expected.strip()


def test_book_overlapped_dates():
    """
    Output Partition
    Testing output for when the user chooses a date that overlaps with 
    previously booked dates for the same listing
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_overlapped,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_overlapped.replace('\r', '')

    assert output.strip() == expected.strip()


def test_book_balance_invalid():
    """
    Output Partition
    Testing output for when the user's balance is less than the listing price
    User can book listing even if balance is invalid
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_balance,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_balance.replace('\r', '')

    assert output.strip() == expected.strip()

    listing = Listing.objects(title="TestListing1")
    listing[0].delete()
    owner = User.objects(email="owner@gmail.com")
    owner[0].delete()
    renter = User.objects(email="renter@gmail.com")
    renter[0].delete()