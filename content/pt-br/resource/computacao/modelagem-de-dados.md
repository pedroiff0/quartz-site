---
publish: false
title: Modelagem de Dados
created: 2026-07-18
modified: 2026-08-27
published: 2026-07-26T11:33:09.975-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] Modelagem de dados é a etapa de projeto que vem antes de qualquer `CREATE TABLE`: entender o domínio do problema, identificar entidades e relacionamentos, e desenhar uma estrutura que represente a realidade sem redundância nem ambiguidade. É a planta baixa do banco de dados.

## Por que estudar isso?

Imagine o sistema acadêmico do IFF projetado às pressas: o nome do aluno gravado em cada linha de nota, em vez de numa tabela própria. O aluno corrige o nome no cadastro — e agora metade dos registros tem o nome novo e metade tem o antigo. Qual está certo? Esse tipo de inconsistência não é bug de código: é defeito de modelagem, e não há programação que conserte depois. Sistemas reais morrem disso — a manutenção vira um campo minado onde cada mudança quebra três coisas.

A modelagem é também a habilidade de tradução mais importante do curso: converter o que o cliente descreve em português impreciso ("todo aluno se matricula em disciplinas, mas só pode cursar as que não têm pré-requisito pendente...") em um diagrama formal e sem ambiguidade. Quem modela bem entende o negócio melhor que muita gente do próprio negócio — e isso vale ouro em qualquer equipe.

## Trilha de estudo

### 1. Modelo entidade-relacionamento (iniciante)

Aprenda os blocos básicos: entidade, atributo, relacionamento, e principalmente cardinalidade (1:1, 1:N, N:N). Pratique modelando domínios que você conhece de cor: a biblioteca do campus, um campeonato de futebol, um app de delivery. Compare seu diagrama com o de um colega — as diferenças geram as melhores discussões. Tempo típico: 3 a 4 semanas.

### 2. Do conceitual ao lógico (intermediário)

Aprenda as regras de mapeamento: entidade vira tabela, relacionamento N:N vira tabela associativa, atributo multivalorado vira tabela própria. Entenda a diferença entre os três níveis — conceitual (ER), lógico (relacional) e físico (SQL de um SGBD específico) — e por que cada um existe. Pratique convertendo seus diagramas da etapa 1 em esquemas relacionais completos. Tempo típico: 3 a 4 semanas.

### 3. Normalização (intermediário)

Domine as três primeiras formas normais e as anomalias que cada uma elimina. O exercício clássico: pegar uma planilha "tudo numa tabela só" (uma nota fiscal, um histórico escolar) e normalizar passo a passo até a 3FN, justificando cada divisão. Entenda também quando desnormalizar deliberadamente é aceitável. Tempo típico: 3 a 4 semanas.

### 4. Modelagem no mundo real (avançado)

Casos que os livros simplificam: dados temporais (histórico de preços, vigência de contratos), hierarquias, herança/generalização no ER, e modelagem para requisitos que mudam. Pratique fazendo engenharia reversa: pegue um sistema aberto, olhe o esquema do banco e tente reconstruir o diagrama ER — e critique as decisões que encontrar. Tempo típico: 4 a 6 semanas.

## Conceitos que você precisa dominar

- **Entidade vs. atributo** — entidade é algo com identidade própria sobre o qual guardamos dados; atributo é uma propriedade de uma entidade. A dúvida clássica ("endereço é atributo ou entidade?") se resolve perguntando: precisa de identidade própria, tem atributos próprios, se relaciona com outras coisas? O contexto do sistema decide.
- **Cardinalidade** — quantas instâncias de uma entidade se associam a quantas da outra: 1:1, 1:N ou N:N. É a decisão mais importante do diagrama, porque cardinalidade errada gera estrutura de tabelas errada — e descobrir isso com o sistema pronto custa caro.
- **Relacionamento N:N e tabela associativa** — o modelo relacional não implementa N:N diretamente; a solução é uma tabela intermediária (Aluno–Matrícula–Disciplina). Essas tabelas associativas frequentemente ganham atributos próprios (a nota vive na matrícula, não no aluno nem na disciplina) e viram entidades de pleno direito.
- **Chave primária e chaves candidatas** — o identificador único de cada linha. A discussão entre chave natural (CPF, matrícula) e chave artificial (ID sequencial) é real e cheia de nuances: chaves naturais mudam mais do que se imagina, e essa é a razão de tanta gente preferir IDs artificiais.
- **Dependência funcional** — a noção formal por trás da normalização: o atributo X determina Y se cada valor de X corresponde a um único Y. As formas normais são, no fundo, regras sobre onde cada dependência funcional pode morar. Entendeu dependência funcional, a normalização deixa de ser receita decorada.
- **Formas normais (1FN, 2FN, 3FN)** — 1FN elimina atributos multivalorados; 2FN elimina dependências parciais da chave; 3FN elimina dependências transitivas. Cada uma remove uma família específica de anomalias de inserção, atualização e exclusão — saiba dar um exemplo de anomalia para cada.
- **Generalização e especialização** — quando entidades compartilham atributos (Pessoa → Aluno, Professor), o ER permite hierarquias tipo herança. O mapeamento para tabelas tem três estratégias clássicas (tabela única, uma por subtipo, uma por tipo concreto), cada uma com prós e contras de desempenho e integridade.

## Erros comuns de quem está começando

- **Modelar pensando nas telas do sistema, não no domínio.** O formulário de cadastro muda toda hora; a natureza dos dados, não. Modele o que as coisas _são_, e as telas que se adaptem.
- **Errar cardinalidade por não interrogar o domínio.** "Um aluno tem um endereço" — sempre? E histórico de endereços? E aluno com residência em duas cidades? Cardinalidade se descobre fazendo perguntas chatas, não assumindo o caso comum.
- **Criar a tabela antes do diagrama.** Ir direto pro SQL parece produtivo, mas pula exatamente a etapa em que erros são baratos de corrigir. Diagrama se apaga com borracha; tabela em produção se migra com dor.
- **Normalizar no automático, sem entender a anomalia que está evitando.** Isso leva tanto a subnormalizar (redundância escondida) quanto a hipernormalizar (JOINs infinitos para qualquer consulta trivial). A forma normal é meio, não fim.
- **Guardar dados calculáveis sem necessidade.** Idade (calculável da data de nascimento), total do pedido (soma dos itens): armazenar cópias que podem divergir da fonte é redundância clássica. Há exceções legítimas por desempenho — mas precisam ser decisões conscientes.

## 📚 Materiais recomendados

**Livros abertos (licença pública):**

- **[Introdução a Banco de Dados](/assets/biblioteca/computacao/introducao-banco-de-dados-etec.pdf)** (Rede e-Tec Brasil) — os capítulos de modelo ER e normalização cobrem o núcleo desta trilha, em português e com exemplos acessíveis. Disponível no portal [Proedu](https://proedu.rnp.br), repositório público da Rede e-Tec.

**Bibliografia clássica (procure na biblioteca do campus):**

- HEUSER, C. A. _Projeto de Banco de Dados_. O livro brasileiro de referência em modelagem — enxuto, direto e com a notação ER mais usada nas disciplinas do país. Se for ler um só, é este.

## 🔗 Referências externas

- [Roadmap: SQL](https://roadmap.sh/sql) — os primeiros blocos do roadmap cobrem modelo relacional e design de esquema; bom para ver como a modelagem desemboca no SQL.
- [SQLBolt](https://sqlbolt.com/) — pratique consultas sobre esquemas prontos e observe como um bom design torna as consultas naturais — e como um design ruim as torna tortuosas.
- [PostgreSQL](https://www.postgresql.org/) — implemente seus modelos num SGBD de verdade: constraints, chaves estrangeiras e tipos ricos do Postgres mostram seu diagrama funcionando (ou quebrando) na prática.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/5-periodo/modelagem-de-dados|Modelagem de Dados]] — a disciplina que este guia acompanha diretamente: ER, mapeamento e normalização.
- [[pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados|Banco de Dados]] — onde o modelo vira sistema: SQL, transações e a implementação de tudo que foi projetado aqui.
