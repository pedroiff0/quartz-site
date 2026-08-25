---
publish: true
titulo:  260413-Aula-AtividadesAbril-1
disciplina:
conteudo:
professor:
criado: segunda-feira 13/04/2026 09:37
modificado: segunda-feira 13/04/2026 09:37
tags:
cssclasses:
  - page-grid
  - center-images

---
# Atividades Projeto e Análise de Algoritmos
Período: 5º
Professora: Ana Mara
Aluno: Pedro Henrique Rocha de Andrade
Valor total: 2pts

Atividades referentes ao mês de abril sobre ordenação externa e tabela hash.
Código em anexo :)
***
# Ordenação Externa
***
# Resolução de Exercícios: Ordenação Externa
---
## Questão 1 - Intercalação de $n$ caminhos

### a) Intercalação
O processo utiliza ponteiros para os elementos iniciais de cada arquivo ordenado disponível:
Entrada Fita 1 - {3, 9, 20, 45}
Entrada Fita 2 - {1, 7, 15, 28}
Entrada Fita 3 - {4, 8, 16, 30}
Entrada Fita 4 - {2, 6, 18, 40}

| Passo | Valores Disponíveis | Saída | Fita | Ponteiro          |
| ----- | ------------------- | ----- | ---- | ----------------- |
| 1     | {3, 1, 4, 2}        | 1     | F2   | F2 avança para 7  |
| 2     | {3, 7, 4, 2}        | 2     | F4   | F4 avança para 6  |
| 3     | {3, 7, 4, 6}        | 3     | F1   | F1 avança para 9  |
| 4     | {9, 7, 4, 6}        | 4     | F3   | F3 avança para 8  |
| 5     | {9, 7, 8, 6}        | 6     | F4   | F4 avança para 18 |
| 6     | {9, 7, 8, 18}       | 7     | F2   | F2 avança para 15 |
| 7     | {9, 15, 8, 18}      | 8     | F3   | F3 avança para 16 |
| 8     | {9, 15, 16, 18}     | 9     | F1   | F1 avança para 20 |
| 9     | {20, 15, 16, 18}    | 15    | F2   | F2 avança para 28 |
| 10    | {20, 28, 16, 18}    | 16    | F3   | F3 avança para 30 |
| 11    | {20, 28, 30, 18}    | 18    | F4   | F4 avança para 40 |
| 12    | {20, 28, 30, 40}    | 20    | F1   | F1 avança para 45 |
| 13    | {45, 28, 30, 40}    | 28    | F2   | F2 esgotado       |
| 14    | {45, 30, 40}        | 30    | F3   | F3 esgotado       |
| 15    | {45, 40}            | 40    | F4   | F4 esgotado       |
| 16    | {45}                | 45    | F1   | F1 esgotado       |

### b) Sequência final resultante
**1, 2, 3, 4, 6, 7, 8, 9, 15, 16, 18, 20, 28, 30, 40, 45**

### c) Por que "intercalação de n caminhos"?
O método tem esse nome porque processa simultaneamente $n$ arquivos (caminhos) de entrada ordenados.

### d) Análise de escala (8 arquivos / 4 caminhos)
Fases necessárias: 2 fases de intercalação.
Agrupamento: Na primeira fase, os 8 arquivos seriam divididos em dois grupos de 4 arquivos cada.
Processamento:
Fita 1: 10
Fita 2: 10
Fita 3: 10
Fita 4: 10
Fita 5: 10
Fita 6: 10
Fita 7: 10
Fita 8: 10

Passada 1: Intercalar a fita 1, 2, 3 e 4 pra fita 9, fita 5, 6, 7 e 8 pra fita 10 (só pode 4 caminhos por vez)
Fita 9: 40 
Fita 10: 40

Passada 2: intercalar fita 9 e 10
Fita 11: 80 

Resultado: Fita 11 ordenada com os 80 registros. 



---

## Questão 2 - Intercalação Balanceada Bloco Variado

Parâmetros: 6 arquivos, 4 valores.
Entrada: 22, 5, 18, 30, 9, 14, 27, 3, 35, 11, 40, 6, 16, 28, 1, 33, 12, 25, 4, 31, 8, 20, 2, 26

### a) Distribuição
Entrada Fita 1 - {5, 18, 22, 30}, {1, 16, 28, 33}
Entrada Fita 2 - {3, 9, 14, 27}, {4, 12, 25, 31}
Entrada Fita 3 - {6, 11, 35, 40}, {2, 8, 20, 26}
Saida Fita 4 - {}
Saida Fita 5 - {}
Saida Fita 6 - {}
### b) Intercalações 
Entrada Fita 1 - {5, 18, 22, 30}, {1, 16, 28, 33}
Entrada Fita 2 - {3, 9, 14, 27}, {4, 12, 25, 31}
Entrada Fita 3 - {6, 11, 35, 40}, {2, 8, 20, 26}


Se fossem duas fitas tb n ficaria com tamanho variado, por conta do tamanho da entrada, ou por causa dos valores, coincidentemente ficaram bons. 
Entrada Fita 1 - {5, 18, 22, 30}, {6, 11, 35, 40}, {1, 16, 28, 33}
Entrada Fita 2 - {3, 9, 14, 27}, {2, 8, 20, 26}, {4, 12, 25, 31}
Saida Fita 3 - {3,5,9,14,18,22,27,30,1,4,12,16,25,28,31,33}
Saida Fita 4 - {2,6,8,11,20,26,35,40}
Reescrever na fita 1 a intercalação do bloco

Comparar Fitas 1,2,3:

| **Passo** | Fita 1 | Fita 2 | Fita 3 | Saída | Destino |
| --------- | ------ | ------ | ------ | ----- | ------- |
| 1         | 5      | 3      | 6      | 3     | Fita 4  |
| 2         | 5      | 9      | 6      | 5     | Fita 4  |
| 3         | 18     | 9      | 6      | 6     | Fita 4  |
| 4         | 18     | 9      | 11     | 9     | Fita 4  |
| 5         | 18     | 14     | 11     | 11    | Fita 4  |
| 6         | 18     | 14     | 35     | 14    | Fita 4  |
| 7         | 18     | 27     | 35     | 18    | Fita 4  |
| 8         | 22     | 27     | 35     | 22    | Fita 4  |
| 9         | 30     | 27     | 35     | 27    | Fita 4  |
| 10        | 30     |        | 35     | 30    | Fita 4  |
| 11        |        |        | 35     | 35    | Fita 4  |
| 12        |        |        | 40     | 40    | Fita 4  |


| **Passo** | Fita 1 | Fita 2 | Fita 3 | Saída | Destino |
| --------- | ------ | ------ | ------ | ----- | ------- |
| 1         | 1      | 4      | 2      | 1     | Fita 5  |
| 2         | 16     | 4      | 2      | 2     | Fita 5  |
| 3         | 16     | 4      | 8      | 4     | Fita 5  |
| 4         | 16     | 12     | 8      | 8     | Fita 5  |
| 5         | 16     | 12     | 20     | 12    | Fita 5  |
| 6         | 16     | 25     | 20     | 16    | Fita 5  |
| 7         | 28     | 25     | 20     | 20    | Fita 5  |
| 8         | 28     | 25     | 26     | 25    | Fita 5  |
| 9         | 28     | 31     | 26     | 26    | Fita 5  |
| 10        | 28     | 31     |        | 28    | Fita 5  |
| 11        | 33     | 31     |        | 31    | Fita 5  |
| 12        | 33     |        |        | 33    | Fita 5  |

| **Passo** | Fita 4 | Fita 5 | Saída | Destino |
| --------- | ------ | ------ | ----- | ------- |
| 1         | 3      | 1      | 1     | Fita 1  |
| 2         | 3      | 2      | 2     | Fita 1  |
| 3         | 3      | 4      | 3     | Fita 1  |
| 4         | 5      | 4      | 4     | Fita 1  |
| 5         | 5      | 8      | 5     | Fita 1  |
| 6         | 6      | 8      | 6     | Fita 1  |
| 7         | 9      | 8      | 8     | Fita 1  |
| 8         | 9      | 12     | 9     | Fita 1  |
| 9         | 11     | 12     | 11    | Fita 1  |
| 10        | 14     | 12     | 12    | Fita 1  |
| 11        | 14     | 16     | 14    | Fita 1  |
| 12        | 18     | 16     | 16    | Fita 1  |
| 13        | 18     | 20     | 18    | Fita 1  |
| 14        | 22     | 20     | 20    | Fita 1  |
| 15        | 22     | 25     | 22    | Fita 1  |
| 16        | 27     | 25     | 25    | Fita 1  |
| 17        | 27     | 26     | 26    | Fita 1  |
| 18        | 27     | 28     | 27    | Fita 1  |
| 19        | 30     | 28     | 28    | Fita 1  |
| 20        | 30     | 31     | 30    | Fita 1  |
| 21        | 35     | 31     | 31    | Fita 1  |
| 22        | 35     | 33     | 33    | Fita 1  |
| 23        | 35     |        | 35    | Fita 1  |
| 24        | 40     |        | 40    | Fita 1  |

Saida Fita 4 - {3, 5, 6, 9, 11, 14, 18, 22, 27, 30, 35, 40} 
Saida Fita 5 - {1, 2, 4, 8, 12, 16, 20, 25, 26, 28, 31, 33}
Saida Fita 6 - {}

Resultado: 1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 16, 18, 20, 22, 25, 26, 27, 28, 30, 31, 33, 35, 40
### c) Explique por que, nesse método, os blocos iniciais podem ficar maiores do que a memória principal.
A memória não precisa armazenar o bloco inteiro, apenas os registros que estão sendo comparados no momento, permitindo que o resultado da junção de vários blocos menores resulte em um bloco final maior que a capacidade da RAM.

---

## Questão 3 - Intercalação Polifásica

Parâmetros: 4 arquivos, 5 valores.
Entrada: 34, 7, 25, 18, 2, 41, 13, 29, 5, 37, 11, 23, 1, 32, 16, 40, 8, 27, 4, 35

### a) Distribuição

Fita 1 - {2-0, 7-0, 13-0, 18-0, 25-0, 29-0, 34-0, 37-0, 41-0, 4-2, 8-2}
Fita 2 - {1-1, 5-1, 11-1, 16-1, 23-1, 27-1, 32-1, 35-1, 40-1} 
Fita 3 - vazia
Fita 4 - vazia

### b) Intercalação
Fita 1 - {2-0, 7-0, 13-0, 18-0, 25-0, 29-0, 34-0, 37-0, 41-0}
Fita 2 - {1-1, 5-1, 11-1, 16-1, 23-1, 27-1, 32-1, 35-1, 40-1} 
Fita 3 - {1-1, 2-0, 5-1, 7-0, 11-1, 13-0, 16-1, 18-0, 23-1, 25-0, 27-1, 29-0, 32-1, 34-0, 35-1, 37-0, 40-1, 41-0}
Fita 4 - {4-2,8-2}
Fita 1 - {1-1, 2-0, 4-2, 5-1, 7-0, 8-2, 11-1, 13-0, 16-1, 18-0, 23-1, 25-0, 27-1, 29-0, 32-1, 34-0, 35-1, 37-0, 40-1, 41-0}

### c) Sequência Final
1, 2, 4, 5, 7, 8, 11, 13, 16, 18, 23, 25, 27, 29, 32, 34, 35, 37, 40, 41

***
# Tabela Hash
***
## Questão 1 - Conceitos Fundamentais
Uma tabela hash é uma estrutura de dados que utiliza uma função específica para mapear chaves a índices em um vetor, permitindo o armazenamento e a recuperação de informações de forma eficiente. Ela resolve o problema da lentidão na busca em grandes conjuntos de dados, eliminando a necessidade de percorrer toda a estrutura linearmente (como em listas) ou realizar múltiplas divisões (como em árvores). O custo médio de busca é $O(1)$ porque a função hash permite acessar diretamente a posição de memória onde o elemento está, tornando o tempo de resposta constante e independente do volume total de dados.

## Questão 2 - Função de Hashing
Uma função de hashing é um algoritmo que codifica uma chave de entrada em um valor numérico que serve como índice para o vetor da tabela. Uma boa função deve ser rápida para calcular, distribuir as chaves de maneira uniforme para evitar acúmulos em poucos índices e minimizar a ocorrência de colisões. O método da divisão é uma técnica onde o índice é definido pelo resto da divisão da chave pelo tamanho da tabela ($m$), seguindo a fórmula $h(k) = k \mod m$.

## Questão 3 - Colisões
Uma colisão ocorre quando duas ou mais chaves diferentes resultam no mesmo índice após o cálculo da função de hashing. Elas são consideradas inevitáveis  pois como a quantidade de chaves possíveis é geralmente muito superior ao tamanho físico da tabela, o mapeamento eventualmente sobrepõe elementos. O impacto direto das colisões é a perda de desempenho, pois o sistema precisa executar passos adicionais para organizar e encontrar elementos que "disputam" o mesmo espaço.

## Questão 4
### a) Encadeamento (Lista Ligada)
Como funciona: Cada posição da tabela armazena o endereço de uma lista ligada. Quando uma colisão ocorre, o novo elemento é inserido no nó dessa lista correspondente ao índice.
Vantagens: A tabela pode armazenar mais elementos que o seu tamanho nominal e a exclusão de itens é tecnicamente mais simples.
Desvantagens: Consome memória extra para os ponteiros da lista e, se houver muitas colisões, a busca pode se tornar lenta (se tornando linear).
### b) Endereçamento Aberto
Como funciona: Todos os elementos são guardados no próprio vetor da tabela. Se a posição original estiver ocupada, o algoritmo procura a próxima célula livre.
Sondagem: É o método de busca por uma vaga disponível. 
Exemplos: Pode ser linear que vai procurar na próxima posição consecutiva, quadrática que usa um salto que cresce com o quadrado ou duplo hashing que usa uma segunda função para definir o intervalo do salto.

---

## Questão 5
Parâmetros: Tamanho 11, Função $h(k) = k \mod 11$.
Chaves: 22, 1, 13, 11, 24, 33, 35, 44, 21, 10.

Cálculos:

| Chave | Cálculo ($k \mod 11$) |
| :---- | :-------------------- |
| 22    | $22 \mod 11 = 0$      |
| 1     | $1 \mod 11 = 1$       |
| 13    | $13 \mod 11 = 2$      |
| 11    | $11 \mod 11 = 0$      |
| 24    | $24 \mod 11 = 2$      |
| 33    | $33 \mod 11 = 0$      |
| 35    | $35 \mod 11 = 2$      |
| 44    | $44 \mod 11 = 0$      |
| 21    | $21 \mod 11 = 10$     |
| 10    | $10 \mod 11 = 10$     |

Inserção:

| Chave | Posição | Representação da Lista   |
| :---- | :------ | :----------------------- |
| 22    | 0       | `[22]`                   |
| 1     | 1       | `[1]`                    |
| 13    | 2       | `[13]`                   |
| 11    | 0       | `[22 -> 11]`             |
| 24    | 2       | `[13 -> 24]`             |
| 33    | 0       | `[22 -> 11 -> 33]`       |
| 35    | 2       | `[13 -> 24 -> 35]`       |
| 44    | 0       | `[22 -> 11 -> 33 -> 44]` |
| 21    | 10      | `[21]`                   |
| 10    | 10      | `[21 -> 10]`             |

Tabela final:

| Posição | Representação da Lista   |
| :------ | :----------------------- |
| 0       | `[22 -> 11 -> 33 -> 44]` |
| 1       | `[1]`                    |
| 2       | `[13 -> 24 -> 35]`       |
| 10      | `[21 -> 10]`             |

---
## Questão 6

Usando a divisão novamente, as posições indicam onde deveriam cair e as tentativas mostram aonde conseguiu a próxima vazia. 

| Chave | Posição | Tentativas                                                          | Posição Final | N Colisões |
| :---- | :------ | :------------------------------------------------------------------ | :------------ | :--------- |
| 22    | 0       | Pos 0 (livre)                                                       | 0             | 0          |
| 1     | 1       | Pos 1 (livre)                                                       | 1             | 0          |
| 13    | 2       | Pos 2 (livre)                                                       | 2             | 0          |
| 11    | 0       | Colisão. Tenta Pos 0, 1, 2 (Ocupadas). Pos 3 (Livre)                | 3             | 3          |
| 24    | 2       | Colisão. Tenta Pos 3 (Ocupada). Pos 4 (Livre)                       | 4             | 1          |
| 33    | 0       | Colisão. Tenta Pos 0, 1, 2, 3, 4  (Ocupadas). Pos 5 (Livre)         | 5             | 4          |
| 35    | 2       | Colisão. Tenta Pos 3, 4, 5 (Ocupadas). Pos 6 (Livre)                | 6             | 3          |
| 44    | 0       | Colisão. Tenta Pos 0, 1, 2, 3, 4, 5, 6 (Ocupadas). Pos 7 (Livre)    | 7             | 7          |
| 21    | 10      | Pos 10 (Livre)                                                      | 10            | 0          |
| 10    | 10      | Colisão. Tenta Pos 0, 1, 2, 3, 4, 5, 6, 7 (Ocupadas). Pos 8 (Livre) | 8             | 8          |

Tabela final

| Chave | Posição |
| :---- | :------ |
| 22    | 0       |
| 1     | 1       |
| 13    | 2       |
| 11    | 3       |
| 24    | 4       |
| 33    | 5       |
| 35    | 6       |
| 44    | 7       |
| 21    | 10      |
| 10    | 8       |

---

## Questão 7 - Análise Comparativa
a) Endereçamento Aberto.
b) Endereçamento Aberto em termos de memória, só utilizou os 11 espaços disponiveis, Encadeamento utilizou MENOS espaços na lista, mas usou mais memória pra encadear no tratamento das colisões. 
c) Encadeamento foi melhor.