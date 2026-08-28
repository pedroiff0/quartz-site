---
publish: false
title: Aula 04 — Espectroscopia e Metalicidade
created: 2026-07-23 12:36
modified: 2026-08-27 12:36
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - espectroscopia
  - metalicidade
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula04
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: Leis de Kirchhoff, formação de linhas espectrais, a descoberta do hélio e a notação de metalicidade [Fe/H]
professor: Hélio Dotto Perottoni
---

# 🔭 Aula 04 — Espectroscopia e Metalicidade

> [!note] Resumo
> A espectroscopia é o fundamento indispensável da astrofísica moderna: revela composição química, movimento e distância a partir de como a matéria emite e absorve radiação. Esta aula percorre a física da formação de linhas espectrais e chega à notação \[Fe/H], usada em toda a arqueologia galáctica para medir metalicidade.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni

---

## 🌈 Espectroscopia moderna

A espectroscopia associa as propriedades observadas nos espectros (linhas espectrais e suas intensidades) a fenômenos físicos que ocorrem em ambientes extraterrestres — transições eletrônicas de diferentes energias em estrelas, nebulosas, planetas etc. Foi essa técnica que permitiu a **Cecilia Payne** descobrir/interpretar a composição química do Sol (ver abaixo). O aparato básico de um espectrógrafo é: fonte → fenda → prisma (hoje, rede de difração) → CCD.

## 🔎 A descoberta do hélio

Uma sequência de marcos no início do séc. XIX/XX:

- **William Wollaston (1802):** descoberta de linhas escuras no espectro do Sol.
- **Joseph Fraunhofer (1814):** catálogo de ~570 linhas escuras — o "espectro de Fraunhofer", nomenclatura usada até hoje.
- **Henry Draper (1872):** pioneiro em espectroscopia estelar.
- **Jules Janssen (1868):** observa uma linha escura não identificada no espectro solar.
- **Norman Lockyer (1868):** identifica essa mesma linha e propõe que ela seria devida a um elemento até então desconhecido — o **hélio**, batizado antes mesmo de ser isolado em laboratório na Terra.

## ⚖️ Leis de Kirchhoff

1. Sólidos, líquidos ou gases muito densos, quando aquecidos, produzem **espectros contínuos**.
2. Gases pouco densos, quando aquecidos, produzem **espectros de emissão**.
3. Gases pouco densos na frente de uma fonte de espectro contínuo produzem **espectros de absorção** — desde que o gás seja mais frio que a fonte.

Cada elemento químico possui um conjunto único e característico de linhas — é isso que permite identificar um elemento através de seu espectro.

## ⚛️ Formação de linhas espectrais

Um elétron ligado a um núcleo tem um **estado fundamental** (energia mínima) e uma **energia de ionização** (acima da qual deixa de estar ligado — o átomo torna-se um íon). Entre esses dois limites, o elétron só pode ocupar **níveis discretos de energia** bem definidos. A energia do fóton emitido/absorvido numa transição é:

$\Delta E = h\nu = \frac{hc}{\lambda} = E_0\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$

onde $E_0 = -13{,}6\,$eV é o potencial de ionização do hidrogênio (fórmula de Rydberg).

O desenvolvimento da Classificação de Harvard (~1910–1920) coincide com o **modelo atômico de Bohr**, que explica por que a intensidade das linhas de H varia com a temperatura estelar:

- **Baixas temperaturas:** o átomo de H fica tipicamente no estado fundamental → linhas de H mais **fracas** (menor frequência de transições).
- **Temperaturas intermediárias:** maior probabilidade do elétron ocupar o primeiro estado excitado (nível 2) → ocorrem as transições da **série de Balmer**, detectáveis no visível. É por isso que **estrelas tipo A** têm as linhas de H mais **fortes** de toda a sequência espectral.
- **Altas temperaturas:** acima de $\sim$10 mil K, o hidrogênio ioniza-se rapidamente → menos H neutro → linhas mais fracas novamente. Por isso, estrelas tipo O e B têm linhas de H mais fracas que as de tipo A.

## 🧪 Composição das estrelas: Cecilia Payne

O entendimento dos processos de excitação/ionização atômica permitiu calcular a intensidade das linhas espectrais em função da temperatura — trabalho de **Cecilia Payne**, que demonstrou que as quantidades de **H e He são muito maiores** do que qualquer outro elemento nas estrelas (e, por extensão, no Universo). No início do séc. XX, a qualidade dos dados ainda não permitia distinguir diferenças finas de composição química entre estrelas; hoje, espectros de alta resolução (mais pixels por comprimento de onda) permitem determinações detalhadas — fundamentais para entender a evolução estelar e a produção dos elementos da tabela periódica.

Comparando espectros de estrelas de tipo espectral semelhante, um aumento na quantidade/intensidade de linhas indica **diminuição** na quantidade de elementos mais pesados que H e He — os **metais**, na acepção astronômica: literalmente qualquer elemento além de hidrogênio e hélio. Assume-se, em geral, que a composição da superfície observada reflete a composição original da nuvem de gás da qual a estrela se formou.

## 🔢 Metalicidades e abundâncias

Os primeiros modelos de evolução estelar consideravam apenas três componentes de abundância: hidrogênio ($X$), hélio ($Y$) e metais ($Z$), com $X+Y+Z=1$. Espectroscopicamente, assume-se $Z \propto n(\text{Fe})$, dando origem à notação padrão:

$[\text{Fe/H}] = \log_{10}\left(\frac{N_{Fe}/N_H}{(N_{Fe}/N_H)_\odot}\right)$

De forma equivalente, define-se uma razão de abundância entre dois elementos quaisquer, $[X/Y]$.

### Interpretando \[Fe/H]

| Valor | Interpretação |
|---|---|
| $[\text{Fe/H}] > 0$ | _metal-rich_ — mais rica em metais que o Sol |
| $[\text{Fe/H}] < 0$ | _metal-poor_ — mais pobre que o Sol |
| $[\text{Fe/H}] = -1$ | 10× menos ferro que o Sol |
| $[\text{Fe/H}] = -2$ | 100× menos ferro |
| $[\text{Fe/H}] = -3$ | 1000× menos ferro |
| $[\text{Fe/H}] = -4$ | 10000× menos ferro |

\[Beers & Christlieb 2005] é a referência clássica para a busca e caracterização de estrelas extremamente pobres em metais — os fósseis mais antigos acessíveis da arqueologia galáctica.

### Metalicidade fotométrica

Também é possível estimar metalicidade a partir de **fotometria** (cores), sem espectroscopia — uma alternativa mais barata para grandes levantamentos, ainda que menos precisa \[Babusiaux et al. 2018].

---

## 📌 Conceitos-chave

- **Leis de Kirchhoff:** espectro contínuo (fonte densa quente) vs. emissão (gás quente rarefeito) vs. absorção (gás frio rarefeito na frente de fonte contínua).
- **Séries de Balmer:** transições do H visíveis no óptico, responsáveis pelo pico de intensidade das linhas de H em estrelas tipo A.
- **\[Fe/H]:** notação logarítmica-relativa ao Sol; base quantitativa de toda a arqueologia química da Galáxia.

## 🔗 Referências e correlatos

- Beers & Christlieb (2005) — estrelas pobres em metais
- Babusiaux et al. (2018) — metalicidade fotométrica com dados Gaia
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-03-magnitudes-cores-e-classificacao-espectral|Aula 03 — Magnitudes, Cores e Classificação Espectral]]
- [[pt-br/resource/curso-on/aula-05-avermelhamento-extincao-e-imf|Aula 05 — Avermelhamento, Extinção e IMF]]
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01|Escola de Inverno — Arqueologia Galáctica, Aula 01]] — notação \[Fe/H] e \[α/Fe] aplicada à separação de populações
- [[pt-br/research/anomaly-detection|Detecção de Anomalias em Dados do Gaia]] — minha pesquisa usa espectros GALAH DR4 processados com os mesmos princípios vistos aqui
