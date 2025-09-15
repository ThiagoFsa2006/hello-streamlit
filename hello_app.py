import streamlit as st

st.markdown("<h1 style='text-align: center;'>Meu App Web</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Clique aqui"):
        st.success("Hello World!")
