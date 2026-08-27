---
publish: false
title: Aula 03 — Magnitudes, Cores e Classificação Espectral
created: 2026-07-23
modified: 2026-08-27
published: 2026-07-26T11:33:09.987-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - fotometria
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula03
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: Escala de magnitudes, magnitude absoluta, sistemas fotométricos, índices de cor e a classificação espectral OBAFGKM
professor: Hélio Dotto Perottoni
---

# ✨ Aula 03 — Magnitudes, Cores e Classificação Espectral

> [!note] Resumo
> Como quantificar o brilho das estrelas — da escala de Hiparco à magnitude absoluta — e como os índices de cor, derivados dessa escala, permitem inferir a temperatura de milhares de estrelas sem precisar de um espectro individual para cada uma.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni

---

## 💡 Propagação da luz e a degenerescência brilho–distância

O fluxo luminoso (energia emitida por unidade de área) diminui com o quadrado da distância à fonte (lei do inverso do quadrado). Isso gera uma **degenerescência** entre brilho intrínseco (luminosidade) e distância: ao observar um objeto brilhante no céu, nunca sabemos, só com o brilho aparente, se ele é intrinsecamente luminoso e distante, ou fraco e próximo. Por isso, o que sempre observamos diretamente é o **brilho aparente** — medido, na prática, contabilizando a quantidade de fótons recebida (hoje, via CCD).

## 📏 Escala de magnitude

**Hiparco** (190–120 a.C.) estabeleceu a primeira escala comparativa de brilho estelar, de 1 (mais brilhante) a 6 (limite da visão humana). Entre as magnitudes 1 e 6 há uma diferença de fator 100× em fluxo — logo, cada magnitude corresponde a um fator de $100^{1/5} \approx 2{,}512$ em fluxo. A definição formal:

$m_1 - m_2 = -2{,}5 \log_{10}\left(\frac{F_1}{F_2}\right)$

O sinal negativo impõe a relação **inversa** entre magnitude e brilho: quanto **menor** a magnitude, **mais brilhante** o objeto.

### Magnitude absoluta

A **magnitude absoluta ($M$)** é a magnitude que uma estrela teria se estivesse a exatamente **10 parsecs** do Sol — uma medida do brilho intrínseco, livre da degenerescência com a distância. A diferença entre magnitude aparente e absoluta é o **módulo de distância**:

$m - M = 5\log_{10}(d) - 5 \quad (d \text{ em parsec})$

Esta é uma das equações fundamentais da Astronomia. Exemplo de aplicação: sabendo que o módulo de distância da Grande Nuvem de Magalhães (LMC) é 18,5, e que a magnitude absoluta do Sol é $\approx4{,}8$, uma estrela de tipo solar na LMC teria magnitude aparente $m = 18{,}5 + 4{,}8 = 23{,}3$.

## 🎨 Sistemas de magnitude e fotométricos

- **VEGA magnitudes:** baseado na estrela Vega, definida com $V\approx0{,}03$ e cores $\approx0$ por construção. O zero-point depende do espectro de Vega em cada banda.
- **AB magnitudes:** definidas por um fluxo físico absoluto constante (independente do espectro de referência).
- **griz / Gunn / Oke:** baseados em calibração observacional, historicamente ligados a estrelas padrão (ex.: subanãs F).

> [!warning] Um sistema de magnitude não é um sistema de filtro
> Você pode usar qualquer filtro em qualquer sistema de magnitude — são dois conceitos independentes. Vários sistemas fotométricos foram desenvolvidos para diferentes aplicações e faixas de comprimento de onda \[Almeida-Fernandes et al. 2021; Perottoni et al. 2024].

## 🌈 Índices de cor

Em Astronomia, uma **cor** (ou índice de cor) é a diferença entre a magnitude de um objeto em duas faixas espectrais — ex.: $B-V$ (sistema Johnson/UBV). Na ausência de absorção seletiva, cores são **independentes de distância** (a degenerescência de brilho se cancela na subtração). Vega tem todas as cores iguais a 0 no sistema VEGAmag, por construção.

Considerando espectros de corpo negro de três estrelas com $T_a > T_b > T_c$:

- $T_a = 30\,000\,$K: fluxo em B maior que em V → $B-V < 0$ (mais azul)
- $T_b = 10\,000\,$K: fluxo em B $\approx$ fluxo em V → $B-V \sim 0$
- $T_c = 3\,000\,$K: fluxo em B menor que em V → $B-V > 0$ (mais vermelha)

Os índices de cor são de extrema importância prática: permitem estimar uma propriedade física (temperatura) de milhares de estrelas de uma vez, sem o custo de obter um espectro individual de cada uma.

## 🔬 Classificação espectral

### Desenvolvimento histórico

- **Final do séc. XIX (~1890):** Universidade de Harvard obtém espectros de ~10 mil estrelas; **Williamina Fleming** desenvolve as bases da classificação moderna com base na intensidade das linhas de H; nasce o **Catálogo Henry Draper (HD)**.
- **Início do séc. XX (~1910):** com uma amostra de ~200 mil espectros, **Annie Jump Cannon** aprimora a classificação considerando a correlação entre tipo espectral e cor (i.e., temperatura) — nasce a **Classificação de Harvard**.

### A sequência OBAFGKM

A classificação de Cannon considera 7 classes principais, organizadas por **temperatura decrescente** (não em ordem alfabética, por ser adaptação da classificação original de Fleming):

| Tipo | Temperatura | Linhas dominantes |
|---|---|---|
| O | Mais quente | He II (ionizado) |
| B | Muito quente | C, He I (neutro) |
| A | Quente | H (mais fortes de toda a sequência) |
| F–G | Intermediária | Metais em geral (Sol é G) |
| K–M | Fria | Linhas metálicas / moléculas (TiO em M) |

O pico do espectro da classe M está deslocado para comprimentos de onda maiores, enquanto o tipo O emite mais intensamente em $\lambda$ pequeno — a **Lei de Wien** em ação. Estrelas de tipo A ($\sim$10 mil K) têm as linhas de absorção de H mais intensas de toda a sequência (ver [[pt-br/resource/curso-on/aula-04-espectroscopia-e-metalicidade|Aula 04]] para a explicação física, via população dos níveis de energia do átomo de hidrogênio).

## 📷 Tipos de fotometria

- **Fotometria absoluta:** mede o brilho em escala física calibrada, permitindo comparar objetos em regiões diferentes do céu (_all sky_). Requer noite fotométrica e calibração com estrelas padrão — mais sensível a variações atmosféricas.
- **Fotometria diferencial:** mede o brilho relativo a outras estrelas do mesmo campo, observadas simultaneamente na mesma imagem. Menos afetada por condições atmosféricas; funciona mesmo sem noite perfeitamente fotométrica.
- **Fotometria no domínio do tempo (_time-domain_):** acompanha variações de brilho de um mesmo objeto ao longo do tempo (essencial para identificar variáveis, como as Cefeidas da Aula 07).

---

## 📌 Conceitos-chave

- **Magnitude aparente vs. absoluta:** a segunda remove a degenerescência com a distância — sua diferença é o módulo de distância, $m - M = 5\log_{10}d - 5$.
- **Índice de cor:** diferença de magnitudes em duas bandas; proxy barato e independente de distância para a temperatura efetiva.
- **OBAFGKM:** sequência de temperatura decrescente; tipo A tem as linhas de H mais fortes.

## 🔗 Referências e correlatos

- Almeida-Fernandes et al. (2021) — sistemas fotométricos
- Perottoni et al. (2024) — calibração fotométrica (GaiaXPy)
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-02-diagrama-hr-e-aglomerados|Aula 02 — Diagrama HR e Aglomerados Estelares]]
- [[pt-br/resource/curso-on/aula-04-espectroscopia-e-metalicidade|Aula 04 — Espectroscopia e Metalicidade]]
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01|Escola de Inverno — Arqueologia Galáctica, Aula 01]] — classificação OBAFGKM revisitada em contexto de nucleossíntese
