import os

import numpy as np
import openmc
import streamlit as st
import plotly.graph_objects as go

key = 1

number_of_elements = st.selectbox(key = key,
                label='Number of different elements',
                options=range(0, 10))

element_symbols_and_values = []
for i in range(number_of_elements):
    key = key + 1
    element_symbol = st.selectbox(key = key,
                label='Element ' + str(i+1) +' symbol',
                options=['a','b'])

    key = key + 1
    element_value = st.number_input(key = key,
                min_value=0.,
                label='Element ' + str(i+1) + ' mass fraction')

    # if element_value 
    element_symbols_and_values.append({element_symbol: element_value})

if st.button('create graph'):
    st.write(element_symbols_and_values)

    fig = go.Figure()

    x_data = [element_symbols_and_values[0]['a']]
    y_data = [element_symbols_and_values[0]['a']]
    mt_number = 5
    print(x_data)

    fig.add_trace(go.Scatter(x=x_data,
                                y=y_data,
                            name= mt_number,
                            mode='markers'
                            )
                    )

    fig.update_layout(barmode='overlay',
                    xaxis_title='Macrosofic ',
                    yaxis_title='energy',
                    title="Impact of ",
                    showlegend=True
                    )

    fig.update_traces(opacity=0.4)

    st.write(fig)
