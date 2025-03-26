import pytest
from src.capitalize_words import capitalize_comma_words

def test_basic_capitalization():
    """Test basic capitalization of words."""
    assert capitalize_comma_words('hello,world') == 'Hello,World'

def test_already_capitalized():
    """Test input with already capitalized words."""
    assert capitalize_comma_words('Hello,World') == 'Hello,World'

def test_mixed_case():
    """Test input with mixed case words."""
    assert capitalize_comma_words('hElLo,wOrLd') == 'Hello,World'

def test_single_word():
    """Test input with a single word."""
    assert capitalize_comma_words('hello') == 'Hello'

def test_multiple_words():
    """Test input with multiple words."""
    assert capitalize_comma_words('python,is,awesome') == 'Python,Is,Awesome'

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        capitalize_comma_words('')

def test_invalid_characters_raises_error():
    """Test that input with non-alphabetical characters raises a ValueError."""
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_words('hello123,world')
    
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_words('hello world')
    
    with pytest.raises(ValueError, match="Input must contain only alphabetical characters and commas"):
        capitalize_comma_words('hello!,world')