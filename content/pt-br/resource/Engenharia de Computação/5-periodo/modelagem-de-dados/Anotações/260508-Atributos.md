---
publish: true
title: 260508-Atributos
created: 2026-05-08 14:49
modified: 2026-09-16 15:35
encrypted: true
password: eng232
tags:
  - aula
  - engenharia-de-computacao
cssclasses:
  - page-layout
---
# Notas de Aula - Atributos
***
## Atributos
***
### Simples
> [!important] **Modelagem_Conceitual___Parte_I (1), p.57**
> > É um tipo de atributo indivisível, ou seja, é um atributo atômico
### Composto
> [!important] **Modelagem_Conceitual___Parte_I (1), p.57**
> > Pode ser dividido em partes menores que representam outros atributos, como endereço
### Multivalorado
> [!important] **Modelagem_Conceitual___Parte_I (1), p.57**
> > É aquele que pode ter um ou N (vários) valores associados a ele.
> 
### Derivado e armazenado
> [!important] **Modelagem_Conceitual___Parte_I (1), p.58**
> > Atributos derivados dependem de outro atributo ou até mesmo outra entidade para existir, como, idade e data de nascimento. 
### Chave
> [!important] **Modelagem_Conceitual___Parte_I (1), p.58**
> > É utilizado para identificar de forma única uma entidade, ou seja, os valores associados a esse atributo são distintos entre o conjunto de entidades. 
> 
> 

## Relacionamento
> [!important] **Modelagem_Conceitual___Parte_I (1), p.60**
> > Cada entidade poderá se relacionar com diversas outras entidades, independentementemente
> >

> [!warning] **Modelagem_Conceitual___Parte_I (1), p.60**
> > Isso significa que, se um relacionamento mapeado espelha a realidade, ele poderá envolver quaisquer tipos ou instâncias de entidades.

Uma pessoa pode ter 0 ou muitos carros (0,1; 0,n)

Um carro tem um proprietário (0,1;0,n)

ENTIDADE RELACIONAMENTO ENTIDADE
SINGULAR VERBO SINGULAR
A posse é da esquerda pra direita;

Ou, analogamente, de CIMA para BAIXO


## Auto-relacionamento
Regra de Negócio é o que define o auto relacionamento:
> [!important] **Modelagem_Conceitual___Parte_I (1), p.67**
> > "um vigilante é substituído poroutro vigilante".
> 
> 

Leitura em sentido horário 
Um vigilante substituí um ou mais
Um vigilante é substituído por nenhum ou por um vigilante

> [!important] **Modelagem_Conceitual___Parte_I (1), p.73**
> > Basicamente, um relacionamento é expresso através de uma construção verbal. O termo designando o relacionamento poderá estabelecer uma forma ativa ou passiva para a aplicação do verbo desejado.


## Cardinalidade

> [!important] **Modelagem_Conceitual___Parte_I (1), p.78**
> > Com quantos elementos do tipo B se relaciona cada um dos elementos do tipo A? Dado um elemento do tipo B, com quantos elementos do tipo A ele se relaciona?

> [!important] **Modelagem_Conceitual___Parte_I (1), p.82**
> > As três alternativas de classificação são: • 1:1 (leia-se um para um) • 1:N (leia-se um para muitos) • M: N (lei-se muitos para muitos)

