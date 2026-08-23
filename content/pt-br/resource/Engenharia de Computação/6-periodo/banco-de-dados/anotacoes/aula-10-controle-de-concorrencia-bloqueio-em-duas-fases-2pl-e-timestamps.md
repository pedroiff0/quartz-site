---
publish: true
title: "Aula 10: Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps — Banco de Dados"
created: '2026-11-03'
modified: '2026-11-03'
password: "eng232"
tags:
  - aula
  - aula-10
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Banco de Dados"
professor: "Sérgio"
conteudo: "Protocolo 2PL (estrito/rigoroso), detecção e prevenção de deadlocks (Wait-Die, Wound-Wait) e controle multiversão (MVCC)."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-09-gerenciamento-de-transacoes-e-propriedades-acid">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-11-recuperacao-de-falhas-logs-wal-checkpoints-e-algoritmo-aries">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Banco de Dados (`CSECBJI.44`)
> - **Docente Responsável:** Sérgio
> - **Data & Horário:** 03/11/2026 (Terça-feira) · `13:40–16:30 (3 tempos)`
> - **Tópico Central:** Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/banco-de-dados/slides-aula-10.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Banco de Dados](/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps](#-1-anotações-do-quadro-controle-de-concorrencia-bloqueio-em-duas-fases-2pl-e-timestamps)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps

### 📐 Fundamentação Teórica
Protocolo 2PL (estrito/rigoroso), detecção e prevenção de deadlocks (Wait-Die, Wound-Wait) e controle multiversão (MVCC).

No contexto de **Banco de Dados**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{banco-de-dados}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps** | Aplicação direta de Banco de Dados | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Controle de Concorrência: Bloqueio em Duas Fases (2PL) e Timestamps**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-09-gerenciamento-de-transacoes-e-propriedades-acid">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/anotacoes/aula-11-recuperacao-de-falhas-logs-wal-checkpoints-e-algoritmo-aries">Próxima Aula</a></b></div>
</div>
