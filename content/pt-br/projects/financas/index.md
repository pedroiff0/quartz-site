---
publish: false
title: Finanças App
created: 2026-08-08 13:04
modified: 2026-08-27 13:04
tags: [Finanças, Full-stack, Web App, Orçamento, Investimentos]
repo: https://github.com/pedroiff0/financas-app
status: privado
cssclasses:
  - page-layout
---

<!-- gerado por portfolio/tools/gen_quartz.py — não editar à mão -->

**Stack:** Node.js 20, Express, MongoDB, Mongoose, EJS, JWT, Zod, Jest, Docker, Helmet

**Repositório:** [https://github.com/pedroiff0/financas-app](https://github.com/pedroiff0/financas-app) · privado

<!-- fim do bloco gerado -->

> [!note] Em uma frase
> Aplicação web de controle financeiro pessoal, carteira de investimentos e gestão de moto, com **três módulos independentes** que ligam e desligam por flag.

Cada módulo funciona sozinho — nenhum é pré-requisito do outro, e o painel se
adapta a qualquer combinação (inclusive com os três desligados):

- **Finanças** (`MODULE_FINANCAS`) — contas, categorias, lançamentos
  (receita/despesa/transferência), fixas x variáveis, recorrências, orçamentos
  por envelope e metas.
- **Investimentos** (`MODULE_INVESTIMENTOS`) — carteira multi-corretora, preço
  médio ponderado por custódia, proventos, resultado realizado e não realizado.
- **Moto** (`MODULE_MOTO`) — oficina e manutenções, abastecimentos com km/l,
  gastos (IPVA, seguro, multa), custo por km e alertas de revisão.

Duas decisões que sustentam o resto: **dinheiro em centavos inteiros** (nada de
float em valor monetário) e **valor agregado sempre derivado, nunca guardado** —
saldo soma lançamentos, preço médio recalcula pelas operações, km/l vem da
diferença de odômetro. Congelar esses números faria a correção de um registro
antigo mentir para sempre.

**Stack:** Node 20 + Express · MongoDB/Mongoose · EJS SSR + JS vanilla · Zod ·
JWT · Jest + Supertest · Docker Compose. Sem etapa de build, sem CDN, sem
framework de frontend.

**Status:** em desenvolvimento ativo, com ambiente de demonstração próprio.

## 🔗 Referências e correlatos

- Construído sobre o [[pt-br/projects/projeto-profissional|Projeto Profissional (template)]].
