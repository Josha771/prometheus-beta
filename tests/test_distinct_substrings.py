import pytest
from src.distinct_substrings import count_distinct_substrings

def test_empty_string():
    """Test that an empty string returns 0 distinct substrings."""
    assert count_distinct_substrings('') == 0

def test_single_character():
    """Test that a single character returns 1 distinct substring."""
    assert count_distinct_substrings('a') == 1

def test_repeated_characters():
    """Test a string with repeated characters."""
    assert count_distinct_substrings('aaaa') == 1

def test_simple_string():
    """Test a simple string with multiple distinct substrings."""
    assert count_distinct_substrings('abab') == 4

def test_varying_string():
    """Test a string with varying characters and multiple unique substrings."""
    assert count_distinct_substrings('banana') == 13

def test_long_string():
    """Test a longer string to verify performance and correctness."""
    test_str = 'abcdefghijklmnopqrstuvwxyz'
    result = count_distinct_substrings(test_str)
    assert result == (len(test_str) * (len(test_str) + 1)) // 2

def test_unicode_characters():
    """Test string with Unicode characters."""
    assert count_distinct_substrings('こんにちは') > 0

def test_alphanumeric_string():
    """Test string with alphanumeric characters."""
    assert count_distinct_substrings('abc123def456') > 0

def test_type_error():
    """Test that type errors are raised for non-string inputs."""
    with pytest.raises(TypeError):
        count_distinct_substrings(123)
    with pytest.raises(TypeError):
        count_distinct_substrings(None)