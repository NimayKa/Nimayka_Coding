import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                     'Age': [25, 30, 22, 35],
                     'Gender': ['Female', 'Male', 'Male', 'Male'],
                     'Score': [85, 92, 78, 88]})


st.title("Indivual Practical")
st.subheader("Made by Bapakjoki")


with st.form('first form'):
    Student_name = st.text_input(label='Enter Your Name')
    Student_age = st.number_input(label='Input Your Age',min_value=0,max_value=50)
    Student_gender = st.radio('Gender',['Male','Female'])
    Student_score = st.number_input(label='Input Your Score',min_value=0,max_value=100)
    submit = st.form_submit_button('Submit')

if submit:
    st.write('Name:',Student_name)
    st.write('Umur Bapaknya:',Student_age)
    st.write('Gender:',Student_gender)
    st.write('Score',Student_score)
    
    new_student = pd.DataFrame( {'Name':[Student_name],'Age':[Student_age],'Gender':[Student_gender],'Score':[Student_score]})
    data = pd.concat([data,new_student],ignore_index=True)
    graph = data['Name','Score']
    
    

st.bar_chart(graph)
st.write(graph)
