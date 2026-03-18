import streamlit as st
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from estilo import aplicar_estilo

aplicar_estilo("pages/3_Banco_de_Dados.py")

@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados_sibm.csv", encoding="utf-8")
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    return df

df = carregar_dados()

st.markdown('<div class="main-title">Banco de Dados</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ===== LAYOUT EM COLUNAS =====
col_esq, col_dir = st.columns([1, 1])

with col_esq:
    st.markdown(
        f"O banco de dados contém **{len(df)} registros** de espécies de mamíferos brasileiros.",
        unsafe_allow_html=False
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        label="⬇️  Baixar banco de dados completo (CSV)",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="dados_sibm.csv",
        mime="text/csv",
        use_container_width=False
    )

with col_dir:
    st.markdown("### Baixe dados de espécies específicas")
    especies_input = st.text_input(
        label="Digite os nomes das espécies separados por **;**",
        placeholder="Ex: Panthera onca; Puma concolor; Tapirus terrestris"
    )
    if especies_input:
        lista_especies = [e.strip() for e in especies_input.split(";") if e.strip()]
        df_filtrado = df[df["binomio"].astype(str).str.lower().isin(
            [e.lower() for e in lista_especies]
        )]
        if not df_filtrado.empty:
            st.markdown(
                f'<div style="background-color:#1a3d2b; color:#4caf88; padding:10px 16px; '
                f'border-radius:6px; font-weight:500;">'
                f'✅ {len(df_filtrado)} registro(s) encontrado(s).</div>',
                unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label="⬇️  Baixar dados filtrados (CSV)",
                data=df_filtrado.to_csv(index=False).encode("utf-8"),
                file_name="dados_sibm_filtrado.csv",
                mime="text/csv",
                use_container_width=False
            )
        else:
            st.markdown(
                '<div style="background-color:#3d1a1a; color:#e57373; padding:10px 16px; '
                'border-radius:6px; font-weight:500;">'
                '⚠️ Nenhum registro encontrado. Verifique a grafia dos nomes.</div>',
                unsafe_allow_html=True
            )
