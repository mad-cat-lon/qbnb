from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# expected input and output
expected_input_2 = open(current_folder.joinpath('test_r1_2.in'))
expected_output_2 = open(current_folder.joinpath('test_register_valid.out')).read()

expected_input_3 = open(current_folder.joinpath('test_r1_3.in'))
expected_output_3 = open(current_folder.joinpath('test_register_invalid.out')).read()

expected_input_4 = open(current_folder.joinpath('test_r1_4.in'))
expected_output_4 = open(current_folder.joinpath('test_register_invalid.out')).read()

expected_input_5 = open(current_folder.joinpath('test_r1_5.in'))
expected_output_5 = open(current_folder.joinpath('test_register_invalid.out')).read()

expected_input_6 = open(current_folder.joinpath('test_r1_6.in'))
expected_output_6 = open(current_folder.joinpath('test_register_invalid.out')).read()

expected_input_7 = open(current_folder.joinpath('test_r1_7.in'))
expected_output_7 = open(current_folder.joinpath('test_register_invalid.out')).read()

""" 
Input Partition Testing
    Partitioned into the 10 requirements

    keep in mind this may be the wrong type of testing, I either need to vary 
    the black box testing methods, or I need to add valid/invalid test cases for each
"""

def test_r1_2_user_register():
    '''
    Testing R1-2: A user is uniquely identified by his/her 
    user id - automatically generated.
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_2,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_2.replace('\r', '')

    assert output.strip() == expected.strip()


def test_r1_3_user_register():
    '''
    Testing R1-3: The email has to follow addr-spec defined in 
    RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a 
    human-friendly explanation). You can use external libraries/imports.
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_3,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_3.replace('\r', '')

    assert output.strip() == expected.strip()


def test_r1_4_user_register():
    '''
    Testing R1-4: Password has to meet the required complexity: 
    minimum length 6, at least one upper case, at least one lower 
    case, and at least one special character.
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_4,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_4.replace('\r', '')

    assert output.strip() == expected.strip()


def test_r1_5_user_register():
    '''
    Testing R1-5: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_5,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_5.replace('\r', '')

    assert output.strip() == expected.strip()


def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_6,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_6.replace('\r', '')

    assert output.strip() == expected.strip()


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_7,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_7.replace('\r', '')

    assert output.strip() == expected.strip()
