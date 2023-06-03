import streamlit as st

options=st.multiselect(
    '請選擇您喜歡的顏色'
    ['green','yellow','red','blue'],
    ['Yellow','Red'])

st.write('您選擇:',options)


