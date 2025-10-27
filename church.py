#homework: create a simple church form with 3 columns 
#1 that has a name (text), type their age and choose their gender (st.radio) on 3 columns

#2 then a text area to ask for other additional message

# decide member class with these categories: (Kids(3-12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) --== if block

# when you click on submit button:
#Make sure you group members in different category based on their age 
#write this welcome [name], you will be in the [churchclass] class
#your message has been received
#show the user message here

import streamlit as st

st.title('Christian Church Foundation')

name,age,gender, = st.columns(3)

with name:
    name = st.text_input('What is your name?')

with age:
    age = st.number_input('How old are you?')

with gender:
    gender = st.radio('Please enter your gender',['Male','Female' ],horizontal=True)

message = st.text_area ('Send your message to the church👍',height = 300)

if st.button('Send to the church'):
    st .success('Your message have been recieved')
    st.info(message)
    if age >=3 and age <=12:
        st.write('You are in the kids group!')

    elif age >=13 and age <=19:
        st.write('You are in the teens group!')

    elif age >=20 and age <=35:
        st.write('You are in the youth group!')

    elif age >=36 and age <=64:
        st.write('You are in the adults group!')

    elif age >=65:
        st.write('You are in the elders group')






