---
publish: true
title: "Hub — Fundamentos Da Computacao"
created: 2026-08-24
modified: 2026-08-27
cssclasses:
  - page-layout
---

# 📚 Hub da Disciplina: Fundamentos Da Computacao

## 📂 Acesso Rápido
- 📝 [[Anotações/index|Anotações de Quadro das Aulas]]

---

## 📋 Aulas da Disciplina

```dataview
TABLE 
  title AS "Conteúdo da Aula",
  created AS "Data"
FROM "pt-br/resource/Engenharia de Computação"
WHERE contains(file.folder, "Fundamentos Da Computacao")
  AND (contains(file.tags, "aula") OR contains(lower(file.name), "aula"))
  AND !contains(lower(file.name), "index")
  AND !contains(lower(file.path), "esboço")
  AND !contains(lower(file.path), "esboco")
SORT file.name ASC
```
