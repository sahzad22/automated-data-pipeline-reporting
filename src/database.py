from datetime import datetime, timezone
from sqlalchemy import create_engine, text

def get_engine(db_url):
    return create_engine(db_url, future=True)

def load_products(df, engine):
    df.to_sql("raw_products", engine, if_exists="replace", index=False)

def create_pipeline_audit(engine, status, records, message=""):
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS pipeline_runs (
                run_id INTEGER PRIMARY KEY AUTOINCREMENT,
                run_timestamp TEXT NOT NULL,
                status TEXT NOT NULL,
                records_loaded INTEGER NOT NULL,
                message TEXT
            )
        """))
        conn.execute(text("""
            INSERT INTO pipeline_runs
            (run_timestamp, status, records_loaded, message)
            VALUES (:ts, :status, :records, :message)
        """), {
            "ts": datetime.now(timezone.utc).isoformat(),
            "status": status,
            "records": records,
            "message": message
        })
