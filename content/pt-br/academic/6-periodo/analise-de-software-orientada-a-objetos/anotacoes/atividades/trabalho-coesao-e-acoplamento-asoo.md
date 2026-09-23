---
publish: false
title: Trabalho - Coesão e Acoplamento em Análise Orientada a Objetos
created: 2026-09-07 16:53
modified: 2026-09-22 22:41
encrypted: true
tags:
- atividade
- trabalho
- engenharia-de-computacao
cssclasses:
- page-layout
- center-titles
- center-images
icon: lucide-book-open
---

# Trabalho - Coesão e Acoplamento em Análise de Software (ASOO)

> [!abstract] Resumo da Apresentação
> Estudo analítico e prático dos princípios de **Alta Coesão** e **Baixo Acoplamento** na engenharia de software. O trabalho aborda as definições teóricas e métricas formais (como LCOM e CBO), explica a dinâmica oposta e complementar desses dois atributos de qualidade, e faz uma conexão direta com os paradigmas de linguagens de programação (Estruturado, Orientado a Objetos e Funcional).

> [!info]  Informações & Checklist do Trabalho
> - **Docente:** Pablo Manhães
> - **Data Prevista:** 02/09/2026
> - **Apresentadores:** Amanda do Carmo de Moraes, Pedro Henrique Rocha de Andrade
> - [x]  Apresentar Trabalho: Coesão e Acoplamento

> [!important]  Acesso e Senha dos Arquivos
> Os materiais gerados na pasta `04-recursos/livros-e-apostilas/engenharia/` e espelhados no Quartz Site são protegidos pela senha:
> **`eng232`**

---

## Recursos & Materiais da Disciplina

<div class="progress-bar-container" style="background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 8px; padding: 12px 16px; margin: 1.5rem 0;">
  <div style="font-weight: 600; font-size: 0.85rem; color: var(--dark, #334155); margin-bottom: 6px;">Progresso das Aulas da Disciplina</div>
  <div style="background: var(--lightgray, #e2e8f0); border-radius: 4px; overflow: hidden; height: 8px;">
    <div style="background: var(--secondary, #6d28d9); width: 10%; height: 100%;"></div>
  </div>
</div>

---

## Sumário Interativo
- [[-1-o-que-são-coesão-e-acoplamento| 1. O que são Coesão e Acoplamento?]]
- [[-2-a-relação-oposta-e-o-equilíbrio-de-design| 2. A Relação Oposta e o Equilíbrio de Design]]
- [[-3-paradigmas-de-linguagens-de-programação| 3. Paradigmas de Linguagens de Programação]]
- [[-4-coesão-e-acoplamento-como-métricas-lcom-e-cbo| 4. Coesão e Acoplamento como Métricas (LCOM e CBO)]]
- [[-5-conclusões| 5. Conclusões]]
- [[-referências-bibliográficas| Referências Bibliográficas]]
---
## . O que são Coesão e Acoplamento?

* **Coesão:** Mede a afinidade e o foco interno de um módulo (classe ou função). Um componente coeso faz **apenas uma coisa** de forma dedicada, sem misturar assuntos.
* **Acoplamento:** Mede a dependência externa de um módulo em relação a outros. Quanto mais conexões, chamadas ou dados compartilhados um módulo possui com o mundo exterior, mais acoplado ele está.

> [!tip] Meta de Melhoria Arquitetural
> Em **Análise de Software Orientada a Objetos**, nosso objetivo principal é obter **Alta Coesão** (dentro do módulo) e **Baixo Acoplamento** (entre módulos).

---

## . A Relação Oposta e o Equilíbrio de Design
Coesão e acoplamento atuam em direções opostas e complementares de complexidade:
- **O Extremo do Zero Acoplamento:** Se tentarmos zerar o acoplamento colocando todo o código em uma única classe gigantesca (para que ela não dependa de mais ninguém), a coesão cai a zero, pois a classe passa a fazer tudo (*God Class*).
- **O Extremo da Alta Coesão Sem Controle:** Se criarmos classes minúsculas contendo apenas um método cada para maximizar a coesão, teremos que conectá-las extensivamente para resolver regras de negócio simples, fazendo o acoplamento explodir.
- **O Equilíbrio:** Bons designs equilibram os dois atributos. A coesão nos diz como agrupar funcionalidades internamente, e o acoplamento nos diz como gerenciar a comunicação entre esses grupos de forma segura.

---

## . Paradigmas de Linguagens de Programação
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

## . Coesão e Acoplamento como Métricas (LCOM e CBO)
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

## . Conclusões
- Coesão e acoplamento andam de mãos dadas: a busca por alta coesão e baixo acoplamento é o objetivo que guia refatorações e padrões de projeto (GRASP e GoF).
- Entender como esses atributos se comportam nos diferentes paradigmas nos permite escolher a melhor abordagem arquitetural dependendo da linguagem e do domínio do problema.

---

## Referências Bibliográficas
- 1. LARMAN, Craig. *Utilizando UML e Padrões*. 3. ed. Porto Alegre: Bookman, 2007.
- 2. CHIDAMBER, S. R.; KEMERER, C. F. *A Metrics Suite for Object Oriented Design*. IEEE Transactions on Software Engineering, v. 20, n. 6, 1994.
- 3. MARTIN, Robert C. *Clean Architecture*. Prentice Hall, 2017.
