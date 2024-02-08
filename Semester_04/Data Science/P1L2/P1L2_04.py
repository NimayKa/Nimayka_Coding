import pandas as pd
import streamlit as st

titanic = pd.read_csv ('Titanic.csv')

with st.form('Titanic Sidebar'):
    with st.sidebar:
        st.header('Filter Option')
        selected_class = st.selectbox('Select Class',titanic['class'].unique())
        selected_sex = st.selectbox('Select Gender',titanic['sex'].unique())
        button = st.form_submit_button('Enter')
        
        
st.header('Practical 1 Lecture 02')

if button == True:
    st.write('Filter by',selected_class,' And ', selected_sex)
    filtered_df = titanic[(titanic['class']== selected_class)&(titanic['sex']== selected_sex)]
    filtered_df = filtered_df[['class','sex','survived']].value_counts().reset_index()
    st.write(filtered_df)
    st.bar_chart(filtered_df, x = 'survived' , y = 'count')
else:
    st.subheader('Enter Filter on Sidebar')
    st.write(titanic)