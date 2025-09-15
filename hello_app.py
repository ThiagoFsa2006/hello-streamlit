import streamlit as st

# Usuários permitidos
USUARIOS = {"thiago": "1234", "admin": "admin"}

# Verifica se já está logado
if "logado" not in st.session_state:
    st.session_state.logado = False

# Tela de login
if not st.session_state.logado:
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            st.session_state.logado = True
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos.")
else:
    st.title("Meu App Web")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Clique aqui"):
            st.success("Hello World!")

