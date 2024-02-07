import streamlit as st
import pandas as pd
import pydeck as pdk 
import altair as alt

st.title('CRIME IN BOSTON')
st.write('INIT BRUVV')
crime_df = pd.read_csv('crime.csv',encoding='windows-1254')
crime_df.dropna(how='any', inplace=True)

sf_initial_view = pdk.ViewState(
    latitude=42.285,
    longitude=-71.06,
    zoom=11.5,
    pitch=30
    )

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

crime_df['MONTHYEAR'] =  crime_df["MONTH"].astype(str)+"/"+crime_df["YEAR"].astype(str)
filtered_occur = crime_df[['MONTHYEAR','SHOOTING']].value_counts().reset_index(name='count')
filtered_occur['MONTHYEAR'] = pd.to_datetime(filtered_occur['MONTHYEAR'], format='%m/%Y')
filtered_occur = filtered_occur.sort_values('MONTHYEAR')

# Create a line chart
chart = alt.Chart(filtered_occur).mark_line().encode(
    x='MONTHYEAR',
    y='count',
    color='SHOOTING'
).properties(
    width=800,
    height=400
)

# Render the chart using Streamlit
st.write(chart)
