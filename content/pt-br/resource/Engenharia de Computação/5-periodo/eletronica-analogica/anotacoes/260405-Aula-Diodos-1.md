---
publish: true
titulo:  260405-Aula-Diodos-1
disciplina:
conteudo:
professor:
criado: domingo 05/04/2026 21:54
modificado: domingo 05/04/2026 21:54
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - Diodos
***
## Anotações
***
> [!NOTE] Atenção: Leitura do capítulo de Diodo do Livro do Malvino
### 2 Semicondutores

### 3 Diodos

Fichamento:

> [!PDF|important] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=74&selection=14,43,22,22&color=important|Eletronica Vol 1 - 8Ed Malvino, p.74]]
> > Ele é um dispositivo não linear porque o gráfico de sua corrente versus tensão não é uma reta.
> 
> 

> ([[Eletronica Vol 1 - 8Ed Malvino.pdf#page=74&selection=32,42,54,34&color=yellow|Eletronica Vol 1 - 8Ed Malvino, p.74]])
> O lado p é chamado de anodo, e o lado n é o catodo. O símbolo do diodo parece uma seta que aponta do lado p para o lado n, ou seja, do anodo para o catodo.

> ([[Eletronica Vol 1 - 8Ed Malvino.pdf#page=74&selection=83,71,89,44&color=red|Eletronica Vol 1 - 8Ed Malvino, p.74]])
> o circuito externo está forçando uma corrente no sentido fácil de circulação? Se a resposta for sim, o diodo está polarizado diretamente

> ([[Eletronica Vol 1 - 8Ed Malvino.pdf#page=78&selection=5,50,13,24&color=red|Eletronica Vol 1 - 8Ed Malvino, p.78]])
> Começaremos com a aproximação mais simples, chamada de diodo ideal. Em termos bem básicos, o que faz um diodo? Ele conduz bem no sentido direto e muito mal no sentido inverso. Idealmente, um diodo funciona como um perfeito condutor (resistência zero) quando polarizado diretamente e como um perfeito isolante (resistência infinita) quando polarizado reversamente.

> ([[Eletronica Vol 1 - 8Ed Malvino.pdf#page=78&selection=21,0,24,52&color=yellow|Eletronica Vol 1 - 8Ed Malvino, p.78]])
> Existe algum dispositivo que funciona como um diodo ideal? Sim. Uma chave comum tem resistência zero quando fechada e uma resistência infinita quando aberta. Logo, um diodo ideal age como uma chave que fecha quando polarizado diretamente e abre-se quando polarizado reversamente

![[Eletronica Vol 1 - 8Ed Malvino.pdf#page=84&rect=67,129,534,504&color=yellow|Eletronica Vol 1 - 8Ed Malvino, p.84]]

> ([[Eletronica Vol 1 - 8Ed Malvino.pdf#page=85&annotation=4096R|Eletronica Vol 1 - 8Ed Malvino, p.85]])
> Os defeitos dos diodos podem ser: resistência extremamente baixa nos dois sentidos de condução (diodo em curto); resistência alta nos dois sentidos de condução (diodo aberto); uma resistência até certo ponto baixa no sentido reverso (chamada de diodo com fuga).

> [!PDF|important] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=95&selection=4,32,6,39&color=important|Eletronica Vol 1 - 8Ed Malvino, p.95]]
> > Já os circuitos digitais geralmente operam com apenas dois níveis de tensões distintas, nível alto e nível baixo, representados por estados lógicos “1” e “0”, respectivamente.

#### Básico
> [!PDF|note] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=96&selection=9,0,23,7&color=note|Eletronica Vol 1 - 8Ed Malvino, p.96]]
> > Um diodo é um dispositivo não linear. A tensão de joelho, aproximadamente de 0,7 V para um diodo de silício é onde a curva direta vira para cima. A resistência de corpo é a resistência ôhmica das regiões p e n. Os diodos têm valores de corrente direta máxima e faixas de potência.

#### Diodo Ideal
> [!PDF|note] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=96&selection=30,7,33,8&color=note|Eletronica Vol 1 - 8Ed Malvino, p.96]]
> > O circuito equivalente é uma chave que fecha quando a polarização é direta e abre quando a polarização é reversa.

#### Segunda Aproximação
> [!PDF|note] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=96&selection=39,34,44,12&color=note|Eletronica Vol 1 - 8Ed Malvino, p.96]]
> > diodo de silício como uma chave em série com uma tensão de joelho de 0,7 V. Se a tensão equivalente de Thevenin que chega ao diodo for maior que 0,7 V, a chave fecha.


#### Terceira aproximação
> [!PDF|note] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=96&selection=51,7,56,9&color=note|Eletronica Vol 1 - 8Ed Malvino, p.96]]
> > a resistência de corpo é geralmente baixa o suficiente para ser desprezada. Nesta aproximação visualizamos o diodo como uma chave em série com uma tensão de joelho e uma resistência de corpo.


![[Eletronica Vol 1 - 8Ed Malvino.pdf#page=52&rect=55,88,202,398&color=note|Eletronica Vol 1 - 8Ed Malvino, p.52]]

p mais proton (positivo), n é mais eletron (negativo) - junção

barreira de potencial, camada de dpeleção

fig 2.14 polarização direta, por baixo, emprura empurra

fig 2.15 polarização reversa ??

depende da temperatura, movimento dos elétrons - banda de conudçõa e banda de valência.

exemplo 2.5

### Corrente Transiente
> [!PDF|yellow] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=63&selection=11,0,17,25&color=yellow|Eletronica Vol 1 - 8Ed Malvino, p.63]]
> > Quando a tensão inversa aumenta, lacunas e elétrons se afastam da junção. Como os elétrons livres e as lacunas se afastam da junção, eles deixam íons positivos e negativos para trás. Portanto, a camada de depleção fica mais larga. Quanto maior a polarização reversa, mais larga a camada de depleção se torna. Enquanto a camada de depleção está se ajustando para sua nova largura, uma corrente circula no circuito externo. Essa corrente de transiente cai a zero quando a camada de depleção pára de crescer.


Exercício Cap 2 - Semicondutores
PDF

### Diodos


> [!PDF|yellow] [[Eletronica Vol 1 - 8Ed Malvino.pdf#page=76&selection=15,2,26,22&color=yellow|Eletronica Vol 1 - 8Ed Malvino, p.76]]
> > Em outras palavras, se as regiões p e n fossem dois pedaços separados de semicondutores, cada um teria uma resistência que poderia ser medida com um ohmímetro, a mesma que um resistor comum.


Exemplo 3.2

