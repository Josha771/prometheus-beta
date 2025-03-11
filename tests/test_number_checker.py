import pytest
from src.number_checker import is_even_or_odd

def test_positive_even_numbers():
    """Test positive even numbers."""
    assert is_even_or_odd(0) == 'even'
    assert is_even_or_odd(2) == 'even'
    assert is_even_or_odd(4) == 'even'
    assert is_even_or_odd(100) == 'even'

def test_positive_odd_numbers():
    """Test positive odd numbers."""
    assert is_even_or_odd(1) == 'odd'
    assert is_even_or_odd(3) == 'odd'
    assert is_even_or_odd(5) == 'odd'
    assert is_even_or_odd(101) == 'odd'

def test_negative_even_numbers():
    """Test negative even numbers."""
    assert is_even_or_odd(-2) == 'even'
    assert is_even_or_odd(-4) == 'even'
    assert is_even_or_odd(-100) == 'even'

def test_negative_odd_numbers():
    """Test negative odd numbers."""
    assert is_even_or_odd(-1) == 'odd'
    assert is_even_or_odd(-3) == 'odd'
    assert is_even_or_odd(-5) == 'odd'

def test_invalid_input_types():
    """Test that non-integer inputs raise TypeError."""
    with pytest.raises(TypeError):
        is_even_or_odd(3.14)
    
    with pytest.raises(TypeError):
        is_even_or_odd("2")
    
    with pytest.raises(TypeError):
        is_even_or_odd(None)
    
    with pytest.raises(TypeError):
        is_even_or_odd([])