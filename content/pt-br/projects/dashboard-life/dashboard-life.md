---
publish: true
title: dashboard-life
tags:
- life-os
- habito
- metricas
repo: https://github.com/pedroiff0/dashboard-life
status: privado
cssclasses:
- page-layout
created: 2026-09-14 11:17
modified: 2026-09-30 13:05
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

# Dashboard Life — Energia, Repositórios, arXiv, Hábitos, Agentes e Tarefas

<div align="center">

<img src="app/public/img/logo.svg" alt="Dashboard Life Logo" width="120" height="120"/>

> Painel pessoal para monitoramento de energia, repositórios, arXiv, hábitos, agentes e tarefas — **sete módulos independentes, uma só aplicação**.

</div>

---

## Telas

<div align="center">

**Tour pela demonstração**

<img src="docs/assets/demo-tour.gif" alt="Tour pela demonstração" width="900"/>

</div>

<div align="center">

| Energia | Repositórios | arXiv |
|:---:|:---:|:---:|
| <img src="docs/assets/tela-energia.png" width="280"/> | <img src="docs/assets/tela-repos.png" width="280"/> | <img src="docs/assets/tela-arxiv.png" width="280"/> |

| Hábitos | Agentes | TodoList |
|:---:|:---:|:---:|
| <img src="docs/assets/tela-habits.png" width="280"/> | <img src="docs/assets/tela-agents.png" width="280"/> | <img src="docs/assets/tela-todolist.png" width="280"/> |

</div>

---

## Índice

- [O que é](#-o-que-é)
- [Módulos](#-módulos)
- [Stack Técnica](#-stack-técnica)
- [Funcionalidades](#-funcionalidades)
- [Demo](#-demo)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Docker](#-docker)
- [Testes](#-testes)
- [Segurança](#-segurança)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Documentação](#-documentação)
- [Roadmap](#-roadmap)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Autor](#-autor)

---

## O que é

O **Dashboard Life** é uma aplicação web para organizar a vida pessoal em sete frentes que **não precisam coexistir**:

- **Energia** — monitoramento de consumo elétrico (CPU, GPU, custo)
- **Repositórios** — estado git dos projetos locais
- **arXiv** — busca e acompanhamento de papers acadêmicos
- **Hábitos** — tracking diário com streaks e heatmap
- **Agentes** — histórico de sessões Hermes/Claude
- **TodoList** — gerenciamento de tarefas
- **Tutorial** — documentação do próprio painel

Desenvolvido com **EJS no servidor + JavaScript vanilla**, sem etapa de build, sem framework frontend, sem CDN.

---

## Módulos

| Módulo | Rota | Sub-abas | Fonte |
|--------|------|----------|-------|
| **Energia** | `/` | Dashboard, Histórico, Configurações | netdata (RAPL) + nvidia-smi |
| **Repositórios** | `/repos` | Lista, Estatísticas | filesystem (git status) |
| **arXiv** | `/arxiv` | Busca, Salvos, Leitura | arXiv API (XML) |
| **Hábitos** | `/habitos` | Tracker, Heatmap | MongoDB |
| **Agentes** | `/agentes` | Hermes, Claude | SQLite + JSONL |
| **TodoList** | `/todolist` | Tarefas, Calendário | MongoDB |
| **Tutorial** | `/tutorial` | Docs | Estático |

>  **Cada módulo é independente.** Energia e Repositórios não usam banco de dados; arXiv, Hábitos e TodoList usam MongoDB; Agentes lêem fontes externas.

---

## Stack Técnica

| Camada | Tecnologia |
|--------|------------|
| **Runtime** | Node.js 22 |
| **Servidor** | Express 4 |
| **Banco** | MongoDB 7 + Mongoose |
| **Views** | EJS (SSR) + JavaScript vanilla |
| **Validação** | Zod (toda entrada) |
| **Autenticação** | Session cookie httpOnly (ou NO_AUTH=1) |
| **Segurança** | Helmet, CSP, rate limit, sanitização |
| **Testes** | Jest + Supertest |
| **Deploy** | Docker Compose (porta 5003) |

---

## Funcionalidades

### Energia
- Monitoramento de CPU via Intel RAPL (netdata)
- Monitoramento de GPU via nvidia-smi
- Cálculo de kWh e custo em R$
- Histórico de 30 dias
- Configuração de tarifa e bandeira

### Repositórios
- Scan automático de diretórios git
- Status (dirty, ahead, behind, clean)
- Último commit por repositório
- Somente leitura (segurança)

### arXiv
- Busca na API do arXiv
- Buscas salvas (MongoDB)
- Lista de leitura
- Parse XML → JSON

### Hábitos
- Tracking diário
- Streaks (sequências)
- Heatmap anual estilo GitHub
- Adesão mensal

### Agentes
- Histórico de sessões Hermes (SQLite)
- Histórico de sessões Claude (JSONL)
- Timeline interativa

### TodoList
- CRUD de tarefas
- Prioridades e datas
- Calendário

### Geral
- Dashboard responsivo
- Tema claro/escuro
- SSR 100% (zero fetch no frontend)
- CSP estrita (zero inline scripts)

---

## Demo

**Acesse:** [dashboard.phrandrade.com](https://dashboard.phrandrade.com/) (exemplo)

- Modo demo com NO_AUTH=1
- Dados de exemplo populados

---

## Instalação

### Pré-requisitos
- Node.js 22+
- MongoDB (local ou Atlas) — opcional para testes (usa `mongodb-memory-server`)

### Local

```bash
git clone https://github.com/pedroiff0/dashboard-life.git
cd dashboard-life
cp .env.example .env
# Edite .env com suas variáveis
cd app && npm install
npm test           # testes (não precisa de banco)
npm run dev        # watch em http://localhost:5003 (precisa de MONGO_URI)
npm start          # produção sem watch
```

---

## Configuração

**Arquivo único:** `.env` (raiz do projeto)

Principais variáveis:

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `PORT` | Porta do app (padrão: 5003) |  |
| `MONGO_URI` | URI do MongoDB |  (para módulos com banco) |
| `SESSION_SECRET` | Secret da sessão |  |
| `NO_AUTH` | Desativa autenticação (dev) |  (padrão: 1) |
| `NETDATA_URL` | URL do netdata |  (padrão: localhost:19999) |
| `ENERGY_BASE_W` | Potência base em W |  (padrão: 42) |
| `ENERGY_PSU_EFF` | Eficiência da fonte |  (padrão: 0.85) |
| `ENERGY_TARIFA_KWH` | Tarifa energia R$/kWh |  (padrão: 0.98) |
| `GPU_NAME` | Nome da GPU |  |
| `GPU_POWER_IDLE` | Potência GPU idle (W) |  (padrão: 15) |
| `GPU_POWER_FULL` | Potência GPU full (W) |  (padrão: 120) |
| `REPOS_ROOTS` | Diretórios de repos |  |

---

## Docker

```bash
cp .env.example .env    # configure SESSION_SECRET
docker compose up -d --build
docker compose logs -f app
docker compose down
```

- **App:** `http://localhost:5003`
- **MongoDB:** volume persistente

>  Toda alteração de frontend exige `ASSET_VERSION` novo.

---

## Testes

```bash
npm test                 # Jest (backend)
npm run test:coverage    # com cobertura
```

**Cobertura:** core, energy, repos, arxiv.

---

## Segurança

- Session cookie httpOnly
- Content Security Policy (CSP) — zero inline scripts
- Validação Zod em todas entradas
- `execFile` com array (nunca string concat)
- Filesystem montado `:ro` (read-only)
- Sem secrets no código (apenas `.env`)

Detalhes: [[SECURITY|SECURITY.md]]

---

## Estrutura do Projeto

```
app/
  src/
    config/        env.js, db.js
    controllers/   energyController, reposController, arxivController, ...
    middleware/    auth, errorHandler
    models/        SavedSearch, ...
    routes/        index, energy.routes, repos.routes, ...
    schemas/       energy.schema, repos.schema, arxiv.schema, ...
    services/      energyService, reposService, arxivService, ...
    utils/         AppError, validation
  views/
    partials/      header.ejs, footer.ejs
    pages/         energia, repos, arxiv, habits, agents, todolist, tutorial
  public/
    css/           main.css (tema espacial glassmorphism)
    js/            common.js, tema.js
  tests/           core.test.js, energy.test.js, repos.test.js
docs/              documentação técnica completa
scripts/           backup.sh
nginx/             default.conf
```

---

## Documentação

| Arquivo | Conteúdo |
|---------|----------|
| [AGENTS.md](AGENTS) | Regras arquiteturais |
| [SECURITY.md](SECURITY) | Política de segurança |
| [CONTRIBUTING.md](CONTRIBUTING) | Guia de contribuição |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT) | Código de conduta |
| [HANDOFF.md](HANDOFF) | Estado do projeto |

---

## Roadmap

Acompanhe no [Project #20 — Dashboard Life Roadmap](https://github.com/users/pedroiff0/projects/20).

| Fase | Status |
|------|--------|
| v2.0 — Estrutura Base (7 módulos, SSR, testes) |  |
| v2.1 — Energia Avançado (média móvel, alertas, CO2) |  |
| v2.2 — Repositórios & arXiv (filtros, reading list) |  |
| v2.3 — Hábitos & Agentes (heatmap, timeline) |  |
| v2.4 — TodoList & Tutorial (CRUD, documentação) |  |

---

## Contribuição

Veja [[CONTRIBUTING|CONTRIBUTING.md]] para guidelines.

Padrões:
- Conventional Commits (`feat:`, `fix:`, `refactor:`, `docs:`, etc.)
- Branch: `feat/short-desc`, `fix/short-desc`
- PR com checklist (testes, docs, responsivo)

---

## Licença

Este projeto está licenciado sob a **GNU Affero General Public License v3.0** (AGPL-3.0).

Veja [[LICENSE]] para o texto completo.

---

## Autor

<div align="center">

<img src="https://raw.githubusercontent.com/pedroiff0/pedroiff0/main/assets/pedroiff0.gif" alt="Pedro Henrique Rocha de Andrade" width="900"/>

</div>

<div align="center">

**2026 Dashboard Life**

Feito com , código e  por **Pedro Henrique Rocha de Andrade**

[![GitHub](https://img.shields.io/badge/GitHub-pedroiff0-181717?logo=github&logoColor=white)](https://github.com/pedroiff0)
[![Site Oficial](https://img.shields.io/badge/Site-Oficial-22c55e?logo=googlechrome&logoColor=white)](https://phrandrade.com/)
[![Portfólio](https://img.shields.io/badge/Portfólio-2563eb?logo=github&logoColor=white)](https://pedroiff0.github.io/webpage/)

</div>

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/dashboard-life](https://github.com/pedroiff0/dashboard-life)
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
