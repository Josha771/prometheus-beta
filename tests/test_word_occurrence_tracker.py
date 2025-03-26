import pytest
from src.word_occurrence_tracker import find_word_occurrences

def test_basic_occurrence():
    """Test finding a word with single occurrence"""
    result = find_word_occurrences("hello world python", "world")
    assert result == [(6, "world")]

def test_multiple_occurrences():
    """Test finding a word with multiple occurrences"""
    result = find_word_occurrences("the cat and the dog and the bird", "the")
    assert result == [(0, "the"), (12, "the"), (25, "the")]

def test_no_occurrences():
    """Test when target word is not in the string"""
    result = find_word_occurrences("hello world python", "java")
    assert result == []

def test_whole_string_match():
    """Test when entire string is the target word"""
    result = find_word_occurrences("python", "python")
    assert result == [(0, "python")]

def test_case_sensitive():
    """Test case sensitivity of word matching"""
    result = find_word_occurrences("Python python PYTHON", "python")
    assert result == [(7, "python")]

def test_empty_input_raises_error():
    """Test that empty inputs raise ValueError"""
    with pytest.raises(ValueError):
        find_word_occurrences("", "test")
    
    with pytest.raises(ValueError):
        find_word_occurrences("test", "")

def test_none_input_raises_error():
    """Test that None inputs raise ValueError"""
    with pytest.raises(ValueError):
        find_word_occurrences(None, "test")
    
    with pytest.raises(ValueError):
        find_word_occurrences("test", None)

def test_non_string_input_raises_error():
    """Test that non-string inputs raise TypeError"""
    with pytest.raises(TypeError):
        find_word_occurrences(123, "test")
    
    with pytest.raises(TypeError):
        find_word_occurrences("test", 123)