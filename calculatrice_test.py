import pytest
from calculatrice import addition, subtraction


def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(-1, -1) == -2


def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(3, 5) == -2
    assert subtraction(-1, -1) == 0
