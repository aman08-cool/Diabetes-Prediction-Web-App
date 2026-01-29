import numpy as np
import random
import pickle
import streamlit as st
from datetime import datetime

# ------------------ Load Model ------------------
loaded_model = pickle.load(open("trained_model.sav", "rb"))

# ------------------ Quotes ------------------
quotes = [
    "I may have diabetes, but I am not limited by it. I can live a happy, healthy, and adventurous life. – Ally Brooks",
    "I was determined to share my positive approach and not let diabetes stand in the way of enjoying my life. – Paula Deen",
    "Diabetes does not define me, but it helps shape who I am. – Amanda Quinne",
    "Life is not over because you have diabetes. Make the most of what you have, be grateful. – Dale Evans",
    "Diabetes may have taken away the sugar in my blood, but it will never take away the sweetness in my life. – Olivia Christian",
    "I do not love to work out, but if I stick to exercising every day and eat right, my diabetes stays in check. – Halle Berry",
    "Diabetes is not a choice, but how I live with it is. – Brett Andreas",
    "Diabetes may slow me down at times, but it will never stop me. – Brittany Steen",
]

# ------------------ Helpers ------------------
def display_random_quote():
    quote = random.choice(quotes)
    st.markdown(
        f"""
        <div style="
            background-color: #ffffff;
            padding: 22px;
            border-radius: 12px;
            color: #1a1a1a;
            font-size: 18px;
            font-style: italic;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        ">
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
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

# ------------------ Main App ------------------
def main():
    st.set_page_config(
        page_title="Diabetes Prediction App",
        page_icon="🩺",
        layout="wide",
    )

    current_time = datetime.now().strftime("%B %d, %Y")

    # App Header
    st.title("Diabetes Prediction Web App")
    st.caption("Early awareness leads to better health decisions.")
    st.markdown("---")

    # User Input
    st.subheader("Patient Information")
    col1, col2 = st.columns(2)

    with col1:
        user_name = st.text_input("Patient Name")
        gender = st.selectbox("Gender", ["Male", "Female"])
        pregnancies = (
            st.number_input("Number of Pregnancies", 0, 20, 0)
            if gender == "Female"
            else 0
        )
        glucose = st.number_input("Glucose Level (mg/dL)", 0, 500, 100)
        blood_pressure = st.number_input("Blood Pressure (mm Hg)", 0, 300, 60)

    with col2:
        skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)
        insulin = st.number_input("Insulin Level (μU/ml)", 0, 1000, 0)
        bmi = st.number_input("BMI", 0.0, 100.0, 25.0, format="%.1f")
        pedigree = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5, format="%.3f")
        age = st.number_input("Age", 0, 120, 30)

    st.markdown("---")

    # Prediction
    if st.button("Get Diabetes Test Result"):
        result = diabetes_prediction(
            [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, pedigree, age]
        )

        st.subheader("Diagnosis")
        if result == "non-diabetic":
            st.success(f"Dear {user_name or 'Patient'}, no signs of diabetes detected.")
            st.balloons()
        else:
            st.error(f"Dear {user_name or 'Patient'}, diabetes detected.")
            display_diabetic_animation()
            st.warning("Please consult a healthcare professional.")

        st.subheader("Health Tips")
        tips = [
            "Maintain a balanced diet.",
            "Exercise at least 30 minutes daily.",
            "Monitor blood sugar regularly.",
            "Stay hydrated.",
            "Get adequate sleep and manage stress.",
        ]
        for tip in tips:
            st.write("•", tip)

    # Quote Section
    st.markdown("---")
    st.subheader("Inspirational Quote")
    display_random_quote()

    # Footer
    st.markdown("---")
    st.caption(f"Created by Aman Dwivedi · Last updated {current_time}")

if __name__ == "__main__":
    main()
