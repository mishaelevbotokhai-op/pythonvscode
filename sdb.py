#A school wants you to develop a web app for their teachers.
#Your app should enable the teacher get the scores of the students
#it will calc the total, average and the grade by itself
#it will plot the chart (bar/pie) of the subjects 
#save into a file on the computer
#view the students database with a table
#classwork:
#name, all school subjects in 2 columns
#if submit button clicked:
#calc totalscore, averagescore
#write (name, your total score is ----. Average is ----)

import streamlit as st

menu = st.sidebar.selectbox('menu',['input score','Information'])

name= st.text_input('Please enter students name')

left,right = st.columns(2)


with left:
    math = st.number_input('Enter your math score',0,100)
    english = st.number_input('Enter your english score',0,100)
    science = st.number_input('Enter your science score',0,100)

with right:
    History =st.number_input('Enter your history score',0,100)
    Spanish =st.number_input('Enter your Spanish score',0,100)
    French =st.number_input('Enter your French score',0,100)


if st.button('See your score'):
    totalscore = math + english + science + History + Spanish + French
    averagescore = totalscore / 6


    if averagescore >= 70:
        grade = 'A'

    elif averagescore >= 60:
        grade = 'B'

    elif averagescore >= 50:
        grade = 'C'

    elif averagescore >= 40:
        grade = 'D' 

    elif averagescore >= 30:
        grade = 'E'

    elif averagescore < 30:
        grade = 'F'                  


    st.write(name,'Your total score is ',totalscore,'and your average score is ',averagescore,'Your grade score is',grade)    