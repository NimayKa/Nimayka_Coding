import pandas as pd
import numpy
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pydeck as pdk 
import plotly.express as px
import extra_streamlit_components as stx

df = pd.read_csv('netflix.csv')
st.set_page_config(page_title="Second Dashboard",layout="wide", page_icon="📈")

st.write("<h1 style='text-align: center;'>Netflix Visualization</h1>", unsafe_allow_html=True)