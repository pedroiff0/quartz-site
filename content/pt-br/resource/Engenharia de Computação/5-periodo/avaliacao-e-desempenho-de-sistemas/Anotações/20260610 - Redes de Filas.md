---
publish: true
titulo:  20260610 - Redes de Filas
created: 2026-06-10 14:49
modified: 2026-08-27 21:54
tags:
cssclasses:

---
# Notas de Reunião - Redes de Filas
## quarta-feira, 10/06/2026
***
## Anotações

### Tópicos

Centros de serviços clientes entre si.
![[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=8&rect=67,98,286,157|Análise_de_Operacional_de_Redes_de_Filas, p.4]]

Classificações:
* Tipo,
* Carga,
* Qntd Carga,

Tipos:
* Aberta
![[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=13&rect=55,68,296,119|Análise_de_Operacional_de_Redes_de_Filas, p.9]]
* Fechada
![[Pasted image 20260610175705.png]]
* Mistas
![[Pasted image 20260610175733.png]]

Cargas:
* Abertas:  
> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=17&selection=20,0,20,29&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.13]]
> > número ilimitado de clientes.
> 
> 

* Fechadas
> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=18&selection=19,28,20,50&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.14]]
> > permite apenas a entrada de um número de clientes no sistema limitado e conhecido
> 
> 

Dividido em: 
* Lote: N Clientes ativos (pop. finita) - ciclo.

* Terminal: N Clientes Ativos, Z tempo pra pensar;

> [!PDF|red] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=18&selection=46,0,47,33&color=red|Análise_de_Operacional_de_Redes_de_Filas, p.14]]
> > Modelos de filas fechados usam cargas fechadas. Filas mistas usam em conjunto cargas fechadas e cargas abertas.
> 
> 

Cargas:
* Única:
> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=20&selection=20,0,22,28&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.16]]
> > As requisições que trafegam na rede de filas são de um mesmo tipo. Todas as requisições possuem as mesmas características de taxa de chegadas, tempo de serviço, prioridade
> 

* Múltiplas Cargas (+ comum): 
> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=20&selection=30,0,31,13&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.16]]
> > O sistema de filas pode aceitar diversos tipos de cargas ao mesmo tempo. 
> > Cada tipo de carga pode ter um tempo diferente para processamento, prioridade, taxa de chegadas de usuários
> 
> 

Probabilidade Pareto 20 80


## Variáveis Operacionais

> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=22&selection=13,0,14,6&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.18]]
> > São definidas as seguintes variáveis operacionais para o sistemas de redes de filas:

$A_i$: n chegadas de transações
$C_{ij}$: n transações saem de i para j
$C_{io}$ n transações que saem de i pro sistema
$C_{o}$ n transações que deixam o sistema
$V_i = \frac{C_i}{C_o}$ taxa relativa de visitas ao servidor i
$D_i = \frac{U_i}{X_o} = V_i S_i$: Demada de serviço servidor i
$X_o$: taxa processamento/vazão
$B_i$: tempo ocupado de i
$S_i$: tempo de serviço de i
$R_i$: tempo de resposta de i

## Lei Operacional

### Lei de fluxo forçado
> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=27&selection=13,0,14,12&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.23]]
> > Esta lei mostra que o fluxo (vazão) em todas as partes do sistema deve ser proporcional

Exemplo:
![[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=28&rect=37,10,324,181&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.24]]

### Lei do tempo de resposta

> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=31&selection=13,0,16,28&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.27]]
> > O tempo de resposta total do sistema (o tempo de processamento de uma requisição, desde a entrada no sistema de filas até sua saída) depende do tempo de resposta de cada fila versus o número de visitas que a mesma requisição faz ao servidor daquela fila
> 
> $R = \sum_{i=1}^{K} V_i R_i = \sum_{i=1}^{K} \frac{D_i}{1-U_i}$
 
### Lei da demanda de serviço
> [!PDF|important] [[Análise_de_Operacional_de_Redes_de_Filas.pdf#page=35&selection=13,0,27,45&color=important|Análise_de_Operacional_de_Redes_de_Filas, p.31]]
> > A demanda de serviço, anteriormente definida como Di = Vi Di , pode ser relacionada a vazão do sistema e sua utilização
