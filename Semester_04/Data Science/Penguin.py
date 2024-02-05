import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title('Penguin')
st.markdown('Make Scatterplot')



penguin_file = st.file_uploader('Upload Your Files')

if penguin_file is not None:
    penguin_df = pd.read_csv(penguin_file)
    with st.form('titan'):
        selected_x_var = st.selectbox('x Variable',penguin_df.columns)
        selected_y_var = st.selectbox('y Variable',penguin_df.columns)
        selected_hue_var = st.selectbox('Hue Variable',penguin_df.columns)
        selected_filter_var = st.selectbox('Filter Variable',penguin_df.columns)
        st.form_submit_button('Submit')
        filtered = penguin_df[selected_filter_var].unique()
        gender_series = pd.series(['All'].append(pd.series(filtered),ignore_index=True))
        filter_var = st.radio('Gender',filtered)
    st.write(penguin_df)
else:
    st.stop()

sns.set_style('darkgrid')

fig,ax = plt.subplots()
ax = sns.scatterplot(data = penguin_df, x=selected_x_var, y=selected_y_var,hue=selected_hue_var)

plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('test')
st.pyplot(fig)

