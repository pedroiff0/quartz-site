---
cssclasses:
  - page-layout
---

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with files in this directory.

# content/ — vault Obsidian do site

Este diretório **é** o vault Obsidian de verdade que Pedro edita diretamente (`.obsidian/` na raiz daqui) — não é uma cópia — e é também, literalmente, a pasta `content/` que o Quartz consome para gerar o site. Para o motor/build/deploy (fora deste diretório), ver o [[../CLAUDE|`CLAUDE.md`]] da raiz do repo; este arquivo cobre convenções de autoria específicas de trabalhar dentro do vault.

## Estrutura e espelhamento bilíngue

- `en/...` e `pt-br/...` — conteúdo bilíngue. **Os slugs (pastas e arquivos) são idênticos nos dois idiomas** — só o segmento de idioma muda (`en/research/x` ↔ `pt-br/research/x`). Isso é o que permite o toggle de idioma (`LanguageToggle.tsx`, na raiz do repo) funcionar sem um dicionário de tradução por pasta. Ao criar conteúdo novo, sempre espelhar o nome da pasta/arquivo nos dois idiomas, mesmo que o conteúdo interno ainda não exista em um deles.
- Todo `index.md` de seção (research, resource, media, projects, blog) precisa de `order: N` no frontmatter — controla a ordem no Explorer (barra lateral). Ferramentas de sync (Quartz Syncer, `npx quartz sync`) às vezes derrubam esse campo ao normalizar frontmatter — conferir depois de qualquer sync.
- Links internos devem usar o **caminho completo a partir da raiz do conteúdo** (ex: `pt-br/research/anomaly-detection`), nunca `./relativo`. A estratégia `markdownLinkResolution: shortest` do Quartz não usa a quantidade de `.` pra calcular profundidade — ela ignora os pontos e tenta casar o restante com um slug existente. `./foo` só funciona se existir um arquivo `foo.md` na raiz.

## Status do rollout de idiomas

- `pt-br` — idioma principal, escrito primeiro, sempre completo.
- `en` — parcial, traduzido conforme o tempo permite; nem toda página tem versão em inglês ainda.
- `es`, `fr` — só a página inicial (`index.md`) existe, com aviso de "tradução ainda em preparação" e links de volta pro conteúdo em português. **Não escrever conteúdo novo nessas pastas a não ser que peçam explicitamente** — o objetivo até agora foi só disponibilizar a troca de idioma no toggle/build (`ignorePatterns` em `quartz.config.yaml`), não traduzir. Páginas ainda não traduzidas nesses idiomas caem no 404 com uma mensagem amigável ("tradução a caminho") — ver `quartz/components/pages/404.tsx` na raiz do repo.

## Frontmatter e templates do QuickAdd

Plugin QuickAdd instalado neste vault com 4 comandos, cada um usando um template em `templates/` (pasta ignorada pelo build do Quartz via `ignorePatterns`):

| Comando | Cria em |
|---|---|
| Blog | `pt-br/blog` |
| Projeto | `pt-br/projects` |
| Pesquisa | `pt-br/research` |
| Aula | `pt-br/Para Alunos` |

Convenções de frontmatter válidas para todo o vault (já embutidas nos templates):

- `publish: true` — obrigatório pra a nota ser considerada pelo Quartz Syncer/build. Sem isso a nota fica só local.
- `title` no frontmatter **nunca leva emoji decorativo** — emoji só entra no H1 do corpo da nota (`# 🔭 Título da Nota`), nunca no frontmatter. Páginas sem H1 manual (ex: notas de `projects/`, que usam só o título do frontmatter como cabeçalho da página) simplesmente não têm emoji nenhum — não é uma exceção, é a mesma regra.
- `type: blog` — habilita o widget de comentários (Giscus), controlado pela condição `is-blog` no layout do plugin `comments` (`quartz.config.yaml`, raiz do repo). Usado em `blog/` e em todas as notas de `media/` (participações em eventos).
- `password` (comentado por padrão no template de Aula) — só para notas em `Para Alunos/` que precisam de proteção por senha (plugin `encrypted-pages`, AES-256-GCM + PBKDF2). Deixar comentado para conteúdo de aula público.

## Vault Obsidian: publicação e cuidados

Publicação normalmente acontece via:

1. **Quartz Syncer** (plugin do Obsidian) — publica notas marcadas com `publish: true`. Tem um bug conhecido e aberto onde a central de publicação mostra "sucesso" mas não empurra nada de fato ([issue #123](https://github.com/saberzero1/quartz-syncer/issues/123)). Se isso acontecer, publicar manualmente com `npx quartz sync`.
2. **`npx quartz sync`** — puxa, commita e dá push. Confiável, usar como plano B.

**Configuração do plugin importa**: nas settings do Quartz Syncer (aba Frontmatter), `Frontmatter Format` precisa estar em **YAML** (não JSON) e `Include all frontmatter` precisa estar **ligado**. Em 01/08/2026 as duas estavam erradas de novo no `data.json` do plugin (`"frontmatterFormat": "json"`, `"includeAllFrontmatter": false`) e foram corrigidas no arquivo; `useBases` também foi ligado, porque as páginas de Journal Club dependem de blocos ` ```base `. Como o Obsidian reescreve esse arquivo ao fechar, **conferir na interface** depois de mexer. Já aconteceu de essas duas ficarem erradas (JSON + desligado) e o publish serializar o frontmatter inteiro como um JSON de uma linha, derrubando qualquer campo customizado que o plugin não gerencia (`titulo`, `disciplina`, `professor` em notas de aula, por exemplo) e republicando frontmatter desatualizado (títulos antigos, com emoji). Se um `git log`/diff mostrar frontmatter virando `{"publish":true,...}` numa linha só, é esse bug — conferir essas duas configurações antes de qualquer coisa.

### A armadilha das caixas de "despublicar" (já apagou o repo duas vezes)

Este repositório guarda **o vault inteiro** — notas publicadas, rascunhos (`publish: false`), o motor do Quartz e a documentação. O Quartz Syncer, porém, trata `content/` como espelho do **subconjunto publicado**: tudo que existe no repo e não está publicável aparece na Central de Publicação como candidato a *despublicar*, e o que estiver marcado ali é **removido do repositório** junto com o publish.

Foi isso — não um bug — que produziu os commits `Deleted 216 files` (31/07/2026) e `Deleted 222 files` (01/08/2026). A correlação é perfeita: dos 111 arquivos apagados no segundo caso, **110 eram `publish: false` e 1 não tinha o campo; nenhum arquivo publicado foi tocado**. Na primeira vez o site chegou a ir ao ar sem conteúdo.

Ao publicar pelo plugin, portanto:

1. Na Central de Publicação, conferir a seção de notas a **despublicar/remover** e **desmarcar tudo** que for rascunho ou arquivo de infraestrutura. Só marcar ali o que você realmente quer sumir do repositório.
2. Publicar.
3. Conferir com `git log --stat -1` que o commit não apagou nada inesperado.

Há uma rede de segurança no CI: o job de deploy tem um passo **"Guarda contra deleção em massa"** que interrompe o deploy quando um push remove mais de 20 arquivos de `content/`, para o site não ir ao ar mutilado. Ele avisa, mas não desfaz — o conserto continua sendo reverter o commit. Para uma remoção grande e intencional, dispare o deploy pelo botão "Run workflow", que não passa pela checagem.

**Cuidado com estado desatualizado**: publicações via Quartz Syncer refletem o estado local do vault Obsidian no momento do clique. Se este ambiente (onde outra sessão/Claude está editando) fez mudanças que ainda não "apareceram" no Obsidian local (ex: arquivos criados diretamente aqui), uma sincronização do plugin pode tentar reverter/apagar esse conteúdo. Sempre `git fetch && git log origin/main` antes de assumir que o remoto está no estado esperado, e resolver conflitos preservando conteúdo novo em vez de aceitar cegamente o lado remoto.

## Notas de `media/` (participações em eventos)

Cada evento é uma nota em `pt-br/media/<ano>/<slug-evento>.md`, seguindo sempre a mesma estrutura (o template em `templates/Evento.md` já vem pronto assim):

1. Frontmatter com `photoFolder: <slug>` (ver seção de fotos/banners no `CLAUDE.md` da raiz do repo) e `type: blog`.
2. `> [!note] Resumo` — 1-2 frases.
3. `## 🗓️ Sobre o evento` — dados factuais (o quê, onde, quando).
4. `## 👋 Minha participação` — o que foi apresentado, com quem, resultado.
5. `> [!note] Opinião` — reflexão pessoal sobre a experiência. **Sempre `[!note]` minúsculo** — já apareceu como `[!NOTE]`/`[!INFO]` maiúsculo por edição direta no Obsidian, e isso é inconsistente com o resto do vault.
6. `## 📎 Banner` (pôster) ou `## 📎 Slides` (apresentação oral) — o embed do PDF em si (`![[assets/banners/Banner....pdf]]`, caminho completo, ver `CLAUDE.md` da raiz).
7. `## 🔗 Referências e correlatos` — sempre linkar a página de pesquisa por trás do trabalho (`pt-br/research/...`) quando houver, e o evento anterior/seguinte que apresentou o mesmo trabalho.

Os índices (`pt-br/media/index.md` e `pt-br/media/<ano>/index.md`) **não têm mais carrossel manual** — ele é gerado automaticamente pelo plugin `photo-carousel` (ver `CLAUDE.md` da raiz). Só precisam de uma lista em markdown (`- [[caminho|Nome do Evento]] — descrição curta`) pra quem prefere navegar por texto; ao adicionar um evento novo, adicionar essa linha também (isso não é automático).

## Notas de `research/` (projetos de pesquisa)

Cada projeto de pesquisa é uma pasta própria — `pt-br/research/<slug>/index.md` (nunca um arquivo solto `pt-br/research/<slug>.md`) —, espelhando o padrão já usado por `anomaly-detection/` (que também tem uma subpasta `articles/`). Linkar sempre pelo caminho da pasta (`pt-br/research/dark-matter-shocks`), nunca com o nome do arquivo (`.../dark-matter-shocks/index.md`) — ambos resolvem, mas só o primeiro segue a convenção do resto do vault.

Sempre que um projeto novo for adicionado: (a) criar a entrada em `pt-br/research/index.md` (carrossel + lista de "Projetos"), e (b) adicionar referência cruzada nos projetos relacionados já existentes — a seção "Referências e correlatos" de cada projeto deveria formar um "triângulo" apontando pros outros projetos relevantes, não só receber links deles.

## Material de `hardcore-life` (outro vault)

`~/hardcore-life` é um vault Obsidian separado (notas pessoais, projetos, recursos de estudo). **Não é a fonte do site** — é de onde materiais específicos são selecionados e copiados manualmente, um de cada vez, nunca em bloco.

- Use `scripts/sync-material.sh "<caminho dentro de hardcore-life>" <topic-slug>` (na raiz do repo) pra copiar um arquivo pra `content[[assets/computacao/|Computacao]]<slug>/`. O script avisa (mas não bloqueia) se o nome do arquivo bate com padrões suspeitos (nome completo do usuário, "prova", "avaliação", fontes pirata como z-lib/kupdf/pdfcoffee).
- **Nunca espelhar `05 - Recursos` inteiro.** Boa parte do conteúdo lá é: (a) cópias de livros com direitos autorais de terceiros, ou (b) provas/trabalhos pessoais com nome completo. Publicar isso no site público seria infração de copyright e exposição de dados pessoais, respectivamente.
- Artigos científicos (`01 - Projetos/Anomaly_Detection/papers/`): a pasta `Anotacoes/` tem sínteses em PT geradas automaticamente (pdftotext/OCR) — algumas têm erro de extração visível (símbolos gregos, fórmulas quebradas). Ao publicar, extrair só a seção `## Síntese PT (didática)` (geralmente limpa) e a citação/BibTeX de `Notes/`; **não publicar os blocos de citação direta/OCR bruto**.
- **Biblioteca de PDFs** (`scripts/import-biblioteca.sh`): curadoria fechada em 2026-07-19 sobre `05 - Recursos/Livros e Apostilas` (4,3GB, 270 arquivos). Só entram os ~62 arquivos (~330MB) com licença aberta verificada no texto do próprio PDF (Rede e-Tec/MEC, Escola Técnica Aberta, UAB, CETAM, CC, ou permissão explícita do autor). Ficam de fora: scans de livros comerciais (Stewart, Halliday, Tanenbaum, Kurose, Iezzi, etc. — muitos vindos de z-lib/pdfcoffee/kupdf), catálogos, duplicatas e a pasta `Provas IFF` (material pessoal com nome completo). O script é executado pelo dono do site, não por sessões automatizadas. Enquanto os PDFs não são importados, as páginas linkam o [ProEdu](https://proedu.rnp.br) (host oficial dos livros e-Tec); depois da importação, trocar para links locais `assets/biblioteca/<area>/<arquivo>.pdf`.

## Pessoas com página própria

Sempre que uma nota mencionar uma destas pessoas pela primeira vez, linkar o nome pra página pessoal dela:

- Ana Cecília Soja: [https://integra.iff.edu.br/p/ana-cecilia-soja](https://integra.iff.edu.br/p/ana-cecilia-soja)
- Maria Luiza Linhares Dantas: [https://www.mlldantas.com](https://www.mlldantas.com)
- Rogério Monteiro-Oliveira: [https://www.monteiro-oliveira.com](https://www.monteiro-oliveira.com)
- Maycon Jorge Deláqua da Silva: [https://mayconjdelaqua.vercel.app/](https://mayconjdelaqua.vercel.app/)
- Ana Mara Figueiredo de Oliveira: [https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora](https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora)
