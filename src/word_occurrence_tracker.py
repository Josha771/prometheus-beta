def find_word_occurrences(input_string: str, target_word: str) -> list:
    """
    Find all occurrences of a target word in a given string, 
    with the character position before each occurrence.

    Args:
        input_string (str): The string to search through
        target_word (str): The word to find occurrences of

    Returns:
        list: A list of tuples, each containing:
            - Character position before the occurrence
            - The occurrence of the target word

    Raises:
        ValueError: If input_string or target_word is empty or None
        TypeError: If inputs are not strings
    """
    # Input validation
    if input_string is None or target_word is None:
        raise ValueError("Input strings cannot be None")
    
    if not isinstance(input_string, str) or not isinstance(target_word, str):
        raise TypeError("Inputs must be strings")
    
    if not input_string or not target_word:
        raise ValueError("Input strings cannot be empty")

    # Split the input string into words
    words = input_string.split()
    
    # Track results and cumulative character count
    occurrences = []
    current_position = 0

    # Iterate through words to find occurrences
    for word in words:
        # Check if current word matches target
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Add word length and space to current position for next iteration
        current_position += len(word) + 1  # +1 for space

    return occurrences