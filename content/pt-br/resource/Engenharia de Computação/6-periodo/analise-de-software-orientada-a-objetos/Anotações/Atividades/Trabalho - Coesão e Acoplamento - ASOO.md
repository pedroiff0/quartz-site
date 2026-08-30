---
publish: true
title: Trabalho - Coesão e Acoplamento em Análise Orientada a Objetos
subtitle: Estudo dos Níveis de Coesão, Princípios GRASP, Paradigmas e Métricas CK
discipline: Análise de Software Orientada a Objetos
period: 6-periodo
professor: Pablo Manhães
date: 02/09/2026
status: concluído
authors:
  - Amanda Moraes
  - Pedro Henrique Rocha de Andrade
corresponding_author: Pedro Henrique Rocha de Andrade <pedroiff0@gmail.com>
presenter: Pedro Henrique Rocha de Andrade
short_title: Coesão & Acoplamento
encrypted: true
password: eng232
disciplina_url: https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/analise-de-software-orientada-a-objetos/
trabalho_url: https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/atividades/trabalho---coesao-e-acoplamento-asoo/
roteiro_pdf: roteiro_iff_asoo.pdf
slides_latex_claro: slides_iff_asoo.pdf
slides_latex_escuro: slides_iff_asoo_preto.pdf
portal_institucional: https://portal1.iff.edu.br/
tags:
  - disciplina
  - engenharia-de-computacao
  - trabalho
  - apresentacao
  - atividade
  - analise-de-software
  - coesao
  - acoplamento
draft: false
cssclasses:
  - page-layout
  - center-titles
  - center-images
modified: 2026-08-29 13:30
---

# 🎓 Trabalho - Coesão e Acoplamento em Análise de Software (ASOO)

> [!abstract] Resumo da Apresentação
> Estudo analítico e prático dos princípios de **Alta Coesão** e **Baixo Acoplamento** na engenharia de software. O trabalho aborda as definições teóricas e métricas formais (como LCOM e CBO), explica a dinâmica oposta e complementar desses dois atributos de qualidade, e faz uma conexão direta com os paradigmas de linguagens de programação (Estruturado, Orientado a Objetos e Funcional).

> [!info] 📌 Informações & Checklist do Trabalho
> - **Docente:** Pablo Manhães
> - **Data Prevista:** 02/09/2026
> - **Apresentadores:** Amanda Moraes, Pedro Henrique Rocha de Andrade
> - [x] Definir Coesão e Acoplamento
> - [x] Explicar a relação oposta e complementar (trade-off)
> - [x] Detalhar como métricas quantificáveis (LCOM e CBO)
> - [x] Conectar com paradigmas de linguagens (Estruturado, OO e Funcional)
> - [x] Compilar materiais pelo pipeline unificado

> [!important] 🔒 Acesso e Senha dos Arquivos
> Os materiais gerados na pasta `_materiais/` e espelhados no Quartz Site são protegidos pela senha:
> **`eng232`**

---

## 📂 Recursos & Materiais da Disciplina

> [!tip] 🔗 Arquivos e Materiais da Disciplina
> - 📄 **Slides do Docente:** *Consulte os anexos vinculados*
> - 📑 **Roteiro / Texto de Apoio:** *Consulte os materiais de aula*
> - 📦 **Exercícios / Anexos:** *Disponíveis no repositório*

---

## 📋 Sumário Interativo
- [🎯 1. O que são Coesão e Acoplamento?](#-1-o-que-são-coesão-e-acoplamento)
- [⚖️ 2. A Relação Oposta e o Equilíbrio de Design](#-2-a-relação-oposta-e-o-equilíbrio-de-design)
- [🧩 3. Paradigmas de Linguagens de Programação](#-3-paradigmas-de-linguagens-de-programação)
- [🧮 4. Coesão e Acoplamento como Métricas (LCOM e CBO)](#-4-coesão-e-acoplamento-como-métricas-lcom-e-cbo)
- [🏁 5. Conclusões](#-5-conclusões)
- [📚 Referências Bibliográficas](#-referências-bibliográficas)

---

## Anotações
Referência prinicipal: https://engsoftmoderna.info/cap5.html#coes%C3%A3o
https://engsoftmoderna.info/cap5.html#acoplamento

https://medium.com/@laurammoraesDev/acoplamento-e-coes%C3%A3o-o-que-s%C3%A3o-795bdde30ddc
https://www.devmedia.com.br/entendendo-coesao-e-acoplamento/18538

## 🎯 1. O que são Coesão e Acoplamento?

* **Coesão:** Mede a afinidade e o foco interno de um módulo (classe ou função). Um componente coeso faz **apenas uma coisa** de forma dedicada, sem misturar assuntos.
* **Acoplamento:** Mede a dependência externa de um módulo em relação a outros. Quanto mais conexões, chamadas ou dados compartilhados um módulo possui com o mundo exterior, mais acoplado ele está.

> [!tip] Meta de Melhoria Arquitetural
> Em **Análise de Software Orientada a Objetos**, nosso objetivo principal é obter **Alta Coesão** (dentro do módulo) e **Baixo Acoplamento** (entre módulos).

---

## ⚖️ 2. A Relação Oposta e o Equilíbrio de Design
Coesão e acoplamento atuam em direções opostas e complementares de complexidade:
- **O Extremo do Zero Acoplamento:** Se tentarmos zerar o acoplamento colocando todo o código em uma única classe gigantesca (para que ela não dependa de mais ninguém), a coesão cai a zero, pois a classe passa a fazer tudo (*God Class*).
- **O Extremo da Alta Coesão Sem Controle:** Se criarmos classes minúsculas contendo apenas um método cada para maximizar a coesão, teremos que conectá-las extensivamente para resolver regras de negócio simples, fazendo o acoplamento explodir.
- **O Equilíbrio:** Bons designs equilibram os dois atributos. A coesão nos diz como agrupar funcionalidades internamente, e o acoplamento nos diz como gerenciar a comunicação entre esses grupos de forma segura.

---

## 🧩 3. Paradigmas de Linguagens de Programação
A forma como lidamos com a coesão e o acoplamento varia de acordo com o paradigma adotado:

1. **Paradigma Estruturado (Procedural):**
   - **Foco:** Funções e variáveis globais.
   - **Coesão:** Uma função deve executar um único subalgoritmo (ex: ordenar vetor).
   - **Acoplamento:** Minimizado evitando o uso de variáveis globais e priorizando a passagem de parâmetros por valor.
2. **Paradigma Orientado a Objetos (OO):**
   - **Foco:** Objetos encapsulando estado (atributos) e comportamento (métodos).
   - **Coesão:** Uma classe representa um único conceito de domínio (ex: `Pedido`).
   - **Acoplamento:** Controlado através de interfaces, polimorfismo e encapsulamento, garantindo que objetos dependam de contratos estáveis e não de implementações concretas (*Inversão de Dependência*).
3. **Paradigma Funcional:**
   - **Foco:** Funções puras e imutabilidade.
   - **Coesão:** Funções matemáticas puras que recebem uma entrada e calculam uma saída única (coesão funcional máxima).
   - **Acoplamento:** Virtualmente nulo no nível de estado, pois não há estado compartilhado ou mutável. As funções são acopladas apenas pela composição de suas assinaturas de tipos.

---

## 🧮 4. Coesão e Acoplamento como Métricas (LCOM e CBO)
A qualidade do design não é apenas subjetiva; ela é medida por métricas estatísticas formais da suite CK (*Chidamber & Kemerer*):

### A. Métrica de Coesão: LCOM (*Lack of Cohesion in Methods*)
Mede o grau em que os métodos de uma classe compartilham seus atributos. 
Seja $M$ o conjunto de métodos e $A$ o conjunto de atributos de uma classe:
- $P$ é o conjunto de pares de métodos que não compartilham atributos de instância.
- $Q$ é o conjunto de pares de métodos que compartilham pelo menos um atributo.
$$LCOM = \begin{cases} |P| - |Q|, & \text{se } |P| > |Q| \\ 0, & \text{caso contrário} \end{cases}$$
* **Interpretação:** LCOM alto indica falta de coesão (módulos desconexos) $\rightarrow$ *Code Smell*.

### B. Métrica de Acoplamento: CBO (*Coupling Between Objects*)
Mede a quantidade de outras classes que estão acopladas a uma determinada classe (por herança, tipos de parâmetros, variáveis locais ou chamadas de métodos).
* **Interpretação:** CBO alto significa que a classe depende de muitas outras ou que muitas outras dependem dela, tornando-a frágil e difícil de alterar sem causar quebras em cascata. Devemos manter o CBO baixo.

---

## 🏁 5. Conclusões
- Coesão e acoplamento andam de mãos dadas: a busca por alta coesão e baixo acoplamento é o objetivo que guia refatorações e padrões de projeto (GRASP e GoF).
- Entender como esses atributos se comportam nos diferentes paradigmas nos permite escolher a melhor abordagem arquitetural dependendo da linguagem e do domínio do problema.

---

## 📚 Referências Bibliográficas
- 1. LARMAN, Craig. *Utilizando UML e Padrões*. 3. ed. Porto Alegre: Bookman, 2007.
- 2. CHIDAMBER, S. R.; KEMERER, C. F. *A Metrics Suite for Object Oriented Design*. IEEE Transactions on Software Engineering, v. 20, n. 6, 1994.
- 3. MARTIN, Robert C. *Clean Architecture*. Prentice Hall, 2017.
