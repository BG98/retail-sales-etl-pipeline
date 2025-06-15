import pandas as pd
import snowflake.connector

def load_to_snowflake():
    df = pd.read_csv('data/processed/cleaned_sales.csv')    
    conn = snowflake.connector.connect(
        user='BHARATH982',
        password='DataEngineerJob@2025',
        account='ds28415.central-india.azure',  
        warehouse='SNOWFLAKE_LEARNING_WH',
        database='snowflake_learning_db',
        schema='PUBLIC'
    )
    cursor = conn.cursor()
    
    cursor.execute("TRUNCATE TABLE RETAIL_SALES")    
    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO RETAIL_SALES (product_id, quantity, price_per_unit, total, order_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                int(row['product_id']),
                int(row['quantity']),
                float(row['price_per_unit']),
                float(row['total']),
                row['order_date']
            )
        )
    conn.commit()
    cursor.close()
    conn.close()

    print(" Data successfully loaded to Snowflake.")

load_to_snowflake()