import streamlit as st

st.set_page_config(
    page_title="SIBM - Sistema de Informação Brasileiro de Mamíferos",
    page_icon="SIBM_logo_semfundo.png",
    layout="wide"
)

# ===== OPEN GRAPH - Preview ao compartilhar link =====
st.markdown("""
    <head>
        <meta property="og:title" content="SIBM - Sistema de Informação Brasileiro de Mamíferos" />
        <meta property="og:description" content="Plataforma gratuita de consulta sobre a mastofauna no Brasil. Dados taxonômicos, distribuição geográfica e status de conservação." />
        <meta property="og:image" content="https://sistemasibm.up.railway.app/app/static/SIBM_logo_semfundo.png" />
        <meta property="og:url" content="https://www.sibm.app.br" />
        <meta property="og:type" content="website" />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="SIBM - Sistema de Informação Brasileiro de Mamíferos" />
        <meta name="twitter:description" content="Plataforma gratuita de consulta sobre a mastofauna no Brasil." />
        <meta name="twitter:image" content="https://sistemasibm.up.railway.app/app/static/SIBM_logo_semfundo.png" />
    </head>
""", unsafe_allow_html=True)

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
