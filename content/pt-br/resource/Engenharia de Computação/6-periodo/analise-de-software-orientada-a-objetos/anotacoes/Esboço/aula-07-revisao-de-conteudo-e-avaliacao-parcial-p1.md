---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-07-revisao-de-conteudo-e-avaliacao-parcial-p1
title: "Aula 07: Revisão de Conteúdo e Avaliação Parcial P1 — Análise de Software Orientada a Objetos"
created: 2026-10-14T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-07
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Análise de Software Orientada a Objetos"
professor: "Bruno"
conteudo: "Avaliação formal e consolidação prática de modelagem de requisitos, classes e diagramas de interação."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-06-diagramas-de-atividades-e-maquinas-de-estados">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-08-principios-de-atribuicao-de-responsabilidades-grasp">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Análise de Software Orientada a Objetos (CSECBJI.42)
> - **Professor:** Bruno
> - **Data Realizada:** 14/10/2026
> - **Tópico Principal:** Revisão de Conteúdo e Avaliação Parcial P1
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** 
> - 🎥 **Short Lecture / Gravação:** [[video-07-analise-de-software-orientada-a-objetos|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Revisão de Conteúdo e Avaliação Parcial P1](#-anotações-do-quadro-revisão-de-conteúdo-e-avaliação-parcial-p1)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Revisão de Conteúdo e Avaliação Parcial P1

### 7.1 Síntese Conceitual para Avaliação Parcial P1
Revisão da Modelagem de Análise e Requisitos com UML:
1. **Engenharia de Requisitos:** Classificação FURPS+ e requisitos não-funcionais mensuráveis.
2. **Processo Unificado:** Fases (Iniciação, Elaboração, Construção, Transição) e características iterativas.
3. **Diagramas de Casos de Uso:** Atores, casos de uso, `<<include>>`, `<<extend>>` e especificações textuais expandidas.
4. **Diagramas Estruturais de Classes:** Visibilidade, multiplicidade, herança, agregação e composição.
5. **Modelagem Comportamental:** Diagramas de Sequência (mensagens, alt, loop) e Diagramas de Atividades com partições.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Resolução de Estudo de Caso de Prova P1: Sistema de Locadora de Veículos

**Enunciado de Prova:**
Modele o caso de uso 'Locar Veículo', apresentando:
1. O Diagrama de Casos de Uso com `<<include>>` para 'Verificar CNH do Cliente' e `<<extend>>` para 'Contratar Seguro Adicional'.
2. O Diagrama de Classes de Domínio com `Locacao`, `Cliente`, `Veiculo` e `Seguro`.
3. O Diagrama de Sequência de Sistema para o fluxo principal de locação.

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart TD
    P1[Prova P1: Análise de Software OO] --> Q1[Engenharia de Requisitos e RUP: 25 pts]
    P1 --> Q2[Diagrama de Casos de Uso e Especificação: 35 pts]
    P1 --> Q3[Diagrama de Classes e Sequência: 40 pts]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Checklist de Prova P1** | 1. Não misture classes de interface visual no modelo de domínio; 2. Confira as setas de include e extend; 3. Especifique os tipos de retorno e parâmetros nas operações das classes. | Apresente diagramas limpos e legíveis. |
| **Composição vs Agregação** | Se a destruição do objeto Pai destruir os filhos, use losango preto! | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Revise todos os estudos de caso das listas 1 a 6.
2. Refaça a modelagem completa de um sistema de streaming de música (playlists, faixas, artistas e assinaturas).

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-06-diagramas-de-atividades-e-maquinas-de-estados">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-08-principios-de-atribuicao-de-responsabilidades-grasp">Próxima Aula</a></b></div>
</div>
