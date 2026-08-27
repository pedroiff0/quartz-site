---
publish: false
title: Sistemas Distribuídos
created: 2026-07-26
modified: 2026-08-27
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] O que é este tópico
> Sistemas Distribuídos é o estudo de como várias máquinas independentes — que não compartilham memória nem relógio — cooperam para parecer, do ponto de vista de quem usa, **um único sistema coerente**. Da comunicação entre processos e sincronização de relógios até a tolerância a falhas e a computação paralela em GPUs/clusters, esta trilha reúne três disciplinas do currículo (Sistemas Distribuídos, Algoritmos Distribuídos e Computação Paralela e Distribuída) porque, na prática, é a mesma família de problemas vista em escalas diferentes: da concorrência dentro de uma máquina multi-core até milhares de servidores num datacenter.

## Por que estudar isso?

Praticamente todo sistema relevante hoje é distribuído: um app de banco replica dados em vários datacenters, um serviço de streaming particiona conteúdo entre servidores, um banco de dados moderno aceita que a rede vai falhar e projeta em torno disso. A parte contraintuitiva — e o motivo de esta disciplina existir — é que **distribuir um sistema não é só "colocar mais máquinas"**: rede tem latência, pacotes se perdem, relógios de máquinas diferentes divergem, e processos podem falhar independentemente uns dos outros sem avisar. Ignorar isso é como prometer uma garantia que a física da rede simplesmente não permite.

Entender os limites fundamentais (o Teorema CAP, consistência eventual vs. forte, os modelos de falha) evita o erro mais caro em sistemas reais: prometer uma consistência que o sistema, sob partição de rede, não consegue entregar. E entender computação paralela (a outra metade desta trilha) é o que permite tirar proveito de múltiplos núcleos/GPUs/nós de um cluster — a mesma motivação, inclusive, do minicurso de [[pt-br/resource/escolainverno/computação|Computação de Alto Desempenho]] que fiz na Escola de Inverno.

## Trilha de estudo

### 1. Conceitos fundamentais e arquiteturas (2 semanas)

O que dominar: a motivação para distribuir um sistema (escalabilidade, disponibilidade, tolerância a falhas), o conceito de **transparência de distribuição** (o usuário não deveria perceber que o sistema é distribuído — transparência de acesso, localização, migração, concorrência, falha), e as duas arquiteturas clássicas: **cliente-servidor** (centralizada, papéis bem definidos) vs. **peer-to-peer** (descentralizada, todo nó pode ser cliente e servidor). O que praticar: para três sistemas que você usa no dia a dia (um app de mensagens, um serviço de streaming, um cliente de torrent), identificar qual arquitetura cada um usa e por quê.

### 2. Comunicação e sincronização (2–3 semanas)

O que dominar: modelos de interação **síncrono** (o remetente espera resposta) vs. **assíncrono** (dispara e segue em frente); por que relógios físicos de máquinas diferentes divergem e como protocolos como o NTP tentam sincronizá-los; e — mais importante — por que **relógios lógicos** (Timestamps de Lamport, Relógios Vetoriais) resolvem o problema real: não "que horas são", mas "o que aconteceu antes do quê". O que praticar: dado um diagrama de eventos em três processos trocando mensagens, atribuir timestamps de Lamport manualmente e verificar a relação de "aconteceu-antes" (_happens-before_).

### 3. Middleware e transações distribuídas (2 semanas)

O que dominar: RPC/RMI (chamar um procedimento como se fosse local, mesmo estando numa máquina remota), serviços de nomes, as propriedades **ACID** de uma transação (Atomicidade, Consistência, Isolamento, Durabilidade), e o protocolo de **Commit em Duas Fases (2PC)** para garantir que uma transação distribuída seja confirmada em todos os nós ou em nenhum. O que praticar: simular manualmente o 2PC com três participantes, incluindo o caso em que um participante falha entre a fase de votação e a de confirmação — é aí que aparece o problema real do protocolo (ele bloqueia esperando o coordenador).

### 4. Tolerância a falhas e consistência (2–3 semanas)

O que dominar: os modelos de falha (_crash_, omissão, temporização, bizantina — cada um assumindo um comportamento diferente e pior para o que pode dar errado), replicação de dados, e o espectro entre **consistência forte** (todo nó vê os mesmos dados, sempre, ao custo de disponibilidade) e **consistência eventual** (nós podem divergir temporariamente, mas convergem). O ponto alto da unidade é o **Teorema CAP**: sob uma partição de rede (P), um sistema distribuído só pode escolher entre Consistência (C) ou Disponibilidade (A) — nunca as duas ao mesmo tempo. O que praticar: para três bancos de dados distribuídos reais (ex: um relacional com replicação síncrona, o DynamoDB, o Cassandra), identificar qual lado do CAP cada um prioriza.

![O Teorema CAP: sob partição de rede (P), um sistema distribuído só pode garantir Consistência (C) ou Disponibilidade (A), nunca as duas simultaneamente.](https://commons.wikimedia.org/wiki/Special:FilePath/CAP_Theorem.svg)

### 5. Computação paralela e algoritmos distribuídos (3–4 semanas)

O que dominar: a Taxonomia de Flynn (SISD, SIMD, MISD, MIMD) para classificar arquiteturas paralelas; os modelos de programação paralela — **OpenMP** (memória compartilhada, laços paralelizados com diretivas) e **MPI** (memória distribuída, troca explícita de mensagens entre processos), os mesmos que aparecem no minicurso de HPC da Escola de Inverno; e os algoritmos distribuídos clássicos: **eleição de líder** (escolher um coordenador sem autoridade central prévia), **exclusão mútua distribuída** (o problema dos "dining/drinking philosophers" em versão distribuída, sem memória compartilhada para um mutex), detecção de terminação e de _deadlock_, e árvore geradora mínima distribuída. O que praticar: implementar (em pseudocódigo ou Python com `multiprocessing`) o algoritmo de eleição de líder em anel (_ring algorithm_) — é curto, mas ilustra bem como coordenação emerge sem um nó "especial" desde o início.

## Conceitos que você precisa dominar

- **Transparência de distribuição** — a promessa (nem sempre cumprida) de que o usuário de um sistema distribuído não deveria perceber que ele é distribuído; é o critério de design por trás de praticamente toda decisão de arquitetura desta área.
- **Relógios lógicos de Lamport** — como ordenar eventos em processos diferentes sem depender de relógios físicos sincronizados: cada processo mantém um contador que avança a cada evento e se ajusta ao receber mensagens, criando uma ordem parcial consistente com causa e efeito.
- **Commit em Duas Fases (2PC)** — protocolo em que um coordenador primeiro pergunta "todos conseguem confirmar?" (fase de votação) e só depois manda "confirmem" ou "cancelem" (fase de decisão) — garante atomicidade entre múltiplos nós, mas pode bloquear se o coordenador falhar no meio do processo.
- **Teorema CAP** — o resultado mais citado (e mais mal-citado) da área: na presença de uma partição de rede, é preciso escolher entre consistência e disponibilidade. Fora de uma partição, um sistema pode, sim, ter as duas.
- **Taxonomia de Flynn** — classifica arquiteturas paralelas por quantos fluxos de instrução e de dados processam simultaneamente; SIMD (uma instrução, muitos dados) é o modelo de GPUs, MIMD (múltiplas instruções, múltiplos dados) é o modelo de clusters.
- **OpenMP vs. MPI** — OpenMP paraleliza dentro de uma máquina com memória compartilhada (threads veem a mesma memória); MPI coordena processos em máquinas diferentes trocando mensagens explicitamente (sem memória compartilhada) — a escolha entre os dois é, no fundo, a escolha entre paralelismo e distribuição.
- **Eleição de líder** — a classe de algoritmos que resolve "como um grupo de processos, sem coordenador prévio, escolhe um entre eles pra coordenar" — problema-base de que dependem consenso, replicação e tolerância a falhas em sistemas reais.

## Erros comuns de quem está começando

- **Ignorar as Falácias da Computação Distribuída** — a lista clássica de Peter Deutsch começa com "a rede é confiável" e "a latência é zero"; todo projeto de sistema distribuído que assume qualquer uma dessas falácias quebra em produção, mais cedo ou mais tarde.
- **Achar que "distribuído" significa "mais rápido"** — coordenar múltiplos nós tem overhead (comunicação, sincronização, protocolos de consenso); um sistema distribuído mal projetado pode ser mais lento que uma versão bem otimizada rodando numa única máquina.
- **Confundir concorrência, paralelismo e distribuição** — concorrência é sobre estruturar um programa em tarefas que progridem intercaladas (mesma máquina, pode ser um único núcleo); paralelismo é sobre executar tarefas literalmente ao mesmo tempo (múltiplos núcleos/GPUs, mesma máquina); distribuição é sobre múltiplas máquinas independentes, cada uma com sua própria memória e podendo falhar sem avisar as outras.
- **Usar 2PC sem entender que ele bloqueia** — se o coordenador cai depois da fase de votação, os participantes ficam travados esperando uma decisão que pode nunca chegar; sistemas de produção usam variantes mais robustas (como protocolos baseados em consenso, ex: Raft/Paxos) justamente por causa dessa limitação.
- **Escolher consistência forte por padrão sem medir o custo** — consistência forte tende a custar disponibilidade e latência; muitos sistemas reais (carrinhos de compra, contadores de curtidas) toleram bem consistência eventual, e insistir em forte só adiciona complexidade sem benefício percebido pelo usuário.

## 📚 Materiais recomendados

### Cross-link no próprio site

- **[[pt-br/resource/escolainverno/computação|Computação de Alto Desempenho]]** — o minicurso de HPC (OpenMP/MPI) que fiz na Escola de Inverno em Astrofísica 2026 é, literalmente, a metade "computação paralela" desta trilha aplicada a processamento de dados científicos.

### Bibliografia clássica (consultar na biblioteca)

- TANENBAUM, A. S., VAN STEEN, M. _Sistemas Distribuídos: Princípios e Paradigmas_ — a referência mais didática, cobre transparência, comunicação, sincronização e tolerância a falhas na mesma ordem desta trilha.
- COULOURIS, G., DOLLIMORE, J., KINDBERG, T. _Sistemas Distribuídos: Conceitos e Projeto_ — mais orientado a middleware e transações distribuídas; bom complemento ao Tanenbaum.

## 🔗 Referências externas

- [MIT 6.824 — Distributed Systems](https://pdos.csail.mit.edu/6.824/) — curso de graduação do MIT, com todas as aulas em vídeo e material gratuitos; referência-padrão mundial na área.
- [Notes on Distributed Systems for Young Bloods](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/) — artigo curto e clássico sobre as armadilhas práticas (não só teóricas) de projetar sistemas distribuídos.
- [The Secret Lives of Data — Raft](http://thesecretlivesofdata.com/raft/) — visualização interativa do algoritmo de consenso Raft, uma ótima ponte entre a teoria de eleição de líder desta trilha e um algoritmo usado em produção (etcd, Consul).

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/9-periodo/sistemas-distribuidos|Sistemas Distribuídos]] — a disciplina do 9º período que cobre as etapas 1 a 4 desta trilha: conceitos, comunicação, middleware e tolerância a falhas.
- [[pt-br/resource/engenharia-de-computação/eletivas/algoritmos-distribuidos|Algoritmos Distribuídos]] — eletiva que aprofunda a etapa 5: modelos síncrono/assíncrono, algoritmos de eleição e exclusão mútua.
- [[pt-br/resource/engenharia-de-computação/eletivas/computacao-paralela-e-distribuida|Computação Paralela e Distribuída]] — eletiva-continuação que foca na parte de arquiteturas paralelas (OpenMP/MPI/CUDA) da etapa 5.
