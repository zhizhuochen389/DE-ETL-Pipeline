import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Number of records:", len(data))
print(data[0])
import json

with open("data/raw/users.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("Data saved to data/raw/users.json")