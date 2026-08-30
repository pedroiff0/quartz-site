---
publish: true
title: "Trabalho - Normalização e Dependências Funcionais"
subtitle: "Fundamentação Matemática das Dependências Funcionais e Decomposição em 1FN, 2FN e 3FN"
discipline: "Banco de Dados"
period: "6-periodo"
professor: "Pablo Manhães"
date: 29/08/2026
status: planejando
authors:
  - Breno Luiz
  - Isaac Salles
  - Pedro Henrique Rocha de Andrade
corresponding_author: "Pedro Henrique Rocha de Andrade <pedroiff0@gmail.com>"
presenter: "Pedro Henrique Rocha de Andrade"
short_title: "Normalização & FN"
encrypted: true
password: "eng232"

# 🔗 Links e Materiais do Trabalho & Slides (LaTeX / Quartz)
disciplina_url: "https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/banco-de-dados/"
trabalho_url: "https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/banco-de-dados/anotacoes/atividades/trabalho---normalizacao-e-dependencias-funcionais/"
roteiro_pdf: "roteiro_iff_disciplina.pdf"
slides_latex_claro: "slides_iff_disciplina.pdf"
slides_latex_escuro: "slides_iff_disciplina_preto.pdf"
portal_institucional: "https://portal1.iff.edu.br/"

tags:
  - disciplina
  - engenharia-de-computacao
  - trabalho
  - apresentacao
  - atividade
  - banco-de-dados
  - normalizacao
  - dependencias-funcionais
draft: false
cssclasses:
  - page-layout
modified: 2026-08-29 13:36
---

# 🎓 Trabalho - Normalização e Dependências Funcionais em Banco de Dados

> [!abstract] Resumo Executivo da Apresentação
> Este trabalho apresenta o estudo formal e aplicado do processo de **Normalização de Esquemas Relacionais**, utilizando a teoria das **Dependências Funcionais (DFs)** como alicerce matemático. Demonstra-se, a partir de um cenário não-normalizado de **Gestão de Projetos e Alocação de Engenharia**, a transição sistemática da **Forma Não-Normalizada (0FN)** para a **1FN**, **2FN** e **3FN** (com considerações sobre BCNF), eliminando anomalias de inserção, atualização e exclusão, com garantia formal de *Junção sem Perdas (Lossless Join)* e *Preservação de Dependências*.

> [!info] 📌 Informações & Checklist do Trabalho
> - **Docente:** Pablo Manhães
> - **Data Prevista:** 29/08/2026
> - **Apresentador:** Pedro Henrique Rocha de Andrade
> - **Autores / Equipe:** Breno Luiz, Isaac Salles e Pedro Henrique Rocha de Andrade
> - **Status da Atividade:** 🟡 `Planejando` *(Status no frontmatter: `status: planejando`)*
> - [ ] 🎯 Apresentar Trabalho: Normalização e Dependências Funcionais

> [!important] 🔒 Acesso e Senha dos Arquivos
> Os materiais gerados na pasta `_materiais/` e espelhados no Quartz Site são protegidos pela senha canônica:
> **`eng232`**

---

## 📂 Recursos & Materiais da Disciplina

> [!tip] 🔗 Arquivos e Materiais da Disciplina
> - 📄 **Slides do Docente:** *Consulte os anexos vinculados*
> - 📑 **Roteiro / Texto de Apoio:** *Consulte os materiais de aula*
> - 📦 **Exercícios / Anexos:** *Disponíveis no repositório*

> [!info] 🛠️ Guia das Propriedades de Links e Apresentação
> - **`disciplina_url`**: URL aberta ao clicar no **Nome da Disciplina** no cabeçalho superior dos slides.
> - **`trabalho_url`**: URL aberta ao clicar no **"Seminário \| `short_title`"** ou no **título do rodapé** dos slides, levando ao endereço público deste `.md` no Quartz.
> - **`short_title`**: Título curto exibido no cabeçalho dos slides (ao lado de `Nome da Disciplina | ...`).
> - **`roteiro_pdf`**: Nome do PDF do relatório em `_materiais/`, linkado no rodapé do card de figura lateral nos slides.
> - **`slides_latex_claro` & `slides_latex_escuro`**: Nomes dos PDFs dos slides Beamer (claro e noturno).
> - **QR Code (Encerramento):** Redireciona para o portal principal de **Engenharia de Computação** (`phrandrade.com/disciplinas`).

---

## 📋 Sumário Interativo
- [🎯 1. Fundamentos & Motivação Teórica](#-1-fundamentos--motivação-teórica)
- [🔍 2. O Cenário Não-Normalizado: Um Caso Prático de Engenharia](#-2-o-cenário-não-normalizado-um-caso-prático-de-engenharia)
- [📐 3. Dependências Funcionais & O Processo de Normalização Passo a Passo](#-3-dependências-funcionais--o-processo-de-normalização-passo-a-passo)
- [📈 4. Comparativo de Esquemas, Garantias Formais & Conclusões](#-4-comparativo-de-esquemas-garantias-formais--conclusões)
- [📚 5. Referências Bibliográficas](#-5-referências-bibliográficas)

---

## Anotações

Referencia: https://www.ibm.com/br-pt/think/topics/database-normalization
https://medium.com/@celionormando/depend%C3%AAncias-funcionais-e-normaliza%C3%A7%C3%A3o-9098c3ac9c33
https://www.datacamp.com/pt/tutorial/normalization-in-dbms

## 🎯 1. Fundamentos & Motivação Teórica

### 1.1 O Papel da Teoria Relacional
O modelo relacional clássico proposto por **Edgar F. Codd (1970)** fundamenta o armazenamento e a recuperação de dados em conceitos matemáticos de conjuntos e lógica de predicados de primeira ordem. Em um ambiente operacional, esquemas relacionais mal projetados sofrem de três patologias graves decorrentes da **redundância de dados**:

```
                  ┌───────────────────────────────────────────┐
                  │          PATOLOGIAS DE ESQUEMA            │
                  ├───────────────────────────────────────────┤
                  │ 1. Anomalia de Inserção                   │
                  │    Impossibilidade de inserir dados de    │
                  │    uma entidade sem criar dados de outra  │
                  │ ───────────────────────────────────────── │
                  │ 2. Anomalia de Exclusão                   │
                  │    A exclusão de uma tupla acarreta a     │
                  │    perda colateral de informações vitais  │
                  │ ───────────────────────────────────────── │
                  │ 3. Anomalia de Atualização                │
                  │    Alteração de um dado exige múltiplos   │
                  │    updates em tuplas redundantes; falha   │
                  │    gera inconsistência interna do SGBD    │
                  └───────────────────────────────────────────┘
```

### 1.2 O Conceito Central: Dependência Funcional (DF)
Uma **Dependência Funcional** é uma restrição formal entre dois conjuntos de atributos $X$ e $Y$ pertencentes a uma relação $R$, denotada por:

$$X \to Y \quad \text{("X determina funcionalmente Y")}$$

Formalmente, diz-se que $X \to Y$ se e somente se, para quaisquer duas tuplas $t_1, t_2 \in R$:

$$t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$

- **Determinante:** O lado esquerdo $X$.
- **Determinado:** O lado direito $Y$.
- **Superchave:** Um conjunto de atributos $K \subseteq R$ tal que $K \to R$.
- **Chave Candidata ($CK$):** Uma superchave mínima (nenhum subconjunto próprio de $CK$ é superchave).
- **Atributo Primo:** Qualquer atributo que componha pelo menos uma chave candidata.
- **Atributo Não-Primo:** Atributo que não participa de nenhuma chave candidata.

---

## 🔍 2. O Cenário Não-Normalizado: Um Caso Prático de Engenharia

Para ilustrar o processo completo de forma direta e compreensível em uma apresentação de 10 minutos, examinamos o sistema de alocação de projetos de um laboratório de engenharia:

### 2.1 A Relação Universal Não-Normalizada (0FN)
Suponha uma tabela única `PROJETOS_ALOCACAO_UNIFICADA` que registra projetos de engenharia, funcionários alocados, seus departamentos e as linguagens/ferramentas utilizadas:

$$\text{Tabela}( \underline{\text{Num\_Proj}}, \underline{\text{Num\_Emp}}, \text{Nome\_Emp}, \text{Cargo}, \text{Num\_Depto}, \text{Nome\_Depto}, \text{Cod\_Gerente}, \text{Habilidades}, \text{Nome\_Proj}, \text{Orcamento}, \text{Horas\_Semana} )$$

| Num_Proj | Nome_Proj | Orcamento | Num_Emp | Nome_Emp | Cargo | Num_Depto | Nome_Depto | Cod_Gerente | Habilidades | Horas_Semana |
| :---: | :--- | :---: | :---: | :--- | :--- | :---: | :--- | :---: | :--- | :---: |
| **P101** | Sistema SCADA | R$ 120.000 | **E01** | Pedro Andrade | Eng. Software | **D01** | Automação | G09 | Python, C++, SQL | 20 |
| **P101** | Sistema SCADA | R$ 120.000 | **E02** | Ana Soja | Eng. Dados | **D02** | Analytics | G12 | Python, Spark | 15 |
| **P102** | Visão Térmica | R$ 85.000 | **E01** | Pedro Andrade | Eng. Software | **D01** | Automação | G09 | Python, C++, SQL | 10 |
| **P103** | Robô AGV | R$ 200.000 | **E03** | Breno Luiz | Eng. Controle | **D01** | Automação | G09 | C++, ROS, VHDL | 30 |

### 2.2 Diagnóstico das Anomalias Práticas
1. **Anomalia de Inserção:** Não é possível cadastrar um novo departamento (ex: `D03 - Robótica`) sem alocar pelo menos um projeto e um empregado ativo.
2. **Anomalia de Exclusão:** Se o projeto `P102` for cancelado e a linha for apagada, não perdemos o empregado porque ele está em `P101`. Porém, se `P103` for cancelado e sua linha excluída, **perdemos o registro de que Breno Luiz trabalha no D01**, pois ele só estava alocado naquele projeto!
3. **Anomalia de Atualização:** O gerente do departamento `D01` está replicado em 3 linhas. Se o gerente mudar, todas as linhas devem ser atualizadas; se uma linha falhar, o banco entra em estado inconsistente.

---

## 📐 3. Dependências Funcionais & O Processo de Normalização Passo a Passo

```
       [ 0FN: Tabela Universal com Listas ]
                         │
                         ▼ (Eliminar Atributos Multivalorados / Não-Atômicos)
       [ 1ª Forma Normal (1FN): Valores Atômicos ]
                         │
                         ▼ (Eliminar Dependências Parciais da Chave Composta)
       [ 2ª Forma Normal (2FN): Total Dependência da Chave ]
                         │
                         ▼ (Eliminar Dependências Transitivas entre Não-Chaves)
       [ 3ª Forma Normal (3FN): Sem Dependências Transitivas ]
```

### 3.1 Mapeamento Formal das Dependências Funcionais
Analisando as regras de negócio do cenário:

1. **$\text{DF}_1$ (Chave Composta $\to$ Atributo da Alocação):**
   $$\{ \text{Num\_Proj}, \text{Num\_Emp} \} \to \text{Horas\_Semana}$$
2. **$\text{DF}_2$ (Dependência Parcial do Projeto):**
   $$\text{Num\_Proj} \to \{ \text{Nome\_Proj}, \text{Orcamento} \}$$
3. **$\text{DF}_3$ (Dependência Parcial do Empregado):**
   $$\text{Num\_Emp} \to \{ \text{Nome\_Emp}, \text{Cargo}, \text{Num\_Depto} \}$$
4. **$\text{DF}_4$ (Dependência Transitiva do Departamento):**
   $$\text{Num\_Depto} \to \{ \text{Nome\_Depto}, \text{Cod\_Gerente} \}$$
5. **$\text{DF}_5$ (Habilidades do Empregado):**
   $$\{ \text{Num\_Emp}, \text{Habilidade} \} \quad (\text{Relação muitos-para-muitos entre Empregado e Habilidade})$$

---

### 3.2 Passo 1: Transição para a 1ª Forma Normal (1FN)

> [!tip] Regra da 1FN
> Uma relação $R$ está na **1FN** se e somente se todos os domínios subjacentes de seus atributos contêm apenas **valores atômicos (indivisíveis)** e não existem atributos multivalorados ou grupos repetitivos.

#### Problema Identificado:
O atributo `Habilidades` contém múltiplos valores em uma mesma célula (e.g. `"Python, C++, SQL"`).

#### Solução:
Isolar o atributo multivalorado em uma tabela associativa atômica `EMPREGADO_HABILIDADE`:

$$\text{EMPREGADO\_HABILIDADE}( \underline{\text{Num\_Emp}}, \underline{\text{Habilidade}} )$$

A tabela principal agora possui apenas valores atômicos, com chave primária composta:

$$\text{R\_1FN}( \underline{\text{Num\_Proj}}, \underline{\text{Num\_Emp}}, \text{Nome\_Proj}, \text{Orcamento}, \text{Nome\_Emp}, \text{Cargo}, \text{Num\_Depto}, \text{Nome\_Depto}, \text{Cod\_Gerente}, \text{Horas\_Semana} )$$

---

### 3.3 Passo 2: Transição para a 2ª Forma Normal (2FN)

> [!tip] Regra da 2FN
> Uma relação $R$ está na **2FN** se e somente se:
> 1. Está na **1FN**;
> 2. **Nenhum atributo não-primo é dependente parcial de qualquer chave candidata composta de $R$**. Todo atributo não-primo deve depender da totalidade de cada chave primária.

#### Problema Identificado:
A chave primária de `R_1FN` é composta: $\{ \text{Num\_Proj}, \text{Num\_Emp} \}$.
- $\text{DF}_2: \text{Num\_Proj} \to \{ \text{Nome\_Proj}, \text{Orcamento} \}$ $\implies$ Dependência Parcial!
- $\text{DF}_3: \text{Num\_Emp} \to \{ \text{Nome\_Emp}, \text{Cargo}, \text{Num\_Depto}, \text{Nome\_Depto}, \text{Cod\_Gerente} \}$ $\implies$ Dependência Parcial!

#### Solução (Decomposição em 2FN):
Criamos relações separadas para cada determinante parcial:

1. **`PROJETO`** (elimina a dependência parcial de `Num_Proj`):
   $$\text{PROJETO}( \underline{\text{Num\_Proj}}, \text{Nome\_Proj}, \text{Orcamento} )$$

2. **`EMPREGADO_TEMP`** (elimina a dependência parcial de `Num_Emp`):
   $$\text{EMPREGADO\_TEMP}( \underline{\text{Num\_Emp}}, \text{Nome\_Emp}, \text{Cargo}, \text{Num\_Depto}, \text{Nome\_Depto}, \text{Cod\_Gerente} )$$

3. **`ALOCACAO`** (mantém apenas atributos totalmente dependentes da chave composta):
   $$\text{ALOCACAO}( \underline{\text{Num\_Proj}}, \underline{\text{Num\_Emp}}, \text{Horas\_Semana} )$$
   *Chaves Estrangeiras:* `Num_Proj REFERENCES PROJETO`, `Num_Emp REFERENCES EMPREGADO`

---

### 3.4 Passo 3: Transição para a 3ª Forma Normal (3FN)

> [!tip] Regra da 3FN
> Uma relação $R$ está na **3FN** se e somente se:
> 1. Está na **2FN**;
> 2. **Nenhum atributo não-primo depende transitivamente da chave primária**.
>
> Em outras palavras, para toda dependência funcional não-trivial $X \to A$, deve ocorrer pelo menos uma das condições:
> - $X$ é uma superchave de $R$; **OU**
> - $A$ é um atributo primo (membro de uma chave candidata).

#### Problema Identificado:
Na tabela `EMPREGADO_TEMP`, a chave primária é $\text{Num\_Emp}$.
Temos a cadeia transitiva:

$$\text{Num\_Emp} \xrightarrow{\text{DF}_3} \text{Num\_Depto} \xrightarrow{\text{DF}_4} \{ \text{Nome\_Depto}, \text{Cod\_Gerente} \}$$

Como $\text{Num\_Depto}$ **não é uma superchave** de `EMPREGADO_TEMP` e $\{\text{Nome\_Depto}, \text{Cod\_Gerente}\}$ não são atributos primos, temos uma violação explícita da 3FN.

#### Solução (Decomposição em 3FN):
Extraímos a relação de departamento para sua própria tabela:

1. **`DEPARTAMENTO`:**
   $$\text{DEPARTAMENTO}( \underline{\text{Num\_Depto}}, \text{Nome\_Depto}, \text{Cod\_Gerente} )$$

2. **`EMPREGADO`** (mantém apenas a chave estrangeira para departamento):
   $$\text{EMPREGADO}( \underline{\text{Num\_Emp}}, \text{Nome\_Emp}, \text{Cargo}, \text{Num\_Depto} )$$
   *Chave Estrangeira:* `Num_Depto REFERENCES DEPARTAMENTO`

---

## 📈 4. Comparativo de Esquemas, Garantias Formais & Conclusões

### 4.1 O Esquema Relacional Final Normalizado (3FN / BCNF)

O banco de dados final é composto por **5 relações especializadas e desacopladas**:

```
 ┌────────────────────────┐             ┌────────────────────────┐
 │        PROJETO         │             │       DEPARTAMENTO     │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 Num_Proj (PK)       │             │ 🔑 Num_Depto (PK)      │
 │    Nome_Proj           │             │    Nome_Depto          │
 │    Orcamento           │             │    Cod_Gerente         │
 └───────────┬────────────┘             └───────────▲────────────┘
             │                                      │ (1:N)
             │ (1:N)                                │
 ┌───────────▼────────────┐             ┌───────────┴────────────┐
 │        ALOCACAO        │             │        EMPREGADO       │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 Num_Proj (PK, FK)   │ (N:1)       │ 🔑 Num_Emp (PK)        │
 │ 🔑 Num_Emp  (PK, FK)   ├─────────────►    Nome_Emp            │
 │    Horas_Semana        │             │    Cargo               │
 └────────────────────────┘             │ 🔗 Num_Depto (FK)      │
                                        └───────────▲────────────┘
                                                    │ (1:N)
                                        ┌───────────┴────────────┐
                                        │  EMPREGADO_HABILIDADE  │
                                        ├────────────────────────┤
                                        │ 🔑 Num_Emp (PK, FK)    │
                                        │ 🔑 Habilidade (PK)     │
                                        └────────────────────────┘
```

### 4.2 Garantias Matemáticas da Decomposição
A normalização não é meramente uma escolha estética de design; ela possui provas formais:

1. **Decomposição sem Perdas (*Lossless-Join Decomposition*):**
   Garante que, ao efetuar o `NATURAL JOIN` das tabelas normalizadas, o resultado é **estritamente idêntico** à tabela original, sem gerar tuplas espúrias (falsas tuplas que violariam a realidade).
   $$\Pi_{R_1}(R) \bowtie \Pi_{R_2}(R) = R \iff (R_1 \cap R_2 \to R_1) \lor (R_1 \cap R_2 \to R_2)$$

2. **Preservação de Dependências (*Dependency Preservation*):**
   Todas as dependências funcionais originais do conjunto $F$ podem ser verificadas dentro de tabelas individuais, sem necessidade de realizar `JOINs` computacionalmente caros em restrições de integridade (*CHECK constraints* / *Triggers*).

### 4.3 Tabela Comparativa de Avaliação

| Métrica / Critério | Esquema 0FN (Tabela Única) | Esquema 3FN (Normalizado) |
| :--- | :---: | :---: |
| **Redundância de Dados** | Alta (nomes de depto e gerentes repetidos) | Nula (cada fato armazenado exatamente uma vez) |
| **Anomalias de Inserção/Exclusão** | Críticas (impossível cadastrar depto isolado) | Inexistentes (entidades independentes) |
| **Integridade dos Dados** | Frágil (risco de divergência de strings) | Máxima (garantida por chaves estrangeiras) |
| **Desempenho de Leitura Simples** | Rápido (sem `JOIN`, mas com leitura de lixo) | Exige `JOIN`, mas usa índices $B\text{-Tree}$ de inteiros |
| **Desempenho de Escrita/Update** | Lento (múltiplas linhas alteradas) | Instantâneo (alteração atômica em linha única) |

---

## 📚 5. Referências Bibliográficas
- 1. ELMASRI, Ramez; NAVATHE, Shamkant B. *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson, 2018. (Capítulo 14: Teoria de Projeto de Bancos de Dados Relacionais e Dependências Funcionais; Capítulo 15: Algoritmos de Projeto de Bancos de Dados Relacionais).
- 2. SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. *Sistema de Banco de Dados*. 6. ed. Rio de Janeiro: Elsevier, 2012. (Capítulo 8: Projeto de Banco de Dados Relacional).
- 3. CODD, Edgar F. *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM, v. 13, n. 6, p. 377-387, 1970.
- 4. DATE, C. J. *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier, 2004.
