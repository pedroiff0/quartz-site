---
publish: true
title: Trabalho - Normalização e Dependências Funcionais
subtitle: Teoria Relacional e Decomposição em 1FN, 2FN e 3FN (Caso Centro de Memória)
discipline: Banco de Dados
period: 6-periodo
professor: Pablo Manhães
date: 2026-09-02
status: concluido
authors:
  - Arthur de Oliveira Lima Potente
  - Breno Luiz Silva do Carmo
  - Isaac Salles Gonçalves
  - Pedro Henrique Rocha de Andrade
corresponding_author: Pedro Henrique Rocha de Andrade <pedroiff0@gmail.com>
presenter: Pedro Henrique Rocha de Andrade
short_title: Normalização & FN
encrypted: true
password: eng232
disciplina_url: https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/banco-de-dados/
trabalho_url: https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/banco-de-dados/anotacoes/atividades/trabalho---normalizacao-e-dependencias-funcionais/
roteiro_pdf: roteiro_bd2026.md
slides_latex_claro: slides_bd2026_branco.pdf
slides_latex_escuro: slides_bd2026_preto.pdf
portal_institucional: https://portal1.iff.edu.br/
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
  - center-images
  - center-titles
modified: 2026-09-01T14:38:09-03:00
---

# 🎓 Trabalho - Normalização e Dependências Funcionais em Banco de Dados

> [!abstract] Resumo Executivo da Apresentação
> Este trabalho apresenta o estudo formal e aplicado do processo de **Normalização de Esquemas Relacionais**, utilizando a teoria das **Dependências Funcionais (DFs)** como alicerce matemático. Demonstra-se, a partir de um cenário não-normalizado de **Centro de Memória** (acervo, doações e exposições), a transição sistemática da **Forma Não-Normalizada (0FN)** para a **1FN**, **2FN** e **3FN**, eliminando anomalias de inserção, atualização e exclusão, com garantia formal de *Junção sem Perdas (Lossless Join)* e *Preservação de Dependências*.

> [!info] 📌 Informações & Checklist do Trabalho
> - **Docente:** Pablo Manhães
> - **Data de Apresentação:** 02/09/2026
> - **Autores / Equipe:** Arthur de Oliveira Lima Potente, Breno Luiz Silva do Carmo, Isaac Salles Gonçalves, Pedro Henrique Rocha de Andrade
> - **Status da Atividade:** Apresentado
> - [x] 🎯 Apresentar Trabalho: Normalização e Dependências Funcionais

> [!important] 🔒 Acesso e Senha dos Arquivos
> Os materiais gerados na pasta `_materiais/` e espelhados no Quartz Site são protegidos pela senha canônica:
> **`eng232`**

---

## 📂 Recursos & Materiais da Disciplina

```dataviewjs
const c = dv.current();
const filePath = c.file?.path || "";
const parts = filePath.split("/");
const periodIndex = parts.findIndex(p => p.toLowerCase().includes("periodo") || p.toLowerCase().includes("período"));
const period = c.period || (periodIndex !== -1 ? parts[periodIndex] : "6-periodo");
const disciplineFolder = (periodIndex !== -1 && parts.length > periodIndex + 1) ? parts[periodIndex + 1] : "banco-de-dados";

let matPath = "02 - Áreas/Acadêmico/IFF - Engenharia de Computação/_materiais";
if (period && disciplineFolder && disciplineFolder !== "Anotações" && disciplineFolder !== "Atividades") {
    matPath += `/${period}/${disciplineFolder}`;
} else if (period) {
    matPath += `/${period}`;
}

const roteiroFile = c.roteiro_pdf || "roteiro_bd2026.md";
const slidesClaroFile = c.slides_latex_claro || "slides_bd2026_branco.pdf";
const slidesEscuroFile = c.slides_latex_escuro || "slides_bd2026_preto.pdf";
const hubEngcomp = "https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/";
const discHubUrl = c.disciplina_url || (disciplineFolder ? `${hubEngcomp}${period}/${disciplineFolder}/` : hubEngcomp);
const portalUrl = c.portal_institucional || "https://portal1.iff.edu.br/";

dv.paragraph(`> [!tip] 🔗 Links e Materiais Vinculados (Automático da Disciplina)
> - 📑 **Roteiro & Documento Técnico:** [[${matPath}/${roteiroFile}|${roteiroFile}]] *(Roteiro completo da apresentação)*
> - 📊 **Slides LaTeX (PDF Claro):** [[${matPath}/${slidesClaroFile}|${slidesClaroFile}]] *(Apresentação Beamer - Modo Claro)*
> - 📊 **Slides LaTeX (PDF Escuro):** [[${matPath}/${slidesEscuroFile}|${slidesEscuroFile}]] *(Apresentação Beamer - Modo Noturno)*
> - 🌐 **Hub da Disciplina:** [Acessar Hub no Quartz](${discHubUrl}) *(Link ao clicar na Disciplina no cabeçalho dos slides)*
> - 🏛️ **Portal Institucional IFF:** [portal1.iff.edu.br](${portalUrl}) *(Portal institucional)*`);
```

---

## 📋 Sumário Interativo
- [🎯 1. Conceitos & Dependências Funcionais](#-1-conceitos--dependências-funcionais)
- [🔍 2. O Cenário Não-Normalizado: Centro de Memória (0FN)](#-2-o-cenário-não-normalizado-centro-de-memória-0fn)
- [📐 3. Normalização Passo a Passo: 1FN, 2FN e 3FN](#-3-normalização-passo-a-passo-1fn-2fn-e-3fn)
- [📈 4. Esquema Final, Garantias Formais & Conclusões](#-4-esquema-final-garantias-formais--conclusões)
- [📚 5. Referências Bibliográficas](#-5-referências-bibliográficas)

---

## 🎯 1. Conceitos & Dependências Funcionais

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

## 🔍 2. O Cenário Não-Normalizado: Centro de Memória (0FN)

Para ilustrar o processo completo de forma direta e compreensível em uma apresentação de 10 minutos, examinamos o sistema de um **Centro de Memória** que gerencia acervo, doações e exposições:

### 2.1 A Relação Universal Não-Normalizada (0FN)
Suponha uma tabela única `ACERVO_COMPLETO` que registra itens do acervo, doações recebidas e exposições realizadas:

$$\text{Tabela}( \underline{\text{cod\_tombo}}, \underline{\text{cod\_exposicao}}, \text{titulo}, \text{descricao}, \text{data\_aquisicao}, \text{cod\_doacao}, \text{data\_doacao}, \text{termo}, \text{id\_doador}, \text{nome\_doador}, \text{cpf\_doador}, \text{email\_doador}, \text{codigo\_exposicao}, \text{titulo\_exposicao}, \text{data\_inicio}, \text{data\_fim}, \text{posicao}, \text{palavras\_chave} )$$

| cod_tombo | titulo | descricao | cod_doacao | nome_doador | cpf_doador | email_doador | codigo_exposicao | titulo_exposicao | posicao | palavras_chave |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :--- | :---: | :--- |
| **T001** | Foto BJ | Foto aérea 1940 | **D01** | Maria Silva | 111.222.333-44 | maria@email.com | **E01** | Memória Urbana | 1 | foto, história, urbano |
| **T001** | Foto BJ | Foto aérea 1940 | **D01** | Maria Silva | 111.222.333-44 | maria@email.com | **E02** | Raízes Rurais | 3 | foto, história, rural |
| **T002** | Cartão Postal | Cartão 1920 | **D02** | João Santos | 555.666.777-88 | joao@email.com | **E01** | Memória Urbana | 2 | cartão, postal, antiguidade |
| **T003** | Jornal 1950 | Edição rara | **D03** | Ana Costa | 999.888.777-66 | ana@email.com | **E02** | Raízes Rurais | 1 | jornal, raro, preservação |

### 2.2 Diagnóstico das Anomalias Práticas
1. **Anomalia de Inserção:** Não é possível cadastrar um novo doador sem que ele tenha doado um item do acervo. O doador só "existe" se houver doação.
2. **Anomalia de Exclusão:** Se a exposição `E01` for cancelada e as linhas forem apagadas, **perdemos o registro de que Maria Silva doou o item T001**, pois ela só estava vinculada àquela exposição!
3. **Anomalia de Atualização:** Os dados do doador (nome, cpf, email) estão replicados em múltiplas linhas. Se o email de Maria mudar, todas as linhas devem ser atualizadas; se uma linha falhar, o banco entra em estado inconsistente.

---

## 📐 3. Normalização Passo a Passo: 1FN, 2FN e 3FN

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
Analisando as regras de negócio do cenário Centro de Memória:

1. **$\text{DF}_1$ (Chave Composta $\to$ Atributo da Exposição):**
   $$\{ \text{cod\_tombo}, \text{codigo\_exposicao} \} \to \text{posicao}$$
2. **$\text{DF}_2$ (Dependência Parcial do Item):**
   $$\text{cod\_tombo} \to \{ \text{titulo}, \text{descricao}, \text{data\_aquisicao}, \text{cod\_doacao} \}$$
3. **$\text{DF}_3$ (Dependência Parcial da Exposição):**
   $$\text{codigo\_exposicao} \to \{ \text{titulo\_exposicao}, \text{data\_inicio}, \text{data\_fim} \}$$
4. **$\text{DF}_4$ (Dependência Transitiva da Doação):**
   $$\text{cod\_doacao} \to \{ \text{data\_doacao}, \text{termo}, \text{id\_doador} \}$$
5. **$\text{DF}_5$ (Dependência Transitiva do Doador):**
   $$\text{id\_doador} \to \{ \text{nome\_doador}, \text{cpf\_doador}, \text{email\_doador} \}$$
6. **$\text{DF}_6$ (Palavras-chave do Item):**
   $$\{ \text{cod\_tombo}, \text{palavra\_chave} \} \quad (\text{Relação muitos-para-muitos})$$

---

### 3.2 Passo 1: Transição para a 1ª Forma Normal (1FN)

> [!tip] Regra da 1FN
> Uma relação $R$ está na **1FN** se e somente se todos os domínios subjacentes de seus atributos contêm apenas **valores atômicos (indivisíveis)** e não existem atributos multivalorados ou grupos repetitivos.

#### Problema Identificado:
O atributo `palavras_chave` contém múltiplos valores em uma mesma célula (e.g. `"foto, história, urbano"`).

#### Solução:
Isolar o atributo multivalorado em uma tabela associativa atômica `ITEM_PALAVRACHAVE`:

$$\text{ITEM\_PALAVRACHAVE}( \underline{\text{cod\_tombo}}, \underline{\text{palavra\_chave}} )$$

A tabela principal agora possui apenas valores atômicos, com chave primária composta:

$$\text{R\_1FN}( \underline{\text{cod\_tombo}}, \underline{\text{codigo\_exposicao}}, \text{titulo}, \text{descricao}, \text{data\_aquisicao}, \text{cod\_doacao}, \text{data\_doacao}, \text{termo}, \text{id\_doador}, \text{nome\_doador}, \text{cpf\_doador}, \text{email\_doador}, \text{titulo\_exposicao}, \text{data\_inicio}, \text{data\_fim}, \text{posicao} )$$

---

### 3.3 Passo 2: Transição para a 2ª Forma Normal (2FN)

> [!tip] Regra da 2FN
> Uma relação $R$ está na **2FN** se e somente se:
> 1. Está na **1FN**;
> 2. **Nenhum atributo não-primo é dependente parcial de qualquer chave candidata composta de $R$**. Todo atributo não-primo deve depender da totalidade de cada chave primária.

#### Problema Identificado:
A chave primária de `R_1FN` é composta: $\{ \text{cod\_tombo}, \text{codigo\_exposicao} \}$.
- $\text{DF}_2: \text{cod\_tombo} \to \{ \text{titulo}, \text{descricao}, \text{data\_aquisicao}, \text{cod\_doacao} \}$ $\implies$ Dependência Parcial!
- $\text{DF}_3: \text{codigo\_exposicao} \to \{ \text{titulo\_exposicao}, \text{data\_inicio}, \text{data\_fim} \}$ $\implies$ Dependência Parcial!

#### Solução (Decomposição em 2FN):
Criamos relações separadas para cada determinante parcial:

1. **`ITEM_ACERVO`** (elimina a dependência parcial de `cod_tombo`):
   $$\text{ITEM\_ACERVO}( \underline{\text{cod\_tombo}}, \text{titulo}, \text{descricao}, \text{data\_aquisicao}, \text{cod\_doacao} )$$
   *Chave Estrangeira:* `cod_doacao REFERENCES DOACAO`

2. **`EXPOSICAO`** (elimina a dependência parcial de `codigo_exposicao`):
   $$\text{EXPOSICAO}( \underline{\text{codigo\_exposicao}}, \text{titulo\_exposicao}, \text{data\_inicio}, \text{data\_fim} )$$

3. **`ITEM_EXPOSICAO`** (mantém apenas atributos totalmente dependentes da chave composta):
   $$\text{ITEM\_EXPOSICAO}( \underline{\text{cod\_tombo}}, \underline{\text{codigo\_exposicao}}, \text{posicao} )$$
   *Chaves Estrangeiras:* `cod_tombo REFERENCES ITEM_ACERVO`, `codigo_exposicao REFERENCES EXPOSICAO`

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
Na tabela `ITEM_ACERVO`, a chave primária é $\text{cod\_tombo}$.
Temos a cadeia transitiva:

$$\text{cod\_tombo} \xrightarrow{\text{DF}_2} \text{cod\_doacao} \xrightarrow{\text{DF}_4} \{ \text{data\_doacao}, \text{termo}, \text{id\_doador} \} \xrightarrow{\text{DF}_5} \{ \text{nome\_doador}, \text{cpf\_doador}, \text{email\_doador} \}$$

Como $\text{cod\_doacao}$ **não é uma superchave** de `ITEM_ACERVO` e os atributos de doação/doador não são atributos primos, temos uma violação explícita da 3FN.

#### Solução (Decomposição em 3FN):
Extraímos a relação de doação e doador para suas próprias tabelas:

1. **`DOACAO`:**
   $$\text{DOACAO}( \underline{\text{cod\_doacao}}, \text{data\_doacao}, \text{termo}, \text{id\_doador} )$$
   *Chave Estrangeira:* `id_doador REFERENCES PESSOA`

2. **`PESSOA`:**
   $$\text{PESSOA}( \underline{\text{id\_doador}}, \text{nome\_doador}, \text{cpf\_doador}, \text{email\_doador} )$$

3. **`ITEM_ACERVO`** (mantém apenas a chave estrangeira para doação):
   $$\text{ITEM\_ACERVO}( \underline{\text{cod\_tombo}}, \text{titulo}, \text{descricao}, \text{data\_aquisicao}, \text{cod\_doacao} )$$
   *Chave Estrangeira:* `cod_doacao REFERENCES DOACAO`

---

## 📈 4. Esquema Final, Garantias Formais & Conclusões

### 4.1 O Esquema Relacional Final Normalizado (3FN)

O banco de dados final é composto por **6 relações especializadas e desacopladas**:

```
 ┌────────────────────────┐             ┌────────────────────────┐
 │       PESSOA           │             │       EXPOSICAO        │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 id_doador (PK)      │             │ 🔑 codigo_exposicao(PK)│
 │    nome_doador         │             │    titulo_exposicao    │
 │    cpf_doador          │             │    data_inicio         │
 │    email_doador        │             │    data_fim            │
 └───────────▲────────────┘             └───────────▲────────────┘
             │ (1:N)                                │ (1:N)
             │                                      │
 ┌───────────┴────────────┐             ┌───────────┴────────────┐
 │       DOACAO           │             │    ITEM_EXPOSICAO      │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 cod_doacao (PK)     │             │ 🔑 cod_tombo (PK, FK)  │
 │    data_doacao         │             │ 🔑 codigo_exposicao    │
 │    termo               │             │       (PK, FK)         │
 │ 🔗 id_doador (FK)      │             │    posicao             │
 └───────────▲────────────┘             └───────────┬────────────┘
             │ (1:N)                                │ (N:1)
             │                                      │
 ┌───────────┴────────────┐             ┌───────────▼────────────┐
 │     ITEM_ACERVO        │             │  ITEM_PALAVRACHAVE     │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 cod_tombo (PK)      │             │ 🔑 cod_tombo (PK, FK)  │
 │    titulo              │             │ 🔑 palavra_chave (PK)  │
 │    descricao           │             └────────────────────────┘
 │    data_aquisicao      │
 │ 🔗 cod_doacao (FK)     │
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

| Métrica / Critério                 |          Esquema 0FN (Tabela Única)           |                 Esquema 3FN (Normalizado)                 |
| :--------------------------------- | :-------------------------------------------: | :-------------------------------------------------------: |
| **Redundância de Dados**           |  Alta (nomes de doadores repetidos)           |      Nula (cada fato armazenado exatamente uma vez)       |
| **Anomalias de Inserção/Exclusão** | Críticas (impossível cadastrar doador isolado) |          Inexistentes (entidades independentes)           |
| **Integridade dos Dados**          |   Frágil (risco de divergência de strings)    |        Máxima (garantida por chaves estrangeiras)         |
| **Desempenho de Leitura Simples**  | Rápido (sem `JOIN`, mas com leitura de lixo)  | Exige `JOIN`, mas usa índices $B\text{-Tree}$ de inteiros |
| **Desempenho de Escrita/Update**   |      Lento (múltiplas linhas alteradas)       |      Instantâneo (alteração atômica em linha única)       |

---

## 📚 5. Referências Bibliográficas
- 1. ELMASRI, Ramez; NAVATHE, Shamkant B. *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson, 2018.
- 2. SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. *Sistema de Banco de Dados*. 6. ed. Rio de Janeiro: Elsevier, 2012.
- 3. CODD, Edgar F. *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM, v. 13, n. 6, p. 377-387, 1970.
- 4. DATE, C. J. *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier, 2004.
- 5. IBM. *Database Normalization: Guia Prático*. IBM Think Topics, 2024.
