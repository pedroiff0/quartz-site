# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

# quartz-site

Site pessoal/acadêmico do Pedro Henrique, publicado em https://pedroiff0.github.io/page/ (migrando para `www.phrandrade.com`, ver `baseUrl` em `quartz.config.yaml`) via GitHub Actions a cada push em `main`.

Conteúdo detalhado sobre convenções de autoria e o vault Obsidian está em [`content/AGENTS.md`](./content/AGENTS.md) — este arquivo cobre o motor/build/deploy do site.

## Commands

```bash
npm install
npx quartz plugin install     # busca os plugins da comunidade declarados em quartz.config.yaml para .quartz/plugins (gitignored) — necessário antes de build/check/test
npx quartz build --serve      # dev server em http://localhost:8080, rebuilda a cada save
npm run check                 # tsc --noEmit + prettier --check
npm run format                 # prettier --write
npm test                       # tsx --test (roda todo *.test.ts sob quartz/)
tsx --test quartz/util/path.test.ts   # rodar um teste específico
npx quartz sync -m "descrição"  # commit + push do conteúdo (ver Deploy/Publicando)
```

`npm run install-plugins` (script de `prebuild`) roda `install-plugins.ts` diretamente — é o que `npx quartz plugin install` invoca por baixo; prefira o comando `quartz plugin install`, que é o documentado e usado no workflow de deploy.

## Arquitetura

- Fork de [jackyzha0/quartz](https://github.com/jackyzha0/quartz). `quartz/` é o motor + componentes próprios deste fork (`Head.tsx`, `LanguageToggle.tsx`, `renderPage.tsx`, `pages/404.tsx`, etc.) — não confundir com os plugins da comunidade.
- **Plugins** são declarados em `quartz.config.yaml` (`plugins:`), cada um com uma `source`:
  - `github:quartz-community/X` — baixado e cacheado em `.quartz/plugins/X` por `npx quartz plugin install` (gitignored, nunca commitado; regenerado a qualquer momento).
  - `./local-plugins/X` — plugin próprio, commitado no repo (`photo-carousel`, `page-title-i18n`). Cada um é um pacote com `package.json` (chave `quartz`: `name`/`displayName`/`category`/`components`/`defaultPosition`/`defaultPriority`) e `dist/` com JS puro compilado à mão usando `h()` do `preact` diretamente — sem etapa de build/tsx para esses.
  - Para sobrepor o comportamento de um plugin da comunidade, é mais seguro forkar como `local-plugins/` do que editar o cache em `.quartz/plugins/` (que é descartável).
- **Build** (`npx quartz build`): parseia `content/**/*.md` (frontmatter + markdown) → roda os plugins configurados (transformers → filters → emitters, na ordem/posição declaradas) → escreve em `public/` (gitignored).
- **i18n é dois sistemas separados**, não confundir:
  1. `quartz/i18n/locales/*` — strings de UI/chrome (botões, labels), várias já vêm prontas (ex: `en-US`, `pt-BR`, `es-ES`, `fr-FR`). Controlado por `cfg.locale` (hoje fixo em `pt-BR` para o site inteiro, mesmo em páginas `en/es/fr` — limitação conhecida, não corrigida).
  2. Pastas de idioma em `content/` (`en/`, `pt-br/`, `es/`, `fr/`) — conteúdo real das páginas, com slugs espelhados entre idiomas. A troca de idioma (`LanguageToggle.tsx`) só troca esse segmento da URL.
- `baseUrl` (`quartz.config.yaml`) alimenta: URLs canônicas/OG, `sitemap.xml`/RSS, e o arquivo `CNAME` (plugin `cname`, gerado automaticamente a partir do hostname do `baseUrl`). **Qualquer código que derive um prefixo de path a partir de `baseUrl` precisa usar `new URL(...).pathname`** (como em `renderPage.tsx` e `LanguageToggle.tsx`) — um split manual por `"/"` já produziu um bug de barra dupla (`//en/`) quando `baseUrl` não tinha subpath.

## Mídia: fotos, banners e o carrossel

- Fotos de eventos ficam em `content/assets/photos/<slug-do-evento>/` (ex: `assets/photos/sab2025/`), banners de pôster em `content/assets/banners/`, slides de apresentação oral em `content/assets/slides/`. Ao criar embeds `![[...]]` para esses arquivos, **sempre usar o caminho completo** (`![[assets/banners/BannerSAB25.pdf]]`), nunca só o nome do arquivo — já houve mais de um arquivo com o mesmo nome em pastas diferentes do vault (ex: `BannerSAB25.pdf` duplicado em `assets/banners/` e `assets/escolainverno/extras/`), e a resolução de "caminho mais curto" do Quartz falha silenciosamente (aponta pro lugar errado) quando há ambiguidade — sempre reconferir com um build real (`grep` no HTML gerado) depois de adicionar um banner novo.
- O plugin `local-plugins/photo-carousel` tem dois modos, ambos no mesmo componente (`dist/components/index.js`):
  1. **Nota de evento** (frontmatter tem `photoFolder`): lista todas as fotos de `assets/photos/<photoFolder>/`, cada uma linkando pro arquivo original (abre em nova aba).
  2. **Página de índice de mídia** (nota `index.md` cujo slug contém o segmento `media`, ex: `pt-br/media/index`, `pt-br/media/2025/index`): busca automaticamente, entre `allFiles`, toda nota descendente que declare `photoFolder`, e monta uma "galeria" com a primeira foto de cada uma como miniatura, linkando pra nota — **sem precisar editar HTML manualmente**. Uma nota nova só precisa de `publish: true` + `photoFolder` preenchido (mesmo que a pasta ainda esteja vazia) pra aparecer aqui; a foto real aparece assim que for adicionada, no próximo build.
  3. Como o plugin usa `fs.readdirSync` (nomes de arquivo tal como estão no disco) mas o emissor de assets do Quartz sempre baixa pra minúsculo (`slugifyFilePath`), o componente reconstrói a URL final passando pelo mesmo `slugifyFilePath` — **nunca montar a URL manualmente concatenando o nome do arquivo**, ou ela quebra pra fotos com maiúsculas (ex: `IMG_20221207_090210.jpg` de celular).
- O hover do carrossel (`.carousel-slide:hover img`, em `quartz/styles/custom.scss`) é um "lightbox" 100% CSS: a imagem some da posição normal e vira `position: fixed`, centralizada e ampliada, sobre um `::before` escurecido de tela cheia — sem JS, sem modal de verdade. Só funciona com mouse (hover); em touch não tem equivalente, e está OK assim.

## Localização física e múltiplos dispositivos

Este repositório vive fisicamente em `~/Repositorios/pessoal/quartz-site` (standalone, fora do vault `hardcore-life`, que fica em `~/hardcore-life`). Ele já morou em `~/Documentos/quartz-site`, com um symlink em `~/Documentos/repositorios/quartz-site` — **os dois caminhos antigos não existem mais** (mudança de 01/08/2026). Se alguma automação ou anotação ainda apontar pra lá, é referência morta.

- O Syncthing sincroniza `content/` (a pasta do vault Obsidian) como uma pasta própria (`quartz-content`, ver `.stfolder` em `content/`), independente do vault `hardcore-life` — não há mais aninhamento entre os dois.
- O `.git` deste repo **não** é sincronizado pelo Syncthing (a pasta `content/` é a unidade sincronizada, e `.git` fica na raiz do repo, fora dela) — histórico e `origin` (pedroiff0/page) são geridos por git normalmente em cada dispositivo.
- Conflitos de sincronização (arquivos `*.sync-conflict-*`) podem aparecer dentro de `content/` quando o Obsidian fica aberto simultaneamente em dois dispositivos — o `.gitignore` já ignora esse padrão, mas vale checar e resolver manualmente de vez em quando (comparar timestamps, escolher a versão certa, apagar a perdedora).
- Edições locais (Obsidian, ou uma sessão de Codex rodando de qualquer um dos dispositivos) chegam nos outros dispositivos quase instantaneamente via Syncthing, mas isso **não publica nada**. Publicar (disparar o deploy) sempre exige um `git push` de fato — via Quartz Syncer, `npx quartz sync`, ou push manual.

## Deploy

Workflow em `.github/workflows/deploy-gh-pages.yaml`. Passos importantes que não são óbvios:

- `npx quartz plugin install` tem que rodar **antes** do build — o script `npm run install-plugins` do `package.json` está quebrado (erro de import de `.scss` fora de bundler), não usar.
- `npm ci` exige `package-lock.json` sincronizado — se o build falhar em "Install Dependencies", rodar `npm install` local e commitar o lockfile atualizado.
