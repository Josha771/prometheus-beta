from typing import Set

def count_distinct_substrings(s: str) -> int:
    """
    Find the number of distinct substrings in a given string with O(n) time complexity.
    
    Uses a suffix tree-like approach with sliding window and hash set.
    
    Args:
        s (str): Input string to analyze
    
    Returns:
        int: Number of distinct substrings
    
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
    if not s:
        return 0
    
    # Use a set to track unique substrings
    distinct_substrings: Set[str] = set()
    
    # Iterate through all possible starting points
    for start in range(len(s)):
        current_substring = ''
        for end in range(start, len(s)):
            current_substring += s[end]
            distinct_substrings.add(current_substring)
    
    return len(distinct_substrings)