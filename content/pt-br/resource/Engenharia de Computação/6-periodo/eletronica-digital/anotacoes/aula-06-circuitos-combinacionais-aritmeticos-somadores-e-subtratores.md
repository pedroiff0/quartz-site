---
publish: true
title: "Aula 06: Circuitos Combinacionais Aritméticos: Somadores e Subtratores — Eletrônica Digital"
created: '2026-10-05'
modified: '2026-10-05'
password: "eng232"
tags:
  - aula
  - aula-06
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Eletrônica Digital"
professor: "Rogério"
conteudo: "Meio-somador (Half-Adder), somador completo (Full-Adder), somador paralelo Ripple-Carry e subtrações em complemento de 2."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-05-condicoes-irrelevantes-don-t-cares-e-mapas-de-5-variaveis">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-07-multiplexadores-demultiplexadores-codificadores-e-decodificadores">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Eletrônica Digital (`CSECBJI.46`)
> - **Docente Responsável:** Rogério
> - **Data & Horário:** 05/10/2026 (Segunda-feira) · `16:40–19:20 (3 tempos)`
> - **Tópico Central:** Circuitos Combinacionais Aritméticos: Somadores e Subtratores
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/eletronica-digital/slides-aula-06.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Eletrônica Digital](/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Circuitos Combinacionais Aritméticos: Somadores e Subtratores](#-1-anotações-do-quadro-circuitos-combinacionais-aritmeticos-somadores-e-subtratores)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Circuitos Combinacionais Aritméticos: Somadores e Subtratores

### 📐 Fundamentação Teórica
Meio-somador (Half-Adder), somador completo (Full-Adder), somador paralelo Ripple-Carry e subtrações em complemento de 2.

No contexto de **Eletrônica Digital**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{eletronica-digital}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Circuitos Combinacionais Aritméticos: Somadores e Subtratores**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Circuitos Combinacionais Aritméticos: Somadores e Subtratores** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Circuitos Combinacionais Aritméticos: Somadores e Subtratores] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Circuitos Combinacionais Aritméticos: Somadores e Subtratores** | Aplicação direta de Eletrônica Digital | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Circuitos Combinacionais Aritméticos: Somadores e Subtratores**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-05-condicoes-irrelevantes-don-t-cares-e-mapas-de-5-variaveis">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-07-multiplexadores-demultiplexadores-codificadores-e-decodificadores">Próxima Aula</a></b></div>
</div>
