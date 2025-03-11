import pytest
from src.string_validator import is_digit_string

def test_valid_digit_string():
    """Test that a string with only digits returns True."""
    assert is_digit_string("12345") == True

def test_empty_string():
    """Test that an empty string returns False."""
    assert is_digit_string("") == False

def test_string_with_spaces():
    """Test that a string with spaces returns False."""
    assert is_digit_string("123 456") == False

def test_string_with_letters():
    """Test that a string with letters returns False."""
    assert is_digit_string("123abc") == False

def test_string_with_special_characters():
    """Test that a string with special characters returns False."""
    assert is_digit_string("123!@#") == False

def test_zero_string():
    """Test that a zero string returns True."""
    assert is_digit_string("0") == True

def test_invalid_input_type():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        is_digit_string(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        is_digit_string(None)