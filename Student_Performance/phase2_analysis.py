import pandas as pd

df = pd.read_csv("students_data.csv")

print("=== First 5 rows of the dataset ===")
print(df.head(), "\n")

print("=== Missing values per column ===")
print(df.isnull().sum(), "\n")

df.fillna(0, inplace=True)

df["Total"] = df["Math"] + df["Physics"] + df["Chemistry"] + df["English"]
df["Percentage"] = df["Total"] / 4
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")

def grade(p):
    if p >= 85:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 55:
        return "C"
    elif p >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(grade)

print("=== Dataset after recalculation ===")
print(df.head(), "\n")

top_10 = df.sort_values("Percentage", ascending=False).head(10)
print("=== Top 10 Students ===")
print(top_10[["Name", "Percentage", "Grade"]], "\n")

failed_students = df[df["Result"] == "Fail"]
print("=== Failed Students ===")
print(failed_students[["Name", "Percentage", "Grade"]], "\n")

subject_avg = df[["Math","Physics","Chemistry","English"]].mean()
print("=== Average Marks per Subject ===")
print(subject_avg, "\n")

grade_dist = df["Grade"].value_counts()
print("=== Grade Distribution ===")
print(grade_dist, "\n")

df.to_csv("students_data_cleaned.csv", index=False)
print("Cleaned dataset saved as 'students_data_cleaned.csv'")
