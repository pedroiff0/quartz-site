---
publish: true
title: LevantamentoEstoque
tags:
- estoque
- compras
repo: https://github.com/pedroiff0/levantamento-estoque
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
 <img width=200px height=200px src="https://i.imgur.com/FxL5qM0.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Levantamento de Estoque</h3>

<div align="center">

[![Status](https://github.com/pedroiff0/LevantamentoEstoque/actions/workflows/ci.yml/badge.svg?event=push)](https://github.com/pedroiff0/LevantamentoEstoque/actions/workflows/ci.yml)
[![GitHub Issues](https://img.shields.io/github/issues/pedroiff0/LevantamentoEstoque)](https://github.com/pedroiff0/LevantamentoEstoque/issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Pequeno sistema para realizar levantamentos de estoque por cor/tamanho, com persistência de sessão, extração de dados de PDF e geração de relatórios. <br></p>

## Sumário

- [Sobre](#sobre)
- [Uso](#uso)
- [Começando](#comecando)
- [Make & Scripts](#make--scripts)
- [Tecnologias](#tecnologias)
- [Testes](#testes)
- [Autores](#autores)

## About <a name="about"></a>

Pequeno sistema para contagens rápidas, persistência de sessão e exportações para análise.

## Recursos principais
- Interface PyQt6 otimizada para input rápido de contagens por produto, cor e tamanho.
- Gerenciamento simples de sessões (JSON) para recuperar trabalhos interrompidos.
- Extração de `produtosvm.csv` a partir de `produtosvm.pdf` (via `tabula-py`), com fallback por subprocesso.
- Geração de relatórios em PDF (ReportLab) e exportação de CSVs de análise.

## Estrutura de diretórios
- `app/source/` — código-fonte modular (ui, session, planilha, pdf_export, utils, startup, sistema).
- `docs/` — documentação do projeto (instalação, arquitetura, testes e exemplos).
- `app/tests/` — testes unitários (pytest).
- `app/saidas/` — pastas geradas em execução (Sessions, Relatorios, Contagens, Levantamentos).

## Instalação rápida

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r app/requirements.txt
```

## Make & Scripts
- `make install` — cria/atualiza `.venv`, faz upgrade do `pip`, executa `scripts/clean_pycache.py --delete` se presente, instala dependências e roda checks locais.
- `make ci` — executa `./scripts/run_ci.sh` (pre-commit, pyflakes, flake8, pytest).
- `make run|stop|status|restart` — controla o serviço via `scripts/run_*.sh`.

## Executar

```bash
python -m app.source.sistema
```

## Testes
- Executar todos os testes:
```bash
pytest -q
```
- Para rodar um teste específico use:
```bash
pytest -q app/tests/test_planilha_unit.py::test_combine_dataframes
```

## Executar CI localmente (mesma ordem do workflow)
O repositório inclui um script que executa localmente os mesmos passos do CI em ordem exata (pré-commit, pyflakes, flake8, pytest):

- Via script:

```bash
./scripts/run_ci.sh
```

- Ou usando Make:

```bash
make ci
```

O script falhará ao primeiro passo que retornar código de erro (comportamento 'fail-fast').
## Desenvolvimento e contribuições
- Mantenha funções puras testáveis e evite lógica pesada na UI.
- Use `monkeypatch` para simular `tabula` e `reportlab` em testes quando necessário.

## Licença
- (ver `LICENSE`)

---

Para detalhes de uso e exemplos, veja `docs/exemplos.md`. Para descrição da arquitetura, veja `docs/arquitetura.md`.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/levantamentoestoque](https://github.com/pedroiff0/levantamentoestoque)
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
