import pandas as pd
import streamlit as st

data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                     'Age': [25, 30, 22, 35],
                     'Gender': ['Female', 'Male', 'Male', 'Male'],
                     'Score': [85, 92, 78, 88]})


highest_score = data[data['Score'] == data['Score'].max()]
st.write("Students with the highest score:")
st.write(highest_score['Name'])

older_than_27 = data[data['Age'] > 27]
st.write("Students older than 27:")
st.write(older_than_27[['Name','Age']])

average_score = data['Score'].mean()
st.write(f"Average score for the class: {average_score}")
