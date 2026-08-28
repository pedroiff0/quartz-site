---
publish: false
title: Engenharia de Software
created: 2026-07-18 13:04
modified: 2026-08-27 21:59
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] Engenharia de software é a disciplina de construir sistemas que sobrevivem ao mundo real: requisitos que mudam, equipes que crescem, código que precisa ser mantido por anos. É a diferença entre programar e construir software que dura.

## Por que estudar isso?

Qualquer um resolve um exercício de programação sozinho num fim de semana. Agora imagine um sistema de gestão hospitalar: 15 desenvolvedores, 5 anos de vida útil mínima, requisitos que mudam a cada norma nova da saúde, e zero tolerância a perder o prontuário de um paciente. Nenhuma genialidade individual sustenta isso — o que sustenta é processo: requisitos bem levantados, arquitetura que isola mudanças, testes automatizados, versionamento disciplinado. Projetos de software falham com frequência assustadora, e as autópsias quase sempre apontam para as mesmas causas: requisitos mal entendidos, ausência de testes, código que ninguém mais consegue modificar.

Há também um motivo egoísta: as perguntas difíceis de entrevistas para vagas plenas e seniores raramente são sobre sintaxe — são sobre design ("como você estruturaria esse sistema?", "por que essa classe está errada?"). Engenharia de software é o que faz você progredir de "escreve código que funciona" para "projeta sistemas nos quais outras pessoas conseguem trabalhar".

## Trilha de estudo

### 1. Processos e ciclo de vida (iniciante)

Entenda o problema que a área resolve: por que software atrasa, estoura orçamento e falha. Estude os modelos de processo (cascata, iterativo, ágil) menos como receitas e mais como respostas a contextos diferentes. Aprenda o ciclo completo: requisitos, projeto, implementação, testes, manutenção. Pratique escrevendo requisitos e casos de uso para um sistema pequeno. Tempo típico: 4 a 6 semanas.

### 2. Orientação a objetos e UML (intermediário)

Domine os pilares de OO de verdade — encapsulamento, herança, polimorfismo, abstração — não como definições de prova, mas como ferramentas de gerenciamento de dependências. Aprenda os diagramas UML que o mercado realmente usa: classes, sequência e casos de uso. Pratique modelando um sistema completo antes de implementá-lo. Tempo típico: 6 a 8 semanas.

### 3. Princípios de design e padrões (intermediário-avançado)

Estude os princípios SOLID e o vocabulário de padrões de projeto (Strategy, Observer, Factory, Adapter...) — o [Refactoring Guru](https://refactoring.guru/) é excelente e gratuito para isso. A prática essencial: pegar código seu de seis meses atrás e refatorá-lo aplicando os princípios, sentindo na pele o que acoplamento alto custa. Tempo típico: 6 a 8 semanas.

### 4. Arquitetura, testes e entrega (avançado)

Suba de altitude: camadas, arquitetura hexagonal, monólito vs. microsserviços, e os artigos do [Martin Fowler](https://martinfowler.com/) como guia. Em paralelo, leve testes a sério: pirâmide de testes, TDD, integração contínua. Pratique num projeto de verdade com equipe — o material de [[pt-br/resource/computacao/pratica-profissional|Prática Profissional]] complementa. Tempo típico: 8+ semanas, contínuo pela carreira.

## Conceitos que você precisa dominar

- **Engenharia de requisitos** — descobrir, negociar e documentar o que o sistema deve fazer, distinguindo requisitos funcionais (o que faz) de não funcionais (quão rápido, quão seguro, quão disponível). É a fase mais barata para errar e corrigir: um requisito mal entendido descoberto em produção custa ordens de magnitude mais do que descoberto na entrevista com o cliente.
- **Coesão e acoplamento** — o par de forças que resume todo o design de software: cada módulo deve fazer uma coisa bem definida (alta coesão) e depender pouco dos outros (baixo acoplamento). Praticamente todo princípio, padrão e arquitetura da área é uma técnica para melhorar essas duas métricas.
- **Encapsulamento e abstração** — esconder o _como_ atrás de uma interface que expõe só o _o quê_. É o que permite trocar a implementação de um módulo sem quebrar o resto do sistema — e é a razão de "atributos privados" existirem, não burocracia de linguagem.
- **Princípios SOLID** — cinco princípios de design OO; o mais rentável é o da responsabilidade única (uma classe, um motivo para mudar) e o de depender de abstrações, não de implementações concretas. Não são dogmas: são heurísticas para manter o custo de mudança baixo.
- **Padrões de projeto** — soluções nomeadas para problemas recorrentes de design (Strategy para variar comportamento, Observer para notificação, Factory para criação). O maior valor é o vocabulário compartilhado: dizer "usa um Adapter aí" comunica em duas palavras o que levaria um parágrafo.
- **Testes automatizados** — testes de unidade, integração e sistema, escritos como código e rodando a cada mudança. Mais que pegar bugs, testes são uma rede de segurança que permite refatorar sem medo — sem eles, o código apodrece porque ninguém ousa mexer.
- **Controle de versão e integração contínua** — Git como ferramenta de colaboração (branches, merges, revisão de código) e CI como garantia de que o projeto compila e passa nos testes a cada commit. É o sistema circulatório de qualquer equipe moderna; entrar no mercado sem fluência em Git não é opção.
- **Dívida técnica** — a metáfora contábil para atalhos de design: você ganha velocidade agora e paga juros em manutenção depois. O conceito importa porque dívida técnica não é sempre errada — é uma decisão econômica que precisa ser tomada conscientemente e paga antes de virar bola de neve.

## Erros comuns de quem está começando

- **Achar que engenharia de software é burocracia que atrasa o código.** Em projeto de uma pessoa e um mês, é mesmo. O valor aparece com escala — mais gente, mais tempo, mais mudanças — e quem só treinou em projetos-solo subestima brutalmente isso no primeiro emprego.
- **Aplicar padrões de projeto onde não precisa.** Depois de aprender padrões, tudo parece pedir um Factory com Strategy dentro de um Singleton. Padrão é resposta a um problema; sem o problema, é só complexidade extra. Comece simples e refatore quando a necessidade aparecer.
- **Escrever testes depois, "quando der tempo".** Nunca dá tempo. Teste escrito junto com o código sai barato e molda um design melhor; teste adiado vira uma montanha intransponível e o projeto fica refém do medo de mudar.
- **Confundir "funciona" com "está bom".** Código que passa no teste manual mas ninguém entende é passivo, não ativo. O leitor mais provável do seu código é você mesmo em seis meses — escreva para ele.
- **Ignorar requisitos não funcionais até o fim.** Desempenho, segurança e disponibilidade não se "adicionam depois": moldam a arquitetura desde o início. Descobrir na entrega que o sistema precisava aguentar 10× a carga é refazer, não ajustar.

## 📚 Materiais recomendados

**Livros abertos (licença pública):**

- **[Análise e Projeto de Sistemas](/assets/biblioteca/computacao/analise-projeto-sistemas-ifb.pdf)** (IFB, licença Creative Commons) — livro aberto de instituto federal cobrindo o ciclo de análise e projeto com notação UML. Disponível no portal [Proedu](https://proedu.rnp.br), repositório público da Rede e-Tec.
- **[Análise de Sistemas](/assets/biblioteca/computacao/analise-de-sistemas-etec.pdf)** (Rede e-Tec Brasil / MEC) — apostila introdutória de levantamento de requisitos e análise. Também no [Proedu](https://proedu.rnp.br).
- **[Projeto de Sistemas](/assets/biblioteca/computacao/projeto-de-sistemas-etec.pdf)** (Rede e-Tec Brasil / MEC) — a continuação: do modelo de análise ao projeto implementável. No [Proedu](https://proedu.rnp.br).

**Bibliografia clássica (procure na biblioteca do campus):**

- SOMMERVILLE, I. _Engenharia de Software_. O livro-texto padrão da disciplina no mundo todo: processos, requisitos, projeto, testes e manutenção com visão panorâmica.
- PRESSMAN, R. _Engenharia de Software: uma abordagem profissional_. O outro clássico, com pegada mais prescritiva e orientada à prática profissional; ótimo contraponto ao Sommerville.

## 🔗 Referências externas

- [Roadmap: Software Design & Architecture](https://roadmap.sh/software-design-architecture) — a trilha que conecta código limpo, princípios de design, padrões e arquitetura numa progressão única. O melhor mapa geral da área.
- [Roadmap: Software Architect](https://roadmap.sh/software-architect) — visão de mais longo prazo: o que um arquiteto de software precisa dominar. Útil para enxergar aonde a trilha leva.
- [Refactoring Guru](https://refactoring.guru/) — o melhor material gratuito sobre padrões de projeto e refatoração, com ilustrações e exemplos em várias linguagens. Use na etapa 3 da trilha.
- [martinfowler.com](https://martinfowler.com/) — o blog de referência em design e arquitetura: refatoração, microsserviços, integração contínua. Leitura de cabeceira permanente da área.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/5-periodo/engenharia-de-software|Engenharia de Software]] — processos, requisitos e ciclo de vida: o panorama da área.
- [[pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos|Análise de Software Orientada a Objetos]] — modelagem OO e UML: transformar requisitos em modelos.
- [[pt-br/resource/engenharia-de-computação/7-periodo/projeto-de-software-orientado-a-objetos|Projeto de Software Orientado a Objetos]] — do modelo ao design implementável: princípios, padrões e arquitetura.
