import pytest
from src.find_first_last_occurrence import find_first_last_occurrence

def test_find_first_last_occurrence_basic():
    """Test basic functionality with a sorted array with multiple occurrences."""
    arr = [1, 2, 2, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 3)

def test_find_first_last_occurrence_single_occurrence():
    """Test with an array where the target appears only once."""
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 3) == (2, 2)

def test_find_first_last_occurrence_not_found():
    """Test when the target is not in the array."""
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 6) == (-1, -1)

def test_find_first_last_occurrence_empty_array():
    """Test with an empty array."""
    arr = []
    assert find_first_last_occurrence(arr, 1) == (-1, -1)

def test_find_first_last_occurrence_beginning():
    """Test when target is at the beginning of the array."""
    arr = [1, 1, 1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 1) == (0, 2)

def test_find_first_last_occurrence_end():
    """Test when target is at the end of the array."""
    arr = [1, 2, 3, 4, 5, 5, 5]
    assert find_first_last_occurrence(arr, 5) == (4, 6)

def test_find_first_last_occurrence_large_array():
    """Test with a larger array to ensure consistent performance."""
    arr = list(range(1000)) + [1000] * 10 + list(range(1001, 2000))
    assert find_first_last_occurrence(arr, 1000) == (1000, 1009)

def test_find_first_last_occurrence_negative_numbers():
    """Test with negative numbers in the array."""
    arr = [-5, -5, -3, -1, 0, 2, 4]
    assert find_first_last_occurrence(arr, -5) == (0, 1)

def test_find_first_last_occurrence_mixed_types():
    """Test type-specific occurrence scenarios."""
    # For strictly integer searches
    arr = [1, 2, 3, 3, 4]
    assert find_first_last_occurrence(arr, 3) == (2, 3)
    
    # Separate test case for floating point
    arr_float = [1.0, 2.0, 3.0, 3.0, 4.0]
    assert find_first_last_occurrence(arr_float, 3.0) == (2, 3)