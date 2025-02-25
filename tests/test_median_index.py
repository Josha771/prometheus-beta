import pytest
from src.median_index import find_median_index

def test_odd_length_array():
    """Test median index for odd-length array"""
    arr = [1, 2, 3, 4, 5]
    assert find_median_index(arr) == 2

def test_even_length_array():
    """Test median index for even-length array"""
    arr = [1, 2, 3, 4]
    assert find_median_index(arr) == 1.5

def test_single_element_array():
    """Test array with a single element"""
    arr = [42]
    assert find_median_index(arr) == 0

def test_large_array():
    """Test a larger odd-length array"""
    arr = [10, 20, 30, 40, 50, 60, 70]
    assert find_median_index(arr) == 3

def test_large_even_array():
    """Test a larger even-length array"""
    arr = [10, 20, 30, 40, 50, 60]
    assert find_median_index(arr) == 2.5

def test_empty_array():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find median of an empty array"):
        find_median_index([])