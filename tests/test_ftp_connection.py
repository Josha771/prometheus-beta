import pytest
import ftplib
import socket
from unittest.mock import patch, MagicMock

from src.ftp_connection import establish_ftp_connection

class TestFTPConnection:
    def test_successful_connection(self):
        """Test successful FTP connection"""
        with patch('ftplib.FTP') as mock_ftp:
            mock_ftp_instance = MagicMock()
            mock_ftp.return_value = mock_ftp_instance

            connection = establish_ftp_connection('example.com', 'testuser', 'testpass')
            
            assert connection == mock_ftp_instance
            mock_ftp.assert_called_once()
            mock_ftp_instance.connect.assert_called_once_with(host='example.com', port=21)
            mock_ftp_instance.login.assert_called_once_with(user='testuser', passwd='testpass')

    def test_empty_parameters(self):
        """Test that empty parameters raise ValueError"""
        with pytest.raises(ValueError, match="Host, username, and password must be non-empty"):
            establish_ftp_connection('', '', '')
        
        with pytest.raises(ValueError, match="Host, username, and password must be non-empty"):
            establish_ftp_connection(None, None, None)

    def test_connection_timeout(self):
        """Test connection timeout scenario"""
        with patch('ftplib.FTP', side_effect=socket.timeout):
            with pytest.raises(ConnectionRefusedError, match="Connection to"):
                establish_ftp_connection('example.com', 'testuser', 'testpass')

    def test_connection_refused(self):
        """Test connection refused scenario"""
        with patch('ftplib.FTP', side_effect=ConnectionRefusedError("Connection failed")):
            with pytest.raises(ConnectionRefusedError, match="Failed to connect to FTP server"):
                establish_ftp_connection('example.com', 'testuser', 'testpass')

    def test_authentication_error(self):
        """Test authentication error scenario"""
        with patch('ftplib.FTP') as mock_ftp:
            mock_ftp_instance = MagicMock()
            mock_ftp_instance.login.side_effect = ftplib.error_perm("Login failed")
            mock_ftp.return_value = mock_ftp_instance

            with pytest.raises(RuntimeError, match="FTP authentication or connection error"):
                establish_ftp_connection('example.com', 'baduser', 'badpass')

    def test_custom_port(self):
        """Test connection with custom port"""
        with patch('ftplib.FTP') as mock_ftp:
            mock_ftp_instance = MagicMock()
            mock_ftp.return_value = mock_ftp_instance

            connection = establish_ftp_connection('example.com', 'testuser', 'testpass', port=2121)
            
            mock_ftp_instance.connect.assert_called_once_with(host='example.com', port=2121)

    def test_custom_timeout(self):
        """Test connection with custom timeout"""
        with patch('ftplib.FTP') as mock_ftp:
            mock_ftp_instance = MagicMock()
            mock_ftp.return_value = mock_ftp_instance

            connection = establish_ftp_connection('example.com', 'testuser', 'testpass', timeout=10)
            
            mock_ftp.assert_called_once_with(timeout=10)