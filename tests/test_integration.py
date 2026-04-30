import pytest

from app.calculator import add, calculate_average, multiply


def test_combined_operations():
    result = multiply(add(2, 3), 4)
    assert result == 20


def test_average():
    assert calculate_average([10, 20, 30]) == 20


def test_average_empty():
    with pytest.raises(ValueError):
        calculate_average([])
