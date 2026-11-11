---
publish: true
title: Formulários
tags:
- resumo
- formulas
repo: https://github.com/pedroiff0/formularios
status: público
cssclasses:
  - page-layout
created: '2026-09-14T11:17:03-03:00'
modified: 2026-11-11T15:23:57-03:00
icon: lucide-notebookpen
sitesync: true
resource-sync: false
mirror_of: pedroiff0/formularios/README.md
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>Projetos Públicos</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Formulários</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/personal/devops-guide/index|← Guia de DevOps e Infraestrutura]]</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">Hub</span> <span class="academic-nav-counter">(6 de 10)</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/personal/meu-setup/index|meu-setup →]]</span>

</div>

</div>

</div>

# Formulários

[![CI](https://github.com/pedroiff0/formularios/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroiff0/formularios/actions/workflows/ci.yml) [![Licença](https://img.shields.io/github/license/pedroiff0/formularios)](https://github.com/pedroiff0/formularios/blob/HEAD/LICENSE) [![Estrelas](https://img.shields.io/github/stars/pedroiff0/formularios?style=flat&logo=github)](https://github.com/pedroiff0/formularios/stargazers) [![Status](https://img.shields.io/badge/status-ativo-informational)](#status)

Coleção de folhas de fórmulas e resumos em LaTeX, organizada por disciplina (Cálculo e Física), com um PDF por capítulo e um PDF combinado.

Este projeto faz parte do [portfólio](https://portfolio.phrandrade.com/#formularios) de Pedro Rocha.

## Sumário

- [Resumo](#resumo)
- [Contexto](#contexto)
- [Tecnologias](#tecnologias)
- [Começando](#começando)
- [Como usar](#como-usar)
- [Reprodução dos resultados](#reprodução-dos-resultados)
- [Metodologia](#metodologia)
- [Dados](#dados)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Trabalhando no projeto](#trabalhando-no-projeto)
- [Status](#status)
- [Como citar](#como-citar)
- [Como contribuir](#como-contribuir)
- [Código de conduta](#código-de-conduta)
- [Segurança](#segurança)
- [Suporte](#suporte)
- [Estrelas e atividade](#estrelas-e-atividade)
- [Autor](#autor)
- [Licença](#licença)

## Resumo

Folhas de fórmulas costumam ficar espalhadas em cadernos e PDFs de origens diferentes, com notação inconsistente. Este repositório reúne, em LaTeX, as fórmulas das disciplinas de Cálculo e Física do curso, com a mesma configuração visual e um Makefile que gera um PDF por capítulo, um por disciplina e um combinado. Limitação: o conteúdo cobre só as disciplinas já cursadas e não substitui o material do professor.

## Contexto

Material de estudo da graduação em Engenharia de Computação (IFF), mantido para consulta rápida em provas e listas.

### Objetivos

- Padronizar a notação das fórmulas entre capítulos e disciplinas.
- Gerar PDFs de consulta curtos, por capítulo.
- Garantir por CI que todos os capítulos compilam.

## Tecnologias

![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white) ![Make](https://img.shields.io/badge/Make-6D00CC?style=flat&logo=gnu&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

## Começando

### Pré-requisitos

- TeX Live com `pdflatex` e o pacote `siunitx` (Debian/Ubuntu: `texlive-science`).
- `make`.

### Instalação

```bash
git clone https://github.com/pedroiff0/formularios.git
cd formularios
```

### Conferindo que funcionou

```bash
make all
```

Saída esperada: o `main.pdf` é gerado na raiz e os arquivos temporários são removidos.

## Como usar

### Exemplo 1: PDF de uma disciplina

```bash
make fisicas
```

Gera `fisicas/fisicas.pdf`. Para Cálculo: `make calculos`.

### Exemplo 2: PDF de um capítulo

```bash
make fisicaiii cap30
```

### Opções principais

| Opção | Efeito |
| :--- | :--- |
| `FAST=1` | Compila em modo rascunho, uma única passada |
| `VERBOSE=1` | Mostra os passos de cada build |
| `disciplines="calculos,fisicas"` | Gera um PDF por capítulo das disciplinas listadas |

## Reprodução dos resultados

Cada PDF é regenerado por um comando `make`; o CI refaz todos a cada push.

| Resultado | Comando |
| :--- | :--- |
| Um PDF por capítulo | `make disciplines="calculos,fisicas" VERBOSE=1` |
| PDF combinado | `make combined VERBOSE=1` |

## Metodologia

Cada capítulo é um arquivo `.tex` incluído por disciplina. O Makefile monta um arquivo temporário (`build_*.tex`) que inclui só o capítulo pedido, compila com `pdflatex` e apaga os auxiliares.

```mermaid
flowchart LR
    A[capítulo .tex] --> B[build_*.tex]
    B --> C[pdflatex]
    C --> D[PDF do capítulo]
```

## Dados

Não há dados externos: o conteúdo é texto LaTeX do próprio repositório.

## Estrutura do repositório

```text
formularios/
├── calculos/      capítulos de Cálculo
├── fisicas/       capítulos de Física
├── animacoes/     figuras animadas
├── latexconfig/   preâmbulo e estilo compartilhados
├── scripts/       utilitários de build
├── main.tex       documento principal
└── Makefile       alvos de compilação
```

## Trabalhando no projeto

### Ambiente de desenvolvimento

```bash
make fisicas-fast
```

### Fluxo de trabalho

1. Crie uma branch a partir de `main`: `git checkout -b feat/<assunto-curto>`.
2. Commits no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
3. Rode `make combined` antes de abrir o pull request.
4. Registre a mudança na seção `Unreleased` de [CHANGELOG.md](https://github.com/pedroiff0/formularios/blob/HEAD/CHANGELOG).

### Convenções

Um capítulo por arquivo, notação do preâmbulo em `latexconfig/` e um parágrafo por linha no texto.

## Status

Estado atual: **ativo**. Faltam capítulos das disciplinas dos próximos períodos.

- [x] Cálculo e Física com build por capítulo
- [x] CI que compila todos os capítulos
- [ ] Novas disciplinas

## Como citar

Use o arquivo [CITATION.cff](CITATION.cff) (botão "Cite this repository" do GitHub).

## Como contribuir

Contribuições são bem-vindas. Antes de começar, leia o [guia de contribuição](https://github.com/pedroiff0/formularios/blob/HEAD/CONTRIBUTING).

1. Abra uma issue descrevendo o problema ou a ideia.
2. Crie uma branch a partir de `main`: `git checkout -b feat/<assunto-curto>`.
3. Faça commits no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
4. Abra o pull request e registre a mudança em [CHANGELOG.md](https://github.com/pedroiff0/formularios/blob/HEAD/CHANGELOG).

## Código de conduta

Este projeto adota o [Código de Conduta](https://github.com/pedroiff0/formularios/blob/HEAD/CODE_OF_CONDUCT). Ao participar, você concorda em segui-lo.

## Segurança

Não abra issue pública para vulnerabilidades. Siga o procedimento de [SECURITY.md](https://github.com/pedroiff0/formularios/blob/HEAD/SECURITY) para reportar de forma confidencial.

## Suporte

Dúvidas e pedidos de ajuda: veja [SUPPORT.md](https://github.com/pedroiff0/formularios/blob/HEAD/SUPPORT).

## Estrelas e atividade

[![Histórico de estrelas](https://api.star-history.com/svg?repos=pedroiff0/formularios&type=Date)](https://star-history.com/#pedroiff0/formularios&Date)

[![Commits por mês](https://img.shields.io/github/commit-activity/m/pedroiff0/formularios?logo=github)](https://github.com/pedroiff0/formularios/graphs/commit-activity) [![Último commit](https://img.shields.io/github/last-commit/pedroiff0/formularios?logo=git&logoColor=white)](https://github.com/pedroiff0/formularios/commits) [![Issues](https://img.shields.io/github/issues/pedroiff0/formularios)](https://github.com/pedroiff0/formularios/issues) [![Pull requests](https://img.shields.io/github/issues-pr/pedroiff0/formularios)](https://github.com/pedroiff0/formularios/pulls)

## Autor

<table>
  <tr>
    <td align="center"><a href="https://github.com/pedroiff0"><img src="https://github.com/pedroiff0.png?size=120" width="96" height="96" alt="Pedro Henrique Rocha de Andrade" /><br /><sub><b>Pedro Henrique Rocha de Andrade</b></sub></a><br />Autor e mantenedor</td>
  </tr>
</table>

### Contribuidores

[![Contribuidores](https://contrib.rocks/image?repo=pedroiff0/formularios)](https://github.com/pedroiff0/formularios/graphs/contributors)

## Licença

Distribuído sob a licença MIT. Texto completo do arquivo [LICENSE](https://github.com/pedroiff0/formularios/blob/HEAD/LICENSE):

```txt
# MIT License

Copyright (c) 2025 Pedro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

<img src="https://api.iconify.design/mdi/star-shooting.svg?color=%23c678dd" width="20" valign="middle" /> *"Keep looking up."*

<br>

<sub>© 2026 Pedro Rocha — Computer Engineering & Computational Astrophysics · IFF / PIBIC-CNPq, made with ☕, code and ☄️ by Pedro Henrique Rocha de Andrade</sub>

</div>
