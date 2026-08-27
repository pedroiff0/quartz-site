---
publish: true
title: Simulando o Impacto de Satélites em Observações Astronômicas
created: 2024-03-06
modified: 2026-07-26T10:19:39.079-03:00
published: 2026-07-26T10:19:39.079-03:00
tags:
  - poluicao-luminosa
  - satelites-artificiais
  - processamento-de-imagens
  - iniciacao-cientifica
cssclasses:
  - page-layout
---

# 🛰️ Simulando o Impacto de Satélites em Observações Astronômicas

> [!note] Resumo
> Projeto de pesquisa (IFF Bom Jesus do Itabapoana, orientação da [Prof.ª Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja)) sobre como a proliferação de satélites artificiais contamina imagens astronômicas com rastros luminosos — e como tratar essa contaminação computacionalmente. Em equipe com [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) e Arthur Miguelito Lopes, o projeto evoluiu de um 3º lugar na [[pt-br/media/2024/febic-2024|FEBIC 2024]] até um algoritmo capaz de recuperar 99,7% da informação perdida, premiado em 1º lugar no [[pt-br/media/2025/mctia-2025|MCTIA 2025]].

<div class="media-carousel">
  <a href="/pt-br/research/satellite-trail-removal" class="carousel-slide">
    <img src="/assets/illustrations/informatica.svg" alt="Remoção de rastros de satélite em imagens astronômicas" />
    <div class="slide-caption">Poluição Luminosa por Satélites</div>
  </a>
</div>

## 🌠 O problema

A década de 2020–2030 traz uma nova geração de telescópios (Vera Rubin, GMT, Euclid) que multiplicará por mais de mil o volume e a qualidade dos dados astronômicos disponíveis. Em paralelo, porém, a popularização de **constelações de satélites comerciais** está povoando a órbita terrestre de milhares de objetos brilhantes, que se interpõem entre os telescópios e a luz das estrelas — contaminando imagens com rastros luminosos e ameaçando degradar justamente a nova geração de levantamentos astronômicos de grande volume.

Diferente das duas barreiras históricas da observação astronômica (clima e limitação instrumental), essa é uma contaminação **artificial**, ainda mal quantificada: o brilho de cada satélite depende de posição, altitude e comprimento de onda de forma complexa, e a comunidade internacional (astrônomos, engenheiros, defensores do céu escuro) vem se mobilizando para desenvolver ferramentas open source de tratamento de imagem.

## 🎯 Objetivos

- Desenvolver um método de tratamento de imagem capaz de **identificar contaminação por satélite** em observações astronômicas.
- Testar esse método em **objetos astronômicos simulados**, com contaminação controlada, avaliando aplicabilidade e eficiência.
- Somar esforços ao movimento internacional por soluções open source para o problema da poluição luminosa orbital.

## 🔧 Metodologia

O projeto foi planejado em 5 fases: (1) revisão sistemática do problema e de códigos já existentes; (2) elaboração de um objeto astronômico simulado (preferencialmente uma galáxia); (3) construção de um código de análise/tratamento de imagem; (4) aplicação do código ao objeto simulado, com poluição luminosa controlada (simulação de rastros de satélite); (5) análise dos resultados.

## 📈 Evolução e resultados

| Etapa | Evento | Resultado |
|---|---|---|
| Proposta inicial | Edital de pré-iniciação científica, IFF (2023) | Aprovação do projeto |
| **[[pt-br/media/2024/febic-2024|FEBIC 2024]]** (Pomerode, SC) | Com [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) | **3º lugar — categoria Graduação**, mesmo com o projeto ainda incompleto, competindo com aplicações já patenteadas — resultado que classificou a equipe para o [[pt-br/media/2025/mctia-2025|MCTIA 2025]] |
| **[[pt-br/media/2025/mctia-2025|MCTIA 2025]]** (Belém, PA) | Com [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) e Arthur Miguelito Lopes | **1º lugar — categoria Ciências Exatas do Ensino Superior**, com um algoritmo de IA capaz de **remover rastros de satélite de dados astronômicos, recuperando 99,7% da informação que seria perdida** — resultado que classificou a equipe para o evento nacional Ciência Jovem (Recife, PE, 2026) |

> [!note] Nota sobre este texto
> Esta página combina a proposta formal de pesquisa (submetida ao IFF em 2023, com introdução, justificativa e metodologia completas) com os resultados divulgados publicamente nas premiações da FEBIC 2024 e do MCTIA 2025. Detalhes técnicos do algoritmo de recuperação de 99,7% ainda não foram documentados nesta página — a atualizar conforme o trabalho avança para publicação.

## 🔗 Referências e correlatos

- Milazzo et al. (2021) — _The Growing Digital Divide and its Negative Impacts on NASA's Future Workforce_, BAAS 53, 436
- Rawls et al. (2020) — _Satellite Constellation Internet Affordability and Need_, RNAAS 4, 189
- Venkatesan et al. (2020) — _The Impact of Satellite Constellations on Space as an Ancestral Global Commons_, Nature Astronomy 4, 1043
- [[pt-br/media/2024/febic-2024|FEBIC 2024]] — cobertura da apresentação e do 3º lugar
- [[pt-br/media/2025/mctia-2025|MCTIA 2025]] — cobertura da apresentação e do 1º lugar
- [[pt-br/research/dark-matter-shocks|Entendendo a Matéria Escura a partir de Choques Extragalácticos]] — projeto anterior, mesma orientadora
- [[pt-br/research/anomaly-detection|Detecção de Anomalias em Dados do Gaia]] — outro projeto com foco em aprendizado de máquina aplicado a dados astronômicos
