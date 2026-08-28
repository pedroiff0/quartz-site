---
publish: false
title: Desenvolvimento Web
created: 2026-07-26 13:04
modified: 2026-08-27 13:04
published: 2026-07-26T11:33:09.975-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] O que é este tópico
> Desenvolvimento Web é o estudo de como um sistema roda distribuído entre um **servidor** e um **navegador**, comunicando através do protocolo HTTP — front-end (o que o usuário vê e interage), back-end (a lógica e o acesso a dados que rodam no servidor) e o banco de dados por trás de tudo.

## Por que estudar isso?

É, com boa margem, a habilidade mais imediatamente empregável do curso: a grande maioria das vagas de estágio e nível júnior em computação passa por alguma camada web, mesmo em áreas que não são "desenvolvimento web" por definição (ciência de dados expõe resultados em dashboards web, sistemas embarcados têm interfaces de configuração via navegador, pesquisa acadêmica publica resultados em páginas — este próprio site é feito com as mesmas ideias de front-end estático).

Além do valor prático, web é onde os conceitos de Redes (HTTP, cliente-servidor) e Banco de Dados (SQL, modelagem) se encontram e viram sistema funcionando de ponta a ponta — é a disciplina mais "integradora" do currículo nesse sentido.

## Trilha de estudo

### 1. Fundamentos da Web (1–2 semanas)

O que dominar: uma breve história da Internet e da World Wide Web (a diferença entre as duas: Internet é a infraestrutura de rede, Web é um dos serviços que roda sobre ela), o modelo **cliente-servidor** — o navegador (cliente) envia uma requisição HTTP, o servidor processa e devolve uma resposta —, os principais métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`) e códigos de status (`200 OK`, `404 Not Found`, `500 Internal Server Error`). O que praticar: abrir as ferramentas de desenvolvedor do navegador (aba Network) e observar as requisições reais que um site qualquer faz ao carregar.

![O modelo cliente-servidor: o cliente envia requisições, o servidor processa e responde — a base de toda comunicação na Web.](https://commons.wikimedia.org/wiki/Special:FilePath/Client-server-model.svg)

### 2. Desenvolvimento Front-End (3–4 semanas)

O que dominar: HTML semântico (estruturar conteúdo com as tags certas, não só `<div>` pra tudo), CSS (o modelo de caixa — _box model_ —, e os dois sistemas de layout modernos, Flexbox e Grid), e JavaScript no navegador (manipulação do DOM, tratamento de eventos, requisições assíncronas com `fetch`). O que praticar: construir uma página estática simples (um formulário com validação em JavaScript) sem usar nenhum framework — entender a plataforma antes de abstraí-la é o que evita depender de "mágica" que você não sabe depurar.

### 3. Desenvolvimento Back-End (3–4 semanas)

O que dominar: como um servidor HTTP roteia requisições para código que as processa, o estilo arquitetural **REST** (recursos identificados por URL, verbos HTTP com significado semântico), e os dois mecanismos mais comuns de autenticação/sessão — sessão baseada em cookie (o servidor guarda estado) vs. token (ex: JWT — o próprio token carrega a informação, sem estado no servidor). O que praticar: construir uma API REST simples (um CRUD de "tarefas", por exemplo) usando qualquer framework (Express, Django, Flask) e testá-la com uma ferramenta como Postman ou `curl`.

### 4. Banco de dados em sistemas Web (2 semanas)

O que dominar: como uma aplicação web se conecta a um Sistema de Gerenciamento de Banco de Dados (SGBD), o papel de um ORM (mapear objetos do código para tabelas do banco, evitando escrever SQL manual toda vez), e por que **nunca** confiar em entrada de usuário sem tratamento — a porta de entrada clássica pra SQL Injection. O que praticar: escrever a mesma consulta de duas formas — concatenando strings diretamente (vulnerável) e usando _prepared statements_/parâmetros (seguro) — e entender exatamente por que a primeira forma é perigosa.

### 5. Engenharia Web (1–2 semanas)

O que dominar: uma visão geral de performance web (tempo de carregamento, cache), acessibilidade (o site funciona com leitor de tela? com teclado apenas?), segurança básica (XSS — injetar script malicioso via entrada não sanitizada —, e CSRF — forjar uma requisição em nome de um usuário autenticado), e o processo de deploy (colocar a aplicação no ar). O que praticar: rodar uma ferramenta de auditoria automática (como o Lighthouse, já embutido no Chrome) num site real e interpretar os resultados de performance/acessibilidade.

## Conceitos que você precisa dominar

- **HTTP request/response** — todo o protocolo se resume a um cliente enviando uma requisição (método + URL + cabeçalhos + corpo opcional) e recebendo uma resposta (código de status + cabeçalhos + corpo); entender essa troca é entender 90% de como a Web funciona por baixo dos panos.
- **REST** — um estilo arquitetural (não um protocolo) em que recursos são identificados por URLs e manipulados com verbos HTTP semânticos (`GET` para ler, `POST` para criar, `PUT`/`PATCH` para atualizar, `DELETE` para remover) — a convenção mais comum pra desenhar APIs web hoje.
- **DOM (Document Object Model)** — a representação em árvore de uma página HTML que o JavaScript manipula; entender que "editar o DOM" não é a mesma coisa que "editar o HTML original" é o que evita confusão ao depurar páginas dinâmicas.
- **Sessão vs. Token (JWT)** — sessão exige que o servidor guarde estado (quem está logado); token (como JWT) carrega essa informação assinada dentro dele mesmo, permitindo autenticação sem estado no servidor — a troca clássica entre simplicidade de revogação (sessão) e escalabilidade sem estado (token).
- **SQL Injection** — a vulnerabilidade que surge quando entrada de usuário é concatenada diretamente numa consulta SQL, permitindo que o "usuário" injete comandos SQL arbitrários; a defesa padrão é sempre usar consultas parametrizadas.
- **XSS (Cross-Site Scripting) e CSRF** — XSS é injetar script malicioso que roda no navegador de outra pessoa (via entrada não sanitizada exibida na página); CSRF é forjar uma requisição que usa a sessão autenticada de uma vítima sem ela saber. Ambas exploram confiança mal colocada — em conteúdo (XSS) ou em origem da requisição (CSRF).

## Erros comuns de quem está começando

- **Misturar lógica de negócio com manipulação de DOM** — front-end sem nenhuma separação de responsabilidades vira, rapidamente, impossível de manter; mesmo sem framework, vale separar "o que calcula" de "o que atualiza a tela".
- **Validar só no front-end** — validação em JavaScript no navegador é conveniência de UX, não segurança; um atacante pode enviar requisições diretamente ao servidor, ignorando o front-end inteiro. Validação de verdade sempre acontece no back-end.
- **Não sanitizar entradas** — qualquer dado vindo do usuário (formulário, URL, cabeçalho) deve ser tratado como não confiável até prova em contrário; é a causa raiz de SQL Injection e XSS.
- **Confundir síncrono e assíncrono em JavaScript** — `fetch` e outras operações de rede são assíncronas por natureza (a resposta não chega instantaneamente); tratar código assíncrono como se fosse síncrono é a fonte mais comum de bugs de iniciante ("por que essa variável ainda está vazia?").
- **Guardar segredos (senhas, chaves de API) no código do front-end** — tudo que roda no navegador é visível a quem inspecionar o código-fonte; segredos sempre ficam no back-end.

## 📚 Materiais recomendados

### Livros e apostilas abertas

- **[Programação Web](/assets/biblioteca/computacao/programacao-web-etec.pdf)** (Escola Técnica Aberta/MEC) — cobre os fundamentos de programação para Web em português, boa base pra quem está começando.
- **[Aplicativos para Web II](/assets/biblioteca/computacao/aplicativos-web-2-etec.pdf)** (Rede e-Tec Brasil/MEC) — continuação prática, com foco em construção de aplicações completas.
- **[Web Design](/assets/biblioteca/computacao/web-design-utfpr.pdf)** (Rede e-Tec Brasil/UTFPR) — front-end e design de interfaces, com boas práticas de usabilidade.
- **[Projeto de Sistemas Web](/assets/biblioteca/computacao/projeto-sistemas-web-ifro.pdf)** (e-Tec Brasil/IFRO) — projeto e arquitetura de sistemas web de ponta a ponta.

### Referência e currículo completo (gratuitos)

- **[MDN Web Docs](https://developer.mozilla.org/pt-BR/)** — a referência definitiva de HTML, CSS e JavaScript, mantida pela Mozilla, com tradução em português.
- **[freeCodeCamp](https://www.freecodecamp.org/)** — currículo completo e gratuito, do zero absoluto até projetos full-stack, com certificados.

## 🔗 Referências externas

- [roadmap.sh/frontend](https://roadmap.sh/frontend) e [roadmap.sh/backend](https://roadmap.sh/backend) — mapas visuais atualizados do que compõe uma formação em front-end e back-end, úteis pra situar onde cada tecnologia (frameworks, bancos, ferramentas) se encaixa.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/eletivas/desenvolvimento-web|Desenvolvimento Web]] — a eletiva que cobre exatamente esta trilha: programação para Web, frameworks, acesso a banco de dados e engenharia Web.
- [[pt-br/resource/computacao/redes|Redes]] — a base de protocolos (TCP/IP, DNS) sobre a qual HTTP roda.
- [[pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados|Banco de Dados]] — o que sustenta a persistência de dados de qualquer aplicação web real.
