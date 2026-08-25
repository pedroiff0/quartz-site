---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-10-metodos-de-avaliacao-de-investimentos-payback-simples-e-descontado
title: "Aula 10: Métodos de Avaliação de Investimentos: Payback Simples e Descontado — Gestão de Projetos"
created: 2026-11-05T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-10
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Gestão de Projetos"
professor: "Hilton"
conteudo: "Cálculo do tempo de retorno do capital investido, limitações do payback simples e ajuste temporal pelo payback descontado."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-09-engenharia-economica-fluxo-de-caixa-projetado-e-taxa-minima-de-atratividade">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-11-avaliacao-economica-avancada-valor-presente-liquido-vpl-e-taxa-interna-de-retorno-tir">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Gestão de Projetos (CSECBJI.49)
> - **Professor:** Hilton
> - **Data Realizada:** 05/11/2026
> - **Tópico Principal:** Métodos de Avaliação de Investimentos: Payback Simples e Descontado
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-10-gestao-de-projetos|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-10-gestao-de-projetos|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Métodos de Avaliação de Investimentos: Payback Simples e Descontado](#-anotações-do-quadro-métodos-de-avaliação-de-investimentos-payback-simples-e-descontado)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Métodos de Avaliação de Investimentos: Payback Simples e Descontado

### 10.1 Método do Payback Simples (Período de Retorno do Capital)
O **Payback Simples** mede o tempo exato necessário para que a soma acumulada dos fluxos de caixa líquidos operacionais recupere o investimento inicial desembolsado ($I_0$):
$$\sum_{t=1}^{\text{Payback}} FC_t = I_0$$
- *Vantagem:* Cálculo simples e métrica intuitiva de liquidez e risco (quanto menor o payback, menor o tempo de exposição ao risco).
- *Limitações Graves:*
  1. **Ignora o valor do dinheiro no tempo** (trata R$ 100 daqui a 5 anos como iguais a R$ 100 hoje).
  2. **Ignora todos os fluxos de caixa gerados após o período de retorno.**

### 10.2 Método do Payback Descontado
Corrige a principal limitação do payback simples, trazendo cada fluxo de caixa futuro ao seu **Valor Presente (VP)** descontado pela Taxa Mínima de Atratividade ($k$ / TMA):
$$VP(FC_t) = \frac{FC_t}{(1 + k)^t}$$
$$\sum_{t=1}^{\text{Payback Descontado}} \frac{FC_t}{(1 + k)^t} = I_0$$
- O Payback Descontado é **sempre maior que o Payback Simples** devido ao desconto temporal dos juros.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Comparação Numérica: Payback Simples vs Descontado (TMA = $10\%$ a.a.)

**Projeto:** Investimento Inicial $I_0 = \text{R\$} 100.000$. Fluxos anuais: $FC_1 = 40\text{k}$, $FC_2 = 40\text{k}$, $FC_3 = 40\text{k}$, $FC_4 = 40\text{k}$.

| Ano | Fluxo Nominal | Saldo Acumulado Simples | Fator $(1.10)^t$ | Fluxo Descontado ($VP$) | Saldo Acumulado Descontado |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | (R$ 100.000) | (R$ 100.000) | 1.000 | (R$ 100.000) | (R$ 100.000) |
| 1 | R$ 40.000 | (R$ 60.000) | 1.100 | R$ 36.364 | (R$ 63.636) |
| 2 | R$ 40.000 | (R$ 20.000) | 1.210 | R$ 33.058 | (R$ 30.578) |
| 3 | R$ 40.000 | **+ R$ 20.000** | 1.331 | R$ 30.053 | **(R$ 525)** |
| 4 | R$ 40.000 | + R$ 60.000 | 1.464 | R$ 27.322 | **+ R$ 26.797** |

**Resultados:**
- **Payback Simples:** $2.5\text{ anos}$ ($2\text{ anos e } 6\text{ meses}$).
- **Payback Descontado:** $3.02\text{ anos}$ ($3\text{ anos e } 7\text{ dias}$).
O método simples mascarou mais de 6 meses de defasagem de juros do capital!

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart LR
    Inv["Investimento Inicial: -R$ 100k"] --> Y1["Ano 1: VP +36.4k (Saldo: -63.6k)"]
    Y1 --> Y2["Ano 2: VP +33.1k (Saldo: -30.6k)"]
    Y2 --> Y3["Ano 3: VP +30.1k (Saldo: -0.5k)"]
    Y3 --> Rec["Ano 3.02: Payback Descontado Atingido!"]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Interpolação Linear no Payback** | Para calcular a fração de meses no ano de virada do saldo: $	ext{Fração} = rac{	ext{Saldo Devedor Residual}}{	ext{Fluxo do Próximo Ano}}$. | Evita arredondamentos grosseiros. |
| **Payback não Mede Rentabilidade** | Um projeto com payback rápido pode ser menos rentável a longo prazo que um projeto com payback mais longo mas com fluxos massivos nos anos seguintes. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Calcule o Payback Simples e Descontado (TMA de $12\%$ a.a.) para um projeto com $I_0 = 	ext{R\$} 250.000$ e fluxos anuais de R$ 70k, R$ 90k, R$ 110k, R$ 120k.
2. Explique por que o Payback Simples pode levar a decisões de investimento errôneas em projetos de longa duração.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-09-engenharia-economica-fluxo-de-caixa-projetado-e-taxa-minima-de-atratividade">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-11-avaliacao-economica-avancada-valor-presente-liquido-vpl-e-taxa-interna-de-retorno-tir">Próxima Aula</a></b></div>
</div>
