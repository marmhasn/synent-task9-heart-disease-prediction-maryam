import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("heart_model.pkl")

st.set_page_config(
    page_title="Heart Disease Prediction System",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ Heart Disease Prediction System")
st.write("Enter patient details below to predict heart disease risk.")

# User Inputs

age = st.number_input("Age", min_value=1, max_value=120, value=50)

sex = st.selectbox(
    "Sex",
    [0, 1],
    format_func=lambda x: "Female" if x == 0 else "Male"
)

cp = st.selectbox(
    "Chest Pain Type (cp)",
    [0, 1, 2, 3]
)

trestbps = st.number_input(
    "Resting Blood Pressure",
    min_value=50,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Cholesterol",
    min_value=100,
    max_value=700,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    [0, 1]
)

restecg = st.selectbox(
    "Resting ECG Results",
    [0, 1, 2]
)

thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=50,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [0, 1]
)

oldpeak = st.number_input(
    "ST Depression (oldpeak)",
    min_value=0.0,
    max_value=10.0,
    value=1.0
)

slope = st.selectbox(
    "Slope",
    [0, 1, 2]
)

ca = st.selectbox(
    "Number of Major Vessels (ca)",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thal",
    [0, 1, 2, 3]
)

# Prediction Button

if st.button("Predict"):

    features = np.array([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    if prediction == 1:
        st.error("⚠️ Heart Disease Risk Detected")
        st.write(f"Confidence: {max(probability)*100:.2f}%")
    else:
        st.success("✅ No Heart Disease Risk Detected")
        st.write(f"Confidence: {max(probability)*100:.2f}%")