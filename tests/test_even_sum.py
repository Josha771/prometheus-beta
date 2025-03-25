import pytest
from src.even_sum import sum_even_numbers

def test_sum_of_even_numbers():
    """Test sum of even numbers in a mixed list of integers"""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12

def test_empty_list():
    """Test sum of even numbers in an empty list"""
    assert sum_even_numbers([]) == 0

def test_only_odd_numbers():
    """Test sum when only odd numbers are present"""
    assert sum_even_numbers([1, 3, 5, 7]) == 0

def test_only_even_numbers():
    """Test sum when only even numbers are present"""
    assert sum_even_numbers([2, 4, 6, 8]) == 20

def test_negative_even_numbers():
    """Test sum of even numbers including negative numbers"""
    assert sum_even_numbers([-2, -1, 0, 1, 2]) == 0

def test_invalid_input_type():
    """Test TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        sum_even_numbers("not a list")

def test_invalid_element_type():
    """Test TypeError is raised for list with non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_even_numbers([1, 2, "3", 4])