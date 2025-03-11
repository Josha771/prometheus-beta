import pytest
from src.symmetric_difference import symmetric_difference

def test_basic_symmetric_difference():
    """Test symmetric difference with simple lists"""
    assert sorted(symmetric_difference([1, 2, 3], [3, 4, 5])) == [1, 2, 4, 5]

def test_empty_lists():
    """Test symmetric difference with empty lists"""
    assert symmetric_difference([], []) == []

def test_one_empty_list():
    """Test symmetric difference with one empty list"""
    assert sorted(symmetric_difference([1, 2, 3], [])) == [1, 2, 3]

def test_identical_lists():
    """Test symmetric difference with identical lists"""
    assert symmetric_difference([1, 2, 3], [1, 2, 3]) == []

def test_list_with_duplicates():
    """Test symmetric difference with lists containing duplicates"""
    assert sorted(symmetric_difference([1, 1, 2, 3], [3, 4, 4, 5])) == [1, 2, 4, 5]

def test_type_error_non_list():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        symmetric_difference(123, [1, 2, 3])
    
    with pytest.raises(TypeError):
        symmetric_difference([1, 2, 3], "not a list")

def test_different_types():
    """Test symmetric difference with lists of different types"""
    assert sorted(symmetric_difference([1, 'a'], ['a', 2])) == [1, 2]