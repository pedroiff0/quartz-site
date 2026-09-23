---
publish: false
title: Aula 01 - Diodos
created: 2026-04-05 14:49
modified: 2026-09-22 22:41
encrypted: true
tags:
- aula
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Aula 01 - Diodos

## Anotações do Quadro & Conteúdo

### Nota de Atenção
Leitura do capítulo de Diodo do Livro do Malvino

### Semicondutores

### Diodos

Fichamento:

> [!important] **Eletronica Vol 1 - 8Ed Malvino, p.74**
> > Ele é um dispositivo não linear porque o gráfico de sua corrente versus tensão não é uma reta.
> 

> (**Eletronica Vol 1 - 8Ed Malvino, p.74**)
> O lado p é chamado de anodo, e o lado n é o catodo. O símbolo do diodo parece uma seta que aponta do lado p para o lado n, ou seja, do anodo para o catodo.

> (**Eletronica Vol 1 - 8Ed Malvino, p.74**)
> o circuito externo está forçando uma corrente no sentido fácil de circulação? Se a resposta for sim, o diodo está polarizado diretamente

> (**Eletronica Vol 1 - 8Ed Malvino, p.78**)
> Começaremos com a aproximação mais simples, chamada de diodo ideal. Em termos bem básicos, o que faz um diodo? Ele conduz bem no sentido direto e muito mal no sentido inverso. Idealmente, um diodo funciona como um perfeito condutor (resistência zero) quando polarizado diretamente e como um perfeito isolante (resistência infinita) quando polarizado reversamente.

> (**Eletronica Vol 1 - 8Ed Malvino, p.78**)
> Existe algum dispositivo que funciona como um diodo ideal? Sim. Uma chave comum tem resistência zero quando fechada e uma resistência infinita quando aberta. Logo, um diodo ideal age como uma chave que fecha quando polarizado diretamente e abre-se quando polarizado reversamente

> 📖 *[Referência: Eletronica Vol 1 - 8Ed Malvino, p.84]*

> (**Eletronica Vol 1 - 8Ed Malvino, p.85**)
> Os defeitos dos diodos podem ser: resistência extremamente baixa nos dois sentidos de condução (diodo em curto); resistência alta nos dois sentidos de condução (diodo aberto); uma resistência até certo ponto baixa no sentido reverso (chamada de diodo com fuga).

> [!important] **Eletronica Vol 1 - 8Ed Malvino, p.95**
> > Já os circuitos digitais geralmente operam com apenas dois níveis de tensões distintas, nível alto e nível baixo, representados por estados lógicos "1" e "0", respectivamente.

### Básico
> [!note] **Eletronica Vol 1 - 8Ed Malvino, p.96**
> > Um diodo é um dispositivo não linear. A tensão de joelho, aproximadamente de 0,7 V para um diodo de silício é onde a curva direta vira para cima. A resistência de corpo é a resistência ôhmica das regiões p e n. Os diodos têm valores de corrente direta máxima e faixas de potência.

### Diodo Ideal
> [!note] **Eletronica Vol 1 - 8Ed Malvino, p.96**
> > O circuito equivalente é uma chave que fecha quando a polarização é direta e abre quando a polarização é reversa.

### Segunda Aproximação
> [!note] **Eletronica Vol 1 - 8Ed Malvino, p.96**
> > diodo de silício como uma chave em série com uma tensão de joelho de 0,7 V. Se a tensão equivalente de Thevenin que chega ao diodo for maior que 0,7 V, a chave fecha.

### Terceira Aproximação
> [!note] **Eletronica Vol 1 - 8Ed Malvino, p.96**
> > a resistência de corpo é geralmente baixa o suficiente para ser desprezada. Nesta aproximação visualizamos o diodo como uma chave em série com uma tensão de joelho e uma resistência de corpo.

> 📖 *[Referência: Eletronica Vol 1 - 8Ed Malvino, p.52]*

p mais proton (positivo), n é mais eletron (negativo) - junção

barreira de potencial, camada de dpeleção

fig 2.14 polarização direta, por baixo, emprura empurra

fig 2.15 polarização reversa ??

depende da temperatura, movimento dos elétrons - banda de conudçõa e banda de valência.

exemplo 2.5

### Corrente Transiente
> [!warning] **Eletronica Vol 1 - 8Ed Malvino, p.63**
> > Quando a tensão inversa aumenta, lacunas e elétrons se afastam da junção. Como os elétrons livres e as lacunas se afastam da junção, eles deixam íons positivos e negativos para trás. Portanto, a camada de depleção fica mais larga. Quanto maior a polarização reversa, mais larga a camada de depleção se torna. Enquanto a camada de depleção está se ajustando para sua nova largura, uma corrente circula no circuito externo. Essa corrente de transiente cai a zero quando a camada de depleção pára de crescer.

Exercício Cap 2 - Semicondutores
PDF

### Diodos

> [!warning] **Eletronica Vol 1 - 8Ed Malvino, p.76**
> > Em outras palavras, se as regiões p e n fossem dois pedaços separados de semicondutores, cada um teria uma resistência que poderia ser medida com um ohmímetro, a mesma que um resistor comum.

Exemplo 3.2

## Resumo Conceitual

Diodos são dispositivos semicondutores não lineares que conduzem bem em polarização direta e conduzem muito pouco em polarização reversa. Estruturalmente, possuem uma junção p-n onde a barreira de potencial determina seu comportamento. O comportamento pode ser aproximado de três formas: ideal (chave perfeita), segunda aproximação (com tensão de joelho de 0,7V), e terceira aproximação (incluindo resistência de corpo).

## Esquemas & Anotações Visuais

As figuras do livro Malvino mostram as características V-I do diodo, as aproximações progressivas e o modelo de chave. As imagens incluem polarizações direta/reversa e a camada de depleção.

## Dúvidas & Exercícios Recomendados

- Entender a diferença entre diodo ideal, segunda e terceira aproximações
- Praticar problemas de polarização direta vs. reversa
- Revisar o Capítulo 2 (Semicondutores) para fundamentação
- Resolver exemplo 2.5 e 3.2 completamente
