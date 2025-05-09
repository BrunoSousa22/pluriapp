import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Demo App", layout="centered")
st.title("🚀 A Equipa de Marketing é a melhor!")

# Text input
name = st.text_input("Insira o seu nome:")

# Number input
idade = st.number_input("A sua idade:", min_value=0, max_value=120, step=1)

# Number input
morada = st.text_input("A sua morada:")

# Number input
cidade = st.text_input("A sua cidade:")

# Button
if st.button("Enviar balões"):
    st.balloons()

# File upload
uploaded_file = st.file_uploader("Faça upload de um arquivo CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Visualização do CSV:")
    st.dataframe(df)
    
