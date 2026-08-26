# Power BI DAX Measures

```DAX
Product Count = DISTINCTCOUNT(vw_product_reporting[product_id])

Average Price = AVERAGE(vw_product_reporting[price])

Average Rating = AVERAGE(vw_product_reporting[rating])

Total Reviews = SUM(vw_product_reporting[review_count])

Premium Product % =
DIVIDE(
    CALCULATE([Product Count], vw_product_reporting[price_band] = "Premium"),
    [Product Count]
)

High Rated Product % =
DIVIDE(
    CALCULATE([Product Count], vw_product_reporting[rating] >= 4),
    [Product Count]
)
```

Recommended pages: Executive Overview, Category Analysis, Catalog Quality and Pipeline Health.
