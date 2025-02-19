def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all multiples of the given numbers up to a limit.

    Args:
        limit (int): The upper bound for finding multiples (inclusive).
        multiples (list): A list of positive integers to find multiples of.

    Returns:
        int: The sum of all unique multiples of the numbers in the list up to the limit.

    Raises:
        ValueError: If limit or any number in multiples is less than or equal to 0.
    """
    # Validate input
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    
    if not all(multiple > 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers.")
    
    # Use a set to store unique multiples to avoid duplicates
    unique_multiples = set()
    
    # Find multiples for each number in the multiples list
    for multiple in multiples:
        # Start from the first multiple that doesn't exceed the limit
        for num in range(multiple, limit + 1, multiple):
            unique_multiples.add(num)
    
    # Return the sum of unique multiples
    return sum(unique_multiples)