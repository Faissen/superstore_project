#Import libraries
import pandas as pd
import psycopg2 # PostgreSQL adapter for Python
from dotenv import load_dotenv # To load environment variables from a .env file
import os # To access environment variables

# Load environment variables from .env file
load_dotenv()

# Load cleaned data
df = pd.read_csv('superstore_cleaned.csv')
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce") #Convert due to null values, prevent errors
df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce") #Convert due to null values, prevent errors
schema = "superstore"

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
    "fact_sales":["row_id", "order_id", "product_id","sales", "customer_id","region_id",
                  "date_id", "ship_mode_id"],
}

def insert_data(schema, table, columns):
    # Create the INSERT INTO SQL query
    cols = ",".join(columns).strip() # Column names for the query, remove any extra spaces
    placeholders = ", ".join(["%s"] * len(columns)) # Placeholder for parameterized query, %s for each column
    query = f"""
    INSERT INTO {schema}.{table} ({cols})
    VALUES ({placeholders})
    ON CONFLICT DO NOTHING;"""
    return query
    
# Insert each row into the table
for table, columns in tables.items(): # Iterate over each table and its columns
# FACT TABLE → insert all rows 
    if table == "fact_sales": 
        df_subset = df[columns] 
# DIMENSIONS → insert only unique rows 
    elif table == "dim_date":
        df_subset = df[columns].drop_duplicates()
        df_subset = df_subset[df_subset["date_id"].notna()] # Remove invalid rows 
    else:
        df_subset = df[columns].drop_duplicates()

    insert_query = insert_data(schema, table, columns) # Get the insert query for the table
    for _, row in df_subset.iterrows(): # Iterate over each row in the DataFrame
        values = [] # List to hold the values for the current row
        for col in columns:
            val = row[col] 
            # Convert NaN to None for PostgreSQL 
            if pd.isna(val):  # Check if the value is NaN
                val = None # Set to None for PostgreSQL
            values.append(val) # Append the value to the list
        cur.execute(insert_query, values)

# Commit changes and close the connection
conn.commit() # Commit the transaction
cur.close() # Close the cursor
conn.close() # Close the connection