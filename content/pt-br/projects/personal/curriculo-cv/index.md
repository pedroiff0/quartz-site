---
publish: true
title: Currículo (CV)
tags:
- multilingue
- pt-en-es-fr
repo: https://github.com/pedroiff0/cv
status: público
cssclasses:
  - page-layout
created: 2026-09-14 11:17:03-03:00
modified: 2026-09-30T13:05:50-03:00
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Curriculum Vitae

---

## Project-specific build (Makefile)

This repository includes a `Makefile` with convenient targets for building the CVs:

Notes:

This repository contains a CV template built using the AltaCV class (provided as `altacv.cls`).

Examples:

```bash
make englishCV
make portugueseCV
make clean
```

---

## Basic CV info

Where to edit your personal details and content:

- Name and tagline: edit the `\name{...}` and `\tagline{...}` commands in `english.tex` and `portuguese.tex` (the files included by `main.tex`).
- Photo: change the image file referenced by `\photo{<size>}{<filename>}` (currently `curriculo` / `curriculo.jpeg`). Place new images in the repository root or update the path.
- Contact block: edit `\personalinfo{...}` in `english.tex` / `portuguese.tex` to update `\email`, `\phone`, `\location`, and links (GitHub, LinkedIn, ORCID, etc.).
- Sections and items: the CV body uses AltaCV helpers such as `\cvsection{}`, `\cvevent{title}{subtitle}{dates}{location}`, `\cvtag{}`, and `\cvskill{}`. Modify those in the language files to change content.
- Bibliography: `sample.bib` is the bibliography file used by `biblatex` — edit or replace it and re-run `make englishCV` / `make portugueseCV` to regenerate citations.
- Icons: the class maps legacy `\fa...` macros to Font Awesome names. Do not remove `\fa` macros from the documents — if an icon fails to render, prefer switching engine to LuaLaTeX or installing the required fonts (Font Awesome, academicons) rather than stripping macros.

Quick edit workflow:

1. Edit `english.tex` or `portuguese.tex` with your personal data and content.
2. Run `make englishCV` or `make portugueseCV` (or `make all`).
3. The Makefile will build the PDF and automatically remove auxiliary files; generated PDFs are preserved unless you run `make distclean`.

If you need help updating a specific field (name, photo, contact), tell me which file and I can apply the change.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/curriculo-cv](https://github.com/pedroiff0/curriculo-cv)
- **Índice de Projetos:** [[pt-br/projects/projetos-publicos|Projetos Públicos]]

---

<p align=center>
  <a href="https://github.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://linkedin.com/in/pedro-andrade-iff" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://instagram.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="mailto:pedro.andrade@iff.edu.br"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://pedroiff.com" target="_blank"><img src="https://img.shields.io/badge/Website-000000?style=flat-square&logo=googlechrome&logoColor=white" alt="Website" /></a>
</p>

<p align=center>
  <sub>© 2026 <b><a href="https://pedroiff.com">Pedro Rocha</a></b> — Computer Engineering &amp; Computational Astrophysics</sub><br />
  <sub>Made with <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M10 2v2'/><path d='M14 2v2'/><path d='M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1'/><path d='M6 2v2'/></svg>" width="16" height="16" valign="middle" alt="coffee" />, <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='m16 18 6-6-6-6'/><path d='m8 6-6 6 6 6'/></svg>" width="16" height="16" valign="middle" alt="code" /> and <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='3'/><path d='M3 12a9 9 0 0 1 9-9 9 9 0 0 1 9 9 9 9 0 0 1-9 9 9 9 0 0 1-9-9'/><path d='M5.5 5.5a13 13 0 0 0 13 13'/><path d='M18.5 5.5a13 13 0 0 1-13 13'/></svg>" width="16" height="16" valign="middle" alt="astrophysics" /> by <b><a href="https://github.com/pedroiff0">Pedro Henrique Rocha de Andrade</a></b></sub>
</p>
