---
title: "Aula 13: Modularização Multi-arquivo e Gestão Bibliográfica com biblatex-biber"
created: 2026-08-04 13:34
modified: 2026-08-27 13:34
publish: true
notas: "[📄 Notas (PDF)](/assets/biblioteca/latex-escrita/notes-latex/aula-13.pdf)"
slide: "[📄 Slide (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-13-branco.pdf)"
tags:
  - latex
  - escrita-academica
  - abnt
  - ifftese
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots">Próxima Aula</a></b></div>
</div>

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material da Aula
> - 📄 **[Slides LaTeX — Modelo Branco (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-13-branco.pdf)** — *Apresentação visual institucional em tema claro.*
> - 📄 **[Slides LaTeX — Modelo Preto (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-13-preto.pdf)** — *Apresentação visual institucional em tema escuro.*
> - 📝 **[Notas de Aula Institucionais (PDF)](/assets/biblioteca/latex-escrita/notes-latex/aula-13.pdf)** — *Apostila técnica completa em LaTeX.*
> 
> ### 🌐 Links Externos de Apoio
> - **[CTAN (Comprehensive TeX Archive Network)](https://ctan.org/)** — *Repositório mundial de pacotes TeX.*
> - **[ABNT — Catálogo de Normas Técnicas](https://www.abnt.org.br/)** — *Portal oficial de normas NBR 14724, 10520 e 6023.*
> - **[Overleaf Documentation](https://www.overleaf.com/learn)** — *Guias interativos de compilação TeX.*

## 📋 Sumário Interativo
- [📍 1. Fundamentos e Contextualização](#-1-fundamentos-e-contextualização)
- [📍 2. Conceitos-Chave e Normas ABNT](#-2-conceitos-chave-e-normas-abnt)
- [📍 3. Aplicação Prática no Ecossistema ReLaTeX](#-3-aplicação-prática-no-ecossistema-relatex)
- [🔗 Aulas Correlatas & Conexões](#-aulas-correlatas--conexões)
- [📚 Referências Bibliográficas](#-referências-bibliográficas)

## 📖 Conteúdo da Aula

Arquitetura modular de grandes documentos acadêmicos via `\input` e `\include`. Gerenciamento profissional de base de dados bibliográfica em formato `.bib` utilizando a engine moderna `biblatex-biber` com conformidade ABNT NBR 6023.

### 📍 1. Modularização do Projeto (`\input` vs. `\include`)

Organização de monografias em capítulos independentes (`cap1-introducao.tex`, `cap2-revisao.tex`). O comando `\include` gerencia quebras de página automáticas e suporte a `\includeonly` para compilação parcial rápida.

### 📍 2. Estrutura do Arquivo de Referências `.bib`

Sintaxe das entradas BibTeX/BibLaTeX: `@article`, `@book`, `@inproceedings`, `@mastersthesis`, `@online`. Preenchimento correto dos campos de metadados.

### 📍 3. Execução da Engine `biber` e Estilo `biblatex-abnt`

Configuração das opções do `biblatex`: `style=abnt`, `citecolor`, `backref=true`. Ciclo de compilação `pdflatex` -> `biber` -> `pdflatex` -> `pdflatex`.

### 📊 Fluxograma Metodológico da Aula (Mermaid)
```mermaid
flowchart TD
    A[Fundamentação Teórica] --> B[Normalização ABNT Vigente]
    B --> C[Implementação em LaTeX/ReLaTeX]
    C --> D[Compilação e Validação de Resultados]
```

## 🔗 Aulas Correlatas & Conexões

Esta aula conecta-se transversalmente aos seguintes tópicos da formação em LaTeX & Escrita Acadêmica:

- 🔗 **[[pt-br/resource/latex/aula-10-discussao-citacoes-nbr-10520-e-referencias-nbr-6023|Aula 10: Discussão, Citações (10520) e Referências (6023)]]**
- 🔗 **[[pt-br/resource/latex/aula-20-automacao-latexmkrc-git-e-integracao-continua|Aula 20: Automação LaTeX, Git e Integração Contínua CI/CD]]**

## 📚 Referências Bibliográficas

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 10520**: Informação e documentação — Citações em documentos — Apresentação. Rio de Janeiro: ABNT, 2023.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6023**: Informação e documentação — Referências — Elaboração. Rio de Janeiro: ABNT, 2018.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots">Próxima Aula</a></b></div>
</div>
