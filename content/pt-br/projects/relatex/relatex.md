---
publish: true
title: ReLaTeX
created: 2026-08-08 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- overleaf-fork
- self-hosted
- iff
- latex
repo: https://github.com/pedroiff0/relatex
status: privado
cssclasses:
- page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# ReLaTeX — self-hosted Overleaf CE for IFF (DWELF)

Single-owner Overleaf Community Edition fork, published at https://planck.dwelf-bull.ts.net
(Tailscale Funnel). Ships the IFF LaTeX classes (`texmf/tex/latex/iff/`) and a gateway that lets
AI agents start projects from templates without ever editing them directly.

## Stack (docker-compose)
- `relatex` (`relatex:fork`): web app, published on `127.0.0.1` only
  - `:8095` -> nginx `:80` (the Funnel target)
  - `:8096` -> nginx `:8081` (agent gateway, tailnet only)
  - `:8097` -> nginx `:8082` (http -> https redirect for tailnet clients)
- `mongo:7` as replica set `overleaf`, `redis:7-alpine`.
- Secrets live in `.env` (gitignored): `OVERLEAF_INVITE_TOKEN_SECRET`, `OVERLEAF_SESSION_SECRET`,
  `OVERLEAF_EMAIL_SMTP_SECRET`, `OVERLEAF_AGENT_GATEWAY_TOKEN`. Keep them stable across restarts.

## Build (important)
The real build is `repo/server-ce/Dockerfile.relatex` (the root `Dockerfile` is obsolete):

    cd repo && docker build -f server-ce/Dockerfile.relatex -t relatex:fork .
    docker compose up -d

- The base image is **pinned to `sharelatex/sharelatex:6.2.2`**. The fork source is a snapshot of
  upstream `main` that matches no release: `:latest` (6.3.0) lacks `dateformat`, 6.2.2 lacks
  `@aws-sdk/client-ses`. Never overlay the whole `services/web/app/src`.
- Only fork files are copied over the base (explicit list in the Dockerfile). `UserCreator.mjs` is
  patched with `sed` on the base file because the fork copy uses newer Analytics APIs.
- Mongo 7 works with base 6.2.2. Moving the base to 6.3.0+ requires Mongo 8 (and its FCV upgrade).
- The boot migration guard `20250519101128_binary_files_migration_check` fails non-fatally
  (database predates it; binaries are already hashed). Boot scripts in `patches/init/` tolerate it.

## Access control
- Only the emails in `OVERLEAF_ALLOWED_EMAILS` (`pedroiff0@gmail.com`) can log in, register or
  reset a password (`Features/Security/EmailAllowlist.mjs`, fail-closed). Other emails get the same
  401 as a wrong password. Public `/register` is not mounted.
- nginx recovers the real client IP from Tailscale's `X-Forwarded-For` (Tailscale overwrites any
  client-supplied value). Login throttling is per client IP: 20 requests/min per IP and 10 attempts
  per 2 min per (email, IP). An attacker cannot lock the owner out from another IP.
- Session cookie is `Secure`; `OVERLEAF_SITE_URL` must stay the https URL.

## Exposure (Tailscale)

    tailscale funnel --bg --https=443 http://127.0.0.1:8095   # public, the UI
    tailscale serve  --bg --https=8443 http://127.0.0.1:8096  # tailnet only, agent gateway
    tailscale serve  --bg --http=80    http://127.0.0.1:8097  # tailnet only, redirect to https

- The host cannot reach its own serve/Funnel ports (name resolves to `127.0.1.1`): test from another
  device, or from the host with `curl --resolve planck.dwelf-bull.ts.net:443:<funnel ip>`.
- `/agent-gateway` returns 404 on the public port by design.

## AI agents
See [`docs/agent-gateway.md`](docs/agent-gateway.md). Agents get a Bearer token, create projects from
`agent-templates/` and can only submit proposals; the owner approves them at `/ai-proposals` and the
text is inserted inside `\begin{iaparagrafo}...\end{iaparagrafo}` (`iaparagrafo.sty`).

## LaTeX classes and templates
`texmf/tex/latex/iff/` (`iffartigo`, `ifftese`, `iffposter`, `iffslides`, `macros.sty`,
`metadados.sty`, `iaparagrafo.sty`) is mounted read-only into the compile environment and
`texhash`ed at boot, so edits need no rebuild. `agent-templates/<class>/` holds one starter
project per class.

## Data
`./data` (app), `./mongo_data`, `./redis_data`. Back up before touching Mongo images: an accidental
`mongo:8` run over these files refuses to start but still rewrites WiredTiger metadata.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/relatex](https://github.com/pedroiff0/relatex)
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
