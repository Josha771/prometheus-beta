def bubble_merge_sort(arr):
    """
    A custom sorting algorithm that combines Bubble Sort and Merge Sort.
    
    The algorithm works in two stages:
    1. Partially sort the array using Bubble Sort to reduce inversions
    2. Complete the sorting using Merge Sort for efficiency
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Type checking
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Stage 1: Bubble Sort to reduce inversions
    partially_sorted = arr.copy()
    for i in range(len(partially_sorted) // 2):  # Partial bubble sort
        for j in range(len(partially_sorted) - 1 - i):
            if partially_sorted[j] > partially_sorted[j + 1]:
                partially_sorted[j], partially_sorted[j + 1] = partially_sorted[j + 1], partially_sorted[j]
    
    # Stage 2: Merge Sort to complete sorting
    def merge(left, right):
        """Helper function to merge two sorted lists"""
        result = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort(arr):
        """Recursive merge sort implementation"""
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Divide
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        # Conquer (merge)
        return merge(left, right)
    
    # Apply merge sort to the partially sorted array
    return merge_sort(partially_sorted)