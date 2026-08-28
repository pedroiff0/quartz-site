---
publish: false
title: Aula 15 — Espectroscopia e Fotometria em Grandes Levantamentos
created: 2026-07-25 12:36
modified: 2026-08-27 21:59
published: 2026-07-26T11:33:09.987-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - levantamentos
  - big-data
cssclasses:
  - page-grid
  - center-images
encrypted: true
discipline: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
content: Panorama histórico dos grandes levantamentos astronômicos — de catálogos visuais e placas fotográficas aos surveys digitais all-sky (SDSS, 2MASS, DES, Euclid, LSST) — e comparação dos principais levantamentos espectroscópicos usados em arqueologia galáctica (Gaia, Gaia-ESO, APOGEE, GALAH, LAMOST, DESI, entre outros)
professor: Hélio Dotto Perottoni
---

# 🔭 Aula 15 — Espectroscopia e Fotometria em Grandes Levantamentos

> [!note] Resumo
> Um panorama de como a astronomia observacional foi da contagem manual de objetos difusos (Messier, séc. XVIII) aos levantamentos digitais que hoje sustentam a arqueologia galáctica — fotografia (Carte du Ciel, POSS), a virada digital (SDSS), surveys all-sky (2MASS, WISE, DES, Euclid, LSST) e, por fim, um comparativo direto dos principais levantamentos espectroscópicos (Gaia, APOGEE, GALAH, LAMOST, DESI e outros) usados para reconstruir a história química e dinâmica da Via Láctea.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** slides oficiais da disciplina — "Espectroscopia e Fotometria estelar em grandes levantamentos"

---

## 📜 Dos catálogos visuais à era fotográfica

Os primeiros grandes catálogos eram compilações visuais: o **Catálogo Messier** (séc. XVIII, ~110 objetos difusos, originalmente pensado para não confundir nebulosas com cometas), o **New General Catalogue** (NGC, Dreyer 1888, ~7.800 nebulosas e aglomerados) e o **Index Catalogue** (IC, Dreyer 1895-1908, mais de 13 mil objetos, já incorporando descobertas por placa fotográfica).

A **era fotográfica** ampliou drasticamente a escala: o **Carte du Ciel** (1887), um projeto colaborativo internacional com mais de 22 mil placas de vidro, tentou (sem nunca concluir) mapear fotograficamente todo o céu; o **Palomar Observatory Sky Survey (POSS)**, entre as décadas de 1950-1990, tornou-se o atlas fotográfico de referência do hemisfério norte, servindo de base para inúmeros catálogos e digitalizações posteriores.

## 💻 A virada digital: SDSS e a primeira geração de CCD

Nos anos 1990, surveys baseados em CCD (DMS, CFRS, LCRS, ESP, entre outros) já exploravam estrutura em grande escala e evolução de galáxias, mas foi o **Sloan Digital Sky Survey (SDSS)**, iniciado em 2000, que marcou a transição definitiva: fotometria digital em 5 bandas (_ugriz_), espectroscopia automatizada, pipeline totalmente digital e banco de dados público — mais de 500 milhões de objetos fotométricos, milhões de espectros, centenas de TB de dados. É o modelo (arquitetura de pipeline + acesso público) que praticamente todo levantamento posterior seguiu.

## 🛰️ Surveys fotométricos all-sky e de grande campo

| Survey | Cobertura/banda | Escala | Papel principal |
|---|---|---|---|
| **2MASS** | Céu inteiro, infravermelho próximo (J, H, Ks) | >470 milhões de fontes | Primeiro grande survey homogêneo no IV — penetra poeira que bloqueia o óptico |
| **WISE** | Espacial, infravermelho médio | Centenas de milhões de objetos | Anãs marrons, galáxias poeirentas, estrutura galáctica |
| **Pan-STARRS** | ~3/4 do céu, múltiplas bandas ópticas | Bilhões de fontes | Consolidou _time-domain astronomy_ (transientes, variáveis) — ponte SDSS→LSST |
| **APASS** | Praticamente all-sky, bandas BVgri | Dezenas de milhões de estrelas | Referência de **calibração fotométrica** entre telescópios diferentes |
| **DES** | Hemisfério sul, óptico profundo | — | Halo tênue: correntes estelares, galáxias anãs, subestruturas de acréscimo |
| **Euclid** | ~15.000 deg², óptico+IV próximo (espacial) | VIS ~24,5 AB / Y,J,H ~24 AB | Focado em energia/matéria escura, mas produz dado estelar/galáctico de altíssima qualidade |
| **J-PLUS / S-PLUS** | Norte / sul, 12 filtros largos+estreitos | ~9.300 deg² (S-PLUS) | Espectrofotometria multibanda de baixo custo |
| **J-PAS** | ~8.500 deg², 56 filtros estreitos | — | Redshifts fotométricos quase espectroscópicos |
| **LSST (Rubin)** | ~18.000 deg², _ugrizy_, 10 anos | ~20 bi galáxias, >10 bi estrelas da MW, halo até ~400 kpc | ~20 TB/noite, >100 PB no total — o maior survey óptico já concebido |

> [!info] O que o DES revelou sobre o halo
> A combinação de profundidade + área do DES permitiu mapear populações estelares muito tênues do halo, revelando **correntes estelares**, **galáxias anãs satélites** e estruturas resultantes de eventos de acréscimo — evidência direta de que o halo estelar da Via Láctea é feito de múltiplas subestruturas fossilizadas da formação hierárquica da Galáxia (o mesmo tema da Escola de Inverno).

## ⚠️ Cuidados ao analisar dados fotométricos

Nem todo objeto num catálogo fotométrico é igualmente confiável. Pontos de atenção recorrentes: comportamento nas extremidades **faint/bright** da distribuição; a relação entre magnitude e seu erro (_mag_ vs. _emag\_err_, que tipicamente cresce nas bordas); e a **completeza** do catálogo — comprometida por limites de detecção/seleção, viés contra objetos de baixo brilho superficial, _blending_/_crowding_ (fontes sobrepostas em regiões densas) e extinção interestelar (Aula 05 do curso-on).

## 🌈 Comparativo dos principais levantamentos espectroscópicos

| Survey | Resolução | Banda | Telescópio/instrumento | Nº de objetos | Objetivo principal |
|---|---|---|---|---|---|
| **Gaia RVS** | Média (R~11.500) | NIR (845-872 nm) | Satélite Gaia (L2), DR3 | 33.812.183 | Astrometria/fotometria de céu todo + o maior catálogo de velocidade radial |
| **Gaia-ESO** | Média/alta (GIRAFFE~20.000, UVES~50.000) | Óptico (370-900 nm) | VLT, DR5 | 114.916 | Parâmetros astrofísicos e abundâncias homogêneas em alta resolução |
| **APOGEE** | Alta (R~22.500) | IV próximo (1,51-1,70 μm) | Las Campanas (SDSS-S), DR19 | 1.074.401 | Formação e evolução da Via Láctea |
| **BOSS** | Baixa (R~2.000) | Óptico (3650-9500 Å) | Telescópio Sloan (SDSS-N/V) | 923.306 | Originalmente BAO, hoje parte dos _Milky Way Mappers_ |
| **SEGUE 1/2** | Baixa (R~1.800) | Óptico (3900-9000 Å) | SDSS, DR7-DR12 | 358.958 | Cinemática e populações da Via Láctea e seu halo |
| **GALAH** | Alta (R~28.000) | Óptico (470-790 nm) | HERMES, DR4 | 1.085.520 | História químico-dinâmica da Via Láctea |
| **RAVE** | Média (R~7.500) | IV próximo (8410-8795 Å) | UK Schmidt (AAO), DR6 | 518.387 | Evolução galáctica via anãs/gigantes homogêneas |
| **LAMOST** | Baixa/média (R~1.800/7.500) | Óptico (3700-9100 Å) | LAMOST, DR11 | 7.898.024 (LRS) + 2.594.070 (MRS) | Arqueologia galáctica, estrutura da Via Láctea, aglomerados |
| **DESI** | Baixa (R~2.000-5.500) | Óptico (3600-9824 Å) | Mayall/Kitt Peak, DR1 | 6.372.607 | Formação, acréscimo e distribuição de disco espesso/halo |

> [!warning] O que observar antes de confiar num espectro
> A qualidade espectroscópica depende de três fatores que afetam diretamente velocidades, abundâncias e parâmetros estelares derivados: **resolução espectral** $R=\lambda/\Delta\lambda$ (baixa resolução mistura linhas próximas), **cobertura espectral** (algumas linhas diagnósticas importantes podem simplesmente estar fora da faixa observada) e **razão sinal/ruído** (S/N baixo compromete tanto abundâncias quanto velocidades radiais). Catálogos também trazem _flags_ de qualidade que sinalizam medidas pouco confiáveis — sempre vale checá-las antes de usar os dados "brutos".

---

## 📌 Conceitos-chave

- **SDSS como ponto de virada:** primeiro survey a combinar fotometria digital multibanda, espectroscopia automatizada e banco de dados público num pipeline unificado — o modelo seguido por praticamente todo survey posterior.
- **Trade-off resolução vs. cobertura/objetos:** levantamentos de alta resolução (GALAH, APOGEE, Gaia-ESO) sacrificam número de objetos por precisão em abundâncias; levantamentos de baixa resolução (SEGUE, BOSS, DESI, LAMOST-LRS) trocam precisão por volume.
- **DES e o halo fossilizado:** profundidade fotométrica revelou que o halo da Via Láctea é feito de subestruturas (correntes, satélites) — evidência observacional direta de formação hierárquica.
- **Completeza de catálogo:** nunca assumir que um catálogo fotométrico é uma amostra não enviesada — limites de detecção, _blending_ e extinção sempre introduzem seletividade.
- **$R=\lambda/\Delta\lambda$:** a resolução espectral que determina se linhas espectrais próximas podem ser distinguidas — crítica para qualquer medida de abundância ou velocidade radial.

## 🔗 Referências e correlatos

- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-05-avermelhamento-extincao-e-imf|Aula 05 — Avermelhamento, Extinção e IMF]] — extinção interestelar como uma das fontes de incompletude discutidas aqui
- [[pt-br/resource/curso-on/aula-12-espaco-de-acoes-apogee|Aula 12 — Espaço de Ações e Diagramas de Arqueologia Galáctica]] — usa exatamente o catálogo APOGEE DR19 apresentado nesta tabela
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01|Escola de Inverno — Arqueologia Galáctica, Aula 01]] — o levantamento GALAH, aqui comparado a seus pares, é a base de dados da minha própria pesquisa
- [[pt-br/research/anomaly-detection|Detecção de Anomalias em Dados do Gaia]] — minha pesquisa combina exatamente GALAH DR4 e astrometria Gaia, dois dos levantamentos desta tabela
- [[pt-br/resource/curso-on/aula-16-determinacao-de-idades-estelares|Aula 16 — Métodos de Determinação de Idades Estelares]] — os dados espectroscópicos/fotométricos vistos aqui alimentam diretamente os métodos de idade discutidos a seguir
