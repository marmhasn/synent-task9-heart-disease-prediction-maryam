# ❤️ Heart Disease Prediction System

## 📌 Project Overview

The Heart Disease Prediction System is an end-to-end Machine Learning project developed to predict the likelihood of heart disease based on patient medical information.

This project covers the complete Data Science workflow, including data preprocessing, exploratory data analysis (EDA), model training, model evaluation, and deployment using Streamlit.

Users can enter medical parameters through an interactive web interface and instantly receive a heart disease prediction along with the model's confidence score.

---

## 🚀 Live Demo

**Streamlit Application:**

https://synent-task9-heart-disease-prediction-maryam-xrcskr7jsukds854c.streamlit.app/

---

## 🎯 Objective

To develop a machine learning model capable of predicting heart disease risk using patient health data and deploy it through a user-friendly web application.

---

## 📊 Dataset

The dataset contains patient medical records and health-related attributes commonly used for heart disease prediction.

### Features Used

* Age
* Sex
* Chest Pain Type (cp)
* Resting Blood Pressure (trestbps)
* Cholesterol (chol)
* Fasting Blood Sugar (fbs)
* Resting ECG Results (restecg)
* Maximum Heart Rate Achieved (thalach)
* Exercise-Induced Angina (exang)
* ST Depression (oldpeak)
* Slope
* Number of Major Vessels (ca)
* Thalassemia (thal)

### Target Variable

* **0** → No Heart Disease
* **1** → Heart Disease Present

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

## 🔍 Data Preprocessing

The following preprocessing steps were performed:

* Dataset inspection
* Missing value analysis
* Duplicate value detection
* Removal of duplicate records
* Feature selection
* Data preparation for model training

---

## 📈 Exploratory Data Analysis (EDA)

Several visualizations were created to better understand the dataset, including:

* Target variable distribution
* Age distribution analysis
* Gender-wise heart disease analysis
* Correlation heatmap
* Feature importance visualization

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

| Model                    | Accuracy |
| ------------------------ | -------- |
| Logistic Regression      | 80.33%   |
| Random Forest Classifier | 83.61%   |
| Decision Tree Classifier | 73.77%   |

### Best Performing Model

**Random Forest Classifier**

Accuracy Achieved: **83.61%**

The Random Forest model was selected as the final model and saved using Joblib for deployment.

---

## 🌐 Streamlit Web Application

The deployed Streamlit application allows users to:

* Enter patient health information
* Generate real-time heart disease predictions
* View prediction confidence scores
* Interact with a simple and user-friendly interface

---

## 📂 Project Structure

```text
synent-task9-heart-disease-prediction-maryam

├── heart_disease_project.ipynb
├── heart.csv
├── heart_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ▶️ Running the Project Locally

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📷 Project Outputs

* Data Cleaning and Preprocessing
* Exploratory Data Analysis
* Model Comparison and Evaluation
* Feature Importance Analysis
* Streamlit Web Application Deployment

---

## 👩‍💻 Author

**Maryam**
