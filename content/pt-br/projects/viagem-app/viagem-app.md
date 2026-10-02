---
publish: true
title: Viagem App
created: 2026-09-28 22:55
modified: 2026-10-01 20:14
tags:
- projeto
- publico
- pessoal
cssclasses:
  - page-layout
icon: lucide-map-pin
repo: https://github.com/pedroiff0/viagem-app
status: em-desenvolvimento
license: MIT
author: Pedro Henrique Rocha de Andrade
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

# Rumo — Viagens em Grupo, Roteiros e Divisão de Gastos

<div align="center">

<img src="app/public/img/logo.svg" alt="Rumo" width="120" height="120"/>

> Planeje a viagem com quem vai junto: **um roteiro compartilhado, as reservas no mesmo lugar e a conta dividida sem briga**.

[![Licença: AGPL v3](https://img.shields.io/badge/licença-AGPL--3.0-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-20%2B-339933?logo=node.js&logoColor=white)](package.json)
[![Beta gratuito](https://img.shields.io/badge/status-beta%20gratuito-8b5cf6)](#-o-que-é)

**[viagens.phrandrade.com](https://viagens.phrandrade.com)** · **[viagens-demo.phrandrade.com](https://viagens-demo.phrandrade.com)** (sem conta, dados de exemplo)

</div>

---

## Índice

- [O que é](#-o-que-é)
- [Como funciona](#-como-funciona)
- [Stack técnica](#-stack-técnica)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Docker](#-docker)
- [Testes](#-testes)
- [Segurança](#-segurança)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Documentação](#-documentação)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Autor](#-autor)

---

## O que é

Viagem em grupo trava em dois pontos: **ninguém sabe o roteiro combinado** e **ninguém sabe quem pagou o quê**. O Rumo resolve os dois no mesmo lugar.

Cada viagem tem participantes convidados por e-mail, um roteiro dia a dia, as reservas de hospedagem e transporte, os passeios planejados e as despesas de todo mundo. No fim, o app calcula quanto cada um pagou, quanto devia e **qual o menor conjunto de transferências que zera as contas** — em vez de dez pessoas se pagando em círculo.

Em **beta gratuito**, sem cobrança. Cadastro é por convite do administrador (sem autoatendimento ainda) — peça acesso pelo formulário de contato da landing.

---

## Como funciona

| Área | O que faz |
|------|-----------|
| **Viagens** | Criar a viagem, definir destino, datas e orçamento; convidar participantes com papel (admin, editor, visualizador) |
| **Roteiros** | Itinerário dia a dia, com as atividades e horários de cada dia |
| **Passeios** | Atrações e ingressos planejados, com custo estimado e status |
| **Hospedagem** | Reservas de hotel, pousada, hostel ou Airbnb, com check-in, check-out e código de reserva |
| **Transportes** | Voos, ônibus, trem e carro, com origem, destino, horário e companhia |
| **Despesas** | Lançamentos da viagem, quem pagou, entre quem dividir — e a prestação de contas com saldos e transferências sugeridas |
| **Visões** | Quadro Kanban por status da viagem, calendário consolidado e relatórios de gasto por categoria |

Viagem concluída fica na **mesma lista**, com filtro de status — nunca uma tela separada de histórico.

---

## Stack técnica

- **Node.js 20+** com **Express 4**
- **MongoDB** via **Mongoose**
- **EJS** no servidor (sem framework de frontend; JS puro no cliente)
- **Zod** para validação de entrada
- **JWT** em cookie `httpOnly` para sessão
- **Jest** + **supertest** para testes; **Cypress** para ponta a ponta
- **Prometheus** (`prom-client`) para métricas
- Login com **Google** e **GitHub** OAuth; anti-bot com **Cloudflare Turnstile**

---

## Instalação

### Pré-requisitos

- Node.js 20+
- MongoDB (local ou Atlas) — dispensável para rodar os testes, que usam `mongodb-memory-server`

### Local

```bash
git clone https://github.com/pedroiff0/viagem-app.git
cd viagem-app
cp .env.example .env
# Edite .env: SESSION_SECRET é obrigatório e precisa de no mínimo 32 caracteres
cd app && npm install
npm test           # testes (não precisa de banco)
npm run dev        # watch em http://localhost:4451 (precisa de MONGO_URI)
npm start          # produção, sem watch
```

---

## Configuração

**Fonte única de verdade:** `app/.env` (o `.env.example` na raiz documenta todas as ~55 variáveis, uma por uma). As mais relevantes:

| Grupo | Variável | Descrição | Obrigatória |
|-------|----------|-----------|-------------|
| Núcleo | `SESSION_SECRET` | Segredo do JWT (mínimo 32 caracteres) |  |
| Núcleo | `MONGO_URI` | URI do MongoDB |  (dev/prod) |
| Núcleo | `APP_BASE_URL` / `PUBLIC_BASE_URL` | Host interno vs. endereço público (e-mail, QR code) |  |
| Admin | `ADMIN_EMAIL` / `ADMIN_NAME` / `ADMIN_PASSWORD` | Credencial do admin inicial |  (obrigatório em produção) |
| Demo | `SEED_DEMO`, `DEMO_EMAIL`, `DEMO_AUTOLOGIN` | Liga a instância de demonstração, com autologin sem senha |  |
| E-mail | `SMTP_HOST`/`SMTP_SERVICE`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SMTP_FROM` | Envio transacional (convite, redefinição de senha, contato). Sem isso, o envio vira log — nada quebra, mas ninguém recebe e-mail de verdade |  |
| OAuth | `GOOGLE_CLIENT_ID/SECRET`, `GITHUB_CLIENT_ID/SECRET` | Login social (opcional, coexiste com e-mail/senha) |  |
| Anti-bot | `TURNSTILE_SITE_KEY` / `TURNSTILE_SECRET_KEY` | Cloudflare Turnstile no login (auto-liga em produção) |  |
| Operação | `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` | Alertas de backup e observabilidade |  |
| Limites | `RATE_LIMIT_*`, `MAX_FAILED_ATTEMPTS`, `LOCKOUT_MIN` | Limitadores de taxa e bloqueio de conta |  (têm padrão) |
| Módulos | `MODULE_VIAGENS` | Liga/desliga o domínio de viagens (404, não 403, quando desligado) |  (padrão: `true`) |

Em produção, segredo sensível (`SESSION_SECRET`, `MONGO_ROOT_PASSWORD`, `SMTP_PASS`, tokens) não trafega por variável de ambiente — vai por **Docker Secret** (`<NOME>_FILE`, montado em `/run/secrets/`). `scripts/setup-secrets.sh` gera os arquivos a partir do `app/.env`.

---

## Docker

Três ambientes, três portas, cada um com seu `docker compose -p <projeto>` — nunca comandos sem `-p` explícito (evita stack duplicada).

```bash
cp .env.example .env      # configure SESSION_SECRET e o resto que precisar
make secrets                # gera secrets/ a partir de app/.env (produção)
make dev                    # stack de desenvolvimento — porta 4489 (watch, só local)
make prod                   # stack de produção — porta 4490, demo em 4491
make seed                   # popula o banco de demonstração
make logs                   # logs do app dev em tempo real
make health                 # saúde das stacks deste repositório
make down                   # derruba a stack dev, mantendo os volumes
```

`make help` lista todos os alvos (desenvolvimento, produção, backup/restore, monitoramento).

>  Toda alteração de frontend exige `ASSET_VERSION` novo antes do rebuild — sem isso o navegador serve o `.css`/`.js` antigo do cache.

---

## Testes

```bash
make test                  # Jest (backend)
npm run test:e2e           # Cypress, headless
npm run cypress            # Cypress interativo (precisa de GUI)
npm run test:e2e:http      # ponta a ponta sem navegador (node:test)
npm run lint               # ESLint
```

Cobertura: viagens e sub-recursos, páginas do domínio, autenticação, admin, demonstração, notificações, segurança e configuração.

---

## Segurança

- Sessão em cookie `httpOnly` + `SameSite=Lax`, com `Secure` automático em HTTPS
- Bloqueio de conta após 3 falhas de login, por 30 minutos — imune a IP distribuído
- `csrfGuard` sobre mutações autenticadas por cookie
- Sub-recursos escopados por viagem via `exigirAcessoViagem` (barra IDOR por troca de id na URL)
- Toda entrada validada por Zod; `sanitizeInput` antes dos controllers
- CSP sem `script-src` inline
- Segredos por Docker Secrets (`<NOME>_FILE`) ou `.env`

Veja [[SECURITY|SECURITY.md]] para a política de divulgação.

---

## Estrutura do projeto

```
app/
  src/
    config/        env.js, db.js, metrics.js, redis.js
    models/        schemas Mongoose (viagem, participante, roteiro,
                   atividade, despesa, hospedagem, transporte, user, …)
    services/      regra de negócio (prestação de contas, participantes, auth, …)
    controllers/   req -> service -> res
    routes/        API (/api/…) e páginas
    middleware/    auth, pageAuth, viagemAccess, csrfGuard, sanitizeInput,
                   rateLimiters, turnstileGuard, errorHandler
    schemas/       Zod de entrada
    seeds/         admin.seed.js, demo.seed.js
    utils/         AppError, validation, contextoViagem, audit
  public/          css/ e js/ com cache-busting (?v=)
  views/           EJS (landing, login, viagens, roteiros, despesas, …)
  tests/           Jest; cypress/ para ponta a ponta
scripts/           backup, restore, deploy, carga
docs/              documentação técnica
```

---

## Documentação

| Arquivo | Conteúdo |
|---------|----------|
| [AGENTS.md](AGENTS) | Regras arquiteturais |
| [docs/viagem.md](docs/viagem) | O domínio de viagens |
| [docs/setup.md](docs/setup) | Ambiente de desenvolvimento |
| [docs/deploy.md](docs/deploy) | Publicação |
| [docs/seguranca.md](docs/seguranca) | Decisões de segurança |
| [SECURITY.md](SECURITY) | Política de segurança |
| [CONTRIBUTING.md](CONTRIBUTING) | Guia de contribuição |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT) | Código de conduta |
| [CHANGELOG.md](CHANGELOG) | Registro de mudanças |

---

## Contribuição

Veja [[CONTRIBUTING|CONTRIBUTING.md]].

Padrões:

- Conventional Commits (`feat:`, `fix:`, `refactor:`, `chore:`, `docs:`)
- Toda mudança nasce de uma **issue**, numa branch dedicada (`feat/…`, `fix/…`), e entra por **pull request**
- PR com checklist: testes, documentação, responsividade e acessibilidade

---

## Licença

**GNU Affero General Public License v3.0** (AGPL-3.0). Texto completo em [[LICENSE]].

---

## Autor

**Pedro Henrique Rocha de Andrade**

- Site: [phrandrade.com](https://www.phrandrade.com/)
- GitHub: [@pedroiff0](https://github.com/pedroiff0)

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/viagem-app](https://github.com/pedroiff0/viagem-app)
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
