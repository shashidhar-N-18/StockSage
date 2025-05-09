import sqlite3
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Load CSV Data
demand_df = pd.read_csv("backend\data\demand_forecasting.csv")
inventory_df = pd.read_csv("backend\data\inventory_monitoring.csv")
pricing_df = pd.read_csv("backend\data\pricing_optimization.csv")
def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("return_rate_%", "return_rate", regex=False)
    )
    return df

# Convert column names to lowercase and replace spaces with underscores
demand_df = clean_columns(demand_df)
inventory_df = clean_columns(inventory_df)
pricing_df = clean_columns(pricing_df)


# Connect to SQLite Database
conn = sqlite3.connect("retail_inventory.db")
cursor = conn.cursor()


# Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS demand (
    product_id INTEGER,
    date TEXT,
    store_id INTEGER,
    sales_quantity INTEGER,
    price REAL,
    promotions TEXT,
    seasonality_factors TEXT,
    external_factors TEXT,
    demand_trend TEXT,
    customer_segments TEXT,
    PRIMARY KEY (product_id, store_id, date)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER,
    store_id INTEGER,
    stock_levels INTEGER,
    supplier_lead_time_days INTEGER,
    stockout_frequency INTEGER,
    reorder_point INTEGER,
    expiry_date TEXT,
    warehouse_capacity INTEGER,
    order_fulfillment_time_days INTEGER,
    PRIMARY KEY (product_id, store_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pricing (
    product_id INTEGER,
    store_id INTEGER,
    price REAL,
    competitor_prices REAL,
    discounts REAL,
    sales_volume INTEGER,
    customer_reviews INTEGER,
    return_rate REAL,
    storage_cost REAL,
    elasticity_index REAL,
    PRIMARY KEY (product_id, store_id)
);
""")

# Insert Data
demand_df.to_sql("demand", conn, if_exists="replace", index=False)
inventory_df.to_sql("inventory", conn, if_exists="replace", index=False)
pricing_df.to_sql("pricing", conn, if_exists="replace", index=False)

print(demand_df)
print(inventory_df)
print(pricing_df)

# Commit and Close
conn.commit()
conn.close()

print("Database initialized successfully!")
