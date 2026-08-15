import json

with open("data/raw/users.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Number of records:", len(data))
print(data[0])
cleaned_data = []

for user in data:
    cleaned_user = {
        "id": user["id"],
        "name": user["name"],
        "username": user["username"],
        "email": user["email"],
        "phone": user["phone"],
        "website": user["website"],
        "city": user["address"]["city"],
        "zipcode": user["address"]["zipcode"],
        "company": user["company"]["name"]
    }

    cleaned_data.append(cleaned_user)

print("Cleaned records:", len(cleaned_data))
print(cleaned_data[0])
import csv

output_file = "data/processed/users_cleaned.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "id",
        "name",
        "username",
        "email",
        "phone",
        "website",
        "city",
        "zipcode",
        "company"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(cleaned_data)

print("Cleaned data saved to:", output_file)