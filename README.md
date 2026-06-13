❤️ Heart Disease Prediction System

📌 Project Overview

The Heart Disease Prediction System is a machine learning project designed to predict the likelihood of heart disease based on patient health information. The project includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment through an interactive Streamlit web application.

Users can enter medical information such as age, cholesterol level, blood pressure, and other health indicators to receive a prediction along with a confidence score.

🎯 Objective

To develop a reliable machine learning model that can assist in predicting heart disease risk and make it accessible through a simple and user-friendly web application.

📊 Dataset

The dataset contains patient medical records with various health-related features and a target variable indicating whether heart disease is present.

Features Used
Age
Sex
Chest Pain Type (cp)
Resting Blood Pressure (trestbps)
Cholesterol (chol)
Fasting Blood Sugar (fbs)
Resting ECG Results (restecg)
Maximum Heart Rate Achieved (thalach)
Exercise-Induced Angina (exang)
ST Depression (oldpeak)
Slope
Number of Major Vessels (ca)
Thalassemia (thal)
Target Variable
0 → No Heart Disease
1 → Heart Disease Present
🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Streamlit
🤖 Model Development

Several machine learning models were trained and evaluated to identify the best-performing approach for heart disease prediction.

Model	Accuracy
Logistic Regression	80.33%
Random Forest Classifier	83.61%
Decision Tree Classifier	73.77%
Best Model

Random Forest Classifier

Accuracy: 83.61%

The trained model was saved and integrated into the Streamlit application for real-time predictions.

🌐 Streamlit Application

The project was deployed as a Streamlit web application, allowing users to:

Enter patient health information
Generate heart disease predictions instantly
View prediction confidence levels
Interact with a simple and intuitive interface

The application loads the trained machine learning model and provides predictions based on user input in real time.

📂 Project Structure
synent-task9-heart-disease-prediction-system-maryam

├── heart_disease_project.ipynb
├── heart.csv
├── heart_model.pkl
├── app.py
├── requirements.txt
└── README.md
▶️ How to Run Locally
Clone the Repository
git clone <repository-link>
Install Dependencies
pip install -r requirements.txt
Run the Streamlit Application
streamlit run app.py
📷 Screenshots

Add screenshots of:

Data Analysis Visualizations
Model Evaluation Results
Streamlit Application Interface
👩‍💻 Author

Maryam
