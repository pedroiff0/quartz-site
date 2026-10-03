---
publish: true
title: Sistema Acadêmico
created: 2026-08-08 13:04
modified: 2026-10-01 20:14
tags:
- full-stack
- web-app
- academia
- cr-boletim
- multi-curso
- api-bot
repo: https://github.com/pedroiff0/sistema-academico
status: privado
cssclasses:
  - page-layout
icon: lucide-graduationcap
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

# Sistema Acadêmico

<p align="center">
  <img src="app/public/img/logo-mark.svg" alt="Sistema Acadêmico" width="72" height="72">
</p>

<p align="center">
  <a href="https://github.com/pedroiff0/sistema-academico/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/pedroiff0/sistema-academico/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://academico.phrandrade.com/demo"><img alt="Demo" src="https://img.shields.io/badge/demo-online-22c55e?logo=googlechrome&logoColor=white"></a>
  <img alt="Versão" src="https://img.shields.io/badge/versão-2.0.0-6366f1">
  <a href="./LICENSE"><img alt="Licença: GPL v3" src="https://img.shields.io/badge/licença-GPL--3.0-blue.svg"></a>
</p>

Sistema web de controle acadêmico para alunos do IFF: grade curricular,
diário de aulas, notas, frequência, boletim, coeficiente de rendimento (CR)
e planejamento de semestre — tudo derivado ao vivo do que o aluno lança, sem
planilha nenhuma no meio. Nasceu como ferramenta pessoal para um único aluno
de Engenharia de Computação e cresceu para um sistema **multi-curso** de
verdade, com painel administrativo, integração OAuth2 com o SUAP, app
mobile e uma demo pública sem senha.

**Quer ver funcionando sem criar conta?**
[academico.phrandrade.com/demo](https://academico.phrandrade.com/demo) —
entra direto autenticado (autologin), com dado sintético num banco
descartável; um botão "sair" re-semeia tudo pro próximo visitante.

## Sumário

- [Capturas de tela](#capturas-de-tela)
- [Funcionalidades](#funcionalidades)
- [Stack](#stack)
- [Como rodar](#como-rodar)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Testes e CI](#testes-e-ci)
- [Documentação](#documentação)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Capturas de tela

<p align="center">
  <img src="app/public/img/telas/tela-painel.png" alt="Painel com indicadores e calendário" width="49%">
  <img src="app/public/img/telas/tela-diario.png" alt="Diário com notas e frequência" width="49%">
</p>
<p align="center">
  <img src="app/public/img/telas/tela-cronograma.png" alt="Cronograma semanal por arrastar e soltar" width="49%">
  <img src="app/public/img/telas/tela-grafo.png" alt="Grafo de dependências entre disciplinas" width="49%">
</p>

## Funcionalidades

### Acompanhamento acadêmico

- **Diário / Boletim / Histórico** — notas por etapa (A1/A2/A3), média
  final, frequência e situação calculados ao vivo a partir de aulas e
  atividades lançadas, sempre em sincronia entre as três telas (o Boletim é
  um recorte de colunas do Diário, não uma cópia separada).
- **Coeficiente de Rendimento** — CR por período e acumulado (`crGlobal`),
  I.R.A. no padrão do SUAP, CP (coeficiente de progresso) e gráficos de
  evolução, tudo com fórmula conferida numericamente contra a planilha de
  controle original (ver [[./docs/formulas|`docs/formulas.md`]]).
- **Grade e Ementário** — catálogo completo do curso por período, com
  ementa, conteúdo programático (hierarquia real de sub-tópicos, mesmo com
  numeração inconsistente na fonte), bibliografia e pré-requisitos.
- **Grafo de Dependências** — visualização interativa (vis-network) de quem
  destrava o quê, com cascata de trancas direta ou recursiva.
- **Cronograma** — montagem da grade semanal por arrastar-e-soltar, horários
  próprios do aluno (não uma grade fixa), exportação/importação em
  JSON/CSV e atalho de impressão em PDF.
- **Chamada da Semana** — checklist rápido de presença por tempo de aula,
  com rascunho local e o dia atual sempre em destaque.
- **Simulação** — edita notas hipotéticas por atividade e vê o impacto
  projetado no CR antes de uma prova valer de verdade; nada é salvo.
- **Planejamento** — escolha de disciplinas para um semestre futuro
  (qualquer um, não só "o próximo"), filtrado pelo que está realmente
  ofertado e pelos pré-requisitos já cumpridos.
- **Cronograma de Provas** — calendário mensal de avaliações; "Atribuir ao
  diário" promove a marcação para um lançamento de nota de verdade,
  vinculado de volta (idempotente).
- **Projeção de Formatura** — quantos semestres faltam, considerando
  correquisitos e o ciclo real de oferta do curso.

### Multi-curso

Um curso (`Curso`) pode ter mais de uma versão curricular vigente ao mesmo
tempo (`PPC`), e toda disciplina é identificada por **código dentro do
curso** — nomes podem colidir entre cursos sem colidir de verdade. Hoje o
sistema atende Engenharia de Computação (IFF Bom Jesus) e Sistemas de
Informação (IFF Itaperuna), cada um com seu próprio calendário letivo e
ciclo de oferta. Detalhes em [[./docs/multi-curso|`docs/multi-curso.md`]].

### Contas e integrações

- **Cadastro provisionado pelo admin** — sem autocadastro público; o admin
  cria a conta (matrícula + nome, e-mail opcional) e o aluno define a
  própria senha no primeiro acesso, por link (convite por e-mail via Brevo)
  ou por senha temporária.
- **OAuth2 com o SUAP** — login direto pelo SUAP institucional, sem senha
  nenhuma passar pelo sistema, com import de histórico acadêmico.
- **Painel administrativo** — cadastro e edição de alunos, cursos, versões
  de PPC (com upload de PDF), catálogo de disciplinas, calendário letivo por
  curso e notificações para todos os alunos.
- **Notificações** — sino com avisos do admin e alertas automáticos do
  próprio sistema (semestre fechando, prova/trabalho a vencer).
- **App mobile** (`mobile/`, Expo/React Native) — consulta a mesma API.

### Segurança e acessibilidade

JWT em cookie httpOnly, rate limiting, CSP estrita sem `unsafe-inline`,
sanitização recursiva contra NoSQL injection, validação Zod em toda rota
mutável, LGPD (exportar/excluir a própria conta) e painel de acessibilidade
(alto contraste, fonte maior, redução de movimento). Ver
[[./SECURITY|`SECURITY.md`]].

## Stack

| Camada | Tecnologias |
|---|---|
| Backend | Node.js + Express 5, MongoDB + Mongoose, Zod (validação), JWT |
| Frontend | EJS (server-side) + JavaScript vanilla, sem bundler nem framework |
| Mobile | Expo (React Native) — `mobile/` |
| Documentos/e-mail | PDFKit (relatórios), Nodemailer/Brevo (transacional) |
| Visualização | vis-network (grafo de dependências) |
| Infra | Docker Compose (`app` + `app-demo` + `mongo` + `nginx`), MongoDB Atlas e Render em produção |
| CI | GitHub Actions — testes, syntax-check e build da imagem Docker |

Sem bundler, sem framework de frontend: cada tela é um par `.ejs` + `.js`
próprio, helpers compartilhados em `app/public/js/common.js`.

## Como rodar

```bash
cp .env.example .env          # na RAIZ do repo; defina JWT_SECRET e ALUNO_SENHA
docker compose up -d nginx    # app + demo + mongo(s), atrás de um nginx único
```

Acesse `http://localhost:4445/` (app) e `http://localhost:4445/demo/` (demo
pública — rode `docker compose exec -T app-demo node scripts/seed-demo.js`
uma vez pra ter o que mostrar). A porta é publicada em `0.0.0.0`, então
também responde pelo IP de LAN/VPN da máquina.

Sem Docker (precisa de um MongoDB acessível):

```bash
cd app && npm install
MONGO_URI=mongodb://localhost:27017/academico_db PORT=5010 npm start
```

Conta de aluno **não é autoatendida** — só o admin provisiona (`/admin`,
`POST /api/admin/alunos`: matrícula+nome, devolve uma senha gerada na hora,
uma única vez). O seed de boot cria a conta admin com senha aleatória
impressa no log do primeiro start
(`docker compose logs app | grep -A3 "Conta admin"`).

Testes (fórmulas — nota de etapa, MF, CR/CRA, CP —, sem precisar de Mongo):

```bash
cd app && npm test
```

Como serviço (systemd):

```bash
sudo cp deploy/sistema-academico.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now sistema-academico    # sobe junto com a máquina
sudo systemctl reload sistema-academico          # rebuild + up, após mudar código
```

## Estrutura do repositório

```
app/
  src/
    models/       # schemas Mongoose
    schemas/      # validação Zod (rotas mutáveis)
    services/     # regra de negócio (aritmética pura testada isoladamente)
    controllers/  # rota -> controller -> service -> model
    routes/       # superfície HTTP/API
    middleware/   # auth, csrf, sanitização, rate limit
    seeds/        # carga inicial idempotente
  views/          # EJS (aluno/*, admin/*)
  public/         # css + js vanilla, sem bundler
  test/           # node:test — fórmulas (nota, MF, CR/CRA, CP)
mobile/           # app Expo/React Native (consome a mesma API)
deploy/           # units systemd (serviço + backup)
scripts/          # backup/restore, seeds, migração de dados
docs/             # documentação de referência (Sphinx/ReadTheDocs)
docker-compose.yml
```

## Testes e CI

O GitHub Actions roda em três camadas a cada push/PR em `master`/`dev`:

1. **testes** — suíte de `node:test` sobre os módulos puros de cálculo
   (nota da etapa, MF, CR/CRA, CP, presença), sem depender de Mongo. É o
   que impede que uma fórmula seja "corrigida" por intuição e quebre em
   silêncio no boletim de alguém — ver
   [[./docs/formulas|`docs/formulas.md`]].
2. **syntax-check** — sintaxe de todo `.js` do backend/frontend e do
   `docker-compose.yml`, cobrindo o que não tem teste (views, client JS,
   scripts).
3. **docker-build** — confirma que a imagem de produção ainda builda.

## Documentação

| Arquivo | Conteúdo |
|---|---|
| [`CLAUDE.md`](./CLAUDE) | Guia técnico completo: fórmulas conferidas contra a planilha, arquitetura, armadilhas conhecidas |
| [`docs/`](./docs) | Documentação de referência: arquitetura, API, fórmulas, deploy, multi-curso, admin |
| [`docs/handoff.md`](./docs/handoff) | Estado atual do sistema em produção — pra quem assume a operação |
| [`docs/issues.md`](./docs/issues) | Bugs/melhorias mapeados, com evidência e status |
| [`CONTRIBUTING.md`](./CONTRIBUTING) | Setup local, convenções de código, fluxo de contribuição |
| [`SECURITY.md`](./SECURITY) | Autenticação, rate limiting, como reportar uma vulnerabilidade |
| [`AGENTS.md`](./AGENTS) | Guia para agentes/IA que trabalham neste repositório |

## Contribuindo

Leia o [[./CONTRIBUTING|`CONTRIBUTING.md`]] antes de abrir um PR — setup
local, convenções de código e o fluxo esperado de contribuição.

## Licença

GPL-3.0 — veja [[./LICENSE|`LICENSE`]]. Uso acadêmico.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/sistema-academico](https://github.com/pedroiff0/sistema-academico)
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
