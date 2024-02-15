import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Central Limit Theorem")
st.subheader("Made by bapak Kau")

with st.form('first form'):
    perc_heads = st.number_input("Chance of Coin Landing on Head",min_value=0.0,max_value=10.0,value=.5)
    graph_title = st.text_input(label='Graph Title')
    submit = st.form_submit_button('Submit')

binom_dist = np.random.binomial(1,perc_heads,1000)
list_of_means = []
for i in range (0, 1000):
    list_of_means.append(np.random.choice(binom_dist,100,replace=True).mean())


fig,ax = plt.subplots()
ax = plt.hist(list_of_means)
plt.title(graph_title)
st.pyplot(fig)