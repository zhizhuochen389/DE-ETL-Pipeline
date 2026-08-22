from unittest.mock import patch, MagicMock

from src.extract import extract_users


@patch("src.extract.requests.get")
@patch("src.extract.open")
def test_extract_users(mock_open, mock_get):
    fake_data = [
        {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
    ]

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = fake_data
    mock_get.return_value = mock_response

    mock_file = MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file

    result = extract_users()

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users"
    )
    mock_response.raise_for_status.assert_called_once()
    mock_response.json.assert_called_once()

    assert result == fake_data