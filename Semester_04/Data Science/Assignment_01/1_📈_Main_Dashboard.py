import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('netflix.csv')
st.set_page_config(page_title="Main Dashboard",layout="wide", page_icon="📈")

unique_type = df['type'].unique()
unique_country = df['country'].unique()
unique_year = sorted(df['release_year'].unique(),reverse=True)
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
            st.subheader('Map Filter') 
            type_default_option = df[df['type'].isin(unique_type)]
            type_option = st.multiselect('Select Your Type',unique_type,(unique_type))
            
            submit1 = st.form_submit_button('Submit')
            if submit1 == True:
                if not type_option:
                    filtered_type_df = type_default_option
                else:
                    filtered_type_df = df[df['type'].isin(type_option)]    
            else:
                filtered_type_df = type_default_option
                
    #Second 
    with st.form('Second Filter',border=False):
        with st.expander('Second Filter'):
            st.subheader('Line Filter') 
            year_option = st.slider('Select a range of years',df['release_year'].min(), df['release_year'].max(),(df['release_year'].min(),df['release_year'].max()))
            type_option1 = st.multiselect('Select Your Type',unique_type,(unique_type))
            submit2 = st.form_submit_button('Submit')
            if submit2 == True:
                filtered_year_df = df[(df['release_year']>=year_option[0])&(df['release_year']<=year_option[1])]
                filtered_year_df = filtered_year_df[(filtered_year_df['type'].isin(type_option1))]
            else:
                filtered_year_df = df[(df['release_year']>=year_option[0])&(df['release_year']<=year_option[1])]
                filtered_year_df = filtered_year_df[(filtered_year_df['type'].isin(type_option1))]
                
    #Third         
    with st.form('Third Filter',border=False):
        with st.expander('Third Filter'):
            st.subheader('Bar Filter')     
            type_option_bar = st.multiselect('Select Your Type to Filter',unique_type,(unique_type))
            submit3 = st.form_submit_button('Submit')
            if submit3 == True:
                if not type_option_bar:
                    filtered_type_bar_df = type_default_option
                else:
                    filtered_type_bar_df = df[df['type'].isin(type_option_bar)]
            else:
                filtered_type_bar_df = df[df['type'].isin(type_option_bar)]
            
        # st.subheader('Most Rating Filter')
        # rating_default_option = df[df['rating'].isin(unique_ratings)]
        # rating_option = st.multiselect('Select Your Rating',df['rating'].unique(),(unique_ratings))
        # if not rating_option:
        #     filtered_rating_df = rating_default_option
        # else:
        #     filtered_rating_df = df[df['rating'].isin(rating_option)]

    #Forth
    with st.form('Forth Filter', border=False):
        with st.expander('Forth Filter'):
            st.subheader('Forth Visualization')
            cyg_c1, cyg_c2, cyg_y = st.selectbox('Select a First Country', unique_country), st.selectbox('Select a Second Country', unique_country), st.selectbox('Select a Year', unique_year)
            cyg_r = st.multiselect('Select Your Type', unique_genre, unique_genre)
            
            forth_submit = st.form_submit_button('Submit')
            if forth_submit:
                cyg_bar1_df = genre_df[(genre_df['country'] == cyg_c1) & (genre_df['release_year'] == cyg_y) & (genre_df['genre'].isin(cyg_r))]
                cyg_bar2_df = genre_df[(genre_df['country'] == cyg_c2) & (genre_df['release_year'] == cyg_y) & (genre_df['genre'].isin(cyg_r))]
            else:
                cyg_bar1_df = genre_df[(genre_df['country'] == cyg_c1) & (genre_df['release_year'] == cyg_y) & (genre_df['genre'].isin(cyg_r))]
                cyg_bar2_df = genre_df[(genre_df['country'] == cyg_c2) & (genre_df['release_year'] == cyg_y) & (genre_df['genre'].isin(cyg_r))]
            
            cyg_bar1_df = cyg_bar1_df[['country','release_year','genre']].value_counts().reset_index().sort_values(by='genre')
            cyg_bar2_df = cyg_bar2_df[['country','release_year','genre']].value_counts().reset_index().sort_values(by='genre')

    with st.form('Fifth Filter', border= False):
        with st.expander('Fifth Filter'):
            filtered_df = df[df['director']!= 'Not Given']
            selected_year =  st.selectbox('Select a year', unique_year)
            filtered_df = filtered_df[(filtered_df['release_year']==selected_year)]
            fifth_button = st.form_submit_button('Submit')
            if fifth_button == True:
                st.write()
            else:
                st.write()
    #Sixth
    with st.form('Sixth Filter',border=False):
        with st.expander('Sixth Filter'):
            st.subheader('Map Filter') 
            rating_default_option = df[df['rating'].isin(unique_rating)]
            rating_option = st.multiselect('Select Your Type',unique_rating,(unique_rating))
            submit4 = st.form_submit_button('Submit')
            if not type_option:
                filtered_rating_df = rating_default_option
            else:
                filtered_rating_df = df[df['rating'].isin(rating_option)]
                
with st.container():

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
        
        filtered_release_year_df=filtered_year_df[['release_year','type']].value_counts().reset_index()
        fig = px.area(data_frame= filtered_release_year_df,
                      x='release_year',
                      y= 'count',
                      color='type',
                      color_discrete_sequence=["#a8f53d","#03AFAE"],
                      template='plotly_dark',
                      title = 'Release Year')
        st.plotly_chart(fig)
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=(f'{cyg_c1} in {cyg_y}', f'{cyg_c2} in {cyg_y}'))
        fig.add_trace(
            go.Bar(x=cyg_bar1_df['genre'], y=cyg_bar1_df['count'], marker=dict(color=cyg_bar1_df['count'])),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=cyg_bar2_df['genre'], y=cyg_bar2_df['count'], marker=dict(color=cyg_bar2_df['count'])),
            row=1, col=2
        )

        fig.update_layout(template='plotly_dark', title_text="Count of Genres by Coutnry & Release Year")

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
        fig = px.pie(
            data_frame=filtered_df['director'].value_counts()[0:5],
            names=filtered_df['director'].value_counts()[0:5].index,
            values=filtered_df['director'].value_counts()[0:5],
            labels={'names': 'Director'},
            title=f'Top Directors',
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