import streamlit as st 
import time as t
st.image("social.png")

st.title("Welcome to Socialprachar")

# header
st.header("Data science")

# sub header
st.subheader("Data types")

# To give information
st.info("Information details of a user")

# warning message
st.warning("Come on time or else you will be marked absent")

# error message
st.error("Wrong Password")

# success message
st.success("congrats you have got A")

# write
st.write("Student name")
st.write(range(50))

## markdown
st.markdown("# Social Prachar")
st.markdown(":moon:")


# text
st.text("Social Prachar")

# to write a caption
st.caption("Caption is here")

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

# text input
st.text_input("Enter your email address")

# data input
st.date_input("Opening ceremony")

# time input
st.time_input("Hey whats the timing")

# text area
st.text_area("welcome to the social prachar website.Hello learners")

st.file_uploader("upload your file/folder")

st.color_picker("color")

st.progress(90)

# spinner

with st.spinner("Just wait"):
    t.sleep(1)
    
    
#  balloons 
st.balloons()  

st.sidebar.title("Social Prachar")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("Password")    
st.sidebar.button("Submit")
st.sidebar.radio("Professional Expert",["Student","Working","Others"])


# data visualization
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=["x","y"])
st.bar_chart(data)
st.title("Line Chart")
st.line_chart(data)
st.title("Area Chart")
st.line_chart(data)

