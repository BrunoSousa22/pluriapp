import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Demo App", layout="centered")
st.title("🚀 Bem-vindo!")

# Use session state to track the steps
if "mostrar_pergunta_1" not in st.session_state:
    st.session_state.mostrar_pergunta_1 = False
if "mostrar_pergunta_2" not in st.session_state:
    st.session_state.mostrar_pergunta_2 = False

# Button click
if st.button("Clicar aqui para uma surpresa"):
    st.session_state.mostrar_pergunta_1 = True

# First question
if st.session_state.mostrar_pergunta_1:
    resposta = st.radio("Tens a certeza que estás pronto?", ["Sim", "Não"], key="pergunta1")

    if resposta == "Sim":
        st.session_state.mostrar_pergunta_2 = True
    elif resposta == "Não":
        st.write("Nem sabes o que perdes")

# Second question
if st.session_state.mostrar_pergunta_2:
    resposta1 = st.radio("Certeza certezinha?", ["Sim", "Não"], key="pergunta2")
    
    if resposta1 == "Sim":
        st.balloons()
    elif resposta1 == "Não":
        st.write("Eu vi logo!")
