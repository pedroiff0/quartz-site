---
publish: true
titulo:  20260708 - ManualTCC
created: 2026-07-08
modified: 2026-08-27
tags:
cssclasses:

---

# MANUAL DE UTILIZAÇÃO — CLASSE `ifftese` (TCC do IFF)

  

> **Para quem é este manual:** você nunca mexeu com LaTeX e precisa escrever um

> Trabalho de Conclusão de Curso (TCC) usando a classe `ifftese` do Instituto

> Federal Fluminense (IFF). Aqui tudo é explicado de forma simples, comandos a

> comando, mostrando o que cada parâmetro faz e o efeito visual de cada opção.

>

> **Como ler os exemplos:** onde aparecer `{texto}` ou `[opção]`, isso é o que

> VOCÊ troca. Chaves `{ }` são obrigatórias; colchetes `[ ]` são opcionais.

  

---

  

## 0. O QUE É TUDO ISSO (o mínimo que você precisa saber)

  
	
LaTeX não é um editor de texto comum (tipo Word). Você escreve um **arquivo de

código** (o `.tex`) e um programa chamado **compilador** transforma esse código

em um PDF. A "classe" (`ifftese`) é o molde que define o visual e as regras do

documento (capa, margens, numeração, estilo ABNT).

  

Na pasta do seu TCC existem 4 arquivos que você precisa conhecer:

  

| Arquivo | O que é | Você mexe? |

|----------------|----------------------------------------------------|------------------------------|

| `ifftese.cls` | A classe (o "molde" do documento) | **NÃO** — é o motor |

| `metadados.sty` | Seus dados pessoais e da banca (pré-preenchido) | **SIM** — preenche os seus dados |

| `macros.sty` | Os "atalhos" (comandos prontos: figura, tabela...) | **NÃO** (só use os comandos) |

| `PedroH_TCC.tex` | O seu trabalho (texto + comandos) | **SIM** — é onde você escreve |

  

> **Termo em inglês que você vai ver:** *class* = classe; *package* (pacote) =

> arquivo de extensão `.sty` com comandos extras; *compile* (compilar) = gerar o PDF;

> *source* (fonte) = o arquivo `.tex` que você edita.

  

### Como compilar (gerar o PDF)

  

No terminal, dentro desta pasta:

  

```bash

pdflatex PedroH_TCC.tex

bibtex PedroH_TCC

pdflatex PedroH_TCC.tex

pdflatex PedroH_TCC.tex

```

  

A sequência `pdflatex → bibtex → pdflatex → pdflatex` é necessária porque a

bibliografia e os índices precisam de duas passadas para "assentar". Se aparecer

`LaTeX Warning: Citation ... undefined`, é só rodar o `pdflatex` mais uma vez.

  

---

  

## 1. A ESTRUTURA GERAL DO TRABALHO

  

Um TCC tem 3 grandes blocos. A classe já separa eles com 3 "faixas" de comando:

  

```

PRÉ-TEXTUAIS → \pretex (capa, folha de rosto, resumo, listas)

TEXTO → \transicaotex (introdução, desenvolvimento...)

PÓS-TEXTUAIS → \transicaopostex (referências, apêndices)

```

  

No seu arquivo principal (`PedroH_TCC.tex`) a ordem correta é:

  

```latex

\documentclass{ifftese} % 1. escolhe a classe

\usepackage{macros} % 2. carrega os atalhos

  

% ----- AQUI VOCÊ COLOCA SEUS METADADOS (Seção 2) -----

  

\begin{document} % 3. começa o documento

  

\pretex % 4. pré-textuais (capa, etc.)

\capa % capa

\contracapa % folha de rosto

\banca % folha de banca (se houver)

\dedicatoria{...} % dedicatória

\agradecimentos{...} % agradecimentos

\resumo{...}{...} % resumo (PT)

\abstractabnt{...}{...} % abstract (EN)

\imprimirListas % lista de figuras, tabelas, siglas...

  

\transicaotex % 5. entra no texto

  

% ===== CAPÍTULOS DO SEU TCC =====

\capitulo{Introdução} % (ou \chapter{...})

... seu texto ...

  

\capitulo{Desenvolvimento}

... seu texto ...

  

\capitulo{Conclusão}

... seu texto ...

  

\transicaopostex % 6. entra nos pós-textuais

  

\bibliographystyle{abntex2-alf}

\bibliography{bib/referencias} % arquivo .bib com as referências

  

\end{document}

```

  

> **Dica de leigo:** não apague `\pretex`, `\transicaotex` nem `\transicaopostex`.

> Eles aplicam as margens e a numeração certas em cada parte. Se você apagar, o

> PDF sai com margens erradas.

  

---

  

## 2. METADADOS — preenchendo os seus dados (`metadados.sty` + topo do `.tex`)

  

Tudo que aparece na **capa, folha de rosto e ficha** vem destes comandos. Eles

têm o formato `\comando{conteúdo}`. Se ficar vazio `{ }`, aquele campo some.

  

### 2.1 Seus dados pessoais e do orientador

  

| Comando | O que preencher | Exemplo |

|----------------------------|--------------------------------|------------------------------------------------|

| `\aluno{Nome Completo}` | Seu nome | `Pedro Henrique Rocha de Andrade` |

| `\abreviaturanome{Iniciais}` | Suas iniciais (para a lombada) | `P. H. R. de A.` |

| `\email{...}` | Seu e-mail | já vem preenchido |

| `\titulo{Título}` | Título do TCC | `Análise de Grandes Volumes de Dados Estelares` |

| `\subtitulo{Subtítulo}` | Subtítulo (vem após `:`) | `Cruzamento dos Catálogos GCNS e GALAH DR4` |

| `\tituloingles{Title}` | Título em inglês (se exigido) | `Analysis of Large Stellar Data Volumes` |

| `\subtituloingles{Subtitle}` | Subtítulo em inglês | `Cross-matching the GCNS and GALAH DR4 Catalogs` |

| `\shortitulo{Abrev.}` | Título curto (cabeçalho) | `Análise de Dados Estelares` |

| `\palavraschave{p1; p2}` | Palavras-chave PT | `Catálogos Estelares; Astronomia` |

| `\keywords{k1; k2}` | Keywords EN | `Stellar Catalogs; Astronomy` |

  

**Efeito visual:** o `\titulo` e `\subtitulo` aparecem na capa em caixa-alta

(LETRAS GRANDES) como `TÍTULO: Subtítulo.`. O `\shortitulo` aparece no topo das

páginas internas (cabeçalho). As `\palavraschave`/`\keywords` são impressas

automaticamente no Resumo/Abstract.

  

### 2.2 Orientador, coorientador e banca

  

| Comando | Função | Exemplo |

|--------------------------------------|-----------------------------|----------------------------------------------|

| `\orientador{Prof.}` | Nome do orientador | `Dra. Ana Cecília Soja` |

| `\abreviaturaorientador{Tít.}` | Titulação curta | `Dra.` (ou deixe vazio) |

| `\siglainstituicaoorientador{Sigla}` | Instituição dele | `IFF` |

| `\coorientador{Prof.}` | Coorientador (opcional) | `Dra. Luiza Linhares Dantas` |

| `\siglainstituicaocoorientador{Sigla}` | Instituição do coorientador | `PUC-Chile` |

| `\coorientadorsegundo{...}` | 2º coorientador (raro) | deixe vazio |

| `\membrobancaum{Prof.}` | 1º membro da banca | `Dr. Fabrício Barros Gonçalves` |

| `\siglainstituicaomembroum{Sigla}` | Instituição do 1º membro | `IFF` |

| `\membrobancadois{Prof.}` | 2º membro da banca | `Me. Ana Mara Figueiredo` |

| `\siglainstituicaomembrodois{Sigla}` | Instituição do 2º membro | `IFF` |

| `\dataaprovacao{\today}` | Data da defesa | `\today` (data de hoje) ou `10 de julho de 2026` |

  

**Variação 1 — sem coorientador:** simplesmente deixe `\coorientador{}` vazio.

A folha de rosto some com a linha do coorientador sozinha.

  

**Variação 2 — banca com 3 membros:** a classe só traz `membrobancaum` e

`membrobancadois` prontos. Se precisar de um 3º, avise quem mantém a classe

(ou copie o padrão no `metadados.sty`).

  

**Efeito visual:** orientador e coorientador aparecem na **folha de rosto**

(`\contracapa`) como `Orientadora: Dra., Ana Cecília Soja.` e na **folha de

banca** (`\banca`).

  

### 2.3 Dados da instituição e do curso

  

| Comando | O que é | Padrão (já preenchido) |

|---------------------------|----------------------|----------------------------------------------------------------|

| `\instituicao{...}` | Nome completo do IFF | `Instituto Federal de Ciência, Tecnologia e Educação Fluminense` |

| `\shortinstituicao{...}` | Nome curto | `Instituto Federal Fluminense` |

| `\siglainstituicao{...}` | Sigla | `IFF` |

| `\curso{...}` | Seu curso | `Bacharelado em Engenharia de Computação` |

| `\areaconcentracao{...}` | Área de concentração | `Engenharia de Computação` |

| `\disciplinaFormatada{...}` | Nome da disciplina | `Trabalho de Conclusão de Curso` |

| `\ano{...}` | Ano | `2026` |

| `\local{...}` | Cidade | `Bom Jesus do Itabapoana` |

| `\estado{...}` | UF | `RJ` |

| `\estadocompleto{...}` | Estado por extenso | `Rio de Janeiro` |

| `\campus{...}` | Campus | já vem como `\textit{Campus} \tcc@local` |

  

> **Atenção:** `\campus` usa `\tcc@local` (a cidade). Não mude a fórmula; só mude

> `\local` que o campus acompanha.

  

### 2.4 "Interruptores" (flags) — liga/desliga comportamentos

  

Estes comandos não recebem texto, recebem `sim` (ligado) ou ficam vazios

(desligado). Estão no `metadados.sty`:

  

| Comando | Se `sim` (ligado) faz... | Se vazio (desligado) |

|-------------------------|------------------------------------------------------|---------------------------------------------------------------|

| `\tipo{tcc}` | Define o tipo de doc. Use `tcc` | `relatorio`, `relatoriotecnico`, `relatoriocientifico` mudam a capa |

| `\figuracaminho{img}` | Pasta onde estão as imagens | se vazio, figuras não carregam |

| `\numeracaoPorSecao{sim}` | Numera Teorema 1.1, 2.1... por capítulo | numeroção contínua (1,2,3...) |

| `\cabecalho{sim}` | Mostra cabeçalho (título) nas páginas | sem cabeçalho |

| `\corlink{sim}` | Links em azul/vermelho | links pretos |

| `\legendacurta{sim}` | Índice usa a legenda CURTA (curta) | índice repete a legenda longa |

| `\sumarioescada{sim}` | Sumário "em escada" (subseções recuadas) | sumário simples |

| `\frenteVerso{sim}` | Impressão frente-e-verso (capítulos em página ímpar) | só frente |

| `\capaiff{sim}` | Capa com a imagem `img/image.png` de fundo | capa só texto |

| `\numero{1}` | Número do relatório (se for relatório) | `1` |

  

**Exemplo de modificação e seu efeito:**

  

```latex

% ANTES (padrão do TCC): capa só com texto

\capaiff{}

  

% DEPOIS: capa com a imagem de fundo do IFF

\capaiff{sim}

```

  

> Efeito: a capa ganha a imagem `img/image.png` como plano de fundo.

  

```latex

% ANTES: Teoremas numerados 1, 2, 3 (contínuo)

\numeracaoPorSecao{}

  

% DEPOIS: Teoremas numerados por capítulo (1.1, 1.2, 2.1)

\numeracaoPorSecao{sim}

```

  

---

  

## 3. MACROS DE INSERÇÃO — figuras, tabelas, quadros, gráficos

  

Estas macros são "caixas prontas": você passa os dados e elas montam a legenda,

a fonte e o rótulo (label) automaticamente, no padrão ABNT.

  

> **Termos em inglês:** *figure* = figura; *table* = tabela; *frame/box* = quadro;

> *chart/graph* = gráfico; *caption* = legenda; *label* = rótulo (usado para

> referenciar com `\autoref{...}`); *source* = fonte.

  

### 3.1 FIGURA — `\inserirfigura`

  

```latex

\inserirfigura[width=0.8\textwidth]{arquivo.png}{Legenda longa.}{Legenda curta}{Fonte: Autor}{fig:minhafig}

```

  

| \# | Parâmetro | O que é | Exemplo |

|-----|--------------------|-----------------------------------------------|--------------------------------------|

| `[1]` | opções (colchetes) | opções do `\includegraphics` | `width=0.8\textwidth` (80% da largura) |

| `2` | arquivo | Nome do arquivo **dentro de** `img/` (sem caminho) | `grafico.pdf` |

| `3` | legenda longa | Texto que aparece embaixo da figura | `Distribuição das estrelas.` |

| `4` | legenda curta | Texto do ÍNDICE (se `\legendacurta{sim}`) | `Distribuição.` |

| `5` | fonte | Texto da fonte (ABNT exige) | `Fonte: O autor.` |

| `6` | label | Nome para referenciar: `\autoref{fig:minhafig}` | `fig:minhafig` |

  

**Variação A — figura menor (50% da página):**

  

```latex

\inserirfigura[width=0.5\textwidth]{arquivo.png}{Legenda longa.}{Leg.}{Fonte: X}{fig:a}

```

  

**Variação B — sem legenda curta (use se** `\legendacurta{}` **estiver desligado):**

  

```latex

\inserirfigura[width=0.8\textwidth]{arquivo.png}{Mesma legenda.}{}{Fonte: X}{fig:b}

```

  

> Efeito: o 4º parâmetro vazio faz o índice repetir a legenda longa.

  

**Como referenciar depois no texto:**

  

```latex

Como visto na \autoref{fig:minhafig}, a distribuição é assimétrica.

```

  

> `\autoref` escreve "Figura 1" automaticamente (com link, se `\corlink{sim}`).

  

### 3.2 TABELA — `\inserirtabela` e `\inserirtabelaL`

  

```latex

\inserirtabela

{Legenda longa da tabela.}{Leg. tab.}

{tab:resultados}

{\begin{tabular}{l|c}

Coluna A & Coluna B \\

\hline

Valor 1 & 10 \\

Valor 2 & 20 \\

\end{tabular}}

{Fonte: O autor.}

```

  

| \# | Parâmetro | O que é |

|---|---------------|----------------------------------------------------------|

| `1` | legenda longa | legenda da tabela |

| `2` | legenda curta | legenda do índice |

| `3` | label | `tab:resultados` (referencie com `\autoref{tab:resultados}`) |

| `4` | conteúdo | O ambiente `\begin{tabular}...\end{tabular}` com os dados |

| `5` | fonte | fonte ABNT |

  

**Diferença** `\inserirtabela` **×** `\inserirtabelaL`**:**

  

- `\inserirtabela`: a tabela fica no tamanho natural (não estica).

- `\inserirtabelaL`: a tabela é **esticada** para ocupar 100% da largura do texto (`\textwidth`). Use quando a tabela for estreita e você quiser preencher a linha.

  

```latex

% Tabela esticada (L = large/large width)

\inserirtabelaL

{Legenda.}{Leg.}

{tab:largura}

{\begin{tabular}{l|c|c}

A & B & C \\ \hline

1 & 2 & 3 \\

\end{tabular}}

{Fonte: O autor.}

```

  

### 3.3 QUADRO — `\inserirquadro`

  

Igual à tabela, mas usa o ambiente `quadro` (no ABNT, quadro é para texto

não-numérico, tabela é para dados numéricos).

  

```latex

\inserirquadro

{Etapas do método.}{Etapas}

{qua:metodo}

{\begin{tabular}{l|p{8cm}}

Etapa & Descrição \\

\hline

1 & Coleta dos dados. \\

2 & Cruzamento dos catálogos. \\

\end{tabular}}

{Fonte: O autor.}

```

  

> Efeito: entra na "Lista de Quadros" (separada da de tabelas) quando você usar

> `\imprimirListas`.

  

### 3.4 GRÁFICO — `\inserirgrafico`

  

```latex

\inserirgrafico[width=0.9\textwidth]{grafico.pdf}{Legenda do gráfico.}{Leg. gráf.}{Fonte: X}{gra:curva}

```

  

Mesmos parâmetros da figura. A diferença é que entra na **Lista de Gráficos**

(que `\imprimirListas` imprime).

  

### 3.5 SUBFIGURAS (várias imagens numa só figura)

  

Úteis para mostrar (a) e (b) lado a lado.

  

**Duas subfiguras:**

  

```latex

\inserirDuasSubfiguras

{\includegraphics[width=0.45\textwidth]{img/a.png}}

{\includegraphics[width=0.45\textwidth]{img/b.png}}

{Legenda geral.}{Leg. geral}

{Fonte: X}

{fig:par}

{0.48\textwidth} % 7º: largura de cada subfigura

```

  

**Variação — três subfiguras:**

  

```latex

\inserirTresSubfigurasL

{\includegraphics[width=0.3\textwidth]{a.png}}

{\includegraphics[width=0.3\textwidth]{b.png}}

{\includegraphics[width=0.3\textwidth]{c.png}}

{Legenda.}{Leg.}

{Fonte: X}

{fig:tres}

{0.32\textwidth} % 8º: largura de cada uma

```

  

> **Dica:** o último número (largura de cada subfigura) deve ser menor que

> `0.5\textwidth` para caberem 2, e menor que `0.34\textwidth` para 3.

  

---

  

## 4. MACROS DE TEXTO — resumo, citações, destaques, notas

  

### 4.1 RESUMO e ABSTRACT

  

```latex

\resumo{%

Neste trabalho analisamos a vizinhança solar por meio do cruzamento

dos catálogos GCNS e GALAH DR4. Os resultados indicam...

}{Catálogos Estelares; Astronomia; Cruzamento de Dados}

```

  

| \# | Parâmetro | O que é |

|---|----------------|----------------------------------------------------|

| `1` | texto | O texto do resumo (1 parágrafo, ~150–250 palavras) |

| `2` | palavras-chave | Separadas por ponto-e-vírgula |

  

```latex

\abstractabnt{%

In this work we analyze the solar vicinity by cross-matching the

GCNS and GALAH DR4 catalogs. Results indicate...

}{Stellar Catalogs; Astronomy; Data Cross-matching}

```

  

> **Efeito:** `\resumo` cria a página "Resumo" em PT e salva as palavras-chave;

> `\abstractabnt` cria "Abstract" em EN. As palavras-chave aparecem sozinhas no

> rodapé de cada página.

  

### 4.2 CITAÇÃO LONGA (mais de 3 linhas)

  

No ABNT, citação com mais de 3 linhas é "citacao longa" (recuo de 4 cm):

  

```latex

\begin{citacaolonga}

É sabido que a caracterização das populações estelares constitui uma

ferramenta de alta resolução para investigar a formação da Via Láctea

(Autor, 2020, p. 45).

\end{citacaolonga}

```

  

> **Efeito:** o texto ganha recuo à esquerda de 4 cm e fonte menor — padrão ABNT.

  

### 4.3 DESTAQUE de número com unidade — `\destaque` e `\destaqueC`

  

```latex

\destaque{5}{km/s} % caixa pequena ao lado do texto: 5 km/s

\destaqueC{9.8}{m/s^2} % caixa CENTRALIZADA (bloco isolado): 9,8 m/s²

```

  

| \# | Parâmetro | O que é |

|---|-----------|---------------------------------|

| `1` | valor | número (use ponto para decimal) |

| `2` | unidade | unidade (no padrão SI) |

  

> **Efeito:** cria uma caixinha destacada com o valor. `\destaque` fica no meio

> da linha; `\destaqueC` fica centralizado no meio da página.

  

### 4.4 NOTA DE RODAPÉ — `\notarodape`

  

```latex

O GCNS reúne cerca de 330 mil estrelas.\notarodape{Valor obtido de Smart et al. (2021).}

```

  

> **Efeito:** cria a numeração¹ no texto e a nota no rodapé automaticamente.

  

### 4.5 COMENTÁRIO de rascunho — `\comentario`

  

```latex

Aqui vai o parágrafo.\comentario{Verificar esse número com o orientador!}

```

  

> **Efeito:** escreve um texto verde teal `[SeuNome: Verificar esse número...]`

> no PDF. É para você mesmo não esquecer de revisar. Apague antes de entregar.

  

---

  

## 5. ELEMENTOS PRÉ-TEXTUAIS (capa, rosto, banca, etc.)

  

Estes comandos só precisam ser chamados (não recebem parâmetro, salvo indicado):

  

| Comando | O que gera | Precisa configurar antes? |

|------------------------|-----------------------------------------------|---------------------------------|

| `\capa` | Capa (instituição, aluno, título, cidade/ano) | metadados §2.1–2.3 |

| `\contracapa` | Folha de rosto (natureza + orientador) | `\orientador`, `\titulo` |

| `\banca` | Folha de aprovação da banca | membros da banca §2.2 |

| `\dedicatoria{texto}` | Dedicatória | texto entre chaves |

| `\agradecimentos{texto}` | Agradecimentos | texto entre chaves |

| `\fichacatalografica` | Ficha catalográfica (CIP) | dados da ficha no `metadados.sty` |

| `\errata{linhas}` | Errata (se houver erro na impressão) | tabela de correções |

| `\identificacao` | Identificação (para relatório técnico) | relatórios only |

  

**Exemplo de uso (no corpo do** `\pretex`**):**

  

```latex

\capa

\contracapa

\banca

\dedicatoria{\textit{Dedico este trabalho ao meu avô José Carlos.}}

\agradecimentos{Primeiramente a Deus...}

\resumo{...}{...}

\abstractabnt{...}{...}

\imprimirListas

```

  

**Variação — capa com imagem de fundo:**

Já vista em §2.4: basta `\capaiff{sim}` nos metadados (precisa de `img/image.png`).

  

---

  

## 6. AMBIENTES (teoremas, exemplos, definições...)

  

A classe traz ambientes prontos para textos matemáticos/pedagógicos. Se

`\numeracaoPorSecao{sim}` estiver ligado, eles são numerados por capítulo.

  

| Ambiente | Nome visual | Uso |

|----------------------------|-------------|-----------------------|

| `\begin{teorema}{Título}` | **Teorema** | Afirmação demonstrada |

| `\begin{exemplo}{Título}` | **Exemplo** | Exemplo ilustrativo |

| `\begin{observacao}{Título}` | **Observação** | Nota importante |

| `\begin{definicao}{Título}` | **Definição** | Definição de termo |

| `\begin{lema}{Título}` | **Lema** | Resultado auxiliar |

| `\begin{corolario}{Título}` | **Corolário** | Consequência |

| `\begin{proposicao}{Título}` | **Proposição** | Afirmação |

| `\begin{axioma}{Título}` | **Axioma** | Verdade assumida |

| `\begin{conjectura}{Título}` | **Conjectura** | Suposição |

| `\begin{resolucao}{Título}` | **Resolução** | Passo a passo |

  

```latex

\begin{teorema}{Central do Limite}

Seja $X_1,...,X_n$ uma amostra aleatória... então a média converge a uma

normal.

\end{teorema}

```

  

> **Efeito:** cria uma caixa estilizada com título colorido e numeração (ex.:

> "Teorema 2.1").

  

---

  

## 7. SIGLAS, SÍMBOLOS E GLOSSÁRIO

  

### 7.1 Siglas (Lista de Abreviaturas)

  

```latex

\addtoSiglas{GCNS}{Gaia Catalogue of Nearby Stars}{Catálogo de Estrelas Próximas do Gaia}

```

  

| \# | Parâmetro | O que é |

|---|---------------------|-----------------------------------------|

| `1` | sigla | a abreviatura (ex.: GCNS) |

| `2` | descrição | o nome por extenso |

| `3` | descrição estendida | versão mais completa (aparece na lista) |

  

> **Efeito:** após `\imprimirListas`, cria a "Lista de Abreviaturas" automaticamente

> ordenada. Coloque os `\addtoSiglas` no pré-texto ou junto ao primeiro uso.

  

### 7.2 Símbolos (Lista de Símbolos)

  

```latex

\addtoSimbolos{$\sigma$}{Desvio padrão}{}

```

  

Mesmos 3 parâmetros (o 3º pode ficar vazio `{}`).

  

### 7.3 Glossário

  

```latex

\addtoGlossario{Cross-matching}{Cruzamento de dois catálogos por identificador comum.}

```

  

Use `\imprimirglossario` (ou `\imprimirListas`) para imprimir.

  

---

  

## 8. GLOSSÁRIO DE TERMOS (PT ⇄ EN) para quem não domina o inglês

  

| Inglês | Português | Onde aparece no manual |

|-----------------------------|---------------------------------------|------------------------|

| class (`.cls`) | classe (o molde do documento) | §0 |

| package (`.sty`) | pacote (arquivo de comandos) | §0 |

| compile / build | compilar (gerar o PDF) | §0 |

| source (`.tex`) | arquivo de código-fonte | §0 |

| preamble | preâmbulo (antes de `\begin{document}`) | §1 |

| metadata | metadados (seus dados) | §2 |

| figure | figura | §3.1 |

| table | tabela | §3.2 |

| frame / box | quadro | §3.3 |

| chart / graph | gráfico | §3.4 |

| caption | legenda | §3.1 |

| label | rótulo (para `\autoref`) | §3.1 |

| cross-reference | referenciar (com `\autoref`) | §3.1 |

| source (of figure) | fonte (da imagem) | §3.1 |

| abstract | resumo em inglês | §4.1 |

| footnote | nota de rodapé | §4.4 |

| theorem / lemma / corollary | teorema / lema / corolário | §6 |

| acronym / abbreviation | sigla / abreviatura | §7.1 |

| symbol | símbolo | §7.2 |

| glossary | glossário | §7.3 |

| bibliography / references | referências bibliográficas | §1 |

| front matter | pré-textuais | §1 |

| main matter / body | texto (corpo) | §1 |

| back matter | pós-textuais | §1 |

  

---

  

## 9. EXEMPLO MÍNIMO DE TCC (copie e adapte)

  

```latex

\documentclass{ifftese}

\usepackage{macros}

  

% ---- METADADOS ----

\aluno{Seu Nome Completo}

\titulo{Meu Título de TCC}

\subtitulo{Meu Subtítulo}

\orientador{Prof. Orientador}

\abreviaturaorientador{Dr.}

\siglainstituicaoorientador{IFF}

\membrobancaum{Prof. Banca 1}

\siglainstituicaomembroum{IFF}

\membrobancadois{Prof. Banca 2}

\siglainstituicaomembrodois{IFF}

\dataaprovacao{\today}

  

\begin{document}

\pretex

\capa

\contracapa

\banca

\resumo{Resumo do trabalho em um parágrafo.}{Palavra1; Palavra2}

\abstractabnt{Abstract in English.}{Keyword1; Keyword2}

\imprimirListas

  

\transicaotex

  

\capitulo{Introdução}

Este trabalho aborda...\autoref{fig:exemplo}.

  

\capitulo{Desenvolvimento}

\inserirfigura[width=0.7\textwidth]{exemplo.png}{Legenda.}{Leg.}{Fonte: Autor}{fig:exemplo}

  

\capitulo{Conclusão}

Conclui-se que...

  

\transicaopostex

\bibliographystyle{abntex2-alf}

\bibliography{bib/referencias}

\end{document}

```

  

---

  

## 10. RESUMO DOS PRIMEIROS PASSOS (checklist)

  

1. Edite `metadados.sty`: nome, título, orientador, banca, ano, curso.

2. No `PedroH_TCC.tex`, troque o conteúdo de `\aluno`, `\titulo`, etc. no topo.

3. Escreva os capítulos com `\capitulo{Nome}` entre `\transicaotex` e `\transicaopostex`.

4. Insira figuras/tabelas com as macros da Seção 3.

5. Compile: `pdflatex → bibtex → pdflatex → pdflatex`.

6. Antes de entregar: apague todos os `\comentario{...}`.

  

> **Termo final:** *debug* (depurar) = quando o LaTeX dá erro, leia a mensagem

> amarela/vermelha no terminal; o erro quase sempre está NA LINHA ANTERIOR à

> indicada. Se travar, comente metade do texto (`%`) para isolar o problema.

  

---

  

## 11. AVISOS ESPERADOS (não são erros de verdade)

  

Ao rodar o **primeiro** `pdflatex`, pode aparecer no terminal:

  

```

! LaTeX Error: Command \su@ExpandTwoArgs already defined.

! LaTeX Error: Command \IfSubStringInString already defined.

```

  

**Isso é inofensivo.** A classe carrega o pacote `xstring` (usado pelas macros

como `\IfStrEq`) e, mais à frente, o pacote `datatool` (usado nas listas de

siglas) carrega o `substr`, que define comandos de mesmo nome. O `xstring`

prevalece e tudo funciona. **Importante:** rode a sequência completa

(`pdflatex → bibtex → pdflatex → pdflatex`) e o PDF final sai correto, mesmo

que esse aviso apareça na primeira passada.

  

> Se quiser eliminar o aviso de forma definitiva, peça a quem mantém a classe

> para trocar o `substr` por `xstring` internamente — mas não é necessário para

> o TCC compilar.

  

---

  

## 12. NOTAS DE MANUTENÇÃO DESTA CLASSE (para quem edita os `.sty`)

  

- **Bug corrigido em** `\inserirfigura` **/** `\inserirgrafico` **/** `\inserirelementografico`**:** o caminho era montado como `\figuracaminho/ #2` (com espaço após a barra), o que fazia a figura sumir (caixa vazia). Foi corrigido para `\figuracaminho/#2` (sem espaço). Se uma figura não aparecer, confira se o arquivo está em `img/` e se o nome bate exatamente (incluindo maiúsculas).

- **Sempre que mexer em** `macros.sty` **ou** `ifftese.cls`**,** recompile o documento inteiro (4 passadas) e confira se as figuras/tabelas ainda entram.
