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
