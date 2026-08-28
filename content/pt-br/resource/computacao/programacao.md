---
publish: false
title: Programação
created: 2026-07-18 13:04
modified: 2026-08-27 13:04
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] O que é este tópico
> Programação é a espinha dorsal prática do curso: da lógica de programação e primeiros algoritmos, passando por C e estruturas de dados, até orientação a objetos e paradigmas de linguagens. É a habilidade que atravessa seis disciplinas e praticamente todos os projetos que você vai fazer.

## Por que estudar isso?

Não existe atalho aqui: programação é a habilidade que o mercado testa na entrevista e que a faculdade testa em quase toda disciplina. Um exemplo concreto do que a trilha completa entrega: no início do curso, "ordenar uma lista" significa chamar `sort()` e torcer. Depois de estruturas de dados, você sabe que aquele `sort()` provavelmente é um algoritmo híbrido, que custa O(n log n), e que se seus dados já estão quase ordenados existe escolha melhor. Depois de POO, você sabe encapsular essa decisão atrás de uma interface pra poder trocá-la sem quebrar o resto do sistema. A mesma tarefa, três níveis de domínio.

E há um detalhe que iniciantes subestimam: programação é habilidade motora tanto quanto intelectual. Assim como ninguém aprende violão lendo partitura, ninguém aprende a programar assistindo videoaula. As disciplinas do curso dão a estrutura; as horas de teclado — resolvendo problema, quebrando a cabeça, lendo mensagem de erro — é que constroem a competência.

## Trilha de estudo

### 1. Lógica de programação e primeiros passos (1–2 meses)

O que dominar: variáveis, tipos, condicionais, laços, funções e leitura/escrita básica — em pseudocódigo e depois numa linguagem real (C ou Python). O que praticar: os problemas iniciantes do beecrowd, pelo menos 30–50 deles. A meta desta fase é uma só: destravar a tradução de "problema em português" pra "passos em código".

### 2. C, ponteiros e memória (3–4 meses)

O que dominar: a linguagem C de verdade — ponteiros, arrays, strings, structs, alocação dinâmica (`malloc`/`free`) e passagem por referência. O que praticar: implementar você mesmo funções que a biblioteca já dá (strlen, cópia de vetor, lista ligada). C dói exatamente onde ensina: é o único momento do curso em que você vê a memória de frente.

### 3. Estruturas de dados e recursão (4–6 meses)

O que dominar: listas ligadas, pilhas, filas, árvores binárias de busca, tabelas hash e os algoritmos clássicos de ordenação e busca — implementando cada um do zero pelo menos uma vez. O que praticar: exercícios do beecrowd de nível intermediário e trilhas do Exercism; use o VisuAlgo pra ver as estruturas se movendo antes de codificar.

### 4. Orientação a objetos e paradigmas (6+ meses, contínuo)

O que dominar: classes, encapsulamento, herança, polimorfismo e interfaces (em Java), e a consciência de que OO é um paradigma entre vários — funcional, procedural, lógico. O que praticar: projetos pequenos porém completos (um sistema de cadastro, um jogo simples), refatorando quando o design ranger. É aqui que você deixa de escrever programas e começa a projetar software.

## Conceitos que você precisa dominar

- **Variáveis e tipos** — Uma variável é um nome pra uma região de memória, e o tipo diz quantos bytes ela ocupa e como interpretá-los. Parece trivial até você entender por que `int` estoura em 2 bilhões e por que dividir dois inteiros em C descarta a parte decimal. Tipagem forte vs. fraca, estática vs. dinâmica: cada linguagem faz escolhas diferentes e elas mudam como você programa.
- **Controle de fluxo** — Condicionais e laços são o esqueleto de qualquer algoritmo. O salto de qualidade vem quando você para de "chutar até funcionar" e passa a raciocinar sobre invariantes: o que é verdade antes, durante e depois de cada iteração do laço. Esse hábito elimina a maioria dos bugs de limite (off-by-one).
- **Funções e escopo** — Dividir o programa em funções pequenas com responsabilidade única é a primeira forma de abstração que você aprende. Escopo determina onde cada nome é visível e quanto tempo vive — confundir variável local com global é fonte clássica de comportamento "fantasma".
- **Ponteiros e gerência de memória** — Um ponteiro guarda um endereço de memória, e em C você aloca e libera memória manualmente. É o conceito que mais reprova e o que mais ensina: depois de entender ponteiros, referências em Java e Python deixam de ser mágica e viram caso particular. Vazamento de memória e ponteiro solto (dangling) são os bugs que essa fase ensina a evitar.
- **Recursão** — Uma função que chama a si mesma, resolvendo o problema em termos de versões menores dele. Exige o "salto de fé": confiar que a chamada recursiva funciona (a indução matemática justifica isso formalmente). Sem recursão não há percurso de árvore, quicksort nem backtracking.
- **Estruturas de dados fundamentais** — Lista ligada, pilha, fila, árvore e tabela hash não são conteúdo de prova: são vocabulário de projeto. Cada uma faz um trade-off diferente entre custo de busca, inserção e remoção. Saber escolher a estrutura certa muda um programa de inutilizável pra instantâneo — e é a pergunta favorita de toda entrevista técnica.
- **Os quatro pilares de OO** — Encapsulamento (esconder estado interno), abstração (expor só o essencial), herança (reaproveitar e especializar) e polimorfismo (tratar objetos diferentes pela mesma interface). O erro comum é decorar as definições; o objetivo é reconhecer qual pilar resolve cada problema de design que aparece no seu código.
- **Paradigmas de programação** — Procedural, orientado a objetos, funcional e lógico são maneiras diferentes de organizar computação. Nenhum é "o melhor": cada um torna certos problemas fáceis e outros difíceis. Conhecer mais de um paradigma muda como você escreve código em qualquer linguagem — quem aprende funcional volta escrevendo laços mais limpos.

## Erros comuns de quem está começando

- **Assistir tutorial em vez de programar** — O "tutorial hell": a sensação de aprender assistindo, sem a habilidade se formar. A proporção saudável é no mínimo 3 horas de teclado pra cada hora de vídeo. Se você não travou em nada esta semana, você não praticou de verdade.
- **Copiar código sem digitar nem entender** — Colar solução do Stack Overflow (ou de IA) resolve a tarefa e adia o aprendizado. Regra prática de quem está aprendendo: digite o código você mesmo e só use uma solução externa depois de conseguir explicar linha por linha o que ela faz.
- **Fugir de ponteiros e de C** — "Vou direto pra Python porque C é difícil" é trocar dor agora por teto baixo depois. As disciplinas de estruturas de dados assumem que você entende memória; quem pulou essa etapa sente o dobro da dificuldade lá na frente.
- **Ignorar as mensagens de erro** — Iniciante vê erro e sai mudando código aleatoriamente. A mensagem de erro diz o tipo do problema e a linha; aprender a lê-la (e a ler o stack trace) é possivelmente a habilidade de maior retorno por hora investida em toda a programação.
- **Querer o projeto grande antes da base** — Começar "um app completo" na terceira semana termina em frustração e abandono. A progressão que funciona: exercícios curtos → programas de 100 linhas → projeto pequeno completo → projeto com outras pessoas.

## 📚 Materiais recomendados

### Livros e apostilas abertas

- **[Lógica de Programação](/assets/biblioteca/computacao/logica-de-programacao-etec.pdf)** e **[Técnicas de Programação](/assets/biblioteca/computacao/tecnicas-de-programacao-ifro.pdf)** (Rede e-Tec/MEC) — a dupla de apostilas do portal público [proedu.rnp.br](https://proedu.rnp.br) pra fase inicial: algoritmos, pseudocódigo e primeiras estruturas.
- **[Fundamentos de Lógica e Algoritmo](/assets/biblioteca/computacao/fundamentos-logica-algoritmo-etec.pdf)** (Escola Técnica Aberta) — alternativa/complemento pra etapa 1, também via [proedu.rnp.br](https://proedu.rnp.br).
- **[Linguagem C Descomplicada](/assets/biblioteca/computacao/linguagem-c-descomplicada-backes.pdf)** (Prof. André Backes, UFU) — apostila gratuita que virou referência nacional pra aprender C; didática forte em ponteiros e alocação dinâmica, exatamente onde os livros tradicionais são áridos.
- **[Apostila C++](/assets/biblioteca/computacao/apostila-cpp-unesp.pdf)** (Prof. Alan Panosso, UNESP) — material gratuito pra transição de C pra C++.
- **[Notas de Aula C++](/assets/biblioteca/computacao/notas-aula-cpp-ufpr.pdf)** (Prof. Armando Delgado, UFPR) — notas de curso abertas, boas como segunda referência de C++.
- **[Estrutura de Dados](/assets/biblioteca/computacao/estrutura-de-dados-etec.pdf)**, 2 volumes (Rede e-Tec) — cobre as estruturas fundamentais da etapa 3 em português acessível, via [proedu.rnp.br](https://proedu.rnp.br).
- **[Introdução à POO com Java](/assets/biblioteca/computacao/intro-poo-java-etec.pdf)** (Rede e-Tec) — apoio direto às disciplinas de orientação a objetos, via [proedu.rnp.br](https://proedu.rnp.br).

## 🔗 Referências externas

- [Roadmap: Python](https://roadmap.sh/python), [Roadmap: C++](https://roadmap.sh/cpp) e [Roadmap: Java](https://roadmap.sh/java) — mapas por linguagem; escolha o da linguagem da sua disciplina atual e use como checklist de tópicos.
- [beecrowd](https://www.beecrowd.com.br/) — juiz online brasileiro com milhares de problemas em português, dos triviais aos de maratona. É onde a etapa 1 e 3 desta trilha acontecem na prática; comece pelos problemas da categoria iniciante.
- [Exercism](https://exercism.org/) — trilhas de exercícios por linguagem com mentoria humana gratuita. Ótimo pra receber feedback sobre a qualidade do seu código, não só sobre se ele funciona.
- [Learn C++](https://www.learncpp.com/) — o tutorial de C++ mais completo e atualizado da web, gratuito. Use como livro-texto de C++ moderno.
- [cppreference](https://cppreference.com/) e [docs.python.org](https://docs.python.org/) e [dev.java](https://dev.java/) — as documentações oficiais. Aprender a consultá-las (em vez de só buscar blog) é marca de programador maduro.
- [VisuAlgo](https://visualgo.net/) — animações passo a passo de estruturas de dados e algoritmos de ordenação. Use antes de implementar cada estrutura: ver o movimento facilita muito o código.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/2-periodo/algoritmos-e-tecnicas-de-programacao|Algoritmos e Técnicas de Programação]] — etapas 1 e 2 da trilha.
- [[pt-br/resource/engenharia-de-computação/3-periodo/algoritmos-e-estruturas-de-dados-i|Algoritmos e Estruturas de Dados I]] — início da etapa 3: listas, pilhas, filas.
- [[pt-br/resource/engenharia-de-computação/4-periodo/algoritmos-e-estruturas-de-dados-ii|Algoritmos e Estruturas de Dados II]] — continuação da etapa 3: árvores, hash, ordenação.
- [[pt-br/resource/engenharia-de-computação/5-periodo/paradigmas-de-linguagem-de-programacao|Paradigmas de Linguagem de Programação]] — a visão comparada de paradigmas da etapa 4.
- [[pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i|Programação Orientada a Objetos I]] — os pilares de OO na prática, com Java.
- [[pt-br/resource/engenharia-de-computação/7-periodo/programacao-orientada-a-objetos-ii|Programação Orientada a Objetos II]] — aprofundamento: design, interfaces e projetos maiores.
