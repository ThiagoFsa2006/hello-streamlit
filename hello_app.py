import streamlit as st

# Estilo para ocupar a tela inteira e destacar o botão
st.markdown("""
    <style>
        .full-screen-box {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(255, 0, 0, 0.1);
            z-index: -1;
        }
        .custom-button {
            display: block;
            width: 100%;
            padding: 1em;
            background-color: white;
            border-left: 10px solid red;
            border-right: 10px solid red;
            font-size: 20px;
            font-weight: bold;
            color: black;
            text-align: center;
            cursor: pointer;
        }
    </style>
    <div class="full-screen-box"></div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Visualização com Botão em Tela Cheia</h1>", unsafe_allow_html=True)

# Botão estilizado
clicked = st.button("Clique aqui", key="custom")

if clicked:
    st.success("Hello World!")


