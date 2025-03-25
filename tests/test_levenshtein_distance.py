import pytest
from src.levenshtein_distance import compute_levenshtein_distance

def test_identical_strings():
    """Test that identical strings have a distance of 0"""
    assert compute_levenshtein_distance('hello', 'hello') == 0

def test_completely_different_strings():
    """Test strings that require complete transformation"""
    assert compute_levenshtein_distance('kitten', 'sitting') == 3

def test_empty_strings():
    """Test distance between empty strings"""
    assert compute_levenshtein_distance('', '') == 0

def test_one_empty_string():
    """Test distance when one string is empty"""
    assert compute_levenshtein_distance('abc', '') == 3
    assert compute_levenshtein_distance('', 'xyz') == 3

def test_case_sensitivity():
    """Test that the function is case-sensitive"""
    assert compute_levenshtein_distance('Hello', 'hello') == 1

def test_unicode_strings():
    """Test strings with unicode characters"""
    assert compute_levenshtein_distance('café', 'cafe') == 1

def test_different_lengths():
    """Test strings of different lengths"""
    assert compute_levenshtein_distance('short', 'shorter') == 2
    assert compute_levenshtein_distance('longer', 'long') == 2

def test_invalid_input_types():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError):
        compute_levenshtein_distance(123, 'abc')
    
    with pytest.raises(TypeError):
        compute_levenshtein_distance('abc', None)
    
    with pytest.raises(TypeError):
        compute_levenshtein_distance([], {})