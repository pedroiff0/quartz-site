---
publish: false
title: Aula 02 - Mapas de Karnough
created: 2026-08-31 17:02
modified: 2026-09-19 13:18
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

# Aula 02 - Mapas de Karnough

> [!info]- Informações & Checklist da Aula
> - **Data da Aula:** 31/08/2026
> - **Status de Revisão:**
>   - [x] Anotações em sala de aula
>   - [x] Revisão e fixação de conceitos
>   - [x] Resolução de exercícios recomendados
>   - [ ] Destilação para [[07-permanente/notas-permanentes|Notas Permanentes]]

---

## Anotações do Quadro & Conteúdo

### Mapas de Karnough

> Simplificação de Expressões Boleanas
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.122]*

### Variáveis

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | 0         | 1     |
| ${A}$     | 2         | 3     |

$$S= \bar{A}\bar{B} + \bar{A}B + A\bar{B} + AB$$
* $\bar{A}\bar{B}$ = Caso 0, ambos são 0 na tabela verdade
* $\bar{A}{B}$ = Caso 1, A = 0; B = 1 na tabela verdae
* ${A}\bar{B}$ = Caso 2, A = 1; B = 0 na tabela verdade
* ${A}{B}$ = Caso 3, ambos são 1 na tabela verdade

|  A  |  B  |
| :-: | :-: |
|  0  |  0  |
|  0  |  1  |
|  1  |  0  |
|  1  |  1  |
### Caso : Quádrupla

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | ==1==     | ==1== |
| ${A}$     | ==1==     | ==1== |
$$S' = 1$$

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.125]*

### Caso : Dupla

$$S= A\bar{B} + AB$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | 0         | 0     |
| ${A}$     | ==1==     | ==1== |
$$S'= A$$ Sempre deixar oq é comum entre si, nesse caso A; B variou. 

### Caso : Dupla Inverso

$$S= \bar{A}\bar{B} + \bar{A}B$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | ==1==     | ==1== |
| ${A}$     | 0         | 0     |
$$S'= \bar{A}$$
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.126]*

### Caso : Dupla Lateral
$$S= \bar{A}{B} + {A}B$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | 0         | ==1== |
| ${A}$     | 0         | ==1== |
$$S'= {B}$$

### Caso : Dupla Inversa

$$S= \bar{A}\bar{B} + {A}\bar{B}$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | ==1==     | 0     |
| ${A}$     | ==1==     | 0     |
$$S'= \bar{B}$$

### Caso : Termos Isolados
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.126]*


### Caso : Se todas forem , então $S=$

|  A  |  B  | S   |
| :-: | :-: | --- |
|  0  |  0  | 0   |
|  0  |  1  | 1   |
|  1  |  0  | 1   |
|  1  |  1  | 1   |

### Variáveis
$$S= \bar{A}B + A\bar{B} + AB$$

| Caso |  A  |  B  | C   |
| :--: | :-: | :-: | --- |
|  0   |  0  |  0  | 0   |
|  1   |  0  |  0  | 1   |
|  2   |  0  |  1  | 0   |
|  3   |  0  |  1  | 1   |
|  4   |  1  |  0  | 0   |
|  5   |  1  |  0  | 1   |
|  6   |  1  |  1  | 0   |
|  7   |  1  |  1  | 1   |

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 0         | 1         | 3     | 2         |
| ${A}$     | 4         | 5         | 7     | 6         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.130]*

### Caso : Oitava
| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 1         | 1         | 1     | 1         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+{A}\bar{B}\bar{C}+{A}\bar{B}{C} + \bar{A}{B}{C} + {A}{B}{C} + \bar{A}{B}\bar{C} + {A}{B}\bar{C}$$
$$S'= 1$$
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.131]*

### Caso : Quadra Superior

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 0         | 0         | 0     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+\bar{A}{B}{C}+\bar{A}{B}\bar{C}$$
$$S'= \bar{A}$$
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.132]*

### Caso : Quadra Lateral

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 0     | 0         |
| ${A}$     | 1         | 1         | 0     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+{A}\bar{B}\bar{C}+{A}\bar{B}{C}$$
$$S'= \bar{B}$$
### Caso : Quadras

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 0         |
| ${A}$     | 1         | 1         | 1     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+{A}\bar{B}\bar{C}+{A}\bar{B}{C} + \bar{A}{B}{C} + {A}{B}{C}$$
$$S'= \bar{B} + C$$
### Caso : Pares

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 1         | 1         | 1     | 1         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=$$
$$S'=$$
### Caso : Isolados

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 1         | 1         | 1     | 1         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=$$
$$S'=$$
### Exemplo do livro
| Caso |  A  |  B  | C   | S   | Min termos |
| :--: | :-: | :-: | --- | --- | ---------- |
|  0   |  0  |  0  | 0   | 0   |            |
|  1   |  0  |  0  | 1   | 1   | S=1        |
|  2   |  0  |  1  | 0   | 0   |            |
|  3   |  0  |  1  | 1   | 1   | S=         |
|  4   |  1  |  0  | 0   | 1   | S=         |
|  5   |  1  |  0  | 1   | 1   | S=         |
|  6   |  1  |  1  | 0   | 1   | S=         |
|  7   |  1  |  1  | 1   | 0   |            |

Extração “Mintermos”: 
$$S=\bar{A}\bar{B}C + \bar{A}BC + A\bar{B}\bar{C} + A\bar{B}C + AB\bar{C}$$

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 0         | 1         | 3     | 2         |
| ${A}$     | 4         | 5         | 7     | 6         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 0         | ==1==     | ==1== | 0         |
| ${A}$     | ==1==     | ==1==     | 0     | ==1==     |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
|           |           |           |       |           |

$$S= \bar{A}\bar{B}C + \bar{A}BC + A\bar{B}\bar{C} + A\bar{B}C + AB\bar{C}$$
$$S'=\bar{A}C + A\bar{B} + A\bar{C}$$

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.134]*


> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.133]*


### Variáveis

| Caso |  A  |  B  | C   | D   |
| :--: | :-: | :-: | --- | --- |
|  0   |  0  |  0  | 0   | 0   |
|  1   |  0  |  0  | 0   | 1   |
|  2   |  0  |  0  | 1   | 0   |
|  3   |  0  |  0  | 1   | 1   |
|  4   |  0  |  1  | 0   | 0   |
|  5   |  0  |  1  | 0   | 1   |
|  6   |  0  |  1  | 1   | 0   |
|  7   |  0  |  1  | 1   | 1   |
|  8   |  1  |  0  | 0   | 0   |
|  9   |  1  |  0  | 0   | 1   |
|  10  |  1  |  0  | 1   | 0   |
|  11  |  1  |  0  | 1   | 1   |
|  12  |  1  |  1  | 0   | 0   |
|  13  |  1  |  1  | 0   | 1   |
|  14  |  1  |  1  | 1   | 0   |
|  15  |  1  |  1  | 1   | 1   |

| Casos     | $\bar{C}$ | $\bar{C}$ | ${C}$ | ${C}$     | Casos     |
| --------- | --------- | --------- | ----- | --------- | --------- |
| $\bar{A}$ | 0         | 1         | 3     | 2         | $\bar{B}$ |
| $\bar{A}$ | 4         | 5         | 7     | 6         | ${B}$     |
| ${A}$     | 12        | 13        | 15    | 14        | ${B}$     |
| ${A}$     | 8         | 9         | 11    | 10        | $\bar{B}$ |
| Casos     | $\bar{D}$ | $D$       | $D$   | $\bar{D}$ | Casos     |

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.136]*

### Caso : Hexas

Tudo é 1, logo S = 1


### Caso : Oitavas

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.139]*

### Caso : Quadras
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.139]*

### Caso : Pares
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.138]*


---

> [!abstract]- Resumo Conceitual
> - **Conceito Central:** Mapas de Karnough como método de simplificação de expressões booleanas
> - **Fórmulas / Algoritmos Relevantes:** Agrupamento de 1s (pares, quartetos, óctetos)
> - **Pegadinhas / Atenção em Provas:** Decorar padrões para 2, 3 e 4 variáveis

---

## Esquemas & Anotações Visuais (excalidraw)
<!-- No iPad: insira desenhos com 'excalidraw: Create and embed new drawing' para desenhar com Apple Pencil -->

---

> [!question]- Dúvidas & Exercícios Recomendados
> - [ ] Lista de Exercícios de Mapas de Karnough
