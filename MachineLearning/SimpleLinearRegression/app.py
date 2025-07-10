import streamlit as st
import pickle 
import numpy as np

# Load the model
model = pickle.load(open(r'C:\Users\hp\OneDrive\Desktop\ML\linear_regression_model.pkl', 'rb'))

# Streamlit UI
st.title("Salary Prediction App")
st.write("this app predicts salary based on the experience they have")
#input
year_experience=st.number_input("Enter Year Of Experience:",label_visibility="visible",min_value=0,max_value=50,step=1)
# prediction
if st.button("Predict Salary"):
    experience_input=np.array([[year_experience]])
    prediction=model.predict(experience_input)
    st.success(f" The Predicted Salary for{year_experience} year of experience is ${prediction[0]:,.2f}")
