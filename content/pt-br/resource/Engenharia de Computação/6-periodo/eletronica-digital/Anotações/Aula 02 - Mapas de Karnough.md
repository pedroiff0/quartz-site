---
publish: true
title: Aula 02 - Mapas de Karnough
subtitle: ""
created: 2026-08-31 17:02
modified: 2026-08-31 19:22
discipline: ""
period: ""
professor: ""
encrypted: true
password: eng232
slides_aula: ""
roteiro_aula: ""
anexos: ""
tags:
  - aula
  - engenharia-de-computacao
  - anotacoes
cssclasses:
  - page-layout
  - center-titles
  - center-images
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="../index">Hub da Disciplina</a></b></div>
  <div>🏠 <b><a href="../index">Visão Geral</a></b></div>
  <div>➡️ <b><a href="../index">Aulas</a></b></div>
</div>

# 📝 Aula 02 - Mapas de Karnough

> [!info] 📌 Informações da Aula
> - **Docente:** 
> - **Data da Aula:** 31/08/2026
> - **Tópico Central:** 
> - **Status das Anotações:** 
>   - [x] 🟡 Planejando 
>   - [x] 🟠 Em Andamento 
>   - [ ] 🟢 Concluído

## 📂 Materiais & Recursos Didáticos da Aula

> [!tip] 🔗 Arquivos e Materiais da Disciplina
> - 📄 **Slides do Docente:** *Consulte os anexos vinculados*
> - 📑 **Roteiro / Texto de Apoio:** *Consulte os materiais de aula*
> - 📦 **Exercícios / Anexos:** *Disponíveis no repositório*

## 📋 Sumário Interativo
- [📍 Anotações](#-anotações)
- [🧠 Resumo](#-resumo)
- [📝 Dúvida](#-dúvida)

---

## 📍 Anotações

### 31/08

##### Mapas de Karnough

> Simplificação de Expressões Boleanas
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=122&rect=215,1194,472,1418|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.122]]

##### 2 Variáveis

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
###### Caso 1: Quádrupla 

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | ==1==     | ==1== |
| ${A}$     | ==1==     | ==1== |
$$S' = 1$$

![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=125&rect=176,720,1503,1304|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.125]]

###### Caso 2: Dupla

$$S= A\bar{B} + AB$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | 0         | 0     |
| ${A}$     | ==1==     | ==1== |
$$S'= A$$ Sempre deixar oq é comum entre si, nesse caso A; B variou. 

###### Caso 3: Dupla Inverso

$$S= \bar{A}\bar{B} + \bar{A}B$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | ==1==     | ==1== |
| ${A}$     | 0         | 0     |
$$S'= \bar{A}$$
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=126&rect=209,1636,1539,2233|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.126]]

###### Caso 4: Dupla Lateral
$$S= \bar{A}{B} + {A}B$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | 0         | ==1== |
| ${A}$     | 0         | ==1== |
$$S'= {B}$$

###### Caso 5: Dupla Inversa

$$S= \bar{A}\bar{B} + {A}\bar{B}$$

| Casos     | $\bar{B}$ | ${B}$ |
| --------- | --------- | ----- |
| $\bar{A}$ | ==1==     | 0     |
| ${A}$     | ==1==     | 0     |
$$S'= \bar{B}$$

###### Caso 6: Termos Isolados
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=126&rect=200,582,1543,1621|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.126]]


###### Caso 7: Se todas forem 0, então $S=0$

|  A  |  B  | S   |
| :-: | :-: | --- |
|  0  |  0  | 0   |
|  0  |  1  | 1   |
|  1  |  0  | 1   |
|  1  |  1  | 1   |

#### 3 Variáveis
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

![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=130&rect=227,1464,1347,2222|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.130]]

###### Caso 1: Oitava
| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 1         | 1         | 1     | 1         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+{A}\bar{B}\bar{C}+{A}\bar{B}{C} + \bar{A}{B}{C} + {A}{B}{C} + \bar{A}{B}\bar{C} + {A}{B}\bar{C}$$
$$S'= 1$$
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=131&rect=163,235,1500,761|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.131]]

###### Caso 2: Quadra Superior

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 0         | 0         | 0     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+\bar{A}{B}{C}+\bar{A}{B}\bar{C}$$
$$S'= \bar{A}$$
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=132&rect=192,1593,1543,2228|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.132]]

###### Caso 3: Quadra Lateral

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 0     | 0         |
| ${A}$     | 1         | 1         | 0     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+{A}\bar{B}\bar{C}+{A}\bar{B}{C}$$
$$S'= \bar{B}$$
###### Caso 4: 2 Quadras

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 0         |
| ${A}$     | 1         | 1         | 1     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=\bar{A}\bar{B}\bar{C}+\bar{A}\bar{B}{C}+{A}\bar{B}\bar{C}+{A}\bar{B}{C} + \bar{A}{B}{C} + {A}{B}{C}$$
$$S'= \bar{B} + C$$
###### Caso 5: Pares

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 1         | 1         | 1     | 1         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=$$
$$S'=$$
###### Caso 6: Isolados

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | 1         | 1         | 1     | 1         |
| ${A}$     | 1         | 1         | 1     | 1         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$S=$$
$$S'=$$
##### Exemplo do livro
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

![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=134&rect=120,1156,1557,2233|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.134]]


![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=133&rect=169,643,715,1353|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.133]]


#### 4 Variáveis

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

![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=136&rect=194,334,844,993|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.136]]

###### Caso 1: Hexas

Tudo é 1, logo S = 1


###### Caso 2: Oitavas

![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=139&rect=171,846,1297,1491|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.139]]

###### Caso 3: Quadras
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=139&rect=145,1510,1508,2210|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.139]]

###### Caso 4: Pares
![[ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415.pdf#page=138&rect=206,350,939,946|ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.138]]



---

## 🧠 Resumo

| Tópico      | Princípio Central | Atenção Especial / Pegadinha |
| :---------- | :---------------- | :--------------------------- |
| min termos  | revisar           |                              |
| 2 Variáveis | decorar           |                              |
| 3 Variáveis | decorar           |                              |
| 4 Variáveis | Decorar           |                              |

> [!tip] 💡 Dica de Prova do Professor
> Destaques e orientações mencionadas pelo docente durante a aula.

---

## 📝 Dúvida
- [ ] Lista de Exercícios de Mapas de Karnough
