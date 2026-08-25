---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-15-avaliacao-pratica-p2-e-montagem-de-circuitos-sequenciais
title: "Aula 15: Avaliação Prática P2 e Montagem de Circuitos Sequenciais — Eletrônica Digital"
created: 2026-12-07T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-15
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Eletrônica Digital"
professor: "Rogério"
conteudo: "Avaliação em laboratório com implementação e análise osciloscópica de FSM e contadores."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-14-maquinas-de-estados-finitos-fsm-modelos-de-mealy-e-moore">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-16-prova-final-de-eletronica-digital-e-encerramento">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Eletrônica Digital (CSECBJI.46)
> - **Professor:** Rogério
> - **Data Realizada:** 07/12/2026
> - **Tópico Principal:** Avaliação Prática P2 e Montagem de Circuitos Sequenciais
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-15-eletronica-digital|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-15-eletronica-digital|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Avaliação Prática P2 e Montagem de Circuitos Sequenciais](#-anotações-do-quadro-avaliação-prática-p2-e-montagem-de-circuitos-sequenciais)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Avaliação Prática P2 e Montagem de Circuitos Sequenciais

### 15.1 Critérios de Avaliação Prática em Bancada e Simulação
A avaliação prática P2 consiste na implementação, montagem e teste funcional de um sistema sequencial digital completo:
1. Projeto conceitual da Máquina de Estados Finitos (FSM) ou Contador Complexo.
2. Montagem e depuração no simulador Logisim com verificação de formas de onda.
3. Montagem física em protoboard utilizando CIs das famílias 74HC/TTL ou kit didático FPGA.
4. Conexão de gerador de pulsos de clock com debouncing em chaves mecânicas (*Anti-Bouncing*).
5. Decodificação de saídas em display de 7 segmentos ou matriz de LEDs.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Circuito Debouncer com Latch SR para Botões Mecânicos

Chaves mecânicas vibram contatos metálicos por $5\text{ms}$ a $20\text{ms}$ ao serem pressionadas, gerando dezenas de falsas bordas de clock.

**Solução por Latch SR (Debouncer Inviolável):**
- A chave de dois polos comuta entre o pino $S$ e o pino $R$.
- O primeiro contato mecânico chaveia o Latch para 1 (ou 0).
- Os repiques subsequentes no ar não alteram o estado do Latch, garantindo exatamente **um pulso de clock limpo**!

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart LR
    Btn[Chave Mecânica com Repiques] --> Latch[Latch SR Debouncer]
    Latch --> CleanClock[Sinal de Clock 100% Limpo]
    CleanClock --> FSM[Controlador Sequencial FSM]
    FSM --> Display[Display 7 Segmentos]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **O Perigo do Repique (*Bouncing*)** | Nunca conecte um botão mecânico direto na entrada de clock de um flip-flop sem circuito debouncer; o contador avançará números aleatórios a cada clique. | Regra prática número 1 de laboratório. |
| **Capacitor de Desacoplamento** | Coloque um capacitor cerâmico de $100	ext{nF}$ entre $V_{CC}$ e GND próximo a cada CI para filtrar ruídos de chaveamento da fonte. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Monte no Logisim um relógio digital que conte segundos de $00$ a $59$ com cascateamento de contadores módulo 10 e módulo 6.
2. Demonstre o funcionamento do circuito debouncer na bancada com osciloscópio.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-14-maquinas-de-estados-finitos-fsm-modelos-de-mealy-e-moore">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-16-prova-final-de-eletronica-digital-e-encerramento">Próxima Aula</a></b></div>
</div>
