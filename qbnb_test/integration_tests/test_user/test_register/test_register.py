from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# expected outputs
expected_output_invalid = open(current_folder.joinpath(
    'test_register_invalid.out')).read()
expected_output_valid = open(current_folder.joinpath(
    'test_register_valid.out')).read()
expected_output_invalid_password = open(current_folder.joinpath(
    'test_register_invalid_password.out')).read()

# Output Partition Testing
expected_input_valid = open(current_folder.joinpath(
    'expected_input_valid.in'))
expected_input_invalid = open(current_folder.joinpath(
    'expected_input_invalid.in'))

# Input Partition Testing
expected_input_3 = open(current_folder.joinpath('test_r1_3.in'))
expected_output_3 = open(current_folder.joinpath('test_r1_3.out')).read()
expected_input_4 = open(current_folder.joinpath('test_r1_4.in'))
expected_output_4 = open(current_folder.joinpath('test_r1_4.out')).read()
expected_input_5 = open(current_folder.joinpath('test_r1_5.in'))
expected_output_5 = open(current_folder.joinpath('test_r1_5.out')).read()
expected_input_7 = open(current_folder.joinpath('test_r1_7.in'))
expected_output_7 = open(current_folder.joinpath('test_r1_7.out')).read()

# Boundary Partition Testing
expected_input_6 = open(current_folder.joinpath('test_r1_6.in'))
expected_output_6 = open(current_folder.joinpath('test_r1_6.out')).read()


"""
Output partition testing
Testing register function for base valid and invalid cases.
Valid: Register successful
Invalid: Register unsuccessful
"""
def test_register_output_valid():
    """
    Output Partition
    Testing output for successful registration"""
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_valid,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_valid.replace('\r', '')

    assert output.strip() == expected.strip()


def test_register_output_invalid():
    """
    Output Partition
    Testing output for failed registration
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_invalid,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_invalid_password.replace('\r', '')

    assert output.strip() == expected.strip()

""" 
Input Partition Testing
"""
def test_r1_3_user_register():
    '''
    Testing R1-3: The email has to follow addr-spec defined in 
    RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a 
    human-friendly explanation). You can use external libraries/imports.
    Partition 1: no prefix to @ - invalid
    Partition 2: no suffix to @ - invalid
    Partition 3: no . - invalid
    Partition 4: no @ - invalid
    Partition 5: contains all - valid
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
    Partition 1: minimum length not reached - invalid
    Partition 2: no upper case - invalid
    Partition 3: no lower case - invalid
    Partition 4: no special character - invalid
    Partition 5: All of the above - valid
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
    Partition 1: Empty - invalid
    Partition 2: non-alphanumeric only - invalid
    Partition 3: Space at prefix - invalid
    Partition 4: Space at suffix - invalid
    Partition 5: Meets all requirements
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_5,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_5.replace('\r', '')

    assert output.strip() == expected.strip()


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    Partition 1: Email has not been used - valid
    Partition 2: Email has been used - invalid
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_7,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_7.replace('\r', '')

    assert output.strip() == expected.strip()


"""
Boundary Testing
"""
def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.
    test 1: 2 characters - invalid
    test 2: 20 characters - invalid
    test 3: 19 characters - valid
    test 4: 3 characters - valid
    '''
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input_6,
        capture_output=True,
    ).stdout.decode()

    output = output.replace('\r', '')
    expected = expected_output_6.replace('\r', '')

    assert output.strip() == expected.strip()
