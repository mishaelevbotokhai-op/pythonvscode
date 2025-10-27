import streamlit as st

st.header('Mishael Restaurant')

st.image('https://tse3.mm.bing.net/th/id/OIP.Kh0CWrWn6l1kz4xtmiEUdwHaDV?pid=Api&P=0&h=180')

st.subheader('food category')
bill = 0

food1,food2,food3,food4 = st.columns(4)

with food1:
    if st.checkbox('Rice and Egusi soup:$20'):
        st.success('Ok Done')

    if st.checkbox('Semo and Ogbono soup:$30'):
        st.success('Ok Done')
        bill += 15
with food2:
    if st.checkbox('Burger:$70'):
         st.success('Ok Done')

    if st.checkbox('French Fries:$80'):
         st.success('Ok Done')
         bill += 20
with food3:
    if st.checkbox('Pizza:$90'):
         st.success('Ok Done')

    if st.checkbox('Cakes:$100'):
         st.success('Ok Done')
         bill += 25
with food4:
    if st.checkbox('Pancakes:$50'):
         st.success('Ok Done')

    if st.checkbox('Chicken:$30'):
         st.success('Ok Done')
         bill += 25

st.image('https://tse1.mm.bing.net/th/id/OIP.VDUfxHV_66PIwETAwrZJcAHaDH?pid=Api&P=0&h=180')
st.subheader('Drinks category')

drink1,drink2,drink3 = st.columns(3)

with drink1:
    if st.checkbox('Pespi:$15'):
        st.success('Ok Done')
    if st.checkbox('Mango juice:$20'):
        st.success('Ok Done')     
        bill += 30 

with drink2:
    if st.checkbox('Cocacola:$25'):
        st.success('Ok Done')
    if st.checkbox('Fanta:$30'):
        st.success('Ok Done') 
        bill += 45     

with drink3:
    if st.checkbox('Sprite:$40'):
        st.success('Ok Done')
    if st.checkbox('Apple Juice:$45'):
        st.success('Ok Done')
        bill += 35
st.subheader('Snacks Category')
st.image('https://tse4.mm.bing.net/th/id/OIP.LNoqmYilMnU8pFmcN7KI9wHaDF?pid=Api&P=0&h=180')
snack1,snack2 = st.columns(2)

with snack1:
    if st.checkbox('Pringles:$10'):
        st.success('Ok Done')
    
   

    if st.checkbox('Oreo Biscuits:$5'):
        st.success('Ok Done')
        bill += 21
   
        

with snack2:
    if st.checkbox('Mars Chocolate:$10'):
        st.success('Ok Done')
        
    if st.checkbox('M & M:$5'):
        st.success('Ok Done')
        bill += 10

st.subheader('Fruits Category')
st.image('https://tse1.mm.bing.net/th/id/OIP.4iVhY0ihCHf47X9w44yKZQHaCf?pid=Api&P=0&h=180')
fruit1,fruit2,fruit3 = st.columns(3)

with fruit1:
    if st.checkbox('Apple:$5'):
        st.success('Ok Done')

    if st.checkbox('Banana:$5'):
        st.success('Ok Done')
        bill += 5

with fruit2:
    if st.checkbox('WaterMelon:$5'):
        st.success('Ok Done')

    if st.checkbox('Pineapple:$5'):
        st.success('Ok Done')
        bill += 5

with fruit3:
    if st.checkbox('Grapes:$5'):
        st.success('Ok Done')

    if st.checkbox('Coconut:$5'):
        st.success('Ok Done')
        bill += 15

if st.checkbox('Check my bill'):
    st.write('Your bill is',bill,'dollars')