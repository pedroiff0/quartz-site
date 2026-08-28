---
publish: true
title: 260423-Aula-Atividades-1
discipline:
content:
professor:
created: 2026-04-23 13:34
modified: 2026-08-27 21:59
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - Atividades
***
# Exercícios Fila M/M/1/$\infty$/FIFO
## Fórmulas Referência:
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
## Questão 1: API de autenticação do portal acadêmico
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho = \frac{18}{24} = \frac{3}{4} = 0,75$$
$$P_0 = (1-0,75) = 0,25$$
$$P(N \geq 4) = \rho^{n} = \left(\frac{3}{4}\right)^4 = \frac{81}{256} = 0,3164$$
$$E[n] = \frac{\rho}{(1-\rho)} = \frac{\frac{3}{4}}{1-\frac{3}{4}} = \frac{12}{4} = 3$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)} = \frac{0,75^2}{0,25} = \frac{9}{16} \cdot \frac{4}{1} = \frac{36}{16} = \frac{9}{4} = 2,25$$
$$E[s] = \frac{1}{(\mu-\lambda)} = \frac{1}{6} = 0,1667$$
$$E[w] = \frac{1}{(\mu-\lambda)} - \frac{1}{\mu} = \frac{1}{(24-18)} - \frac{1}{24} = \frac{4-1}{24} = \frac{3}{24} = \frac{1}{8} = 0,125 $$

b) verifique se a meta de desempenho é atendida; 
Sim, $E[s] \lt 200$


c) faça análise de sensibilidade para: cenário A: aumento da taxa de chegada para 21 req/s; cenário B: otimização do serviço para 30 req/s; 

Cenário A
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos:
$$\rho = \frac{21}{24} = \frac{7}{8} = 0,875$$
$$P_0 = (1-0,875) = 0,125$$
$$P(N \geq 4) = \rho^{n} = \left(\frac{7}{8}\right)^4 = \frac{2401}{4096} = 0,586$$
$$E[n] = \frac{\rho}{(1-\rho)} = \frac{\frac{7}{8}}{1-\frac{7}{8}} = \frac{56}{8} = 7$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)} = \frac{\left(\frac{7}{8}\right)^2}{\frac{1}{8}} = \frac{49}{64} \cdot \frac{8}{1} = \frac{49}{8} = 6,125$$
$$E[s] = \frac{1}{(\mu-\lambda)} = \frac{1}{3} = 0,3333$$
$$E[w] = \frac{1}{(\mu-\lambda)} - \frac{1}{\mu} = \frac{1}{3} - \frac{1}{24} = \frac{8-1}{24} = \frac{7}{24} = 0,291 $$
A latência excede a meta permitida.

Cenário B:
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho = \frac{18}{30} = \frac{9}{15} = 0,6$$
$$P_0 = (1-0,6) = 0,4$$
$$P(N \geq 4) = \rho^{n} = \left(\frac{9}{15}\right)^4 = \frac{6561}{50625} = 0,1296$$
$$E[n] = \frac{\rho}{(1-\rho)} = \frac{\frac{6}{10}}{1-\frac{6}{10}} = \frac{6}{10} \cdot \frac{10}{4} = 1,5$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)} = \frac{\left(\frac{6}{10}\right)^2}{\frac{4}{10}} = \frac{36}{100} \cdot \frac{10}{4} = \frac{9}{10} = 0,9$$
$$E[s] = \frac{1}{(\mu-\lambda)} = \frac{1}{12} = 0,083$$
$$E[w] = \frac{1}{(\mu-\lambda)} - \frac{1}{\mu} = \frac{1}{12} - \frac{1}{30} = \frac{5 - 2}{60} = \frac{3}{60} = \frac{1}{20} = 0,05 \cdot 100 = 50 ms$$
A latência excede a meta permitida.

d) emita um parecer técnico e proponha uma solução.
O servidor está estável mas precisa de atenção para a taxa de chegada, um pouco mais e já estoura o tempo. 
***
## Questão 2: Servidor de arquivos do laboratório
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.


***
## Questão 3: Central de tickets de TI
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.

***
## Questão 4: Impressora compartilhada da secretaria
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.



***
## Questão 5: Gateway de telemetria IoT
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.

***
## Questão 6: Fila de renderização de mapas
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.


***
## Questão 7: Servidor de integração contínua
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.


***
## Questão 8: Validador de notas fiscais eletrônicas
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.

***
## Questão 9: Transcodificador de videoaulas
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.


***
## Questão 10:  Servidor de consultas ao acervo acadêmico
Dados:
$\lambda = 18$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms

a) calcule a, $\rho$, $P_0$, $E[n]$, $E[nw]$, $E[s]$, $E[w]$ e $P(N \geq 4)$; 
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
b) verifique se a meta de desempenho é atendida; 

c) faça análise de sensibilidade para: 

Cenário A: aumento da taxa de chegada para 21 req/s;
Dados:
$\lambda = 21$  reqs/s
$\mu = 24$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$

Cenário B: otimização do serviço para 30 req/s; 
Dados:
$\lambda = 18$  reqs/s
$\mu = 30$ reqs/s
Meta: Tempo médio resposta inferior a 200ms
Cálculos
$$\rho=\frac{\lambda}{\mu}$$
$$P_0 = 1 -\rho$$
$$P_n = (1-\rho)\,\rho^{n}$$
$$P(N \geq n) = \rho^{n}$$
$$E[n] = \frac{\rho}{(1-\rho)}$$
$$E[n_w] = \frac{\rho^2}{(1-\rho)}$$
$$E[s] = \frac{1}{(\mu-\lambda)}$$
$$E[w] = E[s] - \frac{1}{\mu}$$
d) emita um parecer técnico e proponha uma solução.


***
# Exercícios Fila M/M/m/$\infty$/FIFO

## Fórmulas de referência
$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$
## Questão 1:  Cluster de autenticação do portal
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.
***
## Questão 2:  Servidor de imagens de máquinas virtuais
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 3:  Triagem automática de chamados
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 4:  Serviço de renderização de mapas
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 5: Cluster de consultas SQL
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 6:  Sistema de moderação de mensagens
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 7:  Runners de integração contínua
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 8:  Transcodificação de videoaulas
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 9: Validador de documentos fiscais:
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
## Questão 10:  Serviço de busca do acervo
Dados:
$m = 4$
$\lambda = 18$
$\mu = 6$
Meta: Tempo médio na fila inferior a 100ms

a) calcule a, ρ, P0, C(m,ρ), E[nw], E[ns], E[n], E[s] e E[w]

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

b) verifique se a meta é atendida



c) faça análise de sensibilidade para:

Cenário A: aumento da carga para 22 reqs/s
Dados:
$m = 4$ servidores
$\lambda = 22$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$


Cenário B: adição de mais um servidor ($m = 5$)
Dados:
$m = 5$ servidores
$\lambda = 18$ reqs/s
$\mu = 6$ reqs/s
Meta: Tempo médio na fila inferior a 100ms

$$\rho = \frac{\lambda}{m\mu}$$
$$U=\frac{\lambda}{\mu}$$
$$P_n = \begin{cases} \frac{1}{n!}U^n \cdot P_0 \quad\text{se}\quad 1\leq n \lt m \\ \frac{1}{m!m^{n-m}}U^n \cdot P_0 \quad\text{se}\quad n \geq m\end{cases}$$
$$P_0 = \left(\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!}\right)^{-1}$$
$$C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$$
$$\text{E}[n_s] = m\rho$$
$$\text{E}[n] = \text{E}[n_w] + \text{E}[n_s]$$
$$\text{E}[s] = \frac{\text{E}[n]}{\lambda}$$
$$\text{E}[w] = \frac{\text{E}[n_w]}{\lambda}$$

d) Emita parecer técnico.

***
# Exercícios Fila M/M/1/B/FIFO

## Fórmulas de referência
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
## Questão 1:  Gateway de pagamentos instantâneos
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 2:  Spooler de impressão do laboratório
Dados:
$\lambda = 12$/min
$\mu = 16$/min
$B=5$

Meta: A probabilidade de bloqueio deve ser inferior a $6$s

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 3:  Coletor de mensagens de sensores
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 4:  Proxy reverso do portal institucional
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 5:  Triagem automática de chamados
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 6: Exercício 6 — Controlador de consultas SQL
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 7:  Servidor de integração contínua com buffer finito
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 8:  Validador de notas fiscais eletrônicas
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 9:  Transcodificador de videoaulas com fila limitada
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.

***
## Questão 10:  Terminal de autoatendimento da biblioteca
Dados:
$\lambda = 15$
$\mu = 20$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$

a) calcule $\rho$, $P_0$, $P_B$, $\rho'$, $\lambda'$, $\lambda'$, $E[n]$, $E[n_w]$, $E[s]$ e $E[w]$; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


b) verifique se a meta é atendida; 


c) faça análise de sensibilidade para: 

cenário A: aumento da capacidade para $B = 6$; 
Dados:
$\lambda = 15$
$\mu = 20$
$B=6$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$

cenário B: otimização do serviço para $\mu = 24$ req/s; 
Dados:
$\lambda = 15$
$\mu = 24$
$B=4$

Meta: A probabilidade de bloqueio deve ser inferior a $8\%$
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } n < B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$\rho = \frac{\lambda}{\mu}$$

$$\rho' = \rho(1-P_B)$$

$$
P_n = 
\begin{cases}
    & \frac{1-\rho}{1-\rho^{B+1}}\rho^n, & \text{se } 0 \leq n \lt B \\
    &0 &\text{se } n \gt B
\end{cases}
$$
$$P_B = \left(\frac{(1-\rho)}{(1-\rho^{(B+1)})}\right)^{\rho^B}$$
$$\lambda' = \lambda(1-P_B)$$

$$\lambda_{\text{perda}} = \lambda \text{P}_B$$
$$\text{E}[n] = \frac{\rho}{1-\rho} - \frac{(B+1)\rho^{B+1}}{1-\rho^{B+1}}$$
$$\text{E}[n_w] = \frac{\rho}{1-\rho} - \rho\frac{1+B\rho^{B}}{1-\rho^{B+1}}$$

$$\text{E}[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$\text{E}[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$


d) emita parecer técnico.


***
# Exercícios Fila M/M/m/B/FIFO
## Fórmulas Referência:
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***

## Questão 1:  Cluster de autenticação com capacidade finita
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
***
## Questão 2: Gateway SQL com fila limitada
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.

***
## Questão 3:  Sistema de triagem de chamados
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
## Questão 4:  Renderização de mapas com buffer limitado
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
## Questão 5:  Moderação automática de mensagens
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
## Questão 6:  Runners de integração contínua com capacidade finita
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
## Questão 7: Transcodificação de videoaulas
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
## Questão 8: Validação fiscal com cluster finito
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
***
## Questão 9:  Busca do acervo com fila limitada
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
## Questão 10:  Processamento de eventos IoT
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%

a) calcule a, ρ, P_0, P_B, ρ', λ', λ_perda, E[n], E[n_w], E[s] e E[w]; 
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


b) verifique se a meta é atendida; 



c) faça análise de sensibilidade para:

cenário A: aumento da capacidade para $B = 8$; 
Dados:
$m = 3$ servidores
$B=8$ reqs
$\lambda = 14$ reqs/s
$\mu = 6$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***


cenário B: aumento da taxa de serviço para $\mu = 7$ req/s por servidor; 
Dados:
$m = 3$ servidores
$B=6$ reqs
$\lambda = 14$ reqs/s
$\mu = 7$ reqs/s
Meta: Probabilidade de bloqueio inferior a 5%
$$
\lambda_n = 
\begin{cases}
    \lambda & \text{se } 0 \leq n \lt B \\
    0 & \text{se } n \geq B
\end{cases}
$$
$$
\mu_n = 
\begin{cases}
    n\mu & \text{se } 1 \leq n \lt B \\
    m\mu & \text{se } m \leq n \leq B
\end{cases}
$$
$$\rho = \frac{\lambda}{m\mu}$$
$$P_n = 
\begin{cases}
    \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } 1 \leq n \lt B-1 \\
    \frac{1}{m^{n-m}m!} \left(\frac{\lambda}{\mu}\right)^n P_0 & \text{se } m \leq n \leq B
\end{cases}
$$
$$
P_n = 
\begin{cases}
	\left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{B-m+1}{m!}\right]^{-1} & \text{se } \rho = \frac{\lambda}{m\mu} = 1\\
    \left[\sum_{n=0}^{m-1} \frac{1}{n!} \left(\frac{\lambda}{\mu}\right)^n + \left(\frac{\lambda}{\mu}\right) \frac{(1-\rho)^{B-m+1}}{m!(1-\rho)}\right]^{-1}& \text{se } \rho = \frac{\lambda}{m\mu} \neq 1
\end{cases}
$$
$$U= \rho(1-P_0)$$
$$\lambda' = \lambda(1-P_B)$$
$$\lambda_{\text{perda}} = \lambda P_B$$
$$E[n] = \sum_{n=1}^B nP_n$$
$$E[n_w] = \sum_{n=m+1}^B (n-m)P_n$$
$$E[s] = \frac{E[n]}{\lambda(1-P_B)}$$
$$E[w] = \frac{E[n_w]}{\lambda(1-P_B)}$$
***
d) emita parecer técnico.
