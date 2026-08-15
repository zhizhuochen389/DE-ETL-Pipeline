import csv
import sqlite3

csv_file = "data/processed/users_cleaned.csv"
db_file = "data/users.db"

connection = sqlite3.connect(db_file)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    phone TEXT,
    website TEXT,
    city TEXT,
    zipcode TEXT,
    company TEXT
)
""")

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
        INSERT OR REPLACE INTO users (
            id,
            name,
            username,
            email,
            phone,
            website,
            city,
            zipcode,
            company
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["id"],
            row["name"],
            row["username"],
            row["email"],
            row["phone"],
            row["website"],
            row["city"],
            row["zipcode"],
            row["company"]
        ))

connection.commit()
connection.close()

print("Data loaded into SQLite database:", db_file)