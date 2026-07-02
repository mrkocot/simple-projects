# my_project/tests/test_example.py

import pytest

# A simple function to be tested
def add(x, y):
    return x + y

# Test for the 'add' function (this is a test function directly in the module)
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -5) == -6

# A test class
class TestStringOperations:
    # A test method within the class
    def test_string_concatenation(self):
        assert "hello" + " " + "world" == "hello world"

    def test_string_uppercase(self):
        assert "loud".upper() == "LOUD"

# Parameterized test
@pytest.mark.parametrize("input_val, expected_output", [
    (0, 0),
    (1, 1),
    (-1, 1) # An intentional failure for demonstration if we were testing abs()
])
def test_identity_function_for_abs(input_val, expected_output):
    # Let's pretend we are testing abs(), but make it fail for one case
    if input_val == -1 and expected_output == 1:
        assert abs(input_val) == expected_output # This will pass for abs()
    # For demonstration of a failure, let's assert something that will fail for the last case
    # if we were checking identity, not abs.
    # To make a test fail for report example:
    # assert input_val == expected_output # This would fail for (-1, 1)

    # For this example, let's keep it simple and assume we're testing identity (which will make one case fail)
    # For actual abs testing, you'd use abs(input_val)
    if input_val == -1: # Let's make one test case fail to see it in XML
        assert input_val == expected_output, "Intentional failure for demo"
    else:
        assert input_val == expected_output


# A test that is expected to fail
@pytest.mark.xfail(reason="This feature is not yet implemented")
def test_new_feature():
    assert False # This test will be marked as xfailed (expected failure)

# A test that is skipped
@pytest.mark.skip(reason="Skipping this old test")
def test_old_feature():
    # Some old test logic
    assert 1 == 1
