---
publish: true
title: ControleEstoque
tags:
- inventario
- estoque
repo: https://github.com/pedroiff0/controle-estoque
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
    <img width=160px height=160px src="https://i.imgur.com/FxL5qM0.jpg" alt="Logo do projeto"></a>
</p>

<h3 align="center">ControleEstoque — Contagem de Inventário</h3>

<div align="center">

[![Status](https://github.com/pedroiff0/ControleEstoque/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/pedroiff0/ControleEstoque/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">Aplicação para contagem rápida de estoque, com persistência de sessão, consolidação de contagens e geração de relatórios CSV/PDF.</p>

## Sumário

- [ Guia Rápido](#guia-rapido)
- [Sobre](#sobre)
- [Instalação](#instalacao)
- [Uso](#uso)
- [Testes & CI](#testes--ci)
- [Contribuição](#contribuicao)

---

## Guia Rápido <a name="guia-rapido"></a>

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r app/requirements.txt
python -m app.source.sistema
```

### POSIX (Linux / macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
python -m app.source.sistema
```

---

## Sobre <a name="sobre"></a>

O **ControleEstoque** fornece uma interface PyQt para contagens, persistência de sessões, validação de schemas e geração de relatórios detalhados (CSV/PDF). O processamento de PDFs para gerar `produtosvm.csv` é suportado via `tabula-py` com fallback por subprocesso.

---

## Instalação <a name="instalacao"></a>

Recomenda-se usar um venv:

```bash
python -m venv .venv
# ative o venv conforme seu shell
pip install -r app/requirements.txt
```

Dependências principais:
- PyQt6 (UI)
- tabula-py (extração de tabelas de PDF)
- reportlab (opcional, para PDF)
- pytest, pytest-qt (testes)

---

## Uso <a name="uso"></a>

Executar a aplicação de contagem:

```bash
python -m app.source.sistema
```

Gerar `produtosvm.csv` a partir do PDF (quando necessário):

```bash
python -m app.source.planilha
```

---

## Testes & CI <a name="testes--ci"></a>

- Os testes estão em `app/tests/` e usam `pytest` (+ `pytest-qt` para testes de UI).
- Para executar localmente:

```bash
# com venv ativo
pytest -q
```

- CI local (mesma ordem do workflow):

```bash
./scripts/run_ci.sh      # POSIX
scripts\run_ci.ps1      # Windows PowerShell
```

---

## Contribuição <a name="contribuicao"></a>

- Mantenha testes e adicione casos para novas funcionalidades.
- Use `pre-commit` para validar formatação e checks antes de commitar.
- Documente mudanças relevantes em `docs/`.

---

**Licença:** MIT

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/controleestoque](https://github.com/pedroiff0/controleestoque)
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
