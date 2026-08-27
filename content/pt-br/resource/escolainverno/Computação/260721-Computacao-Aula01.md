---
publish: true
encrypted: true
titulo: 260721-Computacao-Aula01
disciplina: Computação Científica de Alto Desempenho
conteudo: Introdução à Computação de Alto Desempenho (HPC) — paralelismo com OpenMP e MPI
professor: Fernando Roig
criado: terça-feira 21/07/2026 14:00
modificado: 22/07/2026
tags:
  - escola-de-inverno-on
  - hpc
  - computacao-paralela
  - openmp
  - mpi
cssclasses:
  - page-grid
  - center-images
---
# Notas de Aula — Computação de Alto Desempenho (Aula 01)

> [!info] Informações da aula
> **Título:** Computação de Alto Desempenho (HPC)
> **Professor:** Prof. Dr. Fernando Roig

---

## 🎯 Visão geral

Muitos problemas de astrofísica (simulações de N corpos, hidrodinâmica, aprendizado de máquina em grandes catálogos) são grandes demais para rodar em um único computador em tempo razoável. A **Computação de Alto Desempenho (HPC)** resolve isso dividindo o trabalho entre muitos processadores que rodam **simultaneamente** — o que chamamos de **computação paralela**. A aula introduz os dois grandes paradigmas de paralelismo (memória compartilhada e memória distribuída) e as duas ferramentas mais usadas para programá-los: **OpenMP** e **MPI**.

![Supercomputador Pleiades (NASA): um cluster HPC é formado por milhares de nós de computação (CPU/GPU) conectados por uma rede de alta velocidade.](https://commons.wikimedia.org/wiki/Special:FilePath/Pleiades_supercomputer.jpg)

### 📑 Tópicos abordados
1. O que é HPC e por que usar programação paralela
2. Processos, threads e os dois modelos de memória
3. OpenMP (memória compartilhada)
4. MPI (memória distribuída)

---

## 1. O que é HPC?

- Uso de **supercomputadores** (clusters de muitos computadores conectados, chamados **nós**) para rodar **computação paralela** — muitas operações acontecendo ao mesmo tempo, em vez de sequencialmente.
- Aplicado a problemas de ciência de dados e engenharia de software que são grandes demais (em volume de dados ou custo computacional) para um único processador.
- Cada nó do cluster pode conter **CPUs** (processadores generalistas, poucos núcleos rápidos) e/ou **GPUs** (milhares de núcleos simples, ótimas para operações repetitivas em paralelo, como álgebra linear).

### Por que programação paralela?
Processadores individuais praticamente pararam de ficar mais rápidos (limites físicos de frequência/dissipação de calor); o ganho de desempenho hoje vem de ter **mais núcleos trabalhando ao mesmo tempo**. Isso exige repensar como escrevemos código: em vez de uma sequência de instruções, precisamos dividir o trabalho em partes independentes que podem rodar simultaneamente.

---

## 2. Processos, threads e os dois modelos de memória

- **Thread:** uma linha de execução — a menor unidade de trabalho que a CPU processa. Múltiplas threads podem rodar em paralelo em núcleos diferentes.
- **Processo:** um programa em execução, com **memória própria** isolada de outros processos.

Existem dois paradigmas principais para organizar o paralelismo:

### Memória distribuída (MPI)
- Cada processo tem seu **próprio espaço de memória**, isolado dos demais.
- Processos só compartilham dados por **troca explícita de mensagens** — cada processo precisa indicar explicitamente o que envia e o que espera receber.
- Escala bem para **muitos nós** (até milhares), pois não depende de memória física compartilhada.
- Ferramenta padrão: **MPI** (Message Passing Interface, ver seção 4).

### Memória compartilhada (OpenMP)
- Múltiplas threads dentro do **mesmo processo** compartilham o mesmo espaço de memória — comunicação é implícita, via leitura/escrita direta nas variáveis compartilhadas.
- Ferramenta padrão: **OpenMP** (ver seção 3).
- Riscos específicos desse modelo:
  - **Controle de acesso concorrente:** duas threads acessando/alterando o mesmo dado ao mesmo tempo pode gerar inconsistência.
  - **Não-determinismo:** a ordem de execução das threads não é garantida, então o resultado pode variar entre execuções se o código não for escrito com cuidado.
  - **Condição de corrida (race condition):** exemplo clássico — `sum += valor_local;` executado por várias threads simultaneamente pode "perder" incrementos, pois a operação não é atômica (lê, soma, escreve — e outra thread pode interferir no meio).

> [!tip] Como evitar condições de corrida
> **Exclusão mútua** (mutex/lock): apenas uma thread pode executar a seção crítica por vez.
> **Barreiras de sincronização:** forçam todas as threads a esperarem um certo ponto antes de continuar — garantem consistência, mas **reduzem o paralelismo** (threads ficam ociosas esperando).

### Desempenho e escalabilidade
- **Problema do serialismo:** toda parte do código que *não* pode ser paralelizada limita o ganho máximo de desempenho, não importa quantos núcleos você adicione (ideia central por trás da **Lei de Amdahl**).
- **Sincronização tem custo:** locks e barreiras, embora necessários, introduzem overhead (tempo perdido esperando).
- **Acesso à memória é o gargalo mais comum:** mesmo com muitos núcleos, se todos competem pelo mesmo barramento de memória, o ganho de velocidade é limitado.

---

## 3. OpenMP — paralelismo de memória compartilhada

**OpenMP** é uma API (conjunto de diretivas de compilador) para programação paralela em memória compartilhada, mais usada em C/C++/Fortran. Seu uso mais comum é a **paralelização de laços (loops)** — o caso ideal, já que iterações independentes de um `for` podem ser distribuídas entre threads sem conflito.

```c
#pragma omp parallel for
for (int i = 0; i < N; i++) {
    // cada iteração roda em uma thread diferente
}
```

### Escopo de variáveis
Definir corretamente o escopo de cada variável é essencial para evitar bugs de concorrência:

| Escopo | Significado |
|---|---|
| `shared` | Variável compartilhada por todas as threads (cuidado com condições de corrida) |
| `private` | Cada thread tem sua própria cópia privada da variável |
| `default(none)` | Obriga o programador a declarar explicitamente o escopo de cada variável — **boa prática**, evita erros silenciosos |
| `num_threads(n)` | Solicita explicitamente o número de threads a usar |

### Seções `critical` e `reduction`
- **`critical`:** marca uma seção de código que só pode ser executada por uma thread de cada vez (exclusão mútua explícita).
- **`reduction`:** cada thread acumula um resultado parcial em uma cópia privada, e o OpenMP combina (soma, por exemplo) todas as cópias no final — evita o custo de sincronização repetida do `critical` e é a forma preferida de somar valores em paralelo (resolve diretamente o problema da condição de corrida citado acima).

### Balanceamento de carga e escalonamento
Nem sempre as iterações de um laço custam o mesmo tempo de processamento — é preciso balancear a carga entre as threads (**particionamento**). A diretiva `schedule` controla como as iterações são distribuídas:

| Tipo | Comportamento |
|---|---|
| `static` | Divide as iterações em blocos fixos, definidos antes da execução |
| `dynamic` | Distribui iterações sob demanda, conforme as threads terminam seu bloco anterior — melhor para cargas desiguais |
| `guided` | Como `dynamic`, mas com blocos que diminuem de tamanho ao longo da execução |

**Exemplos de aplicação:** simulações físicas (ex.: problema de N corpos), processamento de imagens, treinamento de modelos de aprendizado de máquina.

---

## 4. MPI — paralelismo de memória distribuída

Quando o problema é grande demais para caber (ou processar) em um único nó com memória compartilhada, passamos para o **MPI (Message Passing Interface)** — o padrão para programação em **memória distribuída**, com muitos processos rodando potencialmente em **muitos nós físicos diferentes**.

![Arquitetura de memória distribuída: cada nó tem processador e memória próprios, comunicando-se pela rede — o modelo que o MPI programa.](https://commons.wikimedia.org/wiki/Special:FilePath/Hpc-cluster-basic.png)

- Modelo típico: **SPMD** (*Single Program, Multiple Data*) — todos os processos rodam o **mesmo código**, mas cada um opera sobre uma parte diferente dos dados.
- Cada processo tem um identificador único, o **rank** (de 0 a $P-1$, onde $P$ é o número total de processos), que o código usa para saber qual parte do trabalho lhe cabe.
- Risco importante: **deadlock** — quando dois ou mais processos ficam esperando indefinidamente uns pelos outros (ex.: cada um esperando receber uma mensagem que o outro nunca chega a enviar, por erro de lógica no código).

### Operações coletivas de comunicação

| Operação | O que faz |
|---|---|
| **Broadcast** | Um processo distribui o mesmo dado para todos os demais |
| **Reduce** | Combina valores vindos de todos os processos em um único resultado (ex.: soma total) em um processo |
| **Scatter** | Distribui partes diferentes de um conjunto de dados entre os processos |
| **Gather** | Coleta partes de dados espalhadas entre os processos e as reúne em um só lugar |
| **Barrier** | Sincroniza os processos, garantindo que todos alcancem certo ponto antes de continuar |

---

## 📌 Conceitos-chave

- **HPC:** uso de clusters de múltiplos nós (CPU/GPU) para resolver problemas computacionalmente intensivos via paralelismo.
- **Memória compartilhada vs. distribuída:** dois paradigmas de paralelismo — threads compartilhando memória (OpenMP) vs. processos isolados trocando mensagens (MPI).
- **Condição de corrida:** erro que ocorre quando múltiplas threads acessam/alteram a mesma variável sem sincronização adequada.
- **SPMD:** modelo onde todos os processos MPI rodam o mesmo código sobre dados diferentes, distinguidos pelo `rank`.
- **Deadlock:** travamento por espera circular entre processos.

---

## ❓ Perguntas e discussões da aula

> [!question] Perguntas (Aula 1)
> *(nenhuma pergunta registrada nesta aula)*

---
