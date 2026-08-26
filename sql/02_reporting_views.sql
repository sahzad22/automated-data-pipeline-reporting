-- Reporting views are written to work in both SQLite and PostgreSQL.
DROP VIEW IF EXISTS vw_product_reporting;
DROP VIEW IF EXISTS vw_category_summary;

CREATE VIEW vw_product_reporting AS
SELECT
    product_id,
    title,
    category,
    price,
    rating,
    review_count,
    CASE
        WHEN rating >= 4.5 THEN 'Excellent'
        WHEN rating >= 4.0 THEN 'Strong'
        WHEN rating >= 3.0 THEN 'Average'
        ELSE 'Needs Review'
    END AS rating_band,
    CASE
        WHEN price < 25 THEN 'Budget'
        WHEN price < 75 THEN 'Mid-Market'
        ELSE 'Premium'
    END AS price_band
FROM raw_products;

CREATE VIEW vw_category_summary AS
SELECT
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(price), 2) AS avg_price,
    ROUND(AVG(rating), 2) AS avg_rating,
    SUM(review_count) AS total_reviews
FROM raw_products
GROUP BY category;
