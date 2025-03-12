import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_graph():
    """Test a simple graph with a known max flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 14

def test_no_path_graph():
    """Test a graph with no path between source and sink."""
    graph = {
        0: {1: 10},
        1: {2: 5},
        2: {},
        3: {}
    }
    assert edmonds_karp(graph, 0, 3) == 0

def test_complex_graph():
    """Test a more complex graph with multiple paths."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1, 4: 2},
        2: {4: 2},
        3: {5: 2},
        4: {3: 1, 5: 3},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 4

def test_graph_with_multiple_path_selections():
    """Test a graph where multiple path selections matter."""
    graph = {
        0: {1: 1000, 2: 1000},
        1: {2: 1, 3: 1000},
        2: {3: 1000},
        3: {}
    }
    assert edmonds_karp(graph, 0, 3) == 2000

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError."""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        edmonds_karp({}, 0, 1)

def test_invalid_source_sink_raises_error():
    """Test that invalid source or sink nodes raise a ValueError."""
    graph = {1: {2: 10}, 2: {}}
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        edmonds_karp(graph, 0, 1)
    
    with pytest.raises(ValueError, match="Source or sink node not in graph"):
        edmonds_karp(graph, 1, 3)

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {0: {}}
    assert edmonds_karp(graph, 0, 0) == 0

def test_disconnected_nodes():
    """Test a graph where source and sink are not connected."""
    graph = {
        0: {},
        1: {2: 10},
        2: {},
        3: {}
    }
    assert edmonds_karp(graph, 0, 3) == 0