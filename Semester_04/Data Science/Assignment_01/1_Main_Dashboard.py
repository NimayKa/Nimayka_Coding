import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("netflix.csv")
st.set_page_config(page_title="Main Dashboard",layout="wide", page_icon="📈")

unique_type = df["type"].unique()
unique_country = df["country"].unique()
unique_year = sorted(df["release_year"].unique(),reverse=True)
unique_rating = sorted(df["rating"].unique())
genre_df = df[["country", "release_year", "genre_1", "genre_2", "genre_3"]].melt(id_vars=["country", "release_year"], value_vars=["genre_1", "genre_2", "genre_3"], value_name="genre").drop(columns=["variable"]).dropna()
unique_genre = genre_df["genre"].unique()


with st.container():
    st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)
    
with st.sidebar:
    st.write("<h1 style='text-align: center; font-size: 34px;'>Visualization Filter</h1>", unsafe_allow_html=True)
    
    #First
    with st.form("First Filter",border=False): 
        with st.expander("First Filter"): 
            st.subheader("Map Filter") 
            type_map = st.multiselect("Select A Type",unique_type,(unique_type))
            country_map = st.multiselect("Select A Country",unique_country,(unique_country))
            map_df = df[(df["type"].isin(type_map))&(df["country"].isin(country_map))]  
            st.form_submit_button("Submit")
                
    #Second 
    with st.form("Second Filter",border=False):
        with st.expander("Second Filter"):
            st.subheader("Line Filter") 
            line_year = st.slider("Select a range of years",df["release_year"].min(), df["release_year"].max(),(df["release_year"].min(),df["release_year"].max()))
            line_type = st.multiselect("Select Your Type",unique_type,(unique_type))
            st.form_submit_button("Submit")
                
    #Third         
    with st.form("Third Filter",border=False):
        with st.expander("Third Filter"):
            st.subheader("Scatter Filter")     
            scatter_type = st.multiselect(label="Select a Type",options=unique_type,default=unique_type)
            scatter_rating = st.multiselect(label = "Select a rating",options=unique_rating,default=unique_rating)
            scatter_year = st.slider("Select a range of years",df["release_year"].min(), df["release_year"].max(),(df["release_year"].min(),df["release_year"].max()))
            st.form_submit_button("Submit")

    #Forth
    with st.form("Forth Filter", border=False):
        with st.expander("Forth Filter"):
            st.subheader("Forth Visualization")
            country1_bar, country2_bar, year_bar = st.selectbox(label="Select a First Country",options= unique_country), st.selectbox(label="Select a Second Country", options=unique_country), st.selectbox(label="Select a Year", options=unique_year)
            rating_bar = st.multiselect(label="Select Your Type",options= unique_genre,default= (unique_genre))
            st.form_submit_button("Submit")

    #Fifth
    with st.form("Fifth Filter", border= False):
        with st.expander("Fifth Filter"):
            pie_df = df[df["director"]!= "Not Given"]
            year_pie =  st.selectbox("Select a year", unique_year)
            st.form_submit_button("Submit")
    #Sixth
    with st.form("Sixth Filter",border=False):
        with st.expander("Sixth Filter"):
            st.subheader("Map Filter") 
            rating_map1 = st.multiselect(label="Select Your Type",options=unique_rating,default=unique_rating)
            country_map1 = st.multiselect(label="Select A Country",options=unique_country,default=unique_country)
            st.form_submit_button("Submit")
                
with st.container():

    # 4 Column
    st.write("<h3 style='text-align: center;''>Scatter Plot Map</h3>", unsafe_allow_html=True)
    map_df = map_df[["country","type","latitude","longitude"]].value_counts().reset_index()   
    
    fig = px.scatter_mapbox(map_df, 
                            lat="latitude", lon="longitude", 
                            color="type", 
                            size="count",
                            hover_name= "country",  
                            zoom=1,
                            center= None,
                            mapbox_style="carto-darkmatter",
                            title="Occurrences of Types in Different Countries"
                            )
    
    st.plotly_chart(fig,use_container_width=True,use_container_height= True)
    
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("<h3 style='text-align: center;'>Line Graph</h3>", unsafe_allow_html=True)
        line_df = df[(df["release_year"]>=line_year[0])&(df["release_year"]<=line_year[1])]
        line_df = line_df[(line_df["type"].isin(line_type))]
            
        line_df=line_df[["release_year","type"]].value_counts().reset_index()
        fig = px.area(data_frame= line_df,
                      x="release_year",
                      y= "count",
                      color="type",
                      color_discrete_sequence=["#a8f53d","#03AFAE"],
                      template="plotly_dark",
                      title = "Trend of Release Counts by Year and Type")
        st.plotly_chart(fig)
        
        st.write("<h3 style='text-align: center;'>Subplot Bar</h3>", unsafe_allow_html=True)
        
        bar1_df = genre_df[(genre_df["country"] == country1_bar) & (genre_df["release_year"] == year_bar) & (genre_df["genre"].isin(rating_bar))]
        bar2_df = genre_df[(genre_df["country"] == country2_bar) & (genre_df["release_year"] == year_bar) & (genre_df["genre"].isin(rating_bar))]
        bar1_df = bar1_df[["country","release_year","genre"]].value_counts().reset_index().sort_values(by="genre")
        bar2_df = bar2_df[["country","release_year","genre"]].value_counts().reset_index().sort_values(by="genre")
        
        fig = make_subplots(rows=1, cols=2, subplot_titles=(f"{country1_bar}", f"{country2_bar}"))
        fig.add_trace(
            go.Bar(x=bar1_df["genre"], y=bar1_df["count"], marker=dict(color=bar1_df["count"])),
            row=1, col=1
        )

        fig.add_trace(
            go.Bar(x=bar2_df["genre"], y=bar2_df["count"], marker=dict(color=bar2_df["count"])),
            row=1, col=2
        )

        fig.update_layout(template="plotly_dark", title_text=f"Comparison of Genre Counts in {country1_bar} and {country2_bar} for {year_bar}")

        st.plotly_chart(fig)
        
    with col2:
        st.write("<h3 style='text-align: center;'>Scatter Plot</h3>", unsafe_allow_html=True) 
        scatter_df = df[(df["type"].isin(scatter_type))&(df["rating"].isin(scatter_rating))&(df["release_year"]>=scatter_year[0])&(df["release_year"]<=scatter_year[1])]
        scatter_df = scatter_df[["release_year","type","rating"]].value_counts().reset_index()
        
        fig = px.scatter(scatter_df,
                        x="release_year", 
                        y="count", 
                        color="rating",
                        size="count" ,
                        symbol ="type",
                        title="Scatter Plot of Data Counts by Release Year, Type, and Rating"
                        )
        st.plotly_chart(fig)
        
        st.write("<h3 style='text-align: center;'>Pie Graph</h3>", unsafe_allow_html=True)
        pie_df = pie_df[(pie_df["release_year"]==year_pie)]
        fig = px.pie(
            data_frame=pie_df["director"].value_counts()[0:5],
            names=pie_df["director"].value_counts()[0:5].index,
            values=pie_df["director"].value_counts()[0:5],
            labels={"names": "Director"},
            title=f"Distribution of Top Directors in {year_pie}",
            template="plotly_dark"
        )
        st.plotly_chart(fig)
        
with st.container():
    # 4 Column Filter or 1 Column?
    st.write("<h3 style='text-align: center;'>Scatter Plot Map</h3>", unsafe_allow_html=True)
    map1_df = df[(df["rating"].isin(rating_map1))&(df["country"].isin(country_map1))]
    map1_df = map1_df[["country","rating","latitude","longitude"]].value_counts().reset_index() 
    fig = px.scatter_mapbox(map1_df, 
                            lat="latitude", lon="longitude", 
                            color="rating", 
                            size="count",
                            hover_name= "country",  
                            zoom=1,
                            center= None,
                            mapbox_style="carto-darkmatter",
                            title="Distribution of Ratings by Country on Map"
                            )
    st.plotly_chart(fig,use_container_width=True,use_container_height= True)