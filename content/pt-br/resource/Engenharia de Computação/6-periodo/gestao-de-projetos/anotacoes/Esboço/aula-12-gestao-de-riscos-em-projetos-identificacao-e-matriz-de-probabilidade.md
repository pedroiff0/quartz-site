---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-12-gestao-de-riscos-em-projetos-identificacao-e-matriz-de-probabilidade
title: "Aula 12: Gestão de Riscos em Projetos: Identificação e Matriz de Probabilidade — Gestão de Projetos"
created: 2026-11-19T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-12
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Gestão de Projetos"
professor: "Hilton"
conteudo: "Identificação de riscos, análise qualitativa (Matriz de Impacto e Probabilidade), plano de resposta (mitigar, aceitar, transferir, evitar)."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-11-avaliacao-economica-avancada-valor-presente-liquido-vpl-e-taxa-interna-de-retorno-tir">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-13-gerenciamento-de-aquisicoes-contratos-e-comunicacao">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Gestão de Projetos (CSECBJI.49)
> - **Professor:** Hilton
> - **Data Realizada:** 19/11/2026
> - **Tópico Principal:** Gestão de Riscos em Projetos: Identificação e Matriz de Probabilidade
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-12-gestao-de-projetos|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-12-gestao-de-projetos|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Gestão de Riscos em Projetos: Identificação e Matriz de Probabilidade](#-anotações-do-quadro-gestão-de-riscos-em-projetos-identificação-e-matriz-de-probabilidade)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Gestão de Riscos em Projetos: Identificação e Matriz de Probabilidade

### 12.1 Gestão de Riscos em Projetos (PMBOK)
O gerenciamento de riscos visa aumentar a probabilidade e o impacto de eventos positivos (oportunidades) e diminuir a probabilidade e o impacto de eventos adversos (ameaças).

### 12.2 Estrutura Analítica de Riscos (EAR / RBS)
Decomposição hierárquica das fontes potenciais de risco do projeto:
- **Riscos Técnicos:** Complexidade tecnológica, novidade da arquitetura, bugs em bibliotecas de terceiros, falhas de segurança.
- **Riscos de Gestão:** Estimativas irreais, falhas de comunicação, rotatividade da equipe (*Turnover*).
- **Riscos Comerciais:** Variação cambial (dólar em servidores), quebra de fornecedores, alteração de leis (LGPD).
- **Riscos Externos:** Pandemias, intempéries climáticas, crises energéticas.

### 12.3 Análise Qualitativa de Riscos e a Matriz $P \times I$
Atribui-se para cada risco identificado uma pontuação de **Probabilidade ($P$)** e **Impacto ($I$)** de 1 a 5:
$$\text{Severidade do Risco} = P \times I \quad (1 \text{ a } 25)$$
Riscos na zona vermelha ($\ge 15$) exigem plano de resposta formal obrigatório.

### 12.4 Estratégias de Resposta a Ameaças
1. **Prevenir / Evitar (*Avoid*):** Eliminar a ameaça alterando o plano do projeto (ex: trocar tecnologia imatura por estável).
2. **Transferir (*Transfer*):** Repassar o impacto financeiro a terceiros (ex: contratar apólice de seguro ou terceirizar com SLA).
3. **Mitigar (*Mitigate*):** Ações preventivas para reduzir a probabilidade ou o impacto do risco (ex: criar protótipos prévios, redundância).
4. **Aceitar (*Accept*):** Reconhecer o risco e criar uma reserva de contingência financeira/tempo sem ação preventiva ativa.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Matriz de Riscos de Projeto de Sistema Embarcado

| ID | Descrição do Risco | Categoria | $P$ (1-5) | $I$ (1-5) | Severidade ($P \times I$) | Estratégia de Resposta | Plano de Ação Prático |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **R1** | Falta de componentes microcontroladores no mercado global | Comercial | 4 | 5 | **20 (Crítico)** | **Mitigar / Evitar** | Comprar lote de segurança antecipado e homologar CI alternativo pin-compatible. |
| **R2** | Demissão do desenvolvedor sênior de firmware | Gestão | 3 | 4 | **12 (Médio)** | **Mitigar** | Pair programming contínuo, documentação diária de código e testes automatizados. |
| **R3** | Alta do dólar encarecer licenças de nuvem | Comercial | 4 | 3 | **12 (Médio)** | **Transferir / Mitigar** | Contrato de hedge cambial ou contratação de servidores nacionais com fatura em reais. |
| **R4** | Atraso de 2 dias na entrega de cabos | Técnico | 2 | 1 | **2 (Baixo)** | **Aceitar** | Absorver o atraso na folga livre do cronograma. |

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
quadrantChart
    title Matriz de Probabilidade e Impacto (P x I)
    x-axis Baixo Impacto --> Alto Impacto
    y-axis Baixa Probabilidade --> Alta Probabilidade
    quadrant-1 Ameaças Críticas (Mitigar Imediatamente)
    quadrant-2 Riscos de Alta Atenção
    quadrant-3 Riscos Menores (Monitorar)
    quadrant-4 Riscos de Contingência
    "Falta de Chips": [0.9, 0.8]
    "Turnover de Dev": [0.7, 0.6]
    "Alta do Dólar": [0.6, 0.7]
    "Atraso de Cabos": [0.2, 0.3]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Reserva de Contingência vs Reserva Gerencial** | A **Reserva de Contingência** cobre riscos identificados conhecidos (*Known-Unknowns*); a **Reserva Gerencial** cobre imprevistos e emergências não-mapeados (*Unknown-Unknowns*). | Ambas devem constar no orçamento global. |
| **Riscos Positivos (Oportunidades)** | Oportunidades também devem ser gerenciadas via estratégias: Explorar, Compartilhar, Melhorar e Aceitar. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Construa o Registro de Riscos completo com Matriz $P 	imes I$ para o lançamento de um aplicativo de pagamentos via blockchain.
2. Diferencie as estratégias de Mitigação e Transferência de risco com exemplos na área de segurança da informação.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-11-avaliacao-economica-avancada-valor-presente-liquido-vpl-e-taxa-interna-de-retorno-tir">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos/anotacoes/aula-13-gerenciamento-de-aquisicoes-contratos-e-comunicacao">Próxima Aula</a></b></div>
</div>
