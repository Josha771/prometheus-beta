import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiples():
    """Test basic functionality with simple inputs."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9 + 10

def test_single_multiple():
    """Test with a single multiple."""
    assert sum_of_multiples(10, [3]) == 18  # 3 + 6 + 9

def test_no_multiples():
    """Test with no multiples in range."""
    assert sum_of_multiples(2, [4]) == 0

def test_exact_multiple():
    """Test when a number is exactly at the limit."""
    assert sum_of_multiples(6, [3]) == 9  # 3 + 6

def test_unique_multiples():
    """Test that duplicates are not double-counted."""
    assert sum_of_multiples(10, [3, 6]) == 18  # 3 + 6 + 9

def test_zero_limit_error():
    """Test raising ValueError for zero limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(0, [3, 5])

def test_negative_limit_error():
    """Test raising ValueError for negative limit."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(-5, [3, 5])

def test_zero_multiple_error():
    """Test raising ValueError for zero in multiples."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, 0, 5])

def test_negative_multiple_error():
    """Test raising ValueError for negative multiple."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, -5])

def test_large_limit():
    """Test with a larger limit."""
    result = sum_of_multiples(1000, [3, 5])
    assert result == 233168