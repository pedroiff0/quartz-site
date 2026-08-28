---
publish: false
title: Aula 12 — Espaço de Ações e Diagramas de Arqueologia Galáctica
created: 2026-07-25 12:36
modified: 2026-08-27 21:59
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - dinamica-estelar
  - espaco-de-acoes
  - pratica
cssclasses:
  - page-grid
  - center-images
encrypted: true
discipline: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
content: Aula prática (APOGEE DR19) — excentricidade, pericentro/apocentro, diagrama de Toomre, o espaço (E, Lz) e o "diamante" de ações (JR, Jz, Lz) para separar populações estelares e identificar acréscimos
professor: Hélio Dotto Perottoni
---

# 🎯 Aula 12 — Espaço de Ações e Diagramas de Arqueologia Galáctica

> [!note] Resumo
> Aula prática que aplica os conceitos de integrais de movimento (Aula 09) a mais de um milhão de estrelas reais do catálogo **APOGEE DR19**, com parâmetros orbitais já pré-calculados: excentricidade, pericentro/apocentro, $Z_{max}$, o diagrama de Toomre, e o espaço $(E, L_z)$ — a ferramenta mais usada da arqueologia galáctica moderna para separar populações estelares e caçar evidências de fusões antigas.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** notebook oficial da disciplina — "Análise de Parâmetros Orbitais — APOGEE DR19" (`master_final_APOGEEDR19.fits`, 1.074.401 estrelas)

---

## 🎯 Visão geral

O catálogo usado aqui já vem com os parâmetros orbitais de cada estrela **pré-computados** (por integração de órbitas, como nas Aulas 10-11): pericentro, apocentro, excentricidade, $Z_{max}$, momento angular $L_z$, energia orbital $E$, e as ações $J_R$, $J_z$. A aula é, portanto, sobre **interpretar** esse espaço de parâmetros — não sobre recalculá-lo — usando os diagramas clássicos da dinâmica galáctica moderna.

## 📈 Excentricidade, pericentro e apocentro

A **excentricidade** orbital ($e\approx0$: quase circular; $e\to1$: muito alongada) tem uma distribuição populacional informativa por si só — a maior parte das estrelas do disco tem excentricidade baixa, com uma cauda estendendo-se a valores altos (halo). O gráfico $R_{peri}$ vs. $R_{apo}$ mostra a mesma informação de outro ângulo: sobrepondo curvas de excentricidade constante,

$R_{apo} = R_{peri}\,\frac{1+e}{1-e}$

fica visualmente claro que órbitas mais excêntricas têm maior separação relativa entre pericentro e apocentro — exatamente a definição geométrica de excentricidade orbital aplicada a dados reais.

## 🗺️ Diagrama de Toomre e o plano $V_\phi$–$V_R$

O **diagrama de Toomre** ($V_\phi$ vs. $\sqrt{V_R^2+V_Z^2}$) é uma das ferramentas mais usadas para separar populações por cinemática — o mesmo tipo de diagrama já visto na Escola de Inverno e usado na pesquisa de vizinhança solar deste site. Curvas de velocidade total constante centradas em $V_\phi=220\,$km/s (a velocidade circular do LSR, Aula 08) demarcam regiões de referência para disco fino ($\sim$70 km/s), disco espesso ($\sim$180 km/s) e halo ($\sim$250 km/s).

O plano $V_\phi$ vs. $V_R$ complementa essa visão: o disco fino aparece concentrado perto de $V_\phi\sim220\,$km/s com baixa dispersão radial; o halo mostra dispersão de velocidades muito maior e rotação média menor; estrelas **retrógradas** (que orbitam a Galáxia no sentido oposto ao disco) aparecem com $V_\phi<0$ — um sinal cinemático forte de origem acretada, já que praticamente nenhuma estrela nascida in situ no disco deveria ter esse comportamento.

## ⚖️ O espaço $(E, L_z)$: a ferramenta central da arqueologia moderna

Energia orbital $E$ e momento angular azimutal $L_z$ são, em boa aproximação, **integrais de movimento conservadas** (Aula 09) — por isso, estrelas que se originaram no mesmo evento de acréscimo (mesma galáxia satélite, dissolvida há bilhões de anos) tendem a permanecer **agrupadas** nesse espaço, mesmo depois de suas posições espaciais terem se espalhado completamente pela Galáxia. É o princípio por trás da busca por subestruturas dinâmicas: disco (alto $L_z$, órbitas quase circulares, baixa energia) e halo (baixo $L_z$, órbitas excêntricas, alta energia) ocupam regiões bem distintas desse plano, e colorir os mesmos pontos por excentricidade ou por raio galactocêntrico revela ainda mais estrutura interna.

> [!info] O paper fundador: Helmi et al. (1999)
> A ideia de usar o espaço de integrais de movimento para encontrar "fósseis" de fusões antigas remonta a Helmi, White, de Zeeuw & Zhao (1999, _Nature_ 402, 53) — que mostraram que restos (_debris streams_) de uma fusão antiga permanecem agrupados no espaço de integrais de movimento na vizinhança solar, mesmo completamente misturados espacialmente. É a base conceitual direta de todo diagrama $(E,L_z)$ usado hoje para caçar acréscimos na Via Láctea.

## 💎 O "diamante" de ações: $J_R$, $J_z$ e $L_z$ normalizados

Uma forma mais recente e compacta de visualizar o mesmo tipo de informação é normalizar as três ações ($J_R$, $J_z$, $L_z$) pela soma de seus módulos e projetá-las num diagrama em forma de **diamante**, com eixos e vértices interpretáveis fisicamente:

- **Vértices** (prógrado/retrógrado, radial, polar): órbitas dominadas por uma única ação.
- **Diagonais** ("circular", $J_R=0$; "no plano", $J_z=0$): casos limites geometricamente simples.

Esse tipo de diagrama comprime toda a informação dinâmica de uma órbita (forma, orientação, inclinação) num único ponto num espaço limitado e de fácil comparação visual entre populações — um desenvolvimento natural do mesmo espírito do espaço $(E,L_z)$, mas usando as três ações em vez de duas integrais de movimento.

---

## 📌 Conceitos-chave

- **Excentricidade orbital ($e$):** $R_{apo}=R_{peri}(1+e)/(1-e)$ — mede o alongamento da órbita; halo tem $e$ tipicamente alto, disco fino tipicamente baixo.
- **Diagrama de Toomre:** $V_\phi$ vs. $\sqrt{V_R^2+V_Z^2}$, com curvas de referência para disco fino/espesso/halo centradas na velocidade circular do LSR.
- **Estrelas retrógradas ($V_\phi<0$ ou $L_z<0$):** assinatura cinemática direta de origem acretada, não in situ.
- **Espaço $(E, L_z)$:** as duas integrais de movimento mais usadas para identificar subestruturas de acréscimo — estrelas do mesmo evento de fusão permanecem agrupadas aqui, mesmo espacialmente misturadas.
- **Diamante de ações $(J_R, J_z, L_z)$:** visualização normalizada e compacta da forma/orientação orbital, complementar ao espaço $(E,L_z)$.

## 🔗 Referências e correlatos

- Helmi, White, de Zeeuw & Zhao (1999) — _Debris streams in the solar neighbourhood as relics from the formation of the Galaxy_, Nature 402, 53 (bibcode `1999Natur.402...53H`) — paper fundador do uso do espaço de integrais de movimento
- Outras leituras citadas nos slides originais (bibcodes ADS, sem título extraído): `2022ApJ...935L..22T`, `2023A&A...670L...2D`, `2023ApJ...946...66L`, `2023MNRAS.518.6200B`, `2024MNRAS.532.4389D`, `2021A&A...654A..15B`
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-09-orbitas-potenciais-e-integrais-de-movimento|Aula 09 — Órbitas, Potenciais e Integrais de Movimento]] — base teórica de $E$, $L_z$ e das ações usadas aqui
- [[pt-br/resource/curso-on/aula-10-integracao-de-orbitas-com-galpy|Aula 10 — Integração de Órbitas com galpy]] — como esses mesmos parâmetros orbitais são calculados a partir de dados 6D individuais
- [[pt-br/resource/escolainverno/apresentacao/minhapesquisa-vizinhancasolar-tsne|Apresentação de Pesquisa — Vizinhança Solar com t-SNE]] — o mesmo diagrama de Toomre usado aqui aparece na minha própria pesquisa para separar disco de halo
- [[pt-br/resource/curso-on/aula-13-nucleossintese-e-enriquecimento-quimico|Aula 13 — Nucleossíntese Estelar e Enriquecimento Químico]] — a dinâmica orbital vista aqui volta o foco para a química que originou essas populações
