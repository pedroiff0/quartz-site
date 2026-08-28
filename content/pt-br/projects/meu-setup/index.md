---
publish: false
title: meu-setup
created: 2026-08-08 13:04
modified: 2026-08-27 13:04
tags: [Dotfiles, Provisionamento, Multi-distro, Open Source, Idempotente]
repo: https://github.com/pedroiff0/meu-setup
status: público
cssclasses:
  - page-layout
---

<!-- gerado por portfolio/tools/gen_quartz.py — não editar à mão -->

**Stack:** Python, YAML, Bash, PowerShell, apt/dnf/pacman/zypper, winget, Homebrew

**Repositório:** [https://github.com/pedroiff0/meu-setup](https://github.com/pedroiff0/meu-setup) · público

<!-- fim do bloco gerado -->

> [!note] Em uma frase
> Mapa de **todos os programas que eu uso** — Linux, Windows e macOS — com instaladores automáticos, para repopular a máquina depois de formatar com um comando.

Uma única fonte de verdade: `packages.yaml`. Tudo o mais é derivado dela.

- **Instalador Linux** — detecta a distro e escolhe `apt`, `dnf`, `pacman` ou
  `zypper`; é idempotente (pula o que já está instalado); tem cadeia de
  fallback (pacote nativo → flatpak → snap → script oficial); adiciona
  repositórios quando necessário; roda ações pós-instalação; e aceita
  `--dry-run`, `--group` e `--only`.
- **Bootstrap** — um `curl | bash` que instala git/python, clona o repositório
  e roda um dry-run antes de tocar em qualquer coisa.
- **Gerador** — produz o instalador PowerShell (winget), o de macOS (Homebrew)
  e o inventário em Markdown a partir do mesmo YAML.

Os pacotes são organizados em grupos (`base`, `dev`, `python`, `js`, `infra`,
`rede`, `ia`, `gpu`, `latex`, `desktop`…), então dá para provisionar só o que
importa naquela máquina.

**Status:** público, em uso real como plano de recuperação da estação de trabalho.
