import streamlit as st

st.header('My Information (Cloud App)')
name = st.text_input('What is your name?')
st.write('My name is', name,'.')
age = st.number_input('How old are you?')
st.write('I am ', age,'years old.')