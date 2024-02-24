import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('netflix.csv')
st.set_page_config(page_title="Second Dashboard",layout="wide", page_icon="📈")


unique_type = df['type'].unique()
unique_country = sorted(df['country'].unique())
unique_year = sorted(df['release_year'].unique(),reverse=True)
unique_rating = df['rating'].unique()
genre_df = df[['country', 'release_year', 'genre_1', 'genre_2', 'genre_3']].melt(id_vars=['country', 'release_year'], value_vars=['genre_1', 'genre_2', 'genre_3'], value_name='genre').drop(columns=['variable']).dropna().sort_values(by='genre')
unique_genre = genre_df['genre'].unique()

st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)
    
with st.sidebar:
    
    st.write("<h1 style='text-align: center; font-size: 34px;'>Visualization Filter</h1>", unsafe_allow_html=True)
    
    #First
    with st.form('First Filter',border=False): 
        with st.expander('First Filter'): 
            country_map = st.multiselect(label='Select a country',options=unique_country,default=(unique_country))
            st.form_submit_button('Submit')
                
    #Second 
    with st.form('Second Filter',border=False):
        with st.expander('Second Filter'):
            option1_bar = st.selectbox(label='Select First Year For 1st Bar', options=unique_year)
            option2_options = [year for year in unique_year if year != option1_bar]
            option2_bar = st.selectbox(label='Select First Year For 2nd Bar', options=option2_options)
            option3_bar = st.multiselect(label='Select Multi Genre',options=unique_genre,default=(unique_genre))
            bar = genre_df[['genre','release_year']].value_counts().reset_index().sort_values(by='genre')
            button1 = st.form_submit_button('Submit')
            if button1 is True:
                bar1_df = bar[(bar['release_year']==option1_bar)]
                bar2_df = bar[(bar['release_year']==option2_bar)]
            else:
                bar1_df = bar[(bar['release_year']==option1_bar)]
                bar2_df = bar[(bar['release_year']==option2_bar)]
            
                
    #Third         
    with st.form('Third Filter',border=False):
        with st.expander('Third Filter'):
            line_df=df[['country','release_year']].value_counts().reset_index()
            country_line = st.multiselect(label='Select a country',options=unique_country,default=(unique_country))
            year_line = st.slider('Select a range of years',df['release_year'].min(), df['release_year'].max(),(df['release_year'].min(),df['release_year'].max()))
            st.form_submit_button('Submit')
            
    #Forth
    with st.form('Forth Filter', border=False):
        with st.expander('Forth Filter'):
            bar3_df = genre_df[['release_year','genre']].value_counts().reset_index()
            year_bar3_df = st.selectbox('Select a years',options=unique_year)
            genre_bar3_df = st.multiselect(label='Select a genre',options=unique_genre,default=(unique_genre))
            st.form_submit_button('Submit')
            
    with st.form('Fifth Filter', border= False):
        with st.expander('Fifth Filter'):
            line1_df = df[['release_year','rating']].value_counts().reset_index()
            year_line1 = st.slider('Select a range of years',df['release_year'].min(), df['release_year'].max(),(df['release_year'].min(),df['release_year'].max()))
            rating_line1 = st.multiselect('Select a rating',options=unique_rating,default=unique_rating)
            st.form_submit_button('Submit')

    
with st.container():
    st.write("<h3 style='text-align: center;'>Scatter Plot Map</h3>", unsafe_allow_html=True)
    map_df = df[['country','longitude','latitude']].value_counts().reset_index()
    fig = px.scatter_mapbox(map_df, 
                            lat="latitude", lon="longitude", 
                            color="country", 
                            size="count",
                            hover_name= "country",  
                            zoom=1,
                            center= None,
                            mapbox_style="carto-darkmatter",
                            title="Geographical Distribution of Data by Country"
                            )
    st.plotly_chart(fig,use_container_width=True,use_container_height= True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        fig = px.bar(data_frame=bar1_df,
            x = 'genre',
            y = 'count',
            color = 'genre',
            text_auto= True ,
            hover_data=bar1_df,
            template='plotly_dark',
            title = f'Genre Counts in {option1_bar}')
        st.plotly_chart(fig)
        
        st.write("<h3 style='text-align: center;'>Area Line</h3>", unsafe_allow_html=True)
        line_df = line_df[(line_df['country'].isin(country_line))&(line_df['release_year']>=year_line[0])&(line_df['release_year']<=year_line[1])]
        fig = px.area(data_frame= line_df,
                      x='release_year',
                      y= 'count',
                      color='country',
                      template='plotly_dark',
                      title = 'Trend of Data Counts by Country Over Time')
        st.plotly_chart(fig)
        
    with col2:
        st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        fig = px.bar(data_frame=bar2_df,
            x = 'genre',
            y = 'count',
            color = 'genre',
            text_auto= True ,
            hover_data=bar2_df,
            template='plotly_dark',
            title = f'Genre Counts in {option2_bar}')
        st.plotly_chart(fig)
        
        st.write("<h3 style='text-align: center;'>Bar Graph</h3>", unsafe_allow_html=True)
        bar3_df = bar3_df[(bar3_df['release_year']>=year_bar3_df)&(bar3_df['genre'].isin(genre_bar3_df))][0:10]
        fig = px.pie(bar3_df,
            values='count', 
            names='genre', 
            title=f'Top Genres by Count for {year_bar3_df}',
            labels={'value': 'Count', 'genre': 'Genre'})
        st.plotly_chart(fig)
        
        st.write("<h3 style='text-align: center;'>Area Line</h3>", unsafe_allow_html=True)
        line1_df = line1_df[(line1_df['release_year']>=year_line1[0])&(line1_df['release_year']<=year_line1[1])&(line1_df['rating'].isin(rating_line1))]
        fig = px.area(data_frame= line1_df,
                      x='release_year',
                      y= 'count',
                      color='rating',
                      template='plotly_dark',
                      title = 'Trend of Data Counts by Rating Over Time')
        st.plotly_chart(fig)