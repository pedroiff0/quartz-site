---
publish: true
title: "SpectraViewer — Visualizador Espectral"
created: 2026-09-28 22:55
modified: 2026-09-29 09:05
tags:
  - projeto
  - publico
  - academico
cssclasses:
  - page-layout
icon: lucide-activity
repo: "https://github.com/pedroiff0/spectraviewer"
status: ativo
license: MIT
author: Pedro Henrique Rocha de Andrade
---

# SpectraViewer — Visualizador Espectral

<p align="center">
  <a href="https://github.com/pedroiff0/spectraviewer/actions"><img src="https://img.shields.io/github/actions/workflow/status/pedroiff0/spectraviewer/ci.yml?branch=main&label=CI&logo=github" alt="Status CI" /></a>
  <a href="https://github.com/pedroiff0/spectraviewer/issues"><img src="https://img.shields.io/github/issues/pedroiff0/spectraviewer?logo=github&color=blue" alt="Issues Abertas" /></a>
  <a href="https://github.com/pedroiff0/spectraviewer/pulls"><img src="https://img.shields.io/github/issues-pr/pedroiff0/spectraviewer?logo=github&color=purple" alt="PRs" /></a>
  <a href="https://github.com/pedroiff0/spectraviewer/commits/main"><img src="https://img.shields.io/github/last-commit/pedroiff0/spectraviewer?logo=git" alt="Último Commit" /></a>
  <a href="https://github.com/pedroiff0/spectraviewer"><img src="https://img.shields.io/github/repo-size/pedroiff0/spectraviewer" alt="Tamanho do Repositório" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/pedroiff0/spectraviewer?color=brightgreen" alt="Licença" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" /> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit" />
</p>

> [!abstract] Brief do Projeto
> Interface web interativa de inspeção e ajuste contínuo de espectros estelares FITS do GALAH DR4.

---

<details open>
  <summary><b>Índice / Sumário</b></summary>

  - [Visão Geral e Arquitetura](#visão-geral-e-arquitetura)
  - [Tecnologias e Stack](#tecnologias-e-stack)
  - [Pré-requisitos e Configuração](#pré-requisitos-e-configuração)
  - [Como Executar Localmente](#como-executar-localmente)
  - [Comandos e Scripts Disponíveis](#comandos-e-scripts-disponíveis)
  - [Principais Funcionalidades](#principais-funcionalidades)
  - [Contribuição](#contribuição)
  - [Segurança](#segurança)
  - [Licença](#licença)
  - [Autor e Contato](#autor-e-contato)
  - [Links e Referências](#links-e-referências)
</details>

---

## Visão Geral e Arquitetura

Descrição da visão geral da solução, modelo de arquitetura de software, fluxo de dados e integração de componentes.

```mermaid
graph TD
    A["Cliente / Interface Web"] --> B["API Gateway / Servidor"]
    B --> C["Serviços & Regras de Negócio"]
    C --> D["Banco de Dados / Persistência"]
```

---

## Tecnologias e Stack

- **Python**
- **Streamlit**
- **Plotly**
- **Astropy**

---

## Pré-requisitos e Configuração

### Pré-requisitos
- Node.js (versão 18.x ou superior) / Python 3.11+
- Gerenciador de pacotes: `npm` ou `pip`
- Git instalado

---

## Como Executar Localmente

```bash
# 1. Clonar o repositório
git clone https://github.com/pedroiff0/spectraviewer.git

# 2. Acessar o diretório do projeto
cd spectraviewer

# 3. Instalar as dependências
npm install

# 4. Executar a aplicação
npm run dev
```

---

## Comandos e Scripts Disponíveis

| Comando | Descrição |
| :--- | :--- |
| `npm run dev` | Inicia a aplicação em ambiente local |
| `npm run build` | Compila o projeto para produção |
| `npm run test` | Executa a suíte de testes |

---

## Principais Funcionalidades

- **Recurso Principal:** Solução estruturada para o domínio do projeto.
- **Interface e Usabilidade:** Design responsivo e navegação fluida.
- **Integração:** Comunicação com APIs e armazenamento persistente.

---

## Contribuição

Contribuições são muito bem-vindas! Caso deseje contribuir com correções, melhorias ou novas funcionalidades:

1. Faça um Fork do repositório.
2. Crie uma branch para a sua funcionalidade (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'feat: adiciona nova funcionalidade'`).
4. Envie para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request detalhado.

---

## Segurança

Caso você descubra alguma vulnerabilidade de segurança, por favor não abra uma issue pública. Reporte o problema enviando um e-mail diretamente ao mantenedor do projeto.

---

## Licença

Este projeto está licenciado sob os termos da licença **MIT**. Consulte o arquivo [LICENSE](https://github.com/pedroiff0/spectraviewer/blob/main/LICENSE) para obter mais detalhes.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [spectraviewer](https://github.com/pedroiff0/spectraviewer)
- **Índice de Projetos:** [[01-projetos/site-publico/projetos-publicos|Projetos Públicos]]

---

<p align="center">
  <a href="https://github.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://linkedin.com/in/pedro-andrade-iff" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://instagram.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="mailto:pedro.andrade@iff.edu.br"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://pedroiff.com" target="_blank"><img src="https://img.shields.io/badge/Website-000000?style=flat-square&logo=googlechrome&logoColor=white" alt="Website" /></a>
</p>

<p align="center">
  <sub>© 2026 <b><a href="https://pedroiff.com">Pedro Rocha</a></b> — Computer Engineering &amp; Computational Astrophysics</sub><br />
  <sub>Made with <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M10 2v2'/><path d='M14 2v2'/><path d='M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1'/><path d='M6 2v2'/></svg>" width="16" height="16" valign="middle" alt="coffee" />, <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='m16 18 6-6-6-6'/><path d='m8 6-6 6 6 6'/></svg>" width="16" height="16" valign="middle" alt="code" /> and <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='3'/><path d='M3 12a9 9 0 0 1 9-9 9 9 0 0 1 9 9 9 9 0 0 1-9 9 9 9 0 0 1-9-9'/><path d='M5.5 5.5a13 13 0 0 0 13 13'/><path d='M18.5 5.5a13 13 0 0 1-13 13'/></svg>" width="16" height="16" valign="middle" alt="astrophysics" /> by <b><a href="https://github.com/pedroiff0">Pedro Henrique Rocha de Andrade</a></b></sub>
</p>
