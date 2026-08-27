---
publish: true
title: "ReLaTeX: Classe LaTeX para Trabalhos Acadêmicos do IFF"
created: 2026-06-18
modified: 2026-07-31T23:45:03.282-03:00
published: 2026-07-31T23:45:03.282-03:00
tags:
  - latex
  - engenharia-de-software
  - automacao
cssclasses:
  - page-layout
---

# 📄 ReLaTeX: Classe LaTeX para Trabalhos Acadêmicos do IFF

> [!note] Resumo
> Desenvolvimento da classe tipográfica `ifftese.cls` e do pacote de extensão `macros.sty` para LaTeX, com o objetivo de automatizar o cumprimento das normas ABNT (NBR 14724, NBR 6027) em trabalhos acadêmicos do Instituto Federal Fluminense — reduzindo drasticamente o tempo gasto formatando manualmente capas, tabelas, figuras e elementos pré/pós-textuais. A ser apresentado no CONEPE 2026 (Campos Guarus, RJ, 21 a 23 de setembro), em coautoria com [Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja), [Maria Luiza Linhares Dantas](https://www.mlldantas.com) e [Ana Mara Figueiredo de Oliveira](https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora)

<div class="media-carousel">
  <a href="/pt-br/research/relatex" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="ReLaTeX" />
    <div class="slide-caption">Classe LaTeX ifftese.cls</div>
  </a>
</div>

## 🌌 O problema

A redação de documentos acadêmicos sob as diretrizes da ABNT (NBR 14724 para trabalhos acadêmicos, NBR 6023 para referências, NBR 6027 para sumários) impõe uma estrutura rígida, mas o LaTeX — a ferramenta mais indicada tecnicamente para isso, por seu controle tipográfico e ambiente de equações superior a processadores visuais como o Word — tem uma curva de aprendizado alta. A diferença de paradigma explica o porquê: processadores WYSIWYG ("o que você vê é o que você tem") são fáceis de começar mas difíceis de diagramar sem quebrar o layout; o LaTeX é WYSIWYM ("o que você vê é o que você quer dizer") — o iniciante erra bastante e depende de consulta constante, mas, superada a curva de aprendizado, ganha um processo de escrita muito mais confiável e alinhado às normas.

## 🎯 Objetivo

Desenvolver uma classe tipográfica para LaTeX voltada ao usuário típico do IFF, que respeite as diretrizes da ABNT e as particularidades locais (logos e símbolos institucionais), atenuando a curva de aprendizado de quem nunca usou LaTeX e agilizando o trabalho de quem já usa.

## 🔧 Metodologia

O projeto usou como base as classes `abntex2` e `article`, com o pacote bibliográfico `abntex2cite` (compatibilidade ABNT), compilado via TeX Live (`pdflatex`/`bibtex`), com apoio de TeXPage, CTAN e Overleaf como ambientes online. O trabalho foi dividido em três etapas:

1. **Normas** — mapeamento das restrições visuais e estruturais da NBR 14724 e NBR 6027, traduzidas na classe `ifftese.cls`.
2. **Comandos auxiliares** — o pacote `macros.sty`, criado para evitar a sintaxe primitiva do LaTeX e reduzir erros de compilação.
3. **Arquivo principal** — consolidação num único `main.tex`, com todos os ambientes da NBR 14724 já preenchidos como comandos prontos.

## 📊 Resultados

A arquitetura segue a estrutura normativa da ABNT (elementos pré-textuais, textuais e pós-textuais), eliminando a necessidade de o usuário manipular pacotes gráficos ou formatação complexa diretamente:

- **Variáveis de controle** (`\frenteVerso`, `\corlink`, `\sumarioEscada`, `\numeracaoPorSecao`, `\capaiff`, `\legendacurta`, `\cabecalho`) — flags sim/não que geram automaticamente margens, cabeçalhos, links e numeração corretos.
- **Elementos pré-textuais** — variáveis semânticas (`\autor`, `\titulo`, `\orientador`, `\local`, `\instituicao`, `\data`) alimentam macros como `\capa` e `\contracapa`, que renderizam páginas completas já formatadas conforme a norma.
- **Elementos textuais** — a macro `\inserirfigura` encapsula, numa única linha, o dimensionamento, alinhamento, legenda, fonte e rótulo (`label`) para referência cruzada de uma figura. `\inserirtabela` e `\inserirquadro` automatizam a distinção normativa do IBGE entre tabelas e quadros, enviando os metadados diretamente para as listas do pré-texto.
- **Elementos pós-textuais** — macros próprias convertem a numeração de apêndices/anexos de numérica para alfabética sem corromper a numeração dos capítulos, e padronizam a chamada de glossários e índices remissivos.

## 🧾 Conclusão

O encapsulamento dessas rotinas em macros parametrizadas cumpriu o objetivo: reduzir o tempo operacional de formatação e democratizar o rigor tipográfico do LaTeX na produção técnico-científica do IFF, blindando o usuário contra erros de sintaxe e de referências cruzadas. Como desdobramento, está em fase de testes uma interface web opcional, no estilo do Overleaf, focada exclusivamente nesta classe — pensada para quem prefere preencher formulários a editar código-fonte diretamente.

## 🏆 Apresentações

Este projeto será apresentado no **CONEPE 2026** (Congresso de Ensino, Pesquisa e Extensão do IFF _Campus_ Guarus), de 21 a 23 de setembro de 2026.

## 🔗 Referências e correlatos

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 14724: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro, 2011.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 6027: Informação e documentação — Sumário — Apresentação. Rio de Janeiro, 2012.
- KNUTH, D. E. _The TeXbook_. Reading, Massachusetts: Addison-Wesley, 1986.
- LAMPORT, L. _LaTeX: A Document Preparation System_. 2ª ed. Reading, Massachusetts: Addison-Wesley, 1994.
- EQUIPE ABNTEX2 — [a classe abntex2](https://github.com/abntex/abntex2), base de compatibilidade ABNT usada neste projeto.
- CONEPE 2026 — a cobertura da apresentação entra aqui depois do evento (setembro de 2026).
- [[pt-br/resource/latex|LaTeX e Escrita Acadêmica]] — o curso construído em cima deste projeto; as aulas 06 a 08 documentam `ifftese.cls`, `macros.sty` e `metadados.sty` linha a linha.
- [[pt-br/resource/latex/modelos-corporativos|Modelos Corporativos]] — a mesma arquitetura de classe aplicada fora da academia, com manual de marca no lugar da ABNT.
