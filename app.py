import streamlit as st
import pandas as pd
import numpy as np


### title of the app 
st.title("My first streamlit app!!")

## display a simple text
st.write("Hey!! This is my Simple Text")

### display a simple dataframe
df = pd.DataFrame({
    "first column":[1,2,3,4,5,6],
    "second column":[10,20,30,40,50,60]
})

## display dataframe
st.write("Here's a simple DateFrame:")
st.write(df)


### create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)
st.line_chart(chart_data) 


### to display a mathematical equation

st.latex (r'''a+b x*2+c''')   

### widget 

st.checkbox("Login")

### button 
st.button("click")

## radio widget
st.radio("Pick your gender",["Male","Famale","Other"])

### select box
st.selectbox("Pick your course",["ML","Cloud","Data science"])


## multiselect
st.multiselect("Choose the dept",["Content","Sales","Marketing","Testing"])


### selectslider
st.select_slider("Rating",["Bad","Good","Excellent"])

## slider
st.slider("Enter ur number",0,30)

# number input
st.number_input("Pick a number",0,100) 