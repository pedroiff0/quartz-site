---
publish: true
title: Projeto Profissional (template)
created: 2026-08-08 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- template
- boilerplate
- seguranca
- auth
- open-source
repo: https://github.com/pedroiff0/projeto-profissional
status: público
cssclasses:
- page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Projeto Profissional — Template Mestre Canônico

<p align="center">
  <a href="https://github.com/pedroiff0/projeto-profissional/actions"><img src="https://img.shields.io/github/actions/workflow/status/pedroiff0/projeto-profissional/ci.yml?branch=main&label=CI&logo=github" alt="Status CI" /></a>
  <a href="https://github.com/pedroiff0/projeto-profissional/issues"><img src="https://img.shields.io/github/issues/pedroiff0/projeto-profissional?logo=github&color=blue" alt="Issues Abertas" /></a>
  <a href="https://github.com/pedroiff0/projeto-profissional/pulls"><img src="https://img.shields.io/github/issues-pr/pedroiff0/projeto-profissional?logo=github&color=purple" alt="PRs" /></a>
  <a href="https://github.com/pedroiff0/projeto-profissional/commits/main"><img src="https://img.shields.io/github/last-commit/pedroiff0/projeto-profissional?logo=git" alt="Último Commit" /></a>
  <a href="https://github.com/pedroiff0/projeto-profissional"><img src="https://img.shields.io/github/repo-size/pedroiff0/projeto-profissional" alt="Tamanho do Repositório" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/pedroiff0/projeto-profissional?color=brightgreen" alt="Licença" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-22_LTS-43853D?logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/Express-4.x-000000?logo=express&logoColor=white" alt="Express" />
  <img src="https://img.shields.io/badge/MongoDB-7.0-47A248?logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Zod-Validation-3E67B1?logo=zod&logoColor=white" alt="Zod" />
  <img src="https://img.shields.io/badge/Jest-Testing-C21325?logo=jest&logoColor=white" alt="Jest" />
</p>

> [!abstract] Brief do Projeto
> Template base canônico ("Golden Starter") para aplicações web completas: autenticação JWT segura, controle de papéis (`admin`/`user`), validação estrita por Zod, renderização SSR em EJS sem etapa de build, Docker Compose duplo (`dev` e `prod`) e suíte completa de testes Jest em memória desde o primeiro commit.

---

<details open>
  <summary><b>Índice / Sumário</b></summary>

  - [Visão Geral e Arquitetura](#visão-geral-e-arquitetura)
  - [Tecnologias e Stack](#tecnologias-e-stack)
  - [Como Usar este Template](#como-usar-este-template)
  - [Execução Local](#execução-local)
  - [Comandos Disponíveis](#comandos-disponíveis)
  - [Contribuição](#contribuição)
  - [Segurança](#segurança)
  - [Licença](#licença)
  - [Autor e Contato](#autor-e-contato)
</details>

---

## Visão Geral e Arquitetura

O projeto adota uma arquitetura limpa em camadas desacopladas, sem frameworks reativos pesados no frontend, priorizando entrega estável, carregamento instantâneo e conformidade com CSP (Content Security Policy).

```mermaid
graph TD
    A["Cliente / Navegador (SSR EJS + Vanilla JS)"] --> B["Nginx Proxy Reverso"]
    B --> C["Rotas & Middlewares (Auth, CSP, Rate-Limit, Zod)"]
    C --> D["Controllers (Tradução HTTP)"]
    D --> E["Services (Regras de Negócio e Domínio)"]
    E --> F["Mongoose Models / MongoDB"]
```

---

## Tecnologias e Stack

- **Runtime & Servidor:** Node.js 22 LTS, Express 4.
- **Frontend / Renderização:** EJS Server-Side Rendering, CSS modular com variáveis de tema (claro/escuro) e JS Vanilla.
- **Persistência:** MongoDB 7 com Mongoose 8.
- **Segurança:** Helmet, Cookie-Parser (`httpOnly`), JSON Web Tokens (JWT), Rate-Limiter, proteção contra injeções.
- **Qualidade & Testes:** Jest + Supertest com `mongodb-memory-server` isolado.
- **Infraestrutura:** Docker Compose com profiles de desenvolvimento e produção com isolamento de segredos.

---

## Como Usar este Template

Para criar um novo projeto a partir deste template:

```bash
# Via GitHub CLI:
gh repo create meu-novo-app --template pedroiff0/projeto-profissional --private --clone

# Ou clonando manualmente:
git clone https://github.com/pedroiff0/projeto-profissional.git meu-novo-app
cd meu-novo-app
git remote remove origin
```

---

## Execução Local

```bash
# 1. Instalar dependências
cd app && npm install

# 2. Executar suíte de testes em memória
npm test

# 3. Subir ambiente de desenvolvimento via Docker
make dev
```

---

## Comandos Disponíveis

| Comando | Descrição |
| :--- | :--- |
| `make dev` | Sobe a stack local com live-reload na porta 4429 |
| `make down` | Para e remove containers de desenvolvimento |
| `make test` | Roda suíte completa de testes Jest em memória |
| `make lint` | Executa verificações de linter e sintaxe |
| `make prod` | Executa deploy da stack de produção (porta 4430) |
| `make health` | Checa a saúde e status HTTP das portas do app |

---

## Contribuição

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes de desenvolvimento, branches e commits convencionais.

---

## Segurança

Consulte [SECURITY.md](SECURITY.md) para política de suporte e reporte confidencial de vulnerabilidades.

---

## Licença

Este projeto está sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)
- **Website:** [pedroiff.com](https://pedroiff.com)

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/projeto-profissional](https://github.com/pedroiff0/projeto-profissional)
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
