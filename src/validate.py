import sqlite3
import os

db_file = "data/users.db"

print("===== Starting Data Validation =====")

# 1. Check database exists
if not os.path.exists(db_file):
    raise FileNotFoundError("Database file does not exist!")

print("✓ Database exists")

# 2. Connect to database
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# 3. Check users table exists
cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table' AND name='users';
""")

if cursor.fetchone() is None:
    raise Exception("users table does not exist!")

print("✓ users table exists")

# 4. Check number of records
cursor.execute("SELECT COUNT(*) FROM users;")
count = cursor.fetchone()[0]

print(f"✓ Total records: {count}")

if count == 0:
    raise Exception("users table is empty!")

# 5. Check important fields for NULL values
cursor.execute("""
SELECT COUNT(*)
FROM users
WHERE name IS NULL
   OR email IS NULL
   OR city IS NULL;
""")

null_count = cursor.fetchone()[0]

print(f"✓ Records with missing critical fields: {null_count}")

if null_count > 0:
    raise Exception("Missing values found!")

connection.close()

print("===== Data Validation Passed =====")