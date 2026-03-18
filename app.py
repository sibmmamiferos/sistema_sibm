import streamlit as st

st.set_page_config(
    page_title="SIBM",
    page_icon="SIBM_logo_semfundo.png",
    layout="wide"
)

paginas = {
    "": [
        st.Page("pages/1_Inicio.py",          title="Início",                      icon="🏠"),
        st.Page("pages/2_Consulta.py",         title="Consulta de Espécies",        icon="🔍"),
        st.Page("pages/3_Banco_de_Dados.py",   title="Banco de Dados",              icon="📊"),
        st.Page("pages/5_Metodologias.py",     title="Metodologias para Estudos",   icon="📋"),
        st.Page("pages/4_Sobre.py",            title="Sobre o Projeto",             icon="ℹ️"),
    ]
}

nav = st.navigation(paginas, position="hidden")
nav.run()
