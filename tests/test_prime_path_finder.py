import pytest
from src.prime_path_finder import find_prime_path, is_prime

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(29) == True
    
    # Test non-prime numbers
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(15) == False
    assert is_prime(0) == False
    assert is_prime(-7) == False

def test_find_prime_path_basic():
    # Simple grid with a clear prime path
    grid = [
        [2, 3, 5],
        [7, 11, 13],
        [17, 19, 23]
    ]
    path = find_prime_path(grid)
    assert path is not None
    assert len(path) >= 3
    # Verify all path coordinates have prime values
    path_values = [grid[x][y] for x, y in path]
    assert all(is_prime(val) for val in path_values)

def test_find_prime_path_no_path():
    # Grid with no prime path
    grid = [
        [4, 6, 8],
        [9, 12, 15],
        [16, 18, 20]
    ]
    path = find_prime_path(grid)
    assert path is None

def test_find_prime_path_edge_cases():
    # Empty grid
    assert find_prime_path([]) is None
    
    # Single cell grid
    assert find_prime_path([[2]]) is not None
    assert find_prime_path([[4]]) is None

def test_find_prime_path_complex():
    # More complex grid with multiple possible paths
    grid = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29, 31, 37]
    ]
    path = find_prime_path(grid)
    assert path is not None
    assert len(path) >= 3
    
    # Validate path forms a prime sequence
    path_values = [grid[x][y] for x, y in path]
    assert all(is_prime(val) for val in path_values)

def test_find_prime_path_negative_numbers():
    # Grid with negative numbers
    grid = [
        [-2, 3, -5],
        [7, -11, 13],
        [-17, 19, 23]
    ]
    path = find_prime_path(grid)
    assert path is not None
    assert len(path) >= 3
    
    # Validate path forms a prime sequence
    path_values = [grid[x][y] for x, y in path]
    assert all(is_prime(abs(val)) for val in path_values)

def test_find_prime_path_movement():
    # Test that path can move in all 4 directions
    grid = [
        [2, 3, 5],
        [7, 11, 13],
        [17, 19, 23]
    ]
    path = find_prime_path(grid)
    assert path is not None
    
    # Check that path coordinates are adjacent
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i+1]
        # Manhattan distance of 1 indicates adjacent cells
        assert abs(x1 - x2) + abs(y1 - y2) == 1