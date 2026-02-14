import pandas as pd

df = pd.read_csv("healthcare_cleaned_data.csv")

print("📌 First 5 rows:")
print(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Basic statistics for numeric columns:")
print(df.describe())

print("\n📌 Unique diseases:", df["disease"].nunique())
print(df["disease"].value_counts())

print("\n📌 Departments count:",df["department"].nunique())
print(df["department"].value_counts())

print("\n📌 Average age by outcome:")
print(df.groupby("outcome")["age"].mean())

print("\n📌 Average treatment cost by department:")
print(df.groupby("department")["treatment_cost"].mean())

print("\n📌 Average hospital stay days per disease:")
print(df.groupby("disease")["hospital_stay_days"].mean())

