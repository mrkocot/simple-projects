import pytest


def multiply(x, y):
    return x * y


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(7, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6

def another_test_that_will_fail():
    five = 5
    assert 2 + 2 == five


class TestListOperations:
    def test_list_append(self):
        items = [1, 2]
        items.append(3)
        assert items == [1, 2, 3]

    def test_list_reverse(self):
        items = [1, 2, 3]
        items.reverse()
        assert items == [3, 2, 1]


@pytest.mark.parametrize("value, expected", [
    (0, 0),
    (2, 4),
    (5, 25),
])
def test_square(value, expected):
    assert multiply(value, value) == expected
