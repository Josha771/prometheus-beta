import io
import sys
import pytest
from contextlib import redirect_stdout
from src.progress_logger import ProgressBar, log_with_progress

def test_progress_bar_initialization():
    """Test initialization of ProgressBar"""
    pb = ProgressBar(total=100)
    assert pb.total == 100
    assert pb.current == 0
    assert pb.prefix == 'Progress:'
    assert pb.suffix == 'Complete'

def test_progress_bar_update():
    """Test updating progress bar"""
    pb = ProgressBar(total=10)
    
    # Capture stdout
    f = io.StringIO()
    with redirect_stdout(f):
        pb.update(5)
    
    # Check output contains expected elements
    output = f.getvalue()
    assert '50.0%' in output
    assert '█' in output

def test_progress_bar_iteration():
    """Test using progress bar as an iterator"""
    total = 5
    count = 0
    
    f = io.StringIO()
    with redirect_stdout(f):
        for _ in ProgressBar(total):
            count += 1
    
    # Verify iteration and final percentage
    assert count == total
    output = f.getvalue()
    assert '100.0%' in output

def test_log_with_progress():
    """Test log_with_progress wrapper function"""
    test_list = list(range(10))
    
    f = io.StringIO()
    with redirect_stdout(f):
        tracked_list = list(log_with_progress(test_list, prefix='Test'))
    
    output = f.getvalue()
    assert 'Test' in output
    assert '100.0%' in output
    assert tracked_list == test_list

def test_progress_bar_edge_cases():
    """Test edge cases for progress bar"""
    # Test with zero total
    with pytest.raises(ZeroDivisionError):
        ProgressBar(total=0)
    
    # Test with negative total
    with pytest.raises(TypeError):
        ProgressBar(total=-10)

def test_progress_bar_custom_parameters():
    """Test custom initialization parameters"""
    pb = ProgressBar(
        total=100, 
        prefix='Custom', 
        suffix='Done', 
        decimals=2, 
        length=30, 
        fill='#'
    )
    
    f = io.StringIO()
    with redirect_stdout(f):
        pb.update(50)
    
    output = f.getvalue()
    assert 'Custom' in output
    assert 'Done' in output
    assert '50.00%' in output
    assert '#' in output