# 🌐 Pedro Henrique | Digital Garden & Academic Portfolio

<div align="center">

[![Quartz v5](https://img.shields.io/badge/Engine-Quartz%20v5-purple?style=for-the-badge&logo=quartz)](https://quartz.jzhao.xyz/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Obsidian](https://img.shields.io/badge/Obsidian-Vault%20Sync-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white)](https://obsidian.md/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Deploy](https://img.shields.io/github/actions/workflow/status/pedroiff0/quartz-site/deploy.yml?branch=main&label=Deploy&style=for-the-badge)](https://www.phrandrade.com)

**Jardim digital, base de conhecimento acadêmica e portfólio pessoal.**

[🌍 Website Oficial (www.phrandrade.com)](https://www.phrandrade.com) • [💻 Repositório do Cofre (hardcore-life)](https://github.com/pedroiff0/hardcore-life) • [💼 LinkedIn](https://www.linkedin.com/in/pedroiff0/)

</div>

---

## 📖 Visão Geral

Este repositório contém o código-fonte e o ecossistema estático do **site pessoal e jardim digital** de **Pedro Henrique Rocha de Andrade** (Graduando em Engenharia de Computação pelo Instituto Federal Fluminense - IFF).

O projeto é construído sobre o **[Quartz v5](https://quartz.jzhao.xyz/)**, personalizado e estendido para atuar como um portal público de notas, projetos, pesquisas acadêmicas, modelos em LaTeX e documentação técnica, sincronizado diretamente com o cofre de notas Obsidian via pipeline automatizado.

---

## ✨ Principais Funcionalidades

- 🌐 **Arquitetura Multilíngue (i18n):** Suporte completo para **Português (PT-BR)** e traduções integradas para **Inglês (EN)**, **Espanhol (ES)** e **Francês (FR)**, com alternador dinâmico de idiomas baseado em mapeamento de slugs.
- 📚 **Hub Acadêmico & Disciplinas:** Mais de 90 disciplinas e anotações de aula estruturadas por período, com ementas, professores, mintermos, exercícios e tabelas dinâmicas.
- 📊 **Diagramas Mermaid & KaTeX LaTeX:**
  - Renderização nativa de diagramas **Mermaid** com adaptação dinâmica para modo claro e escuro.
  - Suporte completo a fórmulas matemáticas e expressões booleanas em **KaTeX** com macros customizadas (`\bar{}`, `\overline{}`).
- 🕒 **Formatador Inteligente de Metadados:** Conversão automática de datas e horários em formato localizado (`DD de Mês de YYYY HH:MM` para PT-BR e formato 12h com `AM/PM` para EN).
- 🔄 **Pipeline de Sincronização Automatizado:** Script `tools/sync_from_vault.py` responsável por higienizar links Markdown, avaliar queries Dataview para tabelas estáticas, sanitizar tags e sincronizar o cofre Obsidian `hardcore-life`.
- 📖 **Modo Leitor & Tema Escuro/Claro:** Botão de leitura focada e alternador de tema persistente via `localStorage`.

---

## 🗂️ Estrutura do Repositório

```text
quartz-site/
├── content/                     # Conteúdo Markdown sincronizado
│   ├── pt-br/                   # Conteúdo principal (Português)
│   │   ├── sobre-mim/           # Apresentação, Setup, Minhas Coisas e Recomendações
│   │   ├── projects/            # Projetos e sistemas desenvolvidos
│   │   ├── research/            # Pesquisas científicas e publicações
│   │   ├── resource/            # Disciplinas do IFF, Escola de Inverno e Cursos
│   │   └── media/               # Premiações e participações em congressos
│   ├── en/                      # Versão em Inglês
│   ├── es/, fr/                 # Versões em Espanhol e Francês
│   └── assets/                  # Mídias, imagens e documentos PDF
├── quartz/                      # Motor e componentes do Quartz
│   ├── components/              # Componentes Preact customizados (CustomFooter, Date, ReaderMode, etc.)
│   ├── plugins/                 # Transformadores e emissores AST (Markdown/HTML)
│   └── styles/                  # Estilos globais e responsivos em SCSS
├── tools/
│   └── sync_from_vault.py       # Engine de sincronização cofre Obsidian -> site
├── quartz.config.yaml           # Configurações do Quartz, plugins e layouts
└── package.json                 # Dependências e scripts npm
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- [Node.js](https://nodejs.org/) (versão 18+ recomendada)
- [Python 3.10+](https://www.python.org/) (para os scripts de sincronização)

### Instalação e Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/pedroiff0/quartz-site.git
   cd quartz-site
   ```

2. **Instale as dependências:**
   ```bash
   npm install
   ```

3. **Sincronize as notas do cofre (opcional se quiser atualizar conteúdo):**
   ```bash
   python3 tools/sync_from_vault.py
   ```

4. **Inicie o servidor de desenvolvimento:**
   ```bash
   npx quartz build --serve
   ```
   Acesse **`http://localhost:8080`** no seu navegador.

---

## 🧪 Qualidade de Código & Verificação

```bash
# Verificação estática e formatação
npm run check

# Formatar arquivos com Prettier
npm run format

# Executar suíte de testes
npm test
```

---

## 🚢 Deploy e Publicação

O site é automaticamente compilado e publicado via **GitHub Actions** em cada push na branch `main`.

1. As notas editadas no cofre Obsidian são sincronizadas via `tools/sync_from_vault.py`.
2. O workflow `.github/workflows/deploy-gh-pages.yaml` executa o build otimizado com o Quartz.
3. O bundle gerado é distribuído e servido em **[www.phrandrade.com](https://www.phrandrade.com)**.

---

## 📄 Licença

Este projeto é disponibilizado sob a licença [MIT](LICENSE).

O motor base é derivado do [Quartz](https://github.com/jackyzha0/quartz) criado por [Jacky Zhao](https://github.com/jackyzha0).

---

<div align="center">
Desenvolvido com 💜 por <b>Pedro Henrique Rocha de Andrade</b>
</div>
