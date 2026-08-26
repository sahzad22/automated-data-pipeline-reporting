import pandas as pd

REQUIRED = {"product_id", "title", "price", "category", "rating"}

def validate_products(df: pd.DataFrame):
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df["product_id"].isna().any():
        raise ValueError("Product IDs cannot be null")
    if (pd.to_numeric(df["price"], errors="coerce") < 0).any():
        raise ValueError("Negative product prices detected")
    rating = pd.to_numeric(df["rating"], errors="coerce")
    if not rating.dropna().between(0, 5).all():
        raise ValueError("Rating outside 0-5 range detected")
    if df["product_id"].duplicated().any():
        raise ValueError("Duplicate product IDs detected")
