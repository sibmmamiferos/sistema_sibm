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
    st.markdown("""
    <style>
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
    [data-testid="stSidebar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }

    :root {
        --cor-primaria: #2D4F1E;
        --cor-secundaria: #BFA07A;
        --cor-acento: #C36442;
        --cor-fundo: #F4F7F5;
        --cor-texto: #2A2D2B;
    }

    .stApp { background-color: var(--cor-fundo); color: var(--cor-texto); }

    /* Empurra o conteúdo abaixo da navbar */
    .block-container { padding-top: 20px !important; }

    /* ===== NAVBAR: estiliza o primeiro stHorizontalBlock como barra fixa ===== */
    div[class*="stHorizontalBlock"]:has(button[kind="secondary"][key^="nav_"]) {
        position: fixed !important;
        top: 0 !important; left: 0 !important; right: 0 !important;
        z-index: 99999 !important;
        background-color: #2D4F1E !important;
        padding: 8px 24px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.25) !important;
        gap: 4px !important;
        min-height: 70px !important;
    }

    /* Botões dentro da navbar */
    div[class*="stHorizontalBlock"]:has(button[kind="secondary"][key^="nav_"]) button {
        background-color: transparent !important;
        color: rgba(255,255,255,0.85) !important;
        border: none !important;
        box-shadow: none !important;
        border-radius: 6px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        padding: 8px 14px !important;
        width: 100% !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    div[class*="stHorizontalBlock"]:has(button[kind="secondary"][key^="nav_"]) button:hover {
        background-color: rgba(255,255,255,0.15) !important;
        color: white !important;
    }
    div[class*="stHorizontalBlock"]:has(button[kind="secondary"][key^="nav_"]) button.active-nav {
        background-color: rgba(255,255,255,0.22) !important;
        font-weight: 700 !important;
        color: white !important;
    }

    /* Demais estilos gerais */
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
    .main-title { font-size: 32px; font-weight: 600; color: var(--cor-primaria); }
    .section-title { font-size: 20px; font-weight: 600; margin-top: 20px; color: var(--cor-primaria); }
    .info-label { font-weight: 600; color: var(--cor-texto); }
    .card {
        padding: 20px; border-radius: 10px; background-color: white;
        border-left: 4px solid var(--cor-primaria);
    }
    </style>
    """, unsafe_allow_html=True)

    paginas = [
        ("Início",                    "pages/1_Inicio.py"),
        ("Consulta de Espécies",      "pages/2_Consulta.py"),
        ("Banco de Dados",            "pages/3_Banco_de_Dados.py"),
        ("Metodologias para Estudos", "pages/5_Metodologias.py"),
        ("Sobre o Projeto",           "pages/4_Sobre.py"),
    ]

    logo_b64 = _logo_base64()
    logo_html = (
        f'<img src="data:image/png;base64,{logo_b64}" alt="SIBM" style="height:72px;object-fit:contain;vertical-align:middle;">'
        if logo_b64
        else '<span style="color:white;font-weight:700;font-size:20px;">SIBM</span>'
    )

    # Coluna do logo + uma coluna por página (largura proporcional ao texto)
    cols = st.columns([2, 1.1, 1.4, 1.2, 1.8, 1.2])

    with cols[0]:
        st.markdown(
            f'<div style="height:44px;display:flex;align-items:center;">{logo_html}</div>',
            unsafe_allow_html=True
        )

    for i, (titulo, caminho) in enumerate(paginas):
        with cols[i + 1]:
            if st.button(titulo, key=f"nav_{i}", use_container_width=True):
                st.switch_page(caminho)

    # Espaço entre a navbar e o conteúdo de cada página
    st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
