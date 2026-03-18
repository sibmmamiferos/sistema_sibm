import streamlit as st
import base64
import os

def _logo_base64():
    possiveis = [
        "SIBM_logo_semfundo.png",
        os.path.join(os.path.dirname(__file__), "SIBM_logo_semfundo.png"),
    ]
    for caminho in possiveis:
        if os.path.exists(caminho):
            with open(caminho, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return None


def aplicar_estilo(pagina_atual=""):

    paginas = [
        ("Início",                    "pages/1_Inicio.py"),
        ("Consulta de Espécies",      "pages/2_Consulta.py"),
        ("Banco de Dados",            "pages/3_Banco_de_Dados.py"),
        ("Metodologias para Estudos", "pages/5_Metodologias.py"),
        ("Sobre o Projeto",           "pages/4_Sobre.py"),
    ]

    # ── CSS geral (sem nenhum HTML customizado) ────────────────────────────
    st.markdown("""
<style>
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
[data-testid="stSidebar"]        { display: none; }
[data-testid="collapsedControl"] { display: none; }

:root {
    --cor-primaria:  #2D4F1E;
    --cor-secundaria:#BFA07A;
    --cor-acento:    #C36442;
    --cor-fundo:     #F4F7F5;
    --cor-texto:     #2A2D2B;
}

.stApp { background-color: var(--cor-fundo); color: var(--cor-texto); }
.block-container { padding-top: 80px !important; }

.stButton > button {
    background-color: var(--cor-primaria);
    color: white; border: none; border-radius: 8px;
}
.stDownloadButton > button {
    background-color: var(--cor-secundaria);
    color: var(--cor-texto); border: none; border-radius: 8px;
}
.stAlert { border-left: 4px solid var(--cor-acento); }
.stTabs [data-baseweb="tab"] {
    color: var(--cor-primaria);
    padding: 12px 28px !important; font-size: 15px !important;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: var(--cor-primaria); color: white !important;
    border-radius: 6px 6px 0 0; font-weight: 600;
}
.stTextInput label { color: var(--cor-texto) !important; }
.main-title    { font-size: 32px; font-weight: 600; color: var(--cor-primaria); }
.section-title { font-size: 20px; font-weight: 600; margin-top: 20px; color: var(--cor-primaria); }
.info-label    { font-weight: 600; color: var(--cor-texto); }
.card {
    padding: 20px; border-radius: 10px; background-color: white;
    border-left: 4px solid var(--cor-primaria);
}
</style>
""", unsafe_allow_html=True)

    # ── Navbar com st.columns (sem HTML customizado) ───────────────────────
    logo_b64 = _logo_base64()

    cols = st.columns([2, 1.1, 1.4, 1.2, 1.8, 1.2])

    with cols[0]:
        if logo_b64:
            st.image(f"data:image/png;base64,{logo_b64}", width=120)
        else:
            st.markdown("**SIBM**")

    for i, (titulo, caminho) in enumerate(paginas):
        with cols[i + 1]:
            if st.button(titulo, key=f"nav_{i}", use_container_width=True):
                st.switch_page(caminho)

    st.markdown("<div style='margin-top:8px'></div>", unsafe_allow_html=True)
