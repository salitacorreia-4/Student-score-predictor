import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Student Exam Score Predictor")
st.write("Enter your details to predict your expected total exam score")

# Correct 3 input features matching train_model.py
hours = st.slider("Weekly self-study hours", 0.0, 40.0, 15.0)
attendance = st.slider("Attendance percentage (%)", 0.0, 100.0, 75.0)
participation = st.slider("Class participation score", 0.0, 100.0, 50.0)

if st.button("Predict my score"):
    input_data = np.array([[hours, attendance, participation]])
    prediction = model.predict(input_data)
    predicted_score = np.clip(prediction[0], 0, 100)
    st.success(f"Predicted Total Score: {predicted_score:.2f}")
