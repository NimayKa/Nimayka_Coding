import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title('Assginemnt 01')
st.markdown('Netflix Analysis')

netflix_file = st.file_uploader('Upload Your Files')

if netflix_file is not None:
    netflix_df = pd.read_csv(netflix_file)
else:
    st.stop()