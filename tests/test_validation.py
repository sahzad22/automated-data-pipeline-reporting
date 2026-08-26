import pandas as pd
import pytest

from src.validate import validate_products


def valid_df():
    return pd.DataFrame([
        {"product_id": 1, "title": "Product A", "price": 20.0, "category": "electronics", "rating": 4.5},
        {"product_id": 2, "title": "Product B", "price": 50.0, "category": "books", "rating": 3.8},
    ])


def test_valid_products_pass():
    validate_products(valid_df())


def test_negative_price_fails():
    df = valid_df()
    df.loc[0, "price"] = -1
    with pytest.raises(ValueError, match="Negative product prices"):
        validate_products(df)


def test_invalid_rating_fails():
    df = valid_df()
    df.loc[0, "rating"] = 6
    with pytest.raises(ValueError, match="Rating outside"):
        validate_products(df)


def test_duplicate_product_id_fails():
    df = valid_df()
    df.loc[1, "product_id"] = 1
    with pytest.raises(ValueError, match="Duplicate product IDs"):
        validate_products(df)
