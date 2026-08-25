---
title: Anotações e Arquivos
publish: true
permalink: pt-br/resource/engenharia-de-computação/eletivas/energia-e-eficiencia-energetica/anotacoes
---
## 📝 Anotações e Documentos

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/Engenharia de Computação/eletivas/energia-e-eficiencia-energetica/anotacoes")'
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
