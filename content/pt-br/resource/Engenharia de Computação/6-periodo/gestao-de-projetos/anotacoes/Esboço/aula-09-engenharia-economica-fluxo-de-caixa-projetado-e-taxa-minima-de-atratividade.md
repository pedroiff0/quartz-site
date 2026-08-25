---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-09-engenharia-economica-fluxo-de-caixa-projetado-e-taxa-minima-de-atratividade
title: "Aula 09: Engenharia Econômica: Fluxo de Caixa Projetado e Taxa Mínima de Atratividade — Gestão de Projetos"
created: 2026-10-29T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-09
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Gestão de Projetos"
professor: "Hilton"
conteudo: "Construção do fluxo de caixa operacional e de investimentos, custo de oportunidade do capital e determinação da TMA."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-08-gestao-de-custos-estimativas-orcamento-e-analise-de-ponto-de-equilibrio">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-10-metodos-de-avaliacao-de-investimentos-payback-simples-e-descontado">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Gestão de Projetos (CSECBJI.49)
> - **Professor:** Hilton
> - **Data Realizada:** 29/10/2026
> - **Tópico Principal:** Engenharia Econômica: Fluxo de Caixa Projetado e Taxa Mínima de Atratividade
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-09-gestao-de-projetos|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-09-gestao-de-projetos|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Engenharia Econômica: Fluxo de Caixa Projetado e Taxa Mínima de Atratividade](#-anotações-do-quadro-engenharia-econômica-fluxo-de-caixa-projetado-e-taxa-mínima-de-atratividade)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Engenharia Econômica: Fluxo de Caixa Projetado e Taxa Mínima de Atratividade

### 9.1 Estrutura do Fluxo de Caixa Projetado
O Fluxo de Caixa Prospeccional projeta todas as entradas e saídas de caixa operacionais e de capital ao longo do horizonte de planejamento do projeto (tipicamente 5 anos):
- **Investimento Inicial (Capex / Ano 0):** Desembolso de capital em infraestrutura, máquinas, desenvolvimento inicial e capital de giro ($I_0$).
- **Receitas Operacionais Brutas:** Volume de vendas projetado $\times$ preço unitário.
- **Custos Operacionais (Opex):** Custos fixos e variáveis de produção.
- **Depreciação de Ativos:** Despesa não-desembolsável que reduz o lucro tributável (benefício fiscal).
- **Impostos sobre o Lucro (IR/CSLL):** Incidentes sobre o LAIR (*Lucro Antes do IR*).
- **Fluxo de Caixa Líquido ($FC_t$):**
  $$FC_t = (\text{Receitas} - \text{Custos} - \text{Depreciação}) \times (1 - T) + \text{Depreciação} - \Delta\text{Capital de Giro}$$

### 9.2 Taxa Mínima de Atratividade (TMA / Custo de Capital)
A TMA é a taxa de juros que representa o **custo de oportunidade** do capital investido:
- Deve ser superior à taxa livre de risco da economia (ex: Taxa SELIC / Tesouro Direto).
- Incorpora o prêmio de risco do setor tecnológico:
  $$\text{TMA} = R_f + \text{Prêmio de Risco}$$
- Em grandes corporações, utiliza-se o Custo Médio Ponderado de Capital (**WACC - *Weighted Average Cost of Capital***).

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Construção de Demonstração de Fluxo de Caixa Operacional Anual

**Dados Anuais:**
- Receita Operacional: R$ 500.000
- Custos Operacionais: R$ 200.000
- Depreciação Linear: R$ 50.000
- Alíquota de Tributos ($T$): $34\%$ (IRPJ + CSLL)

| Linha do Demonstrativo | Cálculo | Valor (R$) |
| :--- | :--- | :--- |
| **(=) Receita Bruta** | | R$ 500.000 |
| **(-) Custos Operacionais** | | (R$ 200.000) |
| **(-) Depreciação** | | (R$ 50.000) |
| **(=) Lucro Antes do IR (LAIR)** | $500\text{k} - 200\text{k} - 50\text{k}$ | **R$ 250.000** |
| **(-) Impostos ($34\%$)** | $250\text{k} \times 0.34$ | (R$ 85.000) |
| **(=) Lucro Líquido** | $250\text{k} - 85\text{k}$ | **R$ 165.000** |
| **(+) Reversão da Depreciação** | (Não é saída de caixa!) | + R$ 50.000 |
| **(=) Fluxo de Caixa Líquido do Ano** | $165\text{k} + 50\text{k}$ | **R$ 215.000** |

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    Rev[Receita Operacional Bruta] --> Sub1["(-) Custos e Despesas Operacionais"]
    Sub1 --> Sub2["(-) Depreciação de Máquinas"]
    Sub2 --> LAIR[(=) Lucro Antes do IR]
    LAIR --> Tax["(-) Tributos IRPJ/CSLL"]
    Tax --> Net[(=) Lucro Líquido]
    Net --> DepAdd["(+) Reversão da Depreciação (Caixa Real)"]
    DepAdd --> FCL[(=) Fluxo de Caixa Líquido do Período]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Por que Somar a Depreciação de Volta?** | A depreciação reduz o imposto a pagar porque entra como despesa no demonstrativo contábil, mas o dinheiro da depreciação NUNCA saiu do saldo do banco! Por isso, ela é somada de volta no fluxo de caixa líquido. | Conceito indispensável em engenharia econômica. |
| **TMA como Régua de Corte** | Se um projeto render menos que a TMA, é mais vantajoso deixar o dinheiro aplicado em títulos públicos do governo sem risco nenhum. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Projete o fluxo de caixa líquido para um horizonte de 5 anos com investimento inicial de R$ 300.000 e receitas crescentes em 15% ao ano.
2. Calcule o WACC de uma empresa financiada por 60% de capital próprio (custo de 18%) e 40% de capital de terceiros (custo de 12% antes de impostos a 34%).

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-08-gestao-de-custos-estimativas-orcamento-e-analise-de-ponto-de-equilibrio">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-10-metodos-de-avaliacao-de-investimentos-payback-simples-e-descontado">Próxima Aula</a></b></div>
</div>
