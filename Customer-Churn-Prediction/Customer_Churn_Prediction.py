import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

data= pd.read_csv("churn.csv")
data.columns = data.columns.str.strip()
print(data.columns)

print(data.shape)
print(data.head())

data.isnull().sum()

data=data.drop('customerID', axis=1)

data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

data = data.dropna()

data['Churn']=data['Churn'].map({'Yes':1,'No':0})

contract_churn = pd.crosstab(data['Contract'], data['Churn'])
print("\nContract vs Churn:")
print(contract_churn)

contract_churn.plot(kind='bar')
plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Count")
plt.show()

data=pd.get_dummies(data,drop_first=True)

X=data.drop('Churn',axis=1)
y=data['Churn']

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LogisticRegression(max_iter=2000)
model.fit(X_train,y_train)
pred=model.predict(X_test)

knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
knn_pred=knn.predict(X_test)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)
tree_pred = tree.predict(X_test)

print("Logistic Accuracy:", accuracy_score(y_test, pred))
print("KNN Accuracy:", accuracy_score(y_test, knn_pred))
print("Tree Accuracy:", accuracy_score(y_test, tree_pred))

print(confusion_matrix(y_test, pred))

print(classification_report(y_test, pred))


importance=pd.DataFrame({
    'Feature': X.columns,
    'Weight': model.coef_[0]
})

importance = importance.sort_values('Weight',ascending=False)
print("\nFeature Importance (Logistic Regression):")
print(importance)

data['Churn'].value_counts().plot(kind='bar')
plt.title("Churn Distribution")
plt.xlabel("Churn (0 = No, 1 = Yes)")
plt.ylabel("Count")
plt.show()


plt.figure(figsize=(6,4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=data)
plt.title("Monthly Charges vs Churn")
plt.show()