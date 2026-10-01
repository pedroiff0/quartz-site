---
publish: true
title: Planilhador
tags:
- nfce
- planilha
repo: https://github.com/pedroiff0/planilhador
status: privado
cssclasses:
- page-layout
created: 2026-09-14 11:17
modified: 2026-09-30 13:05
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

<p align="center">
  <a href="" rel="noopener">
    <img width=160px height=160px src="https://i.imgur.com/FxL5qM0.jpg" alt="Logo do projeto"></a>
</p>

<h3 align="center">Planilhador — Ferramentas NFCe</h3>

<div align="center">

[![Status](https://github.com/pedroiff0/Planilhador/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/pedroiff0/Planilhador/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">Ferramentas para processar XMLs de NFCe e gerar relatórios automatizados.</p>

## Sumário

- [ Guia Rápido](#guia-rapido)
- [Sobre](#sobre)
- [Instalação](#instalacao)
- [Uso](#uso)
- [Testes & CI](#testes--ci)
- [Contribuição](#contribuicao)

---

## Guia Rápido <a name="guia-rapido"></a>

### Windows - Setup em 3 passos

```powershell
# 1. Criar/ativar virtualenv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Rodar testes
python -m pytest -q -v
```

### POSIX (Linux / macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q -v
```

 **Guia completo:** veja `QUICK_START.md` na raiz do meta-repositório

---

## Sobre <a name="sobre"></a>

O pacote **Planilhador** contém:
- `nfce.py` — processador que lê XMLs de NFCe, extrai dados e gera ODS/PDF
- `monitor_nfce.py` — observador de novas notas que aciona o processador automaticamente

---

## Instalação <a name="instalacao"></a>

Recomenda-se usar um ambiente virtual:

```bash
python -m venv .venv
# Ative o venv (conforme seu shell)
pip install -r requirements.txt
```

Dependências principais:
- `pyexcel-ods3` — exporta ODS
- `fpdf` — gera PDF
- `watchdog` — monitor de diretório
- `pytest` — framework de testes

---

## Uso <a name="uso"></a>

Gerar relatórios do mês atual:

```bash
python -m app.source.nfce
```

Monitorar a pasta do mês atual e gerar automaticamente:

```bash
python -m app.source.monitor_nfce
```

Personalizar saída dos relatórios:
- Defina `NFCE_OUTPUT_DIR` para alterar o diretório de saída

---

## Testes & CI <a name="testes--ci"></a>

A suíte de testes usa `pytest` (veja `app/tests/`).

No Windows, o script `scripts/run_ci.ps1` irá preferir o interpretador do `.venv` (se presente) e executará pre-commit, linters e testes.

Rotinas de CI local:

```bash
# Executar pre-commit, linters e testes usando o python do venv quando disponível
./scripts/run_ci.sh      # POSIX
scripts\run_ci.ps1      # Windows PowerShell
```

---

## Contribuição <a name="contribuicao"></a>

- Abra issues/pull requests no repositório do subprojeto.
- Mantenha `app/.pre-commit-config.yaml` e `app/.flake8` atualizados.
- Adicione testes para novo comportamento em `app/tests/`.

---

**Licença:** MIT

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/planilhador](https://github.com/pedroiff0/planilhador)
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
