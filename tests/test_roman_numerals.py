import pytest
from src.roman_numerals import int_to_roman

def test_int_to_roman_basic_conversions():
    """Test basic integer to Roman numeral conversions."""
    test_cases = [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (27, "XXVII"),
        (49, "XLIX"),
        (99, "XCIX"),
        (500, "D"),
        (2023, "MMXXIII"),
        (3999, "MMMCMXCIX")
    ]
    
    for num, expected in test_cases:
        assert int_to_roman(num) == expected, f"Failed for {num}"

def test_edge_cases():
    """Test edge cases for int_to_roman function."""
    # Zero should return an empty string
    assert int_to_roman(0) == ""

def test_error_cases():
    """Test error handling for invalid inputs."""
    # Negative numbers should raise ValueError
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(-1)
    
    # Numbers above 3999 should raise ValueError
    with pytest.raises(ValueError, match="Input must be between 0 and 3999"):
        int_to_roman(4000)

def test_type_errors():
    """Test type error handling."""
    # Non-integer inputs should raise TypeError
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman("42")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_roman(None)