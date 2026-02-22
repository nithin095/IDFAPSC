import streamlit as st 

st.title("Main Calculator App")

expr = st.text_input("Enter Expression, eg: 2+3","4*3")
if st.button("Calculate"):
    try:
        allowed = "0123456789+-*/().%"
        if all(ch in allowed for ch in expr):
            st.success(eval(expr))
        else:
            st.error("Invalid Characters")
    expect Exception as e:
        st.error(e)            