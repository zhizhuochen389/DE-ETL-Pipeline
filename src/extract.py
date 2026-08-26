import json
import requests


def extract_users():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print("Status Code:", response.status_code)
    print("Number of records:", len(data))

    with open("data/raw/users.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("Data saved to data/raw/users.json")

    return data


if __name__ == "__main__":
    extract_users()  