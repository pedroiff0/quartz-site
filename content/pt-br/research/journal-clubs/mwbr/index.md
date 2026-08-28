---
publish: true
title: MWBR — Journal Club
created: 2026-07-26 13:33
modified: 2026-08-27 13:33
published: 2026-08-01T20:04:12.171-03:00
cssclasses:
  - page-layout
---

> [!note] 🌌 Milky Way Brazil (MWBR)
> Artigos científicos e discussões do **MWBR**, grupo de pesquisa voltado ao estudo da **Via Láctea, Arqueologia Galáctica, Populações Estelares e Astrofísica Observacional**.

---

> [!info] 🌐 Curadoria & Histórico Geral do Grupo
> O histórico completo das reuniões e discussões de todos os membros do grupo pode ser consultado na curadoria oficial mantida por João Amarante:
> 🔗 **[Acessar Curadoria Oficial do MWBR (jasamarante.github.io/jc/mwbr/)](https://jasamarante.github.io/jc/mwbr/)**

---

## 🎙️ Artigos Apresentados por Mim

Artigos e tópicos que selecionei e apresentei nas sessões do Journal Club:

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/research/journal-clubs/mwbr")'
    - 'note.arxiv'
    - 'note.apresentador.contains("Pedro")'
formulas:
  artigo: 'link(file.path, note.title)'
properties:
  formula.artigo:
    displayName: Artigo
  note.authors:
    displayName: Autoria
  note.year:
    displayName: Ano
  note.discutido:
    displayName: Data
  note.arxiv:
    displayName: arXiv / Link
views:
  - type: table
    name: Minhas Apresentações
    order:
      - formula.artigo
      - note.authors
      - note.year
      - note.discutido
      - note.arxiv
    sort:
      - property: note.discutido
        direction: DESC
```

---

## ⭐ Artigos Recomendados & Favoritos (Apresentados por Colegas)

Artigos de destaque apresentados por outros pesquisadores do grupo com discussões e metodologias que considerei fundamentais:

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/research/journal-clubs/mwbr")'
    - 'note.arxiv'
    - '!note.apresentador.contains("Pedro")'
formulas:
  artigo: 'link(file.path, note.title)'
properties:
  formula.artigo:
    displayName: Artigo
  note.apresentador:
    displayName: Apresentado por
  note.authors:
    displayName: Autoria
  note.year:
    displayName: Ano
  note.discutido:
    displayName: Data
  note.arxiv:
    displayName: arXiv / Link
views:
  - type: table
    name: Seleção de Destaques
    order:
      - formula.artigo
      - note.apresentador
      - note.authors
      - note.year
      - note.discutido
      - note.arxiv
    sort:
      - property: note.discutido
        direction: DESC
```

---

## 🔗 Referências e correlatos

- [[pt-br/research/journal-clubs|Journal Clubs — Visão Geral]]
- [[pt-br/research/journal-clubs/engcomp|ENGCOMP Journal Club]]
- [[pt-br/research|Pesquisa — Visão Geral]]
