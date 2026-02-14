import pandas as pd

df=pd.read_csv("sales_data_cleaned.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

print("===== BASIC BUSINESS METRICS =====")

print("total revenue:",df["revenue"].sum())
print("Total Orders:", df["order_id"].nunique())
print("Total Customers:", df["customer_id"].nunique())

print("\n===== MONTHLY SALES TREND =====")
monthly_sales = df.groupby("month")["revenue"].sum()
print(monthly_sales)

print("\n===== TOP 10 PRODUCTS BY REVENUE =====")
top_products = (
    df.groupby("product_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(top_products)

print("\n===== BEST PERFORMING CATEGORIES =====")
category_sales = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(category_sales)

print("\n===== SALES BY REGION =====")
region_sales = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(region_sales)

print("\n===== TOP 5 CUSTOMERS BY REVENUE =====")
top_customers = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print("\n===== SALES BY REGION =====")
region_sales = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)
print(region_sales)

print("\n===== TOP 5 CUSTOMERS BY REVENUE =====")
top_customers = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
print(top_customers)