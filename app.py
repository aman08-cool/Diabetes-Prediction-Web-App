#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:43:53 2023

@author: amankumardwivedi
"""

import numpy as np
import random
import pickle 
import streamlit as st



# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for prediction

def diabetes_prediction(input_data):
    

    # Changing the input data to a NumPy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "non-diabetic"
    else:
        return "diabetic"
    
    
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

# Function to display a random quote
def display_random_quote():
    quote = random.choice(quotes)
    st.markdown(
        f"<p style='display: flex; align-items: center; justify-content: center; height: 200px; font-style: italic; font-weight: bold; font-size: 24px;'>\"{quote}\"</p>",
        unsafe_allow_html=True
    )


# Footer Function
def display_footer():
        st.markdown("<h5 style='position: fixed; bottom : 0; width: 94%; text-align: right; font-style: italic;'>@Made by Aman kr. Dwivedi</h5>", unsafe_allow_html=True)

# User name Function
def get_user_name():
        user_name = st.text_input("Enter your name:")
        return user_name

    
def main():
    
    st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="wide",
    )
    
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: url("https://images.unsplash.com/photo-1686942300971-c8f5d0a3b692");
        background-size: 100%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }
    .stButton button {
        background-color: #d9fdd2;
        color: #419CF0;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }
    
    /* Customize the button style */
    .custom-button {
    	--offset: 10px;
    	--border-size: 2px;
    
    	display: block;
    	position: relative;
    	padding: 1.5em 3em;
    	appearance: none;
    	border: 0;
    	background: transparent;
    	color: #008DC9;
    	text-transform: uppercase;
    	letter-spacing: 0.25em;
    	outline: none;
    	cursor: pointer;
    	font-weight: bold;
    	border-radius: 10px;
    	box-shadow: inset 0 0 0 var(--border-size) currentcolor;
    	transition: background 0.8s ease;
    
    	&:hover {
    		background: rgba(217, 253, 210, 1);
    	}
    }
    
    </style>
    """
    
    button_html = """
    <button class="custom-button" >
        <a href="https://www.who.int/health-topics/diabetes#tab=tab_1">
             What is Diabetes ?
        </a>
    </button>
    """

    st.write(button_html, unsafe_allow_html=True)


    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    # title for webpage
    st.write("<h1><span style='color:#052e7e;'>⚕️ Diabetes Prediction Web App ⚕️</span></h1>", unsafe_allow_html=True)
    #st.title('Diabetes Prediction System Web App')
    st.markdown("---")
    
    # User Name
    user_name = get_user_name()
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
        glucose = st.number_input('Glucose Level', min_value=0, max_value=500, value=100)
        blood_pressure = st.number_input('Blood Pressure Value', min_value=0, max_value=300, value=60)
        skin_thickness = st.number_input('Skin Thickness Value', min_value=0, max_value=100, value=20)
    with col2:
        insulin = st.number_input('Insuline Level', min_value=0, max_value=1000, value=0)
        bmi = st.number_input('BMI Value', min_value=0.0, max_value=100.0, value=25.0)
        diabetes_pedigree_function = st.text_input('Diabetes Pedigree Function Value')
        age = st.number_input('Age of the Person', min_value=0, max_value=150, value=30)
    
    st.markdown("---")
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])
    
    
    st.markdown("---")
    if diagnosis:
        st.subheader('Diagnosis:')
        if diagnosis == 'non-diabetic':
            st.success(f"Dear {user_name}, you don't have diabetes.")
            st.write("Stay healthy and take care!")
        else:
            st.error(f"Dear {user_name}, you have diabetes.")
            st.write("Take necessary steps to manage your diabetes and consult a healthcare professional.")
    

    # Calling Quote Function
    st.write(f"<p style='display: flex; align-items: center; justify-content: center; height: 50px; font-weight: bold; font-size: 34px; color: Red;'>Remember this Warrior 👇</p>",
                unsafe_allow_html=True)
    display_random_quote()
    

    # Footer of the Page
    display_footer()
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
