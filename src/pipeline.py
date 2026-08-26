import logging
from .config import DB_URL, API_URL
from .api_client import fetch_products
from .transform import transform_products
from .validate import validate_products
from .database import get_engine, load_products, create_pipeline_audit

logging.basicConfig(filename="pipeline.log", level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")

def run():
    engine = get_engine(DB_URL)
    try:
        logging.info("Starting pipeline | API=%s", API_URL)
        records = fetch_products()
        df = transform_products(records)
        validate_products(df)
        load_products(df, engine)
        create_pipeline_audit(engine, "SUCCESS", len(df), "Load completed")
        logging.info("Pipeline completed | rows=%s", len(df))
        print(f"SUCCESS: loaded {len(df)} records")
    except Exception as exc:
        logging.exception("Pipeline failed")
        try:
            create_pipeline_audit(engine, "FAILED", 0, str(exc))
        finally:
            raise

if __name__ == "__main__":
    run()
