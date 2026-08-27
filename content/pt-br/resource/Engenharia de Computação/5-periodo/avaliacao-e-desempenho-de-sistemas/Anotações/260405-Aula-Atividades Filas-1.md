---
publish: true
titulo:  260405-Aula-Atividades Filas-1
disciplina:
conteudo:
professor:
created: 2026-04-05
modified: 2026-08-27
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - Atividades Filas
***
### Questão 1 - Servidor de Autenticação Acadêmica

Dados:
Chegada ($\lambda$) = 8 reqs/min
Atendimento ($\mu$) = 12 reqs/min
Modelo: M/M/1/$\infty$/FIFO

a) se o servidor opera com folga; -> Sim, pois $\rho < 1$
b) se a fila média já é perceptível; -> $\text{E}[n_w] \approx 1,333$ já é perceptível

Passo a passo:

Utilização: $\rho = \frac{\lambda}{\mu} = \frac{8}{12} = 0,667 \implies 66,67\%$ 
Número médio: $\text{E}[n] = \frac{\rho}{1-\rho} = \frac{0,667}{0,333} = 2$
Número médio na fila: $\text{E}[n_w] = \frac{\rho^2}{1-\rho} = \frac{0,444}{0,333} = 1,3333$
Tempo médio no sistema: $\text{E}[s] = \frac{1}{\mu(1-\rho} = \frac{1}{12\cdot 0,3333} = 0,25$ min
Tempo médio de espera: $\text{E}[w] = \text{E}[s] - \frac{1}{\mu} = 0,25 - \frac{1}{12} = 0,1667$ min 

c) se a chance de haver pelo menos 4 requisições no sistema é relevante

Probabilidade de haver pelo menos 4 requisições: $\text{P}(N \geq 4) = \rho^4 = (0,667)^4 = 0,198$ 

### Questão 6 - Balanceador com 2 servidores

a) se a utilização por servidor é saudável; -> U e $\rho$
b) se a chance de espera ainda é relevante; -> $\text{E}[n_w]$
c) se o tempo médio total de resposta está adequado. -> $\text{E}[w]$

Dados:
Número de servidores ($m$) = 2
Chegada ($\lambda$) = 8 reqs/min
Atendimento ($\mu$) = 12 reqs/min
Modelo: M/M/m/$\infty$/FIFO

Passo a passo:

Utilização (U) = $\frac{\lambda}{\mu} = \frac{2}{2} = 1$
Utilização ($\rho$) = $\frac{\lambda}{m\mu} = \frac{2}{4} = 0,5 \implies 50\%$

Probabilidade de não ter ninguém ($\text{P}_0$):
$P_0 = (\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!})^{-1} = [\frac{U^0}{0!} + \frac{U^1}{1!} + \frac{U^2}{2!(1-\rho)}]^{-1} = [1+1+1]^{-1} = 0,333$
Probabilidade de todos os servidores estarem ocupados ($C(m,\rho)$): $P[\text{fila}] = C(m,\rho) = P_0\frac{U^m}{m!(1-\rho)} = \frac{1}{3}\cdot\frac{1}{2\cdot0,5} = 0,333 \implies 33,34\%$

Número médio na fila ($E[n_w]$) = $\frac{\rho}{1-\rho} \cdot C = \frac{0,5}{0,5} \cdot 0,333 = 0,333$ 
Número de requisições no sistema:
$E[n] = E[n_w] + E[n_s] = 0,333 + 1 = 1,333$
Tempo médio de espera na fila ($\text{E}[w]$): $\frac{\text{E}[n_w]}{\lambda} = \frac{0,333}{2} = 0,1667$ min
Tempo médio de espera de resposta ($\text{E}[s]$): $\frac{\text{E}[n]}{\lambda} = \frac{1,333}{2} = 0,6667 \implies 40s$  min
***
## Resolução Teste 2025.2

### Resumo de fórmulas com perguntas:

**Cuidado com as unidades de tempo! 1h = 60 min = 3600 segundos

Um servidor, então modelo: M/M/1/$\infty$/FIFO; se tiver m servidores, então modelo: M/M/m/$\infty$/FIFO 
#### Modelo 1 - M/M/1/$\infty$/FIFO
Só tem UM único servidor:

1. Servidor opera com folga/estável? $\rho = \frac{\lambda}{\mu}$
Aqui calcular a taxa de serviço $\rho$

2. A fila média é perceptível/ultrapassa? $\text{E}[n] = \frac{\rho}{1-\rho}$ e $\text{E}[n_w] = \frac{\rho^2}{1-\rho}$
Aqui calcular o número médio no sistema $\text{E}[n]$  e o número médio na fila $\text{E}[n_w]$
A resposta será o $\text{E}[n_w]$

3. O tempo médio fica abaixo de X segundos? $\text{E}[s] = \frac{1}{\mu(1-\rho)}\lt X$
Aqui calcular o tempo médio no sistema $\text{E}[s]$

4. Chance de haver X chamados? $P(N \geq X) =  \rho^X$
Aqui calcular a probabilidade $P$

#### Modelo 2 - M/M/m/$\infty$/FIFO
Tem MAIS de UM servidor (unidade de processamento)
1. Servidor opera com folga/estável? $\rho = \frac{\lambda}{m\mu}$; $U=\frac{\lambda}{\mu}$
Aqui calcular a taxa de serviço de cada servidor $\rho$

2. A probabilidade de todos analistas estarem ocupados? $P_0 = (\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!})^{-1}$ e $C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$
Aqui a resposta é $C(m,\rho)$

3. A fila média é perceptível/ultrapassa?  $\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$; $\text{E}[n] = \text{E}[n_w] + U$
Aqui calcular o número médio no sistema $\text{E}[n]$  e o número médio na fila $\text{E}[n_w]$
A resposta será o $\text{E}[n_w]$

4. A espera média de ultrapassa X segundos? $\text{E}[w] = \frac{\text{E}[n]}{\lambda}\lt X$
Aqui calcular o tempo de espera (wait) $\text{E}[w]$

***
### Questão 1 - Sistema Suporte Técnico
Modelo: M/M/1/$\infty$/FIFO
Chegada ($\lambda$) = 9 requisições/min
Taxa de serviço ($\mu$) = 15 chamados/min

Passo 1:
Calcular $\rho = \frac{\lambda}{\mu} = \frac{9}{15} = 0,6 \implies 60\%$
a) O servidor opera com folga, 60%

Passo 2: $E[n], E[n_w]$
Número médio no sistema: $\text{E}[n] = \frac{\rho}{1-\rho} = \frac{0,6}{1-0,6} = 1,5$
Número médio na fila: $E[n_w] = \frac{\rho^2}{1-\rho} = \frac{0,6^2}{1-0,6} = 0,9$

b) A fila média é perceptível ($E[n] = 0,9$)

Passo 3: $E[s]$
Tempo médio o Sistema: $E[s] = \frac{1}{\mu(1-\rho)} = \frac{1}{15(1-0,6)} = 0,1667 \implies 10$ s
c) o tempo médio total no sistema fica abaixo de 12s 

Passo 4: $P(N\geq4) = \rho^4 = 0,6^4 \approx 0,1296 \implies 12,96\%$
d) a chance de ter pelo menos 4 chamados no sistema é baixa, acima de 10%  
***
### Questão 2 - Plataforma de aulas
Modelo: M/M/1/$\infty$/FIFO
Chegada ($\lambda$): $42$ vídeos/hora
Taxa de serviço ($\mu$): $60$ vídeos/hora

Passo 1: $\rho$
$\rho = \frac{\lambda}{\mu} = \frac{42}{60} = 0,7$
a) Ele está estável, $\rho < 1$

Passo 2: $E[n_w] < 1$
$E[n_w] = \frac{\rho2}{1-\rho} = \frac{0,7^2}{1-0,7} = 1,633$
b) A fila média ultrapassa 1 vídeo. 

Passo 3: $E[w] = E[s] - \frac{1}{\mu}$
$E[s] = \frac{1}{\mu(1-\rho)} = \frac{1}{60(0,3)} = 0,05$ h 
$E[w] = 0,05 - \frac{1}{60} = 0,03 \implies 2,333$ min 

c) Tempo médio total no sistema abaixo de 4 minutos;
(Gabarito: 3,33, acho que tá errado, deveria ser 2,33)

Passo 4: $P(N\geq5)$
$\rho^5 = 0,1680 \implies 16,80\%$
d) Já merece atenção.
***
### Questão 3 - Sistema de monitoramento industrial
Modelo: M/M/4/$\infty$/FIFO
Chegada ($\lambda$) = 8 eventos/min 
Serviço ($\mu$) = 3 eventos/min
Processadores ($m$) = 4

Passo 1: $U, \rho$
$U = \frac{\lambda}{\mu} = \frac{8}{3} = 2,667$
$\rho = \frac{\lambda}{m\mu} = \frac{8}{4\cdot 3} = 0,667$
a) a arquitetura está bem;

Passo 2: $P_0$
$P_0 = (\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!})^{-1} = [\frac{2,667^0}{0!} + \frac{2,667^1}{1!} + \frac{2,667^2}{2!} + \frac{2,667^3}{3!} +\frac{2,667^4}{4!(1-0,667)}]^{-1}$
$$= [1+2,667+1,778+3,161+6,33]^{-1} = 0,06$$

Probabilidade de todos os servidores estarem ocupados ($C(m,\rho)$): $P[\text{fila}] = C(m,\rho) = P_0\frac{U^m}{m!(1-\rho)} = 0,06 \cdot \frac{2,667^4}{4!(1-0,667)} = 0,06 \cdot 6,33 = 0,3798$
b) Permanece abaixo de 40\%

Passo 3: $E[n_w]$
$E[n_w] = \frac{\rho}{1-\rho} \cdot C = \frac{0,667}{1-0,667} \cdot 0,3798 = 2 \cdot 0,3798 = 0,7596 \implies 75,96\%$
c) A fila média é inferior a 1 evento;

Passo 4:
$E[n] = E[n_w] + U = 0,7596 + 2,667 = 3,4266$
$E[w] = \frac{E[n_w]}{\lambda} = \frac{0,7596}{8} = 0,09495$ min
$E[s] = \frac{E[n]}{\lambda} = \frac{3,4266}{8} = 0,4275 \implies = 25,65$ s 

d) Fica abaixo de 30 s;

***
### Questão 4 - Central de protocolas
Modelo: M/M/3/$\infty$/FIFO
Chegada ($\lambda$): 9 solicitações/min
Serviço ($\mu$): 4 solicitações/min
Processadores ($m$): 3 analistas

Passo 1: $U, \rho$
$U = \frac{\lambda}{\mu} = \frac{9}{4} = 2,25$
$\rho = \frac{\lambda}{m\mu} = \frac{9}{3\cdot 4} = 0,75$
a) É alta

Passo 2: $P_0$
$P_0 = (\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!})^{-1} = [\frac{2,25^0}{0!} + \frac{2,25^1}{1!} + \frac{2,25^2}{2!} \frac{2,25^3}{3!(1-0,75)}]^{-1}$
$$= [1+2,25+2,53125+7,59]^{-1} = 0,0748$$
Probabilidade de todos os servidores estarem ocupados ($C(m,\rho)$): $P[\text{fila}] = C(m,\rho) = P_0\frac{U^m}{m!(1-\rho)} = 0,0748 \cdot \frac{2,25^3}{3!(1-0,75)} = 0,0748 \cdot 7,59 = 0,5678 \implies 56,78\%$
b) Ultrapassa 50%.

Passo 3: $E[n_w]$
$E[n_w] = \frac{\rho}{1-\rho} \cdot C = \frac{0,75}{1-0,75} \cdot 0,6192 = 3 \cdot 0,5678 = 1,703$

c) A fila média é SUPERIOR a 1 evento, sendo relevante;

Passo 4:
$E[n] = E[n_w] + U = 1,703 + 2,25 = 3,953$
$E[w] = \frac{E[n_w]}{\lambda} = \frac{1,703}{9} = 0,189 \cdot 60 \implies 11,36$ s
$E[s] = \frac{E[n]}{\lambda} = \frac{3,953}{9} = 0,439 \implies = 26,36$ s 
d) Fica ACIMA de 10 s;


***
### Questão 5 - Sistema acadêmico
Modelo: M/M/1/$\infty$/FIFO
***
Chegada ($\lambda$): $12$ registros/min
Taxa de serviço ($\mu$): $20$ registros/min

Passo 1: $\rho$
$\rho = \frac{\lambda}{\mu} = \frac{12}{20} = 0,6$
a) Ele está estável, $\rho < 1$ e opera com folga.

Passo 2: $E[n_w] < 1$
$E[n_w] = \frac{\rho2}{1-\rho} = \frac{0,6^2}{1-0,6} = 0,9$
b) A fila média é perceptível.

Passo 3: $E[w] = E[s] - \frac{1}{\mu}$
$E[s] = \frac{1}{\mu(1-\rho)} = \frac{1}{20(0,4)} = 0,125$ h 
$E[w] = 0,125 - \frac{1}{20} = 0,075 \implies 4,5$ s 

c) Tempo médio total no sistema abaixo de 8 s (4,5s)
(No gabarito aparece 7,5s, acho que está errado!)

Passo 4: $P(N\geq5)$
$\rho^5 = 0,1296 \implies 12,96\%$
d) A chance é baixa. 
***
