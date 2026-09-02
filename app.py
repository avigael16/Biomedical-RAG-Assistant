import streamlit as st

st.title("Mon premier projet IA")

name = st.text_input("Avigael")

if name:
    st.write("Bonjour", name)