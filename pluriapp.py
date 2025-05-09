import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Surpresa", layout="centered")
st.title("Bem-vindaaaaaa 😃!")

# Initialize state
if "clicou" not in st.session_state:
    st.session_state.clicou = False

# Button
if st.button("Clica para ver a surpresa"):
    st.session_state.clicou = True

# Show radio if button was clicked
if st.session_state.clicou:
    resposta = st.radio("Tens a certeza?", ["Sim", "Não"], index=None, key="resposta_certeza")

    if resposta == "Sim":
        st.balloons()
    elif resposta == "Não":
        st.write("Tudo bem, tu é que perdes😌")
