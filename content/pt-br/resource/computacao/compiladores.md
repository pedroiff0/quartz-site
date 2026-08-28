---
publish: false
title: Compiladores
created: 2026-07-26 13:04
modified: 2026-08-27 21:54
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] O que é este tópico
> Compiladores é a disciplina que abre a "caixa preta" entre o código que você escreve e as instruções que a máquina realmente executa. É onde Linguagens Formais e Autômatos deixa de ser teoria abstrata e vira a engenharia concreta de um programa que lê texto (código-fonte) e produz outro programa (código de máquina, bytecode, ou código intermediário) — passando por análise léxica, sintática, semântica, geração e otimização de código.

## Por que estudar isso?

Depois desta disciplina, uma mensagem de erro do compilador deixa de ser uma caixa preta irritante e vira um diagnóstico legível: "erro de sintaxe na linha 12" é literalmente o analisador sintático dizendo que a sequência de tokens não bate com nenhuma regra da gramática da linguagem. "Variável não declarada" é a tabela de símbolos reportando uma busca que falhou. Entender essas fases muda completamente como você depura.

Além disso, o conhecimento de compiladores se generaliza pra qualquer ferramenta que "parseia" alguma coisa — um linter, um formatter de código, um motor de regex, um parser de JSON ou de arquivo de configuração, até uma calculadora de expressões matemáticas. Todos usam, em miniatura, o mesmo pipeline léxico → sintático → semântico que esta disciplina ensina em tamanho real.

## Trilha de estudo

### 1. Visão geral e análise léxica (2 semanas)

O que dominar: a diferença entre compilador (traduz tudo antes de executar) e interpretador (traduz e executa linha a linha); as fases clássicas de um compilador (léxica → sintática → semântica → geração de código intermediário → otimização → geração de código final); o que é um **token** (a menor unidade com significado — palavra-chave, identificador, operador) versus um lexema (o texto bruto que originou o token); como expressões regulares (de [[pt-br/resource/computacao/linguagens-formais-e-automatos|Linguagens Formais e Autômatos]]) viram, na prática, o analisador léxico via geradores como o _lex_/_flex_. O que praticar: escrever à mão o analisador léxico de uma calculadora simples (números, `+`, `-`, `*`, `/`, parênteses) — reconhecer tokens é mais mecânico e mais rápido de dominar do que parece.

### 2. Análise sintática (3–4 semanas)

O que dominar: como uma gramática livre de contexto (de [[pt-br/resource/computacao/linguagens-formais-e-automatos|Linguagens Formais e Autômatos]]) descreve a estrutura válida de um programa; a Árvore de Sintaxe Abstrata (AST) como representação intermediária que o resto do compilador consome; ambiguidade gramatical e como reescrever gramáticas para eliminá-la; a diferença entre parsing **descendente** (top-down: LL, recursivo, mais fácil de escrever à mão) e **ascendente** (bottom-up: LR, SLR, LALR — mais poderoso, usado por geradores como _yacc_/_bison_); recuperação de erros sintáticos (não parar no primeiro erro, e sim reportar o máximo de problemas possível). O que praticar: desenhar a AST de expressões aritméticas com precedência de operadores (`2 + 3 * 4` não é o mesmo que `(2+3)*4`) — é o exercício mais didático da disciplina inteira.

![Árvore de sintaxe abstrata (AST) para o algoritmo de Euclides — cada nó interno é uma operação/estrutura de controle, e as folhas são variáveis ou valores.](https://commons.wikimedia.org/wiki/Special:FilePath/Abstract_syntax_tree_for_Euclidean_algorithm.svg)

### 3. Tabela de símbolos e análise semântica (2 semanas)

O que dominar: como a tabela de símbolos guarda, para cada identificador, seu tipo, escopo e demais atributos; verificação de tipos (garantir que `"texto" + 5` seja rejeitado ou tratado de forma bem definida); como o analisador semântico percorre a AST anotando e validando essas informações — a fase em que erros como "variável não declarada" ou "tipos incompatíveis" são detectados. O que praticar: para um trecho de código com escopos aninhados (função dentro de função, bloco dentro de bloco), simular manualmente como a tabela de símbolos entra e sai de escopo.

### 4. Geração e otimização de código (3 semanas)

O que dominar: código intermediário (código de três endereços — uma representação mais próxima de assembly, mas ainda independente de máquina), como a AST é convertida para essa forma, e as otimizações clássicas: eliminação de subexpressões comuns, propagação de constantes, eliminação de código morto, análise de fluxo de dados. O que praticar: pegar um trecho de código com redundância óbvia (`x = a + b; y = a + b;`) e otimizá-lo manualmente, depois comparar com o que um compilador real faz usando o [Compiler Explorer](https://godbolt.org/).

### 5. Ambiente de tempo de execução (1–2 semanas)

O que dominar: organização de memória de um programa em execução (pilha, heap, área de código, área estática), a pilha de ativação (_stack frame_) — como cada chamada de função aloca seu próprio espaço para variáveis locais e endereço de retorno — e uma visão geral de coleta de lixo (_garbage collection_) em linguagens que gerenciam memória automaticamente. O que praticar: desenhar a pilha de chamadas de uma função recursiva simples (fatorial, Fibonacci) quadro a quadro — é a melhor forma de entender por que recursão profunda demais causa _stack overflow_.

## Conceitos que você precisa dominar

- **Token vs. lexema** — o lexema é o texto bruto ("`if`", "`42`", "`+`"); o token é sua classificação abstrata (palavra-chave, número, operador). Todo o resto do compilador trabalha com tokens, não com o texto original.
- **Árvore de Sintaxe Abstrata (AST)** — a estrutura de dados central de um compilador: uma vez que o código vira uma AST, análise semântica, otimização e geração de código são só transformações sobre essa árvore.
- **Ambiguidade gramatical** — quando uma mesma cadeia pode ser derivada por mais de uma árvore de sintaxe; o exemplo clássico é a precedência de operadores aritméticos, resolvida reescrevendo a gramática em níveis (expressão → termo → fator).
- **Parsing LL vs. LR** — LL lê a entrada da esquerda pra direita construindo a derivação mais à esquerda (mais simples, usado em parsers recursivos escritos à mão); LR faz o mesmo construindo a derivação mais à direita de trás pra frente (mais poderoso, reconhece uma classe maior de gramáticas, mas exige um gerador de parser).
- **Tabela de símbolos** — a estrutura (geralmente uma pilha de tabelas hash, uma por escopo) que resolve "o que significa este identificador aqui?" — é o que permite que a mesma variável `x` signifique coisas diferentes em escopos diferentes.
- **Código de três endereços** — uma representação intermediária onde cada instrução tem no máximo um operador e três operandos (`t1 = b * c; t2 = a + t1`) — próxima o suficiente de assembly para gerar código de máquina, mas ainda independente da arquitetura alvo.
- **Pilha de ativação (stack frame)** — o bloco de memória que cada chamada de função reserva para parâmetros, variáveis locais e endereço de retorno; entender isso é entender por que recursão tem custo de memória e por que _stack overflow_ acontece.

## Erros comuns de quem está começando

- **Achar que um compilador só "traduz"** — na prática, a maior parte do trabalho é análise (léxica, sintática, semântica) e otimização; a tradução final para código de máquina é, proporcionalmente, uma fase pequena.
- **Confundir erro de compilação com erro de execução** — um erro de tipo é pego na análise semântica, **antes** de o programa rodar; um erro como divisão por zero só aparece em tempo de execução. Essa distinção é a diferença entre linguagens estaticamente e dinamicamente tipadas.
- **Escrever um parser recursivo descendente para uma gramática recursiva à esquerda** — isso entra em loop infinito (a função chama a si mesma antes de consumir qualquer token); é preciso eliminar a recursão à esquerda da gramática antes de implementar um parser LL.
- **Ignorar que otimizações podem mudar comportamento observável** — otimizações agressivas assumem ausência de efeitos colaterais problemáticos; código que depende de ordem de avaliação não especificada pode se comportar diferente compilado com e sem otimização.
- **Pular a base de Linguagens Formais e Autômatos** — expressões regulares e gramáticas livres de contexto não são "matéria antiga passada" aqui: são literalmente a especificação formal do analisador léxico e do analisador sintático que você constrói nesta disciplina.

## 📚 Materiais recomendados

### Livro gratuito online

- **[Crafting Interpreters](https://craftinginterpreters.com/)** (Bob Nystrom) — provavelmente o melhor material introdutório de compiladores/interpretadores que existe hoje, gratuito e completo, construindo dois interpretadores reais do zero (um em Java, outro em C). Referência moderna que complementa muito bem a bibliografia clássica da disciplina.

### Ferramentas gratuitas

- **[ANTLR](https://www.antlr.org/)** — gerador de analisadores léxicos e sintáticos amplamente usado na indústria; bom para ver, na prática, como uma gramática formal vira um parser funcional.
- **[Compiler Explorer](https://godbolt.org/)** — mostra em tempo real o código de máquina/assembly gerado por compiladores reais (GCC, Clang, etc.) para qualquer trecho de C/C++/Rust — ótimo para visualizar otimização de código na prática.

### Bibliografia clássica (consultar na biblioteca)

- AHO, A. V., LAM, M. S., SETHI, R., ULLMAN, J. D. _Compiladores: Princípios, Técnicas e Ferramentas_ (o "Dragon Book") — a referência canônica da área, cobre exatamente as fases desta trilha em profundidade.

## 🔗 Referências externas

- [Let's Build a Simple Interpreter](https://ruslanspivak.com/lsbasi-part1/) — série de posts gratuita e muito didática, construindo um interpretador em Python passo a passo desde o analisador léxico.

## Conexão com as disciplinas do curso

- [[pt-br/resource/computacao/linguagens-formais-e-automatos|Linguagens Formais e Autômatos]] — pré-requisito direto: expressões regulares/AFD viram análise léxica, gramáticas livres de contexto/autômato de pilha viram análise sintática.
- [[pt-br/resource/engenharia-de-computação/6-periodo/compiladores|Compiladores]] — a disciplina do 6º período que cobre exatamente esta trilha.
