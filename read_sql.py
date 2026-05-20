"""read_sql.py — query a SQLite database two ways, with parameterized SQL.

Run:
  python read_sql.py
"""
import sqlite3
import pandas as pd
import polars as pl

SQL = "SELECT * FROM prices WHERE Ticker = ? AND Close > ?"
PARAMS = ("AAPL", 200)

# Method 1: pandas read_sql with sqlite3 connection
conn = sqlite3.connect("prices.db")
df_pd = pd.read_sql(SQL, conn, params=PARAMS)
print(f"pandas read_sql:      {df_pd.shape}")

# Method 2: polars read_database with the same connection
df_pl = pl.read_database(SQL, conn, execute_options={"parameters": PARAMS})
print(f"polars read_database: {df_pl.shape}")
conn.close()
