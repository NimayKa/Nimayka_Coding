#Bokeh 
#conda install bokeh
import streamlit as st
import pandas as pd
from bokeh.plotting import figure

#set the page to full width
st.set_page_config(layout="wide")

#declare your columns
#width between column
col1, col2 = st.columns([0.5, 0.5])

with col1:
    st.title('SF Trees')
    st.write('This app analyses trees in San Francisco using'
            ' a dataset kindly provided by SF DPW')
    st.subheader('Plotly Chart')
    trees_df = pd.read_csv('trees.csv')

    scatterplot = figure(title = 'Bokeh Scatterplot')
    
    scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
    scatterplot.yaxis.axis_label = "site_order"
    scatterplot.xaxis.axis_label = "dbh"
    st.bokeh_chart(scatterplot)

#Altair
#conda install altair
import streamlit as st
import pandas as pd
import altair as alt

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
        ' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('trees.csv')
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count')
st.altair_chart(fig)

with col2:
#Altair pt 2

    import streamlit as st
    import pandas as pd
    import altair as alt

    st.title('SF Trees')
    st.write('This app analyses trees in San Francisco using'
            ' a dataset kindly provided by SF DPW')
    trees_df = pd.read_csv('trees.csv')
    fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y = 'count(*):Q')
    st.altair_chart(fig)

#PyDeck
#conda install pydeck
#streamlit config show - in folder C:/users/.../.streamlit/config.toml - global config
#streamlit config show > ~/.streamlit/config.toml - by default, the file are unavailable, use this to create the file
import streamlit as st
import pandas as pd
import pydeck as pdk 

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
         ' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('trees.csv')
trees_df.dropna(how='any', inplace=True)

sf_initial_view = pdk.ViewState(
    latitude=37.77,
    longitude=-122.4,
    zoom=11,
    pitch=30
    )

hx_layer = pdk.Layer(
    'HexagonLayer',
    data = trees_df,
    get_position = ['longitude', 'latitude'],
    radius=100,
    extruded=True)#true 3d Hex , false 2d hex

#check for styles https://docs.mapbox.com/api/maps/styles/

st.pydeck_chart(pdk.Deck(
   # map_style='mapbox://styles/mapbox/light-v9',
   
    map_style='mapbox://styles/mapbox/satellite-v9',
    initial_view_state=sf_initial_view,
    layers = [hx_layer]
    ))