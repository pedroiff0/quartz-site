---
publish: true
title: meu-setup
created: 2026-08-08 13:04
modified: 2026-09-30 13:05
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
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

<div align="center">

```
      .      *       .     (  )   (   )  )       *       .      .
*       .       .          ) (   )  (  (     .       .      *
   .         *       .     ( )  (    ) )        .        .
.       *        *      .       *
         *        COSMIC SETUP         *       .       .
 *                    *
                     
                  
                       /
                         λ
                           
```

# MEU-SETUP — Universal Multi-System Environment

**Instalador Declarativo, Idempotente e Multi-Sistema para Desenvolvedores de Elite**  
*Temas Cósmicos • Estilização Multi-OS • Otimizações de Servidor 24/7 • Energia & Bateria • 117+ Ferramentas*

[![Release - v2.0.0](https://img.shields.io/badge/Release-v2.0.0-purple?style=for-the-badge&logo=rocket&logoColor=white)](https://github.com/pedroiff0/meu-setup/releases)
[![OS - Linux](https://img.shields.io/badge/OS-Linux%20(Ubuntu%2FFedora%2FArch)-385141?style=for-the-badge&logo=linux&logoColor=white)](https://github.com/pedroiff0/meu-setup)
[![OS - macOS](https://img.shields.io/badge/OS-macOS%20(Darwin)-black?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/pedroiff0/meu-setup)
[![OS - Windows](https://img.shields.io/badge/OS-Windows%2011%20(Winget)-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/pedroiff0/meu-setup)
[![Packages](https://img.shields.io/badge/Packages-117%2B%20Curated-a855f7?style=for-the-badge)](packages.yaml)
[![License - MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

</div>

---

## Início Rápido (1 Comando)

### Linux /  macOS — Repopular do Zero

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/pedroiff0/meu-setup/main/install.sh)
```

> [!TIP]
> O instalador detecta automaticamente a sua distribuição (Debian/Ubuntu, Fedora, Arch Linux, openSUSE, macOS ou Windows/MSYS), prepara o ambiente com verificação de TTY e abre a **TUI Interativa Cósmica**.

---

## Menu Interativo TUI

O instalador conta com navegação via teclado (`[↑/↓]` para mover, `[Espaço]` para alternar `[]`, `[←/b]` para voltar, `[→/Enter]` para avançar, `[/]` para buscar e `[s]` para ordenar):

```
  Escolha o Fluxo de Instalação 
   []   Configuração Personalizada (Wizard Passo a Passo 1-a-1) (Controle total: Temas, Tweaks e Pacotes)
    [ ]  Quick Setup (DevSpace Complete Stack) (Instalação rápida: DevSpace, Firefox, Tmux e 24/7 tweaks)
    [ ]  Themes & Multi-OS Styling Hub (Item por Item) (19 componentes de temas, terminal e desktop)
    [ ]   System Tweaks, Power & Kernel Hub (Item por Item) (17 ajustes de energia, rede e kernel)
    [ ]  Catálogo Completo de Aplicações (Navegue e selecione 1-a-1 entre 117+ pacotes)
    [ ]   Instalar por Packs Temáticos (Com Refinamento) (Full-stack, DevOps, IA/LLMs, Acadêmico, Criativo)
    [ ]  Diagnóstico & Telemetria do Sistema (Inspeciona BBR, suspensão, hardware e ambiente)
    [ ]   Desinstalador & Reversão de Configurações (Reverte temas e configurações)
 [↑/↓: Mover | Espaço: Marcar | →/Enter: Avançar | Esc: Sair]
```

---

## 1. Temas & Estilização Multi-Sistema

O ecossistema visual centraliza a identidade **DevSpace Cósmico (Astronomia, Café & Dev)** e suporta ambientes Linux, macOS e Windows:

| Componente | Plataformas | Descrição |
|---|---|---|
| **DevSpace Terminal** | Linux, macOS, Windows | Prompt Planck dinâmico com café , Git status ` main `, relógio e statusline de IA |
| **WhiteSur macOS Look** | Linux (GNOME/XFCE/KDE) | Tema GTK Dark Purple, ícones, cursores e Plank dock com botões macOS |
| **Firefox Cósmico** | Linux, macOS, Windows | `userChrome.css`, abas compactas em gradiente e `userContent.css` |
| **Tmux Cósmico 24/7** | Linux, macOS | Status bar inferior em português com frases dev, separador `` e anti-ghosting |
| **Starship Prompt** | Linux, macOS, Windows | Configuração `starship.toml` universal em Rust para Bash, Zsh e PowerShell |
| **Terminais Modernos** | Multi-OS | Temas calibrados para Alacritty, Kitty, Windows Terminal e iTerm2 |

```bash
# Aplicar todos os temas e estilizações
./install.sh --themes
# ou via script direto:
bash scripts/apply-all.sh
```

---

## 2. Otimizações de Sistema, Energia & Kernel

Configurações prontas para servidores ininterruptos e notebooks de desenvolvimento:

| Otimização | Alvo | Benefício / Implementação |
|---|---|---|
| **Servidor 24/7 (Anti-Sleep)** | Systemd / GNOME / Lid | Mascara `sleep.target`, `suspend.target`, `hibernate.target` e ignora fechar a tampa |
| **TCP BBR v2 + FQ** | Kernel Linux / Sysctl | Controle de congestionamento de alta vazão do Google em `/etc/sysctl.d/99-bbr.conf` |
| **Sysctl Inotify & FD** | Kernel / Filesystem | Eleva `fs.inotify.max_user_watches = 524288`, `file-max = 2097152` e `swappiness = 10` |
| **Docker Data-Root** | Docker Daemon | Move `/var/lib/docker` para `/home/docker-data` com rotação de logs (max 50MB) |
| **Periodic SSD TRIM** | Discos NVMe / SSD | Ativa `fstrim.timer` no systemd para descarte contínuo de blocos |
| **AdGuard Home** | Docker Container | DNS Sinkhole e bloqueador de anúncios na porta 53 com painel web em `http://localhost:8085` |
| **Laptop Battery Mode** | Notebooks | Ativa TLP, powertop autotune e auto-cpufreq para máxima autonomia de bateria |

```bash
# Aplicar otimizações de sistema
./install.sh --tweaks
# ou individualmente:
bash configs/power/server-24-7.sh
bash configs/network/apply-sysctl-tuning.sh
bash configs/storage/setup-docker-storage.sh
```

---

## 3. Catálogo de Aplicações & Packs Temáticos

Todas as 99+ aplicações são gerenciadas via [`packages.yaml`](packages.yaml), com suporte nativo em:
- **Linux**: `apt`, `dnf`, `pacman`, `zypper`, `flatpak`, `snap`, scripts e PPAs oficiais.
- **macOS**: `brew` (fórmulas) e `brew --cask` (aplicativos).
- **Windows**: `winget` (Microsoft Store App Installer).

### Packs Curados

- **` fullstack`**: Compiladores C/C++, Python, Node.js (via NVM), pnpm, Bun, Rust, Go, Git, Docker, Caddy, SQLite, PostgreSQL CLI.
- **` devops`**: Docker, Compose, Lazydocker, Caddy, Tailscale, Syncthing, Netdata, Ctop, Dive, UFW, Ntfy.
- **` ai`**: Ollama (LLMs locais), Open-WebUI, Hermes Agent, Claude Code, Antigravity CLI, CUDA Toolkit e Nvtop.
- **` academic`**: TeXLive Full, Pandoc, Typst, Zotero, LaTeXmk, Poppler e Ghostscript.
- **` creative`**: FFmpeg, Inkscape, GIMP, VLC, OBS Studio e Kdenlive.
- **` server_min`**: Htop, Btop, Tmux, Duf, Ncdu, Gping, Zoxide, Fzf, Bat, Eza, Ripgrep, Fd-find e Fastfetch.
- **` all`**: Todos os 99+ programas catalogados.

```bash
# Instalar por pack
python3 tools/installer.py --pack fullstack
python3 tools/installer.py --pack devops
python3 tools/installer.py --pack ai
```

---

## Windows (Winget & PowerShell)

```powershell
# Simular instalação (Dry-Run)
powershell -ExecutionPolicy Bypass -File .\windows\install.ps1 -DryRun

# Instalar todos os programas catalogados
powershell -ExecutionPolicy Bypass -File .\windows\install.ps1

# Aplicar tema DevSpace no PowerShell & Windows Terminal
powershell -ExecutionPolicy Bypass -File .\themes\devspace\install-devspace.ps1
```

---

## macOS (Homebrew & Darwin)

```bash
# Simular instalação
DRY_RUN=1 ./macos/install.sh

# Instalar fórmulas e casks
./macos/install.sh

# Aplicar prompt DevSpace no Zsh e perfil iTerm2
bash themes/devspace/install-devspace.sh
```

---

## Estrutura do Repositório

```
meu-setup/
 install.sh                  # Ponto de entrada universal (curl | bash)
 packages.yaml               # FONTE ÚNICA DA VERDADE (99+ aplicações)
 INVENTARIO.md               # Tabela comparativa multiplataforma
 dotfiles/                   # Configurações brutas (DevSpace, Firefox, Tmux, Sysctl, Docker)
 themes/                     # Instaladores modulares de temas
    devspace/               # Terminal cósmico, prompt Planck, fastfetch, aliases
    whitesur/               # Tema GTK WhiteSur, ícones, cursores e Plank dock
    firefox/                # userChrome.css e user.js cósmico
    tmux/                   # .tmux.conf, statusline em português, auto-redraw
    wallpapers/             # Wallpapers Big Sur 5K e gradientes DevSpace
 configs/                    # Otimizações de sistema e infraestrutura
    power/                  # Servidor 24/7 (Anti-Sleep), Laptop Battery (TLP)
    network/                # TCP BBR + FQ, sysctl tuning, AdGuard Home, UFW
    storage/                # Docker data-root (/home/docker-data), SSD fstrim
    monitoring/             # Fastfetch, btop, htop, lazydocker
 scripts/                    # Scripts executáveis standalone
 docs/                       # Documentação detalhada
    ARCHITECTURE.md         # Design do sistema e fluxo de dados
    THEMES_GUIDE.md         # Guia completo de estilização
    SYSTEM_TWEAKS.md        # Guia de energia, BBR e Docker
    PACKAGES_CATALOG.md     # Catálogo completo agrupado por tags
 tools/
     installer.py            # Motor interativo TUI Cósmico Multi-Sistema
     gen.py                  # Gerador automático (Windows, macOS, Inventário, Docs)
     verify.sh               # Suíte com 24+ testes automatizados
```

---

## Verificação & Testes de Integridade

```bash
bash tools/verify.sh
```

A suíte executa 24 validações rigorosas:
- Sintaxe Python e compilação de scripts (`py_compile`).
- Validação de sintaxe Bash em todos os scripts (`bash -n`).
- Parsing e conformidade do manifesto [`packages.yaml`](packages.yaml).
- Idempotência e determinismo dos geradores (`tools/gen.py`).
- Auditoria de segurança contra segredos ou chaves privadas.
- Testes funcionais do instalador com flags `--dry-run`, `--group`, `--only` e `--list`.

---

<div align="center">

Feito com , código limpo e inspiração cósmica por **[Pedro Ildefonso](https://github.com/pedroiff0)**

</div>

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/meu-setup](https://github.com/pedroiff0/meu-setup)
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
