from typing import List, Dict, Optional
from collections import deque

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph
            where keys are nodes and values are dictionaries of adjacent nodes and their capacities.
        source (int): The source node from which flow originates.
        sink (int): The sink node where flow terminates.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
        ValueError: If graph is empty or invalid.
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph (deep copy of the original graph)
    def create_residual_graph():
        residual = {}
        for node, edges in graph.items():
            residual[node] = edges.copy()
        return residual
    
    # Find an augmenting path using BFS
    def bfs(residual_graph: Dict[int, Dict[int, int]]) -> Optional[List[int]]:
        visited = set()
        parent = {}
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # If we've reached the sink, reconstruct and return the path
            if current == sink:
                path = []
                while current in parent:
                    path.append(current)
                    current = parent[current]
                path.append(source)
                return list(reversed(path))
            
            # Explore neighbors
            for neighbor, capacity in residual_graph.get(current, {}).items():
                if neighbor not in visited and capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
        
        return None
    
    # Initialize max flow
    max_flow = 0
    
    # Create residual graph
    residual_graph = create_residual_graph()
    
    # Find augmenting paths
    while True:
        # Find an augmenting path
        path = bfs(residual_graph)
        
        # No more augmenting paths exist
        if not path:
            break
        
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            path_flow = min(path_flow, residual_graph[u].get(v, 0))
        
        # Update residual capacities
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            
            # Reduce forward edge capacity
            residual_graph[u][v] -= path_flow
            
            # Add/update reverse edge for potential flow reduction
            if v not in residual_graph:
                residual_graph[v] = {}
            residual_graph[v][u] = residual_graph[v].get(u, 0) + path_flow
        
        # Add to max flow
        max_flow += path_flow
    
    return max_flow