def get_unique_coordinate_combinations(coordinates):
    """
    Generate a list of unique coordinate combinations in ascending order.

    Args:
        coordinates (list): A list of coordinate pairs, where each pair is a tuple (x, y)

    Returns:
        list: A sorted list of unique coordinate combinations (x, y)

    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not valid tuples of two elements
    """
    # Validate input
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Validate each coordinate pair
    for coord in coordinates:
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise ValueError("Each coordinate must be a tuple of two elements")
        
        try:
            x, y = map(float, coord)
        except (TypeError, ValueError):
            raise TypeError("Coordinates must be numeric values")
    
    # Convert to set to remove duplicates, then sort
    unique_coords = sorted(set(coordinates))
    
    return unique_coords