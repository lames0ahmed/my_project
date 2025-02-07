import pickle as pk
import numpy as np
import streamlit as st
from results import get_results 

with open("model.pkl", "rb") as file:
    model= pk.load(file)  

st.title('Model For Predict Tips 💡')


total_bill = st.number_input("💰 (Total_bill) ",min_value=0.0, step=0.1)
sex = st.selectbox("🚹 (Male) / 🚺 (Female)", ["Male", "Female"])
smoker = st.selectbox("🚬 (Smoking) or ❌🚬 (No Smoking)", ["Yes", "No"])
day = st.selectbox("📅 (Day)", ["Thur", "Fri", "Sat", "Sun"])
time = st.selectbox("🍽️ (Meal Time)", ["Lunch", "Dinner"])
size = st.number_input("👥 (Group Size) ",min_value=0, step=1 )


show = st.button('Click')

if show:

     total_bill = float(total_bill)  
     size = int(size)  
     result = get_results(model, total_bill, sex, smoker, day, time, size)

       
     if isinstance(result, np.ndarray):
            st.title(f'💰Your predicted tip is: ${result[0]:.2f}') 
   



