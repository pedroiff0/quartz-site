---
publish: true
titulo:  260411-Aula-AtividadeModelagem-1
disciplina:
conteudo:
professor:
created: 2026-04-11 14:49
modified: 2026-08-27 14:49
tags:
cssclasses:
  - page-grid
  - center-images

---
# Notas de Aula - AtividadeModelagem
***
## Questão 1
***
### Dados
SoftBridge;
Modelo CONCEITUAL $\rightarrow$ Clientes, Contratos, Projetos, Funcionários, Tarefas, Tecnologias, Parcelas de pagamento. 
***
### Cliente:
1. CNPJ
2. Razão Social
3. Nome Fantasia
4. e-mail
5. Telefone
Cliente pode firmar nenhum, um ou vários [[#Contrato]], mas só pode estar associado a um único cliente, ou seja relação N:1

Relacionamentos: 
Cliente (0,N) firma Contrato (1,1)
***
### Contrato:
1. Número
2. Data de assinatura
3. Valor global
4. Prazo em meses
5. Situação
Todo contrato implica um [[#Projeto]] de software 
Cada projeto está associado a um contrato, ou seja relação 1:1
Cada contrato deve possuir uma ou mais [[#Parcelas]].

Relacionamentos
Contrato (1,1) formaliza Projeto (1,1)
Contrato (1,N) possui Parcelas (1,1)

***
### Projeto
1. Código de projeto -> identificador unico
2. Nome
3. Descrição
4. Data Inicio
5. Data Termino
6. Status
Todo projeto é coordenado por UM funcionário (1:1)
Um [[#Funcionários]] coordena nenhum, um, ou vários projetos (1:N)
Cada projeto deve ter pelo menos UMA ou mais [[#Tecnologias]]
Um projeto possui uma ou mais tarefas

Relacionamentos
Projeto (0,N) possui Tarefa (1,1)
Projeto (1,N) utiliza Tecnologia (0,N)

***
### Funcionários
1. Matricula
2. Nome
3. e-mail
4. Cargo
5. Nível senioridade
Um funcionário atua em nenhum, um ou vários [[#Projeto]] (1:N)

Relacionamentos
Funcionário (0,N) coordenada Projeto (1,1)
Funcionário (0,N) atua Projeto (1,N)
Funcionário (0,N) é responsável por Tarefa (1,1)

***
### Tarefas
1. Código da tarefa -> identificador único
2. Titulo
3. Descrição
4. Prioridade
5. Data inicio
6. Data termino
7. Situação
Toda tarefa pertence a um único [[#Projeto]]

Relacionamentos
Tarefa (0,1) depende de Tarefa (0,N)

***
### Tecnologias
1. Sigla
2. Nome
3. Categoria
Uma tecnologia pode ser utilizada em um ou vários [[#Projeto]]
***
### Parcelas
1. Número
2. Data de vencimento
3. valor previsto
4. data de pagamento
5. status de pagamento
Pertence a um unico contrato
Uma parcela não existe sem o respectivo [[#Contrato]], e só é identificada pela combinação entre o número contrato e o número de parcela;
***
### Alternativas
1. Identificar as entidades do domínio. 
Clientes, funcionários, projetos, tarefas, contratos, parcelas

2. Definir os atributos relevantes de cada entidade. 
Feito acima: [[#Cliente]], [[#Contrato]], [[#Projeto]], [[#Funcionários]], [[#Tarefas]], [[#Tecnologias]], [[#Parcelas]]

3. Identificar os relacionamentos existentes. 
Feito acima: [[#Cliente]], [[#Contrato]], [[#Projeto]], [[#Funcionários]], [[#Tarefas]], [[#Tecnologias]], [[#Parcelas]]

4. Indicar as cardinalidades mínimas e máximas de cada relacionamento. 
Feito acima: [[#Cliente]], [[#Contrato]], [[#Projeto]], [[#Funcionários]], [[#Tarefas]], [[#Tecnologias]], [[#Parcelas]]

5. Apontar, se houver, entidades fortes e entidades fracas. 
Todas são fortes, exceto a [[#Parcelas]], que depende de [[#Contrato]] para que seja identificada. [[#Tarefas]] deveria ser fraco se não fosse a regra de negócio que ela é única em todo o sistema.


6. Desenhar o diagrama entidade-relacionamento conceitual correspondente.
![[Conceitual_1.png]]

***

> [!NOTE] Dúvidas
> Como saber o que é fraco e forte, e pq diferenciar?
> R: ==Entidades fortes possuem existência independente e chave primária própria no banco de dados. Já entidades fracas dependem de uma entidade forte (proprietária) para existir, não possuem chave primária única, utilizando uma chave parcial combinada com a chave da entidade forte para identificação==.





***
