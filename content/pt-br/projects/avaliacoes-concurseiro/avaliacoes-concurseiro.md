---
publish: true
title: Avaliações Concurseiro
created: 2026-08-08 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- concurso
- gamificacao
- mobile
- simulado
repo: https://github.com/pedroiff0/avaliacoes-concurseiro
status: privado
cssclasses:
- page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Sistema de Avaliações — Fork Concurseiro

Sistema web (e mobile Expo) para **concurseiros** montarem bancos de questões,
importarem o conteúdo programático de editais, organizarem o estudo em trilhas,
seguirem um **cronograma maleável** com registro de horas (Pomodoro), e
gerarem **simulados** com variantes compilados em PDF real via LaTeX. Fork do
"Sistema de Avaliações" original, focado exclusivamente no papel **concurseiro**
(não há mais professor, aluno nem módulo Live Quiz).

O concurseiro mantém um banco de questões de múltipla escolha sempre público
(identificado por banca/ano), monta simulados sem cabeçalho institucional,
cadastra questões em massa e acompanha o estudo por trilhas, metas,
cronograma, checklist diário, relatório semanal e gamificação
(XP/níveis/conquistas/streak). Inclui um app mobile com **paridade total** de
funcionalidades.

## Visão geral

- **Concurseiro**: mantém banco de questões público de múltipla escolha; monta simulados (ExamSet) com variantes; escolhe um **edital** do catálogo (ou solicita um por link) e gera uma **trilha travada** de tópicos; acompanha o estudo por **cronograma maleável** (peso por autoavaliação, sugestor de horas, carry-over, recálculo), **checklist diário** (estilo planilhadoaprovado.com), **Pomodoro** (registro de horas na plataforma) e **relatório semanal** (avanço, horas líquidas, horas perdidas/reposição).
- **Admin**: conta única do sistema. Aprova/rejeita cadastros de concurseiros, gere o **catálogo de editais** (sync das 27 UFs + upload/parsing de PDF + publicação) e gestão de usuários. Não gerencia grade curricular nem cursos (removidos neste fork).

## Stack

- **Backend**: Node.js 20 + Express + Mongoose (MongoDB)
- **Autenticação**: JWT em cookie `httpOnly`
- **Frontend web**: server-rendered com EJS + JavaScript vanilla (sem framework de build)
- **Mobile**: React Native (Expo) — paridade de funcionalidades com o web
- **Geração de PDF**: `pdflatex` real, a partir do template `Modelo_Prova_IFFBJI/provaiffmodelo.cls`
- **Arquivos binários** (imagens de questão, PDFs, editais): GridFS (MongoDB)
- **E-mail** (recuperação de senha): Mailpit (SMTP fake local) + Nodemailer
- **Testes**: Jest + Supertest + `mongodb-memory-server` (ou mongo vivo via `MONGO_TEST_URI`)
- **Infraestrutura**: Docker Compose (app + MongoDB + Mailpit)

## Como rodar (Docker - recomendado)

Pré-requisitos: Docker e Docker Compose instalados.

```bash
cp .env.example .env
docker compose up -d --build
```

A aplicação estará disponível em `http://localhost:5007`. A interface do
Mailpit (para visualizar e-mails de recuperação de senha em ambiente local)
fica em `http://localhost:8027`.

Para acompanhar os logs:

```bash
docker compose logs -f app
```

Para parar:

```bash
docker compose down
```

Os dados do MongoDB persistem no volume nomeado `mongo_data` entre
reinicializações (`docker compose down` sem `-v`).

## Como rodar localmente (sem Docker)

Requer Node.js 20+, uma instância MongoDB acessível e uma instalação de
TeX Live (com `pdflatex` no `PATH`) com os pacotes usados pelo template
(`tcolorbox`, `siunitx`, `physunits`, `pgfplots`, `babel-portuguese`, entre
outros - ver `app/Dockerfile` para a lista completa de metapacotes).

```bash
cd app
npm install
cp ../.env.example ../.env   # ajuste MONGO_URI para seu MongoDB local
npm start
```

## Variáveis de ambiente

| Variável           | Descrição                                                 | Padrão                                |
|--------------------|-----------------------------------------------------------|---------------------------------------|
| `MONGO_URI`          | String de conexão do MongoDB                              | `mongodb://localhost:27017/provas_db`   |
| `JWT_SECRET`         | Segredo para assinar os tokens JWT                        | \- (defina em produção)                |
| `JWT_EXPIRES_IN`     | Validade do token de sessão                               | `2h`                                    |
| `PORT`               | Porta HTTP da aplicação                                   | `5001` (publicada em `5007` pelo compose) |
| `NODE_ENV`           | Ambiente (`development`/`production`)                         | `development`                           |
| `APP_BASE_URL`       | URL base usada para montar o link de redefinição de senha | `http://localhost:5007`                 |
| `EDITAL_PDF_PARSING` | Habilita parsing de PDF de edital (admin)                 | `true`                                  |

## Estrutura do repositório

```
avaliacoes-concurseiro/
  Modelo_Prova_IFFBJI/      Template LaTeX (provaiffmodelo.cls) - fonte de
                            verdade para a geração de PDF
  app/
    src/
      config/               Configuração (env, conexão Mongo, GridFS)
      models/                Schemas Mongoose (User, Banca, Topico, Trilha,
                            SessaoEstudo, Meta, Edital, FaltaEstudo,
                            Cronograma, PomodoroSessao, ...)
      schemas/               Validação de entrada (zod)
      routes/ controllers/   Camada HTTP (rotas finas, controllers sem
                              lógica de negócio)
      services/              Lógica de negócio (inclui a geração de LaTeX,
                              compilação de PDF, sync de editais, cronograma,
                              faltas, relatórios, pomodoro)
      middleware/             Autenticação, autorização, upload, erros
      utils/                  Funções puras (escaping de LaTeX, RNG, etc.)
      seeds/                  Seed de bancas, tópicos de exemplo e APIs públicas
                              (sync das 27 UFs de editais)
    views/                    Templates EJS server-rendered
    public/                   CSS e JavaScript do frontend
    test/
      unit/                  Testes de funções puras
      integration/            Testes de rotas HTTP
      pdf/                    Testes de compilação real (skip se pdflatex ausente)
  mobile/                     App React Native (Expo) — paridade com o web
  docker-compose.yml
```

## Como o template LaTeX é usado

O `provaiffmodelo.cls` define macros como `\\questao`, `\\questaoSemNota`
(provas sem pontuação - o caso do concurseiro), `\\inserirfigura`,
`\\inserirtabela`, os ambientes `itens`/`alternativas` e os comandos
`\\ocultarCabecalho`/`\\ocultarRodape`. O serviço
`app/src/services/latexBuilderService.js` traduz os dados de cada questão
(armazenados no MongoDB) nesses comandos, escapando texto livre do usuário
(`app/src/utils/latexEscape.js`) e preservando fórmulas matemáticas
(`$...$`) intactas. O `app/src/services/pdfCompilerService.js` monta um
diretório de build temporário, extrai as imagens necessárias do GridFS e
invoca `pdflatex` duas vezes (padrão LaTeX), persistindo o PDF resultante de
volta no GridFS.

**Simulado concurseiro (regra imutável):** questões sempre do tipo "marcar"
(múltipla escolha) **sem pontuação** e **sem marcação IFF** — usa-se
`\\questaoSemNota` e os cabeçalhos/rodapés institucionais são ocultados.

Qualquer extensão futura ao `.cls` deve ser estritamente aditiva (nunca
alterar uma macro existente) para preservar a compatibilidade com provas já
compiladas.

## Catálogo de editais (admin)

- O admin sincroniza as **27 UFs** (`/api/admin/editais/sync-todas`) a partir da API pública `concursos-api.deno.dev/<uf>` (retorna metadados: Órgão, Vagas, UF, estado). O catálogo é global (`Edital` sem `owner`).
- O admin sobe o **PDF do edital** → parsing do conteúdo programático (disciplinas/tópicos) → revisa manualmente → **publica**.
- O concurseiro **solicita** um edital por link (`status:'solicitado'`); o admin assume e curadoria.
- A partir de um edital publicado, o concurseiro **gera uma trilha travada** (`Trilha.editavel:false`) com os tópicos do conteúdo programático.

## Cronograma de estudo (maleável)

- O usuário informa, por tópico, uma **autoavaliação 1-5** ("bom/ruim nisso") que ajusta o **peso da disciplina** (pior → mais horas).
- O **sugestor de horas** distribui a carga nos dias úteis até a prova (teto 2× a meta diária).
- Não cumprir o dia → saldo vira **carry-over** do próximo dia.
- **Recálculo** é manual e automático (ao detectar dia não cumprido); nunca há planejamento passado não-concluído. Exceção: abandono (offline 30+ dias).

## Checklist diário, Pomodoro e relatórios

- **Checklist diário** (estilo planilhadoaprovado.com): planilha de tópicos do dia, com modo "concluiu" (checkbox) ou modo "horas" (informa horas ou via Pomodoro). 0h ou < meta **exige justificativa de falta**.
- **Pomodoro**: timer (25/5/15, ajustável) acoplado a tópico/sessão; o tempo de foco vira horas estudadas na plataforma.
- **Relatório semanal**: avanço do edital (% de tópicos + horas), **horas líquidas**, **horas perdidas / reposição necessária** e faltas da semana.

## Gamificação e faltas

- XP/níveis/streak/conquistas (`gamificationService`).
- Toda falta (qualquer motivo) → **-50 XP e reset de streak**; `procrastinei` aplica penalidade extra (**-100 XP**).

## Testes

```bash
cd app
npm test              # testes unitários + integração
npm run test:unit
npm run test:integration
npm run test:pdf       # requer pdflatex instalado - compila PDFs reais
```

Para rodar contra o mongo vivo (recomendado neste fork, evita download do
`mongodb-memory-server`):

```bash
MONGO_TEST_URI=mongodb://localhost:27018/concurseiro_test npx jest --runInBand test/unit test/integration
```

## Ajustes recentes (1–9)

Os 9 ajustes deste fork (cadastro sem role, catálogo de editais, justificativa
de falta, relatório diário, cronograma maleável + autoavaliação, simulado
concurseiro sem IFF/sem pontuação, relatório semanal, Pomodoro e paridade
mobile Expo) estão documentados em `CHANGELOG.md`. O `DESIGN.md` traz o mapa
de rotas de API do concurseiro e os fluxos de estudo.

## Licença

Uso interno / educacional.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/avaliacoes-concurseiro](https://github.com/pedroiff0/avaliacoes-concurseiro)
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
