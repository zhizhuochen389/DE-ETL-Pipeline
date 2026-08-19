import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

print("===== Starting Data Validation =====")

# 1. Connect to PostgreSQL
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

cursor = connection.cursor()

print("✓ Database connection successful")

# 2. Check users table exists
cursor.execute("""
SELECT EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'public'
      AND table_name = 'users'
);
""")

table_exists = cursor.fetchone()[0]

if not table_exists:
    raise Exception("users table does not exist!")

print("✓ users table exists")

# 3. Check number of records
cursor.execute("SELECT COUNT(*) FROM users;")
count = cursor.fetchone()[0]

print(f"✓ Total records: {count}")

if count == 0:
    raise Exception("users table is empty!")

# 4. Check important fields for NULL values
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