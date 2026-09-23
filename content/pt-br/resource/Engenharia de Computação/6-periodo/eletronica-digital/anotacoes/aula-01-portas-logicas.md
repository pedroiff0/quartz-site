---
publish: false
title: Aula 01 - Portas Lógicas
created: 2026-08-24 14:50
modified: 2026-09-22 22:41
encrypted: true
tags:
- aula
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---

<div class="progress-bar-container" style="background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 8px; padding: 12px 16px; margin: 1.5rem 0;">
  <div style="font-weight: 600; font-size: 0.85rem; color: var(--dark, #334155); margin-bottom: 6px;">Progresso das Aulas da Disciplina</div>
  <div style="background: var(--lightgray, #e2e8f0); border-radius: 4px; overflow: hidden; height: 8px;">
    <div style="background: var(--secondary, #6d28d9); width: 10%; height: 100%;"></div>
  </div>
</div>

# Aula 01 - Portas Lógicas

> [!info]- Informações & Checklist da Aula
> - **Docente:** Fabrício Barros Gonçalves
> - **Data da Aula:** 24/08/2026
> - **Status de Revisão:**
>   - [x] Anotações em sala de aula
>   - [x] Revisão e fixação de conceitos
>   - [x] Resolução de exercícios recomendados
>   - [ ] Destilação para [[07-permanente/notas-permanentes|Notas Permanentes]]

---

## Anotações do Quadro & Conteúdo

### Revisão de Lógica para Computação & Fundamentação Teórica

Nesta aula de **Eletrônica Digital**, estudamos a transição da lógica matemática/proposicional para o ambiente de hardware por meio dos blocos lógicos fundamentais (portas lógicas).

---

### . NÃO (NOT - Inversor)

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

### . E (AND - Conjunção)

A porta **AND** gera saída alta ($1$) se e somente se todas as suas entradas forem altas ($1$).

```mermaid
flowchart LR
    A[A] & B[B] -->|AND| S[S = A · B]
```

**Expressão Booleana:**
$$S = A \cdot B$$

**Tabela-Verdade:**

|  A  |  B  |  S  |     |
| :-: | :-: | :-: | --- |
|  0  |  0  |  0  |     |
|  0  |  1  |  0  |     |
|  1  |  0  |  0  |     |
|  1  |  1  |  1  |     |

---

### . OU (OR - Disjunção)

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

### . OU EXCLUSIVO (XOR)

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

### . NÃO E (NAND - Porta Universal)

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

### . NÃO OU (NOR - Porta Universal)

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

### . NÃO OU EXCLUSIVO (XNOR - Coincidência)

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

### Mintermos e Maxtermos

1. **Mintermos (Soma de Produtos - SOP):**
   - Correspondem às combinações da tabela-verdade onde a saída do circuito é $1$.
   - Representados pela notação $\sum m$.
   - ==Na forma de mintermos, a variável direta vale $1$ e a variável complementada/barrada vale $0$.==

2. **Maxtermos (Produto de Somas - POS):**
   - Correspondem às combinações da tabela-verdade onde a saída do circuito é $0$.
   - Representados pela notação $\prod M$.
   - Na forma de maxtermos, a variável direta vale $0$ e a variável complementada/barrada vale $1$.

---

### Exemplo do Quadro: Diagrama de Trilhos e Portas Lógicas para ABC

Abaixo está o circuito completo com barramento/trilhos de sinal ($A, B, C$) e seus respectivos inversores (NOT), alimentando os mintermos e maxtermos e conectando à porta principal de saída ao final da expressão:

### . Circuito Mintermo (SOP): $S = \bar{A} B C + A \bar{B} C + A B \bar{C}$

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

### . Circuito Maxtermo (POS): $S = (A + B + C) \cdot (\bar{A} + B + \bar{C}) \cdot (A + \bar{B} + C)$

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

### . Leitura e Síntese de Expressão Complexa do Quadro

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

## Esquemas & Anotações Visuais (excalidraw)
<!-- No iPad: insira desenhos com 'excalidraw: Create and embed new drawing' para desenhar com Apple Pencil -->

---

> [!question]- Dúvidas & Exercícios Recomendados
> - [x] Testar os circuitos das 7 portas no simulador LogiSim
> - [ ] Resolver a Lista de Exercícios de Notação Correta
> - [ ] Desenhar o circuito de mintermos para a função $S(A,B,C) = \sum m(1, 4, 7)$ utilizando os trilhos A, B, C
