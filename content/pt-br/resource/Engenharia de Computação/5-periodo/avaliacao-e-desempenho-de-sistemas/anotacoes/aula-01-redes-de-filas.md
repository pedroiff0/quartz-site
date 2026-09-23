---
publish: false
title: Aula 01 - Redes de Filas
created: 2026-06-10 14:49
modified: 2026-09-22 22:41
encrypted: true
tags:
- aula
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Aula 01 - Redes de Filas

## Anotações do Quadro & Conteúdo

### Tópicos

Centros de serviços clientes entre si.
> 📖 *[Referência: Análise_de_Operacional_de_Redes_de_Filas, p.4]*

Classificações:
* Tipo,
* Carga,
* Qntd Carga,

Tipos:
* Aberta
> 📖 *[Referência: Análise_de_Operacional_de_Redes_de_Filas, p.9]*
* Fechada
![[Pasted image 20260610175705.png]]
* Mistas
![[Pasted image 20260610175733.png]]

Cargas:
* Abertas:  
> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.13**
> > número ilimitado de clientes.
> 

* Fechadas
> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.14**
> > permite apenas a entrada de um número de clientes no sistema limitado e conhecido
> 

Dividido em: 
* Lote: N Clientes ativos (pop. finita) - ciclo.

* Terminal: N Clientes Ativos, Z tempo pra pensar;

> [!danger] **Análise_de_Operacional_de_Redes_de_Filas, p.14**
> > Modelos de filas fechados usam cargas fechadas. Filas mistas usam em conjunto cargas fechadas e cargas abertas.
> 

Cargas:
* Única:
> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.16**
> > As requisições que trafegam na rede de filas são de um mesmo tipo. Todas as requisições possuem as mesmas características de taxa de chegadas, tempo de serviço, prioridade
> 

* Múltiplas Cargas (+ comum): 
> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.16**
> > O sistema de filas pode aceitar diversos tipos de cargas ao mesmo tempo. 
> > Cada tipo de carga pode ter um tempo diferente para processamento, prioridade, taxa de chegadas de usuários
> 

Probabilidade Pareto 20 80

### Variáveis Operacionais

> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.18**
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

### Lei Operacional

#### Lei de fluxo forçado
> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.23**
> > Esta lei mostra que o fluxo (vazão) em todas as partes do sistema deve ser proporcional

Exemplo:
> 📖 *[Referência: Análise_de_Operacional_de_Redes_de_Filas, p.24]*

#### Lei do tempo de resposta

> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.27**
> > O tempo de resposta total do sistema (o tempo de processamento de uma requisição, desde a entrada no sistema de filas até sua saída) depende do tempo de resposta de cada fila versus o número de visitas que a mesma requisição faz ao servidor daquela fila
> 
> $R = \sum_{i=1}^{K} V_i R_i = \sum_{i=1}^{K} \frac{D_i}{1-U_i}$
 
#### Lei da demanda de serviço
> [!important] **Análise_de_Operacional_de_Redes_de_Filas, p.31**
> > A demanda de serviço, anteriormente definida como Di = Vi Di , pode ser relacionada a vazão do sistema e sua utilização

## Resumo Conceitual

Redes de filas envolvem centros de serviço onde os clientes se movem entre diferentes filas. O modelo define tipos de filas (abertas, fechadas, mistas) e tipos de carga (aberta/fechada, única/múltipla). As variáveis operacionais permitem análise de desempenho, como taxa de chegada, taxa de serviço, utilização do servidor e tempo de resposta.

## Esquemas & Anotações Visuais

As imagens PDF referenciadas no quadro apresentam diagramas das redes de filas com as diferentes topologias (abertas, fechadas e mistas).

## Dúvidas & Exercícios Recomendados

- Revisar a Lei de Fluxo Forçado e sua aplicação em redes
- Exercitar o cálculo de variáveis operacionais em diferentes cenários
- Comparar desempenho entre redes abertas, fechadas e mistas
