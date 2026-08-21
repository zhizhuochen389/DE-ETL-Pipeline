from src.transform import transform_users


def test_transform_users():
    raw_users = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "SINCERE@APRIL.BIZ",
            "address": {
                "city": "Gwenborough",
                "zipcode": "92998-3874"
            },
            "phone": "1-770-736-8031",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona"
            }
        }
    ]

    result = transform_users(raw_users)

    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Leanne Graham"
    assert result[0]["email"] == "SINCERE@APRIL.BIZ"
    assert result[0]["city"] == "Gwenborough"


def test_transform_email_to_lowercase():
    raw_users = [
        {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "TEST@EXAMPLE.COM",
            "address": {
                "city": "Sydney",
                "zipcode": "2000"
            },
            "phone": "123456789",
            "website": "example.com",
            "company": {
                "name": "Test Company"
            }
        }
    ]

    result = transform_users(raw_users)

    assert result[0]["email"] == "TEST@EXAMPLE.COM"
def test_transform_empty_list():
    result = transform_users([])

    assert result == []