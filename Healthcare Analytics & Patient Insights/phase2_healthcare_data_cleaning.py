import pandas as pd

df=pd.read_csv("healthcare_data.csv")

print("📌 First 5 rows:")
print(df.head())

print("\n📌 Dataset Info:")
print(df.info())

print("\n📌 Missing Values:")
print(df.isnull().sum())

df["admission_date"]=pd.to_datetime(df["admission_date"])
df["discharge_date"]=pd.to_datetime(df["discharge_date"])

df["age"].fillna(df["age"].mean(),inplace=True)
df["treatment_cost"].fillna(df["treatment_cost"].mean(),inplace=True)

df["gender"].fillna(df["gender"].mode()[0],inplace=True)
df["disease"].fillna(df["disease"].mode()[0],inplace=True)
df["department"].fillna(df["department"].mode()[0],inplace=True)
df["outcome"].fillna(df["outcome"].mode()[0],inplace=True)

df["hospital_stay_days"] = ( df["discharge_date"] - df["admission_date"]).dt.days
df["cost_per_day"] = df["treatment_cost"] / df["hospital_stay_days"]

df.drop_duplicates(inplace=True)

df.to_csv("healthcare_cleaned_data.csv", index=False)

print("\n Phase 2 completed successfully!")
print("Cleaned file saved as healthcare_cleaned_data.csv")