---
publish: true
title: Verdementa
created: 2026-04-01 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- suite-comercial
- erp
repo: https://github.com/pedroiff0/verdementa
status: privado
cssclasses:
- page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

<div align="center">

# VerdeMenta — Meta-Repositório

[![CI](https://github.com/pedroiff0/verdementa/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroiff0/verdementa/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Submodules](https://img.shields.io/badge/Submodules-4%20satellites-green.svg)](#-subprojetos)

**Meta-repositório orquestrador que agrega e unifica os subsistemas do ecossistema VerdeMenta via Git Submodules e Make cross-platform.**

[Visão Geral](#-visão-geral) • [Arquitetura](#-arquitetura) • [Subprojetos](#-subprojetos) • [Comandos](#-comandos-principais) • [Governança](#-governança)

</div>

---

## Visão Geral

O ecossistema **VerdeMenta** é composto por quatro aplicações autônomas e complementares para gestão comercial e operacional:
1. **`caixas`**: Aplicação web Flask para controle financeiro e conferência de caixas.
2. **`controle-estoque`**: Aplicação desktop PyQt para controle e contagem de itens de estoque.
3. **`levantamento-estoque`**: Utilitários e interface de auditoria de inventário.
4. **`planilhador`**: Automação e processamento de documentos fiscais e relatórios.

Este repositório atua como o orquestrador central unificado, gerenciando ambientes locais, scripts de inicialização e sincronização de versões.

## Arquitetura

```mermaid
graph TD
    subgraph MetaRepositório["pedroiff0/verdementa (Meta-Repositório)"]
        RootMake["Root Makefile / Cross-platform Setup"]
        Submodules[".gitmodules Orchestrator"]
    end

    subgraph Satélites["Submódulos Standalone"]
        Caixas["caixas (Web / Flask)<br/>Gestão de Caixa & Operações"]
        Controle["controle-estoque (Desktop / PyQt)<br/>Controle de Estoque & Movimentações"]
        Levantamento["levantamento-estoque (GUI / Scripts)<br/>Auditoria & Conferência Física"]
        Planilhador["planilhador (Python)<br/>Processamento Fiscal & Planilhas"]
    end

    RootMake -->|Instala & Testa| Caixas
    RootMake -->|Instala & Testa| Controle
    RootMake -->|Instala & Testa| Levantamento
    RootMake -->|Instala & Testa| Planilhador
    Submodules -.-> Caixas
    Submodules -.-> Controle
    Submodules -.-> Levantamento
    Submodules -.-> Planilhador
```

## Subprojetos

| Subprojeto | Repositório | Descrição | Stack |
| :--- | :--- | :--- | :--- |
| **`caixas`** | [pedroiff0/caixas](https://github.com/pedroiff0/caixas) | Gestão financeira e controle de caixas | Python / Flask |
| **`controle-estoque`** | [pedroiff0/controle-estoque](https://github.com/pedroiff0/controle-estoque) | Aplicação desktop para controle de estoque | Python / PyQt |
| **`levantamento-estoque`** | [pedroiff0/levantamento-estoque](https://github.com/pedroiff0/levantamento-estoque) | Utilitários e GUI para conferência física | Python |
| **`planilhador`** | [pedroiff0/planilhador](https://github.com/pedroiff0/planilhador) | Utilitários de manipulação de NFCe e planilhas | Python / Pandas |

## Começando

### 1. Clonar com Submódulos

```bash
git clone --recurse-submodules https://github.com/pedroiff0/verdementa.git
cd verdementa
```

Se o repositório já foi clonado sem `--recurse-submodules`:
```bash
make submodules-init
```

### 2. Comandos Principais

| Comando | Descrição |
| :--- | :--- |
| `make help` | Exibe o menu interativo com os comandos disponíveis |
| `make submodules-init` | Inicializa recursivamente todos os submódulos Git |
| `make submodules-update` | Atualiza os submódulos para os commits remotos mais recentes |
| `make install-<modulo>` | Instala dependências e ambiente de um módulo específico (`caixas`, etc.) |
| `make install-all` | Prepara e instala os ambientes virtuais de todos os 4 submódulos |
| `make test-<modulo>` | Executa a suíte de testes de um módulo específico |
| `make test-all` | Executa os testes de todos os módulos |
| `make ci` | Valida a integridade global e suíte de testes |

## Governança

- [Diretrizes de Agentes (AGENTS.md)](AGENTS.md)
- [Regras de Arquitetura e Design (DESIGN.md)](DESIGN.md)
- [Registro de Continuidade (HANDOFF.md)](HANDOFF.md)
- [Guia de Contribuição (CONTRIBUTING.md)](CONTRIBUTING.md)
- [Código de Conduta (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md)
- [Política de Segurança (SECURITY.md)](SECURITY.md)

## Licença

Distribuído sob a licença [MIT](LICENSE).

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/verdementa](https://github.com/pedroiff0/verdementa)
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
