---
publish: true
title: Avaliações Professores
created: 2026-08-08 13:04:00-03:00
modified: 2026-09-30T13:05:50-03:00
tags:
- edtech
- banco-de-questoes
- colaborativo
repo: https://github.com/pedroiff0/avaliacoes-professores
status: privado
cssclasses:
  - page-layout
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Provas

> **Escopo atual (2026-07-15):** núcleo **professor + admin**. Os papéis
> `aluno` e `concurseiro`, bem como turmas, boletim, bancas, tópicos, sessões
> de estudo, live sessions e compartilhamento, foram removidos. Veja
> `AGENTS.md` para detalhes.

Sistema web para criação de provas, listas e trabalhos em PDF a partir de um
banco de questões reutilizável, com geração real em LaTeX e suporte ao papel
de **professor** (e administração via papel **admin**).

O professor mantém um banco de questões (organizado em pastas e tags),
seleciona um conjunto de questões e gera múltiplas variantes (provas
diferentes, com seleção e ordem aleatórias) a partir do mesmo pool, sem
precisar escrever LaTeX manualmente.

## Visão geral

Esta versão tem **dois papéis**:

- **Professor**: mantém um banco de questões **pessoal** (privado, organizado
  em pastas e tags) e consome o banco **global** (público, compartilhado
  entre professores, com _fork_ de questões). Monta provas/listas/trabalhos
  com pool de questões, peso e questões-extra, gera múltiplas variantes e
  compila cada uma em PDF real (com gabarito opcional). Importa questões em
  massa (Markdown, PDF, APIs públicas) e ajusta a apresentação da prova
  (espaço de resposta, quebra de página, cabeçalho/rodapé, instruções).
- **Admin**: aprova/rejeita/desativa contas de professor, inspeciona a saúde
  do sistema e as coleções, e controla a exposição via Tailscale. Usa o mesmo
  workspace do professor para montar provas.

> Documentação completa de engenharia (arquitetura, modelo de dados lógico e
> físico, regras de negócio, segurança, testes e metodologia) em
> [`docs/relatorio-engenharia/relatorio.pdf`](docs/relatorio-engenharia/relatorio.pdf).

## Stack

- **Backend**: Node.js 20 + Express + Mongoose (MongoDB)
- **Autenticação**: JWT em cookie `httpOnly`
- **Frontend**: server-rendered com EJS + JavaScript vanilla (sem framework
  de build)
- **Geração de PDF**: `pdflatex` real, a partir do template
  `Modelo_Prova_IFFBJI/provaiffmodelo.cls`
- **Arquivos binários** (imagens de questão, PDFs gerados): GridFS (MongoDB)
- **E-mail** (recuperação de senha): Mailpit (SMTP fake local) + Nodemailer
- **Testes**: Jest + Supertest + `mongodb-memory-server`
- **Infraestrutura**: Docker Compose (app + MongoDB + Mailpit)

## Como rodar (Docker - recomendado)

Pré-requisitos: Docker e Docker Compose instalados.

```bash
cp .env.example .env
docker compose up -d --build
```

A aplicação estará disponível em `http://localhost:3000`. A interface do
Mailpit (para visualizar e-mails de recuperação de senha em ambiente local)
fica em `http://localhost:8025`.

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

| Variável | Descrição | Padrão |
|---|---|---|
| `MONGO_URI` | String de conexão do MongoDB | `mongodb://localhost:27017/provas_db` |
| `JWT_SECRET` | Segredo para assinar os tokens JWT | - (defina em produção) |
| `JWT_EXPIRES_IN` | Validade do token de sessão | `2h` |
| `PORT` | Porta HTTP da aplicação | `3000` |
| `NODE_ENV` | Ambiente (`development`/`production`) | `development` |
| `PDFLATEX_TIMEOUT_MS` | Timeout da compilação LaTeX | `30000` |
| `MAX_UPLOAD_SIZE_MB` | Tamanho máximo de upload (imagens/arquivos) | `10` |
| `SMTP_HOST` / `SMTP_PORT` | Servidor SMTP para recuperação de senha | `localhost` / `1025` (Mailpit) |
| `MAIL_FROM` | Remetente dos e-mails enviados | `no-reply@provas.local` |
| `PASSWORD_RESET_TOKEN_TTL_MS` | Validade do link de redefinição de senha | `3600000` (1h) |
| `APP_BASE_URL` | URL base usada para montar o link de redefinição de senha | `http://localhost:3000` |

## Estrutura do repositório

```
provas/
  Modelo_Prova_IFFBJI/      Template LaTeX (provaiffmodelo.cls) - fonte de
                            verdade para a geração de PDF
  app/
    src/
      config/               Configuração (env, conexão Mongo, GridFS)
      models/                Schemas Mongoose
      schemas/               Validação de entrada (zod)
      routes/ controllers/   Camada HTTP (rotas finas, controllers sem
                              lógica de negócio)
      services/              Lógica de negócio (inclui a geração de LaTeX
                              e a compilação de PDF)
      middleware/             Autenticação, autorização, upload, erros
      utils/                  Funções puras (escaping de LaTeX, RNG, etc.)
      seeds/                  Seed automático da grade curricular
    views/                    Templates EJS server-rendered
    public/                   CSS e JavaScript do frontend
    test/
      unit/                  Testes de funções puras
      integration/            Testes de rotas HTTP (mongodb-memory-server)
      pdf/                    Testes de compilação real (skip automático se
                              `pdflatex` não estiver disponível)
  docker-compose.yml
```

## Como o template LaTeX é usado

O `provaiffmodelo.cls` define macros como `\questao`, `\questaoSemNota`
(provas sem pontuação - listas/trabalhos), `\inserirfigura`,
`\inserirtabela`, os ambientes `itens`/`alternativas` e os comandos
`\ocultarCabecalho`/`\ocultarRodape`. O serviço
`app/src/services/latexBuilderService.js` traduz os dados de cada questão
(armazenados no MongoDB) nesses comandos, escapando texto livre do usuário
(`app/src/utils/latexEscape.js`) e preservando fórmulas matemáticas
(`$...$`) intactas. O `app/src/services/pdfCompilerService.js` monta um
diretório de build temporário, extrai as imagens necessárias do GridFS e
invoca `pdflatex` duas vezes (padrão LaTeX), persistindo o PDF resultante de
volta no GridFS.

Qualquer extensão futura ao `.cls` deve ser estritamente aditiva (nunca
alterar uma macro existente) para preservar a compatibilidade com provas já
compiladas.

## Testes

```bash
cd app
npm test              # testes unitários + integração
npm run test:unit
npm run test:integration
npm run test:pdf       # requer pdflatex instalado - compila PDFs reais
```

## Licença

Uso interno / educacional.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/avaliacoes-professores](https://github.com/pedroiff0/avaliacoes-professores)
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
