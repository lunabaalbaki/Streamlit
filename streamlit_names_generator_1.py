import streamlit as st
import pandas as pd
import random
import numpy as np

st.title("this is a name generator....")

df_names= pd.read_excel("/Users/user/Desktop/excel_names.xlsx")
df_names.names

#im doing a name list beacuse in the function randpm.sample I can't put a dataframe.
#so this is how we do a list from a dataframe
name_list= df_names.names.tolist()
st.write(name_list)
st.write(len(df_names.names))


#we put value=1 because if we dont r7 ykon float the number not integer
n=st.number_input("Please choose a number", value=1)
#if clicked on the botton this would give us
#if i want to be put the button on the side bar:
#if st.sidebar.button("generate names"):
if st.button("generate names"):
    st.write("the selected names are:", random.sample(name_list,k=n))
    st.balloons()

# lets do slider
#n=st.slider("choose a sample number", min_value=1, max_value=len(name_list))
#if clicked on the botton this would give us
#if st.button("generate names"):
    #st.write("the selected names are:", random.sample(name_list,k=n))

#if i want names to be choosen one at a time. like 5 names but every time a name.
st.header("another way of generating")
if st.button("generate names diff"):
    for i in range(1,3):
        st.write('name is', random.sample(name_list, k=1))
#but here the name can be appeared twice
