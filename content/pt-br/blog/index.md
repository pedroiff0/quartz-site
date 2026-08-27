---
publish: false
title: Blog
created: 2026-07-18
modified: 2026-07-25T23:58:08.061-03:00
published: 2026-07-25T23:58:08.061-03:00
order: 7
cssclasses:
  - page-layout
---

> [!note] Resumo
> Pensamentos aleatórios, tutoriais e reflexões sobre a jornada de pesquisa — sem compromisso de frequência.

<div class="media-carousel">
  <a href="/pt-br/blog/bem-vindo" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="Bem-vindo ao blog" />
    <div class="slide-caption">Bem-vindo ao blog</div>
  </a>
</div>

- [[pt-br/blog/bem-vindo|Bem-vindo ao blog]] — Por que abri esse espaço e o que esperar por aqui.


## 📝 Publicações do Blog

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/blog")'
    - 'note.publish'
formulas:
  post: 'link(file.path, note.title)'
properties:
  formula.post:
    displayName: Artigo / Publicação
  note.created:
    displayName: Data
views:
  - type: table
    name: Publicações do Blog
    order:
      - formula.post
      - note.created
    sort:
      - property: note.created
        direction: DESC
```
