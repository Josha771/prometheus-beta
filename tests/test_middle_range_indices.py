import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_default_range():
    """Test odd-length list with default range size"""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list) == [2]

def test_even_length_list_default_range():
    """Test even-length list with default range size"""
    test_list = [1, 2, 3, 4, 5, 6]
    assert find_middle_range_indices(test_list) == [2, 3]

def test_custom_range_size():
    """Test with a custom range size"""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_middle_range_indices(test_list, range_size=2) == [3, 4, 5]

def test_large_range_size():
    """Test when range size is larger than list length"""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, range_size=10) == list(range(5))

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_middle_range_indices([])

def test_negative_range_size_raises_error():
    """Test that negative range size raises a ValueError"""
    with pytest.raises(ValueError, match="Range size must be non-negative"):
        find_middle_range_indices([1, 2, 3], range_size=-1)

def test_single_element_list():
    """Test list with a single element"""
    test_list = [42]
    assert find_middle_range_indices(test_list) == [0]