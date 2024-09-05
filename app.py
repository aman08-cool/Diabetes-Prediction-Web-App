import numpy as np
import random
import pickle 
import streamlit as st
from datetime import datetime

# Loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

quotes = [
    "I may have diabetes, but I am not limited by it. I can live a happy, healthy, and adventurous life. – Ally Brooks",
    "I was determined to share my positive approach and not let diabetes stand in the way of enjoying my life. – Paula Deen",
    "Diabetes does not define me, but it helps shape who I am. – Amanda Quinne",
    "Life is not over because you have diabetes. Make the most of what you have, be grateful. – Dale Evans",
    "Diabetes may have taken away the sugar in my blood, but it will never take away the sweetness in my life. – Olivia Christian",
    "I do not love to work out, but if I stick to exercising every day and put the right things in my mouth, then my diabetes just stays in check. – Halle Berry",
    "Diabetes is not a choice, but how I live with it is. – Brett Andreas",
    "Diabetes is a great example whereby, giving the patient the tools, you can manage yourself very well. – Clayton M. Christensen ",
    "Diabetes may slow me down at times, but it will never stop me. – Brittany Steen",
    "The way to deal with the devil of obesity and diabetes is literally one day at a time. – Stephen Furst"
]

def display_random_quote():
    quote = random.choice(quotes)
    st.markdown(
        f"<p style='padding: 20px; background-color: #f0f0f0; border-radius: 10px; font-style: italic; font-weight: bold; font-size: 18px;'>\"{quote}\"</p>",
        unsafe_allow_html=True
    )

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return "non-diabetic" if prediction[0] == 0 else "diabetic"

def get_user_name():
    return st.text_input("Enter the Patient name")

def display_diabetic_animation():
    st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .pulse {
        animation: pulse 2s infinite;
        display: inline-block;
    }
    </style>
    <div style='text-align: center;'>
        <h2 class='pulse' style='color: #FF5733;'>⚠️ Diabetes Detected ⚠️</h2>
    </div>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Diabetes Prediction App",
        page_icon="🩺",
        layout="wide",
    )
    current_time = datetime.now().strftime("%B %d, %Y")
    
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

    # App header
    st.title('Diabetes Prediction Web App')
    st.markdown('---')

    # User input section
    st.subheader("Patient Information")
    col1, col2 = st.columns(2)
    
    with col1:
        user_name = get_user_name()
        gender = st.selectbox('Gender', ['Male', 'Female'])
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0) if gender == 'Female' else 0
        glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=500, value=100)
        blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=300, value=60)
    
    with col2:
        skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=100, value=20)
        insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0, max_value=1000, value=0)
        bmi = st.number_input('BMI', min_value=0.0, max_value=100.0, value=25.0, format="%.1f")
        diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.5, format="%.3f")
        age = st.number_input('Age', min_value=0, max_value=150, value=30)

    st.markdown("---")

    # Prediction button
    if st.button('Get Diabetes Test Result'):
        diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age])
        
        st.subheader('Diagnosis:')
        if diagnosis == 'non-diabetic':
            st.success(f"Dear {user_name}, you don't have diabetes.")
            st.balloons()
            st.markdown("### Stay healthy and take care! 💪😊👌")
        else:
            st.error(f"Dear {user_name}, you have diabetes.")
            display_diabetic_animation()
            st.warning("### Please consult a healthcare professional for proper management. 🧑‍⚕️")
        
        # Display health tips
        st.subheader("Health Tips")
        tips = [
            "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
            "Exercise regularly, aiming for at least 30 minutes of moderate activity most days.",
            "Monitor your blood sugar levels as advised by your doctor.",
            "Stay hydrated by drinking plenty of water.",
            "Get enough sleep and manage stress through relaxation techniques."
        ]
        for tip in tips:
            st.markdown(f"- {tip}")

    # Display a random quote
    st.markdown("---")
    st.subheader("Inspirational Quote")
    display_random_quote()

    # Footer
    st.markdown("---")
    st.markdown(f"Created by Aman Dwivedi | Last updated: {current_time}")

if __name__ == '__main__':
    main()