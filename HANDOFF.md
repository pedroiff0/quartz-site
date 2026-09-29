# HANDOFF — Quartz Site (Digital Garden)

## 1. Contexto Rápido
- **Repositório:** `pedroiff0/quartz-site` (`~/Repositorios/pessoal/quartz-site`).
- **Função Principal:** Digital Garden e base de conhecimento pública/semi-pública gerada via Quartz v4 a partir de notas curadas do cofre Obsidian `hardcore-life`.
- **Publicação:** GitHub Pages.

## 2. Arquitetura & Stack
- **Framework:** Quartz v4 (Node.js 22, TypeScript, Preact, MDX / Remark).
- **Conteúdo:** Diretório `content/` espelhado seletivamente do cofre.
- **Plugins Locais:** `local-plugins/` e configurações em `quartz.config.yaml`.
- **Segurança / Criptografia:** Proteção de páginas com senhas via Web Crypto (`QUARTZ_ENCRYPT_PASSWORD`).

## 3. Estado Atual & Diretrizes Operacionais
- **Governança:** AGENTS.md, DESIGN.md, Makefile e templates do GitHub ativos.
- **Comandos Principais:**
  - `make install`: Instala dependências do npm.
  - `make dev`: Sobe servidor local Quartz com live-reload (`npx quartz build --serve`).
  - `make build`: Compila site estático para a pasta `public/`.
  - `make sync`: Executa script de sincronização com o cofre Obsidian.
  - `make clean`: Remove pasta `public/` e `.quartz-cache/`.
- **Próximos Passos:**
  - Refinar filtros do script de sync para garantir que diários e notas privadas nunca sejam incluídos em `content/`.
