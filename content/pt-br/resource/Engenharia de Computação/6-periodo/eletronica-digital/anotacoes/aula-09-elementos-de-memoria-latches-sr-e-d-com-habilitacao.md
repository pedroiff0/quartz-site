---
publish: true
title: "Aula 09: Elementos de Memória: Latches SR e D com Habilitação — Eletrônica Digital"
created: '2026-10-26'
modified: '2026-10-26'
encrypted: true
tags:
  - aula
  - aula-09
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Eletrônica Digital"
professor: "Rogério"
conteudo: "Realimentação em circuitos lógicos, latches com portas NAND/NOR, problemas de metastabilidade e sinal de clock."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-08-avaliacao-teorico-pratica-p1">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-10-flip-flops-disparados-por-borda-sr-d-jk-t">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Eletrônica Digital (`CSECBJI.46`)
> - **Docente Responsável:** Rogério
> - **Data & Horário:** 26/10/2026 (Segunda-feira) · `16:40–19:20 (3 tempos)`
> - **Tópico Central:** Elementos de Memória: Latches SR e D com Habilitação
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/eletronica-digital/slides-aula-09.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Eletrônica Digital](/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Elementos de Memória: Latches SR e D com Habilitação](#-1-anotações-do-quadro-elementos-de-memoria-latches-sr-e-d-com-habilitacao)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Elementos de Memória: Latches SR e D com Habilitação

### 📐 Fundamentação Teórica
Realimentação em circuitos lógicos, latches com portas NAND/NOR, problemas de metastabilidade e sinal de clock.

No contexto de **Eletrônica Digital**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{eletronica-digital}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Elementos de Memória: Latches SR e D com Habilitação**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Elementos de Memória: Latches SR e D com Habilitação** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Elementos de Memória: Latches SR e D com Habilitação] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Elementos de Memória: Latches SR e D com Habilitação** | Aplicação direta de Eletrônica Digital | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Elementos de Memória: Latches SR e D com Habilitação**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-08-avaliacao-teorico-pratica-p1">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-10-flip-flops-disparados-por-borda-sr-d-jk-t">Próxima Aula</a></b></div>
</div>
