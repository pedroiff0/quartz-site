---
publish: true
title: Custos App
created: '2026-09-28T22:55:00-03:00'
modified: 2026-09-30T13:05:50-03:00
tags:
- projeto
- publico
- profissional
cssclasses:
  - page-layout
icon: lucide-calculator
repo: https://github.com/pedroiff0/custos-app
status: ativo
license: MIT
author: Pedro Henrique Rocha de Andrade
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Zenith FinOps & Custos SaaS

> Aplicação SaaS completa para **gestão de custos de infraestrutura cloud (VPS, Hetzner, AWS, DigitalOcean), assinaturas de deploy (Vercel, Supabase, Cloudflare), rateio por cliente e simulação de precificação de software**.

---

## Principais Funcionalidades

1. ** Inventário de Servidores & VPS:**
   - Cadastro de máquinas com especificações (vCPU, RAM, SSD, Provedor).
   - Conversão e câmbio automático de moedas estrangeiras (USD e EUR para BRL).
   - Rateio de custos por cliente e identificação de capacidade ociosa.

2. ** Catálogo de Assinaturas & Ferramentas de Deploy:**
   - Controle de serviços SaaS (Vercel, Supabase, Railway, GitHub, Cloudflare, Sendgrid, domínios).
   - Amortização de planos anuais em custo mensal contábil.
   - Rateio entre projetos ou custo geral compartilhado.

3. ** DRE & Margem de Lucro por Cliente:**
   - Demonstração de Resultado individual: Faturamento Bruto - Custos de Servidores - Custos de Assinaturas = Margem Real de Lucro.
   - Alertas automáticos no dashboard quando a margem de um cliente fica abaixo da meta.

4. ** Calculadora & Simulador de Precificação:**
   - Simulação de novas propostas comerciais.
   - Cálculo automático do Preço de Venda com base em infraestrutura + horas de mão de obra + margem alvo + provisão de impostos.

5. ** API REST & Integração com `financas-app`:**
   - Gerenciamento de chaves de API (`cst_live_...`).
   - Endpoint `GET /api/integracao/v1/resumo` para alimentar dashboards centrais.
   - Endpoint `GET /api/integracao/v1/despesas-mes` para sincronizar as despesas diretamente no `financas-app`.

6. ** Modelo de Negócio SaaS (R$ 10,00 / mês):**
   - Plano Pro com valor acessível de R$ 10,00/mês (1.000 centavos).
   - 14 dias de teste gratuito (Trial) concedidos no cadastro.

7. ** Notificações e Anúncios de Manutenção:**
   - Central de avisos in-app (vencimento de faturas, alertas de margem).
   - Painel para o administrador transmitir comunicados de novas releases para todos os usuários.

---

## Arquitetura do Sistema

```
custos-app/
 app/
    src/
       config/      # env.js, db.js, metrics.js
       models/      # cliente, servidor, assinatura, calculadora, apiKey, user, notification
       services/    # Regras de FinOps, rateio, precificação, integração e SaaS
       controllers/ # req -> service -> res
       routes/      # Endpoints REST e SSR
       middleware/  # auth, apiKeyAuth, saasGuard, csrfGuard, rateLimiters
       schemas/     # Validações estritas com Zod
       seeds/       # Seed de demonstração e admin
    views/           # Telas SSR em EJS
    public/          # Scripts client-side Vanilla JS (sem inline script) e CSS
    tests/           # Suíte de testes automatizados com Jest e Supertest
 .github/
    ISSUE_TEMPLATE/  # Templates de Issue (Feature, Bug, Task, Doc, Release)
    workflows/       # CI/CD automatizado
    PULL_REQUEST_TEMPLATE.md
 GUIA-CAVEMAN-PIPELINE.md # Manual passo a passo do fluxo GitHub
```

---

## Como Executar

### 1. Pré-requisitos
- Node.js >= 20
- MongoDB >= 6.0 (ou Docker)

### 2. Rodando Localmente

```bash
# 1. Entre na pasta da aplicação
cd app

# 2. Instale as dependências
npm install

# 3. Configure o arquivo de ambiente
cp .env.example .env

# 4. Popule com dados de demonstração FinOps
npm run seed:demo

# 5. Inicie o servidor de desenvolvimento
npm run dev
```

Acesse em: `http://localhost:3379` (ou porta configurada no `.env`).

### 3. Rodando com Docker Compose

```bash
docker compose -f compose.dev.yml up -d
```

---

## Rodando os Testes

```bash
cd app
npm test
```

---

## Fluxo de Trabalho (Pipeline Caveman)

Este repositório adota o fluxo de engenharia rigoroso com **Issue First**, **Branch Isolada**, **Commits Semânticos**, **Code Review em Pull Request**, **Merge**, **Aviso aos Usuários** e **Releases Versionadas** (`v0.1.0-beta.1`  `v0.1.1-beta.2`).

 **Consulte o manual completo em [GUIA-CAVEMAN-PIPELINE.md](./GUIA-CAVEMAN-PIPELINE.md)**.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/custos-app](https://github.com/pedroiff0/custos-app)
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
