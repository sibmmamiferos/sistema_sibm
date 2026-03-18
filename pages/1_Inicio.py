import streamlit as st
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from estilo import aplicar_estilo
aplicar_estilo("pages/1_Inicio.py")

@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados_sibm.csv", encoding="utf-8")
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    return df

df = carregar_dados()

# ===== TÍTULO =====
st.markdown(
    """
    <div style="text-align:center; padding-top:30px;">
        <div style="font-size:38px;font-weight:700;color:#2D4F1E;">
            Sistema de Informação Brasileiro de Mamíferos - SIBM
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align:center; padding-top:8px; padding-bottom:4px;">
        <div style="font-size:16px;color:#444;max-width:760px;margin:0 auto;">
            O SIBM é uma plataforma gratuita de consulta integrada sobre a mastofauna no Brasil,
            reunindo informações taxonômicas, distribuição geográfica e status de conservação.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<hr style="border:none;height:2px;background-color:#2D4F1E;margin-top:10px;margin-bottom:30px;">', unsafe_allow_html=True)

# ===== MÉTRICAS =====
total_especies    = df["binomio"].nunique()
total_endemicas   = (df["endemismo"].notna() & ~df["endemismo"].isin(["-", ""])).sum() if "endemismo" in df.columns else "—"
total_vulneraveis = df[df["iucn_2025"] == "VU"]["binomio"].nunique() if "iucn_2025" in df.columns else "—"

card_style_branco = "flex:1;background-color:white;border-left:5px solid #2D4F1E;border-radius:8px;padding:22px 16px;text-align:center;box-shadow:0 2px 6px rgba(0,0,0,0.08);"
num_style_branco  = "font-size:34px;font-weight:700;color:#2D4F1E;"
lab_style_branco  = "font-size:13px;color:#555;margin-top:4px;"

metricas_html = (
    '<div style="display:flex;gap:20px;margin-bottom:6px;">'
    + '<div style="' + card_style_branco + '"><div style="' + num_style_branco + '">' + str(total_especies)     + '</div><div style="' + lab_style_branco + '">Espécies</div></div>'
    + '<div style="' + card_style_branco + '"><div style="' + num_style_branco + '">' + str(total_vulneraveis)  + '</div><div style="' + lab_style_branco + '">Espécies Vulneráveis (VU)</div></div>'
    + '<div style="' + card_style_branco + '"><div style="' + num_style_branco + '">' + str(total_endemicas)    + '</div><div style="' + lab_style_branco + '">Com Endemismo</div></div>'
    + '</div>'
)
st.markdown(metricas_html, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== CARDS POR GRUPO =====
grupos_interesse = ["Aquáticos", "Domésticos", "Exóticos", "Médio e grande porte", "Pequenos mamíferos", "Voadores"]

def count_grupo(grupo):
    if "grupo" not in df.columns:
        return "—"
    return str(df[df["grupo"] == grupo]["binomio"].nunique())

card_style_verde = "flex:1;background-color:#2D4F1E;border-radius:8px;padding:22px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);"
num_style_verde  = "font-size:30px;font-weight:700;color:white;"
lab_style_verde  = "font-size:13px;color:#A8D58A;margin-top:6px;"

def render_linha(grupos):
    html = '<div style="display:flex;gap:20px;margin-bottom:16px;">'
    for g in grupos:
        v = count_grupo(g)
        html += '<div style="' + card_style_verde + '"><div style="' + num_style_verde + '">' + v + '</div><div style="' + lab_style_verde + '">' + g + '</div></div>'
    html += '</div>'
    return html

st.markdown(render_linha(grupos_interesse[:3]), unsafe_allow_html=True)
st.markdown(render_linha(grupos_interesse[3:]), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== GALERIA DE ESPÉCIES =====
st.markdown('''
    <div style="font-size:22px;font-weight:700;color:#2D4F1E;margin-top:4px;margin-bottom:16px;text-align:center;">
        Alguns dos mamíferos presentes no Brasil
    </div>
''', unsafe_allow_html=True)

especies_galeria = [
    {"nome": "Brachyteles arachnoides","comum": "muriqui-do-sul",        "foto": "https://static.inaturalist.org/photos/377786675/medium.jpeg"},
    {"nome": "Puma concolor",          "comum": "suçuarana",             "foto": "https://inaturalist-open-data.s3.amazonaws.com/photos/9834553/medium.jpg"},
    {"nome": "Monodelphis scalops",    "comum": "catita-de-listras",     "foto": "https://inaturalist-open-data.s3.amazonaws.com/photos/65104922/medium.jpg"},
    {"nome": "Molossus rufus",         "comum": "morcego-cauda-de-rato-maior","foto": "https://static.inaturalist.org/photos/6595759/medium.png"},
    {"nome": "Stenella longirostris",  "comum": "golfinho-rotador",      "foto": "https://inaturalist-open-data.s3.amazonaws.com/photos/83099258/medium.jpg"},
    {"nome": "Cerradomys subflavus",   "comum": "rato-do-mato",          "foto": "https://inaturalist-open-data.s3.amazonaws.com/photos/581434226/medium.jpg"},
]

def render_galeria(especies):
    linha1 = especies[:3]
    linha2 = especies[3:]
    card_s = (
        "flex:1;border-radius:10px;overflow:hidden;"
        "box-shadow:0 2px 8px rgba(0,0,0,0.12);background:#fff;"
    )
    img_s   = "width:100%;height:180px;object-fit:cover;display:block;"
    info_s  = "padding:10px 12px 14px 12px;"
    nome_s  = "font-size:13px;font-style:italic;font-weight:600;color:#2D4F1E;margin:0;"
    comum_s = "font-size:12px;color:#777;margin-top:2px;"

    def linha_html(esp_list):
        h = '<div style="display:flex;gap:20px;margin-bottom:16px;">'
        for e in esp_list:
            h += (
                '<div style="' + card_s + '">'
                + '<img src="' + e["foto"] + '" style="' + img_s + '">'
                + '<div style="' + info_s + '">'
                + '<div style="' + nome_s + '">' + e["nome"] + '</div>'
                + '<div style="' + comum_s + '">' + e["comum"] + '</div>'
                + '</div></div>'
            )
        h += '</div>'
        return h

    return linha_html(linha1) + linha_html(linha2)

st.markdown(render_galeria(especies_galeria), unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ===== BOTÃO DE ACESSO RÁPIDO =====
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔍  Acessar Consulta de Espécies", use_container_width=True):
        st.switch_page("pages/2_Consulta.py")

with col2:
    if st.button("📊  Banco de Dados", use_container_width=True):
        st.switch_page("pages/3_Banco_de_Dados.py")

with col3:
    if st.button("📖  Metodologias para Estudos", use_container_width=True):
        st.switch_page("pages/5_Metodologias.py")

st.markdown("<br>", unsafe_allow_html=True)

# ===== COMO CITAR =====
st.markdown(
    """
    <div style="background-color:#f4f8f0;border-left:4px solid #2D4F1E;border-radius:6px;padding:16px 20px;max-width:860px;">
        <div style="font-size:14px;font-weight:700;color:#2D4F1E;margin-bottom:6px;">Como citar</div>
        <div style="font-size:14px;color:#333;line-height:1.7;">
            SIBM, Sistema de Informação Brasileiro de Mamíferos.
            <i>Sistema de Informação Brasileiro de Mamíferos.</i> 2026.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ===== CONTATO =====
st.markdown(
    """
    <div style="text-align:center;">
        <a href="mailto:sibm.mamiferos@gmail.com" style="text-decoration:none;">
            <div style="
                display:inline-block;
                background-color:#2D4F1E;
                color:white;
                font-size:14px;
                font-weight:600;
                padding:10px 28px;
                border-radius:6px;
                cursor:pointer;
            ">
                ✉️  Entre em contato / Relate Bugs
            </div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
