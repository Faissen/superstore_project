#Import libraries
import pandas as pd
import psycopg2 # PostgreSQL adapter for Python
from dotenv import load_dotenv # To load environment variables from a .env file
import os # To access environment variables

# Load environment variables from .env file
load_dotenv()

# Read cleaned data
df = pd.read_csv('cleaned_superstore_data.csv')

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)
cur = conn.cursor() # Create a cursor object

# Insert data into PostgreSQL
# Dictionary mapping table names to their respective columns
tables = {
    "dim_customer":["customer_id", "customer_name", "segment"],
    "dim_product":["product_id", "product_name", "category", "sub_category"],
    "dim_region":["region_id", "country", "state", "city", "postal_code", "region"],
    "dim_ship_mode":["ship_mode_id", "ship_mode"],
    "dim_date":["date_id", "year", "quarter", "month", "day", "weekday", "order_date", "ship_date"],
    "fact_sales":["row_id", "order_id", "product_id","sales", "region_id", "customer_id","region_id",
                  "date_id", "ship_mode_id"],
}

def insert_data(table, columns, df):
    # Create the INSERT INTO SQL query
    cols = ",".join(columns).strip() # Column names for the query, remove any extra spaces
    placeholders = ", ".join(["%s"] * len(columns)) # Placeholder for parameterized query
    return (f"INSERT INTO {table} ({cols}) 
                    VALUES ({placeholders})
                    ON CONFLICT DO NOTHING;") # Handle conflicts by doing nothing
    
# Insert each row into the table
for _, row in df.iterrows():
        values = [row[col] for col in columns]
        cur.execute(insert_query, values)
# Commit changes and close the connection
conn.commit() # Commit the transaction
cur.close() # Close the cursor
conn.close() # Close the connection