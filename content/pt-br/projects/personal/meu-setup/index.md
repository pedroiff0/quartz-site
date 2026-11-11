---
publish: true
title: meu-setup
created: '2026-08-08T13:04:00-03:00'
modified: 2026-11-11T14:05:05-03:00
tags:
- dotfiles
- provisionamento
- multi-distro
- open-source
- idempotente
repo: https://github.com/pedroiff0/meu-setup
status: público
cssclasses:
  - page-layout
icon: lucide-notebookpen
sitesync: true
resource-sync: false
mirror_of: pedroiff0/meu-setup/README.md
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>Projetos Públicos</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">meu-setup</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/personal/formularios/index|← Formulários]]</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">Hub</span> <span class="academic-nav-counter">(7 de 10)</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/personal/portfolio/index|Portfólio (este site) →]]</span>

</div>

</div>

</div>

# meu-setup

[![CI](https://github.com/pedroiff0/meu-setup/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroiff0/meu-setup/actions/workflows/ci.yml)
[![Licença](https://img.shields.io/github/license/pedroiff0/meu-setup)](LICENSE.md)
[![Estrelas](https://img.shields.io/github/stars/pedroiff0/meu-setup?style=flat&logo=github)](https://github.com/pedroiff0/meu-setup/stargazers)
[![Status](https://img.shields.io/badge/status-ativo-informational)](#status-e-próximos-passos)

Instalador declarativo e idempotente do meu ambiente de desenvolvimento para Linux, macOS e Windows: temas, ajustes de sistema para servidor 24/7 e energia, e um catálogo de mais de 100 aplicações.

Este projeto faz parte do [portfólio](https://portfolio.phrandrade.com/#meu-setup) de Pedro Rocha.

## Sumário

- [Por que existe](#por-que-existe)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Personalização](#personalização)
- [Como funciona](#como-funciona)
- [Trabalhando no projeto](#trabalhando-no-projeto)
- [Status e próximos passos](#status-e-próximos-passos)
- [Contribuindo e suporte](#contribuindo-e-suporte)
- [Autores](#autores)
- [Licença](#licença)

## Por que existe

Refazer o ambiente a cada formatação ou máquina nova levava horas e nunca ficava igual. Este repositório descreve o ambiente em `packages.yaml` e nos scripts de `configs/`, e o instalador aplica só o que falta, em qualquer distribuição suportada.

## Funcionalidades

- Instalação por TUI interativa, por packs temáticos (`fullstack`, `devops`, `ai`, `academic`, `creative`, `server_min`) ou pelo catálogo completo.
- Temas: prompt de terminal, WhiteSur, Firefox, Tmux, Starship, Alacritty, Kitty, Windows Terminal e iTerm2.
- Ajustes de sistema: servidor 24/7 (sem suspensão), TCP BBR, limites de inotify, Docker em `data-root` separado, TRIM periódico, AdGuard Home e modo bateria para notebooks.
- Gerenciadores nativos: `apt`, `dnf`, `pacman`, `zypper`, `flatpak`, `snap`, `brew` e `winget`.
- Diagnóstico do sistema e desinstalador que reverte temas e configurações.

## Tecnologias

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Make](https://img.shields.io/badge/Make-6D00CC?style=flat&logo=gnu&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=flat&logo=gnubash&logoColor=white)

## Instalação

### Pré-requisitos

- Linux (Debian/Ubuntu, Fedora, Arch, openSUSE), macOS ou Windows 11 com winget.
- `curl`, `git` e Python 3.

### Passos

```bash
git clone https://github.com/pedroiff0/meu-setup.git
cd meu-setup
./install.sh
```

Instalação direta:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/pedroiff0/meu-setup/main/install.sh)
```

### Conferindo

```bash
./install.sh --diagnostico
```

Saída esperada: sistema detectado, gerenciador de pacotes, estado do BBR, da suspensão e do hardware.

## Como usar

### Uso básico

```bash
./install.sh
```

A TUI detecta a distribuição e abre o menu (setas para mover, espaço para marcar, Enter para avançar).

### Exemplos

| Quero | Comando |
| :--- | :--- |
| Aplicar todos os temas | `./install.sh --themes` |
| Aplicar ajustes de sistema | `./install.sh --tweaks` |
| Instalar um pack | `python3 tools/installer.py --pack fullstack` |
| Modo servidor 24/7 | `bash configs/power/server-24-7.sh` |
| Ajustes de rede | `bash configs/network/apply-sysctl-tuning.sh` |

## Personalização

| Opção | Onde | Padrão | O que muda |
| :--- | :--- | :--- | :--- |
| Pacotes e packs | `packages.yaml` | catálogo completo | O que o instalador oferece |
| Ajustes de energia | `configs/power/` | desligados | Suspensão, tampa, TLP |
| Rede e kernel | `configs/network/` | desligados | BBR e sysctl |

## Como funciona

O `install.sh` detecta o sistema, prepara o Python e chama o instalador (`tools/installer.py`), que lê `packages.yaml` e usa o gerenciador de pacotes certo para cada item. Cada ajuste é um script idempotente em `configs/`, que verifica o estado antes de alterar.

```mermaid
flowchart LR
    A[install.sh] --> B[tools/installer.py]
    B --> C[packages.yaml]
    B --> D[configs/*]
    C --> E[apt, brew, winget...]
```

## Trabalhando no projeto

```bash
bash -n install.sh
python3 -m pytest
```

1. Crie uma branch a partir de `main`: `git checkout -b feat/<assunto-curto>`.
2. Commits no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
3. Rode os testes antes de abrir o pull request.
4. Registre a mudança na seção `Unreleased` de [CHANGELOG.md](CHANGELOG.md).

## Status e próximos passos

Estado atual: **ativo** (versão 2.0.0). Linux é a plataforma mais testada; macOS e Windows seguem o mesmo catálogo com cobertura menor.

- [x] TUI, packs temáticos e catálogo multi-sistema
- [x] Temas e ajustes de servidor 24/7
- [ ] Mais testes automatizados dos scripts de `configs/`

## Contribuindo e suporte

Issues e pull requests são bem-vindos: veja [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) e [SUPPORT.md](SUPPORT.md). Vulnerabilidades seguem [SECURITY.md](SECURITY.md).

## Autores

<table>
  <tr>
    <td align="center"><a href="https://github.com/pedroiff0"><img src="https://github.com/pedroiff0.png?size=120" width="96" height="96" alt="Pedro Henrique Rocha de Andrade" /><br /><sub><b>Pedro Henrique Rocha de Andrade</b></sub></a><br />Autor e mantenedor</td>
  </tr>
</table>

### Contribuidores

[![Contribuidores](https://contrib.rocks/image?repo=pedroiff0/meu-setup)](https://github.com/pedroiff0/meu-setup/graphs/contributors)

## Licença

MIT. Veja [LICENSE](LICENSE.md).

Pedro Henrique Rocha de Andrade, 2026.
