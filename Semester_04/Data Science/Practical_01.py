import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd

today = datetime.date.today()

year = today.year

st.title("Indivual Practical")
st.subheader("Made by Bapakjoki")


with st.form('first form'):
    Student_name = st.text_input(label='Enter Your Name')
    Student_bod = st.number_input(label='Input Your Birth Year',min_value=1900,max_value=2024)
    submit = st.form_submit_button('Submit')

age = year - Student_bod

if submit:
    st.write('Name:',Student_name)
    st.write('Umur Bapaknya:',age)

