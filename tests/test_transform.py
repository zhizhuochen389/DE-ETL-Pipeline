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