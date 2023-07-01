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


# creating a function for prediction

def diabetes_prediction(input_data):
    
    
    # input_data = (6,148,72,35,0,33.6,0.627,50) # the answer should be that this person is Diabetic
    # input_data = (4,110,92,0,0,37.6,0.191,30)  # the answer should be that this person is non-Diabetic

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



# User name Function
def get_user_name():
        user_name = st.text_input("Enter the Female Patient name")
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
        background-color: #56AFCC;
        
        background-size: 100%;
        background-position: top left;
        background-repeat: no-repeat;
        background-attachment: local;
    }
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    # giving a title
    #st.title('Diabetes Prediction Web App')
    st.write("<h1><span style='color:#052e7e;'>Let's Check Your Diabetes 💉</span></h1>", unsafe_allow_html=True)
    st.markdown('---')
    
    
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    with col1:
        user_name = get_user_name()
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=0)
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=500, value=100)
        BloodPressure = st.number_input('Blood Pressure Value', min_value=0, max_value=300, value=60)
        SkinThickness = st.number_input('Skin Thickness Value', min_value=0, max_value=100, value=20)
    with col2:
        Insulin = st.number_input('Insuline Level', min_value=0, max_value=1000, value=0)
        BMI = st.number_input('BMI Value', min_value=0.0, max_value=100.0, value=25.0)
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        Age = st.number_input('Age of the Person', min_value=0, max_value=150, value=30)
    
    
    
    
    #Pregnancies = st.text_input('Number of Pregnancies')
    #Glucose = st.text_input('Glucose Level')
    #BloodPressure = st.text_input('Blood Pressure value')
    #SkinThickness = st.text_input('Skin Thickness value')
    #Insulin = st.text_input('Insulin Level')
    #BMI = st.text_input('BMI value')
    #DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    #Age = st.text_input('Age of the Person')
    
    
    
    

    st.markdown("---")
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    

    if diagnosis:
        st.subheader('Diagnosis:')
        if diagnosis == 'non-diabetic':
            st.success(f"Dear {user_name}, you don't have diabetes.")
            st.write("<h5>Stay healthy and take care!💪🙂👌 </h5>",unsafe_allow_html=True)
        else:
            st.error(f"Dear {user_name}, you have diabetes.")
            st.write("<h5>Take necessary steps to manage your diabetes and consult a healthcare professional 🧑‍⚕️.</h5>")
            
            
    # Calling Quote Function
    display_random_quote()
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    