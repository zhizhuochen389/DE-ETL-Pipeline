# ETL Data Pipeline Project

## Overview

This project is a Python-based ETL (Extract, Transform, Load) data pipeline.

The pipeline extracts user data from a public REST API, transforms and cleans the data, loads the processed data into a SQLite database, and performs data validation to ensure data quality.

## ETL Workflow

The pipeline follows the following workflow:

1. **Extract**
   - Retrieves user data from a REST API.
   - Saves the raw data as JSON.

2. **Transform**
   - Reads the raw JSON data.
   - Cleans and transforms the records.
   - Saves the processed data as CSV.

3. **Load**
   - Loads the cleaned data into a SQLite database.

4. **Validation**
   - Checks whether the database and users table exist.
   - Checks the total number of records.
   - Detects missing values in critical fields.

## Project Structure

```text
DE_Project_1/
│
├── data/
│   ├── raw/
│   │   └── users.json
│   └── processed/
│       └── users_cleaned.csv
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
├── .gitignore
├── README.md
└── test.py
```

## Technologies Used

- Python
- REST API
- JSON
- CSV
- SQLite
- SQL
- Git
- Logging
- Data Validation

## Running the Pipeline

Run the complete ETL pipeline from the project root directory:

```bash
python src/pipeline.py
```

The pipeline will execute:

```text
Extract → Transform → Load → Validation
```

A successful run will display:

```text
ETL Pipeline Completed Successfully
```

## Data Quality Checks

The validation stage checks:

- Database existence
- Table existence
- Total record count
- Missing critical fields

## Key Features

- Automated end-to-end ETL pipeline
- REST API data extraction
- Data cleaning and transformation
- SQLite database storage
- Data validation
- Error handling
- Pipeline logging
- Modular Python project structure