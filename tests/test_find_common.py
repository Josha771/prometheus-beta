import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test finding common elements in simple lists"""
    assert sorted(find_common([1, 2, 3], [3, 4, 5])) == [3]
    assert sorted(find_common(['a', 'b', 'c'], ['b', 'c', 'd'])) == ['b', 'c']

def test_find_common_empty_lists():
    """Test behavior with empty lists"""
    assert find_common([], [1, 2, 3]) == []
    assert find_common([1, 2, 3], []) == []
    assert find_common([], []) == []

def test_find_common_duplicate_elements():
    """Test handling of duplicate elements"""
    assert sorted(find_common([1, 1, 2, 2], [1, 2, 3])) == [1, 2]

def test_find_common_different_types():
    """Test finding common elements with mixed types"""
    assert sorted(find_common([1, 'a', 2], [2, 'a', 3])) == [2, 'a']

def test_find_common_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        find_common(1, [1, 2, 3])
    with pytest.raises(TypeError):
        find_common([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        find_common(None, [1, 2, 3])