---
publish: true
title: 260618-RevisaoProva
created: 2026-06-18 14:49
modified: 2026-09-16 15:35
encrypted: true
password: eng232
tags:
  - aula
  - engenharia-de-computacao
cssclasses:
  - page-layout
---
# Notas de Aula - RevisaoProva
***
## Anotações
***
## Bubble Sort
```cpp
# Bubble Sort
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

### Linha
```cpp
for (i=0; i<=n-1;i++) 
```
Linha 1: Fixos
Atribuições: $i=0$ (1)
Operações: $n-1$ (1)
Total: 2

Linha 1: Testes
Valor Inicial: $i=0$ (0)
Valor Final: $n-1$ (n-1)
Valor Igual: $1$ (1)
Total: $n$

Linha 1: Incrementos
Valor Verdadeiro: $n$ (n)
Valor Falso: $1$ (1)
Total: $2n+3$

Total linha 1: $2n+3$

### Linha
Entra $n$ vezes:

```cpp
for (i=0; i<=n-1;i++) 
```

Linha 2: Fixos
Atribuições: $i=0$ (1)
Operações: $n-1$ (1)
Total: 2

Linha 2: Testes
Valor Inicial: $i=0$ (0)
Valor Final: $n-1$ (n-1)
Valor Igual: $1$ (1)
Total: $n$

Linha 2: Incrementos
Valor Verdadeiro: $n$ (n)
Valor Falso: $1$ (1)
Total: $2n+3$

Total linha 1: $2n+3$

Tabela 

Total Geral Linha 1: 


Melhor caso = ordenado, não entra na condicional, portanto 
### Linha


### Linha


### Linha


### Linha


### Insertion Sort
```cpp
# insertion sort
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

```cpp
# insertion sort
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
***
