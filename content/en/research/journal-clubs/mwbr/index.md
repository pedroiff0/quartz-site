---
publish: true
title: "MWBR"
created: 2026-07-26
modified: 2026-07-31
published: 2026-08-01T20:04:12.171-03:00
cssclasses:
  - page-layout
---

> [!note] Summary
> Articles discussed in the journal club of **MWBR**, research group in Milky Way, galactic archaeology and stellar populations. View [[pt-br/research/journal-clubs#padrão-de-cada-entrada|default of each input]].

 The table below is generated from the frontmatter of the article notes themselves in this folder — a new note appears alone on the next build without editing this page.

 '`base
 filters:
 and:
 'file.folder.startsWith("pt-br/research/journal-clubs/mwbr")'
 Only article notes have `arxiv`; it is what separates an entry from the pages
 folder support (index and whatever else comes).
 note.arxiv
 formulas:
 article: 'link(file.path, note.title)'
 It's okay The URL of arXiv enters as text and the Quartz turns it into external link
 Alone. Do not use link() here: it only solves internal path and transforms
 a URL in "../../https/arxiv.org/...". html() also does not serve — markup
 is escaped before reaching the cell.
 properties:
 formula. article:
 displayName: Article
 note. presenter:
 displayName: Presented
 note. authors:
 displayName: Author
 note.year:
 displayName: Year
 note. discussed:
 displayName: Discussion in
 note. arxiv:
 displayName: arXiv
 views:
 type: table
 name: Articles discussed
 order:
 formula. article
 notice. host
 notice. authors
 notice. year
 notice. discussed
 notice. arxiv
 sort:
 property: note. discussed
 direction:
 '``

 ---

## 🔗 References and correlations

- [[en/research/journal-clubs|Journal Clubs — Overview]]
- [[en/research/journal-clubs/engcomp|ENGCOMP]]
- [[en/research|Research — Overview]]

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
