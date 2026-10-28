---
publish: true
title: Painel interativo de Detecção de Anomalias (Anomaly Viewer)
created: 2026-10-28T08:20:00-03:00
modified: 2026-10-28T08:23:42-03:00
published: 2026-10-28T08:20:00-03:00
tags:
  - projeto
  - streamlit
  - galah-dr4
  - espectroscopia
status: no ar, temporário
cssclasses:
  - page-layout
icon: lucide-layout-dashboard
sitesync: true
resource-sync: false
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>Projetos Públicos</span> <span class="academic-nav-sep">/</span> <span>Anomaly Viewer</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Painel interativo de Detecção de Anomalias (Anomaly Viewer)</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">← Início</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">Hub</span> <span class="academic-nav-counter">(1 de 1)</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">Fim →</span>

</div>

</div>

</div>

# Painel interativo de Detecção de Anomalias (Anomaly Viewer)

> [!abstract] Resumo
> Um painel na web para explorar os mapas de espectros de estrelas da pesquisa [[pt-br/research/deteccao-de-anomalias-iff-2025/index|Detecção de Anomalias Espectrais em Estrelas (GALAH DR4)]]. É um aplicativo em Python (Streamlit) que roda num servidor meu, em [anomaly.phrandrade.com](https://anomaly.phrandrade.com), e foi feito para o SAB 2026: quem vê o banner pode abrir o QR code e mexer nos mesmos mapas.

> [!warning] Painel temporário
> O painel é temporário e será desativado depois do SAB 2026. Para mais informações, entre em contato: [pedroiff0@gmail.com](mailto:pedroiff0@gmail.com).

## O que dá para fazer no painel

O painel tem três páginas, em português e em inglês (seletor de idioma no topo, que começa pelo idioma do navegador), com tema claro, escuro ou OLED e layout que se ajusta ao celular.

- **Visão geral:** o contexto rápido do trabalho, os resultados principais do SAB 2025 e do SAB 2026, as referências com link para cada artigo (arXiv, NASA ADS, IOPscience) e o banner em PDF para ver e baixar.
- **SAB 2025, análises básicas:** as figuras do pôster de 2025 refeitas de forma interativa, com zoom e dica ao passar o mouse: histogramas de metais, magnésio e idade, o diagrama de Kiel com isócronas, o diagrama de Toomre e a separação entre disco fino e espesso.
- **Amostra e projeções:** a amostra de 6.198 estrelas perto do Sol e os mapas t-SNE e UMAP feitos com o espectro, que dá para colorir por temperatura, gravidade e metais, ver os avisos do GALAH, comparar lado a lado e abrir os dados de uma estrela.

## Por trás do painel: a parte de computação

O painel é a ponta visível de um projeto de engenharia de dados e de software. A pesquisa pede que centenas de milhares de espectros (cada um com cerca de 14 mil pontos) virem um mapa que uma pessoa consiga explorar no navegador, sem travar a máquina nem o celular de quem olha. As decisões principais:

- **Pilha:** Python 3.11, Streamlit para a interface, Plotly para os gráficos (com WebGL, para desenhar milhares de pontos sem engasgar), pandas e NumPy para os dados, Astropy para ler os arquivos FITS dos espectros, e scikit-learn, UMAP, HDBSCAN e openTSNE para os mapas. O ambiente é gerenciado com o uv.
- **Um app, várias páginas:** a navegação é uma só (`st.navigation`) e cada página é um arquivo separado. Antes eram seis aplicativos independentes, cada um num processo, porque um único processo chegou a usar 17 GiB de memória e travou a máquina.
- **Memória sob controle:** a matriz de espectros (cerca de 1 GB) fica num cache compartilhado, sem cópia a cada clique, e é carregada só quando uma página pede. Se a memória livre ficar abaixo de 1,5 GB, o painel recusa carregar em vez de derrubar o servidor.
- **Versão pública somente leitura:** a instância pública não tem botão de GPU nem edição, e só lê dados já preparados. O que usa o GALAH inteiro existe, mas é de uso interno.
- **Tradução e tema:** todos os textos ficam num dicionário português e inglês, e o tema acompanha a escolha do navegador, com ajuste para telas pequenas (colunas empilham abaixo de 768 px).
- **No ar:** um serviço do systemd de usuário, que sobe com a máquina e reinicia se cair, escutando só no endereço local. O acesso de fora passa por um túnel da Cloudflare, então o servidor não abre nenhuma porta para a internet.
- **Verificação:** as páginas são verificadas sem navegador com o AppTest do Streamlit, nos dois idiomas, e o repositório valida a sintaxe dos módulos a cada envio por uma checagem automática no GitHub.

## O pipeline que alimenta o painel

Os mapas do painel vêm de um programa de processamento separado, pensado para rodar em lotes, sem supervisão e sem risco para os dados originais. Ele tem cinco etapas: escolher os espectros, extrair cada um para uma matriz, achar os vizinhos mais próximos de cada estrela, desenhar os mapas e empacotar o resultado.

- **Vizinhos sem PCA:** o programa calcula os vizinhos exatos pela similaridade de cosseno direto nos pixels, em blocos, sem nunca carregar tudo na memória. Para o GALAH DR4 inteiro são 905.415 espectros e uma matriz de cerca de 54 GB.
- **Segurança de execução:** teto de memória configurável (12 GB por padrão), parada automática se a memória livre cair demais, retomada de onde parou e nenhuma alteração nos arquivos de origem.
- **Tempos medidos (GPU GTX 1660):** as 5 mil anãs M da amostra local levam cerca de 25 segundos com todas as projeções, e as 21.817 anãs M do GALAH levam cerca de 2,8 minutos.
- **Estimativa para o GALAH inteiro:** cerca de 2,4 x 10^16 operações só para os vizinhos, algo como 4,5 horas numa placa GTX 1660 e perto de 40 minutos numa A100. É uma estimativa, e o gargalo real é ler os 54 GB do disco várias vezes. Ainda não foi executado.

## Limites e próximos passos

- O painel público mostra a amostra perto do Sol, com 6.198 estrelas. O mapa do GALAH completo ainda é interno.
- Os grupos de estrelas que aparecem nos mapas são candidatos, não classes definitivas, e isso vale para o que o painel mostra.
- Depois do SAB 2026 o painel sai do ar. O que fica é o código, o banner e as notas da pesquisa.

## Referências e correlatos

- [[pt-br/research/deteccao-de-anomalias-iff-2025/index|Detecção de Anomalias Espectrais em Estrelas (GALAH DR4)]]: a pesquisa por trás do painel
- [[pt-br/media/2026/sab/index|XLIX RASAB (2026)]]: o evento em que o painel foi apresentado
- SpectraViewer: outro visualizador de espectros do GALAH DR4
- Origem: Site Público
