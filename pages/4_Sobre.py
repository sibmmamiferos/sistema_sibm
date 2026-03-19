import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from estilo import aplicar_estilo

aplicar_estilo("pages/4_Sobre.py")

# Caminho para a pasta img dentro de pages/
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")

st.markdown('<div class="main-title">Sobre o Projeto</div>', unsafe_allow_html=True)
st.markdown('<hr style="border:none;height:2px;background-color:#2D4F1E;margin:16px 0 32px 0;">', unsafe_allow_html=True)

# ===== SIBM =====
st.markdown('<div style="font-size:1.4rem;font-weight:700;color:#2D4F1E;margin-bottom:12px;">SIBM</div>', unsafe_allow_html=True)

col_logo, col_desc = st.columns([1, 3])
with col_logo:
    st.image(os.path.join(IMG_DIR, "SIBM_logo.png"), use_container_width=True)
with col_desc:
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;text-align:justify;">
            O <b>SIBM — Sistema de Informação Brasileiro de Mamíferos</b> é uma plataforma digital
            projetada para centralizar, organizar e democratizar o acesso a dados sobre a mastofauna
            no Brasil. Pautado nos princípios de livre acesso e código aberto, o sistema foi desenvolvido
            para ser uma ferramenta replicável e colaborativa para a comunidade científica e ambiental.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="font-size:15px;line-height:1.8;text-align:justify;">
        <b>No SIBM, você encontrará:</b>
        <ul style="margin-top:8px;">
            <li><b>Dados Taxonômicos:</b> Classificação atualizada das espécies.</li>
            <li><b>Distribuição Geográfica:</b> Ocorrência e limites territoriais.</li>
            <li><b>Status de Conservação:</b> Categorias de ameaça e vulnerabilidade.</li>
            <li><b>Ecologia e Metodologias:</b> Informações sobre o modo de vida das espécies e guias
            técnicos sobre os métodos de amostragem utilizados em campo.</li>
        </ul>
        <br>
        Todos os dados disponibilizados são compilados de fontes públicas, estruturados em um banco
        de dados. O SIBM incentiva a transparência: qualquer usuário pode realizar o download das
        informações e contribuir com melhorias ou atualizações para o fortalecimento da plataforma.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<hr style="border:none;height:1px;background-color:#ccc;margin:8px 0 24px 0;">', unsafe_allow_html=True)

# ===== O DESENVOLVEDOR =====
st.markdown('<div style="font-size:1.4rem;font-weight:700;color:#2D4F1E;margin-bottom:12px;">O Desenvolvedor</div>', unsafe_allow_html=True)

col_foto, col_bio = st.columns([0.7, 3])
with col_foto:
    st.image(os.path.join(IMG_DIR, "gabriel_messias.png"), use_container_width=True)
with col_bio:
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;text-align:justify;">
            <b>Gabriel Messias</b> é Bacharel em Ciências Biológicas pela Universidade Federal de Lavras (UFLA)
            e Mestre em Ciência e Tecnologia Ambiental pela Universidade Federal do ABC (UFABC).
            <br><br>
            Com atuação dedicada à mastofauna desde 2010, Gabriel desenvolveu pesquisas em diversas frentes,
            incluindo ecologia alimentar de roedores e carnívoros, efeitos da fragmentação florestal,
            bioinvasão e tricologia. Atualmente, atua como consultor ambiental especializado em mamíferos.
            <br><br>
            Sua visão para o SIBM é fundamentada na crença de que as ferramentas digitais e os dados abertos
            são os principais motores para o avanço do conhecimento científico e para a proposição de políticas
            públicas eficientes de conservação.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="font-size:15px;line-height:2.0;">
        🔗 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/gabriel-messias-moura-de-faria/" target="_blank">linkedin.com/in/gabriel-messias-moura-de-faria</a><br>
        📄 <b>Currículo Lattes:</b> <a href="https://lattes.cnpq.br/1951568529556092" target="_blank">lattes.cnpq.br/1951568529556092</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<hr style="border:none;height:1px;background-color:#ccc;margin:8px 0 24px 0;">', unsafe_allow_html=True)

# ===== COMO CITAR =====
st.markdown("### Como Citar")
st.markdown(
    """
    <div style="
        font-size:14px;
        line-height:1.8;
        background-color:white;
        border-left:4px solid #2D4F1E;
        border-radius:6px;
        padding:16px 20px;
    ">
        SIBM, Sistema de Informação Brasileiro de Mamíferos. Sistema de Informação Brasileiro de Mamíferos. 2026.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<hr style="border:none;height:1px;background-color:#ccc;margin:8px 0 24px 0;">', unsafe_allow_html=True)

# ===== CONTATO E COLABORAÇÃO =====
st.markdown("### Contato e Colaboração")
st.markdown(
    """
    <div style="font-size:15px;line-height:1.8;">
        Se você deseja contribuir com o código, sugerir novos dados ou reportar ajustes,
        utilize nossos canais oficiais:<br><br>
        📧 <b>E-mail:</b> <a href="mailto:sibm.mamiferos@gmail.com">sibm.mamiferos@gmail.com</a><br>
        🐙 <b>GitHub:</b> <a href="https://github.com/sibmmamiferos/" target="_blank">github.com/sibmmamiferos/</a>
    </div>
    """,
    unsafe_allow_html=True
)
