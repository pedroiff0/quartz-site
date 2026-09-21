---
publish: false
title: Aula 03 - Correção
created: 2026-09-11 23:15
modified: 2026-09-19 13:20
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

# Aula 03 - Correção

> [!info]- Informações & Checklist da Aula
> - **Data da Aula:** 11/09/2026
> - **Status de Revisão:**
>   - [x] Anotações em sala de aula
>   - [x] Revisão e fixação de conceitos
>   - [ ] Resolução de exercícios recomendados
>   - [ ] Destilação para [[07-permanente/notas-permanentes|Notas Permanentes]]

---

## Anotações do Quadro & Conteúdo

### Condição Irrelevante

Significado lógico
Ordem de Gray (organização lógica do mapa, bit a bit)
Célula X quando permitir agrupar melhor (uma “carta” coringa)

Caso 1:
* Sem usar X como 1:

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | X         | 1         | 1     | 1         |
| ${A}$     | 0         | 0         | 0     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$ S = \bar{A}C + \bar{A}B$$

* Usando X como 1:

| Casos     | $\bar{B}$ | $\bar{B}$ | ${B}$ | ${B}$     |
| --------- | --------- | --------- | ----- | --------- |
| $\bar{A}$ | X         | 1         | 1     | 1         |
| ${A}$     | 0         | 0         | 0     | 0         |
| Casos     | $\bar{C}$ | C         | C     | $\bar{C}$ |
$$ S = \bar{A}$$


Caso 2:

| Casos     | $\bar{C}$ | $\bar{C}$ | ${C}$ | ${C}$     | Casos     |
| --------- | --------- | --------- | ----- | --------- | --------- |
| $\bar{A}$ | X         | 0         | X     | 1         | $\bar{B}$ |
| $\bar{A}$ | 1         | 0         | 1     | 1         | ${B}$     |
| ${A}$     | 0         | X         | X     | 0         | ${B}$     |
| ${A}$     | 0         | 1         | 0     | X         | $\bar{B}$ |
| Casos     | $\bar{D}$ | $D$       | $D$   | $\bar{D}$ | Casos     |

Decisões:
* Quais X aumentam grupos úteis?
* Quais X não reduzem o custo?
* Quais grupos cobrem todos os 1 sem incluir o 0?

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.159]*

$$S= \bar{A}C + \bar{A}\bar{D} + A\bar{C}D$$

Exercício Resolvido 1

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.160]*
$$S= \bar{B} + C$$
Exemplo Resolvido 2

| Caso |  A  |  B  | C   | D   | S   |
| :--: | :-: | :-: | --- | --- | --- |
|  0   |  0  |  0  | 0   | 0   | 1   |
|  1   |  0  |  0  | 0   | 1   | X   |
|  2   |  0  |  0  | 1   | 0   | 1   |
|  3   |  0  |  0  | 1   | 1   | 0   |
|  4   |  0  |  1  | 0   | 0   | 1   |
|  5   |  0  |  1  | 0   | 1   | 1   |
|  6   |  0  |  1  | 1   | 0   | 1   |
|  7   |  0  |  1  | 1   | 1   | 0   |
|  8   |  1  |  0  | 0   | 0   | 1   |
|  9   |  1  |  0  | 0   | 1   | 0   |
|  10  |  1  |  0  | 1   | 0   | X   |
|  11  |  1  |  0  | 1   | 1   | 1   |
|  12  |  1  |  1  | 0   | 0   | X   |
|  13  |  1  |  1  | 0   | 1   | 1   |
|  14  |  1  |  1  | 1   | 0   | X   |
|  15  |  1  |  1  | 1   | 1   | 0   |

| Casos     | $\bar{C}$ | $\bar{C}$ | ${C}$ | ${C}$     | Casos     |
| --------- | --------- | --------- | ----- | --------- | --------- |
| $\bar{A}$ | 1         | X         | 0     | 1         | $\bar{B}$ |
| $\bar{A}$ | 1         | 1         | 0     | 1         | ${B}$     |
| ${A}$     | X         | 1         | 0     | X         | ${B}$     |
| ${A}$     | 1         | 0         | 1     | X         | $\bar{B}$ |
| Casos     | $\bar{D}$ | $D$       | $D$   | $\bar{D}$ | Casos     |
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.161]*

$$S = \bar{D} + B\bar{C} + A\bar{B}C$$

Regra prática: começar com agrupamentos obrigatórios e bem definidos, depois completar.

CAda saida é um mapa de karnough

Capítulo 4 (novo tópico)

Teste é no papel pro karnough


| A   | B   | $V_1$ | $V_{M1}$ | $V_2$ | $V_{M2}$ |
| --- | --- | ----- | -------- | ----- | -------- |
| 0   | 0   | 0     | 1        | 1     | 0        |
| 0   | 1   | 0     | 1        | 1     | 0        |
| 1   | 0   | 1     | 0        | 0     | 1        |
| 1   | 1   | 1     | 0        | 0     | 1        |
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.182]*

| Caso |  A  |  B  | C   | $E_V$ | $B_0$ | Interpretação                     |
| :--: | :-: | :-: | --- | ----- | ----- | --------------------------------- |
|  0   |  0  |  0  | 0   | 1     | 0     | Caixa inferior vazia, abastecer   |
|  1   |  0  |  0  | 1   | 1     | 0     | Caixa inferior vazia, não bombear |
|  2   |  0  |  1  | 0   | 1     | 1     | água em B, caixa superior vazia   |
|  3   |  0  |  1  | 1   | 1     | 0     | Caixa superior cheia              |
|  4   |  1  |  0  | 0   | X     | X     | IMPOSSIVEL                        |
|  5   |  1  |  0  | 1   | X     | X     | IMPOSSIVEL                        |
|  6   |  1  |  1  | 0   | 0     | 1     | Caixa inferior cheia, bombear     |
|  7   |  1  |  1  | 1   | 0     | 0     | Ambas cheias                      |
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.184]*

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.185]*

4 variáveis

Ordem de prioridade 

A>B>C>D

> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.186]*
> 📖 *[Referência: ilide.info-elementos-de-eletronica-digital-capuano-francisco-gabriel-idoeta-ivan-valeije-pr_2b9feef9e166b55bcc121dacebf74415, p.187]*



---

> [!abstract]- Resumo Conceitual
> - **Conceito Central:** 
> - **Fórmulas / Algoritmos Relevantes:**
> - **Pegadinhas / Atenção em Provas:**

---

## Esquemas & Anotações Visuais (excalidraw)
<!-- No iPad: insira desenhos com 'excalidraw: Create and embed new drawing' para desenhar com Apple Pencil -->

---

> [!question]- Dúvidas & Exercícios Recomendados
> - [ ] academico exercicio
- [x] Exercício Resolvido da seção 3.9.6.1
- [ ] Exercício de 4 variáveis
