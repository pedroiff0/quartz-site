---
publish: true
title: "Aula 14: Métricas OO e Qualidade de Software — Análise de Software Orientada a Objetos"
created: '2026-12-02'
modified: '2026-12-02'
password: "eng232"
tags:
  - aula
  - aula-14
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Análise de Software Orientada a Objetos"
professor: "Bruno"
conteudo: "Métricas de Chidamber e Kemerer (WMC, DIT, NOC, CBO, RFC, LCOM) para garantia de manutenibilidade."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-13-engenharia-reversa-refatoracao-e-code-smells">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-15-avaliacao-parcial-p2-e-apresentacao-de-projetos">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Análise de Software Orientada a Objetos (`CSECBJI.42`)
> - **Docente Responsável:** Bruno
> - **Data & Horário:** 02/12/2026 (Quarta-feira) · `13:40–16:30 (3 tempos)`
> - **Tópico Central:** Métricas OO e Qualidade de Software
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/analise-de-software-orientada-a-objetos/slides-aula-14.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Análise de Software Orientada a Objetos](/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Métricas OO e Qualidade de Software](#-1-anotações-do-quadro-metricas-oo-e-qualidade-de-software)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Métricas OO e Qualidade de Software

### 📐 Fundamentação Teórica
Métricas de Chidamber e Kemerer (WMC, DIT, NOC, CBO, RFC, LCOM) para garantia de manutenibilidade.

No contexto de **Análise de Software Orientada a Objetos**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{analise-de-software-orientada-a-objetos}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Métricas OO e Qualidade de Software**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Métricas OO e Qualidade de Software** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Métricas OO e Qualidade de Software] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Métricas OO e Qualidade de Software** | Aplicação direta de Análise de Software Orientada a Objetos | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Métricas OO e Qualidade de Software**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-13-engenharia-reversa-refatoracao-e-code-smells">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-15-avaliacao-parcial-p2-e-apresentacao-de-projetos">Próxima Aula</a></b></div>
</div>
