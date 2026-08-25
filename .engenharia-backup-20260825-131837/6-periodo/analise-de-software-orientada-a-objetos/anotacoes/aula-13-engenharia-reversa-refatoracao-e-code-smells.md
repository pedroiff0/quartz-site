---
publish: true
title: "Aula 13: Engenharia Reversa, Refatoração e Code Smells — Análise de Software Orientada a Objetos"
created: '2026-11-25'
modified: '2026-11-25'
encrypted: true
tags:
  - aula
  - aula-13
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Análise de Software Orientada a Objetos"
professor: "Bruno"
conteudo: "Identificação de code smells (God Class, Feature Envy, Long Method) e técnicas sistemáticas de refatoração."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-12-arquitetura-de-software-em-camadas-e-mvc">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-14-metricas-oo-e-qualidade-de-software">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Análise de Software Orientada a Objetos (`CSECBJI.42`)
> - **Docente Responsável:** Bruno
> - **Data & Horário:** 25/11/2026 (Quarta-feira) · `13:40–16:30 (3 tempos)`
> - **Tópico Central:** Engenharia Reversa, Refatoração e Code Smells
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/analise-de-software-orientada-a-objetos/slides-aula-13.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Análise de Software Orientada a Objetos](/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Engenharia Reversa, Refatoração e Code Smells](#-1-anotações-do-quadro-engenharia-reversa-refatoracao-e-code-smells)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Engenharia Reversa, Refatoração e Code Smells

### 📐 Fundamentação Teórica
Identificação de code smells (God Class, Feature Envy, Long Method) e técnicas sistemáticas de refatoração.

No contexto de **Análise de Software Orientada a Objetos**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{analise-de-software-orientada-a-objetos}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Engenharia Reversa, Refatoração e Code Smells**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Engenharia Reversa, Refatoração e Code Smells** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Engenharia Reversa, Refatoração e Code Smells] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Engenharia Reversa, Refatoração e Code Smells** | Aplicação direta de Análise de Software Orientada a Objetos | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Engenharia Reversa, Refatoração e Code Smells**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-12-arquitetura-de-software-em-camadas-e-mvc">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-14-metricas-oo-e-qualidade-de-software">Próxima Aula</a></b></div>
</div>
