import streamlit as st
from auth import verify_user
from pacientes import get_pacientes
from terapeutas import get_terapeutas
from sessoes import add_sessao

st.title("Sistema de Registro de Sessões de Terapia")

# Tela de Login
if 'user' not in st.session_state:
    st.subheader("Login")
    nome = st.text_input("Nome de Usuário")
    senha = st.text_input("Senha", type='password')

    if st.button("Entrar"):
        if verify_user(nome, senha):
            st.session_state.user = nome  # Armazena o usuário na sessão
            st.success("Login bem-sucedido!")
        else:
            st.error("Nome de usuário ou senha inválidos.")

# Tela do Usuário
if 'user' in st.session_state:
    st.subheader("Dashboard")
    # Lógica para exibir funcionalidades com base no tipo de usuário
    # Por exemplo, se for 'User Comum', mostrar apenas o registro de sessões
