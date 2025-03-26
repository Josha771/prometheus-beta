def capitalize_comma_words(input_string: str) -> str:
    """
    Capitalize words in a comma-separated string of alphabetical characters.

    Args:
        input_string (str): A string of words separated by commas, 
                            containing only alphabetical characters.

    Returns:
        str: A new string with each word capitalized.

    Raises:
        ValueError: If the input contains non-alphabetical characters or 
                    is an empty string.
    """
    # Check for empty input
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Validate input contains only alphabetical characters and commas
    if not all(char.isalpha() or char == ',' for char in input_string):
        raise ValueError("Input must contain only alphabetical characters and commas")
    
    # Split the string by commas and capitalize each word
    words = input_string.split(',')
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words back together with commas
    return ','.join(capitalized_words)