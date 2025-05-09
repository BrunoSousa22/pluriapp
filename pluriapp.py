import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Demo App", layout="centered")
st.title("🚀 Bem-vindo!")

# Inicializar estado
if "etapa" not in st.session_state:
    st.session_state.etapa = 0

# Etapa 0: Botão inicial
if st.session_state.etapa == 0:
    if st.button("Clicar aqui para uma surpresa"):
        st.session_state.etapa = 1

# Etapa 1: Primeira pergunta
if st.session_state.etapa == 1:
    resposta = st.radio("Tens a certeza que estás pronto?", ["Sim", "Não"], key="pergunta1")
    if resposta == "Sim":
        st.session_state.etapa = 2
        st.experimental_rerun()
    elif resposta == "Não":
        st.write("Nem sabes o que perdes 😢")

# Etapa 2: Segunda pergunta
if st.session_state.etapa == 2:
    resposta2 = st.radio("Certeza certezinha?", ["Sim", "Não"], key="pergunta2")
    if resposta2 == "Sim":
        st.balloons()
        st.success("🎉 Que bom que estavas pronto!")
        st.session_state.etapa = 3
    elif resposta2 == "Não":
        st.write("Eu vi logo 😄")
        st.session_state.etapa = 3

# Etapa 3: Final
if st.session_state.etapa == 3:
    if st.button("Recomeçar"):
        st.session_state.etapa = 0
        st.experimental_rerun()
