import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Central Limit Theorem")
st.subheader("Made by bapak Kau")

perc_heads = st.number_input("Chance of Coin Landing on Head",min_value=0.0,max_value=100.0,value=2.5)