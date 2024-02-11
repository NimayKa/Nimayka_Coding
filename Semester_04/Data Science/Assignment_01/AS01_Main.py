import pandas as pd
import numpy
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk 
import plotly.express as px

df = pd.read_csv('netflix.csv')
st.set_page_config(layout="wide")

with st.sidebar:
    st.header('Visualization Filter') 
    
      
    st.header('Map Filter') 
    type_data = df['type'].unique()
    type_default_option = df[df['type'].isin(type_data)]
    type_option = st.multiselect('Select Your Type',df['type'].unique(),(type_data))
    if not type_option:
        filtered_type_df = type_default_option
    else:
        filtered_type_df = df[df['type'].isin(type_option)]
    
    
    st.subheader('Release Date Filter')
    year_option = st.slider('Select a range of years',df['release_year'].min(), df['release_year'].max(),(df['release_year'].min(),df['release_year'].max()))

    
    st.subheader('Most Rating Filter')
    unique_ratings = df['rating'].unique()
    rating_default_option = df[df['rating'].isin(unique_ratings)]
    rating_option = st.multiselect('Select Your Rating',df['rating'].unique(),(unique_ratings))
    if not rating_option:
        filtered_rating_df = rating_default_option
    else:
        filtered_rating_df = df[df['rating'].isin(rating_option)]
    

    
    with st.form ('Forth',border=False):
        st.subheader('Forth Visualization')
        forth_submit= st.form_submit_button('Submit')
        if forth_submit:
            st.write('')
    
    with st.form ('Fifth',border=False):
        st.subheader('Fifth Visualization') 
        fifth_submit= st.form_submit_button('Submit')
        if fifth_submit:
            st.write('')
    
    with st.form ('Sixth',border=False):
        st.subheader('Sixth Visualization') 
        sixth_submit= st.form_submit_button('Submit')
        if sixth_submit:
            st.write('')
            

st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)

with st.container():
    st.write("<h3 style='text-align: center;'>Scatter Plot Map</h3>", unsafe_allow_html=True)
    test = filtered_type_df[['country','type','latitude','longitude']].value_counts().reset_index()   
    
    fig = px.scatter_mapbox(test, 
                            lat="latitude", lon="longitude", 
                            color="type", 
                            size="count",
                            hover_name= "country",  
                            zoom=1,
                            center= None,
                            mapbox_style="carto-darkmatter",
                            )
    st.plotly_chart(fig,use_container_width=True,use_container_height= True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("<h3 style='text-align: center;'>Line Graph</h3>", unsafe_allow_html=True)
        
        filtered_year_df = df[(df['release_year']>=year_option[0])&(df['release_year']<=year_option[1])]
        st.write()
        filtered_release_year_df=filtered_year_df[['release_year','type']].value_counts().reset_index()
        fig = px.area(data_frame= filtered_release_year_df,
                      x='release_year',
                      y= 'count',
                      color='type',
                      color_discrete_sequence=["#a8f53d","#03AFAE"],
                      template='plotly_dark',
                      title = 'Release Year')
        st.plotly_chart(fig)
        

        st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        fig = px.bar(data_frame= filtered_rating_df['rating'].value_counts(),
             template='plotly_dark',
             x= filtered_rating_df['rating'].value_counts(),
             y= filtered_rating_df['rating'].value_counts().index,
             orientation='h',
             title = 'Most ratings',
             labels = {"x":"frequency" , "y":"Rating"
                       }
            )
        st.plotly_chart(fig)
        #title, director, country, date_added, release_year, rating, duration, listed_in, latitude, longitude 
        #Map - Type, Country, Lat & Long
        #Line - Release Year + Type
        #Vertizontal Bar - Type Count()
        #Horizantal bar - Rating Count()
        #Pie Chart - Top Director
        
    with col2:
        st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        
        types_of_shows = df['type'].value_counts()
        fig = px.bar(types_of_shows,color = types_of_shows.index,color_discrete_sequence=["#8a12f9", "#FFFFFF"],text_auto= True , template='plotly_dark',title = 'Netflix Data Type')
        st.plotly_chart(fig)
    
        #types_of_shows = df['type'].value_counts()
        #fig, ax = plt.subplots()
        #ax.bar(types_of_shows.index, types_of_shows.values, color=["#8a12f9", "#000000"])
        #ax.set_xlabel('Types of Shows')
        #ax.set_ylabel('Count')
        #ax.set_title('Count of Different Types of Shows')
        #st.pyplot(fig)
        #st.write(types_of_shows)
        
        st.write("<h3 style='text-align: center;'>Pie Graph</h3>", unsafe_allow_html=True)
        filtered_df = df[df['director']!= 'Not Given']
        fig = px.pie(
            data_frame=filtered_df['director'].value_counts()[0:5],
            names=filtered_df['director'].value_counts()[0:5].index,
            values=filtered_df['director'].value_counts()[0:5],
            labels={'names': 'Director'},  # Include director names in hover data
            title='Top Directors',
            template='plotly_dark'
        )
        st.plotly_chart(fig)

# 1Distribution of Netflix Content Type (Pie Chart),2Release Year , 3Most Rating ,4Top 5 directors (Bar Graph) , 
#


