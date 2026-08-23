---
publish: true
title: "Aula 12: Fluxos de Entrada e Saída (I/O) e Serialização de Objetos — Programação Orientada a Objetos I"
created: '2026-11-18'
modified: '2026-11-18'
encrypted: true
tags:
  - aula
  - aula-12
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Programação Orientada a Objetos I"
professor: "Sérgio / Bruno"
conteudo: "Java I/O (FileInputStream, BufferedReader, Scanner, Path/Files) e serialização com Serializable/transient."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-11-mapas-e-tabelas-de-dispersao">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-13-expressoes-lambda-e-streams-api">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Programação Orientada a Objetos I (`CSECBJI.45`)
> - **Docente Responsável:** Sérgio / Bruno
> - **Data & Horário:** 18/11/2026 (Quarta-feira) · `16:40–19:20 (3 tempos)`
> - **Tópico Central:** Fluxos de Entrada e Saída (I/O) e Serialização de Objetos
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/programacao-orientada-a-objetos-i/slides-aula-12.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Programação Orientada a Objetos I](/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Fluxos de Entrada e Saída (I/O) e Serialização de Objetos](#-1-anotações-do-quadro-fluxos-de-entrada-e-saida-i-o-e-serializacao-de-objetos)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Fluxos de Entrada e Saída (I/O) e Serialização de Objetos

### 📐 Fundamentação Teórica
Java I/O (FileInputStream, BufferedReader, Scanner, Path/Files) e serialização com Serializable/transient.

No contexto de **Programação Orientada a Objetos I**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{programacao-orientada-a-objetos-i}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Fluxos de Entrada e Saída (I/O) e Serialização de Objetos**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Fluxos de Entrada e Saída (I/O) e Serialização de Objetos** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Fluxos de Entrada e Saída (I/O) e Serialização de Objetos] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Fluxos de Entrada e Saída (I/O) e Serialização de Objetos** | Aplicação direta de Programação Orientada a Objetos I | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Fluxos de Entrada e Saída (I/O) e Serialização de Objetos**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-11-mapas-e-tabelas-de-dispersao">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-13-expressoes-lambda-e-streams-api">Próxima Aula</a></b></div>
</div>
