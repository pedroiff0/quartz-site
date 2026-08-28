---
publish: false
title: Aula 07 — Distâncias, Escala de Distância e Sistemas de Coordenadas
created: 2026-07-23 12:36
modified: 2026-08-27 12:36
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - distancias
  - coordenadas-galacticas
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula07
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: A escada cósmica de distâncias — de radar a supernovas Ia — e os sistemas de coordenadas horizontal, equatorial e galáctico
professor: Hélio Dotto Perottoni
---

# 📐 Aula 07 — Distâncias, Escala de Distância e Sistemas de Coordenadas

> [!note] Resumo
> As distâncias estabelecem a escala absoluta de toda a Astronomia. Esta aula percorre a "escada cósmica de distâncias" — do radar no Sistema Solar às supernovas tipo Ia em galáxias distantes — e fecha com os três sistemas de coordenadas usados para localizar objetos no céu e na Galáxia.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni

---

## 🪜 A escada cósmica de distâncias

Cada método de medição de distância só é válido dentro de uma faixa de escalas, e o método seguinte precisa ser **calibrado** pelo anterior — daí "escada":

| Escala | Método | Alcance típico |
|---|---|---|
| Sistema Solar | Radar | $10^{-4}$ anos-luz |
| Estrelas próximas | Paralaxe trigonométrica | $10^3$ anos-luz |
| Via Láctea | Ajuste da sequência principal (aglomerados) | $10^5$ anos-luz |
| Galáxias próximas | Variáveis Cefeidas (+ outras) | $10^7$ anos-luz |
| Galáxias distantes | Supernovas Tipo Ia (velas padrão) | $10^{10}$ anos-luz |

## 🛰️ Distâncias no Sistema Solar

A **3ª Lei de Kepler** dá as distâncias **relativas** entre os planetas e o Sol — mas é necessária uma medida **absoluta** de pelo menos um corpo para calibrar toda a escala.

- **Giovanni Cassini (séc. XVII):** primeira estimativa precisa da Unidade Astronômica (U.A. $= 1{,}496\times10^{11}\,$m), via triangulação da distância até Marte, observada simultaneamente da França e da Guiana Francesa. Erro de apenas 7% em relação ao valor atual.
- **Trânsito de Vênus (meados do séc. XVIII):** campanha internacional liderada por **Edmond Halley** (o mesmo do cometa) melhora a precisão para 2%.
- **Radar (RAdio Detection And Ranging, início dos anos 1960):** mede-se o tempo entre emissão e detecção de uma onda refletida por uma superfície sólida; $d = c\,\Delta t / 2$. Os valores obtidos já nos anos 60 concordam com os atuais até a quinta casa decimal. Um dos principais instrumentos históricos foi o **radiotelescópio de Arecibo** (500 m), hoje descomissionado.

## ⭐ Paralaxe trigonométrica

A **paralaxe** é a mudança de posição aparente de um objeto devido ao movimento do observador — o mesmo princípio da percepção de profundidade humana (nossos dois olhos como linha de base). Por triangulação: $d = x/\tan\alpha$, onde $x$ é a linha de base e $\alpha$ o ângulo medido.

Nossos olhos só percebem profundidade a curta distância porque a linha de base (distância interpupilar) é minúscula — para objetos distantes, $\alpha$ se torna imperceptível. Em Astronomia, dispomos de linhas de base muito maiores: o **diâmetro da Terra**, ou, melhor ainda, o **diâmetro da órbita terrestre** (2 U.A.), observando o mesmo objeto com 6 meses de diferença.

Para pequenos ângulos, $\tan p \approx p$, e definindo $p$ em segundos de arco, chega-se à unidade de **parsec** ("_parallax second_"): a distância de um objeto cuja paralaxe é exatamente 1 segundo de arco:

$d\,[\text{pc}] = \frac{1}{p\,['']}$

**Friedrich Bessel (1838)** foi o primeiro a medir uma paralaxe estelar com sucesso, para a estrela **61 Cygni** ($p=0{,}314'' \Rightarrow d=3{,}18\,$pc).

### A evolução das medidas de paralaxe

- **Pré-Hipparcos:** ~1000 estrelas com paralaxes precisas (incerteza relativa <10%).
- **Hipparcos (anos 90):** ~50 mil estrelas até ~1 kpc.
- **Gaia (missão em andamento):** ~500 milhões de estrelas até ~10 kpc do Sol — em unidades de miliarcossegundos de arco, correspondendo a distâncias de kiloparsecs.

> [!tip] Consultando dados do Gaia
> Para encontrar dados de uma estrela específica no catálogo Gaia: buscar por nome/coordenadas em **SIMBAD** (`simbad.u-strasbg.fr`) — obtendo posição, movimento próprio, velocidade radial, paralaxe e magnitudes em várias bandas — e então cruzar o identificador Gaia com o catálogo completo via **VizieR** (`vizier.u-strasbg.fr`).

### Exemplo prático — HD 249117

Paralaxe medida: $p = 0{,}3564 \pm 0{,}1343\,$mas (incerteza alta, pois a estrela é brilhante demais, $V<9$, para medidas ideais do Gaia). Magnitude aparente $m=7{,}76$; distância calculada $\approx2{,}81\,$kpc. Para posicionar a estrela corretamente no diagrama HR, ainda é preciso corrigir por extinção/avermelhamento (Aula 05) antes de converter para magnitude absoluta.

## 🌌 Distâncias na escala da Galáxia — ajuste de sequência principal

Aglomerados estelares são conjuntos de estrelas nascidas aproximadamente juntas — isso se reflete na distribuição de suas estrelas-membro no diagrama HR. Como o brilho aparente depende da distância, e **todas** as estrelas de um mesmo aglomerado estão à mesma distância, é possível ajustar simultaneamente um único modelo teórico (isócrona) a todas elas, com **quatro parâmetros livres**: idade, composição química, avermelhamento e módulo de distância \[ex.: Oliveira et al. 2020, para o aglomerado globular Messier 69]. Isso seria impossível de fazer para uma estrela isolada, mas em aglomerados temos milhares de estrelas simultaneamente restringindo o ajuste.

## 🌠 Distâncias a galáxias próximas — Variáveis Cefeidas

**Henrietta Leavitt** (início do séc. XX), estudando estrelas variáveis nas Nuvens de Magalhães, percebeu uma relação entre o **período de pulsação** e o **brilho** dessas estrelas — a **relação período-luminosidade** ("Lei de Leavitt") \[1912HarCi.173....1L]. As Cefeidas são estrelas pulsantes muito luminosas, brilhantes o bastante para serem observadas em galáxias próximas.

> [!warning] Calibração necessária
> Para aplicar essa relação como medida de distância, é preciso primeiro conhecer a distância de **algumas** Cefeidas por outro método (paralaxe, aglomerados) — só assim a relação período-luminosidade pode ser calibrada em escala absoluta. Uma vez calibrada, uma Cefeida se torna uma **vela padrão**: sua luminosidade é conhecida a partir do período observado, permitindo calcular a distância diretamente.

**Edwin Hubble (1926)** usou Cefeidas para descobrir variáveis em Andrômeda (M31), confirmando que ela era de fato **outra galáxia**, e não uma nebulosa dentro da Via Láctea — o marco que estabeleceu a existência de outras galáxias há exatamente 100 anos. Em **1929**, Hubble usou Cefeidas em várias galáxias próximas para mostrar que (exceto para as mais próximas, como M31 e as Nuvens de Magalhães) galáxias seguem uma relação linear entre velocidade radial e distância — a **Lei de Hubble**, cujo coeficiente angular é a constante de Hubble, medindo a taxa de expansão do Universo.

## 💥 Distâncias a galáxias distantes — Supernovas Tipo Ia

Estrelas de massa próxima à do Sol terminam suas vidas como **anãs brancas** (após a fase de ramo assintótico e ejeção de nebulosa planetária). Uma característica fundamental das anãs brancas é o **limite de massa de Chandrasekhar** ($\sim1{,}4\,M_\odot$). Em um sistema binário, uma anã branca pode acretar material de uma estrela companheira; se atingir o limite de Chandrasekhar, ocorre uma **supernova tipo Ia**.

Como todas as SN Ia explodem com massa muito próxima do mesmo limite, elas liberam quantidades de energia muito semelhantes — suas luminosidades são bem conhecidas e podem ser usadas como **velas padrão** \[K. Maguire 2017]. Diferentemente de estrelas individuais, supernovas podem brilhar tanto quanto uma galáxia inteira, permitindo medir distâncias com precisão a distâncias muito maiores do que qualquer outro método da escada.

### Calibração completa da constante de Hubble

1. Paralaxes de Cefeidas na Via Láctea;
2. Cefeidas em galáxias próximas (ex.: M31);
3. Cefeidas em galáxias que também hospedaram SN Ia;
4. SN Ia em galáxias distantes.

Cada elo depende do anterior — por isso "escada".

## 🧭 Sistemas de coordenadas

### Horizontal

Planos fundamentais: horizonte e meridiano (grande círculo vertical que inclui o zênite e os polos celestes). Coordenadas: **altitude** (ângulo entre horizonte e astro), **distância zenital** (usada para calcular a massa de ar atravessada pela luz na atmosfera) e **azimute** (ângulo entre meridiano e o vertical do astro, no plano horizontal, Leste-Oeste).

### Equatorial

Planos fundamentais: equador celeste e círculo horário (grande círculo pelos polos celestes e o astro, perpendicular ao equador). Coordenadas: **Ascensão Reta** ($\alpha$, medida a partir do ponto vernal, tradicionalmente em h:m:s, mas cada vez mais em graus — ex.: catálogo 2MASS) e **Declinação** ($\delta$, ao longo do círculo horário, do equador até o astro).

### Galáctico

Planos fundamentais: equador galáctico e meridianos pelo astro e polos galácticos — o plano galáctico é inclinado **62°36'** em relação ao equador celeste. Coordenadas: **longitude galáctica** ($l$, a partir da linha Sol–Centro Galáctico, no sentido da rotação) e **latitude galáctica** ($b$, do plano galáctico até o astro).

Convenção de quadrantes: 1º ($0°<l<90°$), 2º ($90°<l<180°$), 3º ($180°<l<270°$), 4º ($270°<l<360°$). Antes de 1958 usava-se um sistema antigo $(l^I, b^I)$, no qual o Centro Galáctico tinha coordenadas $(327°41', -1°24')$; o sistema atual é às vezes indicado $(l^{II}, b^{II})$ para distinguir.

Também é comum representar a posição de um astro em **coordenadas cartesianas galácticas** $(X,Y,Z)$, uma vez conhecida a distância $d$ ao Sol — atenção: convenções diferentes usam o eixo X apontando para o Centro ou para o Anticentro Galáctico, ou colocam a origem no próprio Centro Galáctico em vez do Sol.

### Precessão dos equinócios

Por a Terra não ser uma esfera perfeita, torques diferenciais da Lua e do Sol sobre seu equador fazem o eixo de rotação **precessionar**, com período de ~25.800 anos — mudando a posição do ponto vernal e, portanto, as coordenadas equatoriais de qualquer objeto ao longo do tempo (~1 arcominuto/ano ao longo da eclíptica). Por isso, coordenadas astronômicas só têm significado completo quando acompanhadas do **equinócio de referência** (épocas padrão: 1875.0, 1950.0, 2000.0, 2025.0; as coordenadas do catálogo Hipparcos são válidas para 1991.5). Antes de observar, é preciso precessionar as coordenadas de catálogo para a data corrente.

---

## 📌 Conceitos-chave

- **Escada cósmica de distâncias:** cada método (radar → paralaxe → ajuste de SP → Cefeidas → SN Ia) calibra o próximo, cobrindo escalas de $10^{-4}$ a $10^{10}$ anos-luz.
- **Parsec:** distância correspondente a paralaxe de 1 segundo de arco; $d\,[\text{pc}] = 1/p['']$.
- **Vela padrão:** objeto de luminosidade intrínseca conhecida (Cefeidas via relação P-L; SN Ia via limite de Chandrasekhar) — converte brilho aparente diretamente em distância.
- **Coordenadas galácticas $(l,b)$:** sistema com plano fundamental no disco da Via Láctea, essencial para qualquer estudo de arqueologia galáctica.

## 🔗 Referências e correlatos

- Bessel (1838) — primeira paralaxe estelar medida com sucesso
- Leavitt (1912) — relação período-luminosidade das Cefeidas
- Hubble (1926, 1929) — Cefeidas em M31; Lei de Hubble
- Oliveira et al. (2020) — ajuste de isócrona em Messier 69
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-03-magnitudes-cores-e-classificacao-espectral|Aula 03 — Magnitudes, Cores e Classificação Espectral]] — módulo de distância
- [[pt-br/resource/curso-on/aula-08-velocidades-e-movimento-proprio|Aula 08 — Velocidades e Movimento Próprio]]
- [[pt-br/resource/escolainverno/cosmologia/cosmologia-aula01|Escola de Inverno — Cosmologia, Aula 01]] — o mesmo topo da escada (supernovas Ia como velas padrão), aplicado à escala cosmológica em vez da galáctica
