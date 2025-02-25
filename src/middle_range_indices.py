def find_middle_range_indices(sorted_list, range_size=1):
    """
    Find indices of elements within a given range of the middle value in a sorted list.

    Args:
        sorted_list (list): A sorted list of integers
        range_size (int, optional): Number of elements to include on each side of the middle. 
                                    Defaults to 1.

    Returns:
        list: Indices of elements within the specified middle range

    Raises:
        ValueError: If the input list is empty or range_size is negative
    """
    # Validate input
    if not sorted_list:
        raise ValueError("Input list cannot be empty")
    
    if range_size < 0:
        raise ValueError("Range size must be non-negative")

    # Determine the middle index
    mid_index = len(sorted_list) // 2

    # Calculate the start and end indices for the range
    start_index = mid_index - range_size
    end_index = mid_index + range_size

    # Ensure indices are within list bounds
    start_index = max(0, start_index)
    end_index = min(len(sorted_list) - 1, end_index)

    # Return the indices of elements in the middle range
    return list(range(start_index, end_index + 1))