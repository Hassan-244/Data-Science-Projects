import pandas as pd 

df= pd.read_csv("sales_data.csv")

print("📌 Dataset Loaded Successfully")
print(df.head())

print("\n📌 Dataset Info")
print(df.info())

print("\n📌 Missing Values")
print(df.isnull().sum())

df["quantity"].fillna(df["quantity"].mean,inplace=True)
df["price"].fillna(df["price"].mean,inplace=True)

df["region"].fillna(df["region"].mode()[0],inplace=True)
df["payment_method"].fillna(df["payment_method"].mode()[0],inplace=True)

df["order_date"]=pd.to_datetime(df["order_date"])

df["year"]=df["order_date"].dt.year
df["month"]=df["order_date"].dt.month

df.drop_duplicates(inplace=True)

df.to_csv("sales_data_cleaned.csv", index=False)

print("\n Phase 2 Completed Successfully")
print("Cleaned data saved as 'sales_data_cleaned.csv'")