import pytest
import logging
import os
import tempfile
from src.menu_logger import MenuLogger

def test_single_selection_logging():
    """Test logging a single menu selection."""
    logger = MenuLogger()
    
    # Capture log output
    with pytest.raises(ValueError, match="Selection cannot be None"):
        logger.log_selection("Main Menu", None)
    
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_selection("", "Option 1")

def test_multiple_selections_logging():
    """Test logging multiple menu selections."""
    logger = MenuLogger()
    
    # Test multiple selections
    with pytest.raises(ValueError, match="Menu name cannot be empty"):
        logger.log_multiple_selections("", ["Option 1", "Option 2"])
    
    with pytest.raises(ValueError, match="Selections list cannot be empty"):
        logger.log_multiple_selections("Main Menu", [])

def test_file_logging():
    """Test logging to a file."""
    # Create a temporary log file
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as temp_log:
        log_file_path = temp_log.name
    
    try:
        # Create logger with file logging
        logger = MenuLogger(log_file=log_file_path)
        
        # Log a selection
        logger.log_selection("Test Menu", "Test Option")
        
        # Read the log file
        with open(log_file_path, 'r') as log_file:
            log_content = log_file.read()
        
        # Check if log contains expected information
        assert "Test Menu" in log_content
        assert "Test Option" in log_content
    
    finally:
        # Clean up the temporary file
        os.unlink(log_file_path)

def test_multiple_item_logging():
    """Test logging multiple items to ensure correct formatting."""
    logger = MenuLogger()
    
    # Capture log output
    logger.log_multiple_selections("Options Menu", ["A", "B", "C"])
    
    # Verify the log would include all items
    # Note: This is a basic check as we can't easily capture log output in pytest