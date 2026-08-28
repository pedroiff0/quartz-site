---
title: "Aula 14: Computação Gráfica Vetorial Programável com TikZ e Gráficos PGFPlots"
created: 2026-08-04 13:34
modified: 2026-08-27 21:54
publish: true
notas: "[📄 Notas (PDF)](/assets/biblioteca/latex-escrita/notes-latex/aula-14.pdf)"
slide: "[📄 Slide (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-14-branco.pdf)"
tags:
  - latex
  - escrita-academica
  - abnt
  - ifftese
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/latex/aula-13-modularizacao-multi-arquivo-e-biblatex-biber">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/latex/aula-15-engenharia-do-arquivo-de-metadados-sty">Próxima Aula</a></b></div>
</div>

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material da Aula
> - 📄 **[Slides LaTeX — Modelo Branco (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-14-branco.pdf)** — *Apresentação visual institucional em tema claro.*
> - 📄 **[Slides LaTeX — Modelo Preto (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-14-preto.pdf)** — *Apresentação visual institucional em tema escuro.*
> - 📝 **[Notas de Aula Institucionais (PDF)](/assets/biblioteca/latex-escrita/notes-latex/aula-14.pdf)** — *Apostila técnica completa em LaTeX.*
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

Programação de elementos gráficos vetoriais diretamente no código TeX. Construção de esquemas de rede, arquiteturas de sistemas, circuitos lógicos e plotagem gráfica de dados experimentais em alta resolução sem perda de qualidade.

### 📍 1. Sintaxe Fundamental do `tikz` e Noção de Nós (*Nodes*)

Desenho de formas primitivas, linhas, setas e nós com coordenadas relativas e absolutas. Uso de estilos customizados para criação de diagramas em blocos de arquitetura de software.

### 📍 2. Plotagem Científica de Dados com `pgfplots`

Plotagem direta de arquivos CSV de resultados experimentais (`\addplot table[x=tempo, y=acuracia] {dados.csv};`) com eixos calibrados, legendas e linhas de grade.

### 📍 3. Otimização de Compilação com a Biblioteca `external`

Uso da funcionalidade TikZ Externalize para pré-compilar imagens vetoriais pesadas em arquivos PDF individuais, acelerando drasticamente o tempo de build do documento.

### 📊 Fluxograma Metodológico da Aula (Mermaid)
```mermaid
flowchart TD
    A[Fundamentação Teórica] --> B[Normalização ABNT Vigente]
    B --> C[Implementação em LaTeX/ReLaTeX]
    C --> D[Compilação e Validação de Resultados]
```

## 🔗 Aulas Correlatas & Conexões

Esta aula conecta-se transversalmente aos seguintes tópicos da formação em LaTeX & Escrita Acadêmica:

- 🔗 **[[pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs|Aula 12: Sintaxe Canônica, Ambientes Matemáticos Avançados (amsmath) e Tabelas (booktabs)]]**
- 🔗 **[[pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty|Aula 16: Desenvolvimento de Pacotes .sty - Programação TeX e Macros]]**

## 📚 Referências Bibliográficas

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 10520**: Informação e documentação — Citações em documentos — Apresentação. Rio de Janeiro: ABNT, 2023.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6023**: Informação e documentação — Referências — Elaboração. Rio de Janeiro: ABNT, 2018.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/latex/aula-13-modularizacao-multi-arquivo-e-biblatex-biber">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/latex/aula-15-engenharia-do-arquivo-de-metadados-sty">Próxima Aula</a></b></div>
</div>
