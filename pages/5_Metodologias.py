import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from estilo import aplicar_estilo
aplicar_estilo("pages/5_Metodologias.py")

# ===== TÍTULO =====
st.markdown('<div class="main-title">Metodologias para Estudos</div>', unsafe_allow_html=True)
st.markdown('<hr style="border:none;height:2px;background-color:#2D4F1E;margin-top:10px;margin-bottom:10px;">', unsafe_allow_html=True)

# ===== SUBTÍTULO / INTRODUÇÃO =====
st.markdown(
    """
    <p style="font-size:15px;line-height:1.8;color:#3A3D3B;margin-bottom:28px;">
        O monitoramento e a identificação de mamíferos baseiam-se em diferentes protocolos de campo.
        Explore as abas abaixo para conhecer as principais técnicas aplicadas no estudo deste grupo taxonômico.
    </p>
    """,
    unsafe_allow_html=True
)

# ===== NAVEGAÇÃO (RADIO HORIZONTAL) =====
st.markdown(
    """
    <style>
    div[role="radiogroup"] { display: flex; flex-wrap: wrap; gap: 8px; }
    div[role="radiogroup"] label {
        display: inline-flex !important;
        align-items: center !important;
        padding: 6px 16px !important;
        border-radius: 99px !important;
        border: 1.5px solid #4A7A34 !important;
        font-size: 14px !important;
        cursor: pointer !important;
        background-color: #4A7A34 !important;
        color: white !important;
        transition: all 0.15s !important;
    }
    div[role="radiogroup"] label:hover {
        background-color: #2D4F1E !important;
        border-color: #2D4F1E !important;
    }
    div[role="radiogroup"] label:has(input:checked) {
        background-color: #2D4F1E !important;
        border-color: #2D4F1E !important;
        font-weight: 600 !important;
    }
    div[role="radiogroup"] label p {
        color: white !important;
        margin: 0 !important;
    }
    div[role="radiogroup"] label svg { display: none !important; }
    div[role="radiogroup"] label > div:first-child { display: none !important; }
    </style>
    """,
    unsafe_allow_html=True
)

metodologia = st.radio(
    label="",
    options=[
        "Armadilhas de Captura",
        "Armadilhas de Queda",
        "Armadilhas Fotográficas",
        "Drones (UAS)",
        "Fezes",
        "Pegadas",
        "Playback",
        "Técnicas para Voadores",
        "Tricologia",
    ],
    horizontal=True,
    label_visibility="collapsed",
)

st.markdown("<hr style='border:none;height:1px;background-color:#D6DACE;margin-top:16px;margin-bottom:24px;'>", unsafe_allow_html=True)


# ================= ABA 1 — PEGADAS =================
if metodologia == "Pegadas":

    st.markdown("### Pegadas")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            A identificação de pegadas é uma das ferramentas mais práticas e eficientes para confirmar
            a presença de mamíferos em uma área. Diferente da observação direta, que depende de sorte
            e horários específicos, os rastros são registros permanentes da atividade animal.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Seção: O que as pegadas revelam ---
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                O que as pegadas revelam (Além da Espécie)
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                O rastro permite interpretar a biologia e o comportamento dos indivíduos no local:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;">
                        <strong>Composição familiar:</strong> rastros de tamanhos distintos de uma mesma
                        espécie de felino (como onça-pintada ou parda) geralmente indicam uma fêmea com
                        filhote, já que os machos dessas espécies são solitários e não participam do
                        cuidado parental.
                    </li>
                    <li>
                        <strong>Estimativa de porte e sexo:</strong> pegadas significativamente maiores e
                        mais profundas costumam indicar machos, devido ao maior peso corporal. No entanto,
                        essa análise deve ser feita com cautela, pois o tipo de solo pode mascarar o
                        tamanho real.
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Seção: Fatores que Influenciam ---
    st.markdown(
        """
        <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                    border-radius:6px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Fatores que Influenciam a Qualidade do Registro
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Nem toda pegada estará perfeita. Três fatores principais determinam o que você verá no chão:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;">
                        <strong>Condição do solo:</strong> solos muito compactos ou pedregosos dificultam
                        a impressão de detalhes (como unhas e coxins). O ideal são solos arenosos ou
                        argilosos úmidos.
                    </li>
                    <li style="margin-bottom:8px;">
                        <strong>Condição climática:</strong> o melhor momento para o registro é após chuvas
                        leves ao final do dia ou na madrugada. Isso "limpa" os rastros antigos e destaca as
                        pegadas frescas, já que a maioria dos mamíferos tem hábitos crepusculares/noturnos.
                    </li>
                    <li>
                        <strong>Modo de locomoção (Marcha):</strong> a velocidade do animal e a forma como
                        ele pisa influenciam se a pegada será completa ou se haverá sobreposição (quando a
                        pata traseira pisa em cima da marca da dianteira).
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Seção: Classificação quanto ao Tipo de Pisar ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Classificação quanto ao Tipo de Pisar
        </div>
        <div style="font-size:14.5px;line-height:1.7;color:#2A2D2B;margin-bottom:20px;">
            Para facilitar a identificação, dividimos os mamíferos em três grupos principais
            baseados em qual parte do membro toca o solo:
        </div>
        """,
        unsafe_allow_html=True
    )

    # Cards dos três grupos com imagens
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("pages/img/digitigrados.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Digitígrados
            </div>
            <div style="font-size:13.5px;line-height:1.7;color:#2A2D2B;padding:10px 4px 0 4px;">
                Apoiam apenas os dedos. Adaptados para deslocamento ágil e silencioso.<br>
                <em>Exemplos: onças, gatos-do-mato, lobo-guará e raposas.</em>
            </div>
            <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;font-style:italic;">
                Fonte: PUC-RS. Instituto do Meio Ambiente. Guia de pegadas de mamíferos. Porto Alegre: PRÓ-MATA, 2019.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.image("pages/img/plantigrados.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Plantígrados
            </div>
            <div style="font-size:13.5px;line-height:1.7;color:#2A2D2B;padding:10px 4px 0 4px;">
                Apoiam a "planta" do pé/mão inteira no chão.<br>
                <em>Exemplos: mão-pelada, tatus, tamanduás e primatas.</em>
            </div>
            <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;font-style:italic;">
                Fonte: PUC-RS. Instituto do Meio Ambiente. Guia de pegadas de mamíferos. Porto Alegre: PRÓ-MATA, 2019.
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.image("pages/img/unguligrados.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Ungulígrados
            </div>
            <div style="font-size:13.5px;line-height:1.7;color:#2A2D2B;padding:10px 4px 0 4px;">
                Apoiam-se sobre cascos (ponta da última falange).<br>
                <em>Exemplos: veados, queixadas, catetos e antas.</em>
            </div>
            <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;font-style:italic;">
                Fonte: PUC-RS. Instituto do Meio Ambiente. Guia de pegadas de mamíferos. Porto Alegre: PRÓ-MATA, 2019.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Imagem: Exemplos reais de pegadas ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Exemplos Reais de Pegadas em Campo
        </div>
        """,
        unsafe_allow_html=True
    )
    col_esp, col_img, col_esp2 = st.columns([0.5, 9, 0.5])
    with col_img:
        st.image("pages/img/pegadas_reais.png", use_container_width=True)
        st.markdown(
            """
            <div style="font-size:11px;color:#7A8C76;text-align:right;
                        font-style:italic;margin-top:4px;">
                Fonte: Acervo pessoal
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Seção: Referências / Guias de Apoio ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-top:8px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Guias de Apoio para Identificação
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                Para confirmar suas observações em campo, recomendamos as seguintes referências:
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li>
                        CARVALHO JR., O.; LUZ, N. C. <strong>Pegadas: Série Boas Práticas</strong>, v. 3.
                        Belém: EDUFPA, 2008. 64 p.
                    </li>
                    <li>
                        MORO-RIOS, R. F. et al. <strong>Manual de rastros da fauna paranaense.</strong>
                        Curitiba: Instituto Ambiental do Paraná, 2008. 70 p.
                    </li>
                    <li>
                        PONTIFÍCIA UNIVERSIDADE CATÓLICA DO RIO GRANDE DO SUL. Instituto do Meio Ambiente.
                        <strong>Guia de pegadas de mamíferos.</strong> Porto Alegre: PRÓ-MATA, 2019.
                    </li>
                    <li>
                        PRIST, P. R.; SILVA, M. X.; PAPI, B. <strong>Guia de rastros de mamíferos
                        neotropicais de médio e grande porte.</strong> Organização de Paula Ribeiro Prist.
                        São Paulo: Fólio Digital, 2020.
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 2 — FEZES =================
elif metodologia == "Fezes":

    st.markdown("### Fezes")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            O estudo das fezes é uma das formas mais práticas de saber quais animais vivem em uma área.
            Elas funcionam como uma "assinatura" do animal, revelando detalhes sobre sua alimentação e
            comportamento. Como a literatura sobre o tema é mais restrita que a de pegadas, a prática
            de campo é fundamental para aprender a diferenciá-las.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Prancha de exemplos teóricos ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Prancha de Referência
        </div>
        """,
        unsafe_allow_html=True
    )
    col_esp, col_prancha, col_esp2 = st.columns([1.5, 7, 1.5])
    with col_prancha:
        st.image("pages/img/prancha_fezes.png", use_container_width=True)
        st.markdown(
            """
            <div style="font-size:11px;color:#7A8C76;text-align:right;
                        font-style:italic;margin-top:4px;">
                Fonte: CHAME, M. Terrestrial mammal feces: a morphometric summary and description.
                Memórias do Instituto Oswaldo Cruz, v. 98, p. 71–94, 2003.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Duas colunas: Onde encontrar + Pistas na dieta ---
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown(
            """
            <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                        border-radius:4px;height:100%;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Onde encontrar e o que observar
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    Alguns ambientes são "pontos quentes" para encontrar esses vestígios:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;">
                            <strong>Áreas de grama baixa:</strong> onde há maior chance de encontrar
                            as fezes pequenas e arredondadas do tapeti.
                        </li>
                        <li style="margin-bottom:8px;">
                            <strong>Beira de rios e lagos:</strong> locais ideais para achar fezes
                            de capivaras e lontras, que vivem associadas à água.
                        </li>
                        <li>
                            <strong>Em cima de pedras ou cupinzeiros:</strong> locais altos são
                            escolhidos por canídeos, como o lobo-guará, para marcar território.
                        </li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_b:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                        border-radius:6px;height:100%;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Pistas na dieta e no cheiro
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    O conteúdo das fezes diz muito sobre quem as deixou:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;">
                            <strong>Cheiro, frutos e sementes:</strong> frutos deixam sementes e cheiro
                            característicos — como o lobo-guará, que consome muita lobeira e produz
                            fezes com cheiro forte e repletas de suas sementes.
                        </li>
                        <li style="margin-bottom:8px;">
                            <strong>Escamas e espinhas:</strong> indicam a presença de lontras ou
                            ariranhas, que se alimentam basicamente de peixes e crustáceos.
                        </li>
                        <li>
                            <strong>Pelos:</strong> comuns em fezes de felinos (onças e gatos-do-mato),
                            devido ao hábito de se lamberem constantemente.
                        </li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Importância para a Ciência ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Importância para a Ciência
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Além de identificar a espécie, as fezes permitem que pesquisadores estudem:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">A dieta detalhada do animal em diferentes épocas do ano;</li>
                    <li style="margin-bottom:6px;">A presença de parasitas e a saúde da população;</li>
                    <li style="margin-bottom:6px;">Quais plantas dependem daquele animal para se espalharem pelo ambiente;</li>
                    <li>Quais outros seres vivos estão no ambiente.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Foto de exemplos reais ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Exemplos Reais em Campo
        </div>
        """,
        unsafe_allow_html=True
    )
    col_esp3, col_real, col_esp4 = st.columns([0.5, 9, 0.5])
    with col_real:
        st.image("pages/img/fezes_reais.png", use_container_width=True)
        st.markdown(
            """
            <div style="font-size:11px;color:#7A8C76;text-align:right;
                        font-style:italic;margin-top:4px;">
                Fonte: Acervo pessoal
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Referência bibliográfica ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Guias de Apoio para Identificação
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                Para confirmar suas observações em campo, recomendamos a seguinte referência:
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li>
                        CHAME, M. <strong>Terrestrial mammal feces: a morphometric summary and
                        description.</strong> Memórias do Instituto Oswaldo Cruz, v. 98,
                        p. 71–94, 2003.
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 3 — ARMADILHAS FOTOGRÁFICAS =================
elif metodologia == "Armadilhas Fotográficas":

    st.markdown("### Armadilhas Fotográficas")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            As armadilhas fotográficas, popularmente conhecidas como <em>camera traps</em>, são dispositivos
            equipados com sensores de movimento e luz infravermelha para registros noturnos. Essa ferramenta
            permite a obtenção de dados visuais (fotos ou vídeos) de forma não intrusiva, sendo amplamente
            utilizada em levantamentos de fauna, especialmente para médios e grandes mamíferos.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- BLOCO 1: Evolução — câmera analógica vs digital ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Evolução e Componentes
        </div>
        <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;margin-bottom:16px;">
            Diferente dos modelos antigos, que eram volumosos e utilizavam filmes analógicos, os sistemas
            atuais são digitais, compactos e integrados. Para operar uma unidade, são necessários:
            <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                <li style="margin-bottom:6px;"><strong>Armazenamento:</strong> cartão SD ou microSD.</li>
                <li style="margin-bottom:6px;"><strong>Segurança:</strong> cabo de aço ou corrente com cadeado para prevenir furtos em campo.</li>
                <li><strong>Energia:</strong> conjunto de pilhas (alcalinas ou recarregáveis) ou baterias externas.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_ana, col_dig = st.columns(2)
    with col_ana:
        _, c, _ = st.columns([1.5, 7, 1.5])
        with c:
            st.image("pages/img/modelo_camera_analogico.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Modelo analógico
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: CAMTRAPPER. Discussion thread. Disponível em: camtrapper.com
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_dig:
        _, c2, _ = st.columns([1.5, 7, 1.5])
        with c2:
            st.image("pages/img/modelo_camera_digital.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Modelo digital
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Bushnell. Câmera de trilha Trophy Cam HD. Disponível em: amazon.com.br
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Protocolo + Cuidados em duas colunas ---
    col_prot, col_cuid = st.columns(2)

    with col_prot:
        st.markdown(
            """
            <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                        border-radius:4px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Protocolo de Instalação
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    A eficácia do registro depende diretamente do posicionamento do equipamento:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:6px;"><strong>Fixação:</strong> preferencialmente em troncos retos, perpendiculares ao solo, com espessura média.</li>
                        <li style="margin-bottom:6px;"><strong>Altura:</strong> padrão de 30 cm do solo; pode ser elevada para monitorar fauna arbórea, como primatas.</li>
                        <li style="margin-bottom:6px;"><strong>Localização:</strong> priorize locais com rastros, trilhas ou sinais de atividade.</li>
                        <li style="margin-bottom:6px;"><strong>Limpeza de área:</strong> pode a vegetação rasteira à frente da lente para evitar falsos disparos causados pelo vento.</li>
                        <li><strong>Iscas:</strong> podem ou não ser usadas, depende do seu objetivo.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_cuid:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                        border-radius:6px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Cuidados Ambientais
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    Apesar de serem impermeáveis, as câmeras sofrem com condições extremas:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:6px;"><strong>Umidade:</strong> em períodos chuvosos, recomenda-se o uso de sílica gel no interior da carcaça para absorver a condensação e proteger os circuitos.</li>
                        <li><strong>Exposição solar:</strong> evite que a lente fique voltada diretamente para o sol. O calor excessivo reduz a vida útil das baterias e compromete a qualidade da imagem.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- BLOCO 2: Posições de instalação ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Posições de Instalação em Campo
        </div>
        """,
        unsafe_allow_html=True
    )

    col_solo, col_sub = st.columns(2)
    with col_solo:
        _, c3, _ = st.columns([1.5, 7, 1.5])
        with c3:
            st.image("pages/img/camera_solo.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Câmera instalada a nível do solo
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Acervo pessoal
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_sub:
        _, c4, _ = st.columns([1.5, 7, 1.5])
        with c4:
            st.image("pages/img/camera_subbosque.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Câmera instalada no sub-bosque
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Acervo pessoal
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Vantagens e Desvantagens ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Vantagens e Desvantagens
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Ao planejar o uso desta tecnologia, deve-se considerar os seguintes pontos:
                <ul style="margin-top:8px;margin-bottom:8px;padding-left:20px;">
                    <li style="margin-bottom:6px;"><strong>Vantagens:</strong> alta definição de imagem (HD), facilidade de configuração, leveza e registros precisos de comportamento animal.</li>
                    <li><strong>Desvantagens:</strong> alto custo inicial (entre R$ 600,00 e R$ 3.000,00 devido à importação), risco elevado de furtos e alto consumo/descarte de pilhas.</li>
                </ul>
                <strong>Critérios para aquisição:</strong> antes de escolher uma marca (como a popular Bushnell),
                avalie a autonomia de energia, durabilidade da carcaça, facilidade de importação e capacidade de armazenamento.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- BLOCO 3: Prancha de registros ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Exemplos de Registros Fotográficos
        </div>
        """,
        unsafe_allow_html=True
    )
    col_e1, col_prancha_cam, col_e2 = st.columns([1, 8, 1])
    with col_prancha_cam:
        st.image("pages/img/prancha_camera.png", use_container_width=True)
        st.markdown(
            """
            <div style="font-size:11px;color:#7A8C76;text-align:right;
                        font-style:italic;margin-top:4px;">
                Fonte: Acervo pessoal
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Referências ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">
                        HARMSEN, B. J. et al. <strong>Differential use of trails by forest mammals and the
                        implications for camera-trap studies: a case study from Belize.</strong>
                        Biotropica, v. 42, n. 1, p. 126–133, 2010.
                    </li>
                    <li style="margin-bottom:6px;">
                        LAZARETTI, T. <strong>Métodos de Pesquisa e Levantamento de Fauna Silvestre:
                        Teoria & Prática.</strong> 2013.
                    </li>
                    <li>
                        SRBEK-ARAUJO, A. C.; CHIARELLO, A. G. <strong>Is camera-trapping an efficient
                        method for surveying mammals in Neotropical forests? A case study in south-eastern
                        Brazil.</strong> Journal of Tropical Ecology, v. 21, n. 1, p. 121–125, 2005.
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 4 — ARMADILHAS DE QUEDA =================
elif metodologia == "Armadilhas de Queda":

    st.markdown("### Armadilhas de Queda (Pitfall e Trincheira)")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            Amplamente utilizadas na mastozoologia desde os anos 2000, as armadilhas de queda são
            essenciais para amostrar espécies que raramente entram em gaiolas, como animais fossoriais
            (que vivem sob o solo) ou terrestres de pequeno porte.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Tipos e Estrutura ---
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Tipos e Estrutura
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Existem duas variações principais dependendo do grupo taxonômico visado:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;">
                        <strong>Pitfall (Baldes):</strong> utilizado para pequenos mamíferos. Consiste em
                        recipientes (20L a 100L) enterrados rente ao solo, conectados por uma cerca-guia
                        (lona ou tela) que direciona o animal para a queda.
                    </li>
                    <li>
                        <strong>Trincheira:</strong> estruturas de grandes dimensões escavadas no solo,
                        focadas em grandes mamíferos como a Anta (<em>Tapirus terrestris</em>). Exigem
                        cautela extrema devido ao risco de fraturas nos animais e à dificuldade logística
                        de resgate.
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Protocolo: tabela comparativa Pitfall x Trincheira ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Protocolo de Instalação e Disposição
        </div>
        """,
        unsafe_allow_html=True
    )

    col_pit, col_tri = st.columns(2)

    with col_pit:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:16px 20px;
                        border-radius:6px;height:100%;">
                <div style="font-size:14.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;
                            text-align:center;border-bottom:1px solid #D6DACE;padding-bottom:8px;">
                    Pitfall
                </div>
                <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                    <ul style="padding-left:18px;margin:0;">
                        <li style="margin-bottom:8px;"><strong>Preparação:</strong> os baldes devem ter furos no fundo para evitar acúmulo de água e morte por afogamento. A boca deve estar perfeitamente nivelada ao solo.</li>
                        <li style="margin-bottom:8px;"><strong>Cerca-guia:</strong> instalada com estacas de 50 cm de altura. Lonas são mais econômicas; telas de nylon são mais duráveis em locais com vento, embora algumas espécies consigam escalá-las.</li>
                        <li style="margin-bottom:8px;"><strong>Transecto (Linha):</strong> ideal para cobrir áreas maiores e aumentar a riqueza de espécies amostradas.</li>
                        <li><strong>Formato em "Y":</strong> concentra o esforço de amostragem, sendo eficaz para capturar maior abundância de indivíduos.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_tri:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:16px 20px;
                        border-radius:6px;height:100%;">
                <div style="font-size:14.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;
                            text-align:center;border-bottom:1px solid #D6DACE;padding-bottom:8px;">
                    Trincheira
                </div>
                <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                    <ul style="padding-left:18px;margin:0;">
                        <li style="margin-bottom:8px;"><strong>Preparação:</strong> escavação do solo com dimensões de 2,3 m de comprimento, 1,5 m de largura e 2,2 m de profundidade. Fundamental ser em local de passagem do animal.</li>
                        <li style="margin-bottom:8px;"><strong>Camuflagem:</strong> pode ser coberta com telhas de fibrocimento e camuflada com serapilheira e/ou terra e areia.</li>
                        <li style="margin-bottom:8px;"><strong>Contenção:</strong> o animal é manejado no interior da estrutura.</li>
                        <li><strong>Soltura:</strong> ao final, uma rampa é cavada em um dos lados para que o animal saia com segurança.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Bloco de imagens: configurações pitfall ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Configurações de Layout — Pitfall
        </div>
        """,
        unsafe_allow_html=True
    )

    col_pl, col_py = st.columns(2)
    with col_pl:
        _, c1, _ = st.columns([1.5, 7, 1.5])
        with c1:
            st.image("pages/img/pitfall_linha.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Pitfall em formato de linha
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Acervo pessoal
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_py:
        _, c2, _ = st.columns([1.5, 7, 1.5])
        with c2:
            st.image("pages/img/pitfall_y.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Pitfall em formato de Y
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Acervo pessoal
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Bloco de imagens: esquema e manejo trincheira ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Esquema e Manejo — Trincheira
        </div>
        """,
        unsafe_allow_html=True
    )

    col_et, col_mt = st.columns(2)
    with col_et:
        _, c3, _ = st.columns([1.5, 7, 1.5])
        with c3:
            st.image("pages/img/esquema_trincheira.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Construção de trincheira
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: QUSE; FERNANDES-SANTOS, 2014
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_mt:
        _, c4, _ = st.columns([1.5, 7, 1.5])
        with c4:
            st.image("pages/img/manejo_trincheira.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Manejo de animal capturado em trincheira
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: QUSE; FERNANDES-SANTOS, 2014
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Manejo e segurança + Bem-estar em duas colunas ---
    col_seg, col_bem = st.columns(2)

    with col_seg:
        st.markdown(
            """
            <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                        border-radius:4px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Manejo de Campo e Segurança (Pitfall)
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    A inspeção exige atenção redobrada devido à captura incidental de outros grupos:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Prevenção de acidentes:</strong> utilize ganchos de manejo para verificar o fundo dos baldes sob a folhagem, evitando picadas de serpentes, aranhas ou escorpiões.</li>
                        <li><strong>Manutenção:</strong> retire o acúmulo de folhas a cada revisão. Nos períodos sem amostragem, os baldes devem ser obrigatoriamente tampados para evitar mortes desnecessárias.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_bem:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                        border-radius:6px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Bem-Estar Animal (Pitfall)
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    Para reduzir a mortalidade, recomenda-se:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Abrigo:</strong> colocar folhas secas ou pedaços de isopor dentro do balde para o animal se esconder e evitar hipotermia.</li>
                        <li style="margin-bottom:8px;"><strong>Alimentação:</strong> embora iscas não aumentem a taxa de captura, podem ser usadas como "alimento de manutenção" para evitar mortes por inanição.</li>
                        <li><strong>Drenagem:</strong> monitorar rigorosamente após chuvas intensas.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Vantagens e Desvantagens ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Vantagens e Desvantagens
            </div>
            <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background-color:#2D4F1E;color:white;">
                            <th style="padding:8px 12px;text-align:left;width:15%;">Tipo</th>
                            <th style="padding:8px 12px;text-align:left;width:42.5%;">Vantagens</th>
                            <th style="padding:8px 12px;text-align:left;width:42.5%;">Desvantagens</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background-color:#F8FAF6;">
                            <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Pitfall</td>
                            <td style="padding:8px 12px;vertical-align:top;">Captura de espécies raras e fossoriais; instalação única para estudos de longo prazo; baixo custo operacional após montagem.</td>
                            <td style="padding:8px 12px;vertical-align:top;">Alta taxa de mortalidade (hipotermia, afogamento e predação); dificuldade de transporte e escavação em solos pedregosos; amostragem tendenciosa (não registra espécies arbóreas).</td>
                        </tr>
                        <tr>
                            <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Trincheira</td>
                            <td style="padding:8px 12px;vertical-align:top;">Eficiência na captura; facilidade no manejo.</td>
                            <td style="padding:8px 12px;vertical-align:top;">Tempo e custo elevados para confecção; uma vez capturado um animal, a estrutura precisa ser desfeita.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Imagem: exemplo pitfall em campo ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Exemplo de Pitfall em Campo
        </div>
        """,
        unsafe_allow_html=True
    )
    col_e1, col_epf, col_e2 = st.columns([2.5, 5, 2.5])
    with col_epf:
        st.image("pages/img/exemplo_pitfall.png", use_container_width=True)
        st.markdown(
            """
            <div style="font-size:11px;color:#7A8C76;text-align:right;
                        font-style:italic;margin-top:4px;">
                Fonte: Acervo pessoal
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Referências ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">CACERES, N. C.; NÁPOLI, R. P.; HANNIBAL, W. <strong>Differential trapping success for small mammals using pitfall and standard cage traps in a woodland savannah region of southwestern Brazil.</strong> Mammalia, v. 75, n. 1, p. 45–52, 2011.</li>
                    <li style="margin-bottom:6px;">CECHIN, S. Z.; MARTINS, M. <strong>Eficiência de armadilhas de queda (pitfall traps) em amostragens de anfíbios e répteis no Brasil.</strong> Revista Brasileira de Zoologia, v. 17, n. 3, p. 729–740, 2000.</li>
                    <li style="margin-bottom:6px;">MEDICI, E. P. <strong>Assessing the viability of lowland tapir (Tapirus terrestris) populations in a fragmented landscape.</strong> Tese (Doutorado) – University of Kent, Canterbury, 2010.</li>
                    <li style="margin-bottom:6px;">PASSAMANI, M. et al. <strong>Distribution extension of Phaenomys ferrugineus and new data on two rare rodents in Minas Gerais, Brazil.</strong> Check List, v. 7, n. 6, p. 827–831, 2011.</li>
                    <li style="margin-bottom:6px;">QUSE, V.; FERNANDES-SANTOS, R. C. (eds.). <strong>Manual de medicina veterinária de antas.</strong> 2. ed. Gland: IUCN/SSC Tapir Specialist Group, 2014. 165 p.</li>
                    <li style="margin-bottom:6px;">RIBEIRO-JÚNIOR, M. A. et al. <strong>Influence of pitfall trap size and design on herpetofauna and small mammal studies in a Neotropical Forest.</strong> Zoologia, v. 28, n. 1, 2011.</li>
                    <li style="margin-bottom:6px;">ROCHA, D. G.; PASSAMANI, M. <strong>Influence of pitfall designs and use of baits on the capture of small mammals in Southern Minas Gerais State, Brazil.</strong> Acta Scientiarum. Biological Sciences, v. 35, n. 4, p. 499–503, 2013.</li>
                    <li>UMETSU, F.; NAXARA, L.; PARDINI, R. <strong>Evaluating the efficiency of pitfall traps for sampling small mammals in the Neotropics.</strong> Journal of Mammalogy, v. 87, n. 4, p. 757–765, 2006.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 5 — ARMADILHAS DE CAPTURA =================
elif metodologia == "Armadilhas de Captura":

    st.markdown("### Armadilhas de Captura")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            As armadilhas de captura viva (gaiolas) operam por um sistema de plataforma: ao ser acionada
            pelo animal, o mecanismo de gatilho fecha a porta. Elas são ferramentas essenciais para estudos
            taxonômicos e ecológicos em ambientes neotropicais, sendo geralmente construídas em aço
            galvanizado ou alumínio.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Tabela: Tipos e Aplicações ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Tipos de Armadilhas e Aplicações
        </div>
        <div style="font-size:14px;line-height:1.8;color:#2A2D2B;margin-bottom:8px;">
            <table style="width:100%;border-collapse:collapse;">
                <thead>
                    <tr style="background-color:#2D4F1E;color:white;">
                        <th style="padding:8px 12px;text-align:left;width:18%;">Modelo</th>
                        <th style="padding:8px 12px;text-align:left;width:22%;">Indicação Principal</th>
                        <th style="padding:8px 12px;text-align:left;width:30%;">Vantagens</th>
                        <th style="padding:8px 12px;text-align:left;width:30%;">Desvantagens</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Sherman (Chapa)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Pequenos mamíferos (roedores e marsupiais).</td>
                        <td style="padding:8px 12px;vertical-align:top;">Leve, compacta e com alto bem-estar térmico. Manutenção simples.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Limpeza difícil e estrutura frágil (suscetível a danos por animais grandes).</td>
                    </tr>
                    <tr>
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Tomahawk/Young (Grade)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Médio porte e semiaquáticos (<em>Chironectes minimus</em>).</td>
                        <td style="padding:8px 12px;vertical-align:top;">Resistente, fácil limpeza e versátil para diferentes tamanhos.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Pesada, ocupa volume e exige adaptações para proteção térmica.</td>
                    </tr>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Box-trap (Ferro)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Grandes mamíferos (ex: onça-parda).</td>
                        <td style="padding:8px 12px;vertical-align:top;">Alta robustez; ideal para áreas abertas ou perímetros de criação animal.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Difícil transporte e exige logística complexa para instalação.</td>
                    </tr>
                    <tr>
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Curral (Madeira ou Ferro)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Médios e grandes mamíferos (ex: anta, capivaras, javalis).</td>
                        <td style="padding:8px 12px;vertical-align:top;">Resistente, permite a captura de vários indivíduos.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Custo e tempo para confecção; exige ceva para atrair o animal.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Bloco 1: exemplo_gaiolas + exemplo_curral ---
    col_g, col_c = st.columns(2)
    with col_g:
        _, ci1, _ = st.columns([0.5, 9, 0.5])
        with ci1:
            st.image("pages/img/exemplo_gaiolas.png", use_container_width=True)
            st.markdown(
                """
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.5;">
                    Fonte: Acervo pessoal e ALASKA MILL AND FEED. Produto disponível em loja online.
                    Disponível em: alaskamillandfeed.com
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_c:
        _, ci2, _ = st.columns([0.5, 9, 0.5])
        with ci2:
            st.image("pages/img/exemplo_curral.png", use_container_width=True)
            st.markdown(
                """
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.5;">
                    Fonte: ALMEIDA, A. Armadilha evita ataque de javaporco. Globo Rural, 2022
                    e MEDICI, 2010
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Estratégias de Instalação + Iscas em duas colunas ---
    col_est, col_isc = st.columns(2)

    with col_est:
        st.markdown(
            """
            <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                        border-radius:4px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Estratégias de Instalação por Estrato
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    A amostragem deve considerar a ocupação vertical do habitat:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Solo:</strong> exige proteção contra insolação direta, predadores e risco de inundação.</li>
                        <li style="margin-bottom:8px;"><strong>Sub-bosque (até 3m):</strong> fixação em troncos via arame ou adaptações como a armação em "V" (suporte de ripas) ou o gancho em "L" (suporte metálico acoplado ao tronco).</li>
                        <li><strong>Dossel:</strong> uso de Tomahawks sobre plataformas de madeira, elevadas por cordas e roldanas. A entrada deve ser posicionada para facilitar o acesso do animal após a subida.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_isc:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                        border-radius:6px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Atrativos e Iscas
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    A eficiência da captura varia conforme o item alimentar oferecido:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Iscas padrão:</strong> misturas de amendoim, banana, fubá e óleo de fígado de peixe.</li>
                        <li style="margin-bottom:8px;"><strong>Especificidade:</strong> marsupiais frequentemente respondem melhor a itens de origem animal, como bacon. Outras opções incluem frutas sazonais, milho, sardinha e essência de baunilha.</li>
                        <li><strong>Iscas vivas:</strong> restritas a Box-traps e obrigatoriamente vinculadas à aprovação de um Comitê de Ética.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Bloco 2: dossel imagens ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Captura no Dossel
        </div>
        """,
        unsafe_allow_html=True
    )

    col_d1, col_d2 = st.columns(2)
    with col_d1:
        _, ci3, _ = st.columns([1.5, 7, 1.5])
        with ci3:
            st.image("pages/img/gaiolas_dossel_1.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Disposição de armadilha no dossel
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Adaptado de VIEIRA, 1998
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_d2:
        _, ci4, _ = st.columns([1.5, 7, 1.5])
        with ci4:
            st.image("pages/img/gaiolas_dossel_2.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Disposição de armadilha no dossel
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Adaptado de VIEIRA, 1998
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Bem-estar animal ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Protocolo de Bem-Estar Animal
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Para minimizar o estresse e evitar mortalidade (hipotermia, predação ou ferimentos):
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Proteção térmica:</strong> cobrir parte da armadilha com plástico (proteção contra chuva/vento) e usar tapumes de madeira no fundo para isolar o frio do solo.</li>
                    <li style="margin-bottom:8px;"><strong>Manejo de campo:</strong> revisar as armadilhas nas primeiras horas do dia, garantindo que o animal não exceda 12h de contenção.</li>
                    <li style="margin-bottom:8px;"><strong>Segurança:</strong> fixar as gaiolas para evitar que predadores as desloquem.</li>
                    <li><strong>Cuidados médicos:</strong> em casos de hipotermia, utilizar bolsas de água quente. Para ferimentos leves, aplicar antissépticos (álcool iodado 7%) antes da soltura.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Bloco 3: exemplo_captura_gaiola ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Exemplos de Capturas em Campo
        </div>
        """,
        unsafe_allow_html=True
    )
    col_ec1, col_ecg, col_ec2 = st.columns([1, 8, 1])
    with col_ecg:
        st.image("pages/img/exemplo_captura_gaiola.png", use_container_width=True)
        st.markdown(
            """
            <div style="font-size:11px;color:#7A8C76;text-align:right;
                        font-style:italic;margin-top:4px;">
                Fonte: Acervo pessoal
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Referências ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">ASTÚA, D. et al. <strong>Influence of baits, trap type and position for small mammal capture in a Brazilian lowland Atlantic Forest.</strong> Boletim do Museu de Biologia Mello Leitão, v. 19, n. 1, p. 31–44, 2006.</li>
                    <li style="margin-bottom:6px;">KUHNEN, V. V.; SETZ, E. Z. F. <strong>Bem-estar de pequenos mamíferos capturados em armadilhas de grade.</strong> Bol. Soc. Bras. Mastozool., v. 75, p. 1–7, 2016.</li>
                    <li style="margin-bottom:6px;">LAZARETTI, T. <strong>Métodos de Pesquisa e Levantamento de Fauna Silvestre: Teoria & Prática.</strong> 2013.</li>
                    <li style="margin-bottom:6px;">MEDICI, E. P. <strong>Assessing the viability of lowland tapir (Tapirus terrestris) populations in a fragmented landscape.</strong> Tese (Doutorado) – University of Kent, Canterbury, 2010.</li>
                    <li style="margin-bottom:6px;">NICOLAS, V.; COLYN, M. <strong>Relative efficiency of three types of small mammal traps in an African rainforest.</strong> Belgian Journal of Zoology, v. 136, n. 1, p. 107, 2006.</li>
                    <li style="margin-bottom:6px;">SCHITTINI, G.; OLIVEIRA, L. C.; FERNANDEZ, F. A. S. <strong>Influência de diferentes tipos e posições de armadilhas na caracterização de comunidades de pequenos mamíferos em fragmentos de Mata Atlântica.</strong> Bios, v. 10, n. 10, p. 55–62, 2002.</li>
                    <li>VIEIRA, E. M. <strong>A technique for trapping small mammals in the forest canopy.</strong> Mammalia, v. 62, n. 2, p. 306–310, 1998.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 6 — TRICOLOGIA =================
elif metodologia == "Tricologia":

    st.markdown("### Tricologia")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            A tricologia é o estudo das microestruturas dos pelos para a identificação taxonômica.
            Iniciada por Hausman (1920), a técnica é amplamente aplicada na ecologia, ciência forense
            e paleontologia devido ao seu baixo custo e alto potencial de diagnóstico.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Imagem 1: estrutura do pelo ---

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Anatomia do Pelo ---
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Anatomia do Pelo e Unidade Amostral
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                O pelo é um anexo epidérmico queratinizado composto por três camadas: cutícula (escamas
                externas), córtex e medula (canal central).
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;">
                        <strong>Tipos de pelos:</strong> subpelos (curtos e ondulados) e pelos-guarda
                        (longos e sem constrições). Os pelos-guarda são os ideais para identificação,
                        pois mantêm características constantes na espécie.
                    </li>
                    <li>
                        <strong>Coleta:</strong> as amostras devem ser retiradas preferencialmente da
                        região interescapular (dorso), onde a variação individual é menor.
                    </li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col_e1, col_ep, col_e2 = st.columns([3.1, 3.8, 3.1])
    with col_ep:
        st.image("pages/img/estrutura_pelo.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Estrutura do pelo
            </div>
            <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                        margin-top:4px;line-height:1.4;">
                Fonte: SANTOS, V. S. Pelo humano. Brasil Escola. Disponível em: brasilescola.uol.com.br
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Protocolos de Preparação de Lâminas
        </div>
        """,
        unsafe_allow_html=True
    )

    col_cut, col_med = st.columns(2)

    with col_cut:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:16px 20px;
                        border-radius:6px;height:100%;">
                <div style="font-size:14.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;
                            text-align:center;border-bottom:1px solid #D6DACE;padding-bottom:8px;">
                    A. Impressão Cuticular (Padrão de Escamas)
                </div>
                <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                    <ul style="padding-left:18px;margin:0;">
                        <li style="margin-bottom:6px;"><strong>Limpeza:</strong> lavar os pelos em álcool 92% e secar.</li>
                        <li style="margin-bottom:6px;"><strong>Camada base:</strong> aplicar esmalte incolor na lâmina e aguardar ~10 min até ficar "mordente".</li>
                        <li style="margin-bottom:6px;"><strong>Prensagem:</strong> posicionar os pelos e prensar em torno por 30 minutos.</li>
                        <li><strong>Finalização:</strong> remover os pelos manualmente; a impressão das escamas ficará gravada no esmalte.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_med:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:16px 20px;
                        border-radius:6px;height:100%;">
                <div style="font-size:14.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;
                            text-align:center;border-bottom:1px solid #D6DACE;padding-bottom:8px;">
                    B. Observação de Medula (Estrutura Interna)
                </div>
                <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                    <ul style="padding-left:18px;margin:0;">
                        <li style="margin-bottom:6px;"><strong>Clareamento:</strong> lavar o pelo em álcool e imergir em água oxigenada 30 vol. por ~80 minutos (varia com a espessura do pelo).</li>
                        <li style="margin-bottom:6px;"><strong>Lavagem:</strong> enxaguar em água para interromper a oxidação.</li>
                        <li><strong>Montagem:</strong> fixar o pelo na lâmina com lamínula, vedando as bordas com esmalte incolor para criar uma lâmina semipermanente.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Bloco 2: padrão cuticular + medular ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Padrões de Referência
        </div>
        """,
        unsafe_allow_html=True
    )

    col_pc, col_pm = st.columns(2)
    with col_pc:
        _, ci1, _ = st.columns([0.5, 9, 0.5])
        with ci1:
            st.image("pages/img/padrao_cuticular.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Exemplos de padrões cuticulares
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Quadros & Monteiro-Filho (2006b)
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_pm:
        _, ci2, _ = st.columns([0.5, 9, 0.5])
        with ci2:
            st.image("pages/img/padrao_medular.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Exemplos de padrões medulares
                </div>
                <div style="font-size:11px;color:#7A8C76;text-align:center;font-style:italic;
                            margin-top:4px;line-height:1.4;">
                    Fonte: Quadros & Monteiro-Filho (2006b)
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Análise e Critérios Diagnósticos ---
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Análise e Critérios Diagnósticos
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                A identificação é feita via microscopia óptica, observando-se:
                <ul style="margin-top:8px;margin-bottom:8px;padding-left:20px;">
                    <li style="margin-bottom:6px;"><strong>Na haste (cutícula):</strong> forma, orientação, tamanho e ornamentação das bordas das escamas.</li>
                    <li><strong>No escudo (medula):</strong> continuidade, forma e disposição das células, e número de fileiras celulares.</li>
                </ul>
                <strong>Nota técnica:</strong> grupos como Tayassuidae (catetos/queixadas) e Suidae (porcos)
                apresentam cutículas de difícil impressão, exigindo maior precisão no tempo de secagem do esmalte.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Bloco 3: pranchas cuticular + medular ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Pranchas de Identificação
        </div>
        """,
        unsafe_allow_html=True
    )

    col_prc, col_prm = st.columns(2)
    with col_prc:
        _, ci3, _ = st.columns([0.5, 9, 0.5])
        with ci3:
            st.image("pages/img/prancha_cuticular.png", use_container_width=True)
            st.markdown(
                """
                <div style="font-size:11px;color:#7A8C76;text-align:center;
                            font-style:italic;margin-top:4px;">
                    Fonte: Miranda et al. (2014)
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_prm:
        _, ci4, _ = st.columns([0.5, 9, 0.5])
        with ci4:
            st.image("pages/img/prancha_medular.png", use_container_width=True)
            st.markdown(
                """
                <div style="font-size:11px;color:#7A8C76;text-align:center;
                            font-style:italic;margin-top:4px;">
                    Fonte: Miranda et al. (2014)
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Vantagens e Limitações ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Vantagens e Limitações
            </div>
            <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                <table style="width:100%;border-collapse:collapse;">
                    <thead>
                        <tr style="background-color:#2D4F1E;color:white;">
                            <th style="padding:8px 12px;text-align:left;width:50%;">Vantagens</th>
                            <th style="padding:8px 12px;text-align:left;width:50%;">Limitações</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="background-color:#F8FAF6;">
                            <td style="padding:8px 12px;vertical-align:top;"><strong>Baixo custo:</strong> requer materiais simples e acessíveis.</td>
                            <td style="padding:8px 12px;vertical-align:top;"><strong>Equipamento:</strong> necessidade de microscópio óptico de boa qualidade.</td>
                        </tr>
                        <tr>
                            <td style="padding:8px 12px;vertical-align:top;"><strong>Eficiência:</strong> identifica espécies a partir de fezes, regurgitos ou vestígios ambientais.</td>
                            <td style="padding:8px 12px;vertical-align:top;"><strong>Proximidade genética:</strong> dificuldade em diferenciar espécies ou gêneros muito próximos (ex: alguns roedores da tribo Akodontini).</td>
                        </tr>
                        <tr style="background-color:#F8FAF6;">
                            <td style="padding:8px 12px;vertical-align:top;"><strong>Praticidade:</strong> preparação rápida após padronização dos tempos.</td>
                            <td style="padding:8px 12px;vertical-align:top;"><strong>Refinamento:</strong> em casos complexos, a análise de medula é mais precisa que a cuticular.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Recomendações ---
    st.markdown(
        """
        <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                    border-radius:6px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Recomendações de Campo e Laboratório
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                <ul style="margin-top:4px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Limpeza rigorosa:</strong> amostras de fezes exigem limpeza profunda para não mascarar as escamas.</li>
                    <li style="margin-bottom:8px;"><strong>Padronização:</strong> a qualidade do esmalte e a concentração da água oxigenada variam entre marcas; faça testes prévios antes de processar amostras definitivas.</li>
                    <li><strong>Literatura de referência:</strong> utilize guias clássicos como Quadros e Monteiro-Filho (2006) e Miranda et al. (2014) para a classificação dos padrões.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Referências ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">CHERNOVA, O. F. <strong>Architectonics of the Medulla of Guard Hair and Its Importance for Identification of Taxa.</strong> Doklady Biological Sciences, v. 376, n. 4, 2001.</li>
                    <li style="margin-bottom:6px;">FARIA, G. M. M.; PUERTAS, F.; PASSAMANI, M. <strong>Evaluation of the use of trichology in identification and differentiation of eight species of the Tribe Akodontini.</strong> Bol. Soc. Bras. Mastozool., v. 79, n. 40–43, 2017.</li>
                    <li style="margin-bottom:6px;">FERNANDES, M. A. W. <strong>Análise Comparativa da Morfologia dos Pêlos-Guarda de Mamíferos com Hábito Semi-Aquático.</strong> Monografia – UFPR, Curitiba, 2008.</li>
                    <li style="margin-bottom:6px;">INGBERMAN, B.; MONTEIRO-FILHO, E. L. A. <strong>Identificação microscópica dos pêlos das espécies brasileiras de Alouatta.</strong> Arquivos do Museu Nacional, v. 64, n. 1, p. 61–71, 2006.</li>
                    <li style="margin-bottom:6px;">MARTIN, P. S.; GHELER-COSTA, C.; VERDADE, L. M. <strong>Microestruturas de pêlos de pequenos mamíferos não-voadores.</strong> Biota Neotropica, v. 9, n. 1, p. 232–241, 2009.</li>
                    <li style="margin-bottom:6px;">MARTINS, I. A. <strong>Identificação dos Canídeos Brasileiros através dos seus Pêlos Guarda.</strong> Monografia – UNESP, Assis, 2005.</li>
                    <li style="margin-bottom:6px;">MIRANDA, G. H. B.; RODRIGUES, F. H. G.; PAGLIA, A. P. <strong>Guia de identificação de pelos de mamíferos brasileiros.</strong> Brasília: Ciências Forenses, 2014.</li>
                    <li style="margin-bottom:6px;">QUADROS, J. <strong>Identificação Microscópica de Pêlos de Mamíferos Brasileiros e sua Aplicação no Estudo da Dieta de Carnívoros.</strong> Tese (Doutorado) – UFPR, Curitiba, 2002.</li>
                    <li style="margin-bottom:6px;">QUADROS, J.; MONTEIRO-FILHO, E. L. A. <strong>Collecting and preparing mammal hairs for identification with optical microscopy.</strong> Revista Brasileira de Zoologia, v. 23, n. 1, p. 274–278, 2006a.</li>
                    <li style="margin-bottom:6px;">______. <strong>Review of concepts, microstructural patterns and nomenclature proposal to the guard-hairs of Brazilian mammals.</strong> Revista Brasileira de Zoologia, v. 23, n. 1, p. 279–292, 2006b.</li>
                    <li style="margin-bottom:6px;">SILVEIRA, F. et al. <strong>Proposta de utilização da microestrutura de pelos-guarda para fins de estudos forenses e no controle de qualidade de alimentos.</strong> Revista Brasileira de Criminalística, v. 2, n. 1, p. 32–41, 2013.</li>
                    <li style="margin-bottom:6px;">SILVEIRA, F.; SBALQUEIRO, I. J.; MONTEIRO-FILHO, E. L. A. <strong>Identificação das espécies brasileiras de Akodon através da microestrutura dos pelos.</strong> Biota Neotropica, v. 13, n. 1, 2013.</li>
                    <li style="margin-bottom:6px;">TEERINK, B. J. <strong>Hair of West European Mammals: atlas and identification.</strong> Cambridge University Press, 1991.</li>
                    <li>VANSTREELS, R. E. T.; RAMALHO, F. P.; ADANIA, C. H. <strong>Microestrutura de pêlos-guarda de felídeos brasileiros.</strong> Biota Neotropica, v. 10, n. 1, 2010.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 7 — PLAYBACK =================
elif metodologia == "Playback":

    st.markdown("### Playback")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            O playback consiste na reprodução de estímulos sonoros gravados para induzir respostas em
            animais silvestres. Embora consagrada no estudo de aves e anuros, a técnica tem se mostrado
            uma ferramenta poderosa na mastozoologia para detectar espécies esquivas, mapear territórios
            e compreender interações sociais.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Objetivos + Protocolo em duas colunas ---
    col_obj, col_prot = st.columns(2)

    with col_obj:
        st.markdown(
            """
            <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                        border-radius:4px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Objetivos e Aplicações
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    A técnica pode ser aplicada com diferentes finalidades:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Censos e inventários:</strong> confirmar a presença ou ausência de espécies com baixa taxa de avistamento.</li>
                        <li style="margin-bottom:8px;"><strong>Estudos comportamentais:</strong> analisar a reação de indivíduos a vocalizações de parceiros, competidores ou predadores.</li>
                        <li><strong>Comunicação interespecífica:</strong> investigar como diferentes espécies interpretam alertas sonoros umas das outras.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_prot:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                        border-radius:6px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Protocolo de Campo
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    <ul style="margin-top:4px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Localização dos pontos:</strong> selecionar locais com boa cobertura vegetal para ocultar o observador e o equipamento. Primatas podem ignorar o estímulo se perceberem a origem artificial do som.</li>
                        <li style="margin-bottom:8px;"><strong>Execução:</strong> reproduzir o áudio e alternar com períodos de silêncio absoluto para monitorar respostas. Não reproduzir repetidamente para evitar estresse do animal.</li>
                        <li><strong>Equipamento:</strong> uma caixa de som portátil e smartphone são suficientes para estudos básicos; levantamentos rigorosos exigem gravadores de alta fidelidade e microfones direcionais.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Evidências Científicas ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Evidências Científicas e Estudos de Caso
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                <ul style="margin-top:4px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Canídeos:</strong> Ferreira et al. (2019) validaram a eficácia do playback para o monitoramento de lobo-guará (<em>Chrysocyon brachyurus</em>), facilitando o registro em áreas de campo aberto.</li>
                    <li style="margin-bottom:8px;"><strong>Relação predador-presa:</strong> Weterings et al. (2022) observaram como cervídeos e suídeos alteram seu comportamento de forrageamento ao ouvirem vocalizações de predadores.</li>
                    <li><strong>Complexidade social:</strong> Deecke (2006) revisou como o playback revelou mecanismos de aprendizado vocal e sinais de alerta específicos entre diferentes táxons.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Vantagens e Desvantagens ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Vantagens e Desvantagens
        </div>
        <div style="font-size:14px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            <table style="width:100%;border-collapse:collapse;">
                <thead>
                    <tr style="background-color:#2D4F1E;color:white;">
                        <th style="padding:8px 12px;text-align:left;width:50%;">Vantagens</th>
                        <th style="padding:8px 12px;text-align:left;width:50%;">Desvantagens</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Baixo custo:</strong> acessível com equipamentos simples de reprodução.</td>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Habituação:</strong> o uso repetitivo pode fazer com que o animal pare de responder ao estímulo.</td>
                    </tr>
                    <tr>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Praticidade:</strong> permite cobrir grandes áreas em inventários rápidos.</td>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Subjetividade:</strong> algumas respostas comportamentais são ambíguas e difíceis de interpretar.</td>
                    </tr>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Dados em tempo real:</strong> respostas imediatas que confirmam a ocupação da área.</td>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Exigência de conhecimento:</strong> demanda domínio prévio sobre o repertório vocal e a etologia da espécie.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Fontes de Referência (texto) ---
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Fontes de Referência
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Para obter estímulos sonoros de alta qualidade, recomendam-se as seguintes bibliotecas:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;"><strong>Sounds of Neotropical Rainforest Mammals:</strong> An Audio Field Guide (Emmons et al.) — o melhor no contexto brasileiro.</li>
                    <li><strong>Plataformas colaborativas de bioacústica</strong> (como o Xeno-canto para aves, que por vezes inclui mamíferos).</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Exemplos de Áudio ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:16px;">
            Exemplos de Vocalização
        </div>
        """,
        unsafe_allow_html=True
    )

    # Linha 1
    col_a1, col_a2 = st.columns(2)

    with col_a1:
        st.audio("pages/audio/callithrix_penicillata.mp3")
        st.markdown(
            """
            <div style="font-size:12px;color:#2A2D2B;margin-top:4px;">
                <em>Callithrix penicillata</em> — Sagui-de-tufos-pretos<br>
                <span style="font-size:11px;color:#7A8C76;font-style:italic;">Fonte: Xeno-canto</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_a2:
        st.audio("pages/audio/cerdocyon_thous.mp3")
        st.markdown(
            """
            <div style="font-size:12px;color:#2A2D2B;margin-top:4px;">
                <em>Cerdocyon thous</em> — Cachorro-do-mato<br>
                <span style="font-size:11px;color:#7A8C76;font-style:italic;">Fonte: Xeno-canto</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)

    # Linha 2
    col_a3, col_a4 = st.columns(2)

    with col_a3:
        st.audio("pages/audio/dicotyles_tajacu.mp3")
        st.markdown(
            """
            <div style="font-size:12px;color:#2A2D2B;margin-top:4px;">
                <em>Dicotyles tajacu</em> — Cateto<br>
                <span style="font-size:11px;color:#7A8C76;font-style:italic;">Fonte: Emmons (1998)</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_a4:
        st.audio("pages/audio/inea_geoffrensis.mp3")
        st.markdown(
            """
            <div style="font-size:12px;color:#2A2D2B;margin-top:4px;">
                <em>Inia geoffrensis</em> — Boto-cor-de-rosa<br>
                <span style="font-size:11px;color:#7A8C76;font-style:italic;">Fonte: Emmons (1998)</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:16px;'></div>", unsafe_allow_html=True)

    # Linha 3
    col_a5, col_a6 = st.columns(2)

    with col_a5:
        st.audio("pages/audio/kannabateomys_amblyonyx.mp3")
        st.markdown(
            """
            <div style="font-size:12px;color:#2A2D2B;margin-top:4px;">
                <em>Kannabateomys amblyonyx</em> — Rato-do-bambu<br>
                <span style="font-size:11px;color:#7A8C76;font-style:italic;">Fonte: Xeno-canto</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_a6:
        st.audio("pages/audio/sapajus_nigritus.mp3")
        st.markdown(
            """
            <div style="font-size:12px;color:#2A2D2B;margin-top:4px;">
                <em>Sapajus nigritus</em> — Macaco-prego-preto<br>
                <span style="font-size:11px;color:#7A8C76;font-style:italic;">Fonte: Xeno-canto</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Referências ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">CASADO, J. O. et al. <strong>An experience to remember: lifelong effects of playback-based trapping on behaviour of a migratory passerine bird.</strong> Animal Behaviour, v. 182, p. 19–29, 2021.</li>
                    <li style="margin-bottom:6px;">DEECKE, V. B. <strong>Studying marine mammal cognition in the wild: a review of four decades of playback experiments.</strong> Aquatic Mammals, v. 32, n. 4, p. 461–482, 2006.</li>
                    <li style="margin-bottom:6px;">EMMONS, L. H.; WHITNEY, B. M.; ROSS JR., D. L. <strong>Sounds of Neotropical rainforest mammals: an audio field guide.</strong> Ithaca: Cornell Laboratory of Ornithology, 1998.</li>
                    <li style="margin-bottom:6px;">FERREIRA, L. S. et al. <strong>Using playbacks to monitor and investigate the behaviour of wild maned wolves.</strong> Bioacoustics, v. 30, n. 1, p. 74–92, 2021.</li>
                    <li style="margin-bottom:6px;">FISCHER, J.; NOSER, R.; HAMMERSCHMIDT, K. <strong>Bioacoustic field research: a primer to acoustic analyses and playback experiments with primates.</strong> American Journal of Primatology, v. 75, n. 7, p. 643–663, 2013.</li>
                    <li style="margin-bottom:6px;">FISCHER, J.; HAMMERSCHMIDT, K. <strong>You talkin' to me? Interactive playback is a powerful yet underused tool in animal communication research.</strong> Biology Letters, v. 11, n. 7, 2015.</li>
                    <li>XENO-CANTO FOUNDATION FOR NATURE SOUNDS. <strong>Xeno-canto: sharing bird sounds from around the world.</strong> Disponível em: xeno-canto.org</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 8 — TÉCNICAS PARA VOADORES =================
elif metodologia == "Técnicas para Voadores":

    st.markdown("### Técnicas para Voadores")

    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:28px;">
            O estudo de morcegos exige uma combinação de métodos complementares. Nenhuma técnica sozinho
            amostra 100% da comunidade — por isso, abordagens acústicas e de captura física são utilizadas
            de forma integrada.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---- TEMA 1: BIOACÚSTICA ----
    st.markdown(
        """
        <div style="font-size:18px;font-weight:700;color:#2D4F1E;border-bottom:2px solid #2D4F1E;
                    padding-bottom:6px;margin-bottom:16px;">
            Bioacústica
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:16px;">
            A bioacústica é uma técnica não invasiva baseada na ecolocalização ultrassônica emitida pelos
            morcegos. Como cada espécie possui assinaturas sonoras específicas (frequência, duração e forma
            do pulso), é possível identificá-las sem a necessidade de captura física.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Equipamentos e Processamento
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:20px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Equipamentos e Processamento
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                <ul style="margin-top:4px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Gravadores:</strong> utilizam microfones ultrassônicos. O AudioMoth é uma opção de baixo custo e alta eficiência para inventários.</li>
                    <li style="margin-bottom:8px;"><strong>Análise de dados:</strong> as gravações são convertidas em espectrogramas (visualização gráfica do som).</li>
                    <li><strong>Identificação automatizada:</strong> softwares com machine learning aceleram a triagem, mas a revisão manual por especialistas é indispensável para evitar falsos positivos entre espécies com pulsos similares.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Bloco de imagens: audiomoth + espectrograma
    col_am, col_esp = st.columns(2)
    with col_am:
        _, ci1, _ = st.columns([3.075, 3.85, 3.075])
        with ci1:
            st.image("pages/img/audiomoth.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Aparelho AudioMoth
                </div>
                <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;
                            font-style:italic;text-align:center;">
                    Fonte: OPEN ACOUSTIC DEVICES. AudioMoth.
                    Disponível em: openacousticdevices.info/audiomoth
                </div>
                """,
                unsafe_allow_html=True
            )
    with col_esp:
        _, ci2, _ = st.columns([0.5, 9, 0.5])
        with ci2:
            st.image("pages/img/espectrograma.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Exemplo de espectrograma
                </div>
                <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;
                            font-style:italic;text-align:center;">
                    Fonte: Xeno-canto
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

    # Protocolo de Instalação + Vantagens e Limitações
    col_prot, col_vant = st.columns(2)

    with col_prot:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:16px 20px;
                        border-radius:6px;height:100%;">
                <div style="font-size:15px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Protocolo de Instalação
                </div>
                <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                    <ul style="padding-left:18px;margin:0;">
                        <li style="margin-bottom:8px;"><strong>Posicionamento:</strong> os gravadores devem ser instalados em áreas abertas ou "corredores" de voo. Vegetação densa atua como barreira física e sonora, causando atenuação do som e perda de qualidade no registro.</li>
                        <li><strong>Bibliotecas de referência:</strong> o sucesso da técnica depende de catálogos de áudios locais para comparação e treinamento de algoritmos (machine learning).</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_vant:
        st.markdown(
            """
            <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:16px 20px;
                        border-radius:6px;height:100%;">
                <div style="font-size:15px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Vantagens e Limitações
                </div>
                <div style="font-size:14px;line-height:1.8;color:#2A2D2B;">
                    <ul style="padding-left:18px;margin:0;">
                        <li style="margin-bottom:8px;"><strong>Vantagens:</strong> monitoramento contínuo e automatizado; detecção de espécies que voam alto (dossel) e que evitam redes.</li>
                        <li><strong>Desvantagens:</strong> detecção desigual (espécies com "grito baixo" são difíceis de captar); interferência ambiental (vento, chuva e eco).</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # ---- TEMA 2: REDES DE NEBLINA, HARPA E REDE MÓVEL ----
    st.markdown(
        """
        <div style="font-size:18px;font-weight:700;color:#2D4F1E;border-bottom:2px solid #2D4F1E;
                    padding-bottom:6px;margin-bottom:16px;">
            Redes de Neblina, Harpa e Rede Móvel
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:16px;">
            Para estudos que exigem biometria, coleta de tecido ou identificação taxonômica refinada,
            utiliza-se a captura física.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Tabela dos métodos
    st.markdown(
        """
        <div style="font-size:14px;line-height:1.8;color:#2A2D2B;margin-bottom:20px;">
            <table style="width:100%;border-collapse:collapse;">
                <thead>
                    <tr style="background-color:#2D4F1E;color:white;">
                        <th style="padding:8px 12px;text-align:left;width:22%;">Método</th>
                        <th style="padding:8px 12px;text-align:left;width:39%;">Funcionamento</th>
                        <th style="padding:8px 12px;text-align:left;width:39%;">Aplicação Ideal</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Rede de Neblina (Mist Nets)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Redes de nylon finas estendidas entre mastros.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Sub-bosque e corredores de mata.</td>
                    </tr>
                    <tr>
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Harpa (Harp Trap)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Estrutura com fios de nylon verticais e uma bolsa coletora na base.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Entradas de cavernas, bueiros ou saídas de colônias.</td>
                    </tr>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;font-weight:600;vertical-align:top;">Rede Móvel (Puçá)</td>
                        <td style="padding:8px 12px;vertical-align:top;">Rede acoplada a bastões manejada manualmente pelo pesquisador.</td>
                        <td style="padding:8px 12px;vertical-align:top;">Captura direcionada em locais de baixa abundância ou busca por espécies raras.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Bloco de imagens: rede_neblina, harp_trap, armadilha_movel
    col_rn, col_ht, col_am2 = st.columns(3)

    with col_rn:
        st.image("pages/img/rede_neblina.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Rede de Neblina (Mist Nets)
            </div>
            <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;
                        font-style:italic;text-align:center;">
                Fonte: Borissenko & Kruskop (2003)
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_ht:
        st.image("pages/img/harp_trap.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Harpa (Harp Trap)
            </div>
            <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;
                        font-style:italic;text-align:center;">
                Fonte: Borissenko & Kruskop (2003)
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_am2:
        st.image("pages/img/armadilha_movel.png", use_container_width=True)
        st.markdown(
            """
            <div style="background-color:#2D4F1E;color:white;text-align:center;
                        padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                        margin-top:-8px;">
                Rede Móvel (Puçá)
            </div>
            <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;
                        font-style:italic;text-align:center;">
                Fonte: Borissenko & Kruskop (2003)
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # Considerações Técnicas
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Considerações Técnicas
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                <ul style="margin-top:4px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Seletividade:</strong> redes de neblina são eficientes, mas morcegos com ecolocalização sofisticada (como os insetívoros de voo rápido) podem detectá-las e evitá-las após a primeira exposição.</li>
                    <li style="margin-bottom:8px;"><strong>Manejo na harpa:</strong> embora evite que o animal se enrosque, a captura de muitos indivíduos simultâneos na bolsa exige agilidade para evitar estresse excessivo ou agressividade entre os espécimes.</li>
                    <li><strong>Catação manual:</strong> técnica restrita a abrigos diurnos (troncos ocos, folhagens), exigindo extremo cuidado com o bem-estar animal e segurança do pesquisador (uso de luvas de raspa).</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Vídeo YouTube
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
            Exemplo prático
        </div>
        """,
        unsafe_allow_html=True
    )
    col_ve1, col_vid, col_ve2 = st.columns([0.5, 9, 0.5])
    with col_vid:
        st.video("https://youtu.be/uzhLJyKjCww")

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # Resumo das Metodologias Complementares
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Resumo das Metodologias Complementares
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Nenhum método sozinho amostra 100% da comunidade de morcegos. O ideal é combinar:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;"><strong>Redes de neblina</strong> — para capturar espécies que voam baixo;</li>
                    <li style="margin-bottom:6px;"><strong>Bioacústica</strong> — para registrar espécies de voo alto e insetívoros ariscos;</li>
                    <li><strong>Busca em abrigos</strong> — para encontrar colônias e espécies especialistas.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Referências
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">BORISSENKO, A. V.; KRUSKOP, S. V. <strong>Bats of Vietnam and adjacent territories: an identification manual.</strong> Moscow; Hanoi: Joint Russian-Vietnamese Science and Technological Tropical Centre, 2003.</li>
                    <li style="margin-bottom:6px;">CARVALHO, F.; FABIÁN, M. E. <strong>Método de elevação de redes de neblina em dosséis florestais para amostragem de morcegos.</strong> Chiroptera Neotropical, v. 17, n. 1, p. 895–902, 2011.</li>
                    <li style="margin-bottom:6px;">FERREIRA, D. F. et al. <strong>Are bat mist nets ideal for capturing bats? From ultrathin to bird nets, a field test.</strong> Journal of Mammalogy, v. 102, n. 6, p. 1627–1634, 2021.</li>
                    <li style="margin-bottom:6px;">FRASER, E. E. et al. (eds.). <strong>Bat echolocation research: a handbook for planning and conducting acoustic studies.</strong> 2. ed. Austin: Bat Conservation International, 2020.</li>
                    <li style="margin-bottom:6px;">LARSEN, R. J. et al. <strong>Mist netting bias, species accumulation curves, and the rediscovery of two bats on Montserrat.</strong> Acta Chiropterologica, v. 9, n. 2, p. 423–435, 2007.</li>
                    <li style="margin-bottom:6px;">MITCHELL-JONES, A. J.; MCLEISH, A. P. (eds.). <strong>Bat workers' manual.</strong> 3. ed. Peterborough: JNCC, 2004.</li>
                    <li style="margin-bottom:6px;">REVILLA-MARTÍN, N. et al. <strong>Monitoring cave-dwelling bats using remote passive acoustic detectors.</strong> Bioacoustics, v. 30, n. 5, p. 527–542, 2021.</li>
                    <li style="margin-bottom:6px;">ROBBINS, L. W. et al. <strong>Evaluating the effectiveness of the standard mist-netting protocol for the endangered Indiana bat.</strong> Northeastern Naturalist, v. 15, n. 2, p. 275–282, 2008.</li>
                    <li style="margin-bottom:6px;">RUNKEL, V.; GERDING, G.; MARCKMANN, U. <strong>The handbook of acoustic bat detection.</strong> Exeter: Pelagic Publishing, 2021.</li>
                    <li style="margin-bottom:6px;">SILVA, C. A. et al. <strong>Listening in the dark: acoustics indices reveal bat species diversity in a tropical savannah.</strong> Bioacoustics, v. 32, n. 1, p. 17–32, 2023.</li>
                    <li>SHELDRICK, K. et al. <strong>Standardisation in bat acoustic research: a review of reporting practices in Australia.</strong> Wildlife Research, v. 52, n. 10, 2025.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= ABA 9 — DRONES (UAS) =================
elif metodologia == "Drones (UAS)":

    st.markdown("### Drones (UAS)")

    # --- Introdução ---
    st.markdown(
        """
        <div style="font-size:15px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            O uso de sistemas aéreos não tripulados (UAS), popularmente conhecidos como drones,
            revolucionou a ecologia de campo na última década. Originalmente restritos ao setor militar,
            hoje são ferramentas essenciais para o monitoramento remoto, permitindo observar a fauna em
            locais de difícil acesso e com o mínimo de interferência humana.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Bloco de imagens: drone_asafixa + dronequi ---
    col_da, col_dq = st.columns(2)

    with col_da:
        _, ci1, _ = st.columns([0.5, 9, 0.5])
        with ci1:
            st.image("pages/img/drone_asafixa.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Drone Asa Fixa
                </div>
                <div style="font-size:13.5px;line-height:1.7;color:#2A2D2B;padding:10px 4px 0 4px;">
                    Precisa ser propulsionado para o ar e aterrissa com auxílio de paraquedas.
                    Cobre uma área maior, mas apresenta limitações rotacionais quanto à câmera.
                </div>
                <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;font-style:italic;">
                    Fonte: Menegassi (2023)
                </div>
                """,
                unsafe_allow_html=True
            )

    with col_dq:
        _, ci2, _ = st.columns([0.5, 9, 0.5])
        with ci2:
            st.image("pages/img/dronequi.png", use_container_width=True)
            st.markdown(
                """
                <div style="background-color:#2D4F1E;color:white;text-align:center;
                            padding:7px 0;font-size:14px;font-weight:700;border-radius:0 0 4px 4px;
                            margin-top:-8px;">
                    Dronequi — primeira versão
                </div>
                <div style="font-size:13.5px;line-height:1.7;color:#2A2D2B;padding:10px 4px 0 4px;">
                    Elaborado sob demanda, tem câmera térmica e hélices que permitem se comportar
                    como um helicóptero.
                </div>
                <div style="font-size:11px;color:#7A8C76;padding:6px 4px 0 4px;line-height:1.4;font-style:italic;">
                    Fonte: Menegassi (2023)
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)

    # --- Sensores + Processamento em duas colunas ---
    col_sen, col_proc = st.columns(2)

    with col_sen:
        st.markdown(
            """
            <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                        border-radius:4px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Sensores e Tecnologia Embarcada
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    A versatilidade do drone depende do sensor utilizado:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>RGB (Imagens Visuais):</strong> captura de fotos e vídeos de alta resolução para contagem e identificação.</li>
                        <li style="margin-bottom:8px;"><strong>Sensores Termais:</strong> essenciais para detectar mamíferos pelo calor corporal, especialmente em florestas densas ou durante o crepúsculo.</li>
                        <li style="margin-bottom:8px;"><strong>LiDAR:</strong> mapeia a estrutura 3D da vegetação, auxiliando na análise de habitat.</li>
                        <li><strong>Antenas de Rádio-Telemetria:</strong> modelos avançados podem localizar animais equipados com rádio-colares, otimizando a busca por indivíduos específicos.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_proc:
        st.markdown(
            """
            <div style="background-color:#FAFAF7;border:1px solid #D6DACE;padding:18px 22px;
                        border-radius:6px;">
                <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                    Processamento e Inteligência Artificial
                </div>
                <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                    O grande volume de dados gerado por voos extensos exige novas abordagens:
                    <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                        <li style="margin-bottom:8px;"><strong>Análise manual:</strong> o pesquisador revisa as imagens quadro a quadro (método tradicional).</li>
                        <li><strong>IA e Machine Learning:</strong> desenvolvimento de algoritmos para detecção automática de espécies. O desafio atual é a criação de bancos de dados padronizados para o "treinamento" das redes neurais, visando reduzir o erro de classificação.</li>
                    </ul>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top:24px;'></div>", unsafe_allow_html=True)

    # --- Estudos de Caso no Brasil ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;margin-bottom:24px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Referências e Estudos de Caso no Brasil
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                <ul style="margin-top:4px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Projeto Dronequi (Fabiano de Melo - UFV):</strong> pioneiro no monitoramento de Muriquis em Minas Gerais. O uso de sensores termais (como o DJI Mavic 3 Thermal) permitiu localizar primatas no topo do dossel, algo extremamente difícil por solo.</li>
                    <li style="margin-bottom:8px;"><strong>Monitoramento de Cervídeos (Ismael Brack):</strong> focado no cervo-do-pantanal em Mato Grosso, utilizando drones para estimativas populacionais e automatização da contagem via algoritmos.</li>
                    <li style="margin-bottom:8px;"><strong>Mamíferos Aquáticos (Inst. Mamirauá/WWF):</strong> avaliação da eficiência de detecção de botos e tucuxis na Amazônia, superando as limitações da observação em barcos.</li>
                    <li><strong>Fauna da Mata Atlântica (INMA e Santos et al., 2025):</strong> registros inovadores de preguiças-de-coleira no Espírito Santo e na Bahia.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Vantagens e Desafios ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Vantagens e Desafios Metodológicos
        </div>
        <div style="font-size:14px;line-height:1.8;color:#2A2D2B;margin-bottom:24px;">
            <table style="width:100%;border-collapse:collapse;">
                <thead>
                    <tr style="background-color:#2D4F1E;color:white;">
                        <th style="padding:8px 12px;text-align:left;width:50%;">Vantagens</th>
                        <th style="padding:8px 12px;text-align:left;width:50%;">Desvantagens e Desafios</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Não invasivo:</strong> monitoramento à distância reduz o estresse animal.</td>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Autonomia:</strong> a curta duração das baterias limita o tempo de voo.</td>
                    </tr>
                    <tr>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Segurança:</strong> reduz riscos para pesquisadores em terrenos perigosos.</td>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Ruído:</strong> o som das hélices pode causar reações de fuga em certas espécies.</td>
                    </tr>
                    <tr style="background-color:#F8FAF6;">
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Precisão:</strong> cobertura de grandes áreas com georreferenciamento exato.</td>
                        <td style="padding:8px 12px;vertical-align:top;"><strong>Legislação:</strong> necessidade de autorizações de voo (ANATEL/DECEA).</td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Considerações para Implementação ---
    st.markdown(
        """
        <div style="background-color:#F0F4ED;border-left:4px solid #2D4F1E;padding:18px 22px;
                    border-radius:4px;margin-bottom:28px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:10px;">
                Considerações para Implementação
            </div>
            <div style="font-size:14.5px;line-height:1.8;color:#2A2D2B;">
                Para garantir o sucesso do uso de UAS em projetos de conservação:
                <ul style="margin-top:8px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:8px;"><strong>Padronização:</strong> estabelecer alturas de voo que não perturbem a fauna.</li>
                    <li style="margin-bottom:8px;"><strong>Gestão de dados:</strong> planejar o armazenamento e a curadoria do grande volume de vídeos/fotos.</li>
                    <li><strong>Clima:</strong> considerar que ventos fortes e chuvas impossibilitam a operação da maioria dos modelos comerciais.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- Vídeos ---
    st.markdown(
        """
        <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:14px;">
            Exemplos práticos
        </div>
        """,
        unsafe_allow_html=True
    )

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.video("https://youtu.be/LX3bYZLmEN4")
    with col_v2:
        st.video("https://youtu.be/JLp2UBDCEgE")

    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)

    # --- Referências ---
    st.markdown(
        """
        <div style="background-color:#F5F7F2;border:1px solid #C8D4BF;padding:18px 22px;
                    border-radius:6px;">
            <div style="font-size:15.5px;font-weight:700;color:#2D4F1E;margin-bottom:12px;">
                Referências Indicadas
            </div>
            <div style="font-size:14px;line-height:2;color:#2A2D2B;">
                <ul style="margin-top:10px;margin-bottom:0;padding-left:20px;">
                    <li style="margin-bottom:6px;">ALIANE, N. <strong>Drones and AI-Driven Solutions for Wildlife Monitoring.</strong> Drones, v. 9, n. 7, p. 455, 2025.</li>
                    <li style="margin-bottom:6px;">LINCHANT, J. et al. <strong>Use of unmanned aerial systems for wildlife monitoring: A review.</strong> ISPRS Archives, v. XL-3/W3, p. 379–385, 2015.</li>
                    <li style="margin-bottom:6px;">LINCHANT, J. et al. <strong>Are unmanned aircraft systems (UASs) the future of wildlife monitoring? A review of accomplishments and challenges.</strong> Mammal Review, v. 45, n. 4, p. 239–252, 2015.</li>
                    <li style="margin-bottom:6px;">MENEGASSI, D. <strong>Drones: a nova fronteira tecnológica para o monitoramento da fauna.</strong> ((o))eco, 20 mar. 2023.</li>
                    <li style="margin-bottom:6px;">MUKHERJEE, D. et al. <strong>Drones in Wildlife Monitoring and Habitat Mapping: A Comprehensive Review.</strong> 2025.</li>
                    <li style="margin-bottom:6px;">SANTOS, P. M. et al. <strong>Every flight is a surprise: first records of the southern maned three-toed sloth through drones.</strong> Mammalia, v. 87, n. 3, p. 223–227, 2023.</li>
                    <li style="margin-bottom:6px;">SANTOS, G. N. et al. <strong>Do thermal drones outperform traditional surveys in detecting and estimating population density of sloths?</strong> Perspectives in Ecology and Conservation, 2025.</li>
                    <li>SEYMOUR, A. C. et al. <strong>Automated detection and enumeration of marine wildlife using unmanned aircraft systems (UAS) and thermal imagery.</strong> Scientific Reports, v. 7, p. 45127, 2017.</li>
                </ul>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
