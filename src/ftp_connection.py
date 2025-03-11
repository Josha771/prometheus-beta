import ftplib
import socket

def establish_ftp_connection(host, username, password, port=21, timeout=30):
    """
    Establish a secure FTP connection to a given host.

    Args:
        host (str): The FTP server hostname or IP address.
        username (str): The username for authentication.
        password (str): The password for authentication.
        port (int, optional): The port number. Defaults to 21.
        timeout (int, optional): Connection timeout in seconds. Defaults to 30.

    Returns:
        ftplib.FTP: An established FTP connection object.

    Raises:
        ValueError: If host, username, or password is empty or invalid.
        ConnectionRefusedError: If the connection to the FTP server fails.
        socket.timeout: If the connection times out.
        ftplib.all_errors: For other FTP-related errors.
    """
    # Validate input parameters
    if not host or not username or not password:
        raise ValueError("Host, username, and password must be non-empty")

    try:
        # Establish FTP connection with timeout
        ftp = ftplib.FTP(timeout=timeout)
        ftp.connect(host=host, port=port)
        
        # Attempt login
        ftp.login(user=username, passwd=password)
        
        return ftp

    except socket.timeout:
        raise ConnectionRefusedError(f"Connection to {host}:{port} timed out after {timeout} seconds")
    except (socket.error, ConnectionRefusedError) as e:
        raise ConnectionRefusedError(f"Failed to connect to FTP server: {str(e)}")
    except ftplib.all_errors as e:
        raise RuntimeError(f"FTP authentication or connection error: {str(e)}")