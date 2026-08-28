---
publish: false
title: arXiv Searcher
created: 2026-03-13 13:04
modified: 2026-08-27 21:59
published: 2026-07-26T10:03:17.536-03:00
tags: [Automação, Pesquisa, Daemon, BibTeX]
status: planejamento
cssclasses:
  - page-layout
---

<!-- gerado por portfolio/tools/gen_quartz.py — não editar à mão -->

**Stack:** Python, arXiv API, Docker, LaTeX, Markdown

Sem repositório público ainda. · em planejamento

<!-- fim do bloco gerado -->

> [!note] Em uma frase
> Ferramenta, em **planejamento**, para buscar e organizar automaticamente artigos do arXiv por assunto/palavra-chave.

Pensada para rodar como daemon (talvez dockerizado), consultando a API do arXiv periodicamente e gerando:

- Saída diária em **Markdown**: tabela com data, título, primeiro autor, área e link do arXiv.
- **Citações prontas em LaTeX**, com a mesma estrutura de referência já usada nos meus artigos.
- Configuração via planilha `.csv` — área de busca padrão configurável, com opção de busca por palavra-chave avulsa sem alterar essa configuração.

Referências de projetos abertos parecidos que uso como inspiração: [biblio.el](https://github.com/cpitclaudel/biblio.el), [bibcure](https://github.com/bibcure/bibcure) e [dailyarxiv](https://dailyarxiv.com).

**Status:** em planejamento — desenho da estrutura de dados (Markdown/LaTeX) e do menu de configuração (assunto padrão via cronjob, escolha manual de assunto, ou combinação assunto+palavra-chave) já esboçados.
