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
        f'<img src="data:image/png;base64,{logo_b64}" alt="SIBM" style="height:52px;object-fit:contain;vertical-align:middle;">'
        if logo_b64
        else '<span style="color:white;font-weight:700;font-size:20px;">SIBM</span>'
    )

    # Navbar responsiva com menu hamburguer no mobile
    st.markdown(f"""
    <style>
    .sibm-navbar {{
        position: fixed;
        top: 0; left: 0; right: 0;
        z-index: 99999;
        background-color: #2D4F1E;
        padding: 0 24px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.25);
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 64px;
    }}
    .sibm-logo {{ display: flex; align-items: center; }}
    .sibm-nav-links {{
        display: flex;
        gap: 4px;
        align-items: center;
    }}
    .sibm-nav-links a {{
        color: rgba(255,255,255,0.85);
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        padding: 8px 12px;
        border-radius: 6px;
        white-space: nowrap;
        transition: background 0.2s;
    }}
    .sibm-nav-links a:hover {{
        background-color: rgba(255,255,255,0.15);
        color: white;
    }}
    .sibm-hamburger {{
        display: none;
        flex-direction: column;
        cursor: pointer;
        gap: 5px;
        padding: 8px;
    }}
    .sibm-hamburger span {{
        display: block;
        width: 25px;
        height: 2px;
        background-color: white;
        border-radius: 2px;
        transition: all 0.3s;
    }}
    .sibm-mobile-menu {{
        display: none;
        position: fixed;
        top: 64px; left: 0; right: 0;
        background-color: #2D4F1E;
        z-index: 99998;
        flex-direction: column;
        padding: 8px 16px 16px 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .sibm-mobile-menu.open {{ display: flex; }}
    .sibm-mobile-menu a {{
        color: rgba(255,255,255,0.9);
        text-decoration: none;
        font-size: 15px;
        font-weight: 500;
        padding: 12px 8px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }}
    .sibm-mobile-menu a:last-child {{ border-bottom: none; }}
    .sibm-mobile-menu a:hover {{ color: white; background-color: rgba(255,255,255,0.1); border-radius: 6px; }}

    @media (max-width: 768px) {{
        .sibm-nav-links {{ display: none !important; }}
        .sibm-hamburger {{ display: flex !important; }}
    }}
    </style>

    <div class="sibm-navbar">
        <div class="sibm-logo">{logo_html}</div>
        <nav class="sibm-nav-links">
            <a href="/1_Inicio" target="_self">Início</a>
            <a href="/2_Consulta" target="_self">Consulta de Espécies</a>
            <a href="/3_Banco_de_Dados" target="_self">Banco de Dados</a>
            <a href="/5_Metodologias" target="_self">Metodologias para Estudos</a>
            <a href="/4_Sobre" target="_self">Sobre o Projeto</a>
        </nav>
        <div class="sibm-hamburger" onclick="toggleMenu()" id="hamburger">
            <span></span><span></span><span></span>
        </div>
    </div>

    <div class="sibm-mobile-menu" id="mobileMenu">
        <a href="/1_Inicio" target="_self">Início</a>
        <a href="/2_Consulta" target="_self">Consulta de Espécies</a>
        <a href="/3_Banco_de_Dados" target="_self">Banco de Dados</a>
        <a href="/5_Metodologias" target="_self">Metodologias para Estudos</a>
        <a href="/4_Sobre" target="_self">Sobre o Projeto</a>
    </div>

    <script>
    function toggleMenu() {{
        const menu = document.getElementById('mobileMenu');
        menu.classList.toggle('open');
    }}
    document.addEventListener('click', function(e) {{
        const menu = document.getElementById('mobileMenu');
        const hamburger = document.getElementById('hamburger');
        if (menu && hamburger && !menu.contains(e.target) && !hamburger.contains(e.target)) {{
            menu.classList.remove('open');
        }}
    }});
    </script>
    """, unsafe_allow_html=True)

    # Espaço entre a navbar e o conteúdo de cada página
    st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)

    # Botões invisíveis mantidos para compatibilidade com st.switch_page nas outras páginas
    for i, (titulo, caminho) in enumerate(paginas):
        if st.session_state.get(f"nav_{i}"):
            st.switch_page(caminho)
