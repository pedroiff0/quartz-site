---
publish: true
title: Journal Clubs
created: 2026-07-26
modified: 2026-08-27
published: 2026-08-01T16:28:51.169-03:00
cssclasses:
  - page-layout
---

> [!note] Resumo
> Lista curada dos artigos que já discuti em journal club, separada por grupo/área: **MWBR** (grupo de pesquisa em Via Láctea/arqueologia galáctica) e **ENGCOMP** (Engenharia de Computação). Cada entrada linka o artigo no arXiv e traz minha síntese da discussão — pontos levantados, críticas e conexões com outros trabalhos —, não o artigo completo.

Diferente de uma simples anotação de leitura individual, um Journal Club aqui é **um artigo que passou por discussão em grupo** — a nota registra também o que foi debatido, não só o conteúdo do artigo.

## Grupos

- **[[pt-br/research/journal-clubs/mwbr|MWBR]]** — grupo de pesquisa em Via Láctea, arqueologia galáctica e populações estelares.
- **[[pt-br/research/journal-clubs/engcomp|ENGCOMP]]** — journal club de Engenharia de Computação.

Cada uma dessas páginas monta a própria lista de artigos a partir do frontmatter das notas da pasta, via [Bases do Obsidian](https://help.obsidian.md/bases) — não há lista escrita à mão para manter em dia.

## Padrão de cada entrada

> [!example] Modelo de nota de artigo
> Toda nota de artigo discutido segue a mesma estrutura. Esses campos alimentam sozinhos a tabela da página do grupo e o [[pt-br/research/journal-clubs/engcomp/dashboard]] — basta criar a nota na pasta certa (`mwbr/` ou `engcomp/`) e ela aparece no próximo build.
>
> O campo `arxiv` é obrigatório: é ele que distingue uma nota de artigo das páginas de apoio da pasta (índice, tópicos, dashboard). E o nome do campo de data é `discutido`, sem hífen — propriedade com hífen quebra o motor de expressões das Bases.
>
> ```markdown
> ---
> publish: true
> title: "Título curto do artigo"
> authors: "Sobrenome, A. et al."
> apresentador: "Quem apresentou"
> year: 2026
> arxiv: "https://arxiv.org/abs/XXXX.XXXXX"
> topico: cs.SE # categoria do arXiv; alimenta o dashboard
> discutido: 2026-MM-DD
> tags:
>   - journal-club
>   - mwbr # ou engcomp
> ---
>
> > [!note] Em resumo
> > Uma frase resumindo do que o artigo trata.
>
> _Autores completos (Ano)_
>
> ## Resumo
> Síntese curta do artigo — problema, método, resultado principal.
>
> ## Discussão
> O que o grupo discutiu de fato: pontos levantados, críticas, dúvidas, conexões com outros artigos/projetos.
>
> [Ver no arXiv](https://arxiv.org/abs/XXXX.XXXXX)
> ```

---

## 🔗 Referências e correlatos

- [[pt-br/research|Pesquisa — visão geral]]
