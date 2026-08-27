---
publish: true
titulo:  260508-Atributos
disciplina:
conteudo:
professor:
criado: sexta-feira 08/05/2026 15:11
modificado: sexta-feira 08/05/2026 15:11
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - Atributos
***
## Atributos
***
### Simples
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=61&selection=21,0,22,7&color=important|Modelagem_Conceitual___Parte_I (1), p.57]]
> > É um tipo de atributo indivisível, ou seja, é um atributo atômico
### Composto
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=61&selection=29,0,30,35&color=important|Modelagem_Conceitual___Parte_I (1), p.57]]
> > Pode ser dividido em partes menores que representam outros atributos, como endereço
### Multivalorado
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=61&selection=37,0,39,1&color=important|Modelagem_Conceitual___Parte_I (1), p.57]]
> > É aquele que pode ter um ou N (vários) valores associados a ele.
> 
### Derivado e armazenado
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=62&selection=19,0,21,15&color=important|Modelagem_Conceitual___Parte_I (1), p.58]]
> > Atributos derivados dependem de outro atributo ou até mesmo outra entidade para existir, como, idade e data de nascimento. 
### Chave
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=62&selection=30,0,32,20&color=important|Modelagem_Conceitual___Parte_I (1), p.58]]
> > É utilizado para identificar de forma única uma entidade, ou seja, os valores associados a esse atributo são distintos entre o conjunto de entidades. 
> 
> 

## Relacionamento
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=64&selection=10,0,11,15&color=important|Modelagem_Conceitual___Parte_I (1), p.60]]
> > Cada entidade poderá se relacionar com diversas outras entidades, independentementemente
> >

> [!PDF|yellow] [[Modelagem_Conceitual___Parte_I (1).pdf#page=64&selection=14,0,15,59&color=yellow|Modelagem_Conceitual___Parte_I (1), p.60]]
> > Isso significa que, se um relacionamento mapeado espelha a realidade, ele poderá envolver quaisquer tipos ou instâncias de entidades.

Uma pessoa pode ter 0 ou muitos carros (0,1; 0,n)

Um carro tem um proprietário (0,1;0,n)

ENTIDADE RELACIONAMENTO ENTIDADE
SINGULAR VERBO SINGULAR
A posse é da esquerda pra direita;

Ou, analogamente, de CIMA para BAIXO


## Auto-relacionamento
Regra de Negócio é o que define o auto relacionamento:
> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=71&selection=20,0,21,1&color=important|Modelagem_Conceitual___Parte_I (1), p.67]]
> > "um vigilante é substituído poroutro vigilante".
> 
> 

Leitura em sentido horário 
Um vigilante substituí um ou mais
Um vigilante é substituído por nenhum ou por um vigilante

> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=77&selection=18,0,20,46&color=important|Modelagem_Conceitual___Parte_I (1), p.73]]
> > Basicamente, um relacionamento é expresso através de uma construção verbal. O termo designando o relacionamento poderá estabelecer uma forma ativa ou passiva para a aplicação do verbo desejado.


## Cardinalidade

> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=82&selection=19,0,25,10&color=important|Modelagem_Conceitual___Parte_I (1), p.78]]
> > Com quantos elementos do tipo B se relaciona cada um dos elementos do tipo A? Dado um elemento do tipo B, com quantos elementos do tipo A ele se relaciona?

> [!PDF|important] [[Modelagem_Conceitual___Parte_I (1).pdf#page=86&selection=17,0,35,27&color=important|Modelagem_Conceitual___Parte_I (1), p.82]]
> > As três alternativas de classificação são: • 1:1 (leia-se um para um) • 1:N (leia-se um para muitos) • M: N (lei-se muitos para muitos)



