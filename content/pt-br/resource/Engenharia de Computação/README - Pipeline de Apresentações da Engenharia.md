---
tags:
  - guia
  - pipeline
  - engenharia
  - latex
  - pptx
  - quickadd
draft: true
publish: false
modified: 2026-08-28 21:09
cssclasses:
  - page-layout
---

# 🎓 Guia do Pipeline Institucional: Engenharia de Computação (IFF)

> [!abstract] Visão Geral
> Pipeline padronizado para geração automatizada de **Roteiros Acadêmicos (.pdf)**, **Slides Beamer 16:9 (.pdf)** e **Apresentações PowerPoint (.pptx)** para as disciplinas e seminários do curso de Engenharia de Computação do IFFluminense.

---

## 🔒 Segurança e Senha dos Arquivos Publicados

> [!important] Informação de Acesso
> Os materiais gerados para a pasta pública `_materiais/` e espelhados no Quartz Site são protegidos por criptografia PDF com a senha:
> 
> **`eng232`**
> 
> *(Esta senha é de uso interno e pedagógico para os alunos e professores da turma).*

---

## 📂 Template de Trabalho para Disciplina (QuickAdd / Obsidian)

Ao criar uma nova anotação de trabalho em qualquer pasta de disciplina (ex: `7-periodo/sistemas-operacionais-i/`), utilize este cabeçalho e estrutura:

```markdown
---
tags:
  - disciplina
  - engenharia-de-computacao
  - trabalho
  - apresentacao
disciplina: "[Nome da Disciplina]"
periodo: "[X]-periodo"
data: 28/08/2026
integrantes:
  - Pedro Henrique Rocha de Andrade
  - Ana Cecília Soja
  - Maria Luiza Dantas
draft: true
publish: false
---

# 🎓 [Título do Trabalho / Seminário]

> [!note] Resumo da Apresentação
> Breve descrição do trabalho prático ou teórico apresentado na disciplina.

## 📂 Recursos & Materiais da Disciplina

> [!tip] 🔗 Links e Materiais Vinculados (Dinâmicos)
> - 📑 **Roteiro & Notas de Aula (PDF):** [[pt-br/resource/Engenharia de Computação/_materiais/roteiro_iff_disciplina.pdf|roteiro_iff_disciplina.pdf]]
> - 📊 **Slides da Apresentação (LaTeX PDF Claro):** [[pt-br/resource/Engenharia de Computação/_materiais/slides_iff_disciplina.pdf|slides_iff_disciplina.pdf]]
> - 📊 **Slides da Apresentação (LaTeX PDF Escuro):** [[pt-br/resource/Engenharia de Computação/_materiais/slides_iff_disciplina_preto.pdf|slides_iff_disciplina_preto.pdf]]
> - 💻 **Slides PowerPoint (PPTX Claro):** [[pt-br/resource/Engenharia de Computação/_materiais/slides_iff_disciplina.pptx|slides_iff_disciplina.pptx]]
> - 💻 **Slides PowerPoint (PPTX Escuro):** [[pt-br/resource/Engenharia de Computação/_materiais/slides_iff_disciplina_preto.pptx|slides_iff_disciplina_preto.pptx]]
> - 🌐 **Hub de Disciplinas no Site Pessoal:** [phrandrade.com/disciplinas](https://www.phrandrade.com/pt-br/resource/engenharia-de-computa%C3%A7%C3%A3o/)
> - 🏛️ **Portal Institucional IFFluminense:** [portal1.iff.edu.br](https://portal1.iff.edu.br/)

---

## 🎯 1. Introdução & Contextualização
- **Conceitos Fundamentais:** ...
- **Problemática Abordada:** ...
- **Objetivos:** ...

## ⚙️ 2. Metodologia & Desenvolvimento
- **Ferramentas Utilizadas:** ...
- **Etapas Práticas:** ...

## 📈 3. Resultados & Discussão
- **Análise dos Dados:** ...
- **Validação com a Teoria:** ...

## 🏁 4. Conclusões
- **Síntese:** ...
- **Próximos Passos:** ...
```

---

## 🚀 Como Executar o Pipeline

Após preencher o roteiro e os slides no repositório de templates ([[file:///home/pedro/Repositorios/latex/modelos/slides-iff|`slides-iff/`]]), execute:

```bash
python3 /home/pedro/Repositorios/latex/modelos/slides-iff/gerar_tudo.py
```

### O que o comando faz automaticamente:
1. Compila o **Roteiro Acadêmico** (`roteiro_iff_disciplina.pdf`).
2. Compila os **Slides Beamer 16:9** nas versões Branco/Verde IFF e Preto/Dourado.
3. Gera os arquivos **PowerPoint (.pptx)** com as figuras e layout mapeados.
4. Encripta os PDFs com a senha `eng232` e deposita na pasta:
   - `pt-br/resource/Engenharia de Computação/_materiais/`
   - `quartz-site/content/assets/disciplinas/`
