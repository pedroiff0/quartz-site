---
publish: true
title: "Aula 02: Álgebra Relacional: Seleção, Projeção, Junção e Divisão — Banco de Dados"
created: '2026-09-08'
modified: '2026-09-08'
password: "eng232"
tags:
  - aula
  - aula-02
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Banco de Dados"
professor: "Sérgio"
conteudo: "Operadores formais unários e binários, produto cartesiano, theta-join, natural join e cálculo relacional."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-01-o-modelo-relacional-e-fundamentos-de-bancos-de-dados">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-03-sql-avancado-subconsultas-agrupamento-e-juncoes-complexas">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Banco de Dados (`CSECBJI.44`)
> - **Docente Responsável:** Sérgio
> - **Data & Horário:** 08/09/2026 (Terça-feira) · `13:40–16:30 (3 tempos)`
> - **Tópico Central:** Álgebra Relacional: Seleção, Projeção, Junção e Divisão
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/banco-de-dados/slides-aula-02.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Banco de Dados](/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Álgebra Relacional: Seleção, Projeção, Junção e Divisão](#-1-anotações-do-quadro-algebra-relacional-selecao-projecao-juncao-e-divisao)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Álgebra Relacional: Seleção, Projeção, Junção e Divisão

### 📐 Fundamentação Teórica
Operadores formais unários e binários, produto cartesiano, theta-join, natural join e cálculo relacional.

No contexto de **Banco de Dados**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{banco-de-dados}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Álgebra Relacional: Seleção, Projeção, Junção e Divisão**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Álgebra Relacional: Seleção, Projeção, Junção e Divisão** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Álgebra Relacional: Seleção, Projeção, Junção e Divisão] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Álgebra Relacional: Seleção, Projeção, Junção e Divisão** | Aplicação direta de Banco de Dados | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Álgebra Relacional: Seleção, Projeção, Junção e Divisão**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-01-o-modelo-relacional-e-fundamentos-de-bancos-de-dados">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-03-sql-avancado-subconsultas-agrupamento-e-juncoes-complexas">Próxima Aula</a></b></div>
</div>
