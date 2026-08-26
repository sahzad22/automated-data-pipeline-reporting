# Automated Data Pipeline & Reporting System

> **Python • REST API • SQL • Power BI • Automation**

## Executive Summary

A production-style reporting pipeline that retrieves product data from a REST API, validates and transforms the payload, loads it into a relational SQL database, creates analytics-ready views, and optionally triggers a Power BI dataset refresh.

**REST API → Python ETL → SQL Database → Reporting Views → Power BI → Automated Refresh**

### Business Scenario

A retail/e-commerce team needs a reliable daily view of its product catalog without manually downloading spreadsheets, cleaning data, or rebuilding reports.

The solution supports product count, pricing, ratings, review trends, category performance, data-quality checks, and pipeline health.

## Architecture

```text
REST API
   ↓ JSON
Python ETL
   ├─ Extract
   ├─ Validate
   └─ Transform
   ↓
SQL Database
   ├─ raw_products
   ├─ pipeline_runs
   └─ reporting views
   ↓
Power BI
   ├─ KPI dashboard
   ├─ Category analysis
   ├─ Catalog quality
   └─ Pipeline health
```

## What This Demonstrates

| Capability | Implementation |
|---|---|
| API integration | REST GET with timeout/retry handling |
| ETL | Python extraction, transformation and load |
| Data quality | Required-field, type, range and duplicate checks |
| SQL | Relational tables and analytics views |
| Automation | Single-command pipeline runner |
| BI | Power BI-ready reporting model and DAX |
| Monitoring | Pipeline audit table and logs |
| Production thinking | Environment variables and failure handling |

## Quick Start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m src.pipeline
```

The default configuration uses SQLite, so the project can run locally without a database server.

## Power BI

Connect Power BI to `vw_product_reporting` and build four pages: Executive Overview, Category Analysis, Catalog Quality, and Pipeline Health.

Recommended measures are documented in `powerbi/DAX_MEASURES.md`.

The optional Power BI REST API refresh integration is documented in `src/powerbi_refresh.py` and controlled through environment variables.

## Production Extensions

- Incremental loads with `updated_at`
- PostgreSQL/Azure SQL
- Azure Key Vault for secrets
- Airflow / Azure Data Factory orchestration
- dbt / Great Expectations testing
- Teams or email alerts for failed runs
- GitHub Actions scheduling

## Resume-ready statement

> Built a Python-based automated reporting pipeline that ingests REST API data, validates and transforms records, loads them into SQL, creates analytics-ready reporting views, and triggers Power BI dataset refreshes—replacing repetitive manual data pulls with a repeatable reporting workflow.
