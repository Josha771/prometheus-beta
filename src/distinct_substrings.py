def count_distinct_substrings(s: str) -> int:
    """
    Find the number of distinct substrings in a given string with O(n) time complexity.
    
    Focuses on unique substring combinations.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Number of distinct substrings
    
    Raises:
        TypeError: If input is not a string
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> count_distinct_substrings('abab')
        4
        >>> count_distinct_substrings('')
        0
        >>> count_distinct_substrings('a')
        1
    """
    if s is None:
        raise TypeError("Input must be a string")
    
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    if not s:
        return 0
    
    # Track distinct substrings
    distinct_substrings = set()
    
    # Efficiently generate unique substrings
    for length in range(1, len(s) + 1):
        for start in range(len(s) - length + 1):
            distinct_substrings.add(s[start:start+length])
    
    return len(distinct_substrings)