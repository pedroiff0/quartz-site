---
publish: false
title: "Modelos, Classes (.cls) e Pacotes (.sty) ReLaTeX — Guia e Index Oficial"
created: 2026-08-04 13:33
modified: 2026-08-27 13:33
tags:
  - latex
  - relataex
  - modelos
  - templates
  - iff
cssclasses:
  - page-layout
---

# Modelos, Classes (`.cls`) e Pacotes (`.sty`) — Guia Oficial ReLaTeX

> [!IMPORTANT] **Fonte Única da Verdade para Modelos e Pacotes Institucionais**
> Esta página é o ponto central de referência para todos os modelos oficiais de escrita acadêmica e corporativa desenvolvidos pelo projeto **ReLaTeX** no Instituto Federal Fluminense (IFF) Campus Bom Jesus do Itabapoana.
> 
> Aqui você encontra a especificação de cada classe (`.cls`) e pacote de estilo (`.sty`), **exemplos reais de uso prontos para compilação**, links de download dos pacotes e o redirecionamento direto para a **Aula do Curso (80h)** onde a arquitetura interna e engenharia de cada modelo é estudada a fundo.

---

## 🧭 Guia Rápido de Seleção de Modelo

| Modelo / Pacote | Tipo de Documento / Finalidade | Aula Específica do Curso | Download do Pacote |
| :--- | :--- | :--- | :--- |
| **`ifftese.cls`** | Trabalhos Acadêmicos (TCC, Dissertações, Teses ABNT) | [[pt-br/resource/latex/aula-19-classe-ifftese-engenharia|**Aula 19:** Engenharia da Classe `ifftese.cls`]] | [📥 Baixar `ifftese.cls`](/assets/biblioteca/latex-escrita/classes/ifftese.cls) |
| **`metadados.sty`** | Isolar Dados Biográficos, Banca, Orientação e Título | [[pt-br/resource/latex/aula-17-arquivo-metadados-sty|**Aula 17:** Configuração de `metadados.sty`]] | [📥 Baixar `metadados.sty`](/assets/biblioteca/latex-escrita/pacotes/metadados.sty) |
| **`macros.sty`** | Comandos de Produtividade (Figuras, Quadros, Teoremas) | [[pt-br/resource/latex/aula-18-pacote-macros-sty|**Aula 18:** Produtividade e `macros.sty`]] | [📥 Baixar `macros.sty`](/assets/biblioteca/latex-escrita/pacotes/macros.sty) |
| **`slidesiffmodelo.cls`** | Apresentações Beamer Institucionais Widescreen (16:9) | [[pt-br/resource/latex/aula-21-beamer-slides-defesa|**Aula 21:** Slides de Defesa em Beamer]] | [📥 Baixar `slidesiffmodelo.cls`](/assets/biblioteca/latex-escrita/classes/slidesiffmodelo.cls) |
| **`iffposter.cls`** | Pôsteres Científicos e Banners em Formatos A0 / A1 | [[pt-br/resource/latex/aula-22-poster-cientifico-iffposter|**Aula 22:** Pôster Científico (`iffposter.cls`)]] | [📥 Baixar `iffposter.cls`](/assets/biblioteca/latex-escrita/classes/iffposter.cls) |
| **`relatoriocorp.cls`** | Relatórios Corporativos, Pareceres e Propostas Técnicas | [[pt-br/resource/latex/aula-23-relatorios-corporativos|**Aula 23:** Relatórios Corporativos]] | [📥 Baixar `relatoriocorp.cls`](/assets/biblioteca/latex-escrita/classes/relatoriocorp.cls) |
| **`marca.sty` / `beamerthemecorp.sty`** | Apresentações Executivas e Governança de Paleta Única | [[pt-br/resource/latex/aula-23-relatorios-corporativos|**Aula 23:** Relatórios Corporativos]] | [📥 Baixar Pacote Corporativo](/assets/biblioteca/latex-escrita/pacotes/corporativo.zip) |
| **Scripts de Automação** | Compilação Contínua (`latexmkrc`), Git e Conversão PPTX | [[pt-br/resource/latex/aula-24-latexmk-git-e-submissao|**Aula 24:** Automação, Git e Submissão]] | [[assets/biblioteca/latex-escrita/scripts/latexmkrc|📥 Baixar `latexmkrc`]] |

---

## 1. Classe Acadêmica Canônica: `ifftese.cls`

> **Estudada em detalhes na:** [[pt-br/resource/latex/aula-19-classe-ifftese-engenharia|**Aula 19 — Engenharia de Macros e Estrutura Interna da Classe `ifftese.cls`**]]

A classe **`ifftese.cls`** estende o modelo nacional `abntex2`, ajustando automaticamente as margens para a **ABNT NBR 14724**, gerando a folha de rosto canônica do IFF, ficha catalográfica, folha de aprovação e sumários com pontilhados dinâmicos na norma **ABNT NBR 6027**.

### Exemplo Real de Uso (`main.tex`)

```latex
\documentclass[12pt,openright,twoside,a4paper,english,french,spanish,brazil]{ifftese}

% Importação dos pacotes de isolamento ReLaTeX
\usepackage{metadados} % Configuração biográfica (Autor, Título, Banca)
\usepackage{macros}    % Comandos de produtividade e figuras ABNT

% Gerenciador de Referências ABNT NBR 6023 (BibLaTeX / Biber)
\usepackage[style=abnt,backend=biber,repeatfields=true]{biblatex}
\addbibresource{referencias.bib}

\begin{document}

% Elementos Pré-Textuais Automáticos
\pretextual
\imprimircapa
\imprimirfolhaderosto*
\imprimirfolhadeaprovacao
\tableofcontents*
\cleardoublepage

% Elementos Textuais
\textual
\chapter{Introdução}
Este documento demonstra a integração real entre a classe \texttt{ifftese.cls}, 
os metadados biográficos e as macros de produtividade ABNT.

\chapter{Fundamentação Teórica}
Conforme demonstrado por \cite{silva2026}, a padronização tipográfica reduz 
erros de formatação em teses acadêmicas.

% Elementos Pós-Textuais
\postextual
\printbibliography[title={Referências Bibliográficas}]

\end{document}
```

---

## 2. Isolamento Biográfico: `metadados.sty`

> **Estudado em detalhes na:** [[pt-br/resource/latex/aula-17-arquivo-metadados-sty|**Aula 17 — Arquivo de Configuração de Metadados (`metadados.sty`)**]]

O pacote **`metadados.sty`** centraliza todos os dados de autoria, filiação institucional, título do projeto e composição da banca examinadora. Ele possui detecção gramatical para flexionar automaticamente termos como *"Orientador(a)"* e *"Coorientador(a)"*.

### Exemplo Real de Configuração (`metadados.sty`)

```latex
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{metadados}[2026/08/04 Metadados Institucionais IFF]

% --- Dados da Pesquisa e Autoria ---
\titulo{Arquitetura Modular em LaTeX para Automação de Trabalhos Acadêmicos}
\autor{Maria Eduarda Fernandes}
\local{Bom Jesus do Itabapoana -- RJ}
\data{2026}
\instituicao{%
  INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA FLUMINENSE
  \par
  CAMPUS BOM JESUS DO ITABAPOANA
  \par
  CURSO DE BACHARELADO EM ENGENHARIA DE COMPUTAÇÃO}
\tipotrabalho{Trabalho de Conclusão de Curso (TCC)}

% --- Natureza Acadêmica ---
\preambulo{Trabalho de Conclusão de Curso apresentado ao Curso de Bacharelado em Engenharia de Computação do Instituto Federal Fluminense como requisito parcial para obtenção do título de Bacharela em Engenharia de Computação.}

% --- Orientação e Banca ---
\orientador{Prof. Dr. Pedro Henrique Rocha de Andrade}
\orientadorfeminino{nao}
\coorientador{Profa. Dra. Ana Clara Souza}
\coorientadorfeminino{sim}

% Membros da Banca
\newcommand{\membroA}{Prof. Dr. Carlos Eduardo Lima -- IFF Campus Bom Jesus}
\newcommand{\membroB}{Profa. Dra. Juliana Mendes -- UFRJ}
```

---

## 3. Banco de Produtividade: `macros.sty`

> **Estudado em detalhes na:** [[pt-br/resource/latex/aula-18-pacote-macros-sty|**Aula 18 — Produtividade e Macros Personalizadas (`macros.sty`)**]]

A biblioteca **`macros.sty`** substitui blocos repetitivos de código LaTeX por comandos concisos e blindados contra erros de formatação na NBR 14724 e normas IBGE 1993.

### Exemplo Real de Inserção com Macros

```latex
% Inserindo uma figura com legenda superior ABNT e fonte inferior com 1 comando:
% Sintaxe: \inserirfigura{escala}{caminho_arquivo}{legenda}{fonte}{label}
\inserirfigura{0.8}{diagrama.png}{Fluxo de compilação contínua no ecossistema ReLaTeX}{Fonte: O autor (2026).}{fig:fluxo_relatex}

% Inserindo um Teorema ou Definição numerada automaticamente:
\begin{definicao}[Teorema da Separação de Preocupações]
A formatação tipográfica de um trabalho acadêmico deve permanecer ortogonal 
ao seu conteúdo argumentativo.
\label{def:separacao}
\end{definicao}
```

---

## 4. Slides de Defesa Institucionais: `slidesiffmodelo.cls`

> **Estudada em detalhes na:** [[pt-br/resource/latex/aula-21-beamer-slides-defesa|**Aula 21 — Slides de Defesa Institucionais em Beamer**]]

A classe **`slidesiffmodelo.cls`** formata apresentações Beamer em proporção widescreen **16:9**, herdando os dados do arquivo `metadados.sty` e aplicando a paleta oficial verde (`#2D6238`) e vermelha (`#B3282D`) do Instituto Federal Fluminense.

### Exemplo Real de Apresentação de Defesa (`defesa.tex`)

```latex
\documentclass[aspectratio=169]{slidesiffmodelo}
\usepackage{metadados}
\usepackage{macros}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Objetivos da Investigação}
  \begin{block}{Objetivo Geral}
    Desenvolver um ecossistema unificado para edição acadêmica que assegure 
    100\% de conformidade com a ABNT NBR 14724.
  \end{block}
  \vspace{0.3cm}
  \begin{alertblock}{Justificativa Institucional}
    A eliminação de ajustes manuais de margens reduz o tempo de revisão 
    em 65\% na pós-graduação.
  \end{alertblock}
\end{frame}

\begin{frame}{Resultados Principais}
  % Chamada de tabela IBGE simplificada via macro
  \begin{center}
    \inserirtabelasimples{Tempo de formatação: Word vs. ReLaTeX}{0.7\textwidth}{%
      \toprule
      \textbf{Ferramenta} & \textbf{Tempo Médio (h)} & \textbf{Conformidade ABNT} \\
      \midrule
      Microsoft Word & 42,5 & 78\% \\
      ReLaTeX (ifftese) & 3,2 & 100\% \\
      \bottomrule
    }{Fonte: Dados de pesquisa de campo (2026).}{tab:comparativo}
  \end{center}
\end{frame}

\end{document}
```

---

## 5. Pôster Científico Institucional: `iffposter.cls`

> **Estudada em detalhes na:** [[pt-br/resource/latex/aula-22-poster-cientifico-iffposter|**Aula 22 — Pôster Científico em LaTeX (`iffposter.cls`)**]]

A classe **`iffposter.cls`** padroniza banners científicos nos formatos **A0** e **A1** para feiras, congressos e mostras de iniciação científica, desenhando cabeçalho institucional, logomarcas de fomento e colunas balanceadas.

### Exemplo Real de Pôster (`poster.tex`)

```latex
\documentclass[a0paper,portrait]{iffposter}
\usepackage{metadados}
\usepackage{multicol}

\begin{document}
\imprimircapaposter

\begin{multicols}{3}

\section*{1. Introdução}
A apresentação em eventos científicos requer legibilidade visual de até 2 metros 
de distância. A classe \texttt{iffposter.cls} ajusta dinamicamente a escala 
de fontes e espaçamento entre colunas.

\section*{2. Metodologia}
Os experimentos foram executados em ambiente Linux com o motor \texttt{PDFLaTeX}, 
analisando 120 trabalhos de iniciação científica do IFF.

\section*{3. Conclusão}
O layout vetorial em 3 colunas reduziu o corte de texto e evitou quebras de tabela.

\end{multicols}
\end{document}
```

---

## 6. Documentação Executiva: `relatoriocorp.cls` e `marca.sty`

> **Estudada em detalhes na:** [[pt-br/resource/latex/aula-23-relatorios-corporativos|**Aula 23 — Relatórios Corporativos e Documentação Técnica**]]

No mundo corporativo e industrial, a identidade de marca é governada pelo arquivo central **`marca.sty`**. A classe **`relatoriocorp.cls`** gera pareceres técnicos, diagnósticos e relatórios com sumário executivo em destaque, enquanto **`beamerthemecorp.sty`** produz o pitch deck corporativo a partir da mesma paleta.

### Exemplo Real de Relatório Corporativo (`relatorio-tecnico.tex`)

```latex
\documentclass[11pt,a4paper]{relatoriocorp}
\usepackage{marca} % Importa a cor da empresa e logotipo central

\titulo{Diagnóstico de Eficiência em Infraestrutura Computacional}
\autor{Eng. Pedro Henrique Rocha de Andrade}
\data{\today}

\begin{document}
\imprimircapacorporativa

\section{Sumário Executivo}
\begin{caixaalerta}{Governança e Redução de Custos}
A migração dos servidores departamentais para conteinerização gerou 
uma economia estimada em R\$ 140.000,00 anuais para o setor de TI.
\end{caixaalerta}

\section{Indicadores Financeiros e de Desempenho}
Os dados auditados são apresentados no quadro executivo abaixo, de acordo 
com as normas de apresentação corporativa.

\end{document}
```

---

## 7. Scripts de Automação, Compilação e Conversão

> **Estudados em detalhes na:** [[pt-br/resource/latex/aula-24-latexmk-git-e-submissao|**Aula 24 — Automação com `latexmk`, Git e Submissão**]]

### Arquivo de Configuração de Automação (`latexmkrc`)

Coloque o arquivo `latexmkrc` na raiz do projeto para que o comando `latexmk -pdf` execute toda a cadeia de compilação sem intervenção humana:

```perl
$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';
$biber = 'biber %O %S';
$clean_ext = "aux log out toc lof lot bbl blg run.xml bcf synctex.gz";
```

### Script de Conversão para PowerPoint Institucional (Pandoc / Shell)

Para converter qualquer conjunto de notas Markdown em uma apresentação PowerPoint `.pptx` preservando o layout widescreen:

```bash
#!/usr/bin/env bash
# Uso: ./gerar-pptx.sh aula-01-epistemologia-problematizacao.md
INPUT_FILE="$1"
OUTPUT_FILE="${INPUT_FILE%.md}_institucional.pptx"

echo "=== Convertendo ${INPUT_FILE} para PPTX Institucional ==="
pandoc "${INPUT_FILE}" \
  -o "${OUTPUT_FILE}" \
  --reference-doc=template-iff-widescreen.pptx \
  --slide-level=2 \
  --highlight-style=tango

echo "=== Concluído: ${OUTPUT_FILE} gerado com sucesso! ==="
```
