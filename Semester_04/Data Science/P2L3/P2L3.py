import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pydeck as pdk 

crime_df = pd.read_csv('crime.csv', encoding='windows-1254')
crime_df.dropna(how='any', inplace=True)

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>CRIME IN BOSTON</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>'INIT BRUVV'</p>", unsafe_allow_html=True)

with st.container():
    
    col1, col2 = st.columns([0.5, 0.5])

    with col1:


        sf_initial_view = pdk.ViewState(
            latitude=42.285,
            longitude=-71.06,
            zoom=11.5,
            pitch=30
            )
        # Map Chart
        st.header('Map Chart')
        st.subheader('Location Activity')
        
        with st.form('first form'):
            Month = st.selectbox('Month',crime_df['MONTH'].unique())
            submit = st.form_submit_button('Submit')
            st.write(Month)
            filtered = crime_df[crime_df['MONTH'] == Month]
            
        hx_layer = pdk.Layer(
            'HexagonLayer',
            data = filtered,
            get_position = ['Long','Lat'],
            radius=100,
            extruded=False)#true 3d Hex , false 2d hex


        st.pydeck_chart(pdk.Deck(
        
            map_style='mapbox://styles/mapbox/streets-v12',
            initial_view_state=sf_initial_view,
            layers = [hx_layer]
            ))

    with col2:
        # Line Graph
        st.header('Line Chart')
        st.subheader('Shooting Throughout 2016-2018')
        
        crime_df['MONTHYEAR'] =  crime_df["MONTH"].astype(str)+"/"+crime_df["YEAR"].astype(str)
        filtered_occur = crime_df[['MONTHYEAR','SHOOTING']].value_counts().reset_index(name='count')
        filtered_occur['MONTHYEAR'] = pd.to_datetime(filtered_occur['MONTHYEAR'], format='%m/%Y')
        filtered_occur = filtered_occur.sort_values('MONTHYEAR')
        
        fig, ax = plt.subplots(figsize=(16, 9))
        sns.lineplot(ax=ax, data=filtered_occur, x='MONTHYEAR', y='count', hue='SHOOTING', marker='o')
        ax.set_xlabel('Year - Month')
        ax.set_ylabel('Count')
        ax.set_title('Shooting Throughout 2016-2018')
        ax.tick_params(axis='x')
        st.pyplot(fig)
        
        # Bar Graph
        st.header('Bar Graph')
        st.subheader('Offense Code')
        ocg_selectbox = st.multiselect('Choose a Offense Code',crime_df['OFFENSE_CODE_GROUP'].unique())
        
        ocg = crime_df['OFFENSE_CODE_GROUP'].value_counts().reset_index()
        if not ocg_selectbox :
            ocg_filtered= ocg.head(5)
        else:
            ocg_filtered= ocg[ocg['OFFENSE_CODE_GROUP'].isin(ocg_selectbox)]
            
        fig, ax = plt.subplots(figsize=(16, 9))
        sns.barplot(data=ocg_filtered, x='OFFENSE_CODE_GROUP', y='count', ax=ax)
        ax.set_title('Frequency of Offense Code Groups')
        ax.set_xlabel('Offense Code Group')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)
            
        