import numpy as np
import random
import pickle
import streamlit as st
from datetime import datetime

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide",
)

# ------------------ Load Model ------------------
loaded_model = pickle.load(open("trained_model.sav", "rb"))

# ------------------ Quotes ------------------
quotes = [
    "I may have diabetes, but I am not limited by it. – Ally Brooks",
    "Diabetes does not define me, but it helps shape who I am. – Amanda Quinne",
    "Life is not over because you have diabetes. – Dale Evans",
    "Diabetes may slow me down, but it will never stop me. – Brittany Steen",
    "Diabetes is not a choice, but how I live with it is. – Brett Andreas",
]

# ------------------ Global CSS ------------------
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 26px;
    border-radius: 16px;
    box-shadow: 0 10px 24px rgba(0,0,0,0.15);
    margin-bottom: 28px;
    color: #1a1a1a;
}
.card-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 16px;
}
.stButton > button {
    width: 100%;
    height: 52px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 14px;
    background-color: #4CAF50;
    color: white;
}
.stButton > button:hover {
    background-color: #43a047;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Helpers ------------------
def display_random_quote():
    quote = random.choice(quotes)
    st.markdown(
        f"""
        <div class="card" style="text-align:center; font-style:italic;">
            “{quote}”
        </div>
        """,
        unsafe_allow_html=True
    )

def diabetes_prediction(input_data):
    arr = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(arr)
    return "non-diabetic" if prediction[0] == 0 else "diabetic"

def display_diabetic_animation():
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.08); }
        100% { transform: scale(1); }
    }
    .pulse {
        animation: pulse 1.8s infinite;
    }
    </style>
    <div style="text-align:center;">
        <h2 class="pulse" style="color:#ff4b4b;">⚠️ Diabetes Detected ⚠️</h2>
    </div>
    """, unsafe_allow_html=True)

# ------------------ Hero Section ------------------
st.markdown("""
<div style="text-align:center; padding:40px 20px;">
    <h1>🩺 Diabetes Prediction System</h1>
    <p style="font-size:18px; color:#b0b0b0;">
        Simple • Fast • Awareness-focused
    </p>
</div>
""", unsafe_allow_html=True)

# ------------------ Form ------------------
with st.form("prediction_form"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">👤 Patient Information</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Patient Name")
        gender = st.selectbox("Gender", ["Male", "Female"])
        pregnancies = st.number_input(
            "Number of Pregnancies", 0, 20, 0
        ) if gender == "Female" else 0
        glucose = st.number_input("Glucose Level (mg/dL)", 0, 500, 100)
        blood_pressure = st.number_input("Blood Pressure (mm Hg)", 0, 300, 60)

    with col2:
        skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)
        insulin = st.number_input("Insulin Level (μU/ml)", 0, 1000, 0)
        bmi = st.number_input("BMI", 0.0, 100.0, 25.0, format="%.1f")
        pedigree = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5, format="%.3f")
        age = st.number_input("Age", 0, 120, 30)

    submitted = st.form_submit_button("Get Diabetes Test Result")
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Prediction Result ------------------
if submitted:
    with st.spinner("Analyzing health data..."):
        result = diabetes_prediction([
            pregnancies, glucose, blood_pressure,
            skin_thickness, insulin, bmi, pedigree, age
        ])

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📊 Diagnosis</div>', unsafe_allow_html=True)

    if result == "non-diabetic":
        st.success(f"Dear {name or 'Patient'}, no signs of diabetes detected.")
        st.balloons()
    else:
        st.error(f"Dear {name or 'Patient'}, diabetes detected.")
        display_diabetic_animation()
        st.warning("Please consult a healthcare professional.")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">💡 Health Tips</div>', unsafe_allow_html=True)
    tips = [
        "Maintain a balanced diet",
        "Exercise at least 30 minutes daily",
        "Monitor blood sugar regularly",
        "Stay hydrated",
        "Manage stress and sleep well",
    ]
    for tip in tips:
        st.write("•", tip)
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Quote Section ------------------
st.markdown('<div class="card-title" style="text-align:center;">✨ Thought for Today</div>', unsafe_allow_html=True)
display_random_quote()

# ------------------ Footer ------------------
current_time = datetime.now().strftime("%B %d, %Y")
st.caption(f"Created by Aman Dwivedi · Last updated {current_time}")
