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
# Tables
tables = {
    "":[],
    
}


# Commit changes and close the connection
conn.commit() # Commit the transaction
cur.close() # Close the cursor
conn.close() # Close the connection