---
publish: true
title: "Aula 04: Gramáticas Livres de Contexto (GLC) e Árvores de Derivação — Compiladores"
created: '2026-09-25'
modified: '2026-09-25'
password: "eng232"
tags:
  - aula
  - aula-04
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Compiladores"
professor: "Fabrício Barros"
conteudo: "Terminais, não-terminais, regras de produção, derivações mais à esquerda/direita e eliminação de ambiguidade."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-03-construcao-e-uso-de-geradores-lexicos-flex-jflex">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-05-analise-sintatica-descendente-ll-1-e-parser-por-descida-recursiva">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Compiladores (`CSECBJI.48`)
> - **Docente Responsável:** Fabrício Barros
> - **Data & Horário:** 25/09/2026 (Sexta-feira) · `13:40–16:30 (3 tempos)`
> - **Tópico Central:** Gramáticas Livres de Contexto (GLC) e Árvores de Derivação
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/compiladores/slides-aula-04.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Compiladores](/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Gramáticas Livres de Contexto (GLC) e Árvores de Derivação](#-1-anotações-do-quadro-gramaticas-livres-de-contexto-glc-e-arvores-de-derivacao)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Gramáticas Livres de Contexto (GLC) e Árvores de Derivação

### 📐 Fundamentação Teórica
Terminais, não-terminais, regras de produção, derivações mais à esquerda/direita e eliminação de ambiguidade.

No contexto de **Compiladores**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{compiladores}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Gramáticas Livres de Contexto (GLC) e Árvores de Derivação**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Gramáticas Livres de Contexto (GLC) e Árvores de Derivação** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Gramáticas Livres de Contexto (GLC) e Árvores de Derivação] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Gramáticas Livres de Contexto (GLC) e Árvores de Derivação** | Aplicação direta de Compiladores | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Gramáticas Livres de Contexto (GLC) e Árvores de Derivação**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-03-construcao-e-uso-de-geradores-lexicos-flex-jflex">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores/anotacoes/aula-05-analise-sintatica-descendente-ll-1-e-parser-por-descida-recursiva">Próxima Aula</a></b></div>
</div>
