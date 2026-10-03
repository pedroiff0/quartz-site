---
publish: true
title: Aula 01 - Comparação de Funções de Tempo
created: 2026-06-11 14:49
modified: 2026-10-02 17:13
encrypted: true
tags:
- aula
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
discipline: '[[projeto-e-analise-de-algoritmos]]'
sitesync: true
---
<div class="progress-bar-container" style="background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 8px; padding: 12px 16px; margin: 1.5rem 0;">
  <div style="font-weight: 600; font-size: 0.85rem; color: var(--dark, #334155); margin-bottom: 6px;">Progresso das Aulas da Disciplina</div>
  <div style="background: var(--lightgray, #e2e8f0); border-radius: 4px; overflow: hidden; height: 8px;">
    <div style="background: var(--secondary, #6d28d9); width: 10%; height: 100%;"></div>
  </div>
</div>

# Aula 01 - Comparação de Funções de Tempo

## Anotações do Quadro & Conteúdo

Dadas duas funções de tempo de execução:

$$T_1(n) = n^2 - 600n + 150000$$
$$T_2(n) = 2n^2 - 1200n + 200000$$

Questões a responder:
1. Para que tamanho da entrada T1 é mais rápido que T2? 
2. Para que tamanho da entrada T2 é mais rápido que T1?
3. Para que tamanho da entrada os dois executam em tempos iguais?

Igualando as funções:
$$T_1 = T_2$$
$$n^2 - 600n + 150000 = 2n^2 - 1200n + 200000$$

## Resumo Conceitual

Análise comparativa de complexidade de tempo entre dois algoritmos através de suas funções polinomiais. Determinar os pontos de intersecção permite identificar qual algoritmo é mais eficiente para diferentes tamanhos de entrada.

## Esquemas & Anotações Visuais

Gráfico comparativo das duas funções de tempo, mostrando os intervalos onde cada uma é mais rápida.

## Dúvidas & Exercícios Recomendados

- Completar a resolução das equações T1 = T2
- Plotar ambas as funções em gráfico
- Determinar domínios de eficiência de cada algoritmo
- Praticar análise asintótica com outras funções
