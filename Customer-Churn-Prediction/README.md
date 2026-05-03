# 📊 Customer Churn Prediction (Machine Learning Project)

## 📌 Project Overview
This project predicts whether a customer will leave (churn) or stay using machine learning models. It helps businesses identify at-risk customers and take preventive actions.

---

## 🎯 Objective
- Predict customer churn (Yes/No)
- Identify important factors affecting churn
- Compare multiple ML models for best performance

---

## 📂 Dataset
- Telco Customer Churn Dataset
- Features include:
  - Gender
  - SeniorCitizen
  - Tenure
  - Monthly Charges
  - Total Charges
  - Contract Type
  - Internet Services
  - Payment Method

---

## ⚙️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## 🤖 Machine Learning Models Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

---

## 📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 📈 Results
- Logistic Regression performed best with highest accuracy
- Model helps identify customers likely to churn

---

## 🚀 Key Insights
- Customers with month-to-month contracts are more likely to churn
- Higher monthly charges increase churn probability
- Long-term contracts reduce churn risk

---

## 📌 How to Run
```bash
pip install -r requirements.txt
python churn.py