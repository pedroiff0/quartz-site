---
publish: true
title: arXiv Researcher — Inteligência & Curadoria Científica Automatizada
created: 2026-08-24 14:20:00-03:00
modified: 2026-09-30T13:05:50-03:00
status: ativo
tags:
- projeto
- pessoal
- pesquisa
- astronomia
- arxiv
- automacao
- nodejs
- mongodb
- dataview
cssclasses:
  - page-layout
  - dashboard
  - project-page
icon: lucide-graduationcap
projeto: "[[pt-br/research/research/anotacoes/searcher|anotacoes]]"
sitesync: true
---
# arXiv Researcher — Sistema Autônomo de Inteligência e Curadoria Científica

[[README|← Voltar ao Hub do Projeto]]

**arXiv Researcher** é a central pessoal de ingestão, filtragem, curadoria e exportação multiformato da literatura científica do **arXiv** e **NASA ADS**, projetada especificamente para pesquisa de ponta em **Astrofísica, Astronomia Observacional (GALAH DR4, Gaia, GCNS), Detecção de Anomalias e Aprendizado de Máquina**.

> [!note]  Histórico & Evolução
> O projeto originou-se dos rascunhos arquivados em `07 - Arquivos/Searcher/` ([[20260313 - Searcher]] e [[20260321 - research]]), evoluindo de simples scripts de raspagem para uma infraestrutura completa em **Node.js 22 + Express + MongoDB**, com interface **SSR (Server-Side Rendering)**, renderização matemática com **KaTeX**, gerador de relatórios executivos em **PDF/LaTeX/XLSX/DOCX** e integração com o [[resource/artigos/biblioteca-de-artigos-cientificos|Vault de Artigos (Dataview)]].

---

## Objetivos Centrais do Projeto

1. **Daily Review Automatizado**: Monitorar todos os anúncios diários do arXiv no fuso horário de Brasília (**07:00**), com processamento paralelo de feeds RSS 2.0.
2. **Filtragem Estrita por Categorias**: Ingerir e classificar apenas papers pertencentes às subcategorias cadastradas pelo usuário (ex: `astro-ph.SR`, `astro-ph.GA`, `astro-ph.CO`, `cs.AI`, `stat.ML`).
3. **Casamento Semântico de Palavras-Chave**: Destaque prioritário (*Papers Relevantes*) para artigos cujo título ou resumo contenham termos centrais de pesquisa (`spectral`, `machine learning`, `GAIA`, `GALAH DR4`, `APOGEE`, `anomaly detection`, etc.).
4. **Renderização Matemática & Decodificação LaTeX**: Suporte completo a equações matemáticas renderizadas com **KaTeX** no servidor (SSR) e conversão de acentuação LaTeX (`\'a` $\to$ `á`, `\c{c}` $\to$ `ç`, `\~a` $\to$ `ã`) para Unicode limpo.
5. **Ações Diretas & Triagem Eficiente**: Triagem ágil no Daily Review com apenas 3 ações fundamentais: **Abrir PDF**, **Salvar na Biblioteca** ou **Descartar**.
6. **Exportações Acadêmicas Multiformato**:
   - **PDF Executivo**: Capa Retrato institucional, Tabela Paisagem com chips de categorias e Contracapa com QR Code oficial.
   - **LaTeX (`.tex` / `.cls`)**: Estrutura de artigos com citações BibTeX (`\cite{}`) e modelo tipo "Caderno de Ideias".
   - **Planilhas Excel (`.xlsx`) & Documentos Word (`.docx`)**: Para auditoria, estatísticas e compartilhamento.
   - **Notas Markdown para o Obsidian**: Registro em `05 - Recursos/Artigos/` com metadados estruturados para consulta via **Dataview**.

---

## Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                       arXiv RSS 2.0 Feeds                   │
│   astro-ph.* · cs.* · stat.* · math.* · physics.* · eess.*  │
└──────────────────────────────┬──────────────────────────────┘
                               │ Ingestão Paralela (07:00)
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                  arXiv Researcher Engine                    │
│  ┌───────────────────────┐       ┌───────────────────────┐  │
│  │   Zod Sanitization    │       │   LaTeX / KaTeX SSR   │  │
│  │   & Brasília Date     │       │   Unicode Decoder     │  │
│  └───────────────────────┘       └───────────────────────┘  │
│  ┌───────────────────────┐       ┌───────────────────────┐  │
│  │ Keyword Matching      │       │ Category Strict Group │  │
│  │ (Title + Abstract)    │       │ (Config Checklist)    │  │
│  └───────────────────────┘       └───────────────────────┘  │
└──────────────┬───────────────────────────────┬──────────────┘
               │                               │
               ▼                               ▼
┌──────────────────────────────┐ ┌─────────────────────────────┐
│      MongoDB Database        │ │    Multiformat Exporters    │
│  - DailyPaper (Triagem)      │ │  - PDF Executivo c/ QRCode  │
│  - Paper (Biblioteca Pedro)  │ │  - LaTeX (.tex / .cls)      │
│  - ArxivKeyword (CRUD)       │ │  - Excel (.xlsx) / Word     │
│  - ArxivCategory (CRUD)      │ │  - Obsidian Markdown Sync  │
└──────────────┬───────────────┘ └─────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│       Interfaces de Consumo & Visualização                  │
│  - Dashboard Life SSR Gateway (http://localhost:5003)       │
│  - Researcher CLI (`npm run harvest`)                       │
│  - Obsidian Vault `hardcore-life` (Dataview Queries)        │
│  - Quartz Site (Journal Clubs / MWBR)                       │
└─────────────────────────────────────────────────────────────┘
```

---

## Estrutura de Dados & Modelos

### . `DailyPaper` (Fila Diária de Revisão)
Armazena a coleta diária temporária para triagem rápida:
- `arxivId`: ID oficial (ex: `2608.12345`).
- `title`: Título do artigo.
- `authors`: Array de autores com nome e filiação.
- `abstract`: Resumo do artigo.
- `category`: Categoria correspondente habilitada.
- `keyword`: Palavra-chave que deu match (se houver).
- `reviewDate`: Data da revisão no fuso de Brasília (`YYYY-MM-DD`).
- `status`: `pending` | `saved` | `dismissed`.

### . `Paper` (Biblioteca Pessoal Permanente)
Acervo consolidado de artigos salvos para pesquisa:
- `status`: `saved` | `reading` | `read` | `archived`.
- `interestLevel`: `high` | `medium` | `low`.
- `rating`: Nota de 1 a 5 estrelas.
- `tags`: Marcadores customizados de pesquisa (ex: `galah-dr4`, `gaia-dr3`, `anomalias`).
- `notes`: Anotações analíticas e citações relevantes.

---

## Integração com o Obsidian (`hardcore-life`)

Ao salvar ou exportar artigos para o Obsidian, as notas são gravadas em `05 - Recursos/Artigos/` com o formato padronizado de frontmatter YAML:

```yaml
---
title: "Mapping Chemical Inhomogeneities with GALAH DR4 and Gaia DR3"
authors: "Andrade, P. H. R., Silva, J. et al."
year: 2026
doi: "10.xxxx/xxxxx"
arxiv: "https://arxiv.org/abs/2608.12345"
ads_url: "https://ui.adsabs.harvard.edu/abs/2026arXiv260812345A"
pdf: "[[resource/artigos/astronomia/2608.12345.pdf]]"
area: "Astrofísica"
status: "lido"
rating: 5
tags:
  - artigo
  - astronomia
  - galah-dr4
  - gaia
created: 2026-08-24T14:20:00
---

> [!abstract]  Resumo / Abstract
> Resumo com fórmulas matemáticas em KaTeX.

## Contribuições Principais
- Metodologia de isolamento de anomalias espectrais.

## Referências & Links
- [[resource/artigos/biblioteca-de-artigos-cientificos|Retornar ao Índice Geral de Artigos]]
```

### Consulta Dinâmica via Dataview

---

## Comandos & Operação

| Comando | Descrição |
|---|---|
| `npm run dev` | Executa o servidor com recarregamento ao vivo |
| `npm test` | Executa a suíte de testes com Jest e MongoDB em memória |
| `npm run harvest` | Executa a varredura manual de artigos via CLI |
| `docker compose up -d` | Sobe a stack completa isolada em containers Docker |

---

## Links & Referências Relacionadas

-  Repositório Local: `/home/pedro/Repositorios/pesquisa/research`
-  GitHub Oficial: [github.com/pedroiff0/research](https://github.com/pedroiff0/research)
-  Release Publicada: [Release v2.0.0 — Researcher](https://github.com/pedroiff0/research/releases/tag/v2.0.0)
-  Notas de Origem: [[20260313 - Searcher]] · [[20260321 - research]]
-  Catálogo Obsidian: [[resource/artigos/biblioteca-de-artigos-cientificos|Base de Artigos & Papers]]
-  Journal Club: [[20260414 - MWBR|Sessões MWBR]]