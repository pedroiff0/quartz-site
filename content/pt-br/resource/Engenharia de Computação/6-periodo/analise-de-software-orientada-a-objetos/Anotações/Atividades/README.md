---
publish: false
title: "README — Atividades & Senha dos Arquivos"
created: 2026-08-29 11:15
modified: 2026-08-29 11:52
discipline: "Análise de Software Orientada a Objetos"
period: "6-periodo"
tags:
  - disciplina
  - readme
  - senhas
  - engenharia-de-computacao
cssclasses:
  - page-layout
---

# 🔒 README — Chave de Acesso & Diretrizes de Atividades

Este documento contém instruções de segurança e a chave de descriptografia dos materiais acadêmicos gerados para os trabalhos da disciplina **Análise de Software Orientada a Objetos**.

---

## 🔑 Senha Padrão dos Documentos Criptografados

> [!important] 🔒 Chave Canônica de Descriptografia
> Todos os arquivos em PDF (Roteiros de Aula e Slides LaTeX Beamer) depositados na pasta `_materiais/` e espelhados nos assets do Quartz possuem a senha canônica:
>
> ### **`eng232`**

---

## 📁 Estrutura de Arquivos Gerados por Trabalho

Quando uma apresentação/trabalho é compilado pelo script [`gerar_tudo.py`](file:///home/pedro/Repositorios/latex/modelos/slides-iff/gerar_tudo.py), os seguintes artefatos são produzidos e sincronizados:

1. `roteiro_iff_disciplina.pdf`: Roteiro de apresentação e fundamentação teórica (A4, protegido com senha).
2. `slides_iff_disciplina.pdf`: Apresentação LaTeX Beamer 16:9 em tema claro (protegido com senha).
3. `slides_iff_disciplina_preto.pdf`: Apresentação LaTeX Beamer 16:9 em tema escuro (protegido com senha).
4. `slides_iff_disciplina.pptx`: Apresentação Microsoft PowerPoint 16:9 em tema claro (desbloqueada).
5. `slides_iff_disciplina_preto.pptx`: Apresentação Microsoft PowerPoint 16:9 em tema escuro (desbloqueada).

---

## 🚀 Como Compilar um Trabalho

Para processar uma nova nota de trabalho localizada nesta pasta `Atividades/`, execute no terminal:

```bash
python3 /home/pedro/Repositorios/latex/modelos/slides-iff/gerar_tudo.py --note "/home/pedro/hardcore-life/pt-br/resource/Engenharia de Computação/6-periodo/analise-de-software-orientada-a-objetos/Anotações/Atividades/Trabalho - Coesão e Acoplamento.md"
```
