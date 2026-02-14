import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("healthcare_cleaned_data.csv")

plt.figure()
df["disease"].value_counts().plot(kind="bar")
plt.title("Disease Frequency")
plt.xlabel("Disease")
plt.ylabel("Number of Patients")
plt.show()

avg_cost_dept = df.groupby("department")["treatment_cost"].mean()

plt.figure()
avg_cost_dept.plot(kind="bar")
plt.title("Average Treatment Cost by Department")
plt.xlabel("Department")
plt.ylabel("Average Cost")
plt.show()

plt.figure()
sns.boxplot(x=df["hospital_stay_days"])
plt.title("Distribution of Hospital Stay (Days)")
plt.xlabel("Days Stayed")
plt.show()

plt.figure()
df["outcome"].value_counts().plot(kind="pie",autopct="%1.1f%%",startangle=90)
plt.title("Patient Outcome Distribution")
plt.ylabel("")  
plt.show()

plt.figure()
sns.heatmap(df[["age", "hospital_stay_days", "treatment_cost"]].corr(),annot=True,cmap="coolwarm")
plt.title("Correlation Between Age, Stay Days & Treatment Cost")
plt.show()