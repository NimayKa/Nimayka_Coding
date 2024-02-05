import streamlit as st
import pandas as pd
import numpy as np

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using'
' a dataset kindly provided by SF DPW')
trees_df = pd.read_csv('trees.csv')
st.write(trees_df.head())


#Part 2

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
#st.write(trees_df.groupby(['dbh']).count()['caretaker'])
st.write('---------------')
st.write(df_dbh_grouped)
df_dbh_grouped.columns = ['tree_count']

st.write(df_dbh_grouped)
df_dbh_grouped['new__col'] = np.random.randn(len(df_dbh_grouped))*500

trees_df = trees_df.dropna(subset=['longitude','latitude'])
trees_df = trees_df.sample(n = 1000)
st.map(trees_df)

#create line chart
st.line_chart(df_dbh_grouped)

#create bar chart
st.bar_chart(df_dbh_grouped)

#create area chart
st.area_chart(df_dbh_grouped)