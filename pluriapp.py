import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title="Demo App", layout="centered")
st.title("🚀 CLICAAAAAA!")

# Button
if st.button("Enviar balões"):
    st.balloons()

# File upload
uploaded_file = st.file_uploader("Faça upload de um arquivo CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Visualização do CSV:")
    st.dataframe(df)
    
