# How to Read SQL into a DataFrame in Python — Tutorial

> The single most common analyst pipeline in Python starts with a SQL query and ends with a DataFrame.


📺 **Watch:** https://www.youtube.com/watch?v=L2F-tfApIkU  
📖 **Article:** https://www.codegiz.com/blog/read-sql-dataframe/  
🎓 **Tutorial + quiz:** https://www.codegiz.com/watch/read-sql-dataframe/

Part of the **Common Questions in Python** series — short, search-targeted answers to the questions Python data folks actually type into YouTube.

---

## What you'll learn

- pd.read_sql query connection is the canonical SQL-to-DataFrame in Python.
- Polars offers two flavors.
- Always use parameterized queries.
- Filter at the SQL layer, not in Python.
- Use chunksize for tables too big to fit in memory.

---

## Setup

This demo runs on Python 3.10+ and pandas 2.0+. The other dependencies are installed via the included `requirements.txt`.

```bash
# 1. Clone
git clone https://github.com/GoCelesteAI/read-sql-dataframe.git
cd read-sql-dataframe

# 2. Virtual environment
python3 -m venv .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\activate          # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Run it

```bash
python read_sql.py
```

---

## The code

Here's `read_sql.py` in full — it's deliberately short. The video walks through what each block does.

```python
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
```

---

## Why this exists

Most pandas tutorials are written for the curriculum reader who starts at chapter 1. Real working analysts find pandas through search — `"how do I X in pandas"` typed into Google or YouTube. This series answers each of those questions as a self-contained 4–6 minute single, with a runnable demo you can copy, paste, and adapt to your own data.

---

🤖 *Channel run by Claude AI. Tutorials AI-produced; reviewed and published by Codegiz.* More: [codegiz.com](https://codegiz.com) · [@GoCelesteAI on YouTube](https://www.youtube.com/@GoCelesteAI)
