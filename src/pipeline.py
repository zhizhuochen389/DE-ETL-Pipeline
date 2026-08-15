import subprocess
import sys
import logging


# Configure logging
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


print("===== ETL Pipeline Started =====")
logging.info("ETL Pipeline started")


try:
    # 1. Extract
    print("\n1. Running Extract...")
    logging.info("Extract started")

    subprocess.run(
        [sys.executable, "src/extract.py"],
        check=True
    )

    logging.info("Extract completed successfully")


    # 2. Transform
    print("\n2. Running Transform...")
    logging.info("Transform started")

    subprocess.run(
        [sys.executable, "src/transform.py"],
        check=True
    )

    logging.info("Transform completed successfully")


    # 3. Load
    print("\n3. Running Load...")
    logging.info("Load started")

    subprocess.run(
        [sys.executable, "src/load.py"],
        check=True
    )

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