def bubble_sort(arr):
    """
    Optimized Bubble Sort algorithm that reduces redundant iterations.
    
    This implementation uses a flag to track if any swaps occur in each pass.
    If no swaps occur, the list is already sorted, and the algorithm terminates early.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    n = len(arr)
    if n <= 1:
        return arr
    
    # Optimize by tracking if any swaps occur
    for i in range(n):
        # Flag to track if any swaps occur in this pass
        swapped = False
        
        # Reduce iterations by comparing up to (n-i-1)
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return arr