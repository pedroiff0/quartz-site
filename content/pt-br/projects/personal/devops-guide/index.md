---
publish: true
title: Guia de DevOps e Infraestrutura
created: '2026-09-28T22:55:00-03:00'
modified: 2026-11-11T15:19:40-03:00
tags:
- projeto
- publico
- pessoal
cssclasses:
  - page-layout
icon: lucide-server
repo: https://github.com/pedroiff0/devops-guide
status: ativo
license: MIT
author: Pedro Henrique Rocha de Andrade
sitesync: true
resource-sync: false
mirror_of: pedroiff0/devops-guide/README.md
---

# O.C.T.A. — Omni Clarified Technical Atlas

[![CI](https://github.com/pedroiff0/devops-guide/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroiff0/devops-guide/actions/workflows/ci.yml) [![Licença](https://img.shields.io/github/license/pedroiff0/devops-guide)](https://github.com/pedroiff0/devops-guide/blob/HEAD/LICENSE) [![Estrelas](https://img.shields.io/github/stars/pedroiff0/devops-guide?style=flat&logo=github)](https://github.com/pedroiff0/devops-guide/stargazers) [![Status](https://img.shields.io/badge/status-ativo-informational)](#status-e-próximos-passos)

Jardim digital bilíngue (PT-BR e EN-US) de engenharia e DevOps, publicado em [octa.phrandrade.com](https://octa.phrandrade.com) com Quartz v4: guias de Git e GitHub, Docker, Cloudflare, Claude, Hermes Agent, Lovable e OceanGate.

Este projeto faz parte do [portfólio](https://portfolio.phrandrade.com/#devops-guide) de Pedro Rocha.

## Sumário

- [Por que existe](#por-que-existe)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Personalização](#personalização)
- [Como funciona](#como-funciona)
- [Trabalhando no projeto](#trabalhando-no-projeto)
- [Status e próximos passos](#status-e-próximos-passos)
- [Contribuindo e suporte](#contribuindo-e-suporte)
- [Estrelas e atividade](#estrelas-e-atividade)
- [Autor](#autor)
- [Licença](#licença)

## Por que existe

A documentação oficial costuma ser densa, dispersa ou só descritiva. O O.C.T.A. reúne, em tópicos e subtópicos com exemplos reais, o que uso no dia a dia, com links cruzados entre ferramentas e protocolos.

## Funcionalidades

- Conteúdo espelhado em português (`content/pt-br/`) e inglês (`content/en/`), com troca de idioma sem quebrar a rota.
- Grafo de conhecimento interativo com as relações entre ferramentas e padrões.
- Módulo GitHub completo: Git, Conventional Commits, GitHub Flow, Actions, Snyk, SonarCloud, CLI e Pages.
- Hubs em expansão: Docker, Cloudflare, Claude, Hermes Agent, Lovable e OceanGate.
- Skills para agentes (`skills/`) que padronizam escrita, grafo e manutenção do site.
- Validadores de mensagem de commit e de simetria bilíngue dos slugs.

## Tecnologias

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white) ![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?style=flat&logo=githubpages&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)

## Instalação

### Pré-requisitos

- Node.js 22 ou superior.
- npm 10 ou superior.

### Passos

```bash
git clone https://github.com/pedroiff0/devops-guide.git
cd devops-guide
npm install
npx quartz plugin install
```

### Conferindo

```bash
npm run build
```

Saída esperada: site estático gerado em `public/`, sem erros de build.

## Como usar

### Uso básico

```bash
npm run serve
```

Abra `http://localhost:8080` para ler o site com recarregamento em tempo real.

### Exemplos

| Quero | Comando |
| :--- | :--- |
| Ver o site local | `npm run serve` |
| Gerar o site de produção | `npm run build` |
| Validar uma mensagem de commit | `bash scripts/validate-commit-msg.sh "feat: texto"` |
| Checar a simetria PT/EN | `python3 scripts/check-i18n-mirror.py` |

## Personalização

| Opção | Onde | Padrão | O que muda |
| :--- | :--- | :--- | :--- |
| Plugins, tema e grafo | `quartz.config.yaml` | tema do site | Aparência e comportamento do Quartz |
| Domínio | `static/CNAME` | `octa.phrandrade.com` | Endereço de publicação |
| Plugins locais | `local-plugins/` | título com relógio UTC-3 | Extensões do Quartz |

## Como funciona

O conteúdo é Markdown em `content/`. O Quartz o transforma em site estático e o workflow `deploy-gh-pages.yaml` publica no GitHub Pages a cada push em `main`.

```mermaid
flowchart LR
    A[content/ pt-br e en] --> B[Quartz v4]
    B --> C[public/]
    C --> D[GitHub Pages]
    D --> E[octa.phrandrade.com]
```

## Trabalhando no projeto

```bash
npm install
npm run build
python3 scripts/check-i18n-mirror.py
```

1. Crie uma branch a partir de `main`: `git checkout -b feat/<assunto-curto>`.
2. Commits no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
3. Todo texto novo em `pt-br` precisa do espelho em `en`.
4. Registre a mudança na seção `Unreleased` de [CHANGELOG.md](https://github.com/pedroiff0/devops-guide/blob/HEAD/CHANGELOG).

## Status e próximos passos

Estado atual: **ativo**. O pilar de GitHub está completo; os demais estão em expansão.

- [x] Módulo GitHub e Git completo
- [x] Publicação automática no GitHub Pages
- [ ] Completar Docker, Cloudflare e Claude
- [ ] Completar Hermes Agent, Lovable e OceanGate

## Contribuindo e suporte

Issues e pull requests são bem-vindos: veja [CONTRIBUTING.md](https://github.com/pedroiff0/devops-guide/blob/HEAD/CONTRIBUTING), [CODE_OF_CONDUCT.md](https://github.com/pedroiff0/devops-guide/blob/HEAD/CODE_OF_CONDUCT) e [SUPPORT.md](https://github.com/pedroiff0/devops-guide/blob/HEAD/SUPPORT). Vulnerabilidades seguem [SECURITY.md](https://github.com/pedroiff0/devops-guide/blob/HEAD/SECURITY).

## Estrelas e atividade

[![Histórico de estrelas](https://api.star-history.com/svg?repos=pedroiff0/devops-guide&type=Date)](https://star-history.com/#pedroiff0/devops-guide&Date)

[![Commits por mês](https://img.shields.io/github/commit-activity/m/pedroiff0/devops-guide?logo=github)](https://github.com/pedroiff0/devops-guide/graphs/commit-activity) [![Último commit](https://img.shields.io/github/last-commit/pedroiff0/devops-guide?logo=git&logoColor=white)](https://github.com/pedroiff0/devops-guide/commits) [![Issues](https://img.shields.io/github/issues/pedroiff0/devops-guide)](https://github.com/pedroiff0/devops-guide/issues) [![Pull requests](https://img.shields.io/github/issues-pr/pedroiff0/devops-guide)](https://github.com/pedroiff0/devops-guide/pulls)

## Autor

<table>
  <tr>
    <td align="center"><a href="https://github.com/pedroiff0"><img src="https://github.com/pedroiff0.png?size=120" width="96" height="96" alt="Pedro Henrique Rocha de Andrade" /><br /><sub><b>Pedro Henrique Rocha de Andrade</b></sub></a><br />Autor e mantenedor</td>
  </tr>
</table>

### Contribuidores

[![Contribuidores](https://contrib.rocks/image?repo=pedroiff0/devops-guide)](https://github.com/pedroiff0/devops-guide/graphs/contributors)

## Licença

MIT. Veja [LICENSE](https://github.com/pedroiff0/devops-guide/blob/HEAD/LICENSE).

Pedro Henrique Rocha de Andrade, 2026.
