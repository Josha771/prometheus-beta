import pytest
from src.string_reverser import reverse_string

def test_reverse_single_word():
    """Test reversing a single word."""
    assert reverse_string("hello") == "olleh"

def test_reverse_multi_word_string():
    """Test reversing a multi-word string."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("hello, world! 123") == "321 !dlrow ,olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_character():
    """Test reversing a single character."""
    assert reverse_string("a") == "a"

def test_reverse_with_invalid_input():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
        reverse_string(None)
        reverse_string(["hello"])