import streamlit as st
import pandas as pd
import requests
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from estilo import aplicar_estilo

aplicar_estilo("pages/2_Consulta.py")

# ===== FUNÇÕES =====
@st.cache_data
def carregar_dados():
    df = pd.read_csv("dados_sibm.csv", sep=",", encoding="utf-8")
    df = df.rename(columns={
        "copam_2010":  "copam_mg_2010",
        "iema_2022":   "iema_es_2022",
        "semil_2018":  "semil_sp_2018",
        "sedest_2024": "sedest_pr_2024",
    })
    return df

df = carregar_dados()

@st.cache_data
@st.cache_data
def buscar_taxon_key(nome_cientifico):
    try:
        resp = requests.get(
            "https://api.gbif.org/v1/species/match",
            params={"name": nome_cientifico, "strict": False},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        chave = data.get("usageKey") or data.get("speciesKey")
        return chave, data
    except Exception as e:
        return None, {"erro": str(e)}

@st.cache_data
def buscar_ocorrencias_gbif(nome_cientifico):
    try:
        taxon_key, _ = buscar_taxon_key(nome_cientifico)
        if not taxon_key:
            return None, []
        ocorrencias = []
        offset = 0
        while True:
            resp2 = requests.get(
                "https://api.gbif.org/v1/occurrence/search",
                params={
                    "taxonKey": taxon_key,
                    "country": "BR",
                    "hasCoordinate": True,
                    "hasGeospatialIssue": False,
                    "limit": 300,
                    "offset": offset
                },
                timeout=30
            )
            resp2.raise_for_status()
            data2 = resp2.json()
            resultados = data2.get("results", [])
            if not resultados:
                break
            for r in resultados:
                lat = r.get("decimalLatitude")
                lon = r.get("decimalLongitude")
                if lat and lon:
                    ocorrencias.append({"lat": lat, "lon": lon})
            if data2.get("endOfRecords", True):
                break
            offset += 300
        return taxon_key, ocorrencias
    except Exception:
        return None, []

@st.cache_data
def buscar_sinonimos_gbif(taxon_key):
    if not taxon_key:
        return []
    try:
        resp = requests.get(
            f"https://api.gbif.org/v1/species/{taxon_key}/synonyms",
            params={"limit": 100},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
        nomes = [r.get("canonicalName", "") for r in data.get("results", []) if r.get("canonicalName")]
        return nomes if nomes else []
    except Exception:
        return []

# ===== TÍTULO =====
st.markdown('<div class="main-title">Sistema de Consulta de Espécies</div>', unsafe_allow_html=True)

# ===== BUSCA =====
nome = st.text_input("Nome da Espécie:", placeholder="Digite o binômio da espécie")

if nome:
    resultado_exato = df[df["binomio"].str.lower() == nome.strip().lower()]
    if not resultado_exato.empty:
        resultado = resultado_exato
    else:
        resultado = df[df["binomio"].str.contains(nome.strip(), case=False, na=False)]

    if not resultado.empty:
        row = resultado.iloc[0]

        # Buscar taxonKey uma vez para usar em todas as tabs
        taxon_key_sp, _ = buscar_taxon_key(row['binomio'])

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Taxonomia", "Distribuição", "Status de Conservação", "Referências"]
        )

        # ================= TAXONOMIA =================
        with tab1:
            col1, col2 = st.columns([1, 2])

            with col1:
                foto = str(row.get("foto_inat", "")).strip()
                if foto and foto.lower() not in ("nan", "-", "") and foto.startswith("http"):
                    try:
                        st.image(foto, use_container_width=True)
                    except Exception:
                        st.markdown("*(imagem indisponível)*")

            with col2:
                st.markdown(
                    f"""
                    <div style="line-height:1.2;margin-bottom:25px;">
                        <div style="font-size:34px;font-weight:600;"><i>{row['binomio']}</i></div>
                        <div style="font-size:18px;color:gray;">{row['nome_comum']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                col_tax, col_sin = st.columns([1, 1])

                with col_tax:
                    st.markdown(f"**Classe:** {row.get('classe', '')}")
                    st.markdown(f"**Ordem:** {row.get('ordem', '')}")
                    st.markdown(f"**Família:** {row.get('familia', '')}")
                    st.markdown(f"**Gênero:** {row.get('genero', '')}")

                with col_sin:
                    if taxon_key_sp:
                        sinonimos = buscar_sinonimos_gbif(taxon_key_sp)
                        if sinonimos:
                            st.markdown(f"**Sinônimos:** {', '.join(sinonimos)}")
                        else:
                            st.markdown("**Sinônimos:** Nenhum registrado")

                st.markdown("<br>", unsafe_allow_html=True)
                col_dieta, col_locomocao = st.columns(2)
                with col_dieta:
                    st.markdown("#### Dieta")
                    st.write(row.get("dieta", ""))
                with col_locomocao:
                    st.markdown("#### Locomoção")
                    st.write(row.get("locomocao", ""))

            st.markdown('<hr style="border:none;height:1px;background-color:black;margin:20px 0;">', unsafe_allow_html=True)
            st.markdown(
                """
                <div style="font-size:13px;line-height:1.6;text-align:justify;">
                <b>Dieta:</b> carnívoro/carnivore (Ca), frugívoro/frugivore (Fr),
                folívoro/folivore (Fo), gomívoro/gumivore (Go), granívoro/granivore (Gr),
                herbívoro pastador/herbivore grazer (Hb), hematófago/sanguivore (He),
                insetívoro/insectivore (In), mirmecófago/myrmecophage (Myr),
                nectarívoro/nectarivore (Nec), onívoro/omnivore (On),
                planctófago/planktivore (Pc), piscívoro/piscivore (Ps),
                predador de sementes/seed predator (Se), teutófago/teuthophagous (Te).
                <div style="margin-top:25px;">
                    <b>Locomoção:</b> aquático/aquatic (Aq), arborícola/arboreal (Ar),
                    fossorial (Fs), semi-aquático/semiaquatic (SA),
                    escansorial/scansorial (Sc), semi-fossorial/semifossorial (SF),
                    terrestre/terrestrial (Te), voador/volant (Vo).
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ================= DISTRIBUIÇÃO =================
        with tab2:
            st.markdown("### Distribuição Geográfica")
            col_mapa, col_info = st.columns([1, 1])

            with col_mapa:
                st.markdown("#### Ocorrências no Brasil (GBIF)")
                with st.spinner("Buscando ocorrências no GBIF..."):
                    ocorrencias = buscar_ocorrencias_gbif(row['binomio'])[1]
                    taxon_key = taxon_key_sp

                if taxon_key and ocorrencias:
                    df_occ = pd.DataFrame(ocorrencias)
                    st.map(df_occ, zoom=3)
                    st.markdown(
                        f'<div style="font-size:12px;color:gray;">📍 {len(ocorrencias)} registros &nbsp;|&nbsp; '
                        f'🔗 <a href="https://www.gbif.org/occurrence/search?taxon_key={taxon_key}&country=BR" target="_blank">Ver todos no GBIF</a></div>',
                        unsafe_allow_html=True
                    )
                elif taxon_key and not ocorrencias:
                    st.info("Espécie encontrada no GBIF, mas sem registros com coordenadas para o Brasil.")
                    st.markdown(f'🔗 <a href="https://www.gbif.org/occurrence/search?taxon_key={taxon_key}&country=BR" target="_blank">Ver no GBIF</a>', unsafe_allow_html=True)
                else:
                    st.info("Espécie não encontrada no GBIF.")

            with col_info:
                st.markdown("#### Informações de Distribuição")

                def val(campo, vazio):
                    v = row.get(campo, "")
                    if not pd.notna(v) or str(v).strip() in ("", "-", "nan"):
                        return vazio
                    return str(v).strip()

                st.markdown("**Estados:**")
                st.write(val("distribuicao_estado", "Sem informações"))
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("**Distribuição Geral:**")
                st.write(val("distribuicao", "Sem informações"))
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("**Endemismo:**")
                st.write(val("endemismo", "Sem endemismo"))

        # ================= STATUS =================
        with tab3:
            st.markdown("### Status de Conservação")

            COR_CATEGORIA = {
                "LC": "#4CAF50",
                "NT": "#8BC34A",
                "VU": "#FFC107",
                "EN": "#FF9800",
                "CR": "#FF5722",
                "CR(PEX)": "#C62828",
                "EW": "#B71C1C",
                "EX": "#7B1FA2",
            }
            COR_SEM_CATEGORIA = "#9E9E9E"

            COR_TOPO = {
                "cites_2025":      "#8B6914",
                "iucn_2025":       "#2D4F1E",
                "salve_2023":      "#2D4F1E",
                "mma_2022":        "#2D4F1E",
                "copam_mg_2010":   "#2D4F1E",
                "iema_es_2022":    "#2D4F1E",
                "semil_sp_2018":   "#2D4F1E",
                "sedest_pr_2024":  "#2D4F1E",
                "consema_ma_2025": "#2D4F1E",
                "sema_ba_2017":    "#2D4F1E",
                "consema_sc_2011": "#2D4F1E",
                "gov_rs_2014":     "#2D4F1E",
                "sema_ce_2022":    "#2D4F1E",
            }

            LISTAS = [
                ("cites_2025",      "CITES 2025"),
                ("iucn_2025",       "IUCN 2025"),
                ("salve_2023",      "SALVE 2023"),
                ("mma_2022",        "MMA 2022"),
                ("copam_mg_2010",   "COPAM MG 2010"),
                ("iema_es_2022",    "IEMA ES 2022"),
                ("semil_sp_2018",   "SEMIL SP 2018"),
                ("sedest_pr_2024",  "SEDEST PR 2024"),
                ("consema_ma_2025", "CONSEMA MA 2025"),
                ("sema_ba_2017",    "SEMA BA 2017"),
                ("consema_sc_2011", "CONSEMA SC 2011"),
                ("gov_rs_2014",     "GOV RS 2014"),
                ("sema_ce_2022",    "SEMA CE 2022"),
            ]

            CITES_VALIDOS = {"I", "II", "III", "I/II", "II/III", "I/III"}

            def cor_categoria(campo, valor):
                v = str(valor).strip().upper()
                if campo == "cites_2025":
                    return "#BFA07A" if v in CITES_VALIDOS else COR_SEM_CATEGORIA
                return COR_CATEGORIA.get(v, COR_SEM_CATEGORIA)

            def texto_categoria(campo, valor):
                v = str(valor).strip().upper()
                if campo == "cites_2025":
                    return v if v in CITES_VALIDOS else "SEM CATEGORIA"
                if v in COR_CATEGORIA:
                    return v
                return "SEM CATEGORIA"

            for linha in range(4):
                cols = st.columns(4)
                for i, col in enumerate(cols):
                    idx = linha * 4 + i
                    if idx >= len(LISTAS):
                        break
                    campo, label = LISTAS[idx]
                    valor = row.get(campo, "")
                    cor_topo = COR_TOPO[campo]
                    cor_base = cor_categoria(campo, valor)
                    texto = texto_categoria(campo, valor)
                    with col:
                        st.markdown(
                            f"""
                            <div style="border-radius:10px;overflow:hidden;box-shadow:0 2px 6px rgba(0,0,0,0.15);margin-bottom:16px;">
                                <div style="background-color:{cor_topo};color:white;text-align:center;padding:18px 8px;font-size:20px;font-weight:600;letter-spacing:0.5px;">
                                    {label}
                                </div>
                                <div style="background-color:{cor_base};color:white;text-align:center;padding:18px 8px;font-size:26px;font-weight:700;letter-spacing:1px;text-shadow:1px 1px 3px rgba(0,0,0,0.35);">
                                    {texto}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            st.markdown('<hr style="border:none;height:1px;background-color:black;margin:24px 0;">', unsafe_allow_html=True)

            iucn_rationale = row.get("iucn_rationale", "")
            if pd.notna(iucn_rationale) and str(iucn_rationale).strip() not in ("", "-"):
                st.markdown("#### Explicação IUCN")
                st.write(iucn_rationale)
                st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                """
                <div style="font-size:13px;line-height:1.8;text-align:justify;">
                <b>Categorias:</b><br>
                <b>I</b> - Apêndice I &nbsp;|&nbsp;
                <b>II</b> - Apêndice II &nbsp;|&nbsp;
                <b>III</b> - Apêndice III &nbsp;|&nbsp;
                <b>EX</b> - Extinto &nbsp;|&nbsp;
                <b>EW</b> - Extinto na Natureza &nbsp;|&nbsp;
                <b>CR</b> - Criticamente em Perigo &nbsp;|&nbsp;
                <b>CR(PEX)</b> - Provavelmente Extinta &nbsp;|&nbsp;
                <b>EN</b> - Em Perigo &nbsp;|&nbsp;
                <b>VU</b> - Vulnerável &nbsp;|&nbsp;
                <b>NT</b> - Quase Ameaçado &nbsp;|&nbsp;
                <b>LC</b> - Pouco Preocupante
                <div style="margin-top:16px;">
                <b>Siglas:</b><br>
                <b>IUCN</b> - International Union for Conservation of Nature &nbsp;|&nbsp;
                <b>SALVE</b> - Sistema de Avaliação do Risco de Extinção da Biodiversidade &nbsp;|&nbsp;
                <b>MMA</b> - Ministério do Meio Ambiente &nbsp;|&nbsp;
                <b>COPAM MG</b> - Conselho Estadual de Política Ambiental - MG &nbsp;|&nbsp;
                <b>IEMA ES</b> - Instituto Estadual de Meio Ambiente - ES &nbsp;|&nbsp;
                <b>SEMIL SP</b> - Secretaria de Meio Ambiente, Infraestrutura e Logística - SP &nbsp;|&nbsp;
                <b>SEDEST PR</b> - Secretaria de Estado do Desenvolvimento Sustentável - PR &nbsp;|&nbsp;
                <b>CONSEMA MA</b> - Conselho Estadual do Meio Ambiente - MA &nbsp;|&nbsp;
                <b>SEMA BA</b> - Secretaria do Meio Ambiente - BA &nbsp;|&nbsp;
                <b>CONSEMA SC</b> - Conselho Estadual do Meio Ambiente - SC &nbsp;|&nbsp;
                <b>GOV RS</b> - Governo Estadual Rio Grande do Sul &nbsp;|&nbsp;
                <b>SEMA CE</b> - Secretaria do Meio Ambiente - CE
                </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ================= REFERÊNCIAS =================
        with tab4:
            refs_especie = row.get("referencias", "")
            if pd.notna(refs_especie) and str(refs_especie).strip() not in ("", "-"):
                st.markdown("#### Referências da Espécie")
                st.write(refs_especie)
                st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("#### Referências Gerais")
            st.markdown(
                """
                <div style="font-size:14px;line-height:2.0;text-align:justify;">
                Abreu, E.F., Casali, D.M., Garbino, G.S.T., Loss, A.C., Moras, L.M., Nascimento, F.O.,
                Oliveira, M.L., Pavan, S.E., Percequillo, A.R., & Nascimento, M.C. 2025.
                Lista de Mamíferos do Brasil (2025-1) [Data set]. Zenodo.
                <a href="https://doi.org/10.5281/zenodo.18378485" target="_blank">https://doi.org/10.5281/zenodo.18378485</a>
                <br><br>
                CITES, Convention on International Trade in Endangered Species of Wild Fauna and Flora.
                Appendices | CITES. Disponível em:
                <a href="https://cites.org/eng/app/appendices.php" target="_blank">https://cites.org/eng/app/appendices.php</a>
                <br><br>
                CONSEMA, Conselho Estadual de Meio Ambiente – CONSEMA. Resolução CONSEMA nº 82, de 5 de maio de 2025. Aprova a Lista Oficial de Espécies da Fauna de Vertebrados Ameaçadas de Extinção do Estado do Maranhão. São Luís: CONSEMA, 2025. Disponível em:
                <a href="https://www.sema.ma.gov.br/uploads/sema/docs/Resolu%C3%A7%C3%A3o_Consema_n_82-2025_-_lista_vermelha_MA_05mai2025.pdf" target="_blank">https://www.sema.ma.gov.br/...</a>
                <br><br>
                CONSEMA, Conselho Estadual do Meio Ambiente – CONSEMA. Resolução CONSEMA nº 002, de 06 de dezembro de 2011. Reconhece a Lista Oficial de Espécies da Fauna Ameaçadas de Extinção no Estado de Santa Catarina e dá outras providências. Florianópolis: CONSEMA, 2011. Disponível em:
                <a href="https://www.ima.sc.gov.br/index.php/downloads/biodiversidade/fauna/2430-resolucao-consema-02-2011-reconhece-a-lista-oficial-de-especies-da-fauna-ameacadas-de-extincao" target="_blank">https://www.ima.sc.gov.br/...</a>
                <br><br>
                COPAM, Conselho Estadual de Política Ambiental.
                Deliberação Normativa COPAM N° 147, 30 abr. 2010. Disponível em:
                <a href="https://www.siam.mg.gov.br/sla/download.pdf?idNorma=13192" target="_blank">https://www.siam.mg.gov.br/sla/download.pdf?idNorma=13192</a>
                <br><br>
                ICMBio, Instituto Chico Mendes de Conservação da Biodiversidade. 2026.
                Sistema de Avaliação do Risco de Extinção da Biodiversidade – SALVE. Disponível em:
                <a href="https://salve.icmbio.gov.br/" target="_blank">https://salve.icmbio.gov.br/</a>
                <br><br>
                IEMA, Instituto Estadual de Meio Ambiente.
                Decreto N° 5237-R, 25 nov. 2022. Disponível em:
                <a href="https://iema.es.gov.br/Media/iema/FAUNA/Decreto%205237-R_2022_25-Nov%20-%20Fauna%20(s-peixes)%20-%20Lista%20de%20Esp%C3%A9cies%20Amea%C3%A7adas%20de%20Extin%C3%A7%C3%A3o.pdf" target="_blank">https://iema.es.gov.br/...</a>
                <br><br>
                iNaturalist community. Observations of Mammals from Brazil. Exported from
                <a href="https://www.inaturalist.org" target="_blank">https://www.inaturalist.org</a>
                <br><br>
                IUCN, International Union for Conservation of Nature. 2025.
                The IUCN Red List of Threatened Species. Version 2025-2.
                <a href="https://www.iucnredlist.org" target="_blank">https://www.iucnredlist.org</a>
                <br><br>
                MMA, Ministério do Meio Ambiente.
                Portaria MMA N° 148, 8 jun. 2022. Disponível em:
                <a href="https://www.gov.br/icmbio/pt-br/assuntos/centros-de-pesquisa/aves-silvestres/arquivos/portaria-148-2022.pdf" target="_blank">https://www.gov.br/icmbio/...</a>
                <br><br>
                RIO GRANDE DO SUL (Estado). Decreto nº 51.797, de 8 de setembro de 2014. Declara as espécies da fauna silvestre ameaçadas de extinção no Estado do Rio Grande do Sul. Porto Alegre: Governo do Estado do Rio Grande do Sul, 2014. Disponível em:
                <a href="https://www.sema.rs.gov.br/upload/arquivos/201804/11120520-dec-51-797.pdf" target="_blank">https://www.sema.rs.gov.br/...</a>
                <br><br>
                SEDEST, Secretaria de Estado do Desenvolvimento Sustentável.
                Decreto N° 6.040, 5 jun. 2024. Disponível em:
                <a href="https://leisestaduais.com.br/pr/decreto-n-6040-2024-parana-reconhece-as-especies-da-fauna-ameacada-de-extincao-no-estado-do-parana-e-da-outras-providencias" target="_blank">https://leisestaduais.com.br/...</a>
                <br><br>
                SEMA, Secretaria do Meio Ambiente – SEMA. Portaria nº 37, de 15 de agosto de 2017. Torna pública a Lista Oficial das Espécies da Fauna Ameaçadas de Extinção do Estado da Bahia. Salvador: SEMA, 2017.
                <br><br>
                SEMA, Secretaria do Meio Ambiente e Mudança do Clima. Livro vermelho dos animais ameaçados de extinção do Ceará. Volume 1: Mamíferos. Fortaleza: SEMA, 2022. Disponível em:
                <a href="https://www.sema.ce.gov.br/wp-content/uploads/sites/36/2025/12/Vol.1_MAMIFEROS_Livro-Vermelho-do-Ceara-3.pdf" target="_blank">https://www.sema.ce.gov.br/...</a>
                <br><br>
                SEMIL, Secretaria de Meio Ambiente, Infraestrutura e Logística.
                Decreto N° 63.853, 27 nov. 2018. Disponível em:
                <a href="https://www.al.sp.gov.br/repositorio/legislacao/decreto/2018/decreto-63853-27.11.2018.htmll" target="_blank">https://www.al.sp.gov.br/...</a>
                </div>
                """,
                unsafe_allow_html=True
            )

        # ===== EXPORTAR =====
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <style>
            [data-testid="stDownloadButton"] button {
                background-color: #2D4F1E;
                color: white;
                border: none;
            }
            [data-testid="stDownloadButton"] button:hover {
                background-color: #1e3714;
                color: white;
                border: none;
            }
            </style>
        """, unsafe_allow_html=True)
        st.download_button(
            "Exportar Dados",
            resultado.to_csv(index=False),
            file_name="dados_especie.csv"
        )

    else:
        st.warning("Espécie não encontrada.")
