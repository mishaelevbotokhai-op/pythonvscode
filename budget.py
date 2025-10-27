import streamlit as st

name = st.text_input('Enter your name here')

monthly_income = st.number_input('Enter your monthly income')

rent = st.number_input('Enter your monthly rent ')

groceries = st.number_input('What is monthly groceries')

transportation = st.number_input('Enter your monthly transportati0n')

other_expenses = st.number_input('Enter your other monthly expenses')

total_expenses = monthly_income + rent + groceries + transportation + other_expenses

remaining_balance = monthly_income - total_expenses

if remaining_balance >= 500:
    st.write('Good Job', name,'! You have ',remaining_balance,' left. consider saving or investing some of it.')

elif remaining_balance >0 and remaining_balance <500 :
    st.write('Nice work', name,'! You have ',remaining_balance,' left. consider saving or investing some of it.')

elif remaining_balance <=0 :
    st.write('Oops', name,'! You are over ',remaining_balance,' left. consider cutting back on expenses.')

