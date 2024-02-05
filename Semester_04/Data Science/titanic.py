import pandas as pd
import streamlit as st

titanic = pd.read_csv ('Titanic.csv')

with st.form('Titanic'):
    selected_column = st.selectbox('Select 1 Column',titanic.columns)
    selected_groupby = st.selectbox('Group By',titanic.columns)
    st.form_submit_button('Submit')
    st.write('Before Filter')
    st.write (titanic)
    st.write('-----------------------')
    st.write('After Filter')
    filtered_titanic = pd.DataFrame(titanic.groupby([selected_groupby]).count()[selected_column])
    st.write (filtered_titanic)



st.line_chart(filtered_titanic)
st.bar_chart(filtered_titanic)
st.area_chart(filtered_titanic)