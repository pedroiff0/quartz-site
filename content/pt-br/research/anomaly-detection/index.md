---
publish: true
title: "Detecção de Anomalias em Dados do Gaia"
created: 2025-09-01
cssclasses:
  - page-layout
---
# Detecção de Anomalias em Dados do Gaia

> [!note] Resumo
> Pesquisa de iniciação científica que cruza astrometria de altíssima precisão do Gaia (GCNS) com espectroscopia de alta resolução (GALAH DR4) para encontrar e caracterizar estrelas anômalas na vizinhança solar — via t-SNE sobre parâmetros físico-químicos (Etapa 1, publicada) e diretamente sobre espectros brutos (Etapa 2, em andamento).

## Visão geral

Minha pesquisa de iniciação científica busca **encontrar e caracterizar estrelas anômalas na vizinhança solar**, cruzando astrometria de altíssima precisão do **Gaia Catalogue of Nearby Stars (GCNS)** com espectroscopia de alta resolução do **GALAH DR4**. O projeto é orientado pela Prof.ª Dr.ª Maria Luiza Linhares Dantas (Instituto de Astrofísica da Pontificia Universidad Católica de Chile) e conta com apoio do CNPq e do IFF.

O trabalho está dividido em duas etapas, uma já publicada e outra em andamento:

1. **Mapeamento não supervisionado via t-SNE em cima de parâmetros físico-químicos** (concluída, publicada) — reduz a dimensionalidade de temperatura, gravidade, metalicidade e cinemática de ~6.000 estrelas para encontrar agrupamentos e outliers, validando o método com métricas quantitativas e caracterizando a amostra com diagramas astrofísicos clássicos.
2. **Detecção de anomalias diretamente nos espectros brutos** (em andamento) — replicando a metodologia de Traven et al. (2017) para o GALAH, aplicando t-SNE, UMAP, HDBSCAN, Isolation Forest e autoencoders diretamente sobre os pixels dos espectros normalizados, sem passar pelos parâmetros já derivados pelo pipeline do survey.

> [!note] Nota sobre este texto
> Esta página reúne o estado atual da pesquisa a partir da minha documentação de trabalho (metodologia, revisão bibliográfica, notas de reunião). A Etapa 1 corresponde a resultados já publicados; a Etapa 2 é trabalho ativo, com resultados preliminares — tratem-se como tal.

---

## Os dados

| Catálogo | O que fornece | Tamanho |
|---|---|---|
| **GCNS** (Gaia Catalogue of Nearby Stars, Gaia DR3) | Astrometria e fotometria de altíssima precisão | ~330.000 estrelas a até 100 pc do Sol |
| **GALAH DR4** (Buder et al., 2025) | Espectros de alta resolução (R≈28.000), até 30 abundâncias químicas, parâmetros atmosféricos (Teff, log g, [Fe/H]), idades via isócronas PARSEC+COLIBRI, cinemática (Galpy + potencial de McMillan 2017) | ~1.017.000 estrelas |
| **Amostra cruzada (GCNS ∩ GALAH DR4)** | Estrelas com astrometria e espectroscopia completas | **~6.000 estrelas** |

O GALAH observa cada estrela em **4 bandas (CCDs)** do espectrógrafo HERMES, no Anglo-Australian Telescope: azul (4718–4903 Å), verde (5649–5873 Å), vermelho (6481–6739 Å) e infravermelho (7590–7890 Å), cada uma com 4.096 pixels — ou seja, cada espectro é um vetor de **16.384 dimensões** antes de qualquer redução.

### A ferramenta que construí para explorar os espectros

Para inspecionar espectros individuais durante a análise, desenvolvi um **visualizador web público de espectros do GALAH DR4** — mostra as 4 bandas de cada estrela (por `sobject_id`), com anotação das regiões de comprimento de onda associadas a cada grupo de elementos químicos (elementos de pico de ferro, captura de nêutrons, processo-α, CNO, Hα/Hβ, etc.):

![Visualizador de espectros GALAH DR4: as 4 bandas (azul, verde, vermelho, infravermelho) de uma estrela, com as regiões espectrais de cada grupo de elementos químicos marcadas na legenda.](assets/anomaly-detection/spectra-viewer.png)

---

## 1⃣ Etapa 1 — Mapeamento t-SNE em parâmetros físico-químicos (publicado)

Em vez de plotar diagramas prontos escolhidos à mão, alimentei o **t-SNE** diretamente com os parâmetros físico-químicos e cinemáticos de cada estrela (Teff, log g, [Fe/H], [Mg/Fe] e componentes de velocidade), deixando o algoritmo encontrar sozinho os agrupamentos, e só depois coloração pelos parâmetros conhecidos como teste de honestidade do método.

**Validação quantitativa** — testei uma grade de perplexidades de 15 a 90 e medi:
- **Divergência KL** — cai de forma constante com a perplexidade.
- **Trustworthiness** — entre ~0,89 e 0,95 (estável).
- **Continuity** — entre ~0,97 e 0,98 (estável).

Ambas as métricas de vizinhança ficaram altas e estáveis, indicando que a projeção 2D preserva bem tanto a estrutura local (perplexidade 30) quanto a global (perplexidade 50) do espaço original de alta dimensão. Em ambas, aparece um **pequeno subgrupo destacado**, com gradiente interno de metalicidade próprio — candidato a população anômala, que motivou a Etapa 2.

**Caracterização astrofísica** — usando a amostra completa: diagrama de Kiel (Teff × log g, colorido por [Fe/H], com isócronas PARSEC+COLIBRI), diagrama de Toomre (V × √(U²+W²), separando disco de halo) e diagrama de Tinsley-Wallerstein ([Mg/Fe] × [Fe/H], separando disco fino/espesso). A amostra é dominada por estrelas de sequência principal F/G/K, idade mediana ≈ 1,6 Gyr (0,1–14,8 Gyr), [Fe/H] mediano ≈ −0,19 dex. No diagrama de Toomre, **228 estrelas (3,8% da amostra) têm velocidade acima de 100 km/s** em relação ao Sol — candidatas a membros do halo, e a anomalia cinemática mais direta encontrada até agora.

Este trabalho foi publicado como:

> ANDRADE, P. H. R. et al. *Stellar properties and chemical features of the Gaia Catalogue of Nearby Stars observed by GALAH DR4*. Boletim da Sociedade Astronômica Brasileira, 2025.

E apresentado como pôster na **SAB 2025**, na **78ª Reunião Anual da SBPC (2026)** e nesta **Escola de Inverno do Observatório Nacional (2026)** — ver [[pt-br/resource/escolainverno/Apresentacao/MinhaPesquisa-VizinhancaSolar-tSNE|Apresentação de Pesquisa]] para o texto completo dessa apresentação.

---

## 2⃣ Etapa 2 — Anomalias direto nos espectros (em andamento)

O subgrupo destacado na Etapa 1 levantou uma pergunta: será que essa anomalia também aparece se eu não passar pelos parâmetros já derivados pelo pipeline do GALAH — ou seja, se eu deixar o algoritmo ver o **espectro bruto** diretamente? Essa é a pergunta que motiva a Etapa 2, replicando a metodologia de **Traven et al. (2017)**, que usou t-SNE sobre espectros do GALAH DR3 para identificar 10 categorias morfológicas de estrelas peculiares.

### Colunas de catálogo vs. pixels do espectro

Uma decisão metodológica central foi entender a diferença entre alimentar o t-SNE com **colunas do catálogo** (parâmetros já derivados, como na Etapa 1) ou com os **pixels brutos do espectro**:

- **Colunas do catálogo** (ex.: [Fe/H], [Mg/Fe] + ações orbitais $J_x$, $J_y$ — abordagem também usada por da Silva & Smiljanic 2023): custo computacional baixo, interpretação direta, mas o agrupamento fica **dependente dos modelos** que geraram essas colunas — um erro sistemático no pipeline (ex.: log g mal ajustado numa estrela fria) contamina o agrupamento.
- **Pixels do espectro** (o vetor de fluxo normalizado, dado bruto): agrupa por **similaridade morfológica da luz**, imune a erros de modelos de atmosfera estelar — melhor para achar binárias não catalogadas ou defeitos de instrumento, mas computacionalmente mais caro e sem "rótulo físico" pronto (é preciso inspecionar manualmente o que causa cada agrupamento).

### O que já foi testado

Rodei o t-SNE sobre os espectros normalizados (HDU 1 do FITS de cada estrela/CCD) em várias configurações, comparando com a abordagem por colunas:

![t-SNE sobre os espectros brutos (4 CCDs concatenados, ~5.900 estrelas), colorido por Teff, log g e [Fe/H] do catálogo — usado como teste de honestidade do agrupamento.](assets/anomaly-detection/tsne-espectros-brutos.png)

![Comparação de diferentes perplexidades do t-SNE sobre os espectros (dados de pixel), colorido pela temperatura efetiva — perplexidades mais altas suavizam a estrutura local em favor da global.](assets/anomaly-detection/tsne-comparacao-perplexidade.png)

Também testei quantitativamente a **estabilidade dos agrupamentos entre diferentes perplexidades**, usando o Índice de Rand Ajustado (ARI) para medir a concordância entre clusters obtidos em cada perplexidade, e rastreando como estrelas individuais "migram" de cluster ao variar esse hiperparâmetro:

![Concordância entre perplexidades (matriz ARI), score de estabilidade por estrela e migração de clusters entre perplexidade 5 e 30 — usado para escolher hiperparâmetros de forma menos arbitrária.](assets/anomaly-detection/validacao-perplexidade-ari.png)

### Comparação de técnicas de redução + clustering

Testei três combinações de redução de dimensionalidade + clustering sobre os espectros, com resultados preliminares:

| Combinação | Resultado observado |
|---|---|
| **UMAP + HDBSCAN** | Melhor equilíbrio até agora: 6 clusters, poucos outliers (~25) |
| **t-SNE + DBSCAN** | Mais granular, mas inicialmente super-segmentado (86+ clusters); melhorou ajustando ε |
| **PCA + HDBSCAN** | Muitos outliers (~4.469) — evidência de que a estrutura dos espectros é não linear e PCA não a captura bem |

Também testei dois detectores de anomalia diretamente sobre o embedding: **Isolation Forest** (contaminação assumida de 10%, inspirada na fração de espectros peculiares encontrada por Traven et al. 2017) e um **autoencoder** simples (MLPRegressor, codificador 4096→64, threshold no percentil 95 do erro de reconstrução) — ambos ainda em fase de validação cruzada contra as categorias morfológicas de Traven et al. (2017).

---

## Discussões e decisões (linha do tempo)

Resumo das principais decisões metodológicas tomadas ao longo do projeto, a partir das notas de reunião:

- **29/03/2026** — Definição da amostra (GCNS 330k, GALAH AllStars 980k, amostra cruzada 6k, espectros 24k) e primeiros testes de t-SNE sobre os espectros brutos, com problemas de inconsistência entre CCDs de uma mesma estrela.
- **30/03/2026** — Limpeza de dados espúrios (Teff/log g negativos), padronização (*standardization*) dos vetores de espectro antes do t-SNE.
- **11/04/2026** — Revisão cruzada dos papers de referência (GALAH DR4, Traven et al. 2017) para decidir entre usar os CCDs brutos ou o catálogo derivado (AllSpec).
- **04/05/2026** — Discussão sobre a diferença entre alimentar o t-SNE com colunas de catálogo vs. pixels do espectro (ver seção acima); construção e publicação do visualizador de espectros; classificação preliminar de estrelas por tipo espectral (OBAFGKM) a partir do Teff.

---

## Próximos passos

- Validar os clusters encontrados na Etapa 2 com **HDBSCAN sobre a projeção t-SNE**, comparando diretamente com as 10 categorias morfológicas de Traven et al. (2017).
- Cruzar os *outliers* espectrais da Etapa 2 com o subgrupo cinemático/químico destacado na Etapa 1, para verificar se são a mesma população.
- Comparar sistematicamente Isolation Forest, autoencoder e HDBSCAN como detectores de anomalia, com métricas de precisão/recall contra rótulos conhecidos.
- Complementar com mais diagnósticos de *chemical tagging* para testar se o grupo anômalo é de fato uma população química à parte.

---

## Bibliografia principal

- Traven et al. (2017) — *The GALAH survey: classification and diagnostics with t-SNE reduction of spectral information* — metodologia-base da Etapa 2.
- Buder et al. (2025) — GALAH DR4.
- Gaia Collaboration et al. (2021) — Gaia Catalogue of Nearby Stars.
- da Silva & Smiljanic (2023) — t-SNE em espaço quimiodinâmico (base para a comparação colunas vs. pixels).
- Hughes et al. (2022) — descoberta de estrelas extremamente pobres em metais no GALAH DR3 via ML supervisionado.
- Pettee et al. (2023) — detecção fracamente supervisionada de streams estelares no Gaia (CWoLa).
- Ver [Artigos](pt-br/research/anomaly-detection/articles) para as anotações completas de leitura de todos os papers usados nesta pesquisa.

---

## Referências e correlatos

- [[pt-br/resource/escolainverno/Apresentacao/MinhaPesquisa-VizinhancaSolar-tSNE|Apresentação de Pesquisa]] — texto de preparação para apresentar a Etapa 1 (Banner SBPC 2026 e Banner desta Escola de Inverno).
