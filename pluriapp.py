import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Demo App", layout="centered")
st.title("🚀 Bem-vindo!")

# Button
if st.button("Clicar aqui para uma surpresa"):
    resposta = st.radio("Tens a certeza que estás pronto?", ["Sim", "Não"], index=None)

    if resposta == "Sim":
        resposta1 = st.radio("Certeza certezinha?", ["Sim", "Não"], index=None)
        if resposta1 == "Sim":
            st.balloons()
        elif resposta1 == "Não":
            st.write("Nem sabes o que perdes")

    elif resposta == "Não":
        st.write("Nem sabes o que perdes")
