import sqlite3
import pandas as pd

conn = sqlite3.connect("publications.db")

query = """
SELECT Book_Name, Publishing_Year
FROM books
WHERE Publishing_Year > 2010
ORDER BY Publishing_Year ASC;
"""

result = pd.read_sql_query(query, conn)
print(result.head())

conn.close()
