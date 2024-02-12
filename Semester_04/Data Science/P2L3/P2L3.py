import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pydeck as pdk 
import altair as alt

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
        
        df = pd.read_csv('crime.csv',encoding='windows-1254')
        df.dropna(how='any', inplace=True)

        st.title('Im BATMAN :smiling_imp:')
        st.write('This shows the area of the criminally criminal act that criminals had done during the specific month')
        with st.form("Filter Month Form"):
            select_month = st.selectbox("Month", df["MONTH"].unique())
            select_offense = st.selectbox("Offense",df['OFFENSE_CODE_GROUP'].unique())
            my_submit_button = st.form_submit_button()

                #filtered_month = df[df['MONTH'] == select_month]
                #filtered_crime = df[df['OFFENSE_CODE_GROUP'] == select_offense]
                
            filtered = (df['MONTH'] == select_month) & (df['OFFENSE_CODE_GROUP'] == select_offense) #combination of the above

            filtered_month_offense = df[filtered]

            sf_initial_view = pdk.ViewState(
                latitude=42.30,
                longitude=-71.06,
                zoom=13,
                pitch=30
                )

            hx_layer = pdk.Layer(
                'HexagonLayer',
                data = filtered_month_offense,
                get_position = ['Long', 'Lat'],
                radius=100,
                extruded=True)

            #check for styles https://docs.mapbox.com/api/maps/styles/

            st.pydeck_chart(pdk.Deck(
                #map_style='mapbox://styles/mapbox/light-v9',
                map_style='mapbox://styles/mapbox/satellite-v9',
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



        #Second Visualization

        st.title('Crime Count Bar Chart')
        st.write('This shows the count of the criminally criminal act that criminals had done during the specific month')

        crime_counts = filtered_month_offense.groupby('OFFENSE_CODE_GROUP').size().reset_index(name='count')
        crime_counts = crime_counts[crime_counts['OFFENSE_CODE_GROUP'] == select_offense]

        fig = alt.Chart(crime_counts).mark_bar().encode(x= alt.X('OFFENSE_CODE_GROUP', title = "Crime\Offense"),y= 'count')

        st.altair_chart(fig)