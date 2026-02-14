import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students_data_cleaned.csv")

subject_avg = df[["Math", "Physics", "Chemistry", "English"]].mean()

plt.figure()
subject_avg.plot(kind="bar")
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show(block=True)

plt.figure()
df.sort_values("Student_ID")["Percentage"].plot()
plt.title("Student Performance Trend")
plt.xlabel("Student ID")
plt.ylabel("Percentage")
plt.show(block=True)

grade_dist = df["Grade"].value_counts()

plt.figure()
grade_dist.plot(kind="pie", autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.ylabel("")
plt.show(block=True)

plt.figure()
sns.heatmap(
    df[["Math", "Physics", "Chemistry", "English"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Subject Correlation Heatmap")
plt.show(block=True)


plt.figure()
df[["Math", "Physics", "Chemistry", "English"]].boxplot()
plt.title("Marks Distribution per Subject")
plt.ylabel("Marks")
plt.show(block=True)