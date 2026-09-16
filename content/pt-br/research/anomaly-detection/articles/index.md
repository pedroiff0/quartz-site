---
publish: false
title: Artigos
created: 2026-07-23
modified: 2026-07-25T23:58:08.061-03:00
published: 2026-07-25T23:58:08.061-03:00
order: 1
---

> [!note] Resumo
> Anotações de leitura sobre 28 artigos científicos relevantes para o projeto [Detecção de Anomalias em Dados do Gaia](pt-br/research/anomaly-detection), organizadas por tema.

<div class="media-carousel">
  <a href="/pt-br/research/anomaly-detection/articles/collaboration2016" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="A Missão Gaia" />
    <div class="slide-caption">A Missão Gaia</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/buder2025" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GALAH DR4" />
    <div class="slide-caption">GALAH DR4</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/majewski2017" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="APOGEE" />
    <div class="slide-caption">APOGEE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/deandrade2025" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GCNS × GALAH DR4" />
    <div class="slide-caption">GCNS × GALAH DR4</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/traven2017" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GALAH — Classificação via t-SNE" />
    <div class="slide-caption">GALAH — Classificação via t-SNE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/lochner2021" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="ASTRONOMALY" />
    <div class="slide-caption">ASTRONOMALY</div>
  </a>
</div>

Anotações de leitura sobre artigos científicos relevantes para minha pesquisa em detecção de anomalias em populações estelares — sínteses próprias, não os artigos completos (direitos autorais das editoras/arXiv permanecem com os autores originais). Agrupadas por papel no projeto: os levantamentos e dados que uso, os métodos de aprendizado de máquina que aplico, os modelos estelares que calibram minhas idades/isócronas, e o contexto de dinâmica/química galáctica que interpreta os resultados.

## 🛰️ Levantamentos e catálogos (dados)

- [A Missão Gaia](pt-br/research/anomaly-detection/articles/collaboration2016) — astrometria de bilhões de estrelas; fonte das coordenadas cinemáticas do projeto.
- [Gaia EDR3 — Gaia Catalogue of Nearby Stars](pt-br/research/anomaly-detection/articles/collaboration2021) — catálogo limpo a 100 pc do Sol, base da amostra GCNS.
- [GCNS × GALAH DR4](pt-br/research/anomaly-detection/articles/deandrade2025) — meu próprio artigo, a análise conjunta que fundamenta a Etapa 1.
- [GALAH DR4](pt-br/research/anomaly-detection/articles/buder2025) — 4º release do GALAH: até 32 elementos por estrela via redes neurais.
- [GALAH — Pipeline de Redução de Dados](pt-br/research/anomaly-detection/articles/kos2017) — como os espectros brutos do HERMES viram os parâmetros do catálogo.
- [APOGEE](pt-br/research/anomaly-detection/articles/majewski2017) — survey infravermelho de alta resolução, usado como comparação/contexto.
- [LAMOST DR5 — Abundâncias de 16 Elementos](pt-br/research/anomaly-detection/articles/xiang2019) — outro survey espectroscópico de grande volume, abordagem _data-driven_ (DD-Payne).
- [S-PLUS DR4 — Outliers de SED](pt-br/research/anomaly-detection/articles/quispehuaynasi2025) — detecção de anomalias fotométricas em survey diferente, paralelo metodológico.

## 🤖 Aprendizado de máquina e detecção de anomalias

- [GALAH — Classificação via t-SNE](pt-br/research/anomaly-detection/articles/traven2017) — metodologia-base da Etapa 2 (t-SNE sobre espectros brutos).
- [da Silva & Smiljanic (2023) — t-SNE Quimiodinâmico](pt-br/research/anomaly-detection/articles/dasilva2023) — base da comparação entre colunas de catálogo e pixels do espectro.
- [ASTRONOMALY](pt-br/research/anomaly-detection/articles/lochner2021) — motivação de escala: por que big data astronômico exige detecção automática de anomalias.
- [Detecção Ativa de Anomalias (Time-Domain)](pt-br/research/anomaly-detection/articles/ishida2021) — _active learning_ aplicado à descoberta de objetos incomuns.
- [Machine Learning para Binárias](pt-br/research/anomaly-detection/articles/traven2019) — revisão de métodos de ML em grandes levantamentos.
- [GALAH — Estrelas de Linhas de Emissão](pt-br/research/anomaly-detection/articles/otar2021) — autoencoder que reconstrói espectros para achar emissões anômalas — mesma família de método da Etapa 2.
- [GALAH — Estrelas Extremamente Pobres em Metais](pt-br/research/anomaly-detection/articles/hughes2022) — ML supervisionado para achar 54 candidatas EMP no GALAH.
- [GALAH — Bandas Interestelares Difusas](pt-br/research/anomaly-detection/articles/vogrini2023) — outro exemplo de mineração de _big data_ espectroscópico do GALAH.

## ⭐ Modelos estelares e idades

- [PARSEC — Isócronas Estelares](pt-br/research/anomaly-detection/articles/bressan2012) — código de evolução estelar que gera as isócronas usadas no diagrama de Kiel.
- [PARSEC-COLIBRI — Isócronas com Fase TP-AGB](pt-br/research/anomaly-detection/articles/marigo2017) — geração mais recente das isócronas, com fase TP-AGB detalhada.
- [GALAH — Relógios Químicos](pt-br/research/anomaly-detection/articles/hayden2022) — idades via XGBoost a partir só de metalicidade/abundâncias.
- [GALAH — Binárias FGK](pt-br/research/anomaly-detection/articles/traven2020) — amostra de binárias espectroscópicas, relevante para limpar contaminantes da amostra.
- [SpectroTranslator](pt-br/research/anomaly-detection/articles/thomas2024) — rede neural para converter parâmetros entre surveys diferentes.

## 🌌 Dinâmica e química galáctica (interpretação)

- [galpy](pt-br/research/anomaly-detection/articles/bovy2015) — pacote usado para calcular órbitas e ações, base da cinemática do projeto.
- [Distribuição de Massa e Potencial da Via Láctea](pt-br/research/anomaly-detection/articles/mcmillan2017) — o potencial galáctico usado no galpy para integrar órbitas.
- [GALAH — Quimiodinâmica da Vizinhança Solar](pt-br/research/anomaly-detection/articles/hayden2020) — estrutura quimiodinâmica de referência para comparar com a amostra cruzada.
- [Gaia-ESO — Transição Disco Fino/Espesso](pt-br/research/anomaly-detection/articles/recioblanco2014) — contexto de populações estelares e migração radial.
- [Coformação dos Discos Fino/Espesso (z>2)](pt-br/research/anomaly-detection/articles/borbolato2025) — cenário de formação para a dicotomia disco fino/espesso.
- [Tempos de Vida Estelares e Razões de Abundância](pt-br/research/anomaly-detection/articles/tinsley1979) — artigo clássico de evolução química, base teórica da nucleossíntese.
- [Abundâncias em Anãs G VI](pt-br/research/anomaly-detection/articles/wallerstein1962) — artigo histórico, uma das primeiras determinações sistemáticas de abundância estelar.
