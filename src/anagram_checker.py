import unicodedata

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another, 
    using all the original letters exactly once.
    
    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Check input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both arguments must be strings")
    
    # Normalize unicode characters and remove accents
    def normalize(s: str) -> str:
        # Remove accents and convert to lowercase
        normalized = ''.join(
            char.lower() for char in unicodedata.normalize('NFKD', s) 
            if not unicodedata.combining(char)
        )
        # Remove non-alphanumeric characters
        return ''.join(char for char in normalized if char.isalnum())
    
    # Normalize and compare
    str1_normalized = normalize(str1)
    str2_normalized = normalize(str2)
    
    # Empty strings are anagrams of each other
    if not str1_normalized and not str2_normalized:
        return True
    
    # Quick length check
    if len(str1_normalized) != len(str2_normalized):
        return False
    
    # Quick check to avoid trivial matches
    if str1_normalized == str2_normalized:
        return False
    
    # Create character frequency dictionaries
    char_count1 = {}
    char_count2 = {}
    
    # Count character frequencies
    for char in str1_normalized:
        char_count1[char] = char_count1.get(char, 0) + 1
    
    for char in str2_normalized:
        char_count2[char] = char_count2.get(char, 0) + 1
    
    # Compare character frequencies
    return char_count1 == char_count2