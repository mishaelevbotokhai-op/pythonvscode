import streamlit as st

saved_amount = (200)

charity_donation = ('Enter how much that you and your friends donated')

gift_cost = ('How much did they spent buying gifts for the elderly in their neighborhood')

cleanup_cost = ('How much did they spend organizing a community claenup event')

refreshment_cost = ('How much did you spend on refreshments')

total_amount = charity_donation + gift_cost + cleanup_cost + refreshment_cost

saved_amount - total_amount

st.write

if st.button('Total amount'):
    saved_amount - total_amount