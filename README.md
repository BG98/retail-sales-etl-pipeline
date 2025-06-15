<<<<<<< HEAD
# Retail Sales ETL Pipeline

## Tools Used
- Python (Pandas)
- Apache Airflow
- Snowflake (simulated here)

## Project Flow
1. Extract: Sales data from raw CSV.
2. Transform: Clean and enrich data.
3. Load: Simulated load to Snowflake (or real if configured).

## Folders
- `dags/` — Airflow DAG
- `scripts/` — Python ETL scripts
- `data/raw/` — Input sales data
- `data/processed/` — Cleaned output

>  **Disclaimer**: This project is inspired by real-world tasks. It uses dummy data and doesn't expose proprietary systems.

## Author
Bharathwaj Ganesan — [LinkedIn](https://linkedin.com/in/bharathwaj-ganesan-b22b91116/)
=======
#  Retail Sales ETL Pipeline

This project demonstrates an end-to-end ETL pipeline to ingest, clean, and load retail sales data into Snowflake using Apache Airflow and Python.

## Tools Used
- Apache Airflow
- Snowflake
- Python (Pandas, os, logging)
- SQL

## Pipeline Steps
1. Extract CSV sales data from `data/raw/`
2. Transform using `scripts/transform_sales.py`
3. Load cleaned data into Snowflake table: `RETAIL_SALES`
4. Scheduled via Airflow DAG: `retail_sales_dag.py`

## How to Run
- Add your Snowflake creds to `.env`
- Start Airflow with `astro dev start` or Docker
- Trigger `retail_sales_dag`

## Validation
- Row counts pre/post
- NULL checks
- Column type enforcement

## 📈 Author
[Bharathwaj Ganesan](https://www.linkedin.com/in/bharathwaj-ganesan-b22b91116/)
>>>>>>> 7d7fb0e83c5934d980a8f8fac14eab0d1cf2bdbe
