from typing import List, Tuple, Optional

def is_prime(n: int) -> bool:
    """
    Check if a given number is prime.
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    n = abs(n)  # Handle negative numbers
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid: List[List[int]]) -> Optional[List[Tuple[int, int]]]:
    """
    Find a continuous path of prime numbers in the grid.
    
    Args:
        grid (List[List[int]]): 2D grid of integers
    
    Returns:
        Optional[List[Tuple[int, int]]]: Path of coordinates forming a prime number sequence,
        or None if no such path exists
    """
    if not grid:
        return None
    
    # Handle single cell grid
    if len(grid) == 1 and len(grid[0]) == 1:
        return [(0, 0)] if is_prime(grid[0][0]) else None
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(x: int, y: int, path: List[Tuple[int, int]], current_num: int) -> Optional[List[Tuple[int, int]]]:
        # Check bounds and visited status
        if (x < 0 or x >= rows or y < 0 or y >= cols or 
            visited[x][y] or not is_prime(abs(grid[x][y])) or 
            not is_prime(abs(current_num))):
            return None
        
        # Mark current cell as visited and add to path
        visited[x][y] = True
        path.append((x, y))
        
        # If path length is 3 or more and forms a valid prime sequence, return path
        if len(path) >= 3:
            return path
        
        # Try all 4 directions
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            # Skip if out of bounds
            if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                continue
            
            # Construct next number by appending digits
            next_num = current_num * 10 + abs(grid[new_x][new_y])
            
            # Recursively search from the new position
            result = dfs(new_x, new_y, path.copy(), next_num)
            if result:
                return result
        
        return None
    
    # Try starting DFS from each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Reset visited for each starting point
            visited = [[False] * cols for _ in range(rows)]
            result = dfs(i, j, [], abs(grid[i][j]))
            if result:
                return result
    
    return None