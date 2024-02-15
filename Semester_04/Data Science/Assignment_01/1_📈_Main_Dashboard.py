import pandas as pd
import numpy
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk 
import plotly.express as px
import extra_streamlit_components as stx

df = pd.read_csv('netflix.csv')
st.set_page_config(page_title="Main Dashboard",layout="wide", page_icon="📈")

st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)
    
with st.sidebar:
    st.write("<h1 style='text-align: center; font-size: 34px;'>Visualization Filter</h1>", unsafe_allow_html=True)
    st.subheader('Map Filter') 
    type_data = df['type'].unique()
    type_default_option = df[df['type'].isin(type_data)]
    type_option = st.multiselect('Select Your Type',df['type'].unique(),(type_data))
    if not type_option:
        filtered_type_df = type_default_option
    else:
        filtered_type_df = df[df['type'].isin(type_option)]
        
    st.subheader('Line Filter') 
    year_option = st.slider('Select a range of years',df['release_year'].min(), df['release_year'].max(),(df['release_year'].min(),df['release_year'].max()))

    st.subheader('Bar Filter')     
    type_option_bar = st.multiselect('Select Your Type to Filter',df['type'].unique(),(type_data))
    if not type_option_bar:
        filtered_type_bar_df = type_default_option
    else:
        filtered_type_bar_df = df[df['type'].isin(type_option_bar)]
        
    st.subheader('Map Filter') 
    rating_data = df['rating'].unique()
    
    rating_default_option = df[df['rating'].isin(rating_data)]
    
    rating_option = st.multiselect('Select Your Type',df['rating'].unique(),(rating_data))
    if not type_option:
        filtered_rating_df = rating_default_option
    else:
        filtered_rating_df = df[df['rating'].isin(rating_option)]
        
    # st.subheader('Most Rating Filter')
    # unique_ratings = df['rating'].unique()
    # rating_default_option = df[df['rating'].isin(unique_ratings)]
    # rating_option = st.multiselect('Select Your Rating',df['rating'].unique(),(unique_ratings))
    # if not rating_option:
    #     filtered_rating_df = rating_default_option
    # else:
    #     filtered_rating_df = df[df['rating'].isin(rating_option)]

    
    with st.form ('Forth',border=False):
        st.subheader('Forth Visualization')
        forth_submit= st.form_submit_button('Submit')
        if forth_submit:
            st.write('')
                
with st.container():
    
    st.write(df)
    #4 Column
    genre = df[['country','genre_1','genre_2','genre_3']]
    stacked_df = genre.set_index('country').stack().reset_index()
    stacked_df.columns = ['country', 'genre_level', 'genre']
    stacked_df.drop(columns=['genre_level'], inplace=True)
    st.write(stacked_df.value_counts())
    
    
    #Line Graph
    yg_option = df['release_year'].unique()
    yg_option = sorted(yg_option,reverse=True)
   
    
    yg_selectbox1 = st.selectbox(label='Select First Year',options=yg_option,index=None,placeholder='Select Year')
    yg_option1 = [year for year in yg_option if year != yg_selectbox1]
    yg_selectbox2 = st.selectbox(label='Select Second Year',options=yg_option1,index=None,placeholder='Select Year')
    
    if yg_selectbox1 is None:
        yg_selectbox1 = yg_option[0]
    else:
        yg_selectbox1 = yg_selectbox1
        
    if yg_selectbox2 is None:
        yg_selectbox2 = yg_option[1]
    else:
        yg_selectbox2 = yg_selectbox2
    
    st.write('Select first year',yg_selectbox1)
    st.write('Select second year',yg_selectbox2)
    
    
    year = df[['release_year','genre_1','genre_2','genre_3']]
    stacked_year = year.set_index('release_year').stack().reset_index()
    stacked_year.columns = ['release_year', 'genre_level', 'genre']
    stacked_year.drop(columns=['genre_level'], inplace=True)
    stacked_year = stacked_year.value_counts().reset_index(name='count')
    yg = stacked_year.sort_values(ascending=False,by='release_year')
    
    #yr = year and genre
    yg_df = yg[(yg['release_year']>=year_option[0])&(yg['release_year']<=year_option[1])]
    st.write()
    filtered_release_year_df=yg_df[['release_year','type']].value_counts().reset_index()
    year_fig = px.area(data_frame= filtered_release_year_df,
            x='release_year',
            y= 'count',
            color='type',
            color_discrete_sequence=["#a8f53d","#03AFAE"],
            template='plotly_dark',
            title = 'Release Year')
    st.plotly_chart(year_fig)
    
    st.write(stacked_year)
    # 4 Column
    st.write("<h3 style='text-align: center;'>Scatter Plot Map</h3>", unsafe_allow_html=True)
    map_filtered = filtered_type_df[['country','type','latitude','longitude']].value_counts().reset_index()   
    
    fig = px.scatter_mapbox(map_filtered, 
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
        
        # 2 Column Filter
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
        
        
                
        

        
        # 1 Column Filter
        # st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        # fig = px.bar(data_frame= filtered_rating_df['rating'].value_counts(),
        #     template='plotly_dark',
        #     x= filtered_rating_df['rating'].value_counts(),
        #     y= filtered_rating_df['rating'].value_counts().index,
        #     orientation='h',
        #     title = 'Most ratings',
        #     labels = {"x":"frequency" , "y":"Rating"
        #             }
        #     )
        # st.plotly_chart(fig)
        
        
        #title, director, country, date_added, release_year, rating, duration, listed_in, latitude, longitude 
        #Map - Type, Country, Lat & Long
        #Line - Release Year + Type
        #Vertizontal Bar - Type Count()
        #Horizantal bar - Rating Count()
        #Pie Chart - Top Director
        
        # 1Distribution of Netflix Content Type (Pie Chart),2Release Year , 3Most Rating ,4Top 5 directors (Bar Graph) , 
        
    with col2:
        st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        
        # 1 Column Filter
        
        types_of_shows = filtered_type_bar_df[['type','rating']].value_counts().reset_index()[0:5]
        
        fig = px.bar(data_frame=types_of_shows,
                     x = 'rating',
                     y = 'count',
                    color = 'rating',
                    text_auto= True ,
                    hover_data=types_of_shows,
                    template='plotly_dark',
                    title = 'Netflix Data Type')
        st.plotly_chart(fig)

        
        st.write("<h3 style='text-align: center;'>Pie Graph</h3>", unsafe_allow_html=True)
        # 2 Column Filter
        filtered_df = df[df['director']!= 'Not Given']
        fig = px.pie(
            data_frame=filtered_df['director'].value_counts()[0:5],
            names=filtered_df['director'].value_counts()[0:5].index,
            values=filtered_df['director'].value_counts()[0:5],
            labels={'names': 'Director'},
            title='Top Directors',
            template='plotly_dark'
        )
        st.plotly_chart(fig)
        
with st.container():
    # 4 Column Filter or 1 Column?
    st.write("<h3 style='text-align: center;'>Scatter Plot Map</h3>", unsafe_allow_html=True)
    rating_map_filtered = filtered_rating_df[['country','rating','latitude','longitude']].value_counts().reset_index()
    
    fig = px.scatter_mapbox(rating_map_filtered, 
                            lat="latitude", lon="longitude", 
                            color="rating", 
                            size="count",
                            hover_name= "country",  
                            zoom=1,
                            center= None,
                            mapbox_style="carto-darkmatter",
                            )
    st.plotly_chart(fig,use_container_width=True,use_container_height= True)
    
    

            

