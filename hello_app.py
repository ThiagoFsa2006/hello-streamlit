import streamlit as st

# Verifica login (opcional)
if "logado" not in st.session_state:
    st.session_state.logado = True  # Simula login para teste

if st.session_state.logado:
    st.title("Meu App Web")

    # Quadro vermelho para visualização
    st.markdown("""
        <div style="border: 2px solid red; padding: 20px; border-radius: 10px; background-color: #ffe6e6;">
            <h3 style="color: red; text-align: center;">Área para colocar informações</h3>
            <p style="text-align: center;">Você pode adicionar texto, gráficos, campos de entrada, etc.</p>
        </div>
    """, unsafe_allow_html=True)

    # Botão central
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Clique aqui"):
            st.success("Hello World!")

