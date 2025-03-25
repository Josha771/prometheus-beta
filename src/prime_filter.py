def filter_primes(numbers):
    """
    Filter and return only prime numbers from the given list.
    
    Args:
        numbers (list): A list of integers to filter for prime numbers.
    
    Returns:
        list: A list containing only the prime numbers from the input list.
    
    Notes:
        - Handles both positive and negative numbers
        - 1 and numbers less than 1 are not considered prime
        - 2 is the smallest prime number
        - Negative primes use absolute primality
    """
    def is_prime(n):
        # Handle non-prime cases first
        if n < 2:
            return False
        
        # Check for primality using trial division
        # Use abs() to handle negative numbers
        n = abs(n)
        
        # Optimization: only check up to square root of the number
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    # Use list comprehension to filter prime numbers, keeping sign for output
    return [num for num in numbers if is_prime(abs(num))]