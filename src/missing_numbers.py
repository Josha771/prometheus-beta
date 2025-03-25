def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers in ascending order.
    
    Returns:
        list: A list of missing numbers between the smallest and largest elements.
    
    Raises:
        ValueError: If the input array is empty or not sorted.
    """
    # Check for empty array
    if not arr:
        return []
    
    # Validate the array is sorted
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input array must be sorted in ascending order")
    
    # Find all missing numbers
    missing_numbers = []
    
    # Iterate through the range from the smallest to the largest number
    for num in range(arr[0], arr[-1] + 1):
        if num not in arr:
            missing_numbers.append(num)
    
    return missing_numbers