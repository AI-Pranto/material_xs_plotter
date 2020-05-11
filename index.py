import os

import numpy as np
import openmc
import streamlit as st

key = 1



number_of_elements = st.selectbox(key = key,
                label='Number of different elements',
                options=range(1, 10))

for i in range(number_of_elements):
    key = key + 1
    element_symbol = st.selectbox(key = key,
                label='Element',
                options=['a','b'])

    key = key + 1
    element_value = st.text_input(key = key,
                label='Element')


if st.button('create graph'):
    number_of_elements=number_of_elements+1
    print(number_of_elements)
