import pytest
import random
from src.bubble_merge_sort import bubble_merge_sort

def test_basic_sorting():
    """Test basic list sorting"""
    test_cases = [
        [5, 2, 9, 1, 7, 6],
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [1],
        []
    ]
    
    for case in test_cases:
        sorted_case = bubble_merge_sort(case)
        assert sorted_case == sorted(case), f"Failed to sort {case}"
        assert sorted_case is not case, "Should return a new list"

def test_type_error():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        bubble_merge_sort("not a list")
    with pytest.raises(TypeError):
        bubble_merge_sort(123)
    with pytest.raises(TypeError):
        bubble_merge_sort(None)

def test_large_random_list():
    """Test sorting a large random list"""
    # Generate a large random list
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    
    # Compare with Python's built-in sort
    sorted_list = bubble_merge_sort(large_list)
    assert sorted_list == sorted(large_list), "Failed to sort large random list"

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    test_cases = [
        [3, 3, 3, 3],
        [1, 2, 2, 1, 3, 3, 1],
        [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    ]
    
    for case in test_cases:
        sorted_case = bubble_merge_sort(case)
        assert sorted_case == sorted(case), f"Failed to sort list with duplicates: {case}"

def test_mixed_type_comparisons():
    """Test sorting lists with mixed numeric types"""
    mixed_list = [5, 2.5, 7, 1, 3.14, 6]
    sorted_mixed = bubble_merge_sort(mixed_list)
    assert sorted_mixed == sorted(mixed_list), "Failed to sort mixed numeric types"

def test_negative_numbers():
    """Test sorting lists with negative numbers"""
    negative_list = [-5, -2, -9, -1, -7, -6]
    sorted_negative = bubble_merge_sort(negative_list)
    assert sorted_negative == sorted(negative_list), "Failed to sort list with negative numbers"

def test_already_sorted_list():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    result = bubble_merge_sort(sorted_list)
    assert result == sorted_list, "Failed to handle already sorted list"
    assert result is not sorted_list, "Should return a new list"

def test_reverse_sorted_list():
    """Test sorting a reverse-sorted list"""
    reverse_sorted = [5, 4, 3, 2, 1]
    result = bubble_merge_sort(reverse_sorted)
    assert result == sorted(reverse_sorted), "Failed to sort reverse-sorted list"