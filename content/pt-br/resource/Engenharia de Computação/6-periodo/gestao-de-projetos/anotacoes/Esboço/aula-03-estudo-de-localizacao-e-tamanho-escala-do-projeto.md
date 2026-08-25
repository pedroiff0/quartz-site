---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-03-estudo-de-localizacao-e-tamanho-escala-do-projeto
title: "Aula 03: Estudo de Localização e Tamanho/Escala do Projeto — Gestão de Projetos"
created: 2026-09-17T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-03
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Gestão de Projetos"
professor: "Hilton"
conteudo: "Fatores locacionais qualitativos e quantitativos (Método dos Pesos Ponderados), escala produtiva e curva de aprendizagem."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-02-estudo-de-viabilidade-tecnico-economica-evte-e-analise-de-mercado">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-04-engenharia-do-projeto-balanco-de-materiais-e-layout-operacional">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Gestão de Projetos (CSECBJI.49)
> - **Professor:** Hilton
> - **Data Realizada:** 17/09/2026
> - **Tópico Principal:** Estudo de Localização e Tamanho/Escala do Projeto
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-03-gestao-de-projetos|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-03-gestao-de-projetos|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Estudo de Localização e Tamanho/Escala do Projeto](#-anotações-do-quadro-estudo-de-localização-e-tamanho/escala-do-projeto)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Estudo de Localização e Tamanho/Escala do Projeto

### 3.1 Estudo de Localização de Projetos
A escolha do local para instalação de uma fábrica, data center ou filial corporativa impacta permanentemente os custos operacionais e a qualidade dos serviços:
- **Fatores Locacionais Qualitativos e Quantitativos:**
  - Proximidade com o mercado consumidor e clientes estratégicos.
  - Disponibilidade e custo de mão de obra qualificada (desenvolvedores, engenheiros).
  - Infraestrutura básica: redundância de energia elétrica, fibra óptica de múltiplos provedores (Carrier-Neutral), água e saneamento.
  - Incentivos fiscais municipais/estaduais (redução de ISS/ICMS).
  - Custo de aquisição ou locação do metro quadrado de terreno/imóvel.

### 3.2 O Método dos Pesos Ponderados (Ponto Ponderado)
Método analítico multicritério para ranqueamento de cidades/locais candidatos:
1. Atribui-se um peso $w_i$ ($\sum w_i = 1.0$) a cada critério locacional.
2. Atribui-se uma nota de desempenho $N_{ij}$ (escala de 1 a 10) para cada localidade $j$.
3. A pontuação global é: $P_j = \sum_{i=1}^k w_i \cdot N_{ij}$.

### 3.3 Escala do Projeto e Curva de Aprendizagem
- **Economia de Escala:** Redução do custo médio unitário com o aumento do volume de produção decorrente da diluição dos custos fixos.
- **Curva de Aprendizagem (Wright, 1936):** Toda vez que a produção acumulada de um produto dobra, o tempo e o custo de mão de obra por unidade caem em uma taxa percentual constante $L$.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Aplicação do Método dos Pesos Ponderados para Escolha de Data Center

Cidades Candidatas: **Campos dos Goytacazes (RJ)** vs **Macaé (RJ)** vs **São Paulo (SP)**

| Critério Locacional | Peso ($w_i$) | Campos (Nota) | Macaé (Nota) | São Paulo (Nota) |
| :--- | :---: | :---: | :---: | :---: |
| 1. Redundância de Energia e Conectividade | 0.30 | 7 (2.1) | 8 (2.4) | 10 (3.0) |
| 2. Custo do Terreno e Infraestrutura | 0.25 | 9 (2.25) | 6 (1.5) | 4 (1.0) |
| 3. Mão de Obra de Engenharia (IFF/UENF) | 0.20 | 8 (1.6) | 7 (1.4) | 9 (1.8) |
| 4. Incentivos Fiscais Municipais | 0.15 | 8 (1.2) | 7 (1.05) | 5 (0.75) |
| 5. Proximidade com Clientes Regionais | 0.10 | 8 (0.8) | 9 (0.9) | 7 (0.7) |
| **Pontuação Ponderada Final** | **1.00** | **7.95** | **7.25** | **7.25** |

**Resultado:** **Campos dos Goytacazes** venceu a avaliação devido ao menor custo imobiliário e excelente oferta de engenheiros formados pelo IFF/UENF!

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart LR
    Crit[Critérios: Energia, Custo, Pessoal, Impostos] --> Weights[Atribuição de Pesos Ponderados w_i]
    Weights --> Eval[Avaliação das Cidades Candidatas]
    Eval --> Score[Cálculo da Pontuação Ponderada Final]
    Score --> Pick[Decisão Ótima de Localização]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Sensibilidade das Notas** | Sempre realize uma análise de sensibilidade variando os pesos $w_i$ para verificar se a decisão é robusta ou se depende excessivamente de um único critério subjetivo. | Apresente cenários alternativos. |
| **Capacidade Nominal vs Efetiva** | Capacidade Nominal é o máximo teórico ininterrupto (24/7 sem paradas); Capacidade Efetiva considera paradas programadas de manutenção e eficiência operacional real ($\sim 85\%$). | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Aplique o método do ponto ponderado para escolher o fornecedor de nuvem ótimo (AWS, Azure, GCP) considerando custo, latência, suporte e conformidade com LGPD.
2. Explique como a Curva de Aprendizagem de $80\%$ reduz o tempo de montagem de servidores em lote.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-02-estudo-de-viabilidade-tecnico-economica-evte-e-analise-de-mercado">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-04-engenharia-do-projeto-balanco-de-materiais-e-layout-operacional">Próxima Aula</a></b></div>
</div>
