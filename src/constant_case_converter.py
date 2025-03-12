import re

def to_constant_case(input_string: str) -> str:
    """
    Convert a given string to CONSTANT_CASE.
    
    This function handles various input formats including:
    - camelCase
    - snake_case
    - PascalCase
    - kebab-case
    - Spaces
    
    Args:
        input_string (str): The input string to convert
    
    Returns:
        str: The input string converted to CONSTANT_CASE
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("helloWorld")
        'HELLO_WORLD'
        >>> to_constant_case("hello_world")
        'HELLO_WORLD'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace hyphens with spaces
    input_string = input_string.replace('-', ' ')
    
    # Insert spaces before capital letters 
    # (handles camelCase and PascalCase)
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', input_string)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)
    
    # Replace underscores and multiple spaces with single space
    normalized = re.sub(r'[_\s]+', ' ', s2)
    
    # Convert to uppercase and replace spaces with underscores
    return normalized.strip().upper().replace(' ', '_')