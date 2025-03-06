import pytest
from src.array_sum import calculate_array_sum

def test_calculate_array_sum_basic():
    """Test sum of standard numeric array"""
    assert calculate_array_sum([1, 2, 3, 4, 5]) == 15

def test_calculate_array_sum_empty():
    """Test sum of empty array"""
    assert calculate_array_sum([]) == 0

def test_calculate_array_sum_negative():
    """Test sum of array with negative numbers"""
    assert calculate_array_sum([-1, -2, -3]) == -6

def test_calculate_array_sum_mixed():
    """Test sum of array with mixed positive and negative numbers"""
    assert calculate_array_sum([-1, 2, -3, 4]) == 2

def test_calculate_array_sum_floats():
    """Test sum of array with floating point numbers"""
    assert round(calculate_array_sum([1.5, 2.5, 3.0]), 2) == 7.0

def test_calculate_array_sum_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_array_sum("not a list")

def test_calculate_array_sum_non_numeric():
    """Test error handling for non-numeric elements"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_array_sum([1, 2, "3", 4])