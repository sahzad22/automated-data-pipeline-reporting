import logging
from .config import DB_URL, API_URL
from .api_client import fetch_products
from .transform import transform_products
from .validate import validate_products
from .database import get_engine, load_products, create_pipeline_audit
from .powerbi_refresh import trigger_powerbi_refresh

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


def run():
    engine = get_engine(DB_URL)
    records_loaded = 0

    try:
        logging.info("Starting pipeline | API=%s", API_URL)

        records = fetch_products()
        df = transform_products(records)
        validate_products(df)
        records_loaded = len(df)

        load_products(df, engine)
        refresh_result = trigger_powerbi_refresh()

        message = f"SQL load completed; Power BI refresh: {refresh_result['status']}"
        create_pipeline_audit(engine, "SUCCESS", records_loaded, message)

        logging.info("Pipeline completed | rows=%s | %s", records_loaded, message)
        print(f"SUCCESS: loaded {records_loaded} records")
        print(f"Power BI refresh: {refresh_result['status']}")

    except Exception as exc:
        logging.exception("Pipeline failed")
        try:
            create_pipeline_audit(engine, "FAILED", records_loaded, str(exc))
        finally:
            raise


if __name__ == "__main__":
    run()
