---
publish: false
title: "Tarefas do 6º Período"
created: 2026-08-24
modified: 2026-08-27
cssclasses:
  - page-layout
---
# 📋 Painel Geral de Tarefas (6º Período)

Este painel consolida automaticamente todas as tarefas declaradas nas notas de aula e ementas do período. Para adicionar uma nova tarefa, basta utilizar `- [ ] Descrição da tarefa` em qualquer anotação ou ementa.

```dataview
TABLE 
  t.text AS "Tarefa", 
  choice(t.completed, "✅ Feito", "❌ Pendente") AS "Status", 
  choice(disciplina, disciplina, file.folder) AS "Origem",
  t.section AS "Seção"
FROM "pt-br/resource/Engenharia de Computação/6-periodo"
FLATTEN file.tasks AS t
WHERE !contains(lower(file.name), "index")
  AND !contains(lower(file.path), "esboço") 
  AND !contains(lower(file.path), "esboco")
  AND !contains(lower(t.text), "planejando")
  AND !contains(lower(t.text), "em andamento")
  AND !contains(lower(t.text), "concluí")
  AND !contains(lower(t.text), "conclui")
```
