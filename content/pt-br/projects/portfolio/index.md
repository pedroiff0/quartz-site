---
publish: true
title: Portfólio (este site)
created: 2026-08-08 13:04
modified: 2026-10-01 20:14
tags:
- portfolio
- pagina-unica
- multilingue
- sem-framework
repo: https://github.com/pedroiff0/portfolio
status: público
cssclasses:
  - page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

# Portfolio — Pedro Rocha

Página de portfólio estática (GitHub Pages) — tema astronomia, design profissional,
animações e conteúdo em uma única página com navegação por *anchors* e seções
reveláveis (conteúdo "invisível" que aparece ao clicar).

## Conteúdo

- **Sobre mim** — trajetória, formação (Eng. de Computação / IFF) e atuação (PIBIC/CNPq).
- **Projetos** (cartões clicáveis): ReLaTeX, Sistema Acadêmico, Sistema de Avaliações e Currículo (LaTeX).
- **Pesquisa** (accordion): arqueologia galáctica, anomaly_detection (GAIA×GALAH), simulações de aglomerados e SpectraViewer.
- **Currículo**, **Lattes** e **Contato**.

## Estrutura

```
index.html              # página única (single-page, anchors)
assets/css/style.css    # tema deep-space, glassmorphism, animações
assets/js/projects.js   # dados dos projetos e da pesquisa
assets/js/main.js       # starfield canvas, scroll reveal, accordions, nav
```

## Como editar

**A fonte é o Markdown, não o JS.** Nunca edite `assets/js/projects.js` à mão:
ele é compilado e sobrescrito pelo pre-commit.

- Projetos, bolsas e contatos: `src/portfolio.md`
- Textos de interface (nav, hero, rótulos, i18n): `src/interface.yaml`
- Cores/tipografia/animações: `assets/css/style.css`

Depois de editar:

```bash
python3 tools/build.py     # regenera assets/js/projects.js
node tools/verify.js       # confere contra o snapshot .orig
```

O hook `pre-commit` já roda o build e faz `git add` do JS gerado.

### Formato de um projeto

```
### Nome do Projeto
repo: https://github.com/pedroiff0/foo     (opcional — sem ele, o cartão
slug: foo                                   mostra "sem repositório público")
stack: Node.js, Express, MongoDB
tags: Full-stack, Web App
cat: software | academico | pesquisa | pessoal
visibility: público | privado | planejamento | elaboracao
icon: cash

 texto em português
 english text
 texto en español
 texte en français
```

Idioma faltando herda o . O campo `slug:` é opcional e só serve para casar
com a nota já existente no quartz-site (ver abaixo); sem ele, o slug é
derivado do nome.

## Sincronizar com o quartz-site

`src/portfolio.md` é a **fonte única** dos projetos: as notas de
`content/<lang>/projects/` do quartz-site são geradas a partir dele.

```bash
python3 tools/gen_quartz.py            # dry-run: mostra o que mudaria
python3 tools/gen_quartz.py --write    # aplica
python3 tools/gen_quartz.py --check    # exit 1 se dessincronizado
```

O script gera as quatro línguas (`pt-br`, `en`, `es`, `fr`) e só controla:

- os campos de frontmatter `title`, `tags`, `repo`, `status`;
- o bloco entre `<!-- gerado por ... -->` e `<!-- fim do bloco gerado -->`.

O resumo, o rótulo de repositório e o status saem traduzidos por idioma. O
`title` e as `tags` ficam no original de propósito: o título é nome próprio do
projeto, e as tags são usadas pelo Quartz para agrupar notas — traduzi-las
fragmentaria cada grupo em quatro.

Todo o resto — `publish`, `created`, `password`, e principalmente o corpo
escrito à mão — é preservado. Em notas que já têm texto humano o bloco entra
em modo reduzido (só stack e repositório), para não duplicar o resumo.

O caminho do site vem de `$QUARTZ_SITE` (padrão:
`/home/pedro/Repositorios/pessoal/quartz-site`).

**Atenção:** o `content/` do quartz-site é um vault Obsidian sincronizado por
Syncthing e vive sujo no git. O script nunca commita — rode `git status` lá e
separe as mudanças à mão.

## Rodar localmente

```bash
cd portfolio
python3 -m http.server 8000
# abra http://localhost:8000
```

## Publicar no GitHub Pages

1. Faça push deste repositório para `pedroiff0/portfolio`.
2. Em **Settings → Pages**, escolha a branch `master` (ou `main`) e a pasta `/ (root)`.
3. O site ficará em `https://pedroiff0.github.io/portfolio/`.

Não depende de build: é HTML/CSS/JS puro, servido diretamente.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/portfolio](https://github.com/pedroiff0/portfolio)
- **Índice de Projetos:** [[01-projetos/site-publico/projetos-publicos|Projetos Públicos]]

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
