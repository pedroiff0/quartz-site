---
publish: false
title: Atividade 01 - Atividades - Filas
created: 2026-04-05 14:49
modified: 2026-09-22 22:41
encrypted: true
tags:
- atividade
- trabalho
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Atividade 01 - Atividades - Filas

## Resumo Executivo

Conjunto de exercícios práticos sobre modelos de filas M/M/1 e M/M/m, com aplicações em sistemas acadêmicos, servidores autenticação, balanceadores e plataformas de aula. Os problemas cobrem análise de utilização de servidores, cálculo de métricas de desempenho (filas médias, tempos de espera) e avaliação de probabilidades de congestionamento.

## Informações & Checklist de Entrega

- Resolver problemas com modelos M/M/1/$\infty$/FIFO e M/M/m/$\infty$/FIFO
- Apresentar cálculos passo a passo para cada questão
- Validar se os servidores operam com folga (ρ < 1)
- Avaliar se filas médias são perceptíveis
- Analisar probabilidades de congestionamento

## Objetivos do Trabalho

1. Aplicar fórmulas de filas em cenários reais
2. Calcular variáveis operacionais (ρ, E[n], E[n_w], E[w], E[s])
3. Interpretar resultados em contexto de sistemas
4. Comparar desempenho de configurações de servidor único vs. múltiplos servidores

## Metodologia & Desenvolvimento Prático

### Questão 1 - Servidor de Autenticação Acadêmica

Dados:
- Chegada (λ) = 8 reqs/min
- Atendimento (μ) = 12 reqs/min
- Modelo: M/M/1/$\infty$/FIFO

Passo a passo:
- Utilização: $\rho = \frac{\lambda}{\mu} = \frac{8}{12} = 0,667 \implies 66,67\%$ 
- Número médio: $\text{E}[n] = \frac{\rho}{1-\rho} = \frac{0,667}{0,333} = 2$
- Número médio na fila: $\text{E}[n_w] = \frac{\rho^2}{1-\rho} = \frac{0,444}{0,333} = 1,3333$
- Tempo médio no sistema: $\text{E}[s] = \frac{1}{\mu(1-\rho} = \frac{1}{12\cdot 0,3333} = 0,25$ min
- Tempo médio de espera: $\text{E}[w] = \text{E}[s] - \frac{1}{\mu} = 0,25 - \frac{1}{12} = 0,1667$ min
- Probabilidade de haver pelo menos 4 requisições: $\text{P}(N \geq 4) = \rho^4 = (0,667)^4 = 0,198$

### Questão 2 - Balanceador com Servidores

Dados:
- Número de servidores (m) = 2
- Chegada (λ) = 8 reqs/min
- Atendimento (μ) = 12 reqs/min
- Modelo: M/M/m/$\infty$/FIFO

Passo a passo:
- Utilização (U) = $\frac{\lambda}{\mu} = \frac{2}{2} = 1$
- Utilização (ρ) = $\frac{\lambda}{m\mu} = \frac{2}{4} = 0,5 \implies 50\%$
- Probabilidade de não ter ninguém (P₀):
  $P_0 = (\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!})^{-1} = [\frac{U^0}{0!} + \frac{U^1}{1!} + \frac{U^2}{2!(1-\rho)}]^{-1} = [1+1+1]^{-1} = 0,333$
- Probabilidade de todos os servidores estarem ocupados (C(m,ρ)): 
  $P[\text{fila}] = C(m,\rho) = P_0\frac{U^m}{m!(1-\rho)} = \frac{1}{3}\cdot\frac{1}{2\cdot0,5} = 0,333 \implies 33,34\%$
- Número médio na fila (E[n_w]) = $\frac{\rho}{1-\rho} \cdot C = \frac{0,5}{0,5} \cdot 0,333 = 0,333$
- Número de requisições no sistema:
  $E[n] = E[n_w] + E[n_s] = 0,333 + 1 = 1,333$
- Tempo médio de espera na fila (E[w]): $\frac{\text{E}[n_w]}{\lambda} = \frac{0,333}{2} = 0,1667$ min
- Tempo médio de espera de resposta (E[s]): $\frac{\text{E}[n]}{\lambda} = \frac{1,333}{2} = 0,6667 \implies 40s$ min

### Questão 3 - Sistema Suporte Técnico
Modelo: M/M/1/$\infty$/FIFO
- Chegada (λ) = 9 requisições/min
- Taxa de serviço (μ) = 15 chamados/min
- Resultado: ρ = 0,6 (60%), E[n_w] = 0,9, E[s] = 0,1667 min (10s), P(N≥4) = 12,96%

### Questão 4 - Plataforma de Aulas
Modelo: M/M/1/$\infty$/FIFO
- Chegada (λ) = 42 vídeos/hora
- Taxa de serviço (μ) = 60 vídeos/hora
- Resultado: ρ = 0,7 (estável), E[n_w] = 1,633 (ultrapassa 1 vídeo), tempo médio = 3 min

### Questão 5 - Sistema de Monitoramento Industrial
Modelo: M/M/4/$\infty$/FIFO
- Chegada (λ) = 8 eventos/min
- Serviço (μ) = 3 eventos/min
- Processadores (m) = 4
- Resultado: ρ = 0,667, P₀ = 0,06, C(m,ρ) = 37,98%, E[n_w] = 0,7596, E[s] = 25,65s

### Questão 6 - Central de Protocolos
Modelo: M/M/3/$\infty$/FIFO
- Chegada (λ) = 9 solicitações/min
- Serviço (μ) = 4 solicitações/min
- Processadores (m) = 3
- Resultado: ρ = 0,75 (alta), C(m,ρ) = 56,78%, E[n_w] = 1,703, E[s] = 26,36s (acima de 10s)

### Questão 7 - Sistema Acadêmico
Modelo: M/M/1/$\infty$/FIFO
- Chegada (λ) = 12 registros/min
- Taxa de serviço (μ) = 20 registros/min
- Resultado: ρ = 0,6, E[n_w] = 0,9 (perceptível), E[s] = 7,5s, P(N≥5) = 12,96%

## Resumo de Fórmulas com Perguntas

**Cuidado com as unidades de tempo! 1h = 60 min = 3600 segundos

Um servidor, então modelo: M/M/1/$\infty$/FIFO; se tiver m servidores, então modelo: M/M/m/$\infty$/FIFO 

### Modelo - M/M/1/$\infty$/FIFO
Só tem UM único servidor:

1. Servidor opera com folga/estável? $\rho = \frac{\lambda}{\mu}$
2. A fila média é perceptível/ultrapassa? $\text{E}[n] = \frac{\rho}{1-\rho}$ e $\text{E}[n_w] = \frac{\rho^2}{1-\rho}$
3. O tempo médio fica abaixo de X segundos? $\text{E}[s] = \frac{1}{\mu(1-\rho)}\lt X$
4. Chance de haver X chamados? $P(N \geq X) = \rho^X$

### Modelo - M/M/m/$\infty$/FIFO
Tem MAIS de UM servidor (unidade de processamento)

1. Servidor opera com folga/estável? $\rho = \frac{\lambda}{m\mu}$; $U=\frac{\lambda}{\mu}$
2. A probabilidade de todos analistas estarem ocupados? $P_0 = (\frac{U^m}{m!(1-\rho)} + \sum_{n=0}^{m-1}\frac{U^n}{n!})^{-1}$ e $C(m,\rho) = \text{P}_0 \cdot \frac{U^m}{m!(1-\rho)}$
3. A fila média é perceptível/ultrapassa? $\text{E}[n_w] = \frac{\rho}{1-\rho} \cdot C(m,\rho)$; $\text{E}[n] = \text{E}[n_w] + U$
4. A espera média de ultrapassa X segundos? $\text{E}[w] = \frac{\text{E}[n]}{\lambda}\lt X$

## Resultados Obtidos & Conclusão

Os exercícios demonstram que:
- Sistemas com um único servidor (M/M/1) apresentam filas perceptíveis quando ρ > 0,5
- Adicionar múltiplos servidores reduz significativamente os tempos de espera
- Monitoramento de probabilidades (P(N≥X)) é essencial para detectar congestionamento
- A escolha entre servidor único vs. múltiplos depende do equilíbrio entre custo e desempenho

## Referências & Links

- Material: "Análise Operacional de Redes de Filas"
- Modelos de fila Markoviana: M/M/1 e M/M/m
- Fórmulas de Erlang e Lei de Little
