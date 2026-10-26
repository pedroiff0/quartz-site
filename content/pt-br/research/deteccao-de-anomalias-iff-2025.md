---
publish: true
title: Detecção de Anomalias Espectrais em Estrelas (GALAH DR4)
created: 2026-09-19T13:18:29-03:00
modified: 2026-10-26T15:15:18-03:00
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

> [!abstract] Ficha Técnica da Pesquisa
> - **Projeto:** Detecção de anomalias espectrais em estrelas da Via Láctea via GALAH DR4 e BASTA
> - **Instituição:** Instituto Federal Fluminense (IFF) & PUC-Chile / CNPq
> - **Status:** Em andamento

---

## Síntese da Pesquisa

Aplicação de métodos de aprendizado de máquina não supervisionado e códigos de inferência estelar (BASTA) para a identificação e caracterização de anomalias químicas e espectrais no levantamento GALAH DR4.

---

## Cronologia 2025 a 2026: começo, meio e fim

Essa pesquisa tem uma história de dois congressos. Em 2025 eu fui ao SAB mostrar o que os parâmetros do catálogo dizem sobre as estrelas perto do Sol. Em 2026 volto ao SAB com uma pergunta maior: e se a gente olhar o espectro inteiro de cada estrela, o que aparece que os parâmetros não mostram? Entre um e outro, o projeto parou, voltou, mudou de método e ganhou um painel na web. Abaixo está o caminho, na ordem em que aconteceu.

| Quando | Fase | O que saiu dela |
| :--- | :--- | :--- |
| 07/2025 a 09/2025 | Começo | Análise dos parâmetros, artigo em LaTeX e o banner do SAB 2025 |
| 10/2025 a 11/2025 | Transição | Fotometria do Gaia, primeiro ensaio de ML e primeira tentativa com o espectro |
| 03/2026 a 07/2026 | Meio | Notebooks de ML, versão anterior do TCC e uma pausa longa |
| 09/2026 | Meio | Retomada, escolha do espectro nativo e matriz de 54 GB |
| 10/2026 | Fim da etapa | Banner do SAB 2026, painel público e viewer |
| 2027 a 2028 | Próxima etapa | GALAH DR4 completo e TCC |

### Começo: o que o catálogo diz (07/2025 a 10/2025)

Tudo começou em 04/07/2025, com uma pergunta simples: quão variadas são as populações de estrelas até 100 pc do Sol? Eu cruzei o Gaia Catalogue of Nearby Stars (GCNS) com o GALAH DR4 e fiquei com 6.198 estrelas que têm os dois. Nessa fase eu só usei o que já vem pronto no catálogo: Teff, log g, [Fe/H], abundâncias, idade e as velocidades. Nenhum espectro foi olhado.

Em julho e agosto foi o trabalho pesado: abundâncias, idades, metalicidade, diagrama de Kiel com isócronas, diagrama de Toomre, separação entre disco fino e espesso, histograma de todos os elementos e o artigo em LaTeX. O banner ficou pronto em 25/09/2025 e foi apresentado no SAB 2025, em Caxambu. Logo depois, em outubro, fiz a fotometria do Gaia (diagrama cor-magnitude) e limpei o repositório.

### Meio: do parâmetro ao espectro (11/2025 a 10/2026)

Em novembro de 2025 eu comecei a testar t-SNE, UMAP, PCA e HDBSCAN e fiz a primeira tentativa de ler os espectros (24/11/2025). Em março de 2026 vieram dezenas de variantes desses métodos, junto com Isolation Forest e autoencoders, só que sem um relatório fechando o que cada um mostrou. Em junho e julho eu escrevi uma versão anterior do TCC e fiz a primeira figura dos bits de `flag_sp`. Depois disso, de 05/07/2026 a 01/09/2026, não há nada registrado.

A retomada foi em setembro, com quatro reuniões (01/09, 08/09, 15/09 e 22/09). Nelas ficou decidido usar o espectro single fit do DR4 como ele vem, sem interpolar. No dia 17/09 eu reorganizei o repositório e, no dia 25/09, tirei o Isolation Forest do centro do trabalho. No dia 26/09 terminei a extração da matriz espectral completa do GALAH DR4 (54 GB) e escolhi o caminho que virou o banner: t-SNE e UMAP sobre os 4 CCDs, com métrica cosseno e sem PCA.

Em 02/10/2026 saiu o pacote de processamento que roda no Mac e o painel unificado. Em outubro vieram as estrelas com emissão, os subclusters por HDBSCAN e as duas versões do banner do SAB 2026.

### Fim da etapa: SAB 2026 e o painel (10/2026)

De 25/10/2026 a 30/10/2026 eu apresento o banner no SAB 2026, em Natal. No dia 26/10/2026 o painel público entrou no ar, com a figura principal do banner e a análise da amostra local. O que falta, o GALAH DR4 inteiro, está na seção de trabalhos futuros, mais abaixo. O histórico completo, com cada commit e cada dúvida em aberto, está na linha do tempo detalhada.

---

## SAB 2025: o pôster em detalhe

O SAB 2025 foi em Caxambu (MG), de 28/09/2025 a 02/10/2025, e foi a minha primeira participação em um congresso nacional. A nota do evento está em [[pt-br/media/2025/sab|SAB 2025]]. Apresentei o pôster *Stellar properties and chemical features of the Gaia Catalogue of Nearby Stars observed by GALAH DR4*, junto com a professora Ana Cecília Soja. O banner completo está em [[resource/meta/banners/bannersab25.pdf|bannersab25.pdf]].

A ideia do pôster era descrever a vizinhança solar só pelos parâmetros do catálogo. As figuras abaixo são as que mais orientam o trabalho, na ordem em que eu as usaria para explicar.

**Metalicidade.** Esse é o histograma de [Fe/H] da amostra. A mediana fica em -0,19 dex, ou seja, as estrelas por aqui são um pouco mais pobres em metais que o Sol, e a cauda para a esquerda mostra a população mais antiga.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig2-feh.png|560]]

**[Mg/Fe].** É o indicador que ajuda a separar disco fino de disco espesso. A mediana é 0,12 dex e a distribuição é bem concentrada, o que já sugere uma população dominada por disco fino.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig3-mgfe.png|560]]

**Idade.** O pico perto de zero pode vir de degenerescência na idade, de um artefato ou de uma subpopulação jovem de verdade, e eu não tentei separar isso no pôster. O pico em torno de 3 Gyr é a população principal, e a mediana da amostra é 1,5 Gyr (de 0,10 a 14,79 Gyr).

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig4-idade.png|560]]

**Diagrama de Kiel.** A amostra (pontos vermelhos) está quase toda na sequência principal fria, sobre o GALAH DR4 inteiro em amarelo. As isócronas ajudam a ver onde ficam as estrelas de 1,5 Gyr, perto da idade mediana.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig5-kiel.png|620]]

**Diagrama de Toomre.** Separa disco de halo pela velocidade em relação ao LSR. São 5.970 estrelas de disco e 228 de halo, com o limite de 100 km/s. A maioria esmagadora é disco.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig6-toomre.png|700]]

**Disco fino e espesso.** O gráfico de [Mg/Fe] contra [Fe/H], com a curva de Recio-Blanco et al. (2014), classifica as estrelas pela distância à curva. As estrelas acima de 2σ são 22,51% da amostra, e o disco espesso rico em metais e enriquecido em alfa deve ser, em parte, efeito de seleção.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig7-tinsley.png|700]]

O resultado em poucas linhas: cerca de 6.000 estrelas, a maioria FGK de sequência principal (com alguns tipos A) entre 3000 K e 8000 K, idade mediana de 1,5 Gyr, [Fe/H] mediano de -0,19 dex e disco dominante. A lacuna que ficou é que tudo isso é catálogo. Os espectros ficaram de fora, e é daí que sai o trabalho de 2026.

## SAB 2026: a continuação

O SAB 2026 é em Natal (RN), de 25/10/2026 a 30/10/2026. A nota do evento está em [[pt-br/media/2026/sab/index|SAB 2026]]. O trabalho se chama *How varied are stellar populations in the Solar vicinity? Exploring GCNS and GALAH DR4 with t-SNE* e é feito com a Maria Luiza Linhares Dantas e a Ana Cecília Soja. Os banners estão em [[resource/meta/banners/bannersab26-mapa-mental.pdf|versão mapa mental]] e [[resource/meta/banners/bannersab26-base-v3.pdf|versão base]], e o roteiro completo em Narrativa do banner SAB26.

Eu mantive a mesma amostra de 6.198 estrelas, mas agora olho o espectro single fit inteiro, pixel a pixel, nos 4 CCDs (14.245 pixels), sem interpolar e sem PCA, com métrica cosseno. Entram no mapa 5.304 estrelas. As outras 894 ficam de fora porque não têm os 4 CCDs completos, e eu nunca preencho o que falta. No banner de mapa mental, o mapa t-SNE é o centro e cada painel ao redor é uma pergunta sobre ele.

**O mapa.** Cada ponto é uma estrela. Estrelas com espectros parecidos ficam perto. As cores são Teff, e os símbolos marcam emissão (laranja), SB1 (losango) e SB2 (círculo). O mapa nunca viu os parâmetros, só o espectro.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig1-mapa-tsne.png|760]]

**Colorações.** Pintando o mesmo mapa por Teff, log g e [Fe/H], aparece uma ordenação por temperatura e um gradiente de gravidade e metalicidade. Nada disso foi dado ao método.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig2-coloracoes.png|760]]

**Flags.** Aqui eu separo as estrelas pelo `flag_sp` do GALAH: sem flag, com flag e só emissão. É uma forma de ver onde ficam as estrelas que o próprio GALAH marcou como problemáticas. Os cortes de S/N e de Teff só filtram o que aparece, não recalculam o mapa, e 52% das estrelas mapeadas têm a flag de S/N baixo.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig3-flags.png|760]]

**Estrelas com emissão.** São 286 estrelas e elas formam cinco subclusters por HDBSCAN. O S0 é o maior, frio e de [Fe/H] solar, e o S1 e o S2 são pobres em metais.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig4-emissao-subclusters.png|760]]

No diagrama de Kiel, as emissoras ficam na sequência principal fria, em cima do ramo das anãs M. O S3, perto de 4500 K, é o mais quente.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig5-kiel-subclusters.png|620]]

**Outras configurações.** t-SNE com perplexidade 30 e 50 e UMAP com 15 e 30 vizinhos, com a emissão destacada. A estrutura sobrevive à troca de método e de parâmetros, que é o que eu queria testar.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig6-outras-projecoes.png|760]]

**Espectros.** Uma emissora e uma anã sem flag lado a lado, um painel por CCD, com as linhas de Hα, Li e K I. É a checagem de que o que o mapa separou aparece de fato no espectro.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig7-espectros.png|760]]

O que fica do banner: a ordenação por Teff surge sem rótulos no t-SNE e no UMAP, em todas as configurações que testei, e o bit de emissão se divide em cinco grupos. O resultado são candidatos, não classes, porque o HDBSCAN e os cortes ainda não foram varridos.

## Trabalhos futuros: o GALAH completo

O próximo passo é levar o mesmo método do GALAH local para o GALAH DR4 inteiro. A matriz espectral já está extraída: 905.415 espectros válidos, cerca de 54 GB. O que falta é calcular o mapa em cima dela.

A figura abaixo é o ensaio que existe hoje. À esquerda está a amostra local de anãs M e, à direita, uma subamostra de 30 mil estrelas do GALAH completo, ambas em t-SNE e coloridas por Teff. Ela mostra que o método continua ordenando por temperatura quando a amostra cresce e fica mais variada. Não é o resultado do GALAH completo, é só um ensaio com uma fração dele.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/futuro-galah-completo-subamostra.png|760]]

O que já está pronto e o que falta:

- **Pacote para o Mac:** o pacote `processing/` calcula o kNN exato, UMAP, t-SNE e HDBSCAN sem PCA, com teto de memória e retomada, e já foi testado com 10 mil espectros reais. O 100k e o completo ainda não foram medidos. Detalhes em pipeline do Mac.
- **Custo estimado:** cerca de 4,5 horas por rodada numa GTX 1660 e perto de 40 minutos numa A100. O plano é de 18 rodadas, entre 40 e 60 horas de GPU A100, ainda não executado.
- **Painel web:** o painel de análise já tem a parte do GALAH completo (projeções com as janelas de Traven et al. 2017), de uso interno por enquanto. A versão pública mostra só a amostra local.
- **Depois do mapa:** varrer o HDBSCAN e os cortes, confirmar os candidatos nos espectros e comparar as idades do GALAH com as do BASTA em uma amostra de 100 estrelas.
- **Escrita:** o TCC, em 2027.2 e 2028.1, com a análise do GALAH completo como parte central.

---

## Estrutura do Projeto

- **Anotações:** Notas e Rascunhos
- **Arquivos:** Registros e atas de progresso
- **Meetings:** Ata da Reunião Mais Recente
- **Notes:** Metodologia TCC & Web Interface
- **Papers:** Artigos de referência

## Viewer e processamento (02/10/2026)

- **Arquitetura do viewer (app único, porta 8507):** como roda, como editar
- **Processamento portátil no Mac (GALAH DR4 completo, sem PCA):** decisões, medições e pendências
- **Diário da sessão:** 02/10/2026
- **Diretriz de dados reais & Relatório de erros:** Relatório de inconsistências e descontinuação de artefatos

