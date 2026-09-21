---
publish: false
title: Aula 01 - Atributos e Relacionamentos
created: 2026-05-08 14:49
modified: 2026-09-19 13:18
encrypted: true
tags:
- aula
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Aula 01 - Atributos e Relacionamentos

## Anotações do Quadro & Conteúdo

### Atributos

#### Simples
> [!important] **Modelagem_Conceitual___Parte_I (1), p.57**
> > É um tipo de atributo indivisível, ou seja, é um atributo atômico

#### Composto
> [!important] **Modelagem_Conceitual___Parte_I (1), p.57**
> > Pode ser dividido em partes menores que representam outros atributos, como endereço

#### Multivalorado
> [!important] **Modelagem_Conceitual___Parte_I (1), p.57**
> > É aquele que pode ter um ou N (vários) valores associados a ele.
> 

#### Derivado e Armazenado
> [!important] **Modelagem_Conceitual___Parte_I (1), p.58**
> > Atributos derivados dependem de outro atributo ou até mesmo outra entidade para existir, como, idade e data de nascimento. 

#### Chave
> [!important] **Modelagem_Conceitual___Parte_I (1), p.58**
> > É utilizado para identificar de forma única uma entidade, ou seja, os valores associados a esse atributo são distintos entre o conjunto de entidades. 
> 

### Relacionamento
> [!important] **Modelagem_Conceitual___Parte_I (1), p.60**
> > Cada entidade poderá se relacionar com diversas outras entidades, independentementemente
> 

> [!warning] **Modelagem_Conceitual___Parte_I (1), p.60**
> > Isso significa que, se um relacionamento mapeado espelha a realidade, ele poderá envolver quaisquer tipos ou instâncias de entidades.

Uma pessoa pode ter 0 ou muitos carros (0,1; 0,n)

Um carro tem um proprietário (0,1;0,n)

ENTIDADE RELACIONAMENTO ENTIDADE
SINGULAR VERBO SINGULAR
A posse é da esquerda pra direita;

Ou, analogamente, de CIMA para BAIXO

### Auto-Relacionamento
Regra de Negócio é o que define o auto relacionamento:
> [!important] **Modelagem_Conceitual___Parte_I (1), p.67**
> > "um vigilante é substituído poroutro vigilante".
> 

Leitura em sentido horário 
Um vigilante substituí um ou mais
Um vigilante é substituído por nenhum ou por um vigilante

> [!important] **Modelagem_Conceitual___Parte_I (1), p.73**
> > Basicamente, um relacionamento é expresso através de uma construção verbal. O termo designando o relacionamento poderá estabelecer uma forma ativa ou passiva para a aplicação do verbo desejado.

### Cardinalidade

> [!important] **Modelagem_Conceitual___Parte_I (1), p.78**
> > Com quantos elementos do tipo B se relaciona cada um dos elementos do tipo A? Dado um elemento do tipo B, com quantos elementos do tipo A ele se relaciona?

> [!important] **Modelagem_Conceitual___Parte_I (1), p.82**
> > As três alternativas de classificação são: • 1:1 (leia-se um para um) • 1:N (leia-se um para muitos) • M: N (lei-se muitos para muitos)

## Resumo Conceitual

Atributos em modelagem de dados podem ser classificados como simples (atômicos), compostos (divisíveis), multivalorados (N valores) ou derivados (dependem de outros). Chaves são atributos que identificam unicidade. Relacionamentos descrevem associações entre entidades, expressos através de verbos, com cardinalidades 1:1, 1:N ou M:N que especificam a multiplicidade da associação.

## Esquemas & Anotações Visuais

As ilustrações do PDF mostram exemplos de atributos simples vs. compostos, relacionamentos pessoa-carro, auto-relacionamentos de vigilantes, e as três cardinalidades principais.

## Dúvidas & Exercícios Recomendados

- Classificar atributos em um domínio real
- Identificar relacionamentos e suas cardinalidades
- Desenhar diagramas ER com auto-relacionamentos
- Validar se um atributo é simples, composto ou multivalorado
