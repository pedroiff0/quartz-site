---
publish: true
title: Caixas
tags:
- controle-de-caixa
- relatorio
repo: https://github.com/pedroiff0/caixas
status: privado
cssclasses:
  - page-layout
created: 2026-09-14 11:17
modified: 2026-10-01 20:14
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Bot logo"></a>
</p>

<h3 align="center">Caixas — Gerenciamento de Caixas</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
[![CI](https://github.com/pedroiff0/Caixas/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroiff0/Caixas/actions)

</div>

---

<p align="center">Aplicação web para registrar fechamentos diários de caixa, gerar relatórios e manter histórico — construída com Flask, SQLAlchemy e Alembic.</p>

## Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Deploying your own app](#deployment)
- [Built Using](#built_using)
- [[docs/TODO]]
- [[CONTRIBUTING|Contributing]]
- [Authors](#authors)
- [Acknowledgements](#acknowledgement)

## About <a name = "about"></a>

`Caixas` é um sistema leve para controlar o fluxo diário de caixa em pequenos estabelecimentos. Ele permite criar e editar fechamentos diários, gerar relatórios e imprimir históricos.

---

## Demo / Working <a name = "demo"></a>

A interface usa templates Jinja2 e AdminLTE; veja `build/adminlte_tmp` para screenshots e recursos.

---

## How it works <a name = "working"></a>

- O modelo `FechamentoDiario` registra valores de vendas, depósitos, vales e o total contado na gaveta.
- As rotas expõem views HTML e endpoints REST (ex.: `/api/troco_anterior`).
- `scripts/migrate_snapshot.py` aplica migrations a um DB alvo; em CI o script cria um DB temporário e prepara o esquema.

---

## Usage <a name = "usage"></a>

### Run in development

```bash
# create/activate virtualenv
pip install -r app/requirements.txt
python app/run.py
```

### Apply migrations

```bash
python scripts/migrate_snapshot.py sqlite:///dev.db
flask db upgrade
```

---

## Getting Started <a name = "getting_started"></a>

### Prerequisites

- Python 3.10+
- Virtual environment

### Installing

```bash
git clone https://github.com/pedroiff0/Caixas.git
cd Caixas
python -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
```

---

## Deploying your own app <a name = "deployment"></a>

- Use a WSGI server in production (Waitress is provided as a minimal option).
- Ensure `DATABASE_URL` and `SECRET_KEY` are set in production.
- Do not enable `ALLOW_CREATE_PROD_DB` in production unless you know the implications.

---

## Built Using <a name = "built_using"></a>

- Flask - Web framework
- SQLAlchemy - ORM
- Alembic / Flask-Migrate - Migrations
- Waitress - WSGI server

---

## Authors <a name = "authors"></a>

- Pedro Iff — https://github.com/pedroiff0

## Acknowledgements <a name = "acknowledgement"></a>

- AdminLTE (UI)
- Flask community

---

> See `docs/TODO.md` for planned improvements and tasks.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/caixas](https://github.com/pedroiff0/caixas)
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
