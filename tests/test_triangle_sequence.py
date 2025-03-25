import pytest
from src.triangle_sequence import generate_triangle_sequence

def test_generate_triangle_sequence_basic():
    """Test generating a basic sequence of triangle numbers."""
    assert generate_triangle_sequence(5) == [1, 3, 6, 10, 15]

def test_generate_triangle_sequence_zero():
    """Test generating sequence with zero elements."""
    assert generate_triangle_sequence(0) == []

def test_generate_triangle_sequence_single():
    """Test generating sequence with a single element."""
    assert generate_triangle_sequence(1) == [1]

def test_generate_triangle_sequence_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Number of sequence elements must be non-negative"):
        generate_triangle_sequence(-1)

def test_generate_triangle_sequence_invalid_type():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_sequence(None)