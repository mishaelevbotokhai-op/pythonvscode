import streamlit as st

point = 0

st.title('🚑First Aid Quiz')

name = st.text_input ('Enter your name here')

st.subheader('Question 1: Nosebleed')
st.write('Your friend nose suddenly starts bleeding 😮 what should you do first? ')
q1 = st.selectbox('Pick an answer',['Tilt their head back and pinch the nose','Tilt their head forward and pinch the nose','Make them lie flat on the ground'])

if q1 == 'Tilt their head forward and pinch the nose':
    point  +=1
    st.write(' ✅ That is right',name,' !')

else:
    st.write('❌ Oops, not the best choice.')

st.subheader('Question 2: Choking')
st.write('Someone is eating and suddenly starts coughing hard, can’t speak, and looks panicked 😨 what should you do first? ')
q2 = st.selectbox('Pick an answer',[' Give them water to drink','Perform the Heimlich maneuver',' Tell them to lie down and rest'])

if q2 == 'Perform the Heimlich maneuver':
    point  +=1
    st.write(' ✅ That is right',name,' !')

else:
    st.write('❌ Oops, not the best choice.')


st.subheader('Question 3: Fainting')
st.write('You see your friend faint while standing in the sun ☀️ what should you do first? ')
q3 = st.selectbox('Pick an answer',['Lay them on their back and lift their legs',' Give them food immediately',' Shake them to wake them up'])

if q3 == 'Lay them on their back and lift their legs':
    point  +=1
    st.write(' ✅ That is right',name,' !')

if point == 3:
    st.write("🎉 Excellent! You know your first aid well.")

elif point == 2:
    st.write("👍 Good job! Just a little more practice needed.")

elif point <2:
    st.write("📚 Keep learning! First aid can save lives.")