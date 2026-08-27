---
publish: true
title: "Journal Clubs"
created: 2026-07-26
modified: 2026-07-26
published: 2026-08-01T16:28:51.169-03:00
cssclasses:
  - page-layout
---

> [!note] Resumen
> Lista curada de los artículos que ya discute en journal club, separada por grupo/área: **MWBR**(grupo de investigación en Vía Láctea/arqueología galáctica) y**ENGCOMP** (Engenharia de Computación). Cada entrada enlaza el artículo en el arXiv y trae mi síntesis de la discusión — puntos levantados, críticas y conexiones con otros trabajos—, no el artículo completo.

 A diferencia de una simple anotación de lectura individual, un Journal Club aquí es **un artículo que pasó por discusión en grupo** — la nota registra también lo que fue debatido, no sólo el contenido del artículo.

## Grupos

- **[[es/research/journal-clubs/mwbr|MWBR]]** — grupo de investigación en Vía Láctea, arqueología galáctica y poblaciones estelares.
- **[[es/research/journal-clubs/engcomp|ENGCOMP]]** — journal club de Ingeniería de Computación.

 Cada una de estas páginas monta la propia lista de artículos desde el frontmatter de las notas de la carpeta, vía [Bases del Obsidian](https://help.obsidian.md/bases)— no hay lista escrita a mano para mantener en día.

## Patrón de cada entrada

> [!example] Modelo de nota de artículo
> Toda nota de artículo discutido sigue la misma estructura. Estos campos alimentan solos la tabla de la página del grupo y el [[es/research/journal-clubs/engcomp/dashboard]]— simplemente crea la nota en la carpeta correcta (`mwbr/` o `engcomp/`) y aparece en el siguiente build.
>
> El campo `arxiv` es obligatorio: es él que distingue una nota de artículo de las páginas de apoyo de la carpeta (índice, tópicos, dashboard). Y el nombre del campo de fecha es `discutido`, sin hífen — propiedad con hífen rompe el motor de expresiones de las bases.
>
> `markdown
> ---
> publish: true
> title: "Título corto del artículo"
> authors: "Sobrenombre, A. et al."
> presentador: "Quién presentó"
> year: 2026
> arxiv: "https://arxiv.org/abs/XXXX.XXXX"
> topico: cs.SE # categoría de arXiv; alimenta el dashboard
> discutido: 2026-MM-DD
> etiquetas:
>   journal-club
>   mwbr # o engcomp
> ---
>
> > [!note] En resumen
> > Una frase resumiendo de lo que el artículo trata.
>
> Autores completos (Ano) 
>
> ## Resumen
> Síntesis corta del artículo — problema, método, resultado principal.
>
> ## Discusión
> Lo que el grupo discutió de hecho: puntos levantados, críticas, dudas, conexiones con otros artículos/proyectos.
>
> [Ver en arXiv](https://arxiv.org/abs/XXXX.XXXXX)
> ````

 ---

## 🔗 Referencias y correcciones

- [[es/research|Investigación — visión general]]

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
