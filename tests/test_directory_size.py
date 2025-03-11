import os
import pytest
import tempfile
import shutil

from src.directory_size import calculate_directory_total_size


def test_empty_directory():
    """Test calculating size of an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert calculate_directory_total_size(temp_dir) == 0


def test_directory_with_multiple_files():
    """Test calculating size of a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test files with known sizes
        with open(os.path.join(temp_dir, 'file1.txt'), 'wb') as f:
            f.write(b'1' * 100)  # 100 bytes
        
        with open(os.path.join(temp_dir, 'file2.txt'), 'wb') as f:
            f.write(b'2' * 200)  # 200 bytes
        
        assert calculate_directory_total_size(temp_dir) == 300


def test_nested_directory():
    """Test calculating size of files in nested directories."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        nested_dir = os.path.join(temp_dir, 'nested')
        os.makedirs(nested_dir)
        
        with open(os.path.join(temp_dir, 'root_file.txt'), 'wb') as f:
            f.write(b'1' * 50)  # 50 bytes
        
        with open(os.path.join(nested_dir, 'nested_file.txt'), 'wb') as f:
            f.write(b'2' * 150)  # 150 bytes
        
        assert calculate_directory_total_size(temp_dir) == 200


def test_nonexistent_directory():
    """Test that FileNotFoundError is raised for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        calculate_directory_total_size('/path/to/nonexistent/directory')


def test_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            calculate_directory_total_size(temp_file.name)