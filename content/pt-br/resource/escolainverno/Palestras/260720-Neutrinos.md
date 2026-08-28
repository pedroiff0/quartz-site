---
publish: true
encrypted: true
titulo: 260720-Neutrinos
disciplina: Palestra — Física de Partículas e Cosmologia
conteudo: Neutrinos e a Cosmologia — da física de partículas ao Universo em grande escala
professor: Gabriel Rodrigues
created: 2026-07-20 13:34
modified: 2026-08-27 21:54
tags:
  - escola-de-inverno-on
  - palestra
  - neutrinos
  - cosmologia
  - fisica-de-particulas
cssclasses:
  - page-grid
  - center-images
---
# Notas de Palestra — Neutrinos e a Cosmologia

> [!info] Informações da palestra
> **Título:** Neutrinos e a Cosmologia
> **Palestrante:** Prof. Gabriel Rodrigues

---

## 🎯 Visão geral

O **neutrino** é uma das partículas mais abundantes do Universo e, ao mesmo tempo, uma das mais difíceis de detectar — interage tão fracamente com a matéria que bilhões passam pelo seu corpo a cada segundo sem qualquer efeito perceptível. Esta palestra conecta duas escalas radicalmente diferentes: (1) a física de partículas do neutrino — sua descoberta, seus "sabores" e sua massa — e (2) seu papel na **cosmologia**, como parte do inventário de matéria/energia do Universo e como sonda da física fundamental. A ferramenta central que une as duas escalas é a **métrica de Friedmann** e as equações que descrevem a expansão do Universo.

### 📑 Tópicos abordados
1. O que são neutrinos: história e descoberta
2. O Modelo Padrão da física de partículas
3. Neutrinos têm massa: hierarquia de massas
4. Cosmologia: a métrica de Friedmann e a expansão do Universo
5. Neutrinos cósmicos e seu papel no $\Lambda$CDM

---

## 1. O que são neutrinos? Uma "partícula fantasma"

Em **1930**, **Wolfgang Pauli** propôs a existência do neutrino para resolver um problema no **decaimento beta** (um nêutron decaindo em um próton e um elétron): a energia do elétron emitido variava continuamente, o que parecia violar a conservação de energia — a menos que uma partícula adicional, neutra e quase indetectável, carregasse a energia "extra" para fora. Pauli chamou-a de "partícula fantasma", pois parecia impossível de observar diretamente.

**Enrico Fermi** desenvolveu, em seguida, a primeira teoria quantitativa do decaimento beta incorporando essa partícula (batizada de "neutrino", "pequeno nêutron" em italiano).

- **1956:** Primeira detecção experimental direta de neutrinos, usando um **reator nuclear** como fonte intensa (reatores produzem um fluxo grande e conhecido de neutrinos) — encerrando essa "caça ao fantasma" décadas depois da previsão teórica.

![Interior do detector Super-Kamiokande (Japão): um tanque com 50 mil toneladas de água ultrapura, revestido por milhares de fotomultiplicadoras, usado para detectar a raríssima interação de neutrinos com a matéria.](https://commons.wikimedia.org/wiki/Special:FilePath/Super_Kamiokande,_1_to_135th.jpg)

### Os três sabores de neutrinos

Hoje sabemos que existem **três "sabores" de neutrinos**, cada um associado a um lépton carregado correspondente:

![O Modelo Padrão da física de partículas: os neutrinos ($\nu_e, \nu_\mu, \nu_\tau$) aparecem na segunda linha, entre os léptons.](https://commons.wikimedia.org/wiki/Special:FilePath/Standard_Model_of_Elementary_Particles.svg)

- **Quarks:** up, down, charm, strange, top, bottom (partículas que se combinam para formar prótons, nêutrons, etc. — o **glúon** é o bóson mediador da força forte que os une, não um quark).
- **Léptons:** elétron, múon, tau — e seus respectivos neutrinos ($\nu_e$, $\nu_\mu$, $\nu_\tau$).
- **Bósons mediadores:** o fóton (força eletromagnética) e os bósons **Z e W** (força fraca — é essa a força responsável pelo decaimento beta e pelas interações do neutrino).

---

## 2. Neutrinos são massivos!

Por muito tempo, o Modelo Padrão assumia neutrinos **sem massa**. Isso mudou definitivamente em **1998**, com a descoberta da **oscilação de neutrinos** (um neutrino de um sabor se transformando espontaneamente em outro sabor ao longo de sua propagação) — fenômeno que só é possível na mecânica quântica se os neutrinos tiverem **massas diferentes de zero** (e diferentes entre si).

Isso levanta uma pergunta em aberto: qual é a ordem das massas dos três sabores? Existem dois cenários possíveis, chamados de **hierarquia de massas**:

- **Hierarquia normal (NH):** dois neutrinos leves e um mais pesado.
- **Hierarquia invertida (IH):** dois neutrinos pesados e um mais leve.

Uma quantidade-chave, especialmente relevante para a cosmologia, é a **soma das massas dos três sabores** $\sum m_\nu$. Experimentos de oscilação estabelecem limites inferiores para essa soma, dependendo da hierarquia:

- Hierarquia normal: $\sum m_\nu \gtrsim 0{,}06$ eV
- Hierarquia invertida: $\sum m_\nu \gtrsim 0{,}1$ eV

É exatamente esse ponto que conecta a física de partículas à cosmologia: **medidas cosmológicas independentes também restringem $\sum m_\nu$** (ver seção 5), e comparar os dois tipos de limite (oscilação vs. cosmologia) é uma forma poderosa de testar a física fundamental.

---

## 3. Do micro ao macro: entrando na cosmologia

Para conectar neutrinos ao Universo como um todo, mudamos de escala — de partículas subatômicas para as maiores distâncias observáveis:

**Escalas de distância:** UA (unidade astronômica) < ly (ano-luz) < pc < kpc < Mpc < **Gpc** (a escala que a cosmologia tipicamente utiliza).

A cosmologia estuda a origem, evolução e composição do Universo assumindo que ele é **homogêneo e isotrópico** em grandes escalas (>100 Mpc) — "isotropia" significa que **qualquer direção do céu é estatisticamente equivalente**.

### A métrica de Friedmann

Uma **métrica** descreve a geometria do espaço-tempo — como medir distâncias em um sistema de coordenadas de 4 dimensões (3 espaciais + tempo). Assumindo homogeneidade e isotropia, a solução geral das equações de Einstein para a Relatividade Geral é a **métrica de Friedmann-Lemaître-Robertson-Walker (FLRW)**:

$$ds^2 = -c^2dt^2 + a(t)^2\left[\frac{dr^2}{1-kr^2} + r^2 d\Omega^2\right]$$

onde:
- $ds$: intervalo de espaço-tempo entre dois eventos.
- $a(t)$: **fator de escala** — descreve como as distâncias no Universo crescem (ou diminuem) com o tempo; por convenção, $a(t_{hoje}) = 1$.
- $k = 0, \pm1$: **curvatura espacial** (plano, esférico ou hiperbólico).

> [!tip] A intuição de Wheeler
> O físico **John Archibald Wheeler** resumiu a Relatividade Geral numa frase: *"o espaço-tempo diz à matéria como se mover; a matéria diz ao espaço-tempo como se curvar."* As **equações de campo de Einstein** formalizam exatamente essa via de mão dupla entre geometria e conteúdo de matéria/energia.

### As equações de Friedmann

A partir da métrica FLRW e das equações de campo de Einstein, obtemos duas equações que governam a expansão cósmica:

- **Equação de Friedmann** (taxa de expansão): relaciona $\left(\dot{a}/a\right)^2$ (o quadrado da "velocidade" relativa de expansão, o parâmetro de Hubble) com a densidade total de energia do Universo.
- **Equação da aceleração:** descreve $\ddot{a}$ (a aceleração da expansão), que depende da densidade de energia **e** da pressão do conteúdo do Universo.

Combinando essas equações com a **equação de estado** $p = w\rho c^2$ (que relaciona pressão $p$ e densidade de energia $\rho$ para cada componente do Universo, via o parâmetro $w$) e a **equação do fluido** (conservação de energia em um Universo em expansão), conseguimos modelar como cada componente (matéria, radiação, energia escura) evolui ao longo do tempo cósmico.

A **energia escura** é o componente com $w \approx -1$ que faz a taxa de expansão de Friedmann **aumentar** com o tempo — a origem da aceleração cósmica observada (ver nota de Cosmologia). Esse é o ingrediente central do **modelo $\Lambda$CDM**.

---

## 4. Neutrinos cósmicos

Olhando a história do Universo do ponto de vista **térmico**:

- No **Universo primordial**, a temperatura era muito maior que a massa de repouso dos neutrinos ($k_BT \gg m_\nu c^2$) — nessas condições, os neutrinos se movem à **velocidade da luz** e se comportam como **radiação** (relativísticos).
- Conforme o Universo se **expande e esfria**, em algum momento a temperatura cai abaixo da escala de massa dos neutrinos, e eles passam a se comportar como **matéria** (não-relativísticos) — uma transição semelhante à que ocorre com os fótons na recombinação, mas em uma época muito mais antiga.

### O Fundo Cósmico de Neutrinos (C$\nu$B)

Assim como existe uma Radiação Cósmica de Fundo em fótons (a **2,725 K** hoje), existe também um **fundo cósmico de neutrinos**, remanescente de quando o Universo tinha apenas ~1 segundo de idade:

- Temperatura hoje: **~1,945 K** (mais fria que os fótons, pois os neutrinos "se desacoplaram" antes de um processo de aniquilação elétron-pósitron que reaqueceu os fótons).
- Densidade numérica: **~336 neutrinos/cm³** em todo o Universo — enorme, mas praticamente indetectável, pois interagem muito fracamente.

### Restrições cosmológicas sobre a massa dos neutrinos
A soma das massas dos neutrinos deixa impressões sutis em duas observáveis cosmológicas principais:
- **Espectro angular de potência da RCF** (medido pelo satélite **Planck**).
- **Espectro de potência de matéria** (a distribuição estatística da matéria em grande escala, medida por levantamentos como o **DESI**).

Atualmente, os **limites superiores cosmológicos** sobre $\sum m_\nu$ estão numa faixa que já começa a **tensionar os limites inferiores** exigidos pelas oscilações de neutrino (hierarquia normal vs. invertida) — uma área ativa de pesquisa, pois cosmologia e física de partículas podem, em breve, se contradizer ou se confirmar mutuamente.

> [!tip] "Energia escura fantasma"
> Alguns modelos alternativos de energia escura (chamados de **"energia escura fantasma"**, *phantom dark energy*, com $w < -1$) alterariam a taxa de expansão de forma diferente do $\Lambda$CDM padrão — e podem, inclusive, afetar como interpretamos os limites cosmológicos sobre a massa dos neutrinos.

---

## 📌 Conceitos-chave

- **Neutrino:** partícula leptônica neutra, de interação fraca extremamente sutil, existente em três sabores ($\nu_e, \nu_\mu, \nu_\tau$).
- **Oscilação de neutrinos:** transformação entre sabores durante a propagação — prova de que neutrinos têm massa (descoberta em 1998).
- **Hierarquia normal/invertida:** os dois possíveis ordenamentos das massas dos três neutrinos.
- **Métrica FLRW:** descreve a geometria de um Universo homogêneo, isotrópico e em expansão.
- **Fundo Cósmico de Neutrinos:** análogo "invisível" da RCF, a 1,945 K, remanescente de ~1 segundo após o Big Bang.

---

## ❓ Perguntas e discussões da palestra

> [!question] Perguntas
> *(nenhuma pergunta registrada nesta palestra)*

---
