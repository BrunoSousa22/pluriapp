import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Surpresa", layout="centered")
st.title("Bem-vindaaaaaas 😃!")
# Button
if st.button("Clica para ver a surpresa"):
    resposta = st.radio("Tens a certeza?", ["Sim", "Não"], index=None)

    if resposta == "Sim":
        st.balloons()
    elif resposta == "Não":
        st.write("Tudo bem, sem balões por enquanto 😌")
