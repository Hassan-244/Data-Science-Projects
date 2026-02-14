import pandas as pd
import sqlite3

df = pd.read_csv("healthcare_cleaned_data.csv")

conn = sqlite3.connect("healthcare_database.db")
cursor = conn.cursor()

df.to_sql("patients", conn, if_exists="replace", index=False)

print("✅ Data successfully inserted into database!")

query1 = """
SELECT disease, COUNT(*) as total_cases
FROM patients
GROUP BY disease
ORDER BY total_cases DESC;
"""
print("\n📌 Most Common Diseases:")
print(pd.read_sql_query(query1, conn))

query2 = """
SELECT department, AVG(treatment_cost) as avg_cost
FROM patients
GROUP BY department
ORDER BY avg_cost DESC;
"""
print("\n📌 Average Treatment Cost per Department:")
print(pd.read_sql_query(query2, conn))

query3 = """
SELECT patient_id, hospital_stay_days
FROM patients
ORDER BY hospital_stay_days DESC
LIMIT 5;
"""
print("\n📌 Top 5 Longest Hospital Stays:")
print(pd.read_sql_query(query3, conn))

query4 = """
SELECT outcome, COUNT(*) as total
FROM patients
GROUP BY outcome;
"""
print("\n📌 Outcome Distribution:")
print(pd.read_sql_query(query4, conn))

conn.close()
