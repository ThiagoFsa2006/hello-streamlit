import streamlit as st

# Remove margens e ocupa a tela inteira
st.markdown("""
    <style>
        .full-screen-box {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(255, 0, 0, 0.2);
            z-index: -1;
        }
    </style>
    <div class="full-screen-box"></div>
""", unsafe_allow_html=True)

st.title("Visualização de Tela Cheia")
st.write("Esse fundo vermelho mostra a área total disponível para o app.")

