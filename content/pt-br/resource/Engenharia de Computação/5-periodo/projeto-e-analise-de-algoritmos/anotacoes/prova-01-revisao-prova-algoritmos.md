---
publish: false
title: Prova 01 - Revisão Prova - Algoritmos
created: 2026-06-18 14:49
modified: 2026-09-22 22:41
encrypted: true
tags:
- prova
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Prova 01 - Revisão Prova - Algoritmos

## Resumo Executivo

Revisão para prova de Projeto e Análise de Algoritmos, cobrindo análise de complexidade com foco em Bubble Sort e Insertion Sort.

## Informações & Checklist de Entrega

Tópicos cobertos:
- Bubble Sort
- Insertion Sort
- Análise de complexidade de tempo

## Objetivos do Trabalho

Preparar para avaliação em análise de algoritmos e complexidade de tempo.

## Metodologia & Desenvolvimento Prático

### Bubble Sort

```cpp
for (i=0; i<=n-1;i++) {
	for(j=n-1; j<=i+1;j--){
		if (A[j-1] > A[j]) {
			temp = A[j-1];
			A[j-1] = A[j];
			A[j] = temp;
		}
	}
}
```

#### Análise da Linha 1: Inicialização do Loop Externo
```cpp
for (i=0; i<=n-1;i++) 
```

**Fixos:**
- Atribuições: $i=0$ (1)
- Operações: $n-1$ (1)
- Total: 2

**Testes:**
- Valor Inicial: $i=0$ (0)
- Valor Final: $n-1$ (n-1)
- Valor Igual: $1$ (1)
- Total: $n$

**Incrementos:**
- Valor Verdadeiro: $n$ (n)
- Valor Falso: $1$ (1)
- Total: $2n+3$

**Total linha 1: $2n+3$**

#### Análise da Linha 2: Loop Interno

Entra $n$ vezes (por cada iteração do loop externo)

```cpp
for (j=n-1; j<=i+1;j--) 
```

**Fixos:**
- Atribuições: $j=n-1$ (1)
- Operações: $i+1$ (1)
- Total: 2

**Testes:**
- Inicial: $n-1$ (0)
- Final: varia com i
- Total: varia

**Incrementos:**
- Verdadeiro: varia
- Falso: 1
- Total: varia

**Análise iterativa necessária para complexidade total**

Melhor caso = ordenado, não entra na condicional

### Insertion Sort

```cpp
for (i=1; i<=n-1;i++) {
	atual = A[j];
	j = i-1;
	while (j>=0 && A[j] > atual){
		A[j+1] = A[j];
		j = j - 1;
	}
		A[j+1] = atual;
}
```

Variante com loop aninhado:

```cpp
for (i=1; i<=n-1;i++) {
	for (j=0;j<=i-1;j++){
		if(M[i][j] != M[j][i]) {
			temp = M[i][j];
			M[i][j] = M[j][i];
			M[j][i] = temp;
		}
	}
}
```

## Resumo Conceitual

Análise de complexidade de tempo através de contagem de operações primitivas em algoritmos de ordenação. Bubble Sort e Insertion Sort possuem complexidade O(n²) no caso geral, mas o melhor caso varia conforme a entrada.

## Esquemas & Anotações Visuais

Diagramas de loops aninhados para visualizar a quantidade de iterações.

## Dúvidas & Exercícios Recomendados

- Completar análise de todas as linhas do Bubble Sort
- Calcular complexidade total em melhor, pior e caso médio
- Comparar Bubble Sort vs. Insertion Sort
- Análise asintótica (Big O) para ambos
