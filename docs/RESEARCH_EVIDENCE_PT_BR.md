# Pesquisa inicial de evidências — dez casos reais

Pesquisa realizada em 10/10/2026. Autoria do projeto: Raquel Cruz.

Foram organizados dez dossiês e 24 registros de fontes. Esta entrega documenta descoberta de fontes e leitura disponível; não comprova desempenho retrospectivo do sistema nem preservação da versão histórica das páginas.

## Como usar

`data/research_dossiers.json` é um arquivo de preparação de pesquisa, não um arquivo diretamente importável na interface. As datas de corte dos nove novos casos ficam nulas até escolhermos o objetivo e o momento de decisão. O corte de Pas-de-Calais foi preservado. Nenhum horário de publicação desconhecido foi inventado.

As fontes ficam fora de `evidence` até confirmar horário, disponibilidade histórica e escopo. Assim, relatórios posteriores não são enviados automaticamente ao Gemini. Cada registro diferencia fonte contemporânea candidata, resposta, avaliação posterior ou índice para descoberta.

Uma data de corte durante a enchente permite estudar resposta ao evento; isso não constitui teste de previsão anterior à enchente. Para esse teste precisamos de boletins emitidos antes dos impactos.

## Dossiês

### Pas-de-Calais — Aa River

**Período:** November 2023. **Status:** validação retrospectiva pendente.

**Data de corte:** 2023-11-06T08:00:00Z.

- [Risk of rain, floods and river flooding](https://www.ecologie.gouv.fr/presse/ministere-appelle-plus-grande-prudence-raison-du-risque-pluie-dinondations-crues-regions) — French ecological transition ministry. Data registrada: 2023-11-06. Papel: `contemporaneous_candidate`. Acesso: `search_metadata_only`. Ministry reports red river-flood vigilance on the Aa and orange vigilance on other Pas-de-Calais rivers. Observação: Publication day is known, exact issue time not recovered; cannot admit at 08:00 UTC.
- [Autumn 2023 rainfall and historical floods](https://meteofrance.com/actualites/automne-2023-beaucoup-de-pluies-et-des-inondations-historiques) — Météo-France. Data registrada: 2023-12-13. Papel: `evaluation_only`. Acesso: `content_read`. Repeated rainfall from mid-October contributed to flooding, including Nord–Pas-de-Calais.

**Lacunas para análise:** Original 08:00 UTC bulletin and Aa gauges; Local rainfall and soil saturation before cutoff; Separate November and January episodes.

### Gard / Hérault — episode identity pending

**Período:** October 2024; multiple episodes. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [October 2024 rainfall review](https://meteofrance.com/actualites/octobre-2024-marque-par-plusieurs-episodes-pluvieux-intenses) — Météo-France. Data registrada: 2024-10-31. Papel: `evaluation_only`. Acesso: `content_read`. October included several intense rainfall episodes. Regional review does not uniquely identify the proposed Gard/Hérault case.
- [Gard rain-flood vigilance](https://www.gard.gouv.fr/Actualites/Vigilance-orange-Pluie-Inondations) — Gard prefecture. Data registrada: 2024-10-25 event text; exact issue time unknown. Papel: `contemporaneous_candidate`. Acesso: `search_metadata_only`. Gard experienced a Mediterranean episode beginning 24 October with orange rain-flood vigilance on 25 October. Observação: Page opening failed (502).
- [Alès weather situation](https://lemag.ales.fr/intemperies-le-point-sur-la-situation/) — Alès municipal publication. Data registrada: October 2024; text discusses 17–18 October. Papel: `evaluation_or_response_candidate`. Acesso: `content_read`. Heavy rain led to road closures and drinking-water restrictions in five communes. Observação: This concerns a different October interval from 24–27 October.
- [Hérault October 2024 press-release archive](https://www.herault.gouv.fr/Publications/Espace-presse/Communiques-de-presse/Annee-2024/Octobre-2024) — Hérault prefecture. Data registrada: Archive includes 17 and 26 October 2024. Papel: `discovery_index`. Acesso: `search_metadata_only`. Archive contains distinct vigilance updates for 17 and 26 October.

**Lacunas para análise:** Choose the original episode, commune and catchment; Do not merge 15–18 and 24–27 October; Retrieve original timed PDF bulletins and local impacts.

### Nancy — storm flooding

**Período:** Night of 21–22 May 2012. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [Natural hazard prevention](https://www.nancy.fr/services/urbanisme/prevention-des-risques-naturels) — Ville de Nancy. Data registrada: Undated current historical page. Papel: `evaluation_only`. Acesso: `content_read`. City identifies storms during 21–22 May 2012 and affected areas Clos de Médreville and Place de la Commanderie.

**Lacunas para análise:** Contemporaneous storm warnings and rainfall gauges; Source issue date of historical page; Distinguish urban runoff from Meurthe river flooding.

### Porto Alegre — Guaíba flood

**Período:** May 2024. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [Floodgates closure and emergency declaration](https://prefeitura.poa.br/gp/noticias/prefeitura-fecha-comportas-do-cais-maua-e-decreta-situacao-de-emergencia) — Prefeitura de Porto Alegre. Data registrada: 2024-05-02 08:44 displayed local time. Papel: `contemporaneous_candidate`. Acesso: `content_read`. Municipality reported a recent 2.01 m Guaíba level, a 3 m downtown flood threshold and planned floodgate closure. Observação: Confirm page timezone and original archived version before converting to UTC.
- [Guaíba level on 15 May](https://prefeitura.poa.br/defesa-civil/noticias/nivel-do-guaiba-chega-519-metros-na-manha-desta-quarta-feira) — Prefeitura de Porto Alegre. Data registrada: 2024-05-15 09:20 displayed local time. Papel: `response_or_evaluation_candidate`. Acesso: `search_metadata_only`. Municipality reports 5.19 m at 08:15 and shelter support during the ongoing flood.

**Lacunas para análise:** Choose early-warning or response decision point; Archived original forecasts and gauge times; Do not treat state casualty figures as city-only figures.

### Ahr Valley — July flood

**Período:** 14–15 July 2021. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [Hydro-climatological assessment of low Bernd](https://dwdbib.dwd.de/retrosammlung/content/titleinfo/700030) — Deutscher Wetterdienst. Data registrada: 2021-07-21. Papel: `evaluation_only`. Acesso: `catalogue_read`. DWD catalogue identifies an assessment of heavy rainfall associated with Bernd during 12–19 July 2021. Observação: Bibliographic record read; full report still requires extraction.
- [DWD annual report 2021](https://www.dwd.de/EN/ourservices/annual_reports_dwd/annual_reports_pdf/annual_report_2021.pdf?__blob=publicationFile&v=2) — Deutscher Wetterdienst. Data registrada: Annual report 2021; publication timestamp unknown. Papel: `evaluation_only`. Acesso: `search_metadata_only`. Annual report describes severe losses in the Ahr Valley associated with the July rainfall. Observação: PDF opening failed.

**Lacunas para análise:** Original DWD warnings before selected cutoff; Ahr gauge station/datum and warning chronology; Extract full DWD report and separate reconstructed observations from contemporaneous availability.

### Sindh — monsoon floods

**Período:** 2022 monsoon. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [Pakistan monsoon floods situation report 5](https://reliefweb.int/report/pakistan/pakistan-2022-monsoon-floods-situation-report-no-5-9-september-2022) — OCHA via ReliefWeb. Data registrada: 2022-09-09 report label. Papel: `response_candidate`. Acesso: `search_metadata_only`. Search metadata identifies severe housing losses in Sindh in report 5. Observação: Full page blocked by 403; figures not admitted as verified evidence.
- [Revised Pakistan floods response plan](https://reliefweb.int/report/pakistan/revised-pakistan-2022-floods-response-plan-01-sep-2022-31-may-2023-04-oct-2022) — OCHA via ReliefWeb. Data registrada: 2022-10-04 report label. Papel: `evaluation_or_late_response_candidate`. Acesso: `search_metadata_only`. Response plan provides later humanitarian impact context for Sindh.

**Lacunas para análise:** Choose district and decision date in prolonged flood; Retrieve original OCHA PDFs and PMD/NDMA warnings; Separate province, district and national totals.

### Rasuwa — Bhote Koshi / Trishuli corridor

**Período:** 26 August 2026. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [Rasuwa flash-flood media advisory](https://www.icimod.org/press-release/major-flash-flood-sweeps-through-nepals-rasuwa-district-raising-fears-of-further-downstream-flooding/) — ICIMOD. Data registrada: 2026-08-26; exact time pending. Papel: `response_candidate`. Acesso: `content_read`. ICIMOD reports a major flash flood in Rasuwa and downstream concerns along Bhote Koshi and Trishuli.
- [Kyirong–Rasuwa flood resource hub](https://www.icimod.org/kyirong-rasuwa-flood-2026-nepal-china-border/) — ICIMOD. Data registrada: Current evolving page; original publication time unknown. Papel: `evaluation_only`. Acesso: `content_read`. Resource hub identifies the 26 August event and discusses unresolved cascade timing and mechanisms. Observação: Do not label the event a rainfall flood or GLOF without qualification; page includes later updates.
- [Situation Update 3](https://www.bwsn.org.np/2925-2/) — Bagmati Welfare Society Nepal. Data registrada: Header 28 August; body update 30 August 2026. Papel: `evaluation_only`. Acesso: `content_read`. NGO update reports evolving impacts and infrastructure disruption. Observação: Internal dates and totals conflict; not used as authoritative casualty baseline.

**Lacunas para análise:** Exact advisory issue time and early DHM/NDRRMA alerts; Separate 2026 event from July 2025 flood; Resolve scientific disagreement on initiation and warning window.

### Valencia — DANA

**Período:** 29 October 2024. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [AEMET episode study catalogue](https://www.aemet.es/en/conocermas/recursos_en_linea/publicaciones_y_estudios/estudios/detalles/episodio_dana_oct_nov24) — AEMET. Data registrada: Preliminary report prepared early November 2024; full report date pending. Papel: `evaluation_only`. Acesso: `content_read`. AEMET documents the 29 October Valencia event and provides studies of rainfall and warning chronology.
- [October climate balance](https://www.miteco.gob.es/es/prensa/ultimas-noticias/2024/noviembre/octubre-de-2024-fue-el-mas-lluvioso-de-la-serie-historica.html) — MITECO / AEMET. Data registrada: 2024-11-08. Papel: `evaluation_only`. Acesso: `content_read`. Balance reports 771 mm in 24 hours and 185 mm in one hour at Turís. Observação: Turís station totals must not be assigned to all Valencia or to city gauges.

**Lacunas para análise:** Archived AEMET and CHJ/SAIH warnings and measurements; Choose municipality and cutoff before or during impacts; Keep November reports outside October agent inputs.

### Texas — Guadalupe River

**Período:** 4 July 2025. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [NWS EWX flash-flood emergency bulletin](https://mesonet.agron.iastate.edu/wx/afos/p.php?e=202507041912&pil=FFWEWX) — NWS Austin/San Antonio; archived by Iowa State IEM. Data registrada: 2025-07-04T19:12:00Z. Papel: `contemporaneous_candidate`. Acesso: `content_read`. Bulletin identifies an ongoing dangerous flood wave from Hunt through Kerrville and Center Point, based on radar and gauges. Observação: Issuance time explicit; independent archive preserves primary NWS text. Choose response cutoff, not a pre-flood prediction test.
- [Guadalupe River at Kerrville](https://water.noaa.gov/gauges/krrt2) — NOAA / NWS. Data registrada: Current gauge page; historical data access pending. Papel: `evaluation_candidate`. Acesso: `dynamic_page_limited`. Gauge page provides station context; historical peaks need direct data extraction.
- [Texas flooding activation](https://disasters.nasa.gov/what-we-do/disasters/disasters-activations/texas-flooding-july-2025) — NASA. Data registrada: July 2025; exact publication date pending. Papel: `evaluation_or_response_candidate`. Acesso: `search_metadata_only`. NASA describes aerial and satellite data supporting flood-impact assessment.

**Lacunas para análise:** Earlier timed warnings if evaluating anticipatory decisions; USGS discharge and station datum; Cutoff explicitly distinguishes ongoing-response assessment from prediction.

### Derna — Storm Daniel and dam failures

**Período:** 10–11 September 2023. **Status:** validação retrospectiva pendente.

**Data de corte:** a definir; não presumida.

- [UN support after Storm Daniel](https://libya.un.org/en/246089-united-nations-libya-steps-support-those-affected-storm-daniel) — United Nations in Libya. Data registrada: Page date 15 September; dateline 16 September 2023. Papel: `evaluation_only`. Acesso: `content_read`. UN describes northeastern Libya flooding, dam failures in Wadi Derna and response constraints. Observação: Publication labels disagree by one day; no precise UTC timestamp asserted.
- [Satellite flood extent in Derna](https://unosat.org/products/3671) — UNOSAT. Data registrada: Imagery acquired 2023-09-13 at 13:39 local; publication date pending. Papel: `evaluation_only`. Acesso: `search_metadata_only`. Product metadata identifies satellite mapping of Derna after Daniel. Observação: Imagery acquisition time is not the product publication time; page text unavailable.
- [Storm Daniel meteorological review](https://public.wmo.int/media/news/storm-daniel-leads-extreme-rain-and-floods-mediterranean-heavy-loss-of-life-libya) — WMO. Data registrada: 2023-09-12. Papel: `evaluation_only`. Acesso: `search_metadata_only`. WMO describes Mediterranean storm rainfall and catastrophic Derna impacts.

**Lacunas para análise:** Libyan meteorological forecasts before dam failures; Dam-specific records and evacuation chronology; Do not attribute regional rainfall values to Derna gauge without station evidence.

## Conclusões e limites

- As fontes de Nancy situam o evento na noite de 21–22/05/2012. A fonte ICIMOD identifica o evento do Nepal em 26/08/2026, separado do evento de julho de 2025.
- Gard/Hérault continua sem identidade única: existem fontes para mais de um episódio em outubro de 2024. Preservar o caso como pendente em vez de combinar eventos.
- Texas possui um boletim primário do NWS preservado pelo arquivo universitário IEM, emitido em 04/07/2025 às 19:12 UTC. É evidência de resposta a inundação em andamento, não aviso anterior ao início.
- Porto Alegre possui comunicado municipal com horário exibido; o fuso e a versão histórica precisam ser confirmados antes de habilitar entrada no corte.
- As páginas de ReliefWeb para Sindh não foram lidas integralmente nesta sessão (403). O levantamento registra metadados e links, sem apresentar o conteúdo como verificado.
- Não foram coletadas séries completas de sensores, imagens georreferenciadas ou rótulos de decisão humana. Ausência desses dados permanece explícita.

## Próximo passo técnico

Selecionar o objetivo e o corte de cada caso; recuperar originais/arquivos históricos; converter somente evidências temporalmente admissíveis para o schema de `data/evidence_template.json`. Conservar um conjunto separado de resultados posteriores para avaliação. Apenas depois executar Gemini, revisar criticamente e medir resultados.

## Integração na versão 0.2

Os dez dossiês agora têm cadastros correspondentes no seletor da interface. O arquivo de pesquisa continua sendo um registro de preparação; suas fontes não são admitidas automaticamente como evidência. Os cadastros podem ser editados e salvos com **Register / update**. Nove datas de corte permanecem pendentes.
