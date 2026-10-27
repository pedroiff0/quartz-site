---
publish: true
title: Detecção de Anomalias Espectrais em Estrelas (GALAH DR4)
created: 2026-09-19T13:18:29-03:00
modified: 2026-10-27T12:32:51-03:00
tags:
  - pesquisa
  - academico
cssclasses:
  - page-layout
icon: lucide-book-open
sitesync: true
resource-sync: true
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>[[pt-br/research/index|Pesquisas]]</span> <span class="academic-nav-sep">/</span> <span>Deteccao De Anomalias Iff 2025</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Detecção de Anomalias Espectrais em Estrelas (GALAH DR4)</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">← Início</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">[[pt-br/research/index|Hub]]</span> <span class="academic-nav-counter">(1 de 2)</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/research/index|Pesquisas →]]</span>

</div>

</div>

</div>

# Detecção de Anomalias Espectrais em Estrelas (GALAH DR4)

> [!abstract] Ficha da Pesquisa
> - **Projeto:** procurar estrelas diferentes das outras olhando o espectro de cada uma, com dados do GALAH DR4 e do Gaia
> - **Equipe:** Pedro Henrique Rocha de Andrade, [Dra. Maria Luiza Linhares Dantas](https://www.mlldantas.com) e [Dra. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja)
> - **Instituição:** Instituto Federal Fluminense (IFF) e Pontificia Universidad Católica de Chile, com apoio do CNPq
> - **Status:** em andamento

---

## Síntese da Pesquisa

O espectro de uma estrela é a luz dela separada em cores, como um arco-íris cheio de linhas escuras e claras. Cada estrela tem o seu, e ele diz do que ela é feita, quão quente ela é e se tem alguma coisa estranha acontecendo. A pesquisa usa métodos de aprendizado de máquina que não recebem nenhuma resposta pronta: eles só olham os espectros e agrupam os parecidos. A pergunta é o que aparece quando a gente deixa os próprios espectros se organizarem, e quais estrelas ficam fora do padrão.

---

## A história até aqui

Essa pesquisa tem uma história de dois congressos. No SAB 2025 eu mostrei o que os números do catálogo dizem sobre as estrelas perto do Sol. No SAB 2026 eu volto com uma pergunta maior: e se a gente olhar o espectro inteiro de cada estrela, o que aparece que esses números não mostram? Entre um congresso e outro, o projeto parou, voltou, mudou de método e ganhou um painel na web.

| Fase | Quando | O que aconteceu |
| :--- | :--- | :--- |
| Começo | 2025 | Uma pergunta sobre as estrelas perto do Sol, respondida com os números do catálogo e levada ao SAB 2025 |
| Transição | Fim de 2025 | Primeiros testes com aprendizado de máquina e a primeira tentativa de ler os espectros |
| Meio | 2026 | Muitos testes de métodos, uma primeira versão do TCC e uma pausa |
| Retomada | 2026 | A decisão de usar o espectro do jeito que ele vem e a extração dos espectros de todo o GALAH |
| Agora | SAB 2026 | O banner de mapa mental e o painel na web para explorar o mapa |
| Próxima etapa | Próximos anos | O mapa com o GALAH completo e o TCC |

### O começo: o que o catálogo diz

Tudo começou com uma pergunta simples: quão variadas são as estrelas que estão a até 100 parsecs do Sol (cerca de 326 anos-luz)? Para responder, eu cruzei dois catálogos. O Gaia Catalogue of Nearby Stars (GCNS) diz quais são as estrelas mais próximas, e o GALAH DR4 diz como elas são por dentro. Sobraram 6.198 estrelas que aparecem nos dois. Nessa fase eu usei só o que já vem pronto no catálogo, como temperatura, gravidade na superfície, quantidade de metais, idade e velocidade, sem abrir nenhum espectro.

Foi um período de trabalho pesado: medir a composição química, as idades e a metalicidade, montar os diagramas que separam as estrelas por tipo e por movimento, escrever um artigo em LaTeX e fechar o banner que levei ao SAB 2025, em Caxambu. Logo depois ainda fiz a fotometria do Gaia, que mostra o brilho e a cor de cada estrela, e organizei o repositório do projeto.

### O meio: dos números ao espectro

Depois do congresso comecei a testar métodos que desenham mapas a partir de muitos dados ao mesmo tempo, como o t-SNE e o UMAP, e fiz a primeira tentativa de ler os espectros. Vieram muitas variações desses métodos, algumas boas, outras que não levaram a lugar nenhum, e uma primeira versão do texto do TCC. Aí o projeto ficou parado por alguns meses.

A retomada veio com uma série de reuniões com a equipe, e delas saiu a decisão que mudou o trabalho: usar o espectro do GALAH exatamente como ele vem, sem ajustar nem inventar nenhum ponto. Reorganizei o projeto, deixei de lado os métodos que não estavam ajudando e extraí os espectros de todas as estrelas do GALAH DR4, um volume de dados de cerca de 54 GB. Desse esforço saiu o caminho que virou o banner de 2026: mapas feitos com o espectro inteiro de cada estrela.

### Onde estou agora

Agora o trabalho está no SAB 2026, em Natal, com um banner novo e um painel na web onde dá para explorar os mapas da amostra. O próximo passo é aplicar o mesmo método a todas as estrelas do GALAH, que está descrito mais abaixo.

---

## SAB 2025: o pôster em detalhe

O SAB 2025 foi em Caxambu (MG) e foi a minha primeira participação em um congresso nacional. A nota do evento está em [[pt-br/media/2025/sab|SAB 2025]]. O pôster se chama *Stellar properties and chemical features of the Gaia Catalogue of Nearby Stars observed by GALAH DR4* e foi feito com a [Dra. Maria Luiza Linhares Dantas](https://www.mlldantas.com) e a [Dra. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja). O banner completo está em [[resource/meta/banners/bannersab25.pdf|bannersab25.pdf]].

A ideia do pôster era descrever a vizinhança do Sol só com os números do catálogo. As figuras abaixo estão na ordem em que eu as usaria para explicar.

**Metais.** Para a astronomia, "metal" é qualquer elemento mais pesado que o hélio. O histograma mostra quanto ferro as estrelas têm em comparação com o Sol ([Fe/H]). A mediana fica em -0,19, ou seja, as estrelas por aqui têm um pouco menos metal que o Sol, e a cauda para a esquerda mostra as estrelas mais antigas e mais pobres.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig2-feh.png|560]]

**Magnésio em relação ao ferro.** Essa medida ([Mg/Fe]) ajuda a separar as duas partes do disco da Galáxia: o disco fino, mais jovem, e o disco espesso, mais antigo. A mediana é 0,12 e a distribuição é bem concentrada, o que já sugere que a maioria das estrelas é do disco fino.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig3-mgfe.png|560]]

**Idade.** O pico perto de zero pode ser um limite do método que calcula as idades, um erro ou estrelas jovens de verdade, e eu não tentei separar isso no pôster. O pico em torno de 3 bilhões de anos é a população principal, e a mediana da amostra é 1,5 bilhão de anos.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig4-idade.png|560]]

**Diagrama de Kiel.** Ele coloca cada estrela pela temperatura e pela gravidade na superfície. A amostra (pontos vermelhos) está quase toda na sequência principal fria, a fase em que as estrelas passam a maior parte da vida, sobre o GALAH DR4 inteiro em amarelo. As linhas são modelos de estrelas com 1,5 bilhão de anos, perto da idade mediana.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig5-kiel.png|620]]

**Diagrama de Toomre.** Ele separa as estrelas pelo jeito como se movem na Galáxia. As que giram junto com o disco ficam perto do Sol no gráfico, e as que se movem muito diferente, acima de 100 km/s, são candidatas ao halo. São 5.970 estrelas de disco e 228 de halo: a maioria esmagadora é disco.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig6-toomre.png|700]]

**Disco fino e espesso.** Este gráfico cruza magnésio e ferro, e a curva de Recio-Blanco et al. (2014) divide as estrelas: acima dela, disco espesso; abaixo, disco fino. As estrelas bem acima da curva são 22,51% da amostra. Parte desse disco espesso rico em metais deve vir do jeito como os dois catálogos escolheram as estrelas, e não da Galáxia em si.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig7-tinsley.png|700]]

O resultado em poucas linhas: cerca de 6.000 estrelas, a maioria parecida com o Sol (com algumas mais quentes), temperaturas entre 3000 K e 8000 K, idade mediana de 1,5 bilhão de anos, um pouco menos de metal que o Sol e quase todas no disco. A lacuna que ficou é que tudo isso veio do catálogo. Os espectros ficaram de fora, e é daí que sai o trabalho de 2026.

### Banner do SAB 2025

![[resource/meta/site-static/banners/bannersab25.pdf]]

## SAB 2026: a continuação

O SAB 2026 é em Natal (RN). A nota do evento está em [[pt-br/media/2026/sab/index|SAB 2026]]. O trabalho se chama *How varied are stellar populations in the Solar vicinity? Exploring GCNS and GALAH DR4 with t-SNE* e é feito com a [Dra. Maria Luiza Linhares Dantas](https://www.mlldantas.com) e a [Dra. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja). Os banners estão em [[resource/meta/banners/bannersab26-mapa-mental.pdf|versão mapa mental]] e [[resource/meta/banners/bannersab26-base-v3.pdf|versão base]].

As estrelas são as mesmas 6.198, mas agora eu olho o espectro inteiro de cada uma, ponto por ponto: são 14.245 pontos por estrela, vindos das quatro câmeras do instrumento, uma para cada faixa de cor. Eu uso o espectro do jeito que ele vem, sem ajustes. Entram no mapa 5.304 estrelas. As outras 894 ficam de fora porque falta o pedaço de alguma das câmeras, e eu nunca invento o que falta. No banner de mapa mental, o mapa fica no centro e cada painel ao redor é uma pergunta sobre ele.

**O mapa.** Cada ponto é uma estrela. Estrelas com espectros parecidos ficam perto. A cor é a temperatura, e os símbolos marcam estrelas com linhas de emissão (laranja), sinais de que estão brilhando além do normal, e estrelas que na verdade são duplas (losango e círculo). O mapa nunca viu a temperatura nem nenhum outro número: só o espectro.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig1-mapa-tsne.png|760]]

**Cores.** Pintando o mesmo mapa por temperatura, gravidade e metais, aparece uma ordem por temperatura e uma variação suave de gravidade e de metais. Nada disso foi dado ao método. Ele descobriu sozinho.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig2-coloracoes.png|760]]

**Avisos do GALAH.** O próprio GALAH marca as estrelas em que viu algum problema ou característica especial. Aqui eu separo as estrelas sem aviso, com aviso e só com emissão, para ver onde elas caem no mapa. Esses filtros só mudam o que aparece na tela, não refazem o mapa. Mais da metade das estrelas do mapa (52%) tem o aviso de sinal fraco.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig3-flags.png|760]]

**Estrelas com emissão.** São 286 estrelas, e elas se dividem em cinco grupos menores dentro do mapa. O maior é de estrelas frias com metais parecidos com os do Sol, e outros dois são de estrelas pobres em metais.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig4-emissao-subclusters.png|760]]

No diagrama de Kiel, as estrelas com emissão ficam na sequência principal fria, em cima das anãs vermelhas. Um dos grupos, perto de 4500 K, é o mais quente.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig5-kiel-subclusters.png|620]]

**Outras configurações.** O mesmo mapa feito com outros ajustes do t-SNE e com o UMAP, com a emissão destacada. A organização das estrelas continua lá quando troco o método e os ajustes, que é exatamente o que eu queria testar.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig6-outras-projecoes.png|760]]

**Espectros.** Uma estrela com emissão e uma estrela comum lado a lado, com as linhas do hidrogênio (Hα), do lítio e do potássio. É a checagem de que a diferença que o mapa mostrou aparece de verdade na luz das estrelas.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig7-espectros.png|760]]

O que fica do banner: a ordem por temperatura aparece sozinha, sem ninguém dizer ao método o que é temperatura, em todas as versões que testei, e as estrelas com emissão se dividem em cinco grupos. Por enquanto esses grupos são candidatos, não classes definitivas: ainda falta testar com cuidado se eles se mantêm quando mudo os ajustes.

### Banners do SAB 2026

A versão mapa mental é a que será apresentada: o mapa central e, ao redor, as perguntas sobre ele. A versão base segue o layout linear do banner do SAB 2025.

#### Versão mapa mental

![[resource/meta/site-static/banners/bannersab26-mapa-mental.pdf]]

#### Versão base

![[resource/meta/site-static/banners/bannersab26-base-v3.pdf]]

## Trabalhos futuros: o GALAH completo

O próximo passo é levar o mesmo método da amostra perto do Sol para o GALAH DR4 inteiro, com mais de 900 mil estrelas. Os espectros já estão extraídos. O que falta é desenhar o mapa com todos eles.

A figura abaixo é um ensaio. À esquerda estão as anãs vermelhas da amostra local e, à direita, 30 mil estrelas sorteadas do GALAH completo, as duas coloridas por temperatura. Ela mostra que o método continua ordenando as estrelas por temperatura quando a amostra cresce e fica mais variada. Ainda não é o resultado com o GALAH completo.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/futuro-galah-completo-subamostra.png|760]]

O que já está pronto e o que falta:

- **Programa para rodar tudo:** já existe e foi testado com 10 mil espectros reais. Falta rodar com as centenas de milhares de estrelas.
- **Computação:** o GALAH inteiro precisa de horas de processamento em placas de vídeo potentes para cada versão do mapa.
- **Painel na web:** a versão pública mostra a amostra perto do Sol. A parte do GALAH completo existe, mas por enquanto é de uso interno.
- **Depois do mapa:** confirmar se os grupos se mantêm e olhar os espectros das estrelas candidatas, uma a uma.
- **Escrita:** o TCC, com a análise do GALAH completo como parte central.
