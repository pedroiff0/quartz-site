---
publish: false
draft: true
title: "Aula 01: Introdução e Fundamentação Teórica"
created: 2026-08-04
modified: '2026-08-04'
tags:
  - aula
  - modelo-curso
cssclasses:
  - page-layout
---

# Aula 01: Introdução e Fundamentação Teórica

> [!IMPORTANT] Acesso Restrito Institucional
> Este material pedagógico, bem como seus slides em **LaTeX (.pdf)** e **PowerPoint (.pptx)**, são de uso exclusivo dos estudantes do Instituto Federal Fluminense (*Campus* Bom Jesus do Itabapoana) e estão protegidos com senha institucional.

**Carga Horária Equivalente:** 2 horas/aula diárias.  
**Professor Responsável:** Prof. Dr. Pedro Henrique Rocha de Andrade

---

## 1. Fundamentação Teórica

Esta aula apresenta os fundamentos teóricos canônicos e a relevância do método científico aplicado à engenharia e tecnologia. Discutimos como estruturar problemas complexos em formulações precisas e verificáveis.

```mermaid
graph TD
    A[Observação Empírica] --> B[Formulação do Problema]
    B --> C[Hipótese Científica]
    C --> D[Experimentação / Automação]
    D --> E[Validação das Normas ABNT NBR 14724]
```

---

## 2. Normas Técnicas e Padrões Aplicáveis

- **ABNT NBR 14724:2011**: Informação e documentação — Trabalhos acadêmicos — Apresentação.
- **ABNT NBR 10520:2023**: Citações em documentos — Apresentação.

---

## 3. Código LaTeX Canônico dos Slides (Beamer)

Abaixo apresentamos o código-fonte canônico utilizado na apresentação oficial desta aula, utilizando a classe institucional `if-beamer.cls`:

```latex
\documentclass{if-beamer}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[brazil]{babel}

\title{Aula 01: Introdução e Fundamentação Teórica}
\author{Prof. Dr. Pedro Henrique Rocha de Andrade}
\institute{Instituto Federal Fluminense --- Campus Bom Jesus do Itabapoana}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Objetivos da Aula}
  \begin{itemize}
    \item Compreender o método científico hipotético-dedutivo.
    \item Aplicar normas técnicas \textbf{ABNT NBR 14724} na redação.
    \item Dominar a automação tipográfica no ecossistema IFF.
  \end{itemize}
\end{frame}

\end{document}
```

---

## 4. Estudo de Caso e Exercícios Práticos

1. Elaborar a delimitação do problema de pesquisa com base na ABNT NBR 14724.
2. Compilar o código Beamer institucional no VS Code ou Overleaf.

---

## 5. Referências Bibliográficas

- ABNT. **NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
- GIL, A. C. **Como elaborar projetos de pesquisa**. 7. ed. São Paulo: Atlas, 2022.


## 🛠️ Recursos Adicionais e Material Suplementar

- **[[pt-br/resource/latex/modelos-de-documento|🏛️ Guia Oficial de Modelos, Classes e Pacotes ReLaTeX]]** — Exemplos canônicos de código, classes (`ifftese.cls`, `slidesiffmodelo.cls`) e documentação interna.
- **[[pt-br/resource/latex/planejamento-e-cronograma|📅 Planejamento Letivo e Cronograma de Atividades]]** — Matriz analítica de 80h (Terças, 14h30-17h30) e avaliação em 2 bimestres.
- **[[pt-br/resource/latex/codigo-de-conduta-e-diretrizes|📜 Código de Conduta e Diretrizes Acadêmicas]]** — Regimento ético, normas CEP/CONEP e uso transparente de IA.
- **[CTAN (Comprehensive TeX Archive Network)](https://ctan.org/)** — Portal oficial mundial de pacotes LaTeX2e.
- **[ABNT Catálogo de Normas](https://www.abnt.org.br/)** — Acesso e consulta às normas técnicas vigentes.
- **[Overleaf Documentation](https://www.overleaf.com/learn)** — Base de conhecimento e guias práticos sobre compilação TeX.

