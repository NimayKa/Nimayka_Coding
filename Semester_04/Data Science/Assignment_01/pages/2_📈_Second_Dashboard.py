import pandas as pd
import numpy
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk 
import plotly.express as px
import extra_streamlit_components as stx

df = pd.read_csv('netflix.csv')
st.set_page_config(page_title="Second Dashboard",layout="wide", page_icon="📈")


unique_type = df['type'].unique()
unique_country = df['country'].unique()
unique_year = df['release_year'].unique()
unique_rating = df['rating'].unique()
genre_df = df[['country', 'release_year', 'genre_1', 'genre_2', 'genre_3']].melt(id_vars=['country', 'release_year'], value_vars=['genre_1', 'genre_2', 'genre_3'], value_name='genre').drop(columns=['variable']).dropna()
unique_genre = genre_df['genre'].unique()
st.write(df)
st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)
    
with st.sidebar:
    
    st.write("<h1 style='text-align: center; font-size: 34px;'>Visualization Filter</h1>", unsafe_allow_html=True)
    
    #First
    with st.form('First Filter',border=False): 
        with st.expander('First Filter'): 
            st.write()
                
    #Second 
    with st.form('Second Filter',border=False):
        with st.expander('Second Filter'):
            st.write()
                
    #Third         
    with st.form('Third Filter',border=False):
        with st.expander('Third Filter'):
            st.write()

    #Forth
    with st.form('Forth Filter', border=False):
        with st.expander('Forth Filter'):
            st.write()
            
    with st.form('Fifth Filter', border= False):
        with st.expander('Fifth Filter'):
            st.write()
    #Sixth
    with st.form('Sixth Filter',border=False):
        with st.expander('Sixth Filter'):
            st.write()
                
with st.container():
    st.write()
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write()

        
    with col2:
        st.write()
        
with st.container():
    st.write()