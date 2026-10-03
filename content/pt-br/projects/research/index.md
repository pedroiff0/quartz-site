---
publish: true
title: research
tags:
- literatura
- arxiv
repo: https://github.com/pedroiff0/research
status: privado
cssclasses:
  - page-layout
created: 2026-09-14 11:17
modified: 2026-10-01 20:14
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

# Researcher Hub

**Inteligência & automação de pesquisa acadêmica sobre o arXiv.**

Uma varredura diária automática das ~20 áreas e 155 subcategorias oficiais do arXiv, com uma biblioteca pessoal de papers, rastreamento inteligente de autores e palavras-chave, exportação executiva em PDF e um gateway REST para integrações externas — tudo sem depender de React ou de um passo de build.

[![Release](https://img.shields.io/github/v/release/pedroiff0/research?label=release)](https://github.com/pedroiff0/research/releases/latest)
[![Node](https://img.shields.io/badge/node-%3E%3D20-339933?logo=node.js&logoColor=white)](package.json)
[![Tests](https://img.shields.io/badge/tests-348%20passing-2ea44f)](#testes)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Índice

- [O que é](#o-que-é)
- [Recursos principais](#recursos-principais)
- [Stack tecnológica](#stack-tecnológica)
- [Como rodar](#como-rodar)
- [Deploy](#deploy)
- [Testes](#testes)
- [API REST](#api-rest-apiv1)
- [Documentação](#documentação)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

---

## O que é

Researcher Hub nasceu de uma necessidade concreta: acompanhar, todo dia, o volume de pré-publicações que o arXiv recebe em astrofísica, ciência da computação e áreas correlatas — sem abrir o feed manualmente e sem perder artigos relevantes no meio do ruído.

- **Daily Review & Ingestão RSS** — varredura automática de todas as áreas/subcategorias do arXiv, todo dia, no fuso `America/Sao_Paulo`.
- **Busca Global (`Ctrl+K`)** — command palette buscando ao mesmo tempo em Daily Review, Biblioteca, palavras-chave e autores.
- **Exploração Pública (`/explorar`)** — varredura ao vivo sem login, com filtros próprios de palavras-chave/autores/categorias.
- **Biblioteca & Anotações** — papers salvos com notas, nível de interesse e tags.
- **Rastreamento de Autores** — correspondência inteligente por iniciais e sobrenome (`A. Einstein`, `M. Curie`, `Marie Curie`, ...).
- **Multiusuário & Administração** — cadastro com aprovação de admin, painel `/admin` (saúde do sistema, broadcast, relatos) e `/admin/users` restritos a `role: admin`.
- **Exportação & Importação** — relatório executivo em PDF (capa, tabela por categoria, QR code) do dia ou da Biblioteca inteira; importe por link direto do arXiv ou entrada BibTeX.
- **Renderização de LaTeX** — título e resumo renderizam fórmulas de verdade (KaTeX vendorizado, CSP estrita).
- **Notificações inteligentes** — resumo diário automático de categorias/autores/palavras-chave usados e quantos artigos relevantes voltaram.
- **API Gateway** — REST em `/api/v1/*` autenticado via `Authorization: Bearer res_live_...` ou `X-API-Key`, para scripts externos e automações.

---

## Recursos principais

### Daily Review
KPI grid com percentual e volume diário por categoria, painel de busca com período/data/chips de filtro, cards colapsáveis por categoria/subcategoria destacando "Papers Relevantes" vs. "Papers para Revisar", e ações de 1 clique (PDF, salvar na Biblioteca via AJAX, descartar).

### Exploração Pública
Acesso irrestrito, sem cadastro, pra qualquer pesquisador explorar as publicações do dia — bloqueio amigável de salvamento que orienta para o cadastro gratuito.

### Chaves de API (Bearer / Gateway)
Criação, listagem e revogação de chaves em `/perfil`; endpoints em `/api/v1/*` autenticados via `Authorization: Bearer res_live_...` ou header `X-API-Key`.

### Acessibilidade & Temas
Contraste WCAG AA verificado via Playwright real (não só suposto), modo Alto Contraste, escala de fonte A++, tema claro/escuro com switch de estado visível, e modais responsivos sem scroll duplo no mobile.

---

## Stack tecnológica

| Camada | Tecnologia |
|---|---|
| Backend | Node.js 22 + Express 4 |
| Interface | EJS (SSR) + JavaScript vanilla — sem React, sem build step |
| Estilos | CSS modular (`main.css`, `sidebar.css`, `topnav.css`, `research.css`) |
| Banco de dados | MongoDB / Mongoose |
| Validação | Zod em toda entrada de rota |
| Segurança | CSP estrita (sem `unsafe-inline`, sem CDN externo de script), rate limiting, Bcrypt |
| Testes | Jest + Supertest + `mongodb-memory-server` |
| Infra | Docker Compose (dev/prod/demo) + Nginx |

---

## Como rodar

Requer Docker + Docker Compose (recomendado) ou Node 22+ com um MongoDB acessível.

```bash
git clone https://github.com/pedroiff0/research.git
cd research
cp .env.example .env    # ajuste os valores conforme necessário
make dev                # sobe a stack de desenvolvimento em http://localhost:4409
```

Sem Docker/Make:

```bash
npm install
cp .env.example .env
npm run dev              # node --watch app/src/server.js
```

Todos os comandos disponíveis:

```bash
make dev            # Stack dev com live-reload (porta 4409)
make prod            # Produção (4410) + demo (4411)
make test            # Suíte completa via mongodb-memory-server
make lint            # Sanity check: confirma que app.js carrega
make secrets         # Gera/sincroniza secrets/ a partir do .env
make health           # Health-check das três portas
make backup / restore # Backup e restauração do banco local
```

---

## Deploy

- **Produção em nuvem:** [Render](https://render.com) (`render.yaml`) + MongoDB Atlas — guia completo em [[docs/deploy-atlas-render|`docs/deploy-atlas-render.md`]].
- **Self-hosted (Docker Compose):**

  | Porta | Ambiente | Stack |
  | :--- | :--- | :--- |
  | `4409` | Desenvolvimento (live-reload) | `compose.dev.yml` |
  | `4410` | Produção (hardened + secrets) | `compose.prod.yml` |
  | `4411` | Demonstração | `compose.prod.yml` |

  Detalhes de hardening (filesystem read-only, Docker Secrets, `cap_drop: ALL`, `no-new-privileges`) em [[DEPLOY|`DEPLOY.md`]].

---

## Testes

```bash
npm test
```

41 suítes / 348 testes, 100% aprovados (Jest + Supertest contra `mongodb-memory-server`, sem dependência de banco externo). Estado detalhado da última verificação em [[HANDOFF|`HANDOFF.md`]].

---

## API REST (`/api/v1`)

| Método | Endpoint | Descrição |
|---|---|---|
| `GET` | `/api/v1/health` | Healthcheck do serviço |
| `GET` | `/api/v1/daily` | Lista preprints do daily review com filtros |
| `POST` | `/api/v1/daily/scan` | Dispara varredura sob demanda no arXiv |
| `PATCH` | `/api/v1/daily/:id` | Atualiza status e anotações do paper diário |
| `GET` | `/api/v1/papers` | Lista biblioteca de papers salvos |
| `POST` | `/api/v1/papers` | Salva preprint na biblioteca permanente |
| `GET` | `/api/v1/keywords` | Lista palavras-chave monitoradas |
| `POST` | `/api/v1/keywords` | Adiciona nova palavra-chave |
| `GET` | `/api/v1/authors` | Lista autores monitorados |
| `POST` | `/api/v1/authors` | Adiciona autor para acompanhamento |
| `GET` | `/api/v1/stats` | Métricas e KPIs de pesquisa |

Toda rota em `app/src/routes/api.routes.js` responde tanto em `/api/*` quanto em `/api/v1/*`.

---

## Documentação

- [[HANDOFF|`HANDOFF.md`]] — estado do sistema, decisões de arquitetura e histórico de sessões.
- [[DEPLOY|`DEPLOY.md`]] — deploy self-hosted e hardening de produção.
- [[docs/deploy-atlas-render|`docs/deploy-atlas-render.md`]] — deploy em nuvem (Render + MongoDB Atlas).
- [[CLAUDE|`CLAUDE.md`]] / [[AGENTS|`AGENTS.md`]] — guia de arquitetura para agentes de código.

### Navegando o código com graphify

O repositório versiona um grafo de conhecimento gerado (`graphify-out/`) — nós, comunidades e relações entre arquivos/símbolos. Pra qualquer pergunta de arquitetura, prefira consultar o grafo a grepar o código cru:

```bash
graphify query "<pergunta>"          # subgrafo focado na pergunta
graphify path "<A>" "<B>"            # caminho de relação entre dois símbolos/arquivos
graphify explain "<conceito>"        # conceito específico, explicado
graphify update .                    # re-indexa depois de mudanças (AST-only, sem custo de API)
```

---

## Contribuindo

Este projeto está a caminho de se tornar open source. Até lá, issues e pull requests ainda não são aceitos publicamente — quando o repositório abrir, esta seção vai trazer o guia de contribuição (setup, convenções de commit, como rodar a suíte de testes antes de abrir um PR).

---

## Licença

[[LICENSE|MIT]] — livre para uso, cópia, modificação e redistribuição, inclusive comercial, mantendo o aviso de copyright. Todas as dependências diretas (Express, Mongoose, EJS, Zod, PDFKit, etc.) usam licenças permissivas compatíveis (MIT, BSD, Apache-2.0, ISC).

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/research](https://github.com/pedroiff0/research)
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
