---
publish: false
title: Atividade 01 - Atividade Modelagem - SoftBridge
created: 2026-04-11 14:49
modified: 2026-09-19 13:18
encrypted: true
tags:
- atividade
- trabalho
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---
# Atividade 01 - Atividade Modelagem - SoftBridge

## Resumo Executivo

Modelo conceitual para sistema de gerenciamento de projetos de software SoftBridge. A análise identifica entidades principais (Clientes, Contratos, Projetos, Funcionários, Tarefas, Tecnologias, Parcelas), seus atributos e relacionamentos, diferenciando entidades fortes de fracas.

## Informações & Checklist de Entrega

Dados:
- Sistema: SoftBridge
- Modelo: CONCEITUAL
- Entidades: Clientes, Contratos, Projetos, Funcionários, Tarefas, Tecnologias, Parcelas de pagamento

## Objetivos do Trabalho

1. Identificar entidades do domínio
2. Definir atributos relevantes
3. Identificar e mapear relacionamentos
4. Indicar cardinalidades mínimas e máximas
5. Classificar entidades como fortes ou fracas
6. Desenhar diagrama ER conceitual

## Metodologia & Desenvolvimento Prático

### Cliente

Atributos:
1. CNPJ
2. Razão Social
3. Nome Fantasia
4. e-mail
5. Telefone

Cliente pode firmar nenhum, um ou vários contratos, mas só pode estar associado a um único cliente, ou seja relação N:1

Relacionamentos: 
Cliente (0,N) firma Contrato (1,1)

### Contrato

Atributos:
1. Número
2. Data de assinatura
3. Valor global
4. Prazo em meses
5. Situação

Todo contrato implica um projeto de software 
Cada projeto está associado a um contrato, ou seja relação 1:1
Cada contrato deve possuir uma ou mais parcelas.

Relacionamentos:
- Contrato (1,1) formaliza Projeto (1,1)
- Contrato (1,N) possui Parcelas (1,1)

### Projeto

Atributos:
1. Código de projeto -> identificador único
2. Nome
3. Descrição
4. Data Início
5. Data Término
6. Status

Todo projeto é coordenado por UM funcionário (1:1)
Um funcionário coordena nenhum, um, ou vários projetos (1:N)
Cada projeto deve ter pelo menos UMA ou mais tecnologias
Um projeto possui uma ou mais tarefas

Relacionamentos:
- Projeto (0,N) possui Tarefa (1,1)
- Projeto (1,N) utiliza Tecnologia (0,N)

### Funcionários

Atributos:
1. Matricula
2. Nome
3. e-mail
4. Cargo
5. Nível senioridade

Um funcionário atua em nenhum, um ou vários projetos (1:N)

Relacionamentos:
- Funcionário (0,N) coordenada Projeto (1,1)
- Funcionário (0,N) atua Projeto (1,N)
- Funcionário (0,N) é responsável por Tarefa (1,1)

### Tarefas

Atributos:
1. Código da tarefa -> identificador único
2. Titulo
3. Descrição
4. Prioridade
5. Data inicio
6. Data termino
7. Situação

Toda tarefa pertence a um único projeto

Relacionamentos:
- Tarefa (0,1) depende de Tarefa (0,N)

### Tecnologias

Atributos:
1. Sigla
2. Nome
3. Categoria

Uma tecnologia pode ser utilizada em um ou vários projetos

### Parcelas

Atributos:
1. Número
2. Data de vencimento
3. valor previsto
4. data de pagamento
5. status de pagamento

Pertence a um único contrato
Uma parcela não existe sem o respectivo contrato, e só é identificada pela combinação entre o número contrato e o número de parcela.

## Análise de Alternativas

1. Identificar as entidades do domínio: 
   Clientes, funcionários, projetos, tarefas, contratos, parcelas

2. Definir os atributos relevantes de cada entidade: 
   Feito acima

3. Identificar os relacionamentos existentes: 
   Feito acima

4. Indicar as cardinalidades mínimas e máximas de cada relacionamento: 
   Feito acima

5. Apontar, se houver, entidades fortes e entidades fracas: 
   Todas são fortes, exceto Parcelas, que depende de Contrato para que seja identificada. Tarefas deveria ser fraca se não fosse a regra de negócio que ela é única em todo o sistema.

6. Desenhar o diagrama entidade-relacionamento conceitual correspondente:
   ![[Conceitual_1.png]]

## Dúvidas & Resolução

> [!NOTE] Dúvidas
> Como saber o que é fraco e forte, e pq diferenciar?

Resolução: Entidades fortes possuem existência independente e chave primária própria no banco de dados. Já entidades fracas dependem de uma entidade forte (proprietária) para existir, não possuem chave primária única, utilizando uma chave parcial combinada com a chave da entidade forte para identificação.

## Resultados Obtidos & Conclusão

O modelo conceitual SoftBridge identifica 7 entidades principais com 28 atributos e múltiplos relacionamentos. A análise destaca que Parcelas é uma entidade fraca dependente de Contratos, enquanto as demais são fortes. O diagrama ER conceitual mapeia todas as associações e cardinalidades.

## Referências & Links

Modelagem Conceitual - Parte I
