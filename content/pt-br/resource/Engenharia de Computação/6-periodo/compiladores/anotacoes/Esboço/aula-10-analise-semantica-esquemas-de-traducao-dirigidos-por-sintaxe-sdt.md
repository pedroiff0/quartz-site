---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-10-analise-semantica-esquemas-de-traducao-dirigidos-por-sintaxe-sdt
title: "Aula 10: Análise Semântica: Esquemas de Tradução Dirigidos por Sintaxe (SDT) — Compiladores"
created: 2026-11-06T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-10
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Compiladores"
professor: "Fabrício Barros"
conteudo: "Definições Dirigidas por Sintaxe (SDD), atributos sintetizados e herdados, e gramáticas S-atribuídas e L-atribuídas."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-09-estruturas-e-gerenciamento-da-tabela-de-simbolos">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-11-sistemas-de-tipos-inferencia-e-verificacao-semantica">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Compiladores (CSECBJI.48)
> - **Professor:** Fabrício Barros
> - **Data Realizada:** 06/11/2026
> - **Tópico Principal:** Análise Semântica: Esquemas de Tradução Dirigidos por Sintaxe (SDT)
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-10-compiladores|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-10-compiladores|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Análise Semântica: Esquemas de Tradução Dirigidos por Sintaxe (SDT)](#-anotações-do-quadro-análise-semântica-esquemas-de-tradução-dirigidos-por-sintaxe-sdt)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Análise Semântica: Esquemas de Tradução Dirigidos por Sintaxe (SDT)

### 10.1 Definições Dirigidas por Sintaxe (SDD)
Uma **Definição Dirigida por Sintaxe (SDD)** associa regras semânticas a cada produção gramatical. Cada símbolo possui atributos:
- **Atributos Sintetizados:** O valor no nó pai $N$ é calculado estritamente a partir dos valores dos nós filhos de $N$.
- **Atributos Herdados:** O valor no nó $N$ é calculado a partir dos atributos dos nós irmãos de $N$ ou do seu nó pai.

### 10.2 Classes de Gramáticas com Atributos
1. **Gramáticas $S$-Atribuídas:** Utilizam **exclusivamente atributos sintetizados**. Podem ser avaliadas de forma puramente *bottom-up* durante o parsing LR em um único passe.
2. **Gramáticas $L$-Atribuídas:** Permitem atributos herdados, com a restrição de que cada atributo herdado de um nó filho depende apenas dos atributos do pai ou dos irmãos à sua esquerda.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Exemplo: SDD para Calculadora de Expressões ($S$-Atribuída)

| Produção Gramatical | Regra Semântica Associada |
| :--- | :--- |
| $L \to E \; \mathbf{n}$ | $\text{print}(E.val)$ |
| $E \to E_1 + T$ | $E.val = E_1.val + T.val$ |
| $E \to T$ | $E.val = T.val$ |
| $T \to T_1 * F$ | $T.val = T_1.val * F.val$ |
| $T \to F$ | $T.val = F.val$ |
| $F \to ( E )$ | $F.val = E.val$ |
| $F \to \mathbf{digit}$ | $F.val = \mathbf{digit}.lexval$ |

**Grafo de Dependência para `3 * 5 + 4`:**
- Folha $F_1.val = 3$, Folha $F_2.val = 5 \implies T_1.val = 15$
- Folha $F_3.val = 4 \implies T_2.val = 4$
- Raiz $E.val = 15 + 4 = 19$

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    E["E.val = 19"] --> T1["T.val = 15"]
    E --> PLUS["+"]
    E --> T2["T.val = 4"]
    T1 --> T11["T.val = 3"]
    T1 --> MULT["*"]
    T1 --> F1["F.val = 5"]
    T11 --> F2["F.val = 3"]
    T2 --> F3["F.val = 4"]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Ciclos no Grafo de Dependência** | Se o grafo de dependência contiver ciclos, a SDD não pode ser avaliada! Garanta que seja $S$-atribuída ou $L$-atribuída. | A ordenação topológica do grafo fornece a sequência exata de avaliação. |
| **Ações Embutidas no Bison** | Ações como `{ $$ = $1 + $3; }` em especificações Bison implementam diretamente SDDs $S$-atribuídas. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Escreva a SDD para converter números binários para base decimal (ex: `1101` $	o 13$).
2. Diferencie formalmente um atributo sintetizado de um herdado.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-09-estruturas-e-gerenciamento-da-tabela-de-simbolos">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-11-sistemas-de-tipos-inferencia-e-verificacao-semantica">Próxima Aula</a></b></div>
</div>
