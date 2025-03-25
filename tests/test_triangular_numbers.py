import pytest
from src.triangular_numbers import count_triangular_numbers

def test_count_triangular_numbers_zero():
    """Test count of triangular numbers less than or equal to 0."""
    assert count_triangular_numbers(0) == 0

def test_count_triangular_numbers_small():
    """Test count of triangular numbers for small inputs."""
    assert count_triangular_numbers(1) == 1  # First triangular number (1)
    assert count_triangular_numbers(3) == 2  # First two triangular numbers (1, 3)
    assert count_triangular_numbers(6) == 3  # First three triangular numbers (1, 3, 6)

def test_count_triangular_numbers_medium():
    """Test count of triangular numbers for medium inputs."""
    assert count_triangular_numbers(10) == 4  # First four triangular numbers (1, 3, 6, 10)
    assert count_triangular_numbers(15) == 5  # First five triangular numbers (1, 3, 6, 10, 15)

def test_count_triangular_numbers_large():
    """Test count of triangular numbers for larger inputs."""
    assert count_triangular_numbers(100) == 14  # Verify count for larger input

def test_count_triangular_numbers_invalid_inputs():
    """Test invalid input handling."""
    with pytest.raises(TypeError):
        count_triangular_numbers(3.14)
    
    with pytest.raises(TypeError):
        count_triangular_numbers("10")
    
    with pytest.raises(ValueError):
        count_triangular_numbers(-5)