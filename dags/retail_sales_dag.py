from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scripts.transform_sales import transform_sales_data
from scripts.load_to_snowflake import load_to_snowflake

default_args = {
    'owner': 'bharath',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='retail_sales_etl',
    default_args=default_args,
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['retail', 'etl']
) as dag:

    task_transform = PythonOperator(
        task_id='transform_sales_data',
        python_callable=transform_sales_data
    )

    task_load = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=load_to_snowflake
    )

    task_transform >> task_load
