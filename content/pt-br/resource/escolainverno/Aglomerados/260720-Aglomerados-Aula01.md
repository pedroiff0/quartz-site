---
publish: true
encrypted: true
titulo: 260720-Aglomerados-Aula01
disciplina: Astrofísica Extragaláctica
conteudo: Aglomerados de Galáxias — as maiores estruturas gravitacionalmente ligadas do Universo
professor: Rogério Monteiro-Oliveira
criado: segunda-feira 20/07/2026 09:19
modificado: 22/07/2026
tags:
  - escola-de-inverno-on
  - astrofisica-extragalactica
  - aglomerados-de-galaxias
  - materia-escura
  - cosmologia
cssclasses:
  - page-grid
  - center-images
---
# Notas de Aula — Aglomerados de Galáxias

> [!info] Informações da aula
> **Título:** Aglomerados de Galáxias: as maiores estruturas do Universo
> **Professor:** Prof. Dr. Rogério Monteiro-Oliveira
> **Material:** [Aula 01](https://www.monteiro-oliveira.com/talks)

---

## 🎯 Visão geral

Um **aglomerado de galáxias** é a maior estrutura do cosmos que já colapsou gravitacionalmente e atingiu equilíbrio (virialização). Acima dessa escala, o Universo ainda está se expandindo e não formou objetos ligados — por isso aglomerados são laboratórios naturais para estudar gravidade, matéria escura e a formação de estruturas em grande escala. A aula introduz a hierarquia de escalas do Universo, a composição física de um aglomerado (galáxias + gás quente + matéria escura) e as diferentes janelas observacionais (óptico, raio-X, micro-ondas) usadas para detectá-los.

### 📑 Tópicos abordados
1. Escalas do cosmos
2. A "receita" de um aglomerado (do que ele é feito)
3. Como detectar aglomerados

---

## 1. Escalas do cosmos

Para descrever distâncias astronômicas usamos unidades muito maiores que o metro:

- **1 ano-luz (ly):** distância percorrida pela luz em um ano ($\approx 9{,}46\times10^{15}$ m).
- **1 parsec (pc):** unidade padrão em astronomia, definida geometricamente por paralaxe. $1\ \text{pc} = 3{,}26\ \text{ly}$.
- **1 Mpc (megaparsec)** $= 1000\ \text{kpc} = 3{,}26\times10^{6}\ \text{ly}$ — escala típica de distância *entre* aglomerados.
- Acima de **~500 Mpc**, o Universo é considerado **homogêneo e isotrópico** (o chamado *princípio cosmológico*): em escalas menores existe estrutura (galáxias, aglomerados, filamentos), mas em escalas muito grandes a distribuição de matéria é estatisticamente uniforme em qualquer direção.

> [!tip] Simulação de referência
> A **Millennium Run** é uma simulação cosmológica de N-corpos de grande escala, usada como referência visual para entender como a matéria escura se organiza no Universo ao longo do tempo cósmico.

### A Teia Cósmica

A distribuição de matéria em grande escala forma a chamada **teia cósmica**, análoga a uma esponja:

- **Vazios (voids):** regiões de baixíssima densidade, ocupando a maior parte do volume.
- **Filamentos:** estruturas alongadas que conectam regiões densas — por onde a matéria "escoa" gravitacionalmente.
- **Nós:** interseções dos filamentos, onde a densidade é máxima — é justamente aqui que se formam os **aglomerados de galáxias**.

A existência dessa teia — incluindo sua componente invisível de matéria escura — pode ser mapeada indiretamente através de **lentes gravitacionais**: a luz de galáxias de fundo é deformada ao passar por concentrações de massa em primeiro plano, permitindo "pesar" a matéria mesmo quando ela não emite luz.

![Aglomerado de galáxias Abell 1689: os arcos azuis são imagens distorcidas de galáxias de fundo, "lenteadas" pela massa do aglomerado em primeiro plano (Hubble/NASA/ESA).](https://commons.wikimedia.org/wiki/Special:FilePath/Abell_1689.jpg)

---

## 2. O que é um aglomerado (a "receita")

Aglomerados são **sistemas que já colapsaram e estão virializados**, ou seja, atingiram um equilíbrio dinâmico entre gravidade e movimento interno.

- O Universo está em **expansão acelerada**, o que tende a *diluir* a densidade de matéria com o tempo.
- Para uma estrutura se formar, ela precisa **colapsar**: sua autogravidade local deve vencer localmente a expansão cósmica.
- **Virializar** significa que o sistema parou de colapsar e atingiu um estado estacionário estatístico, onde energia cinética e potencial gravitacional obedecem ao **teorema do virial** (ver seção 4).

Aglomerados são os maiores objetos virializados conhecidos, com **massas totais entre $10^{14}$ e $10^{15}\,M_{\odot}$** contidas dentro de um **raio virial** $R_{200}$ — o raio dentro do qual a densidade média é 200 vezes a densidade crítica do Universo $\rho_c$ (por isso o índice "200"):

$$M_{200} = \frac{4\pi}{3} R_{200}^3 \,(200\,\rho_c)$$

O fator $200\,\rho_c$ vem de previsões de colapso esférico: é aproximadamente a densidade que uma região esfericamente simétrica atinge quando termina de virializar.

### Balanço de massa de um aglomerado

Um aglomerado *não* é feito principalmente de galáxias — sua massa se distribui, tipicamente, assim:

| Componente | Fração da massa |
|---|---|
| Gás quente (meio intra-aglomerado, ICM) | ~15% |
| Galáxias (estrelas) | ~5% |
| Matéria escura | ~80% |

Ou seja, a parte *luminosa* (estrelas + gás) é uma minoria — o aglomerado é dominado por massa que não emite luz.

### Dispersão de velocidades ($\sigma_v$)

As galáxias dentro de um aglomerado não estão paradas: orbitam o centro de massa com velocidades que variam estatisticamente. Essa variação é medida pela **dispersão de velocidades** $\sigma_v$.

> [!tip] Analogia do "exame de abelhas"
> Pense em um enxame de abelhas voando ao redor de uma colmeia: se elas voam devagar e próximas umas das outras, a dispersão de velocidades é **baixa** (sistema "frio", pouco massivo). Se voam muito rápido e espalhadas, a dispersão é **alta** — o que, pelo teorema do virial, indica um poço de potencial gravitacional mais profundo, logo, **mais massa**.

Na prática, medimos a velocidade de cada galáxia em relação à velocidade média do aglomerado ($V_m$) através do **efeito Doppler**: galáxias se afastando de nós têm luz deslocada para o vermelho (*redshift*) e galáxias se aproximando, para o azul (*blueshift*). O deslocamento relativo do comprimento de onda é o redshift:

$$z = \frac{\lambda_{\text{observado}} - \lambda_{\text{emitido}}}{\lambda_{\text{emitido}}}$$

que, para velocidades não relativísticas, se relaciona à velocidade radial por $v \approx c\,z$.

### Teorema do virial

Para um sistema gravitacional em equilíbrio estatístico, o teorema do virial relaciona a energia cinética total $K$ e a energia potencial gravitacional total $U$:

$$2K + U = 0$$

com

$$K = \frac{1}{2} M \sigma_v^2 \qquad U \approx -\frac{GM^2}{r}$$

Substituindo e isolando $M$, obtemos uma estimativa da **massa dinâmica** do aglomerado a partir de quantidades observáveis (dispersão de velocidades e raio):

$$M_{\text{din}} \sim \frac{\sigma_v^2\, r}{G}$$

Essa é uma das formas mais diretas — e historicamente a primeira — de "pesar" um aglomerado sem depender da luz que ele emite.

### Estimando a massa luminosa

Alternativamente, podemos estimar a massa a partir da luz que as galáxias emitem:

- $L_{tot}$: luminosidade total gerada por todas as estrelas do aglomerado.
- **Razão massa-luminosidade** $M/L$: quanto de massa "corresponde" a cada unidade de luminosidade emitida (varia com o tipo estelar, idade da população, etc.).

$$M_{\text{lum}} = \frac{M}{L}\, L_{tot}$$

Ingenuamente, esperaríamos $M_{\text{din}} \approx M_{\text{lum}}$ — que a massa medida dinamicamente batesse com a massa que "vemos" em estrelas. **Não é o que acontece**, e essa discrepância é a origem histórica da matéria escura.

### A descoberta da matéria escura

Em **1933**, **Fritz Zwicky** analisou o **Aglomerado de Coma** e mediu uma dispersão de velocidades de **~1000 km/s** entre as galáxias membro. Usando o teorema do virial, isso implicava uma massa dinâmica **~400 vezes maior** que a massa luminosa estimada pelas estrelas visíveis:

$$M_{\text{din}} = 400 \times M_{\text{lum}}$$

Esse enorme excesso de massa invisível é uma das primeiras evidências históricas da **matéria escura** — hoje também confirmada de forma independente por lentes gravitacionais (ver seção 4).

![Bullet Cluster (1E 0657-56): em rosa, o gás quente do ICM visto em raio-X (Chandra); em azul, a distribuição de massa reconstruída por lentes gravitacionais — mostrando que a maior parte da massa (matéria escura) está separada do gás visível (NASA/CXC).](https://commons.wikimedia.org/wiki/Special:FilePath/Bullet_cluster.jpg)

### O meio intra-aglomerado (ICM)

Entre as galáxias existe um gás muito rarefeito (densidade $\sim 10^{-3}$ partículas/cm³) mas extremamente quente (**1–10 keV**, ou seja, dezenas de milhões de graus). Gás tão quente emite fortemente em **raio-X** — essa é uma das principais formas de detectar aglomerados (ver seção 4).

#### Equilíbrio hidrostático do gás

Esse gás não colapsa para o centro porque sua **pressão térmica** sustenta o peso do próprio gás contra a gravidade do aglomerado — o mesmo princípio físico que mantém o interior de uma estrela estável (equilíbrio hidrostático):

$$\frac{dP}{dr} = -\rho_{\text{gás}}(r)\,\frac{G\,M(<r)}{r^2}$$

Do lado esquerdo, o gradiente de pressão; do lado direito, a força gravitacional por unidade de volume exercida por toda a massa contida dentro do raio $r$, $M(<r)$. Assumindo a **lei dos gases ideais** ($P = \frac{\rho}{\mu m_p}k_BT$) para relacionar pressão, densidade e temperatura, essa equação permite **estimar a massa total do aglomerado a partir de perfis observados de densidade e temperatura do gás** — um terceiro método de pesagem, independente do virial.

---

## 3. Galáxias dentro do aglomerado

O ambiente de um aglomerado (alta densidade de galáxias, gás quente, interações gravitacionais frequentes) influencia fortemente a **forma e o destino evolutivo** das galáxias membro — algo visível principalmente no óptico.

### Relação morfologia–densidade

Quanto mais denso o ambiente, maior a proporção de galáxias do tipo:

- **Early type** (elípticas/lenticulares): antigas, avermelhadas, compostas por estrelas velhas e frias, gigantes.
- **Late type** (espirais/irregulares): mais jovens, azuladas, com formação estelar em curso.

Essa correlação (mais elípticas em regiões densas, mais espirais em regiões isoladas) é uma das evidências de que o ambiente afeta a evolução galáctica (ex.: remoção de gás por interação com o ICM, fusões, "assédio" gravitacional).

---

## 4. Como detectar um aglomerado

Existem múltiplas "janelas" observacionais, cada uma sensível a um componente diferente do aglomerado:

### Domínio óptico
Detecta as galáxias membro diretamente. Problema principal: a **projeção** — observamos o céu em 2D, mas o aglomerado é um objeto 3D, e galáxias de campo (não pertencentes ao aglomerado) podem se sobrepor na linha de visada, contaminando a amostra.

- **Sequência vermelha:** no diagrama cor × magnitude, as galáxias elípticas de um aglomerado formam uma reta estreita e bem definida (por isso "sequência"). Isso ocorre porque essas galáxias, com muitas gerações estelares e metalicidade alta, têm cores muito similares e previsíveis — servindo como identificador eficiente de membros do aglomerado.
- **Espectroscopia:** mede o redshift individual de cada galáxia, resolvendo o problema da projeção (galáxias com redshift muito diferente do aglomerado não são membros).

### Domínio do gás (raio-X)
Como a massa bariônica do aglomerado está majoritariamente no gás quente do ICM, observações em **raio-X** (ex.: satélites **Chandra**, **XRISM**, **XMM-Newton**) detectam essa emissão diretamente. Vantagem importante: **não há problema de projeção**, pois o gás está fisicamente distribuído de forma suave por todo o aglomerado (ao contrário de galáxias individuais espalhadas ao acaso na linha de visada).

### Domínio de micro-ondas — Efeito Sunyaev-Zel'dovich (SZ)
Fótons "frios" da **Radiação Cósmica de Fundo (CMB)**, ao atravessarem o gás extremamente quente do ICM, colidem com elétrons de alta energia e **ganham energia** no processo — um **efeito Compton inverso**. Isso distorce ligeiramente o espectro da CMB na direção do aglomerado, criando uma assinatura característica conhecida como **efeito Sunyaev-Zel'dovich (SZ)**, hoje usada para detectar aglomerados distantes independentemente do brilho óptico ou de raio-X.

### Lentes gravitacionais fracas (weak lensing)
Mapeia a massa **total** (incluindo matéria escura) de forma independente do gás ou das estrelas, através da distorção estatística sutil na forma de galáxias de fundo causada pela curvatura do espaço-tempo. Levantamentos como **DES**, **Euclid** e **LSST** usam extensivamente essa técnica para mapear a distribuição de massa em grande escala.

---

## 📌 Conceitos-chave

- **Virialização:** estado de equilíbrio dinâmico atingido após o colapso gravitacional de uma estrutura.
- **$R_{200}$ / $M_{200}$:** raio e massa definidos pela região onde a densidade média é 200× a densidade crítica do Universo.
- **ICM (meio intra-aglomerado):** gás quente e rarefeito que preenche o espaço entre as galáxias de um aglomerado.
- **Efeito SZ:** distorção da CMB causada pela interação com elétrons quentes do ICM (Compton inverso).
- **Weak lensing:** técnica de mapeamento de massa via distorção estatística de galáxias de fundo.

---

## ❓ Perguntas e discussões da aula

> [!question] Perguntas (Aula 1)
> 1. **Qual a melhor técnica, fotometria ou espectroscopia?** R.: Um meio-termo — fotometria de banda estreita de alta resolução espectral, como o levantamento **J-PAS**, combina velocidade (fotometria) com boa resolução em redshift (próxima da espectroscópica).
> 2. **A massa medida é "sólida" (confiável)?** R.: Depende da região analisada — diferentes métodos (virial, raio-X, lensing) sondam regiões e componentes distintos do aglomerado, então é preciso cuidado ao comparar.
> 3. **Como entender os "fótons gelados" em termos de temperatura vs. energia?** *(em aberto)*
> 4. **O que sabemos hoje sobre a natureza da matéria escura?** *(em aberto — ver candidatos como WIMPs e áxions na nota de Cosmologia)*

---

## 🔗 Referências
- [Página do Prof. Rogério Monteiro-Oliveira — Aula 01](https://www.monteiro-oliveira.com/talks)
- Simulação **Millennium Run**
