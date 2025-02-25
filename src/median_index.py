def find_median_index(arr):
    """
    Find the median index or value in a sorted array of integers.
    
    Args:
        arr (list): A sorted list of integers
    
    Returns:
        float or int: The median index for odd-length arrays,
                      or the average of middle indices for even-length arrays
    
    Raises:
        ValueError: If the input array is empty
    """
    # Check for empty array
    if not arr:
        raise ValueError("Cannot find median of an empty array")
    
    # Get the length of the array
    n = len(arr)
    
    # For odd-length arrays, return the middle index
    if n % 2 == 1:
        return n // 2
    
    # For even-length arrays, return average of two middle indices
    return (n // 2 - 1 + n // 2) / 2