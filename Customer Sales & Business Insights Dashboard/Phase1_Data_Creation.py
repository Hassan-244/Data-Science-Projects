import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

num_orders=200

order_id=np.arange(1,num_orders+1)
customer_id=np.random.randint(1,76,size=num_orders)

order_dates=pd.date_range(start='2026-05-28', end='2026-12-08').tolist()
order_dates=np.random.choice(order_dates,num_orders)

product_categories=['Electronics', 'Clothing', 'Books', 'Home', 'Toys']
product_names={
    'Electronics': ['Phone', 'Laptop', 'Headphones', 'Smartwatch'],
    'Clothing': ['Shirt', 'Jeans', 'Jacket', 'Dress'],
    'Books': ['Novel', 'Comics', 'Notebook', 'Magazine'],
    'Home': ['Chair', 'Lamp', 'Table', 'Cushion'],
    'Toys': ['Puzzle', 'Doll', 'Action Figure', 'Board Game']
}

regions=['North', 'South', 'East', 'West']
payment_methods=['Cash', 'Card', 'UPI']

categories=np.random.choice(product_categories,num_orders)
products=[np.random.choice(product_names[cat])for cat in categories]
quantities=np.random.randint(1,6,size=num_orders)
prices= np.random.randint(100,2000,size=num_orders)
revenues=prices * quantities
region=np.random.choice(regions,num_orders)
payment_method=np.random.choice(payment_methods,num_orders)

df=pd.DataFrame({
    'order_id':order_id,
    'customer_id':customer_id,
    'order_date':order_dates,
    'product_category':categories,
    'product_name':products,
    'quantity':quantities,
    'price':prices,
    'revenue':revenues,
    'region':region,
    'payment_method':payment_method
})


df.to_csv("sales_data.csv",index=False)
print("Sample dataset created: sales_data.csv")


print("\nFirst 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nNumeric summary:")
print(df.describe())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

categorical_cols = df.select_dtypes(include="object").columns
print("\nCategorical Columns Unique Values:")
for col in categorical_cols:
    print(f"{col}: {df[col].nunique()} unique values")

numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include='object').columns

print("\nNumeric columns:", numeric_cols)
print("Categorical columns:", categorical_cols)

df['order_date'] = pd.to_datetime(df['order_date'])
print("\nEarliest order:", df['order_date'].min())
print("Latest order:", df['order_date'].max())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nNumber of duplicate rows:", df.duplicated().sum())

