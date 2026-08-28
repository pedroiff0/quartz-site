---
publish: false
title: ReLaTeX
created: 2026-08-08 13:04
modified: 2026-08-27 13:04
tags: [Overleaf Fork, Self-hosted, IFF, LaTeX]
repo: https://github.com/pedroiff0/relatex
status: privado
cssclasses:
  - page-layout
---

<!-- gerado por portfolio/tools/gen_quartz.py — não editar à mão -->

**Stack:** Docker, Node.js, MongoDB, Redis, Pug, LaTeX

**Repositório:** [https://github.com/pedroiff0/relatex](https://github.com/pedroiff0/relatex) · privado

<!-- fim do bloco gerado -->

> [!note] Em uma frase
> Fork do **Overleaf Community Edition** com a identidade do IFF, hospedado por mim e acessível pela tailnet.

Além do Overleaf padrão, a instância traz:

- As **classes oficiais do IFF** embutidas (`ifftese`, `iffposter`), para
  começar uma tese ou um pôster sem caçar template.
- Tema visual azul do instituto e página inicial própria.
- Dez botões extras no editor para as construções que mais uso.

**Stack:** Docker Compose com `sharelatex/sharelatex`, MongoDB 8 em *replica
set* (exigência das versões recentes do CE) e Redis para cache e sessões.

**Status:** em produção na rede pessoal.
