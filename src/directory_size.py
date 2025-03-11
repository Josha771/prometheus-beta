import os


def calculate_directory_total_size(directory_path):
    """
    Calculate the total size of all files in a given directory.

    Args:
        directory_path (str): Path to the directory to calculate file sizes for.

    Returns:
        int: Total size of all files in bytes.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are permission issues accessing files.
    """
    # Validate input is a directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Specified path is not a directory: {directory_path}")
    
    total_size = 0
    
    # Walk through directory and calculate total file size
    try:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Handle symbolic links and avoid errors with unreadable files
                if os.path.isfile(file_path) and not os.path.islink(file_path):
                    try:
                        total_size += os.path.getsize(file_path)
                    except (OSError, PermissionError):
                        # Skip files that can't be read
                        continue
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing directory: {directory_path}")
    
    return total_size