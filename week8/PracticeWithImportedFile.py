import pandas as pd
import sqlite3
# Read CSV into DataFrame
df = pd.read_csv("/Users/stepanpelc/Library/CloudStorage/OneDrive-MiddlesexUniversity/Lessons/1 Year/Programming for Data Communications and Networks/Week7-12_Labs/week8/cyber incidents.csv")

# View first 5 rows
print(df.head())
# Check data types and missing values
print(df.info())
# # Check for missing data
print(df.isnull().sum())

# Connect to database
conn = sqlite3.connect('intelligence_platform.db')
# Bulk insert all rows
df.to_sql('cyber_incidents', conn, if_exists='append', index=False)
print("✓ Data loaded successfully")

# Count rows in database
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM cyber_incidents")
count = cursor.fetchone()[0]
print(f"Loaded {count} incidents")  # View sample data
cursor.execute("SELECT * FROM cyber_incidents LIMIT 3")
for row in cursor.fetchall():
    print(row)
