import pandas as pd

def transform_products(records):
    rows = []
    for p in records:
        rating = p.get("rating") or {}
        rows.append({
            "product_id": p.get("id"),
            "title": p.get("title"),
            "price": p.get("price"),
            "category": p.get("category"),
            "description": p.get("description"),
            "rating": rating.get("rate"),
            "review_count": rating.get("count"),
        })
    df = pd.DataFrame(rows)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce").fillna(0).astype(int)
    df["title"] = df["title"].astype("string").str.strip()
    df["category"] = df["category"].astype("string").str.strip()
    return df
