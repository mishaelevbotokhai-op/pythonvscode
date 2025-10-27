
import streamlit as st

st.subheader('Mishael age calculator')

name = st.text_input('Enter your name here')

yob = st.number_input('Enter your year of birth here',0)

cy = st.number_input('Enter your current year',0)

age = cy - yob

st.write(name,' you will be',age,'in year',cy)