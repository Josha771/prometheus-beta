def find_common(list1, list2):
    """
    Find and return a list of elements common to both input lists.
    
    Args:
        list1 (list): The first input list
        list2 (list): The second input list
    
    Returns:
        list: A list of elements that appear in both input lists
    
    Raises:
        TypeError: If either input is not a list
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both arguments must be lists")
    
    # Use set intersection for efficient common element finding
    common_elements = list(set(list1) & set(list2))
    
    # Try to sort if possible, otherwise return as is
    try:
        return sorted(common_elements)
    except TypeError:
        return common_elements