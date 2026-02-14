import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data_cleaned.csv")

df["order_date"] = pd.to_datetime(df["order_date"])

df["month"] = df["order_date"].dt.to_period("M")

monthly_sales = df.groupby("month")["revenue"].sum()
plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.show(block=True)

top_products = (
    df.groupby("product_name")["revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show(block=True)

category_sales = df.groupby("product_category")["revenue"].sum()

plt.figure()
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%")
plt.title("Revenue Share by Product Category")
plt.show(block=True)

plt.figure()
sns.heatmap(
    df[["quantity", "price", "revenue"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Between Quantity, Price & Revenue")
plt.show(block=True)