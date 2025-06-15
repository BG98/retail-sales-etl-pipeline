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
