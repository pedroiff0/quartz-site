---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-05-analise-sintatica-descendente-ll-1-e-parser-por-descida-recursiva
title: "Aula 05: Análise Sintática Descendente: LL(1) e Parser por Descida Recursiva — Compiladores"
created: 2026-10-02T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-05
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Compiladores"
professor: "Fabrício Barros"
conteudo: "Cálculo de conjuntos FIRST e FOLLOW, construção de tabelas preditivas LL(1) e tratamento de recursão à esquerda."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-04-gramaticas-livres-de-contexto-glc-e-arvores-de-derivacao">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-06-analise-sintatica-ascendente-conceitos-lr-0-e-tabelas-slr-1">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Compiladores (CSECBJI.48)
> - **Professor:** Fabrício Barros
> - **Data Realizada:** 02/10/2026
> - **Tópico Principal:** Análise Sintática Descendente: LL(1) e Parser por Descida Recursiva
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-05-compiladores|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-05-compiladores|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Análise Sintática Descendente: LL(1) e Parser por Descida Recursiva](#-anotações-do-quadro-análise-sintática-descendente-ll1-e-parser-por-descida-recursiva)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Análise Sintática Descendente: LL(1) e Parser por Descida Recursiva

### 5.1 Pré-Requisitos para Análise Preditiva LL(1)
Um analisador sintático **LL(1)** (*Left-to-right, Leftmost derivation, 1 lookahead token*) opera de cima para baixo (*Top-Down*). Para uma gramática ser LL(1), ela não pode ter recursão à esquerda e deve estar devidamente fatorada à esquerda.

#### 1. Eliminação de Recursão à Esquerda Direta:
$$A \to A\alpha \mid \beta \implies A \to \beta A', \quad A' \to \alpha A' \mid \epsilon$$

#### 2. Fatoração à Esquerda:
$$A \to \alpha\beta_1 \mid \alpha\beta_2 \implies A \to \alpha A', \quad A' \to \beta_1 \mid \beta_2$$

### 5.2 Algoritmos de FIRST e FOLLOW
- $\text{FIRST}(\alpha)$: Conjunto de terminais que iniciam cadeias derivadas de $\alpha$.
- $\text{FOLLOW}(A)$: Conjunto de terminais que podem aparecer imediatamente após $A$ em derivações.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Cálculo de FIRST, FOLLOW e Tabela LL(1)

**Gramática Aritmética Transformada:**
1. $E \to T E'$
2. $E' \to + T E' \mid \epsilon$
3. $T \to F T'$
4. $T' \to * F T' \mid \epsilon$
5. $F \to ( E ) \mid \mathbf{id}$

**Conjuntos Calculados:**
- $\text{FIRST}(F) = \text{FIRST}(T) = \text{FIRST}(E) = \{ (, \mathbf{id} \}$
- $\text{FIRST}(E') = \{ +, \epsilon \}$, $\text{FIRST}(T') = \{ *, \epsilon \}$
- $\text{FOLLOW}(E) = \text{FOLLOW}(E') = \{ \$, ) \}$
- $\text{FOLLOW}(T) = \text{FOLLOW}(T') = \{ +, \$, ) \}$
- $\text{FOLLOW}(F) = \{ *, +, \$, ) \}$

**Tabela Sintática Preditiva $M[A, a]$:**

| Não-Terminal | $\mathbf{id}$ | $+$ | $*$ | $($ | $)$ | $\$$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **$E$** | $E \to T E'$ | | | $E \to T E'$ | | |
| **$E'$** | | $E' \to + T E'$ | | | $E' \to \epsilon$ | $E' \to \epsilon$ |
| **$T$** | $T \to F T'$ | | | $T \\to F T'$ | | |
| **$T'$** | | $T' \to \epsilon$ | $T' \to * F T'$ | | $T' \to \epsilon$ | $T' \to \epsilon$ |
| **$F$** | $F \to \mathbf{id}$ | | | $F \to ( E )$ | | |

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    Top[Entrada de Tokens + Lookahead] --> Check{Consulta M[Topo, Lookahead]}
    Check -->|Produção A -> alpha| Exp[Desempilha A, Empilha alpha em ordem inversa]
    Check -->|Terminal Casa| Cons[Desempilha e consome token de entrada]
    Check -->|Entrada Vazia| Err[Dispara Erro de Sintaxe]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Critério Formal LL(1)** | Para cada $A 	o lpha \mid eta$: $	ext{FIRST}(lpha) \cap 	ext{FIRST}(eta) = \emptyset$. Se $\epsilon \in 	ext{FIRST}(lpha)$, então $	ext{FIRST}(eta) \cap 	ext{FOLLOW}(A) = \emptyset$. | Se uma célula tiver mais de uma produção, a gramática NÃO é LL(1)! |
| **Descida Recursiva** | Cada não-terminal vira uma função em C/Java. Não-terminais com $\epsilon$ usam o `FOLLOW` para decidir retornar sem erro. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Implemente em pseudocódigo a função de descida recursiva para o não-terminal `E()` e `E_Linha()`.
2. Construa a tabela preditiva LL(1) para uma gramática de declaração de variáveis.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-04-gramaticas-livres-de-contexto-glc-e-arvores-de-derivacao">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-06-analise-sintatica-ascendente-conceitos-lr-0-e-tabelas-slr-1">Próxima Aula</a></b></div>
</div>
