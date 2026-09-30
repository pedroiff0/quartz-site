---
publish: true
title: Finanças App
created: 2026-08-08 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- financas
- full-stack
- web-app
- orcamento
- investimento
repo: https://github.com/pedroiff0/financas-app
status: privado
cssclasses:
- page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Zênite — Finanças Pessoais, Investimentos e Veículos

<div align="center">

<img src="app/public/img/logo.svg" alt="Zênite Logo" width="120" height="120"/>

[![Jest](https://img.shields.io/badge/tests-352%2B%20tests-22c55e?logo=jest&logoColor=white)](https://github.com/pedroiff0/financas-app/actions)
[![Cypress](https://img.shields.io/badge/E2E-13%20specs-17202C?logo=cypress&logoColor=white)](https://www.cypress.io/)
[![Node](https://img.shields.io/badge/node-%3E%3D20-339933?logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![MongoDB](https://img.shields.io/badge/Mongoose-8-47A248?logo=mongodb&logoColor=white)](https://mongoosejs.com/)
[![License](https://img.shields.io/badge/license-AGPL--3.0-e11d48)](LICENSE)

Controle financeiro pessoal, carteira de investimentos e gestão de veículos — **três módulos independentes, uma só aplicação**.

</div>

---

## Telas

<div align="center">

**Tour pela demonstração**

<img src="docs/assets/demo-tour.gif" alt="Tour pela demonstração" width="900"/>

</div>

<div align="center">

| Painel | Lançamentos | Investimentos |
|:---:|:---:|:---:|
| <img src="docs/assets/tela-painel.png" width="280"/> | <img src="docs/assets/tela-lancamentos.png" width="280"/> | <img src="docs/assets/tela-investimentos.png" width="280"/> |

| Orçamentos | Veículos | Cadastros |
|:---:|:---:|:---:|
| <img src="docs/assets/tela-orcamentos.png" width="280"/> | <img src="docs/assets/tela-veiculos.png" width="280"/> | <img src="docs/assets/tela-cadastros.png" width="280"/> |

</div>

---

## Índice

- [O que é](#o-que-é)
- [Módulos](#módulos)
- [Stack Técnica](#stack-técnica)
- [Funcionalidades](#funcionalidades)
- [Demo](#demo)
- [Instalação](#instalação)
- [Desenvolvimento](#desenvolvimento)
- [Docker](#docker)
- [Testes](#testes)
- [Segurança](#segurança)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Documentação](#documentação)
- [Roadmap](#roadmap)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Autor](#autor)

---

## O que é

O **Zênite** é uma aplicação web para organizar a vida financeira pessoal em três frentes que **não precisam coexistir**:

- **Finanças** — lançamentos, contas, categorias, orçamentos, metas
- **Investimentos** — carteira multi-corretora, proventos, swing trade, pregões
- **Veículos** — manutenções, abastecimentos, alertas de revisão

Desenvolvido com **EJS no servidor + JavaScript vanilla**, sem etapa de build, sem framework frontend, sem CDN.

---

## Módulos

| Módulo | Flag | Rotas | Cobertura |
|--------|------|-------|-----------|
| **Finanças** | `MODULE_FINANCAS` | `/api/financas/*` | Contas, categorias, lançamentos, recorrências, orçamentos, metas |
|| **Investimentos** | `MODULE_INVESTIMENTOS` | `/api/investimentos/*` | Carteiras, preço médio, proventos, resultado, swing trade, pregões |
|| **Veículos** | `MODULE_VEICULOS` | `/api/veiculos/*` | Manutenções, abastecimentos (km/l), gastos, alertas de revisão |

> **Desligue o que não usa.** Cada módulo liga/desliga por flag de ambiente. Desligar = API responde `404`, menu some, dashboard funciona com qualquer combinação.

---

## Stack Técnica

| Camada | Tecnologia |
|--------|------------|
| **Runtime** | Node.js 20+ |
| **Servidor** | Express 4 |
| **Banco** | MongoDB 6 + Mongoose 8 |
| **Views** | EJS (SSR) + JavaScript vanilla |
| **Validação** | Zod (toda entrada via `validate`) |
| **Autenticação** | JWT (HS256) — cookie httpOnly ou Bearer |
| **Segurança** | Helmet, CSP, CSRF, rate limit, sanitização, 2FA TOTP |
| **Testes** | Jest + Supertest (backend), Cypress (E2E interface) |
| **Deploy** | Docker Compose + nginx |

---

## Funcionalidades

### Finanças
- Contas bancárias com saldo automático (derivado)
- Categorias personalizáveis
- Lançamentos (receita/despesa/transferência)
- Recorrências
- Orçamentos por envelope
- Metas financeiras
- Financiamentos (SAC/Price/CET)

### Investimentos
- Cadastro de ativos (ações, FIIs, ETFs, etc.)
- Carteira multi-corretora
- Preço médio ponderado por custódia
- Proventos (dividendos/JCP)
- Resultado realizado e não realizado
- Swing Trade (operações de curto prazo)
- Pregões e radar de proventos
- Dashboard de investimentos

### Veículos
- Cadastro de veículos (carro/moto/etc.)
- Manutenções com alertas por data ou km
- Abastecimentos com consumo (km/l) derivado
- Gastos diversos (IPVA, seguro, multa, etc.)
- Histórico completo por veículo

### Geral
- Dashboard responsivo
- Autenticação JWT (admin/user) com 2FA TOTP obrigatório
- Registro controlado por administrador (sem autocadastro)
- Modo demo com autologin
- Exportação CSV/PDF
- Notificações em tempo real
- Tema claro/escuro
- Exportação de dados (LGPD art. 41) e autoexclusão (art. 18)
- Simulações (crescimento, parcelas, comparação de cenários)
- Planos e assinaturas (Stripe + Mercado Pago)
- PWA instalável

---

## Demo

**Acesse:** [financas.phrandrade.com](https://financas.phrandrade.com/)

- Usuário demo com autologin
- Banco de dados isolado
- Dados de exemplo populados

---

## Instalação

### Pré-requisitos
- Node.js 20+
- MongoDB 6+ (local ou Atlas) — opcional para testes (usa `mongodb-memory-server`)
- Redis 7+ (cache; opcional para testes)

### Local

```bash
git clone https://github.com/pedroiff0/financas-app.git
cd financas-app
cp .env.example app/.env
# Edite app/.env com suas variáveis (JWT_SECRET obrigatório, mínimo 32 chars)
cd app && npm install
npm test           # suíte completa (Jest, Mongo em memória, ~2min)
```

---

## Desenvolvimento

O ambiente de desenvolvimento é **nativo no host** (`make dev`), fora do Docker.

| Ambiente | Porta | Como roda | Banco |
|---|---|---|---|
| **DEV** | **6790** | **Nativo** (`make dev`) | `financas_dev` |
| PROD | 6789 | Docker (`make prod`) | `financas_db` |
| DEMO | 6791 | Docker | `financas_demo_db` |

```bash
make dev          # sobe dev NATIVO na 6790 (nodemon, foreground)
make dev-check    # confere mongod + redis nativos + porta 6790
make env-dev      # regenera app/.env.dev a partir do app/.env
```

O `make dev` roda em **foreground** (Ctrl+C para parar) — os logs saem no terminal. O `nodemon` reinicia automaticamente a cada alteração em `.js`, `.ejs` ou `.css`.

O banco de desenvolvimento é `financas_dev` em `127.0.0.1:27017` (mongod nativo via systemd). O Redis é `127.0.0.1:6379`.

Fallback em Docker (imagem pode servir código velho):
```bash
make dev-docker       # stack dev em Docker na 6790
make dev-docker-down  # para stack dev em Docker
```

---

## Configuração

**Fonte única:** `app/.env` (o `.env` da raiz é um symlink). O `app/.env.dev` é derivado por `scripts/gerar-env-dev.sh` — troca apenas host/porta, nunca guarda segredo próprio.

Principais variáveis:

| Variável | Descrição | Obrigatória |
|----------|-----------|-------------|
| `JWT_SECRET` | Segredo do JWT (mínimo 32 chars) |  |
| `MONGO_URI` | URI do MongoDB |  (dev/prod) |
| `REDIS_URL` | URL do Redis |  |
| `ADMIN_EMAIL` | Email do admin inicial |  |
| `ADMIN_PASSWORD` | Senha do admin inicial |  |
| `MODULE_FINANCAS` | Ativar módulo Finanças |  (padrão: true) |
| `MODULE_INVESTIMENTOS` | Ativar módulo Investimentos |  (padrão: true) |
| `MODULE_MOTO` | Ativar módulo Veículos |  (padrão: true) |
| `SMTP_HOST` | Servidor de e-mail transacional |  |

---

## Docker

```bash
cp .env.example app/.env    # configure JWT_SECRET (mínimo 32 chars)
make prod                   # build + up da produção na 6789
make prod-verify            # prova hardening (read-only + secrets + health)
make prod-down              # para produção mantendo volumes
make prod-logs              # tail dos logs da produção
```

- **App principal:** `http://localhost:6789`
- **Demo:** `http://localhost:6791`

---

## Testes

```bash
# Backend (Jest + Supertest)
make test                  # suíte rápida: auth (~17s)
make test-all              # suíte completa: 78 arquivos (~2min)
cd app && npx jest --testPathPattern="auth" --runInBand --forceExit  # uma suíte

# E2E de interface (Cypress)
cd app && npm run test:e2e  # headless (22 specs)
cd app && npm run cypress   # modo interativo (GUI)

**Cobertura:** 78 suítes Jest (auth, admin, finanças, investimentos, veículos, security, config, modulos, LGPD, billing, etc.) + 22 specs Cypress (login, dashboard, finanças, investimentos, veículos, extrato, notificações, e-mail, perfil, navegação, admin).

Total: **890+ testes** verdes.

---

## Segurança

- JWT HS256 com algoritmo fixado, cookie httpOnly
- 2FA TOTP obrigatório (RFC 6238) com códigos de backup
- bcrypt custo 12 (`passwordHash` é `select: false`)
- Bloqueio POR CONTA (3 falhas / 30 min) + rate limit POR IP
- `sanitizeInput` remove `$` e `.` (anti-NoSQL injection)
- CSRF: Origin/Referer para mutações autenticadas por cookie
- CSP restritiva via Helmet (sem `unsafe-inline`)
- Honeypot em formulários públicos
- Turnstile auto-ativado em produção
- Validação Zod em toda entrada (via `validate(schema)`)
- Dinheiro em centavos inteiros (sem float)
- Valores agregados derivados (nunca guardados)
- Sem segredos no código (apenas `app/.env`)
- Auditoria de segurança em `docs/seguranca.md`

Detalhes: [SECURITY.md](SECURITY.md) · [docs/seguranca.md](docs/seguranca.md)

---

## Estrutura do Projeto

```
app/
  src/
    config/        env.js, db.js
    models/        27 schemas Mongoose
    services/      34 services (regra de negócio, escopados por userId)
    controllers/   req -> service -> res
    routes/        endpoints + pages
    middleware/    auth, pageAuth, requireRole, csrfGuard, sanitizeInput,
                   rateLimiters, errorHandler, cacheControl
    schemas/       Zod de entrada (5 arquivos)
    seeds/         admin.seed.js, demo.seed.js
    utils/         AppError, validation, audit
  public/          css/ e js/ com cache-busting (?v=)
  views/           EJS (landing, login, painel, admin, etc.)
  tests/           78 suítes Jest + 22 specs Cypress
scripts/           seed, backup, deploy, gerar-env-dev
docs/              documentação técnica completa
```

---

## Documentação

| Arquivo | Conteúdo |
|---------|----------|
| [AGENTS.md](AGENTS.md) | Regras arquiteturais e checklist de PR |
| [SECURITY.md](SECURITY.md) | Política de segurança e DPO |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Guia de contribuição |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Código de conduta |
| [CHANGELOG.md](CHANGELOG.md) | Registro de mudanças |
| [HANDOFF.md](HANDOFF.md) | Contexto acumulado das sessões |
| [PRIVACIDADE.md](PRIVACIDADE.md) | Política de Privacidade (LGPD) |
| [TERMOS.md](TERMOS.md) | Termos de Uso |

Documentação técnica completa em [`docs/`](docs/) — arquitetura, segurança, testes, deploy, operações, backup, monitoramento, LGPD.

---

## Roadmap

Acompanhe no [Project #17 — Finanças App Roadmap](https://github.com/users/pedroiff0/projects/17).

| Fase | Estado |
|------|--------|
| 1 — Documentação |  Concluída |
| 1.5 — SaaS / Billing |  Concluída |
| 1.6 — Integrações |  Concluída |
| 1.7 — LGPD Compliance |  Concluída |
| 1.8 — Agente IA + Telegram |  Concluída |
| 2 — Segurança |  Concluída |
| 3 — Testes |  Concluída |
| 4 — Performance (Cache/ETag) |  Concluída |
| 5 — Interface (template-oficial, gráficos) |  Pendente |
| 6 — Infraestrutura (réplicas, PM2) |  Pendente |
| 7 — PWA + Gráficos |  Pendente |

---

## Contribuição

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o processo completo.

Resumo:
- Commits atômicos em PT-BR seguindo Conventional Commits (`feat:`, `fix:`, `docs:`, etc.)
- Branches: `feat/descricao`, `fix/descricao`, `docs/descricao`
- PRs vinculando issues (`Closes #NNN`)
- Toda entrada validada via Zod (`validate(schema)`)
- Teste junto (nunca depois)

---

## Licença

Este projeto está licenciado sob a **GNU Affero General Public License v3.0** (AGPL-3.0).

Veja [LICENSE](LICENSE) para o texto completo.

---

## Autor

<div align="center">

**2026 Zênite — Finanças Pessoais**

[![GitHub](https://img.shields.io/badge/GitHub-pedroiff0-181717?logo=github&logoColor=white)](https://github.com/pedroiff0)
[![Site Oficial](https://img.shields.io/badge/Site-Oficial-22c55e?logo=googlechrome&logoColor=white)](https://phrandrade.com/)

</div>

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/financas](https://github.com/pedroiff0/financas)
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
