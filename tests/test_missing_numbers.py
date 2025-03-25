import pytest
from src.missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test finding missing numbers in a typical scenario."""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_find_missing_numbers_consecutive():
    """Test array with consecutive numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_find_missing_numbers_large_gaps():
    """Test array with large gaps between numbers."""
    assert find_missing_numbers([1, 10]) == [2, 3, 4, 5, 6, 7, 8, 9]

def test_find_missing_numbers_empty_array():
    """Test empty input array."""
    assert find_missing_numbers([]) == []

def test_find_missing_numbers_single_element():
    """Test array with a single element."""
    assert find_missing_numbers([5]) == []

def test_find_missing_numbers_negative_numbers():
    """Test array with negative numbers."""
    assert find_missing_numbers([-3, -1]) == [-2]

def test_unsorted_array_raises_error():
    """Test that an unsorted array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array must be sorted in ascending order"):
        find_missing_numbers([5, 3, 1])