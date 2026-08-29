---
publish: true
title: "Prompt as a Data Type: In-Database LLM Prompt Management and Rewriting"
authors: "Martins, D. M. L. & Vossen, G."
presenter: "Pedro Henrique Rocha de Andrade"
year: 2026
arxiv: "https://arxiv.org/abs/2607.21756"
topic: cs.DB
discussed: 2026-08-01
tags:
  - journal-club
  - engcomp
cssclasses:
  - page-layout
modified: 2026-08-28 21:09
---

<div class="paper-banner">
  <div class="paper-title">Prompt as a Data Type: In-Database LLM Prompt Management and Rewriting</div>
  <div class="paper-meta">
    <b>Autores:</b> Martins, D. M. L. & Vossen, G. (2026)<br>
    <b>Apresentador / Pesquisa:</b> Pedro Henrique Rocha de Andrade &nbsp;•&nbsp; <b>Grupo:</b> ENGCOMP — Journal Club (IFF BJI)<br>
    <a href="https://arxiv.org/abs/2607.21756">arXiv:2607.21756 [cs.DB]</a> &nbsp;|&nbsp; 
    <a href="https://arxiv.org/pdf/2607.21756">PDF Original (arXiv)</a>
  </div>
</div>

> [!abstract] Resumo Executivo
> Modelos de Linguagem de Grande Porte (LLMs) estão sendo progressivamente acoplados a Sistemas Gerenciadores de Banco de Dados Relacionais (SGBDs). Contudo, os prompts tradicionalmente permanecem encapsulados na camada de aplicação externa, isolados dos motores de consulta. Este trabalho propõe o **PromptDB**, que introduz `PROMPT` como um **tipo de dado nativo de primeira classe** no banco de dados, permitindo que o otimizador relacional realize reescrita de prompts, controle de versões, cache semântico e parametrização segura diretamente via SQL.

***

## ❓ Perguntas Norteadoras da Discussão

> [!question] Roteiro de Discussão no Clube ENGCOMP
> 1. **Qual é o principal gargalo arquitetural da separação entre lógica de prompts (na aplicação) e dados estruturados (no SGBD)?**
> 2. **Como a tipagem formal `PROMPT` permite que o otimizador de consultas (Query Optimizer) deduza equivalências semânticas e reduza custos de inferência de LLMs?**
> 3. **Quais são os mecanismos de segurança e integridade de dados introduzidos para mitigar *Prompt Injection* diretamente na camada relacional?**
> 4. **De que forma o PromptDB se integra com sistemas relacionais modernos (e.g. PostgreSQL) e dialetos SQL existentes?**

***

## 📖 1. Motivação e Isolamento Atual de Prompts

> [!warning|#ffd000] [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/Artigo - Martins2026.pdf#page=1|Artigo - Martins2026, p.1]]
> > *"Currently, prompts sent to LLMs reside entirely within application business logic, rendering them opaque to database optimization engines."*
> 
> **Anotação:** A opacidade dos prompts impede que o banco aplique técnicas consagradas como *pushdown de predicados*, reutilização de planos e estimativa de cardinalidade em consultas aumentadas por IA.

***

## 🔬 2. Arquitetura do PromptDB & O Tipo de Dado `PROMPT`

> [!tip|#1e823c] [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/Artigo - Martins2026.pdf#page=3|Artigo - Martins2026, p.3]]
> > *"By defining PROMPT as a composite SQL domain, database engines can perform algebraic rewrites, syntactic validation, and version branching natively."*
> 
> **Anotação:** O tipo `PROMPT` armazena templates, parâmetros e metadados contextuais, transformando o prompt em uma entidade versionável e transacional dentro da relação.

***

## 📂 Recursos & Materiais do Estudo

> [!tip] 🔗 Links e Materiais Vinculados (Dinâmicos)
> - 📄 **Artigo Original PDF:** [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/Artigo - Martins2026.pdf|Artigo - Martins2026.pdf]]
> - 📑 **Roteiro de Leitura (Lecture PDF):** [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/roteiro_Martins2026.pdf|roteiro_Martins2026.pdf]]
> - 📊 **Slides Beamer (LaTeX PDF Claro):** [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/slides_engcomp_artigo.pdf|slides_engcomp_artigo.pdf]]
> - 📊 **Slides Beamer (LaTeX PDF Escuro):** [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/slides_engcomp_artigo_preto.pdf|slides_engcomp_artigo_preto.pdf]]
> - 💻 **Slides PowerPoint (PPTX Claro):** [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/main_slides_169_branco.pptx|main_slides_169_branco.pptx]]
> - 💻 **Slides PowerPoint (PPTX Escuro):** [[pt-br/research/Journal-Clubs/engcomp/_materiais/2607.21756/main_slides_169_preto.pptx|main_slides_169_preto.pptx]]
> - 👥 **Grupo de E-mails do Clube (Google Groups):** [groups.google.com/g/engcompbji](https://groups.google.com/g/engcompbji)
> - 🏠 **Hub ENGCOMP no Site Pessoal:** [phrandrade.com/engcomp](https://www.phrandrade.com/pt-br/research/journal-clubs/engcomp/)
> - 🔗 **Versão Publicada Desta Nota (Web):** [Acessar Nota Publicada Online](https://www.phrandrade.com/pt-br/research/journal-clubs/engcomp/prompt-as-a-data-type)

---

## 🔗 Referências e Correlatos

- [[pt-br/research/journal-clubs/engcomp|ENGCOMP — Journal Club]]
- [[pt-br/research/journal-clubs|Journal Clubs — Visão Geral]]
- [[pt-br/research|Pesquisas Acadêmicas — Visão Geral]]
