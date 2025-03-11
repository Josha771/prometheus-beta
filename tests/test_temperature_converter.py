import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_freezing_point():
    """Test conversion of freezing point of water."""
    assert fahrenheit_to_celsius(32) == 0

def test_boiling_point():
    """Test conversion of boiling point of water."""
    assert fahrenheit_to_celsius(212) == 100

def test_zero_fahrenheit():
    """Test conversion of 0°F."""
    assert fahrenheit_to_celsius(0) == -17.78

def test_fractional_temperature():
    """Test conversion of a fractional temperature."""
    assert fahrenheit_to_celsius(98.6) == 37

def test_negative_temperature():
    """Test conversion of a negative temperature."""
    assert fahrenheit_to_celsius(-40) == -40

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")

def test_invalid_input_none():
    """Test error handling for None input."""
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)