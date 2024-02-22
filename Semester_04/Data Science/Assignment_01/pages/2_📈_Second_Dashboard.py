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
unique_country = sorted(df['country'].unique())
unique_year = sorted(df['release_year'].unique(),reverse=True)
unique_rating = df['rating'].unique()
genre_df = df[['country', 'release_year', 'genre_1', 'genre_2', 'genre_3']].melt(id_vars=['country', 'release_year'], value_vars=['genre_1', 'genre_2', 'genre_3'], value_name='genre').drop(columns=['variable']).dropna().sort_values(by='genre')
unique_genre = genre_df['genre'].unique()
st.write(df)
st.write(genre_df)
st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)
    
with st.sidebar:
    
    st.write("<h1 style='text-align: center; font-size: 34px;'>Visualization Filter</h1>", unsafe_allow_html=True)
    
    #First
    # with st.form('First Filter',border=False): 
    #     with st.expander('First Filter'): 
    #         option1_bar = st.selectbox(label='Select First Year For 1st Bar', options=unique_year)
    #         option2_options = [year for year in unique_year if year != option1_bar]
    #         option2_bar = st.selectbox(label='Select First Year For 2nd Bar', options=option2_options)
    #         option3_bar = st.multiselect(label='Select Multi Genre',options=unique_genre,default=(unique_genre))
    #         bar = genre_df[['genre','release_year']].value_counts().reset_index().sort_values(by='genre')
    #         button1 = st.form_submit_button('Submit')
    #         if button1 is True:
    #             bar1 = bar[(bar['release_year']==option1_bar)]
    #             bar2 = bar[(bar['release_year']==option2_bar)]
    #         else:
    #             bar1 = bar[(bar['release_year']==option1_bar)]
    #             bar2 = bar[(bar['release_year']==option2_bar)]
                
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
    col1, col2 = st.columns(2)
    
    with col1:
        st.write()
        # fig = px.bar(data_frame=bar1,
        #     x = 'genre',
        #     y = 'count',
        #     color = 'genre',
        #     text_auto= True ,
        #     hover_data=bar1,
        #     template='plotly_dark',
        #     title = 'Netflix Data Type')
        # st.plotly_chart(fig)
        
    with col2:
        st.write()
        # fig = px.bar(data_frame=bar2,
        #     x = 'genre',
        #     y = 'count',
        #     color = 'genre',
        #     text_auto= True ,
        #     hover_data=bar2,
        #     template='plotly_dark',
        #     title = 'Netflix Data Type')
        # st.plotly_chart(fig)
        