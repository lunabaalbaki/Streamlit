import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Suicide per Country")
#Import
df = pd.read_csv("/Users/user/Desktop/master.csv")
#Image
from PIL import Image
image = Image.open('/Users/user/Desktop/viz/sui2.jpeg')
st.image(image, caption='Suicide', use_column_width=True)

#Information about all Countries
if st.button('Click to Check Information for all Countries'):
    st.write(df)

#Information About Albania
Kyrgyzstan = df[df['country']=='Kyrgyzstan']
if st.button('Click to check Information for Kyrgyzstan'):
    st.write(Kyrgyzstan)

#Compare Argentina and Albania in the number of Suicide cases per 100k per population
import plotly.graph_objects as go

years = [1987, 1992, 1995, 1998, 2001, 2010]

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=[6.71, 3.41, 5.06, 7.74, 10.65, 8.27],
                name='Albania',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=years,
                y=[7.27, 13.7, 13,5, 8,4, 5.2, 3.2],
                name='Argenina',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='Number of Suicide/100k per population - Comparing Argentina and Albania',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Per 100k per population',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig)

#Check the population of canada over the years
df_canada = px.data.gapminder().query("country == 'Canada'")
fig2 = px.bar(df_canada, x='year', y='pop', title= "Population in Canada over the years")
st.plotly_chart(fig2)
