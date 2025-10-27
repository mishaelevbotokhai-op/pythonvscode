import streamlit as st

st.title(':rainbow[Cool Swords]')

k1,k2,k3 = st.columns(3)

with k1:
    st.image('https://tse2.mm.bing.net/th/id/OIP.PlSjNScEnnlSG3RqOgXT9QHaEK?pid=Api&P=0&h=180')

with k2:
    st.subheader(':rainbow[Katanas:£39]')

with k3:
    Katana = st.number_input(':rainbow[How much katanas do you want to buy?]',0)

st.divider()

s1,s2,s3 = st.columns(3)

with s1:
    st.image('https://tse2.mm.bing.net/th/id/OIP.ptpOx03vp6b8D6TG7Sg34gHaEK?pid=Api&P=0&h=180')

with s2:
    st.subheader(':rainbow[Scimitar:£199]')

with s3:
    Scimitar = st.number_input(':rainbow[How much scimitars do you want to buy?]',0)

st.divider()

r1,r2,r3 = st.columns(3)

with r1:
    st.image('https://tse4.mm.bing.net/th/id/OIP.rCfr5p3eP0yslbWSRZQG8AHaFK?pid=Api&P=0&h=180')

with r2:
    st.subheader(':rainbow[Rapier:£300]')

with r3:
    Rapier = st.number_input(':rainbow[How much rapiers do you want to buy?]',0)

st.divider()

h1,h2,h3 = st.columns(3)

with h1:
    st.image('https://tse3.mm.bing.net/th/id/OIP.08fH-8tsGREn43Ow7T9iWAHaE6?pid=Api&P=0&h=180')

with h2:
    st.subheader(':rainbow[Hook Sword:£58]')

with h3:
    HookSword = st.number_input(':rainbow[How much hook swords do you want to buy?]',0)

st.divider()

d1,d2,d3 = st.columns(3)

with d1:
    st.image('https://tse2.mm.bing.net/th/id/OIP.BF63cfCIT8trKqP6zGJRAwHaHa?pid=Api&P=0&h=180')

with d2:
    st.subheader(':rainbow[Dagger:28]')

with d3:
    Dagger = st.number_input(':rainbow[How much daggers do you want to buy?]',0)

Katanaprice = Katana * 39
Scimitarprice = Scimitar * 199
Rapierprice = Rapier * 300
HookSwordprice = HookSword * 58
Daggerprice = Dagger * 28

bill = Katanaprice + Scimitarprice + Rapierprice + HookSwordprice + Daggerprice

if st.button('Check your bill'):
    st.success(f'Your bill is {bill} dollars')