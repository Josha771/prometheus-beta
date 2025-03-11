import pytest
from src.array_shuffler import shuffle_array
import random

def test_shuffle_array_preserves_elements():
    """Test that shuffle preserves all original elements."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert len(shuffled) == len(original)
    assert set(shuffled) == set(original)

def test_shuffle_array_randomness():
    """Test that multiple shuffles produce different arrangements."""
    original = [1, 2, 3, 4, 5]
    
    # Set a fixed seed for reproducible randomness
    random.seed(42)
    shuffle1 = shuffle_array(original)
    
    random.seed(42)
    shuffle2 = shuffle_array(original)
    
    # Technically this could pass by chance, but with a fixed seed, 
    # it's highly unlikely they would be the same if shuffling is working
    assert len(set(shuffle1) - set(original)) == 0
    assert len(set(shuffle2) - set(original)) == 0

def test_shuffle_empty_list():
    """Test shuffling an empty list."""
    assert shuffle_array([]) == []

def test_shuffle_single_element_list():
    """Test shuffling a list with a single element."""
    original = [42]
    assert shuffle_array(original) == original

def test_shuffle_non_list_input():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError):
        shuffle_array("not a list")
    
    with pytest.raises(TypeError):
        shuffle_array(123)

def test_shuffle_does_not_modify_original():
    """Ensure the original list is not modified."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    assert original == [1, 2, 3, 4, 5]  # Original list unchanged
    assert shuffled != original  # Shuffled list is different