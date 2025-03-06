import pytest
from src.fibonacci import generate_fibonacci_sequence

def test_fibonacci_sequence_basics():
    # Test basic sequences
    assert generate_fibonacci_sequence(0) == []
    assert generate_fibonacci_sequence(1) == [0]
    assert generate_fibonacci_sequence(2) == [0, 1]
    assert generate_fibonacci_sequence(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci_sequence(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_sequence_longer():
    # Test a longer sequence
    full_sequence = generate_fibonacci_sequence(10)
    assert len(full_sequence) == 10
    assert full_sequence[-1] == 34  # Check the last term

def test_fibonacci_invalid_inputs():
    # Test error handling
    with pytest.raises(TypeError, match="Number of terms must be an integer"):
        generate_fibonacci_sequence("5")
    
    with pytest.raises(TypeError, match="Number of terms must be an integer"):
        generate_fibonacci_sequence(5.5)
    
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_fibonacci_sequence(-1)

def test_fibonacci_large_sequence():
    # Test a large sequence to ensure no overflow
    large_sequence = generate_fibonacci_sequence(50)
    assert len(large_sequence) == 50
    
    # Verify Fibonacci property for the entire sequence
    for i in range(2, len(large_sequence)):
        assert large_sequence[i] == large_sequence[i-1] + large_sequence[i-2]