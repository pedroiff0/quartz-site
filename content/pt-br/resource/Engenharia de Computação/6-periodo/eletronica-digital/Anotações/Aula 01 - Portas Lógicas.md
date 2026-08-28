---
publish: true
title: Aula 01 - Portas Lógicas
created: 2026-08-24 14:50
modified: 2026-08-27 22:29
encrypted: true
tags:
  - aula
  - engenharia-de-computacao
  - anotacoes-de-quadro
discipline: Eletrônica Digital
professor: Fabrício Barros Gonçalves
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Tópico Central:** Portas Lógicas & Álgebra Booleana
> - **Status das Anotações:** 🟢 Concluído

> [!note] 📦 Material Didático & Recursos da Aula
> - 📄 **[Lista de Exercícios de Notação Correta em PDF](/assets/disciplinas/6-periodo/eletronica-digital/Lista_Eletronica_Digital_Notacao_Correta.pdf)**
> - 📖 **[Livro Texto de Apoio (Capuano & Idoeta)](/assets/disciplinas/6-periodo/eletronica-digital/ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf)**
> - 💻 **[Simulador LogiSim (Executável JAR)](/assets/disciplinas/6-periodo/eletronica-digital/logisim-generic-2.7.1.jar)**

## 📋 Sumário Interativo
- [📍 Anotações](#-anotações)
- [🧠 Resumo](#-resumo)
- [📝 Dúvida](#-dúvida)

---

## 📍 Anotações

### 📐 Revisão de Lógica para Computação & Fundamentação Teórica

Nesta aula de **Eletrônica Digital**, estudamos a transição da lógica matemática/proposicional para o ambiente de hardware por meio dos blocos lógicos fundamentais (portas lógicas).

---

### 1. NÃO (NOT - Inversor)

A porta **NOT** realiza a operação lógica de inversão ou complemento.

```mermaid
flowchart LR
    A[Entrada: A] -->|NOT| S[Saída: S = Ā]
```

**Expressão Booleana:**
$$S = \bar{A}$$

**Tabela-Verdade:**

| A | S |
| :---: | :---: |
| 0 | 1 |
| 1 | 0 |

---

### 2. E (AND - Conjunção)

A porta **AND** gera saída alta ($1$) se e somente se todas as suas entradas forem altas ($1$).

```mermaid
flowchart LR
    A[A] & B[B] -->|AND| S[S = A · B]
```

**Expressão Booleana:**
$$S = A \cdot B$$

**Tabela-Verdade:**

| A | B | S |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

### 3. OU (OR - Disjunção)

A porta **OR** gera saída alta ($1$) quando pelo menos uma das suas entradas for alta ($1$).

```mermaid
flowchart LR
    A[A] & B[B] -->|OR| S[S = A + B]
```

**Expressão Booleana:**
$$S = A + B$$

**Tabela-Verdade:**

| A | B | S |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

---

### 4. OU EXCLUSIVO (XOR)

A porta **XOR** (Ou-Exclusivo) produz saída alta ($1$) se e somente se as entradas forem **diferentes**.

```mermaid
flowchart LR
    A[A] & B[B] -->|XOR| S[S = A ⊕ B]
```

**Expressão Booleana:**
$$S = A \oplus B = \bar{A}B + A\bar{B}$$

**Tabela-Verdade:**

| A | B | S |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

### 5. NÃO E (NAND - Porta Universal)

A porta **NAND** é a negação da saída da porta AND. É uma porta **universal**, pois qualquer circuito combinacional pode ser construído apenas com portas NAND.

```mermaid
flowchart LR
    A[A] & B[B] -->|NAND| S[S = Ā·B]
```

**Expressão Booleana:**
$$S = \overline{A \cdot B}$$

**Tabela-Verdade:**

| A | B | S |
| :---: | :---: | :---: |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---

### 6. NÃO OU (NOR - Porta Universal)

A porta **NOR** é a negação da porta OR. Também possui caráter de **universalidade**.

```mermaid
flowchart LR
    A[A] & B[B] -->|NOR| S[S = Ā+B]
```

**Expressão Booleana:**
$$S = \overline{A + B}$$

**Tabela-Verdade:**

| A | B | S |
| :---: | :---: | :---: |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

---

### 7. NÃO OU EXCLUSIVO (XNOR - Coincidência)

A porta **XNOR** gera saída alta ($1$) quando as entradas forem **iguais** (coincidência).

```mermaid
flowchart LR
    A[A] & B[B] -->|XNOR| S[S = A ⊙ B]
```

**Expressão Booleana:**
$$S = \overline{A \oplus B} = A B + \bar{A}\bar{B}$$

**Tabela-Verdade:**

| A | B | S |
| :---: | :---: | :---: |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

---

### 🧮 Mintermos e Maxtermos

1. **Mintermos (Soma de Produtos - SOP):**
   - Correspondem às combinações da tabela-verdade onde a saída do circuito é $1$.
   - Representados pela notação $\sum m$.
   - Na forma de mintermos, a variável direta vale $1$ e a variável complementada/barrada vale $0$.

2. **Maxtermos (Produto de Somas - POS):**
   - Correspondem às combinações da tabela-verdade onde a saída do circuito é $0$.
   - Representados pela notação $\prod M$.
   - Na forma de maxtermos, a variável direta vale $0$ e a variável complementada/barrada vale $1$.

---

### 📖 Exemplo do Quadro: Diagrama de Trilhos e Portas Lógicas para ABC

Abaixo está o circuito completo com barramento/trilhos de sinal ($A, B, C$) e seus respectivos inversores (NOT), alimentando os mintermos e maxtermos e conectando à porta principal de saída ao final da expressão:

#### 1. Circuito Mintermo (SOP): $S = \bar{A} B C + A \bar{B} C + A B \bar{C}$

```mermaid
flowchart LR
    subgraph Trilhos ["Barramento de Entradas"]
        A["Trilho A"]
        B["Trilho B"]
        C["Trilho C"]
        NOT_A["NOT A (Ā)"]
        NOT_B["NOT B (B̄)"]
        NOT_C["NOT C (C̄)"]
        A --> NOT_A
        B --> NOT_B
        C --> NOT_C
    end

    subgraph Mintermos ["Portas de Produto (AND)"]
        m1["AND m1 (Ā·B·C)"]
        m2["AND m2 (A·B̄·C)"]
        m3["AND m3 (A·B·C̄)"]
    end

    NOT_A & B & C --> m1
    A & NOT_B & C --> m2
    A & B & NOT_C --> m3

    subgraph Estagio_Final ["Porta Principal de Saída"]
        OR_FINAL["Porta OR Principal (Soma)"]
    end

    m1 & m2 & m3 --> OR_FINAL
    OR_FINAL --> SAIDA["Saída S (SOP)"]
```

---

#### 2. Circuito Maxtermo (POS): $S = (A + B + C) \cdot (\bar{A} + B + \bar{C}) \cdot (A + \bar{B} + C)$

```mermaid
flowchart LR
    subgraph Trilhos ["Barramento de Entradas"]
        A["Trilho A"]
        B["Trilho B"]
        C["Trilho C"]
        NOT_A["NOT A (Ā)"]
        NOT_B["NOT B (B̄)"]
        NOT_C["NOT C (C̄)"]
        A --> NOT_A
        B --> NOT_B
        C --> NOT_C
    end

    subgraph Maxtermos ["Portas de Soma (OR)"]
        M0["OR M0 (A + B + C)"]
        M5["OR M5 (Ā + B + C̄)"]
        M2["OR M2 (A + B̄ + C)"]
    end

    A & B & C --> M0
    NOT_A & B & NOT_C --> M5
    A & NOT_B & C --> M2

    subgraph Estagio_Final ["Porta Principal de Saída"]
        AND_FINAL["Porta AND Principal (Produto)"]
    end

    M0 & M5 & M2 --> AND_FINAL
    AND_FINAL --> SAIDA["Saída S (POS)"]
```

---

#### 3. Leitura e Síntese de Expressão Complexa do Quadro

$$S = (A + B + C) \cdot \left\{ B \left[ (A + C) + \overline{B \cdot C} \right] \cdot (\bar{A} \cdot B \cdot \bar{C}) \right\}$$

```mermaid
flowchart LR
    subgraph Trilhos ["Barramento de Entradas"]
        TA["Trilho A"]
        TB["Trilho B"]
        TC["Trilho C"]
        T_N_A["NOT A (Ā)"]
        T_N_B["NOT B (B̄)"]
        T_N_C["NOT C (C̄)"]
        TA --> T_N_A
        TB --> T_N_B
        TC --> T_N_C
    end

    subgraph Estagio1 ["Estágio 1 - Termos Internos"]
        OR_ABC["OR 1: (A + B + C)"]
        OR_AC["OR 2: (A + C)"]
        NAND_BC["NAND: NOT(B·C)"]
        AND_ABC_BAR["AND: (Ā · B · C̄)"]
    end

    TA & TB & TC --> OR_ABC
    TA & TC --> OR_AC
    TB & TC --> NAND_BC
    T_N_A & TB & T_N_C --> AND_ABC_BAR

    subgraph Estagio2 ["Estágio 2 - Combinação Intermediária"]
        OR_SUB["OR 3: [(A+C) + NOT(B·C)]"]
    end

    OR_AC & NAND_BC --> OR_SUB

    subgraph Estagio3 ["Estágio 3 - Bloco Interno"]
        AND_BLOCO["AND 2: B · [OR 3] · [AND Ā·B·C̄]"]
    end

    TB & OR_SUB & AND_ABC_BAR --> AND_BLOCO

    subgraph Estagio_Saida ["Porta Principal de Saída"]
        AND_SAIDA["Porta AND Principal"]
    end

    OR_ABC & AND_BLOCO --> AND_SAIDA
    AND_SAIDA --> S_OUT["Saída Final S"]
```

---

## 🧠 Resumo

| Tópico | Princípio Central | Atenção Especial / Pegadinha |
| :--- | :--- | :--- |
| **Mintermos ($\sum m$)** | Agrupa as saídas $1$ da tabela | Variáveis sem barra correspondem a $1$ |
| **Maxtermos ($\prod M$)** | Agrupa as saídas $0$ da tabela | Variáveis sem barra correspondem a $0$ |
| **Universalidade NAND/NOR** | Implementa qualquer circuito lógico | Atenção às inversões duplas ao aplicar De Morgan |
| **Diagrama de Trilhos** | Conecta barramentos A, B, C | Passar por portas NOT antes dos blocos AND/OR |

> [!tip] 💡 Dica de Prova do Professor Fabrício
> Em avaliações e no laboratório, dê preferência a trabalhar com **mintermos ($\sum m$)**, pois simplifica a conversão para circuitos AND-OR e facilita a montagem dos diagramas de trilho no **LogiSim**!

---

## 📝 Dúvidas & Exercícios Recomendados

- [x] Testar os circuitos das 7 portas no simulador LogiSim (`logisim-generic-2.7.1.jar`).
- [ ] Resolver a [Lista de Exercícios de Notação Correta em PDF](/assets/disciplinas/6-periodo/eletronica-digital/Lista_Eletronica_Digital_Notacao_Correta.pdf).
- [ ] Desenhar o circuito de mintermos para a função $S(A,B,C) = \sum m(1, 4, 7)$ utilizando os trilhos A, B, C.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>
