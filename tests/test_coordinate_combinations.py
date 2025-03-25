import pytest
from src.coordinate_combinations import get_unique_coordinate_combinations

def test_basic_unique_combinations():
    """Test basic functionality with unique coordinate pairs"""
    input_coords = [(1, 2), (3, 4), (1, 2), (5, 6)]
    expected = [(1, 2), (3, 4), (5, 6)]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_empty_list():
    """Test with an empty list"""
    assert get_unique_coordinate_combinations([]) == []

def test_all_duplicate_coordinates():
    """Test list with all duplicate coordinates"""
    input_coords = [(1, 1), (1, 1), (1, 1)]
    assert get_unique_coordinate_combinations(input_coords) == [(1, 1)]

def test_mixed_numeric_types():
    """Test coordinates with mixed numeric types"""
    input_coords = [(1, 2), (1.0, 2.0), (3, 4.5)]
    expected = [(1, 2), (3, 4.5)]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_sorting_order():
    """Test that coordinates are sorted correctly"""
    input_coords = [(3, 1), (1, 4), (2, 2), (1, 4)]
    expected = [(1, 4), (2, 2), (3, 1)]
    assert get_unique_coordinate_combinations(input_coords) == expected

def test_invalid_input_type():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_type():
    """Test that invalid coordinate types raise ValueError"""
    with pytest.raises(ValueError, match="Each coordinate must be a tuple of two elements"):
        get_unique_coordinate_combinations([(1, 2), [3, 4]])

def test_non_numeric_coordinates():
    """Test that non-numeric coordinates raise TypeError"""
    with pytest.raises(TypeError, match="Coordinates must be numeric values"):
        get_unique_coordinate_combinations([(1, 'a'), (2, 3)])