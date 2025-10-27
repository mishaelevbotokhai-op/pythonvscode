import streamlit as st

st.subheader("Mishael's stickers ")

name = st.text_input('Enter your name here')

animal_stickers = st.number_input('Enter how many animal stickers you have',0)

superhero_stickers = st.number_input('Enter how many super hero stickers you have',0)

star_stickers = st.number_input('Enter how many star stickers you have')

total_stickers = animal_stickers + superhero_stickers +star_stickers

st.write  ('Hi' ,name, 'You have collected a total of' ,total_stickers,' stickers.')