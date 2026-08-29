---
publish: true
title: "Trabalho - Coesão e Acoplamento em Análise Orientada a Objetos"
subtitle: "Estudo dos Princípios GRASP e Métricas CK em Sistemas Orientados a Objetos"
discipline: "Análise de Software Orientada a Objetos"
period: "6-periodo"
professor:
date: 2026-08-29
authors:
  - Pedro Henrique Rocha de Andrade
  - Ana Cecília Soja
  - Maria Luiza Dantas
corresponding_author: "Pedro Henrique Rocha de Andrade <pedroiff0@gmail.com>"
presenter: "Pedro Henrique Rocha de Andrade"
encrypted: true
password: "eng232"
tags:
  - disciplina
  - engenharia-de-computacao
  - trabalho
  - apresentacao
  - analise-de-software
  - coesao-acoplamento
draft: false
cssclasses:
  - page-layout
modified: 2026-08-29 11:39
---

# 🎓 Trabalho - Coesão e Acoplamento em Análise de Software

> [!abstract] Resumo da Apresentação
> Estudo analítico e prático dos princípios de **Alta Coesão** e **Baixo Acoplamento** no desenvolvimento orientado a objetos, investigando o impacto desses atributos de qualidade na manutenibilidade, extensibilidade e modularidade de arquiteturas de software modernas.

> [!important] 🔒 Acesso e Senha dos Arquivos
> Os materiais gerados na pasta `_materiais/` e espelhados no Quartz Site são protegidos pela senha canônica:
> **`eng232`**

---

## 📂 Recursos & Materiais da Disciplina

| Aula / Conteúdo | Data |
| :--- | :---: |
| [[Trabalho - Coesão e Acoplamento\|Trabalho - Coesão e Acoplamento em Análise Orientada a Objetos]] | 29/08/2026 |

> [!info] 🛠️ Guia de Edição dos Materiais & Slides
> - **O que alterar no Dataview:** Substitua `roteiro_iff_disciplina.pdf`, `slides_iff_disciplina.pdf` e `slides_iff_disciplina_preto.pdf` pelos nomes exatos dos PDFs gerados no seu projeto.
> - **O que cada arquivo representa na apresentação:**
>   - **Roteiro (PDF):** Texto base / relatório do trabalho técnico.
>   - **Slide Claro (PDF):** Slides compilados em LaTeX Beamer com fundo claro para exibição em auditórios e salas de aula.
>   - **Slide Escuro (PDF):** Slides compilados em LaTeX Beamer com fundo escuro para ambientes com iluminação reduzida / telas de alto contraste.
> - **Diretório dos PDFs:** Salve os arquivos em `pt-br/resource/Engenharia de Computação/_materiais/<periodo>/<disciplina>/`.

---

## 📋 Sumário Interativo
- [🎯 1. Introdução & Contextualização](#-1-introdução--contextualização)
- [⚙️ 2. Metodologia & Desenvolvimento](#-2-metodologia--desenvolvimento)
- [📈 3. Resultados & Discussão](#-3-resultados--discussão)
- [🏁 4. Conclusões](#-4-conclusões)
- [📚 5. Referências Bibliográficas](#-5-referências-bibliográficas)

---

## 🎯 1. Introdução & Contextualização
- **Conceitos Fundamentais:** Definição formal de coesão (grau de responsabilidade unívoca de um módulo) e acoplamento (grau de dependência entre módulos).
- **Problemática Abordada:** O surgimento de "God Classes", efeitos colaterais em cascata e complexidade ciclomática elevada em sistemas mal arquitetados.
- **Objetivos:** Demonstrar como padrões GRASP e SOLID auxiliam na obtenção de designs sustentáveis e desacoplados.

---

## ⚙️ 2. Metodologia & Desenvolvimento
- **Ferramentas Utilizadas:** Modelagem UML estrutural (Diagrama de Classes) e análise estática de código.
- **Etapas Práticas:**
  1. Identificação de *code smells* e classes hipertrofiadas em projetos Java/Python.
  2. Aplicação de refatorações orientadas a padrões (e.g. *Extract Class*, *Inversion of Control*).
  3. Comparação de métricas CK (*Chidamber & Kemerer*) antes e depois da reestruturação.

---

## 📈 3. Resultados & Discussão
- **Análise dos Dados:** Redução drástica nas métricas CBO (*Coupling Between Objects*) e aumento no LCOM (*Lack of Cohesion in Methods*).
- **Validação com a Teoria:** Confirmação empírica de que módulos coesos facilitam a cobertura de testes unitários e a substituição polimórfica.

---

## 🏁 4. Conclusões
- **Síntese:** Coesão e acoplamento não são apenas métricas acadêmicas, mas pilares que determinam o custo de ciclo de vida do software.
- **Próximos Passos:** Extensão para arquiteturas baseadas em microsserviços e mensageria assíncrona.

---

## 📚 5. Referências Bibliográficas
- 1. LARMAN, Craig. *Utilizando UML e Padrões: Uma Introdução à Análise e ao Projeto Orientados a Objetos e ao Desenvolvimento Iterativo*. 3. ed. Porto Alegre: Bookman, 2007.
- 2. CHIDAMBER, Shyam R.; KEMERER, Chris F. *A Metrics Suite for Object Oriented Design*. IEEE Transactions on Software Engineering, v. 20, n. 6, p. 476-493, 1994.
- 3. MARTIN, Robert C. *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall, 2017.
