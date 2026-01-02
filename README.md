Project Goal
The objective of this project is to analyze sales performance, customer behavior, and product trends using the Superstore dataset from Kaggle (www.kaggle.com/datasets/rohitsahoo/sales-forecasting).

The project follows a full data‑analytics workflow:
- Designing a relational database model from raw CSV files
- Loading and transforming data using Python (ETL)
- Running analytical SQL queries to uncover insights
- Building a final interactive dashboard in Tableau or Looker Studio

The analysis focuses on understanding:
- Sales performance across regions
- Customer purchasing patterns
- Product category profitability
- Shipping behavior and delivery timelines

This project demonstrates end‑to‑end data engineering and analytics skills using real‑world data.

Data Modeling Decisions
This project required designing a relational database schema from a raw CSV file. The goal was to create a clean, normalized structure that supports efficient querying, ensures data integrity, and reflects real‑world analytical workflows. Below is a summary of the key modeling decisions and the reasoning behind each one.

1. Use of Separate Dimension and Fact Tables
The dataset contains repeated information about customers, products, and geographic locations. To avoid redundancy and improve query performance, the data was normalized into:
- Dimension tables: customers, products, regions
- Fact table: order_items
- Context table: orders

This structure resembles a simplified star schema, commonly used in analytics and BI environments. It allows for fast aggregations and clear relationships between entities.

2. Keeping row_id as the Primary Key in order_items
Although order_id and product_id could form a composite key, the dataset includes a unique row_id for each line item. Keeping it as the primary key provides several advantages:
- Simplifies the ETL process
- Guarantees uniqueness without relying on composite keys
- Makes debugging and referencing individual rows easier
- Reflects the structure of the original dataset

This choice improves maintainability without compromising relational integrity.

3. Using SERIAL for region_id
The dataset does not include a natural unique identifier for geographic locations. To ensure each region entry is uniquely identifiable, an artificial key was created. Reasons for this choice:
- Avoids relying on combinations of city/state/region
- Simplifies foreign key relationships
- Ensures consistency even if location names change or contain duplicates

Artificial keys are a standard practice when natural keys are unavailable or unstable.

4. Choosing Between VARCHAR(n) and TEXT
The schema uses a mix of VARCHAR(n) and TEXT, depending on the nature of each field. 
Fields such as customer_id, product_id, category, and product_name have predictable maximum lengths. Setting a limit (VARCHAR(n)):
- Documents the expected size of the field
- Prevents accidental insertion of malformed or excessively long values
- Makes the schema more explicit and self‑describing

For example product_name VARCHAR(255):
The limit of 255 characters was chosen after inspecting the dataset and confirming that no product name exceeded this length. This is a common and safe convention in database design.

Although PostgreSQL treats VARCHAR(n) and TEXT similarly in performance, TEXT was avoided for descriptive fields because:
- It removes constraints on data quality
- It makes the schema less explicit
- It can lead to inconsistent data entry in real‑world scenarios


5. Use of Foreign Keys to Enforce Integrity, to ensure that:
- Every order references a valid customer
- Every order references a valid region
- Every order item references a valid order
- Every order item references a valid product

This prevents orphan records and maintains referential integrity across the database, even as data grows.

6. Date Fields Stored as DATE
order_date and ship_date were stored as DATE instead of TEXT to:
- Enable date arithmetic (delivery time, monthly trends, etc.)
- Improve query performance
- Ensure correct sorting and filtering

The ETL pipeline handles the conversion from string to date format.

7. Numeric Fields Stored as NUMERIC(10,2)
Sales values were stored using NUMERIC(10,2). This ensures:
- Accurate decimal representation
- No floating‑point rounding errors
- Compatibility with financial calculations

Results
The analysis uncovered several key insights:

* Regional Performance
Sales vary significantly across regions, with some states consistently outperforming others. Regional segmentation reveals clear opportunities for targeted marketing and logistics optimization.

* Customer Behavior
Customer segments (Consumer, Corporate, Home Office) show distinct purchasing patterns. Some segments contribute disproportionately to total revenue.

* Product Trends
Furniture and Technology categories generate the highest revenue, while Office Supplies show high volume but lower margins. Sub‑category analysis highlights which products drive profitability.

* Shipping & Delivery
Shipping mode influences delivery time and customer experience. Standard Class is the most used method, but Second Class and First Class show faster delivery with higher associated costs.

* Business Insights
- Marketing efforts should prioritize high‑performing regions and customer segments.
- Inventory planning should focus on top‑selling categories and sub‑categories.
- Shipping optimization could reduce delivery delays and improve customer satisfaction.

Tools Used
- PostgreSQL (database + SQL queries)
- pgAdmin (query execution & schema management)
- Python (Pandas, SQLAlchemy) for ETL
- Tableau / Looker Studio for dashboard visualization
- Jupyter Notebook for exploratory analysis

Skills & Competencies Developed

Throughout this project, I strengthened several key data‑analytics and data‑engineering skills:
- Designing a relational database schema from raw data
- Writing SQL queries for aggregation, joins, CTEs, and analytical insights
- Building ETL pipelines using Python (Pandas + SQLAlchemy)
- Cleaning, transforming, and loading structured datasets
- Creating interactive dashboards for business reporting
- Communicating insights clearly through visualizations and narrative explanations
- Structuring a complete analytical workflow from raw data to final dashboard

Areas for Improvement
- Adding statistical tests (e.g., ANOVA, correlation analysis)
- Incorporating forecasting models for sales prediction
- Automating the ETL pipeline with Airflow or Prefect
- Expanding the dashboard with drill‑down capabilities
- Adding customer lifetime value (CLV) or cohort analysis
- Deploying the dashboard online for public access

Dataset Includes
* Order ID
* Order Date & Ship Date
* Customer ID, Name, and Segment
* Product ID, Category, Sub‑Category, Product Name
* Sales values
* Geographic information (City, State, Region, Postal Code)
* Shipping mode

Methodology
1. Data Loading & Inspection
- Import CSV files
- Inspect structure, data types, and missing values
- Identify duplicated rows

2. Data Cleaning
- Remove duplicates
- Convert date fields to datetime
- Standardize categorical fields
- Normalize tables into a relational model

3. ETL (Extract, Transform, Load)
- Build dimension tables (customers, products, regions)
- Build fact tables (orders, order_items)
- Load cleaned data into PostgreSQL

4. SQL Analysis
- Sales by region, category, and customer segment
- Monthly and yearly sales trends
- Product profitability
- Shipping performance metrics

5. Visualization
- Interactive dashboard in Tableau / Looker Studio
- Charts for sales trends, product performance, and regional insights

6. Insights & Conclusions
- Summarize findings
- Provide business recommendations

How to Run the Project
1. Clone the repository (git clone https://github.com/your-username/superstore-sales-sql-etl)
2. Navigate into the project folder (cd superstore-sales-sql-etl)
3. Install required libraries (pip install -r requirements.txt)
4. Set up the PostgreSQL database
- Run the SQL schema file to create tables
- Execute the ETL script to load data
5. Open the Jupyter Notebook
- Run the notebook cells to reproduce the analysis.

Visual Summary
- Sales by Region  (link-to-plot-1)
- Category Performance  (link-to-plot-2)
- Customer Segment Analysis  (link-to-plot-3)
- Tableau Dashboard  (link-to-dashboard-image)
