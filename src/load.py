import csv
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

csv_file = "data/processed/users_cleaned.csv"

connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

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
            INSERT INTO users (
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
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET
                name = EXCLUDED.name,
                username = EXCLUDED.username,
                email = EXCLUDED.email,
                phone = EXCLUDED.phone,
                website = EXCLUDED.website,
                city = EXCLUDED.city,
                zipcode = EXCLUDED.zipcode,
                company = EXCLUDED.company
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

print("Data loaded into PostgreSQL database: sql_practice")