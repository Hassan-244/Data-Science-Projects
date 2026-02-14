import numpy as np
import pandas as pd

np.random.seed(42)

num_students = 75

student_ids = np.arange(1, num_students + 1)
names = [f"Student_{i}" for i in student_ids]

math = np.random.randint(0, 101, num_students)
physics = np.random.randint(0, 101, num_students)
chemistry = np.random.randint(0, 101, num_students)
english = np.random.randint(0, 101, num_students)

attendance = np.random.randint(60, 101, num_students)

total_marks = math + physics + chemistry + english

percentage = total_marks / 4

pass_fail = np.where(percentage >= 40, "Pass", "Fail")

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

grades = np.array([grade(p) for p in percentage])

df = pd.DataFrame({
    "Student_ID": student_ids,
    "Name": names,
    "Math": math,
    "Physics": physics,
    "Chemistry": chemistry,
    "English": english,
    "Attendance": attendance,
    "Total": total_marks,
    "Percentage": percentage,
    "Result": pass_fail,
    "Grade": grades
})

df.to_csv("students_data.csv", index=False)

print("CSV file 'students_data.csv' created successfully with 75 students!\n")
print("Preview of first 10 students:\n")
print(df.head(10))
