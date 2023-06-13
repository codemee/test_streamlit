import streamlit as st
import time

hist=[]
count = 0

st.write(count)

if st.checkbox("use web"):
    count += 1
    st.text("use web")
