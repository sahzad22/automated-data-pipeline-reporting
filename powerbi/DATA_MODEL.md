# Power BI Data Model

Connect Power BI to the SQL view `vw_product_reporting`.

## Core fields

- `product_id` — unique product key
- `title` — product name
- `category` — business category
- `price` — product price
- `rating` — average customer rating
- `review_count` — number of reviews
- `rating_band` — derived quality segment
- `price_band` — derived commercial segment

## Recommended report pages

1. **Executive Overview** — product count, average price, average rating, total reviews
2. **Category Analysis** — price and rating comparison by category
3. **Catalog Quality** — rating bands, price bands and products needing review
4. **Pipeline Health** — latest run status, timestamp and records loaded
