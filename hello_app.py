import streamlit as st

# Estilo para fundo vermelho em tela cheia
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

# Título
st.markdown("<h1 style='text-align: center;'>Área Interativa em Tela Cheia</h1>", unsafe_allow_html=True)

# Área interativa dentro do fundo vermelho
with st.container():
    st.markdown("<h3 style='text-align: center;'>Informações dentro da área vermelha</h3>", unsafe_allow_html=True)
    nome = st.text_input("Digite seu nome")
    opcao = st.selectbox("Escolha uma opção", ["Opção 1", "Opção 2", "Opção 3"])
    st.write(f"Você selecionou: {opcao}")

# Botão estilizado
clicked = st.button("Clique aqui", key="custom")
if clicked:
    st.success("Hello World!")
