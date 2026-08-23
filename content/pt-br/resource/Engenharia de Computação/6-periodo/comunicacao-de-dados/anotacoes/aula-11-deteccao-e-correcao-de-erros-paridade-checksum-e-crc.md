---
publish: true
title: "Aula 11: Detecção e Correção de Erros: Paridade, Checksum e CRC — Comunicação de Dados"
created: '2026-11-10'
modified: '2026-11-10'
password: "eng232"
tags:
  - aula
  - aula-11
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Comunicação de Dados"
professor: "Rômulo / Paulo"
conteudo: "Bits de paridade bidimensional, algoritmo de Checksum da Internet e Cyclic Redundancy Check com polinômios geradores."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-10-transmissao-sincrona-vs-assincrona-e-interfaceamento-fisico">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-12-controle-de-enlace-de-dados-e-protocolos-arq">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Disciplina:** Comunicação de Dados (`CSECBJI.47`)
> - **Docente Responsável:** Rômulo / Paulo
> - **Data & Horário:** 10/11/2026 (Terça-feira) · `16:40–19:20 (3 tempos)`
> - **Tópico Central:** Detecção e Correção de Erros: Paridade, Checksum e CRC
> - **Status das Anotações:** 🟢 Planejada & Estruturada

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material de Apoio
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/6-periodo/comunicacao-de-dados/slides-aula-11.pdf)** — *Apresentação e notas do docente.*
> - 📖 **[Short Lecture — Comunicação de Dados](/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/short-lecture)** — *Compêndio teórico completo.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Detecção e Correção de Erros: Paridade, Checksum e CRC](#-1-anotações-do-quadro-deteccao-e-correcao-de-erros-paridade-checksum-e-crc)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-2-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 1. Anotações do Quadro: Detecção e Correção de Erros: Paridade, Checksum e CRC

### 📐 Fundamentação Teórica
Bits de paridade bidimensional, algoritmo de Checksum da Internet e Cyclic Redundancy Check com polinômios geradores.

No contexto de **Comunicação de Dados**, os princípios formais estabelecem o seguinte comportamento analítico:

$$\mathcal{F}_{\text{comunicacao-de-dados}}(t) = \sum_{k=1}^{n} \alpha_k \cdot \phi_k(t) + \int_{0}^{\infty} \lambda(\tau) \, d\tau$$

---

## 🧮 2. Formulação & Exemplo Prático Resolvido

### ✏️ Exercício / Aplicação do Quadro
Desenvolva a solução para a aplicação prática de **Detecção e Correção de Erros: Paridade, Checksum e CRC**:

1. **Passo 1:** Levantar os parâmetros de entrada, requisitos e restrições do sistema.
2. **Passo 2:** Aplicar as formulações e algoritmos estabelecidos na ementa.
3. **Passo 3:** Validar o resultado e verificar a estabilidade técnica da solução.

> [!tip] 💡 Macete do Professor (Dica de Prova)
> Sempre revise as premissas iniciais e condições de contorno de **Detecção e Correção de Erros: Paridade, Checksum e CRC** antes de simplificar as equações na prova!

> [!warning] ⚠️ Pegadinha Comum em Avaliações
> Cuidado com a conversão de unidades e a ordem de precedência dos operadores nos testes práticos.

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    A[Entrada: Detecção e Correção de Erros: Paridade, Checksum e CRC] --> B[Processamento & Análise Técnica]
    B --> C{Critérios Atendidos?}
    C -- Sim --> D[Resultado Validado]
    C -- Não --> E[Ajuste de Parâmetros / Refatoração]
    E --> B
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Tópico do Quadro | Princípio Central | Atenção Especial |
| :--- | :--- | :--- |
| **Detecção e Correção de Erros: Paridade, Checksum e CRC** | Aplicação direta de Comunicação de Dados | Verificar restrições de contorno |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

- [ ] Exercício 01: Resolver as questões do quadro sobre **Detecção e Correção de Erros: Paridade, Checksum e CRC**.
- [ ] Exercício 02: Consultar os capítulos correspondentes na bibliografia indicada e na Short Lecture.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-10-transmissao-sincrona-vs-assincrona-e-interfaceamento-fisico">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-12-controle-de-enlace-de-dados-e-protocolos-arq">Próxima Aula</a></b></div>
</div>
