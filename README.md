# ETL Data Pipeline Project

## Overview

This project is a Python-based ETL (Extract, Transform, Load) data pipeline.

The pipeline extracts user data from a public REST API, cleans and transforms the data, loads the processed data into a PostgreSQL database, and performs data validation to ensure data quality.

## ETL Workflow

The pipeline follows four main stages:

1. **Extract**
   - Retrieves user data from a REST API.
   - Saves the raw data locally.

2. **Transform**
   - Reads the extracted raw data.
   - Cleans and transforms the records.
   - Saves the processed data as CSV.

3. **Load**
   - Connects to PostgreSQL.
   - Creates the required table if necessary.
   - Loads the cleaned data into the database.

4. **Validation**
   - Verifies the database connection.
   - Checks whether the users table exists.
   - Checks the total number of records.
   - Detects missing values in critical fields.

## Project Structure

```text
DE_Project_1/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│   └── pipeline.log
│
├── sql/
│   └── queries.sql
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── validate.py
│   └── pipeline.py
│
├── .env
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── test.py
```

## Technologies Used

- Python
- PostgreSQL
- REST API
- JSON
- CSV
- SQL
- Git
- GitHub
- python-dotenv
- psycopg2

## Environment Variables

Database credentials are stored in a local `.env` file.

For security reasons, the `.env` file is excluded from Git.

An `.env.example` file is provided as a template:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sql_practice
DB_USER=postgres
DB_PASSWORD=your_password_here
```

Create your own `.env` file and replace the example values with your PostgreSQL credentials.

## Installation

Clone the repository and install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Pipeline

Run the complete ETL pipeline from the project root directory:

```bash
python src/pipeline.py
```

The pipeline executes:

```text
Extract → Transform → Load → Validation
```

A successful run will display:

```text
ETL Pipeline Completed Successfully
```

## Data Quality Checks

The validation stage checks:

- Database connection
- Users table existence
- Total record count
- Missing critical fields

## Logging

Pipeline execution information and errors are recorded in:

```text
logs/pipeline.log
```

This makes it easier to monitor pipeline execution and troubleshoot failures.

## SQL

SQL queries used by the project are stored in:

```text
sql/queries.sql
```

## Key Features

- Automated end-to-end ETL pipeline
- REST API data extraction
- Data cleaning and transformation
- PostgreSQL database integration
- Environment-variable based credential management
- Data validation
- Error handling
- Pipeline logging
- Modular Python project structure
- Git and GitHub version control