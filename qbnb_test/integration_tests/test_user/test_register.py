from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# expected input and output
expected_input = open(current_folder.joinpath('test_register.in'))
expected_output = open(current_folder.joinpath('test_register.out')).read()

def test_register():
    """Uses capsys in pytest to capture stdout and stderr
    Currently working on getting tests working before doing actual tests
    """
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_input,
        capture_output=True,
    ).stdout.decode()

    """Issue
    expected_output.strip() adds an additional backslash while,
    output.strip() adds an additional blackslash followed by an r
    They do not equate as a result"""
    assert output.strip() == expected_output.strip()

""" 
Input Partition Testing
"""
def ipt_user_register():
    print("input partition testing")

"""
Black Box Shotgun Testing
"""
def bbst_user_register():
    print("black box shotgun testing")


"""
Model-Based Output Testing
"""
def mbt_user_register():
    print("Model-Based Testing")