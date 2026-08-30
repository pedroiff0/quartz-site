---
publish: true
encrypted: true
title: 00-Resumo-Escola-de-Inverno
discipline: Resumo Geral
content: Panorama de tudo o que foi visto na Escola de Inverno do Observatório Nacional (ON) 2026
professor:
created: 2026-07-22 13:34
modified: 2026-08-27 21:59
tags:
  - escola-de-inverno-on
  - resumo
cssclasses:
  - page-grid
  - center-images
---
# 🌌 Resumo Geral — Escola de Inverno do Observatório Nacional (2026)

> [!info] Sobre este arquivo
> Panorama de todas as áreas cobertas até agora na Escola de Inverno. Cada seção resume a nota detalhada correspondente — clique nos links para ver a aula completa, com explicações, fórmulas e imagens.

---

## 🗺️ Mapa geral das disciplinas

| Área | Professor(a) | Do que trata | Nota completa |
|---|---|---|---|
| 🌐 Aglomerados de Galáxias | Rogério Monteiro-Oliveira | As maiores estruturas gravitacionalmente ligadas do Universo | [260720-Aglomerados-Aula01](260720-Aglomerados-Aula01) |
| ⭐ Arqueologia Galáctica | — | História da Via Láctea lida na composição química das estrelas | [260720-Arqueologia-Galactica-Aula01](260720-Arqueologia-Galactica-Aula01) |
| 💻 Computação de Alto Desempenho | Fernando Roig | Programação paralela (OpenMP/MPI) para ciência de dados | [260721-Computacao-Aula01](260721-Computacao-Aula01) |
| 🌀 Cosmologia | Carlos Bengaly | O modelo padrão ΛCDM e suas sondas observacionais | [260721-Cosmologia-Aula01](260721-Cosmologia-Aula01) |
| 👻 Neutrinos (Palestra) | Gabriel Rodrigues | Física de partículas + cosmologia dos neutrinos | [260720-Neutrinos](260720-Neutrinos) |
| 🪐 Ciências Planetárias | — | Sistema Solar: inventário, arquitetura e dinâmica orbital | [260720-Planetaria-Aula01](260720-Planetaria-Aula01), [260721-Planetaria-Aula02](260721-Planetaria-Aula02) |

---

## 🧵 O fio condutor: uma história em escalas

Um jeito de amarrar todas as aulas é pensar em **escala**, do menor para o maior:

1. **Partículas fundamentais** (Neutrinos): quarks, léptons e bósons formam toda a matéria — inclusive os neutrinos, partículas quase fantasmas que carregam massa e cruzam o Universo sem interagir quase nunca.
2. **Estrelas** (Arqueologia Galáctica): fundem elementos leves em pesados (nucleossíntese) e, ao morrer, espalham esses elementos pelo espaço — cada átomo do seu corpo mais pesado que hidrogênio "nasceu" dentro de uma estrela ou na colisão de estrelas de nêutrons.
3. **Sistemas planetários** (Ciências Planetárias): nuvens de gás e poeira ao redor de uma estrela recém-formada colapsam, giram e se organizam em planetas, seguindo as leis de Kepler e da gravitação.
4. **Galáxias e aglomerados de galáxias** (Aglomerados): a maior escala onde a gravidade "venceu" a expansão do Universo e formou estruturas ligadas — dominadas por matéria escura, não por estrelas.
5. **O Universo como um todo** (Cosmologia): acima de ~100 Mpc, tudo se torna estatisticamente uniforme (homogêneo e isotrópico), e o que resta estudar é sua composição global (~68% energia escura, ~27% matéria escura, ~5% matéria bariônica) e sua expansão acelerada.

Por trás de tudo isso está a **Computação de Alto Desempenho**: a ferramenta que permite simular numericamente desde a formação de um único planeta até a evolução de toda a teia cósmica.

---

## 🔑 Grandes ideias que aparecem repetidamente

> [!tip] Temas recorrentes entre as aulas
> - **Matéria escura:** aparece em Aglomerados (Zwicky/Coma, lentes gravitacionais), em Cosmologia (CDM, candidatos WIMP/áxion) e em Neutrinos (neutrinos como matéria escura "quente", mas insuficiente).
> - **Supernovas:** conectam Arqueologia Galáctica (nucleossíntese, origem dos elementos) e Cosmologia (supernovas Ia como "velas padrão" para medir a expansão do Universo).
> - **Teorema do virial e equilíbrio:** usado tanto para "pesar" aglomerados de galáxias quanto para entender o equilíbrio hidrostático de estrelas e do gás intra-aglomerado.
> - **Simulações numéricas:** a Millennium Run (Aglomerados), simulações de N-corpos (Planetária) e a própria disciplina de HPC mostram que boa parte da astrofísica moderna depende de supercomputadores.
> - **Ondas gravitacionais:** aparecem na linha do tempo da Cosmologia (2016+) e como mecanismo de nucleossíntese pesada (processo-r) em Arqueologia Galáctica.

---

## 📚 Resumo por área

### 🌐 Aglomerados de Galáxias
Os aglomerados são os maiores objetos já **virializados** do Universo ($10^{14}$–$10^{15}\,M_\odot$), compostos majoritariamente por **matéria escura (~80%)**, com gás quente (ICM, ~15%) e galáxias (~5%). Zwicky, em 1933, foi o primeiro a notar essa discrepância de massa usando o **teorema do virial** no Aglomerado de Coma. Hoje detectamos aglomerados por 4 vias complementares: óptico (galáxias, sequência vermelha), raio-X (gás do ICM), micro-ondas (efeito Sunyaev-Zel'dovich) e lentes gravitacionais fracas (mapeando a matéria escura diretamente).

### ⭐ Arqueologia Galáctica
Estrelas são classificadas pela sequência espectral **OBAFGKM** (temperatura decrescente). Ao longo da vida e, principalmente, ao morrer (supernovas, nebulosas planetárias, colisões de estrelas de nêutrons), as estrelas produzem e espalham elementos químicos pelo espaço — os processos **s** (lento, em estrelas AGB) e **r** (rápido, em fusões de estrelas de nêutrons) explicam a origem de praticamente toda a tabela periódica além do ferro. Comparando a composição química de estrelas antigas e novas (populações I, II e III), reconstruímos a história de formação da Via Láctea.

### 💻 Computação de Alto Desempenho
Para simular os fenômenos acima (N-corpos, hidrodinâmica, aprendizado de máquina), astrônomos usam **clusters de supercomputadores**. Dois paradigmas principais: **OpenMP** (memória compartilhada, paraleliza laços dentro de um mesmo nó) e **MPI** (memória distribuída, troca mensagens entre muitos nós via broadcast/reduce/scatter/gather).

### 🌀 Cosmologia
O modelo padrão **ΛCDM** descreve um Universo composto por ~68% energia escura, ~27% matéria escura fria e ~5% matéria comum. Ele é testado por três sondas principais: **supernovas Ia** (expansão acelerada, descoberta em 1998), a **Radiação Cósmica de Fundo** (fóssil térmico do Universo primordial, a 2,725 K) e a **Estrutura em Grande Escala** (a teia cósmica de filamentos e aglomerados).

### 👻 Neutrinos
Previstos por Pauli (1930) para salvar a conservação de energia no decaimento beta, os neutrinos só foram detectados em 1956. Em 1998, a descoberta da **oscilação de neutrinos** provou que eles têm massa — um dado que hoje é comparado diretamente com limites obtidos da própria cosmologia (RCF + estrutura em grande escala), unindo física de partículas e o Universo em grande escala.

### 🪐 Ciências Planetárias
O Sistema Solar se formou a partir do colapso gravitacional de uma nuvem molecular, passando por um disco protoplanetário. Sua dinâmica é regida pela gravitação newtoniana e pelas **leis de Kepler**, com órbitas descritas por 6 elementos orbitais constantes (no problema de 2 corpos). Modelos dinâmicos como o **Grand Tack** e o **modelo de Nice** explicam características hoje observadas, como a baixa massa de Marte e o Bombardeio Intenso Tardio da Lua.

---

## 🔗 Notas completas
- [[260720-Aglomerados-Aula01]]
- [[260720-Arqueologia-Galactica-Aula01]]
- [[260721-Computacao-Aula01]]
- [[260721-Cosmologia-Aula01]]
- [[260720-Neutrinos]]
- [[260720-Planetaria-Aula01]] · [[260721-Planetaria-Aula02]]

> [!note] Próximos passos
> Este resumo e as notas de aula serão atualizados conforme novas aulas acontecem e conforme os **PDFs oficiais das aulas** ficarem disponíveis — o que deve permitir preencher os pontos ainda marcados como "a preencher" e corrigir/expandir qualquer detalhe.
