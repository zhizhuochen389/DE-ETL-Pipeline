from unittest.mock import patch, MagicMock

from src.load import load_users


@patch("src.load.psycopg2.connect")
def test_load_users_connects_to_database(mock_connect):
    mock_connection = MagicMock()
    mock_cursor = MagicMock()

    mock_connect.return_value = mock_connection
    mock_connection.cursor.return_value = mock_cursor

    with patch("src.load.open", mock_open := MagicMock()):
        mock_open.return_value.__enter__.return_value = []

        load_users()

    mock_connect.assert_called_once()
    mock_connection.cursor.assert_called_once()
    mock_connection.commit.assert_called_once()
    mock_connection.close.assert_called_once()