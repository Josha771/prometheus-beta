def count_triangular_numbers(n):
    """
    Count the number of triangular numbers less than or equal to n.
    
    A triangular number is a number that can be represented as a triangular 
    grid of points where the first row contains a single element and each 
    subsequent row contains one more element than the previous one.
    
    Triangular numbers follow the formula: T(k) = k * (k + 1) // 2
    
    Args:
        n (int): The upper limit to count triangular numbers.
    
    Returns:
        int: The count of triangular numbers less than or equal to n.
    
    Raises:
        ValueError: If n is negative.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # If n is 0, return 0
    if n == 0:
        return 0
    
    # Count triangular numbers using the inverse triangular number formula
    # The kth triangular number is k * (k + 1) // 2
    # We want to find the largest k such that k * (k + 1) // 2 <= n
    k = int((2 * n + 0.25)**0.5 - 0.5)
    
    return k