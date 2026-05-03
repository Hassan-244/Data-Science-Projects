import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

data=pd.read_csv("Mall_Customers.csv")

print("shape of data:",data.shape)

print("\nFirst 5 Rows:")
print(data.head())

print("\nColumns:")
print(data.columns)

print("\nMissing Values:")
print(data.isnull().sum)

print(data.describe())

plt.figure(figsize=(6,4))
sns.histplot(data['Annual Income (k$)'],bins=20,kde=True)
plt.title("Annual Income Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.histplot(data['Spending Score (1-100)'], bins=20, kde=True)
plt.title("Spending Score Distribution")
plt.show()

plt.figure(figsize=(7,5))
sns.scatterplot(x='Annual Income (k$)',y='Spending Score (1-100)',data=data)
plt.title("Income vs Spending Score")
plt.show()

X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
kmeans=KMeans(n_clusters=5 , random_state=42)
data['Cluster']=kmeans.fit_predict(X)
print(data.head())

wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(7,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

plt.figure(figsize=(8,6))

sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    palette='Set1',
    data=data,
    s=80
)

plt.scatter(
    kmeans.cluster_centers_[:,0],
    kmeans.cluster_centers_[:,1],
    s=250,
    c='black',
    marker='X',
    label='Centroids'
)

plt.title("Customer Segments")
plt.legend()
plt.show()

pca = PCA(n_components=2)
pca_data = pca.fit_transform(X)

plt.figure(figsize=(8,6))

sns.scatterplot(
    x=pca_data[:,0],
    y=pca_data[:,1],
    hue=data['Cluster'],
    palette='Set2',
    s=80
)

plt.title("PCA Visualization of Customer Segments")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.show()