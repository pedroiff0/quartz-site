---
publish: true
encrypted: true
title: MinhaPesquisa-VizinhancaSolar-tSNE
discipline: Apresentação de Pesquisa
content: Mapeamento não supervisionado da vizinhança solar com GCNS + GALAH DR4 usando t-SNE (Banner SBPC e Banner Escola de Inverno)
professor: Orientação de Maria Luiza Linhares Dantas
created: 2026-07-22 13:34
modified: 2026-08-27 21:59
tags:
  - pesquisa
  - t-sne
  - galah
  - gcns
  - arqueologia-galactica
  - apresentacao
cssclasses:
  - page-grid
  - center-images
---
# 🔭 Minha Pesquisa — Mapeando a Vizinhança Solar com t-SNE

> [!abstract] Sobre esta nota
> Este é um texto corrido, em linguagem tranquila, para eu (re)explicar minha própria pesquisa antes de apresentá-la — reunindo o que está nos dois banners que preparei: o **Banner SBPC 2026** e o **Banner da Escola de Inverno**. Os PDFs originais ficam anexados abaixo só como referência visual (pra eu olhar os gráficos); o conteúdo escrito já está todo explicado em texto aqui embaixo, então não preciso decorar o banner palavra por palavra.

---

## 📎 Banners (anexar aqui como referência)

> [!example]- 📄 Banner SBPC 2026 — "Unveiling the Solar vicinity..." (clique para expandir)
> ![[BannerSBPC.pdf]]
> *Coloque aqui o PDF exportado do Overleaf (projeto `BannerSBPC`). Basta arrastar o arquivo para esta mesma pasta (`Apresentacao/`) com o nome `BannerSBPC.pdf` que o embed acima passa a funcionar sozinho no Obsidian.*

> [!example]- 📄 Banner Escola de Inverno — versão em português (clique para expandir)
> ![[BannerEscolaInverno.pdf]]
> *Mesma ideia: arraste o PDF exportado do projeto `BannerEscolaInverno` para esta pasta com esse nome.*

---

## 🎯 Do que se trata a pesquisa, em uma frase

Estou tentando entender **quem são as estrelas perto do Sol** — de onde vieram, que idade têm, que "sotaque químico" carregam — só que, em vez de plotar diagramas prontos escolhidos à mão, deixo um algoritmo de **aprendizado não supervisionado (t-SNE)** encontrar sozinho os agrupamentos diretamente nos espectros das estrelas, e só depois eu confiro se esses agrupamentos fazem sentido físico.

---

## 🧑‍🤝‍🧑 Quem fez

O trabalho é assinado por mim (**Pedro Henrique Rocha de Andrade**, IFF – Campus Bom Jesus do Itabapoana), pela **Ana Cecília Soja** (também IFF) e pela minha orientadora **Maria Luiza Linhares Dantas** (Instituto de Astrofísica da Pontificia Universidad Católica de Chile). O projeto tem apoio do CNPq, do IFF e, do lado da Maria Luiza, da ANID (agência chilena de pesquisa).

---

## 🌌 Por que olhar para a "vizinhança solar"?

Essa ideia de usar a composição química das estrelas como pista da história da Galáxia é exatamente a **arqueologia galáctica** que discuti na nota da Escola de Inverno (ver [[260720-Arqueologia-Galactica-Aula01]]): cada estrela "carrega" no espectro dela a assinatura química do gás de que se formou, então olhar abundâncias + movimento (cinemática) das estrelas funciona como pistas químio-dinâmicas para reconstruir de onde vieram, quais nasceram juntas (grupos coetâneos) e como o enriquecimento químico local aconteceu ao longo do tempo. O problema é que descrever uma estrela direito envolve muita coisa ao mesmo tempo — posição e movimento no espaço (astrometria/cinemática), temperatura, gravidade superficial, e até **dezenas de abundâncias químicas diferentes**. Isso é um espaço de parâmetros gigante e cheio de relações não lineares, difícil de visualizar com os diagramas tradicionais (um par de eixos de cada vez). Por isso a ideia de usar uma técnica de **redução de dimensionalidade não supervisionada**, que olha tudo de uma vez e organiza sozinha.

---

## 📊 Os dados: GCNS + GALAH DR4

Dois catálogos entram nessa história:

- **GCNS (Gaia Catalogue of Nearby Stars):** vem da missão espacial *Gaia* e reúne astrometria e fotometria de altíssima precisão para cerca de **330 mil estrelas** dentro de 100 parsecs do Sol — basicamente o "censo" de quem mora no nosso quintal galáctico.
- **GALAH DR4:** um levantamento espectroscópico terrestre (*GALactic Archaeology with HERMES*) que observou quase **1 milhão de estrelas** e fornece, para cada uma, até **30 abundâncias químicas diferentes**, além do espectro reduzido e normalizado.

Cruzando esses dois catálogos por identificação segura de cada estrela, sobra uma amostra de **cerca de 5 a 6 mil estrelas** que têm tanto a posição/movimento precisos do Gaia quanto a "ficha química" completa do GALAH. É nessa amostra combinada que a análise inteira acontece.

---

## 🧠 A ideia central: deixar o t-SNE "descobrir" sozinho

Aqui está a virada de chave dos dois banners: em vez de já entrar calculando `[Fe/H]` ou `[Mg/Fe]` e jogando num gráfico (o jeito clássico), eu alimento o algoritmo **diretamente com o fluxo espectral normalizado** — ou seja, o espectro bruto (já tratado) de cada estrela, que tem milhares de pontos (dimensões). O algoritmo usado é o **t-SNE** (*t-distributed Stochastic Neighbor Embedding*): ele pega esse espaço de altíssima dimensão e "achata" numa projeção 2D, tentando preservar ao máximo quem estava perto de quem originalmente — estrelas com espectros parecidos acabam próximas no mapa final, mesmo sem eu ter dito ao algoritmo o que procurar.

Só **depois** de gerar essa projeção 2D é que eu volto e coloro cada ponto pelos parâmetros físicos já conhecidos (temperatura efetiva `Teff`, gravidade superficial `logg`, metalicidade `[Fe/H]`) — isso funciona como um teste de honestidade do método: se o algoritmo realmente capturou física de verdade (e não só ruído), esses parâmetros deveriam variar suavemente pelo mapa, em vez de aparecerem espalhados ao acaso.

> [!tip] Um hiperparâmetro importante: a perplexidade
> O t-SNE tem um parâmetro chamado **perplexidade**, que controla, grosso modo, "quantos vizinhos" cada estrela considera ao se posicionar no mapa. Testei uma perplexidade **baixa (30)**, que dá mais peso a vizinhanças pequenas e por isso realça **estruturas locais** (pequenos subgrupos bem definidos), e uma **mais alta (50)**, que enxerga vizinhanças maiores e representa melhor a **topologia global** do conjunto todo (a forma geral do mapa).

---

## ✅ Isso realmente funciona? (validação quantitativa)

Não basta o mapa "parecer bonito" — dá pra medir objetivamente se a projeção em 2D é confiável, usando três métricas (essa parte é o coração do **Banner SBPC**, mais focado na validação técnica do método):

- **Divergência KL:** mede o quanto a distribuição de vizinhança no mapa 2D se afasta da distribuição original em alta dimensão — quanto **menor**, melhor (indica que o algoritmo "convergiu" bem).
- **Trustworthiness (confiabilidade):** confere se os vizinhos que aparecem próximos no mapa 2D **realmente eram** vizinhos no espaço original — evita "vizinhos falsos" criados só pelo achatamento.
- **Continuity (continuidade):** o oposto: confere se vizinhos que eram próximos no espaço original **continuam** próximos no mapa 2D — evita "perder" vizinhos verdadeiros.

Testando uma grade de perplexidades de 15 a 90, encontrei **Trustworthiness entre ~0,89 e 0,95** e **Continuity entre ~0,97 e 0,98** — ambas altas e estáveis o tempo todo, o que quer dizer que tanto a vizinhança local quanto a global estão bem preservadas na projeção. Já a divergência KL cai de forma constante conforme aumento a perplexidade, sugerindo que perplexidades maiores dão um ajuste global um pouco melhor — no fim, isso bate exatamente com a ideia de que **30 é melhor pra ver detalhe local** e **50 é melhor pra ver o quadro geral**.

E o resultado mais interessante: em **ambas** as perplexidades (30 e 50), aparece um **pequeno subgrupo destacado**, meio "separado" do resto do mapa, com seu próprio gradiente interno de metalicidade — ou seja, algo que pode ser uma população estelar diferente ou um grupo de estrelas anômalas, e que merece ser investigado com mais calma (é exatamente esse achado que puxa o "trabalho futuro" da pesquisa).

---

## 🪐 E a astrofísica por trás disso? (o que o Banner da Escola de Inverno acrescenta)

Enquanto o banner do SBPC fica mais no "o método funciona e é confiável", o **Banner da Escola de Inverno** dá um passo a mais e usa a amostra pra **caracterizar de fato quem são essas estrelas da vizinhança solar**, com os diagramas astrofísicos clássicos:

- **Distribuições de `[Fe/H]` e `[Mg/Fe]`:** mostram, respectivamente, o quão rica ou pobre em metais é a amostra e a razão entre magnésio e ferro (um traçador clássico de disco fino vs. disco espesso).
- **Diagrama de Kiel** (temperatura efetiva vs. gravidade superficial, colorido por `[Fe/H]`, com isócronas teóricas PARSEC+COLIBRI sobrepostas) + **histograma de idades:** usado pra checar se os parâmetros espectroscópicos batem com o esperado teoricamente e pra estimar a idade das estrelas.
- **Diagrama de Toomre** (velocidade $V$ vs. $\sqrt{U^2+W^2}$, as componentes de velocidade da estrela em relação ao Sol): separa estatisticamente estrelas de **disco** (movimento mais "manso", parecido com o do Sol) de estrelas de **halo** (movimento muito mais rápido/desalinhado) — o Sol aparece marcado como referência.
- **Diagrama de Tinsley-Wallerstein** (`[Mg/Fe]` vs. `[Fe/H]`, comparado com a referência de Recio-Blanco et al. 2014): esse é o clássico "mapa" para separar disco fino de disco espesso químicamente, olhando o quanto cada população é enriquecida em elementos-$\alpha$ (como o magnésio) em relação ao ferro.

### O que esses diagramas mostram, na prática
A vizinhança solar analisada é dominada por estrelas de **sequência principal dos tipos F, G e K** (ver a classificação espectral em [[260720-Arqueologia-Galactica-Aula01]]), com **idade mediana em torno de 1,6 bilhão de anos** e uma **leve deficiência de metais** em relação ao Sol (`[Fe/H]` mediano ≈ −0,19 dex — ou seja, um pouquinho menos "temperada" em metais que o Sol). O diagrama de Kiel bate bem com as isócronas teóricas, o que dá confiança nos parâmetros espectroscópicos usados. O diagrama de Toomre confirma que a amostra é majoritariamente de **disco galáctico**, com só uma fração pequena de estrelas de halo. E, entre as estrelas de disco espesso presentes na amostra, a componente mais comum é justamente a **rica em metais e enriquecida em elementos-$\alpha$** — só que aqui vale uma ressalva importante: isso pode ser, em parte, um efeito da **função de seleção** combinada dos dois catálogos (ou seja, um viés de quais estrelas entraram na amostra), não necessariamente um fato 100% intrínseco da Galáxia.

---

## 🔮 Próximos passos

A ideia daqui pra frente é usar **clusterização baseada em densidade** (como o algoritmo **HDBSCAN**) em cima da projeção do t-SNE, para caracterizar de forma mais objetiva (e não só visual) aquele subgrupo destacado que apareceu tanto em perplexidade 30 quanto em 50 — e complementar com mais diagnósticos de *chemical tagging* (comparação detalhada de abundâncias químicas) pra testar se esse grupo é mesmo uma população à parte.

---

## 📌 Glossário rápido (pra não esquecer na hora de apresentar)

- **t-SNE:** técnica de redução de dimensionalidade não linear que projeta dados de altíssima dimensão em 2D, preservando ao máximo as relações de vizinhança.
- **Perplexidade:** hiperparâmetro do t-SNE que controla o "tamanho" da vizinhança considerada — baixa = foco local, alta = foco global.
- **Divergência KL / Trustworthiness / Continuity:** métricas que medem, de formas diferentes, o quão fiel é a projeção 2D em relação ao espaço original de alta dimensão.
- **GCNS:** catálogo astrométrico do Gaia com estrelas a até 100 pc do Sol.
- **GALAH DR4:** levantamento espectroscópico com abundâncias químicas detalhadas de quase 1 milhão de estrelas.
- **Diagrama de Kiel:** como o diagrama HR, mas com gravidade superficial no lugar de luminosidade — usado com isócronas para estimar idades.
- **Diagrama de Toomre:** separa estrelas de disco e de halo pela velocidade espacial em relação ao Sol.
- **`[Fe/H]`, `[Mg/Fe]`:** notações de abundância química (ver também [[260720-Arqueologia-Galactica-Aula01]]) usadas para identificar populações estelares (disco fino vs. disco espesso).
- **dex:** unidade logarítmica (base 10) usada para expressar essas razões de abundância.

---

## 🔗 Ver também
- [[260720-Arqueologia-Galactica-Aula01]] — conceitos de populações estelares, metalicidade e classificação espectral usados nesta pesquisa.
- [[00-Resumo-Escola-de-Inverno]] — panorama geral da Escola de Inverno.
