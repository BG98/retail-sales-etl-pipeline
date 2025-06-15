import pandas as pd
import os

def transform_sales_data():
    raw_path = 'data/raw/sales.csv'
    processed_path = 'data/processed/cleaned_sales.csv'

    df = pd.read_csv(raw_path)    
    df.dropna(subset=['product_id', 'quantity'], inplace=True)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total'] = df['quantity'] * df['price_per_unit']    
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv(processed_path, index=False)
    print(f" Transformed data saved to {processed_path}")

transform_sales_data()
