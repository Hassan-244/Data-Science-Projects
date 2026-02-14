import numpy as np
import pandas as pd

np.random.seed(42)

num_patients=100

patient_id=np.arange(1,num_patients+1)

age = np.random.randint(1,99,size=num_patients)

gender=np.random.choice(["Male","female"],size=num_patients)

disease=np.random.choice(["Diabetes", "Heart Disease", "Flu", "Cancer", "Asthma"],size=num_patients)

department=np.random.choice(["Cardiology", "General", "Oncology", "Pulmonology"],size=num_patients)

outcome=np.random.choice(["Recovered","Not Recovered"],size=num_patients,p=[0.8, 0.2])

treatment_cost = np.random.randint(5000, 200000, size=num_patients)

admission_date=pd.to_datetime("2024-01-01")+pd.to_timedelta(np.random.randint(1,15,size=num_patients),unit="D")

discharge_date=admission_date+pd.to_timedelta(np.random.randint(1,15,size=num_patients),unit="D")

df = pd.DataFrame({
    "patient_id": patient_id,
    "age": age,
    "gender": gender,
    "disease": disease,
    "admission_date": admission_date,
    "discharge_date": discharge_date,
    "treatment_cost": treatment_cost,
    "department": department,
    "outcome": outcome
})

df.to_csv("healthcare_data.csv", index=False)

print("✅ Healthcare dataset created successfully!")
print(df.head())