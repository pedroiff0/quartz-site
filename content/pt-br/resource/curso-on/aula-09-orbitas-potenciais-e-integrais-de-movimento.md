---
publish: false
title: Aula 09 — Órbitas, Potenciais e Integrais de Movimento
created: 2026-07-25
modified: 2026-08-27
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - dinamica-estelar
  - dinamica-galactica
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula09
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: Da massa ao potencial gravitacional (equação de Poisson), órbitas em sistemas esféricos e axissimétricos, formalismo hamiltoniano e coordenadas ação-ângulo, colisões estelares, a equação de Boltzmann sem colisões, as equações de Jeans e o teorema do virial
professor: Hélio Dotto Perottoni
---

# 🌀 Aula 09 — Órbitas, Potenciais e Integrais de Movimento

> [!note] Resumo
> Esta aula abre a unidade de Dinâmica do curso: como ir da distribuição de massa de uma galáxia ao potencial gravitacional que a governa (equação de Poisson), como descrever órbitas estelares nesse potencial (sistemas esféricos e axissimétricos, coordenadas ação-ângulo), por que galáxias podem ser tratadas como sistemas não colisionais, e como a equação de Boltzmann sem colisões e suas equações de Jeans conectam a dinâmica teórica a quantidades observáveis — fechando com o teorema do virial.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** slides oficiais da disciplina — "Órbitas, parâmetros orbitais e integrais de movimento"

---

## 🎯 As metas da dinâmica estelar

De forma empírica, a dinâmica estelar/galáctica busca responder perguntas em camadas crescentes de profundidade:

- **Mais direto:** qual é a distribuição total de massa de um sistema, e em que órbitas se movem seus elementos de massa?
- **Mais fundo:** quais são os componentes dessa massa (estrelas, gás, matéria escura)? O conteúdo de massa observado é explicado pelos constituintes conhecidos? A maioria dos sistemas está em equilíbrio (aproximadamente estacionário) numa escala de tempo dinâmica?
- **Mais além:** a variedade de estruturas de galáxias observadas é determinada pela estabilidade dinâmica? O que se pode aprender sobre a formação de galáxias a partir do seu estado dinâmico atual? Há remodelamento interno lento ("secular")?

Na prática, essas perguntas são respondidas a partir de observáveis concretos: a **curva de rotação** (disco de estrelas e gás) dá a massa total; a **dispersão de velocidades** das estrelas revela a estrutura e massa do disco/bojo; o **halo estelar e os aglomerados globulares** traçam o potencial a grandes raios; e as **correntes estelares de maré** (_streams_) mapeiam diretamente o potencial gravitacional e o halo de matéria escura. Como o tempo dinâmico típico de uma galáxia é da ordem de $10^8$ anos, qualquer observação é essencialmente um "instantâneo" — a única exceção relevante é o Centro Galáctico, onde órbitas estelares individuais já foram acompanhadas ao longo de décadas.

## 🌌 Da massa ao potencial: a equação de Poisson

A gravitação pode ser descrita, de forma equivalente à força newtoniana entre pares de partículas, por um **potencial escalar** $\Phi(\mathbf{x})$. A relação fundamental entre a distribuição de massa e o potencial que ela gera é a **equação de Poisson**:

$\nabla^2 \Phi(\mathbf{x}) = 4\pi G \rho(\mathbf{x})$

onde $\rho(\mathbf{x})$ é a densidade de massa. A distribuição de massa gera o potencial; o movimento das partículas, por sua vez, é determinado pelo **gradiente** desse potencial ($\mathbf{a} = -\nabla\Phi$). O problema da dinâmica estelar tem, portanto, duas direções:

$\rho(\mathbf{x}) \;\xrightarrow{\text{Poisson}}\; \Phi(\mathbf{x}) \;\xrightarrow{\text{integrar órbitas}}\; \text{órbitas}$

Esse limite (equação de Poisson) é o **limite newtoniano** da Relatividade Geral — válido quando se negligenciam efeitos relativísticos e a expansão cosmológica. Em geral, $\Phi$ é negativo e tende a zero no infinito.

> [!tip] Por que sistemas esféricos primeiro?
> A maioria das galáxias está longe de ser esfericamente simétrica, mas boa parte das propriedades de distribuições não esféricas pode ser entendida aproximando-as por uma distribuição esférica equivalente — daí o valor pedagógico (e prático) de começar por esse caso mais simples.

### Os teoremas das cascas de Newton

Para sistemas esféricos, dois teoremas simplificam drasticamente o cálculo do potencial:

1. **Primeiro teorema:** um corpo dentro de uma casca esférica uniforme de matéria não sofre força gravitacional resultante dessa casca.
2. **Segundo teorema:** a força gravitacional sobre um corpo _fora_ de uma casca esférica uniforme é idêntica à que ocorreria se toda a massa da casca estivesse concentrada em um ponto no seu centro.

Somando as contribuições de cascas sucessivas ($dM \to d\rho$), obtém-se o potencial de qualquer distribuição esférica de massa.

## 🔄 Velocidade circular e tempo dinâmico

Numa órbita circular, a aceleração centrípeta é equilibrada pelo campo gravitacional, o que dá diretamente a **velocidade circular**:

$v_c(r) = \sqrt{\frac{GM(<r)}{r}}$

Essa é uma relação poderosa: medir $v_c(r)$ como função do raio equivale a medir diretamente a distribuição de massa contida dentro de $r$ — o princípio por trás de toda curva de rotação galáctica.

O **tempo dinâmico** — o período de uma órbita circular no raio $r$ — pode ser reescrito em termos da densidade média interior a $r$, $t_{din} \sim 1/\sqrt{G\bar\rho}$. Para a Via Láctea, esse tempo é da ordem de $10^8$ anos — a escala que justifica tratar observações de galáxias como "instantâneos" dinâmicos (ver seção anterior).

> [!info]- Exemplos de potenciais esféricos usados na prática
> Esfera homogênea, esfera de Plummer, e potenciais com lei de potência (simples ou dupla) são os modelos analíticos de referência mais usados para descrever perfis de massa esféricos idealizados.

## 🧮 Formalismo lagrangiano e hamiltoniano

Além da 2ª lei de Newton, formulações mais poderosas descrevem a mesma dinâmica:

- **Princípio de Hamilton / formalismo lagrangiano:** o movimento de um sistema é tal que a **ação** $S=\int L\,dt$ (com $L=T-V$, energia cinética menos potencial) é estacionária — as equações de Euler-Lagrange formalizam essa condição. Uma consequência direta (**teorema de Noether**): se uma coordenada $q_j$ não aparece explicitamente em $L$, o momento associado a ela é conservado.
- **Formalismo hamiltoniano:** trata coordenadas $q$ e momentos $p$ de forma simétrica, trocando um conjunto de equações diferenciais de 2ª ordem (Newton/Lagrange) por um conjunto de equações de 1ª ordem para $(q,p)$.
- **Equação de Hamilton-Jacobi:** reformula a dinâmica em termos da função ação $S(q,t)$. Resolvendo por separação de variáveis, chega-se às **coordenadas ação-ângulo** $(\theta_i, J_i)$: os $J_i$ (variáveis de ação) são integrais de movimento ($\dot J=0$), e os $\theta_i$ (variáveis angulares) crescem linearmente no tempo com frequência $\Omega_i = \partial H/\partial J_i$.

> [!warning] Coordenadas ação-ângulo: poderosas, mas caras de calcular
> São conceitualmente centrais em dinâmica galáctica — o Hamiltoniano depende só das ações, o que simplifica enormemente a descrição do movimento. Na prática, porém, transformar $(x,v) \to (\theta,J)$ — e principalmente o caminho inverso — geralmente exige integrar numericamente a órbita por um tempo longo, ou aproximar o potencial de formas que nem sempre são válidas para todos os tipos de órbita.

## 🪐 Órbitas em sistemas esféricos e axissimétricos

Num potencial que **não varia no tempo**, a energia $E$ é conservada. Num potencial **esférico**, o momento angular $\mathbf{L}$ também é conservado, e o movimento fica restrito ao plano orbital — de 6 dimensões do espaço de fase, restam apenas 2 (um plano), descritas em coordenadas polares $(r,\phi)$.

Para uma galáxia **axissimétrica** (disco), usam-se coordenadas cilíndricas $(R,\phi,z)$, com $z=0$ no plano de simetria. Estruturas não axissimétricas (barra, braços espirais) são negligenciadas nesse tratamento. Como o potencial não depende de $\phi$ ($\partial\Phi/\partial\phi=0$), a força na direção $\phi$ é nula, e as estrelas do disco **conservam o momento angular** em torno do eixo $z$ ($L_z$) — uma das integrais de movimento mais usadas em arqueologia galáctica para caracterizar órbitas estelares.

## 💥 Colisões importam em galáxias?

Diferente de um gás molecular (onde colisões frequentes redistribuem energia e momento), em galáxias a força gravitacional é de longo alcance e a **distribuição média de massa** é o que determina o movimento estelar — encontros próximos individuais quase não importam. Formalmente, distinguem-se dois regimes:

- **Encontros fortes (próximos):** a energia potencial trocada é comparável à energia cinética inicial — a trajetória muda drasticamente. O raio característico $r_s$ para isso, perto do Sol ($v\sim30\,$km/s, $m=0{,}5\,M_\odot$), é de apenas $\sim1\,$UA — muitíssimo menor que a distância típica entre estrelas ($\sim271\,000\,$UA até a estrela mais próxima). O tempo característico entre encontros fortes chega a $t_s\sim10^{15}$ anos, muito maior que a idade do Universo: **encontros fortes só importam nos núcleos densos de aglomerados globulares**.
- **Encontros distantes (fracos):** a estrela perturbadora mal desvia a trajetória ($\delta v/v \ll 1$, a "aproximação de impulso"). Cada encontro distante produz uma pequena variação de velocidade $\delta v$ perpendicular à trajetória; como as perturbações têm direções aleatórias, o efeito vetorial médio é nulo (sem mudança de direção líquida, mas o caminho fica "irregular").

Essa hierarquia de escalas de tempo é o que justifica tratar galáxias como sistemas **não colisionais** na prática.

## 📊 A equação de Boltzmann sem colisões

Seguir a órbita de cada uma das bilhões de estrelas de uma galáxia não é prático nem necessário. Em vez disso, define-se uma **função distribuição** $f(\mathbf{x},\mathbf{v},t)$, tal que $f\,d^3x\,d^3v$ é a probabilidade de uma estrela escolhida aleatoriamente ocupar aquele elemento de espaço de fase no instante $t$ — normalizada de forma que a integral sobre todo o espaço de fase dê o número total de estrelas.

Como o sistema é não colisional (seção anterior), $f$ obedece à **equação de Boltzmann sem colisões**:

$\frac{Df}{Dt} = \frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla_{\mathbf x} f - \nabla\Phi\cdot\nabla_{\mathbf v} f = 0$

Em equilíbrio ($\partial f/\partial t=0$), essa equação descreve qualquer sistema estacionário sob gravidade — não apenas casos especiais.

## 📐 As equações de Jeans e o teorema de Jeans

A função distribuição $f$ não é diretamente observável. Multiplicando a equação de Boltzmann por momentos da velocidade ($v_i$, $v_iv_j$, ...) e integrando sobre a velocidade, obtêm-se as **equações de Jeans** — que conectam a dinâmica a grandezas diretamente observáveis: densidade $\nu(r)$, velocidade média e **dispersão de velocidades** $\sigma(r)$.

Isso permite inverter o problema de sempre: em vez de conhecer a massa e prever o movimento, observa-se o movimento (densidade + dispersão de velocidades de uma população traçadora) e **infere-se a massa**:

$\nu(r),\ \sigma_r(r),\ \beta(r) \;\longrightarrow\; \Phi(r) \;\longrightarrow\; M(r)$

onde $\beta(r)$ é o parâmetro de **anisotropia** orbital: $\beta=0$ (isotropia, sem direção preferida), $0<\beta\le1$ (anisotropia radial, órbitas quase radiais), $\beta<0$ (anisotropia tangencial, órbitas mais circulares).

> [!info] Teorema de Jeans
> Qualquer função das integrais de movimento é solução da equação de Boltzmann sem colisões em equilíbrio; e, reciprocamente, qualquer solução estacionária dessa equação depende das coordenadas de espaço de fase **apenas** através das integrais de movimento. É o que garante formalmente que descrever uma população estelar em termos de $(E, L, ...)$, em vez de $(\mathbf{x},\mathbf{v})$ diretamente, é matematicamente legítimo.

## ⚖️ O teorema do virial

Para um sistema em equilíbrio vale a relação escalar:

$2K + W = 0$

onde $K$ é a energia cinética total do sistema ($K=\tfrac{1}{2}M\langle v^2\rangle$, com $\langle v^2\rangle$ a velocidade quadrática média das estrelas) e $W$ é a energia potencial gravitacional total. Rearranjando, obtém-se a massa necessária para sustentar os movimentos observados, $M \sim \langle v^2\rangle\, r_g / G$, com $r_g$ o raio gravitacional do sistema — a mesma lógica já usada em Aglomerados de Galáxias (Zwicky, Coma) para inferir a existência de matéria escura a partir do teorema do virial.

---

## 📌 Conceitos-chave

- **Equação de Poisson** ($\nabla^2\Phi=4\pi G\rho$): a ponte entre distribuição de massa e potencial gravitacional; toda a dinâmica estelar flui de $\rho \to \Phi \to$ órbitas.
- **Velocidade circular** $v_c(r)=\sqrt{GM(<r)/r}$: medir $v_c(r)$ equivale a medir $M(<r)$ diretamente — base de toda curva de rotação.
- **Coordenadas ação-ângulo:** as ações $J_i$ são integrais de movimento; o Hamiltoniano depende só delas, simplificando a descrição do movimento — mas custosas de calcular na prática.
- **Sistemas não colisionais:** em galáxias, o tempo entre encontros fortes ($\sim10^{15}$ anos) excede a idade do Universo — a distribuição média de massa, não colisões individuais, governa o movimento estelar.
- **Equação de Boltzmann sem colisões** ($Df/Dt=0$): descreve a evolução da função distribuição $f(\mathbf{x},\mathbf{v},t)$ de qualquer sistema estelar não colisional.
- **Equações de Jeans:** momentos da equação de Boltzmann que conectam $f$ a observáveis (densidade, dispersão de velocidades) — permitem inferir massa a partir de cinemática.
- **Teorema do virial** ($2K+W=0$): relação mais direta entre dispersão de velocidades observada e massa total de um sistema em equilíbrio.

## 🔗 Referências e correlatos

- Binney & Tremaine — _Galactic Dynamics_ (livro-texto de referência da disciplina para esta unidade)
- Bovy, J. — _Dynamics and Astrophysics of Galaxies_
- Notas de aula de Amina Helmi; apresentações de Eugene Vasiliev
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-08-velocidades-e-movimento-proprio|Aula 08 — Velocidades e Movimento Próprio]] — pré-requisito direto: $(U,V,W)$ e o LSR introduzidos ali reaparecem aqui como condições iniciais de órbitas
- [[pt-br/resource/escolainverno/aglomerados/aglomerados-aula01|Escola de Inverno — Aglomerados, Aula 01]] — o mesmo teorema do virial ($2K+W=0$), aplicado à escala de aglomerados de galáxias em vez de estrelas individuais
- [[pt-br/resource/curso-on/aula-10-integracao-de-orbitas-com-galpy|Aula 10 — Integração de Órbitas com galpy]] — todo este formalismo posto em prática com código real
