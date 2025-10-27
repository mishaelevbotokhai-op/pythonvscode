import streamlit as st

st.header('Mishael fashion place')

st.image('https://tse1.mm.bing.net/th/id/OIP.JLw1VWyq4vahk1epQKKcFQHaE8?pid=Api&P=0&h=180')

st.subheader('Children category')
bill = 0

cloth1,cloth2,cloth3 = st.columns(3)

with cloth1:
    if st.checkbox('Red Top:15'):
        st.success('Ok Done')
        bill+=15
    
    if st.checkbox('Black Top:$15'):
        st.success('Ok Done')
        bill+=15

with cloth2:
    if st.checkbox('spiderman costume:$20'):
        st.success('Ok Done')
        bill+=20
    
    if st.checkbox('batman costume:$20'):
        st.success('Ok Done')
        bill+=20

with cloth3:
    if st.checkbox('Blue puma top:$10'):
        st.success('Ok Done')
        bill+=10
    
    if st.checkbox('Red puma top:$10'):
        st.success('Ok Done')
        bill+=10
 

st.image('https://tse2.mm.bing.net/th/id/OIP.NaVJIWXmXOiBQiGtgiCBYQHaEc?pid=Api&P=0&h=180')
st.subheader('Mens category')
bill = 0

Men1,Men2,= st.columns(2)

with Men1:
    if st.checkbox('Tie:$5'):
        st.success('Ok Done')
        bill+=5

    if st.checkbox('Buxers:$5'):
        st.success('Ok Done')
        bill+=5


with Men2:
    if st.checkbox('Shorts:$10'):
        st.success('Ok Done')
        bill+=10

    if st.checkbox('Suit:$10'):
        st.success('Ok Done')
        bill+=10


st.image('https://tse2.mm.bing.net/th/id/OIP.xb0-7OI5IIQxz1b2FS4GngHaE-?pid=Api&P=0&h=180')
st.subheader('Women category')

women1,women2 =st.columns(2)

with women1:
    if st.checkbox('Bra:$5'):
        st.success('Ok Done')
        bill+=5

    if st.checkbox('Gown:$20'):
        st.success('Ok Done')
        bill+=20


with women2:
    if st.checkbox('Crop Top:$10'):
        st.success('Ok Done')
        bill+=10

    if st.checkbox('Tights:$10'):
        st.success('Ok Done')
        bill+=10

if st.checkbox('Check my bill'):
    st.write('Your bill is',bill,'dollars')