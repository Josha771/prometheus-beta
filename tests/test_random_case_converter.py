import pytest
import random
from src.random_case_converter import convert_to_alternating_random_case

def test_convert_to_alternating_random_case_basic():
    """Test that the function works with a basic string."""
    # Set a fixed seed for reproducibility in randomness
    random.seed(42)
    
    result = convert_to_alternating_random_case("hello")
    assert result.lower() == "hello"
    assert len(result) == 5

def test_convert_to_alternating_random_case_empty_string():
    """Test that an empty string returns an empty string."""
    assert convert_to_alternating_random_case("") == ""

def test_convert_to_alternating_random_case_error_handling():
    """Test that the function raises TypeError for non-string inputs."""
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(None)

def test_convert_to_alternating_random_case_randomness():
    """Test that the function produces different results across multiple calls."""
    random.seed(None)  # Reset seed
    
    input_str = "testing randomness"
    results = set()
    
    # Generate multiple results to check for variation
    for _ in range(10):
        results.add(convert_to_alternating_random_case(input_str))
    
    # Ensure at least some variation in results
    assert len(results) > 1

def test_convert_to_alternating_random_case_preservation():
    """Test that the function preserves the original characters."""
    input_str = "Hello, World! 123"
    result = convert_to_alternating_random_case(input_str)
    
    # Check that the result contains the same characters (just in different case)
    assert sorted(result.lower()) == sorted(input_str.lower())
    assert len(result) == len(input_str)