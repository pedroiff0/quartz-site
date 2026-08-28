---
publish: false
title: Projeto e Análise de Algoritmos
created: 2026-07-18 13:04
modified: 2026-08-27 13:04
published: 2026-07-26T11:33:09.975-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] O que é este tópico
> Projeto e Análise de Algoritmos é a disciplina que transforma programação em engenharia: medir formalmente o custo de um algoritmo (notação assintótica) e dominar as técnicas clássicas de projeto — divisão e conquista, programação dinâmica, algoritmos gulosos. É onde "funciona" deixa de ser suficiente e "funciona em quanto tempo?" vira a pergunta central.

## Por que estudar isso?

Um exemplo que acontece em produção o tempo todo: um sistema testado com 100 registros roda instantâneo; em produção, com 1 milhão, trava. O culpado costuma ser um algoritmo O(n²) escondido — um laço dentro de outro comparando tudo com tudo. Com 100 itens são 10 mil operações (imperceptível); com 1 milhão são 1 trilhão (horas). Nenhum hardware salva: a diferença entre O(n²) e O(n log n) em escala grande não é otimização, é viabilidade.

Análise de algoritmos dá o instrumento pra prever isso **antes** de escrever o código — no papel, em minutos. E a parte de projeto dá o repertório pra fazer melhor: reconhecer que um problema tem subestrutura ótima e cai em programação dinâmica, ou que uma escolha gulosa basta, é o tipo de olhar que separa quem resolve problemas novos de quem só reaplica receitas. Não por acaso, é o conteúdo central das entrevistas técnicas das grandes empresas.

## Trilha de estudo

### 1. Análise assintótica (3–4 semanas)

O que dominar: notações O, Ω e Θ, análise de pior/melhor/caso médio, e o custo dos algoritmos que você já conhece (buscas, ordenações, operações em estruturas de dados). O que praticar: pegar código seu antigo e calcular a complexidade de cada função; comparar com medições reais de tempo pra ganhar intuição de quanto n log n e n² divergem na prática.

### 2. Divisão e conquista (3–4 semanas)

O que dominar: o padrão dividir-resolver-combinar (mergesort, quicksort, busca binária), recorrências e o Teorema Mestre pra resolvê-las. O que praticar: implementar mergesort e quicksort do zero, escrever a recorrência de cada um e resolvê-la à mão. A recorrência é a ligação entre o código recursivo e sua complexidade.

### 3. Programação dinâmica e algoritmos gulosos (5–8 semanas)

O que dominar: identificar subproblemas sobrepostos e subestrutura ótima, memoização vs. tabulação, e os problemas canônicos (mochila, subsequência comum mais longa, troco, escalonamento de intervalos). Saber quando guloso funciona — e provar quando não funciona. O que praticar: resolver os clássicos sem olhar solução; PD só entra na cabeça pelo sofrimento produtivo de montar a tabela sozinho.

### 4. Grafos e limites da computação (4–6 semanas)

O que dominar: BFS, DFS, Dijkstra, árvore geradora mínima, ordenação topológica; e uma noção honesta de NP-completude — o que significa um problema não ter (até onde se sabe) solução eficiente, e o que fazer nesses casos (heurísticas, aproximações). O que praticar: modelar problemas do mundo real como grafos e escolher o algoritmo certo; é a habilidade mais transferível de toda a disciplina.

## Conceitos que você precisa dominar

- **Notação Big-O (e Ω, Θ)** — Descreve como o custo cresce com o tamanho da entrada, ignorando constantes e termos menores. O(n²) significa "quadruplicar a entrada multiplica o tempo por ~16". É a linguagem universal pra comparar algoritmos sem depender de máquina, linguagem ou compilador — e o vocabulário mínimo de qualquer entrevista técnica.
- **Análise de pior caso vs. caso médio** — O mesmo algoritmo pode ter comportamentos radicalmente diferentes: quicksort é O(n log n) em média e O(n²) no pior caso (entrada já ordenada com pivô ingênuo). Saber qual análise importa em cada contexto — sistema de tempo real exige garantia de pior caso; um script pontual, não — é decisão de engenharia.
- **Recorrências e o Teorema Mestre** — Algoritmos recursivos têm custo descrito por recorrências como T(n) = 2T(n/2) + n. O Teorema Mestre resolve as mais comuns por classificação direta. Sem isso, a complexidade de qualquer divisão e conquista vira chute.
- **Divisão e conquista** — Quebrar o problema em subproblemas independentes, resolver recursivamente e combinar. O padrão por trás de mergesort, busca binária e multiplicação rápida. A palavra-chave é _independentes_: quando os subproblemas se repetem, a técnica certa muda pra programação dinâmica.
- **Programação dinâmica** — Aplicável quando o problema tem subproblemas sobrepostos e subestrutura ótima: resolve-se cada subproblema uma vez e guarda-se o resultado (memoização ou tabela). Transforma soluções exponenciais em polinomiais — Fibonacci recursivo ingênuo é O(2ⁿ); com memoização, O(n). É a técnica de maior salto de desempenho do repertório.
- **Algoritmos gulosos** — Fazer a escolha localmente ótima em cada passo e nunca voltar atrás. Quando funciona (troco com moedas canônicas, escalonamento de intervalos, Dijkstra), é simples e rápido; quando não funciona, falha silenciosamente dando resposta errada. Por isso o par obrigatório: algoritmo guloso + argumento de correção.
- **Algoritmos em grafos** — BFS encontra caminhos mínimos em arestas não ponderadas; DFS revela estrutura (ciclos, componentes, ordem topológica); Dijkstra generaliza pra pesos. Uma fração enorme dos problemas reais — rotas, dependências, redes, recomendação — é grafo disfarçado, e reconhecer isso é metade da solução.
- **P, NP e NP-completude** — A fronteira entre problemas com solução eficiente conhecida e problemas (como o caixeiro-viajante) em que só sabemos verificar soluções rapidamente, não encontrá-las. Reconhecer um problema NP-completo evita semanas perdidas buscando o algoritmo exato perfeito — a resposta profissional é heurística, aproximação ou reformulação.

## Erros comuns de quem está começando

- **Confundir Big-O com tempo de execução** — O(1) não significa "rápido", significa "custo constante" — e a constante pode ser enorme. Pra n pequeno, um O(n²) simples vence um O(n log n) cheio de overhead. Big-O descreve crescimento, não velocidade absoluta; as duas informações se complementam.
- **Decorar complexidades sem saber derivá-las** — Saber que "quicksort é n log n" sem conseguir explicar por quê não sobrevive à primeira variação do problema. Aprenda a contar operações e resolver recorrências; a tabela de complexidades vira consequência, não decoreba.
- **Aplicar guloso sem provar que funciona** — O guloso é sedutor porque é fácil de implementar, e por isso é a armadilha clássica: em muitos problemas ele dá resposta errada de forma convincente. Antes de usar, exija de si mesmo um argumento de por que a escolha local não estraga o ótimo global — ou um contraexemplo.
- **Pular a formulação na programação dinâmica** — Tentar escrever o código da PD antes de definir no papel o que é o estado, qual a recorrência e quais os casos base. PD se resolve primeiro em português e matemática, depois em código; invertido, vira tentativa e erro interminável.
- **Otimizar sem medir e sem analisar** — Gastar horas otimizando micro-detalhes de uma função que contribui 1% do tempo total, enquanto o gargalo assintótico fica intocado. A ordem certa: analisar a complexidade, medir onde o tempo vai de fato, e só então otimizar — o algoritmo antes da constante.

## 📚 Materiais recomendados

### Livros e apostilas abertas

- **[Estrutura de Dados](/assets/biblioteca/computacao/estrutura-de-dados-etec.pdf)** (Rede e-Tec, 2 volumes) — a base necessária antes desta trilha: as estruturas sobre as quais os algoritmos operam. Disponível no portal público [proedu.rnp.br](https://proedu.rnp.br).

### Bibliografia clássica (consultar na biblioteca)

- CORMEN, T. H. et al. _Algoritmos: Teoria e Prática_ (CLRS). — **A** referência da área, adotada no mundo inteiro. Denso, mas é o livro que cobre desta trilha inteira com rigor: análise, recorrências, PD, gulosos, grafos e NP-completude. Use como consulta por capítulo, não como leitura linear.

## 🔗 Referências externas

- [Roadmap: Data Structures & Algorithms](https://roadmap.sh/datastructures-and-algorithms) — checklist completo do que dominar em estruturas e algoritmos, na ordem certa de dependência.
- [VisuAlgo](https://visualgo.net/) — animações passo a passo de ordenações, árvores, grafos e até recursão. Ver o mergesort dividir e mesclar visualmente vale por páginas de explicação; use antes de cada implementação.
- [beecrowd](https://www.beecrowd.com.br/) — pratique nas categorias de paradigmas: há seções específicas de programação dinâmica, grafos e guloso, com problemas em português e correção automática.
- [MIT OpenCourseWare — Introduction to Algorithms](https://ocw.mit.edu/) — o curso 6.006 do MIT, com aulas gravadas e listas: acompanha o CLRS e é o melhor complemento gratuito à disciplina.
- [Exercism](https://exercism.org/) — bom pra treinar a implementação limpa dos algoritmos clássicos em várias linguagens, com feedback de mentores.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/5-periodo/projeto-e-analise-de-algoritmos|Projeto e Análise de Algoritmos]] — a disciplina do 5º período que cobre exatamente esta trilha; chegue nela com as estruturas de dados frescas na cabeça.
