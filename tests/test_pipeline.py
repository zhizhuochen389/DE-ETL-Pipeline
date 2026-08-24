from unittest.mock import patch

from src.pipeline import run_pipeline


@patch("src.pipeline.subprocess.run")
@patch("src.pipeline.load_users")
@patch("src.pipeline.transform_users")
@patch("src.pipeline.extract_users")
def test_run_pipeline(
    mock_extract,
    mock_transform,
    mock_load,
    mock_subprocess
):
    raw_data = [
        {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "TEST@EXAMPLE.COM"
        }
    ]

    transformed_data = [
        {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
    ]

    mock_extract.return_value = raw_data
    mock_transform.return_value = transformed_data

    run_pipeline()

    mock_extract.assert_called_once_with()
    mock_transform.assert_called_once_with(raw_data)
    mock_load.assert_called_once_with(transformed_data)
    mock_subprocess.assert_called_once()