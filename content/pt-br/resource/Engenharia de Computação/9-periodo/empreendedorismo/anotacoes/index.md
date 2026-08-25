---
title: Anotações e Arquivos
publish: true
permalink: pt-br/resource/engenharia-de-computação/9-periodo/empreendedorismo/anotacoes
---
## 📝 Anotações e Documentos

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/9-periodo/empreendedorismo/anotacoes")'
    - '!file.name.endsWith("index")'
formulas:
  anotacao: 'link(file.path, note.title)'
properties:
  formula.anotacao:
    displayName: Anotação / Documento
  note.created:
    displayName: Data de Criação
views:
  - type: table
    name: Anotações da Disciplina
    order:
      - formula.anotacao
      - note.created
    sort:
      - property: file.name
        direction: ASC
```
