---
publish: false
title: "Tarefas do 6º Período"
created: 2026-08-24
modified: 2026-08-24
---

# 📋 Painel Geral de Tarefas (6º Período)

Este painel consolida automaticamente todas as tarefas declaradas nas notas de aula do período. Para adicionar uma nova tarefa, basta utilizar `- [ ] Descrição da tarefa` em qualquer anotação de aula.

```dataview
TABLE 
  t.text AS "Tarefa", 
  choice(t.completed, "✅ Feito", "❌ Não feito") AS "Status", 
  disciplina AS "Disciplina",
  t.section AS "Sessão / Data"
FROM "02 - Áreas/Acadêmico/IFF - Engenharia de Computação/6-periodo"
FLATTEN file.tasks AS t
WHERE regexmatch("^aula [0-9]+ -.*", lower(file.name))
```
