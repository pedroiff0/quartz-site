---
publish: false
title: SAB 2026 — Banner
created: 2026-09-26 22:05
modified: 2026-09-26 21:56
tags:
- midia
- pesquisa
icon: lucide-presentation
cssclasses:
  - page-layout
---

# SAB 2026 — Banner

> [!warning]- Em construção!
> Esta página está em construção: o banner ainda será refeito e os resultados podem mudar (análises com e sem estrelas de CCD ausente, cortes de qualidade e o GALAH completo ainda estão em andamento).

> [!note] Evento
> Reunião Anual da Sociedade Astronômica Brasileira (SAB 2026), Natal - RN, 25 a 30 de outubro de 2026. Página do evento: [[03-midia/2026/sab-2026|SAB 2026]].

**Título:** *How varied are stellar populations in the Solar vicinity? Exploring GCNS and GALAH DR4 with t-SNE*
**Autores:** Pedro Henrique Rocha de Andrade (IFF Bom Jesus do Itabapoana) e Maria Luiza Linhares Dantas (PUC Chile).
**Pesquisa:** [[01-projetos/site-publico/anomaly-detection/anomaly-detection|Detecção de Anomalias em Estrelas da Via Láctea]].

## Pergunta

O t-SNE consegue, sem supervisão, (i) recuperar propriedades de populações estelares colocando estrelas parecidas próximas e (ii) apontar *outliers* genuínos na vizinhança solar?

## Dados

- **GCNS** (Gaia Catalogue of Nearby Stars, ~330 mil estrelas a menos de 100 pc) cruzado por *source_id* com o **GALAH DR4**: 6.198 estrelas.
- **5.073 anãs M** (Teff ≤ 4500 K, log g ≥ 3,5) com espectro *single-fit*, cada uma um vetor de **14.800 pixels** (4 CCDs). Parâmetros (Teff, log g, [Fe/H]) servem só para colorir os mapas, nunca como entrada.
- 915 dessas anãs M (18%) têm pelo menos um CCD ausente (`flag_sp`, bit de valor 2).

## O que encontramos

- **Gradientes sem supervisão:** o t-SNE (perplexidade 30) organiza as anãs M em gradientes suaves de Teff, log g e [Fe/H].
- **Um pequeno grupo destacado (grupo A):** 77 estrelas (mediana de [Fe/H] = −0,79; S/N = 51) se separam do corpo principal em perplexidade 30. O destaque **depende da perplexidade**: em perplexidade 50 o grupo destacado é outro (grupo B, 43 estrelas, sem membros em comum com A) e o UMAP não isola A. Refazendo o t-SNE sem as estrelas de CCD ausente, A continua destacado em perplexidade 30. Por isso o tratamos como candidato a investigar, não como população única.
- **Os "braços" isolados do mapa são qualidade do espectro:** 807 estrelas (16%) com S/N mediana 12; 85% têm CCD ausente (contra 6% no corpo principal) e 86% a *flag* de S/N baixo. Um CCD ausente deixa um trecho plano no vetor de 14.800 pixels.
- **Grupo B:** 91% das 43 estrelas carregam a *flag* de emissão.
- **Hiperparâmetros:** o número de *clusters* do HDBSCAN varia de 172 a 2 conforme `min_cluster_size` e `min_samples`; o t-SNE troca estrutura local por global conforme a perplexidade. Não há um ótimo único.

## Figuras do banner

| Figura | Conteúdo |
|---|---|
| F1 | t-SNE (perplexidade 30) de 5.073 anãs M, colorido por Teff |
| F2 | Gradientes de log g e [Fe/H] no mapa |
| F3 | Perplexidade 30 × 50, colorido por [Fe/H] |
| F4 | Grupo A × corpo principal nos planos Teff–log g e Teff–[Fe/H] (correlação de Spearman) |
| F5 | Clusters do HDBSCAN e S/N do mesmo mapa |
| F6 | Caracterização da amostra: Kiel, Toomre e Tinsley-Wallerstein |
| F7 | Contexto: amostra local × subamostra aleatória de 30 mil estrelas do GALAH |
| F8 | Varredura de perplexidade do t-SNE (vizinhança local, correlação global, R² de Teff/log g/[Fe/H], nº de clusters) |
| F9–F10 | Varreduras do UMAP (`n_neighbors` × `min_dist`) e do HDBSCAN |
| F11 | Matriz de mapas t-SNE por perplexidade |
| F12 | UMAP e HDBSCAN: varreduras combinadas |
| F13 | Onde caem os grupos A, B e as binárias SB2 em perplexidades de 10 a 200 |
| F14 | Enriquecimento de vizinhança e *gap* de isolamento × perplexidade |
| Mapa de *flags* | Percentual de estrelas com cada bit de `flag_sp`, por região do mapa |

## Método (resumo)

Espectros *single-fit* do GALAH DR4 reamostrados numa grade comum de 14.800 pixels (lacunas preenchidas com 1,0). Os mapas t-SNE do banner partem de PCA de 50 componentes; o UMAP "direto" usa os 14.800 pixels (métrica do cosseno). HDBSCAN sobre o UMAP; grupos A e B acompanhados entre perplexidades (pureza e enriquecimento de vizinhança, *gap* e isolamento). Todas as etapas são reproduzíveis por *scripts* de linha de comando com semente 42.

## Próximo passo

Análises separadas com e sem estrelas de CCD ausente, cortes de qualidade (S/N, `flag_sp`) e a projeção do GALAH completo.
