import streamlit as st
import pandas as pd
# Page title
st.set_page_config(page_title="Demo App", layout="centered")
st.title("🚀 Bem-vindo!")

# Initialize session state
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
if "resposta1" not in st.session_state:
    st.session_state.resposta1 = None
if "resposta2" not in st.session_state:
    st.session_state.resposta2 = None

# Etapa 0: Botão inicial
if st.session_state.etapa == 0:
    if st.button("Clicar aqui para uma surpresa"):
        st.session_state.etapa = 1
# Etapa 1: Primeira pergunta
elif st.session_state.etapa == 1:
    st.session_state.resposta1 = st.radio(
        "Tens a certeza que estás pronto?", ["Sim", "Não"], key="pergunta1"
    )

    if st.session_state.resposta1 == "Sim":
    elif st.session_state.resposta1 == "Não":
        st.write("Nem sabes o que perdes 😢")

# Etapa 2: Segunda pergunta
elif st.session_state.etapa == 2:
    st.session_state.resposta2 = st.radio(
        "Certeza certezinha?", ["Sim", "Não"], key="pergunta2"
    )

    if st.session_state.resposta2 == "Sim":
        st.balloons()
        st.success("🎉 Que bom que estavas pronto!")
        st.session_state.etapa = 3
    elif st.session_state.resposta2 == "Não":
        st.write("Eu vi logo 😄")
        st.session_state.etapa = 3

# Etapa 3: Final
elif st.session_state.etapa == 3:
    st.write("Fim do processo.")
    if st.button("Recomeçar"):
        st.session_state.etapa = 0
        st.session_state.resposta1 = None
        st.session_state.resposta2 = None
