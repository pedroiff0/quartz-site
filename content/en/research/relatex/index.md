---
publish: true
title: "\"ReLaTeX: LaTeX Class for Academic IFF Works\""
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

# 📄 ReLaTeX: LaTeX Class for Academic IFF Works

> [!note] Summary
> Development of the typographic class `iffthesis. cls` and the 'macros.sty' extension package for LaTeX, with the aim of automating compliance with ABNT standards (NBR 14724, NBR 6027) in academic works of the Fluminense Federal Institute — drastically reducing the time spent manually formatting covers, tables, figures and pre/post-textual elements. To be presented at CONEPE 2026 (Campos Guarus, RJ, 21-23 September), in co-authorship with [Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja),[Maria Luiza Linhares Dantas](https://www.mlldantas.com) and [Ana Mara Figueiredo de Oliveira](https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora)


<div class="media-carousel">
  <a href="/pt-br/research/relatex" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="ReLaTeX" />
    <div class="slide-caption">Class LaTeX iffthesis. cls</div>
  </a>
</div>


## 🌌 The Problem

 The writing of academic documents under ABNT guidelines (NBR 14724 for academic works, NBR 6023 for references, NBR 6027 for summaries) imposes a rigid structure, but LaTeX — the most technically suitable tool for this, for its typographical control and equations environment superior to visual processors like Word — has a high learning curve. The paradigm difference explains why: WYSIWYG processors ("what you see is what you have") are easy to get but difficult to diagram without breaking the layout; LaTeX is WYSIWYM ("what you see is what you mean") — the beginner misses a lot and depends on constant query, but, after the learning curve, wins a much more reliable writing process and aligned to standards.

## 🎯 Objective

 Develop a typographic class for LaTeX focused on the typical user of the IFF, which respects ABNT guidelines and local particularities (logs and institutional symbols), attenuating the learning curve of those who have never used LaTeX and accelerating the work of those who already use it.

## 🔧 Methodology

 The project used the classes `abntex2` and `article' as a basis, with the bibliographic package `abntex2cite` (ABNT compatibility), compiled via TeX Live (`pdflatex`/`bibtex`), with TeXPage, CTAN and Overleaf support as online environments. The work was divided into three stages:

1. **Standards** — mapping of visual and structural constraints of NBR 14724 and NBR 6027, translated into class `iffthesis. cls`.
2. **Auxiliary Commands** — the 'macros.sty' package, created to avoid the primitive syntax of LaTeX and reduce build errors.
3. **Main archive** —consolidation into a single 'main.tex', with all NBR 14724 environments already filled as ready commands.

## 📊 Results

 The architecture follows the normative structure of ABNT (pretextual, textual and posttextual elements), eliminating the need for the user to manipulate graphics packages or complex formatting directly:

- **Control variables**(\frontVerso`, `\corlink`, `\sumarioScala`, `\numberBySecao`, `\capaiff`, `\legendacurita`, `\head¿) — flags yes/no that automatically generate margins, headers, links and correct numbering.
- * Pretextual elements ** — semantic variables (`\author`, `\title`, `\guideer`, `\local`, `\institutional`, `\data`) feed macros such as `\capa` and `\countercapa`, which render complete pages already formatted as standard.
- * Textual elements** — the macro `\insertfigura` encapsulates, in a single line, the sizing, alignment, caption, font and label (`label`) for cross reference of a figure. `\insertabela` and `\insertabela` automate the normative distinction of IBGE between tables and tables, sending the metadata directly to the pretext lists.
- * Posttextual elements ** — own macros convert the numbering of appendages/appendices from numerical to alphabetical without corrupting the numbering of chapters, and standardize the call of glossaries and remissive indexes.

## 🧾 Conclusion

 The encapsulation of these routines in parameterized macros met the objective: to reduce the operational time of formatting and democratize the typographic rigor of LaTeX in the technical-scientific production of the IFF, shielding the user against syntax errors and cross-references. As a deployment, an optional Overleaf-style web interface is in the testing phase, focused exclusively on this class — designed for those who prefer to fill out forms rather than edit source code directly.

## 🏆 Presentations

 This project will be presented at **CONEPE 2026** (Congress on Education, Research and Extension of the IFF  Campus Guarus), from 21 to 23 September 2026.

## 🔗 References and correlations

- BRAZILIAN ASSOCIATION OF TECHNICAL STANDARDS. NBR 14724: Information and documentation — Academic work — Presentation. Rio de Janeiro, 2011.
- BRAZILIAN ASSOCIATION OF TECHNICAL STANDARDS. NBR 6027: Information and documentation — Summary — Presentation. Rio de Janeiro, 2012.
- KNUT, D. E.  The TeXbook . Reading, Massachusetts: Addison-Wesley, 1986.
- LAMPORT, L.  LaTeX: A Document Preparation System . 2nd ed. Reading, Massachusetts: Addison-Wesley, 1994.
- TEAM ABNTEX2 —[class abntex2](https://github.com/abntex/abntex2), ABNT compatibility base used in this project.
- CONEPE 2026 — the coverage of the presentation enters here after the event (September 2026).
- [[pt-br/resource/latex|LaTeX and Academic Writing]]— the course built on top of this project; classes 06 to 08 document 'ifftese'. cls`, `macros.sty` and `metadata. sty` line by line.
- [[pt-br/resource/latex/modelos-corporativos|Corporate Models]]— the same class architecture applied outside the academy, with a brand manual in place of ABNT.

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
