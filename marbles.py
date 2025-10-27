import streamlit as st

st.subheader("Mishael's marbles ")

name = st.text_input('Enter your name here')

red_marbles = st.number_input('Enter how many red marbles you have',0)

blue_marbles = st.number_input('Enter how many blue marbles you have',0)

green_marbles = st.number_input('Enter how many green marbles you have',0)

total_marbles = red_marbles +  blue_marbles +green_marbles
if st.button('Total marbles'):
   st.write('Hi' ,name, 'You have collected a total of' ,total_marbles,' marbles.')