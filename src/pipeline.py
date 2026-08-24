import subprocess
import sys
import logging

from src.extract import extract_users
from src.transform import transform_users
from src.load import load_users


# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def run_pipeline():
    print("===== ETL Pipeline Started =====")
    logging.info("ETL Pipeline started")

    try:
        # 1. Extract
        print("\n1. Running Extract...")
        logging.info("Extract started")

        raw_data = extract_users()

        logging.info("Extract completed successfully")

        # 2. Transform
        print("\n2. Running Transform...")
        logging.info("Transform started")

        transformed_data = transform_users(raw_data)

        logging.info("Transform completed successfully")

        # 3. Load
        print("\n3. Running Load...")
        logging.info("Load started")

        load_users()

        logging.info("Load completed successfully")

        # 4. Validation
        print("\n4. Running Validation...")
        logging.info("Validation started")

        subprocess.run(
            [sys.executable, "src/validate.py"],
            check=True
        )

        logging.info("Validation completed successfully")

        print("\n===== ETL Pipeline Completed Successfully =====")
        logging.info("ETL Pipeline completed successfully")

    except Exception as error:
        print("\n===== ETL Pipeline Failed =====")
        logging.exception(f"ETL Pipeline failed: {error}")
        raise


if __name__ == "__main__":
    run_pipeline()