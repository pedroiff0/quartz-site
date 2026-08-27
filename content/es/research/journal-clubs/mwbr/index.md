---
publish: true
title: "MWBR"
created: 2026-07-26
modified: 2026-07-31
published: 2026-08-01T20:04:12.171-03:00
cssclasses:
  - page-layout
---

> [!note] Resumen
> Artículos discutidos en el journal club del **MWBR**, grupo de investigación en Vía Láctea, arqueología galáctica y poblaciones estelares. Ver el [[pt-br/research/journal-clubs#padrão-de-cada-entrada|patrón de cada entrada]].

 La siguiente tabla se genera a partir del frontmatter de las propias notas de artículo de esta carpeta — una nota nueva aparece sola en el siguiente build, sin editar esta página.

 ``base
 filters:
 and:
 'file.folder.startsWith("pt-br/research/journal-clubs/mwbr")'
 Sólo notas de artículo tienen `arxiv`; es lo que separa una entrada de las páginas
 de apoyo de la carpeta (index y lo que más venga).
 note.arxiv
 formulaciones:
 artículo: 'link(file.path, note.title)'
 La URL arXiv entra como texto y el Quartz la transforma en enlace externo
 solo. No usar enlace() aquí: solo resuelve el camino interno y transforma
 una URL en "../../https/arxiv.org/...". html() tampoco sirve — markup
 se escapa antes de llegar a la célula.
 properties:
 formula. artículo:
 displayName: Artículo
 note. presentador:
 displayName: Apresentó
 note. authors:
 displayName: Autor
 note.year:
 displayName: Año
 note. discutido:
 displayName: Discutido en
 note. arxiv:
 displayName: arXiv
 vistas:
 -type: table
 name: Artículos discutidos
 order:
 formula. artículo
 note. presentador
 note. authors
 note. year
 note. discutido
 note. arxiv
 sort:
 property: note. discutido
 direction: DESC
 ````

 ---

## 🔗 Referencias y correcciones

- [[es/research/journal-clubs|Journal Clubs — visión general]]
- [[es/research/journal-clubs/engcomp|ENGCOMP]]
- [[es/research|Investigación — visión general]]

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
