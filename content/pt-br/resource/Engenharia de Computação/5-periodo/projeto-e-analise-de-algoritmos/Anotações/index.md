---
publish: true
title: "Anotações de Quadro — Projeto E Analise De Algoritmos"
created: 2026-08-24
modified: 2026-08-27
cssclasses:
  - page-layout
  - cards
---

# 📝 Anotações de Quadro & Conteúdo das Aulas

Este repositório consolida as anotações detalhadas de quadro, exercícios e materiais de apoio da disciplina **Projeto E Analise De Algoritmos**.

## 📋 Relação de Aulas Registradas

```dataview
TABLE 
  title AS "Título / Conteúdo",
  dateformat(date(created), "dd/MM/yyyy") AS "Data",
  professor AS "Docente"
FROM ""
WHERE contains(file.folder, "Anotações")
  AND contains(file.path, "projeto-e-analise-de-algoritmos")
  AND (contains(file.tags, "aula") OR contains(lower(file.name), "aula"))
  AND !contains(lower(file.name), "index")
  AND !contains(lower(file.path), "esboço")
  AND !contains(lower(file.path), "esboco")
SORT file.name ASC
```
