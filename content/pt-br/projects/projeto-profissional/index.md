---
publish: false
title: Projeto Profissional (template)
created: 2026-08-08 13:04
modified: 2026-08-27 21:59
tags: [Template, Boilerplate, Segurança, Auth, Open Source]
repo: https://github.com/pedroiff0/projeto-profissional
status: público
cssclasses:
  - page-layout
---

<!-- gerado por portfolio/tools/gen_quartz.py — não editar à mão -->

**Stack:** Node.js 20, Express, MongoDB, Mongoose, EJS, JWT, Zod, Jest, Docker

**Repositório:** [https://github.com/pedroiff0/projeto-profissional](https://github.com/pedroiff0/projeto-profissional) · público

<!-- fim do bloco gerado -->

> [!note] Em uma frase
> Template minimalista e endurecido para iniciar um repositório web Node novo — o *first commit* de qualquer projeto meu.

A premissa é ser um **ponto de partida limpo e seguro**, não um framework:
clonar, renomear e começar a adicionar domínio, com as proteções já ligadas por
padrão.

O que já vem pronto:

- Autenticação **JWT** (cookie httpOnly ou Bearer) e dois papéis, `admin` e `user`.
- **Registro controlado pelo administrador** — não existe endpoint público de
  cadastro, por design.
- CSP sem `unsafe-inline`, sanitização de entrada, rate limiters, guard de CSRF
  e validação **Zod** obrigatória em toda entrada.
- Suíte de testes **Jest + Supertest** com MongoDB em memória desde o primeiro commit.
- **Docker Compose** com o container da aplicação rodando não-root e com
  filesystem read-only.

Arquitetura em camadas estritas — Rota → Controller → Service → Model — e
interface guiada por tokens de um `DESIGN.md` versionado.

**Status:** público e estável; é a base de projetos derivados.

## 🔗 Referências e correlatos

- Derivado: [[pt-br/projects/financas|Finanças App]].
