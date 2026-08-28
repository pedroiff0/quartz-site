---
publish: false
title: Machine Learning
created: 2026-07-18 13:04
modified: 2026-08-27 13:04
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] Machine learning é a área que constrói programas que aprendem padrões a partir de dados, em vez de seguir regras escritas à mão. É a tecnologia por trás de recomendações, detecção de fraude, diagnóstico por imagem — e da pesquisa em detecção de anomalias que desenvolvo neste site.

## Por que estudar isso?

Pegue um problema concreto: detectar fraude em cartão de crédito. Escrever regras à mão ("bloqueie compras acima de X em país diferente") é uma corrida perdida — fraudadores se adaptam mais rápido do que analistas escrevem regras. A abordagem de ML inverte o jogo: alimente um modelo com milhões de transações rotuladas e deixe-o aprender os padrões, inclusive combinações sutis que nenhum humano formularia. O mesmo princípio vale para diagnóstico médico, previsão de demanda, tradução automática — e é por isso que ML saiu do laboratório para virar infraestrutura básica da indústria.

Aqui tem também uma conexão direta com a pesquisa deste site: trabalho com [[pt-br/research/anomaly-detection|detecção de anomalias em dados astronômicos]] — ensinar modelos a encontrar, em milhões de observações do céu, os objetos que fogem do padrão e podem ser fenômenos novos. É um exemplo honesto do que ML faz de melhor: vasculhar volumes de dados impossíveis para humanos atrás do que interessa. Se o tema te atrai, a página de pesquisa mostra o caminho na prática.

## Trilha de estudo

### 1. Base matemática e Python científico (iniciante)

Não dá para pular: álgebra linear (vetores, matrizes), estatística e probabilidade (distribuições, média/variância, teorema de Bayes) e noções de cálculo (derivada como taxa de variação — o gradiente vem daí). Em paralelo, o stack Python: NumPy, pandas e matplotlib. Pratique explorando datasets do [Kaggle](https://www.kaggle.com/) só com pandas, sem modelo nenhum ainda. Tempo típico: 6 a 8 semanas.

### 2. Aprendizado supervisionado clássico (intermediário)

O núcleo: regressão linear e logística, árvores de decisão, florestas aleatórias, k-vizinhos. Mais importante que os algoritmos, a metodologia — divisão treino/validação/teste, validação cruzada, métricas (e por que acurácia engana em dados desbalanceados). O [scikit-learn](https://scikit-learn.org/) é a ferramenta; o guia oficial dele é um curso disfarçado. Tempo típico: 8 a 10 semanas.

### 3. Não supervisionado e engenharia de atributos (intermediário-avançado)

Clustering (k-means, DBSCAN), redução de dimensionalidade (PCA) e detecção de anomalias — aprender estrutura sem rótulos. Junto, a habilidade que mais separa iniciantes de praticantes: engenharia de atributos, limpeza e preparação de dados, que consomem 80% do tempo de qualquer projeto real. Pratique em competições encerradas do Kaggle, estudando as soluções vencedoras depois. Tempo típico: 6 a 8 semanas.

> [!example] Caso real: t-SNE em meio milhão de espectros estelares
> Em [[pt-br/research/anomaly-detection/articles/traven2019|Traven et al. (2019)]], os autores tentam primeiro reduzir a dimensionalidade de ~587 mil espectros do levantamento GALAH com um autoencoder — o mapa 2D resultante não separa as classes de forma útil. Trocam para t-SNE, e o mapa revela, sem nenhum rótulo prévio, aglomerados que correspondem a estrelas binárias, gigantes pobres em metais e estrelas quentes de rotação rápida; o algoritmo DBSCAN então isola cada grupo automaticamente. É clustering e redução de dimensionalidade — os temas desta etapa — resolvendo um problema real de descoberta em astronomia, e ilustra também por que a escolha do algoritmo importa: nem toda técnica de redução de dimensionalidade produz um mapa útil para o mesmo dado.

### 4. Redes neurais e especialização (avançado)

Do perceptron ao deep learning: backpropagation, redes convolucionais (imagens), arquiteturas para sequências e a família dos transformers. A partir daqui, escolha uma especialização — visão computacional, NLP, dados científicos — e acompanhe a literatura no [arXiv](https://arxiv.org/). Tempo típico: 10+ semanas, e a rigor não termina nunca.

## Conceitos que você precisa dominar

- **Supervisionado vs. não supervisionado** — no supervisionado, cada exemplo tem a resposta certa (rótulo) e o modelo aprende a mapeá-la; no não supervisionado, não há rótulos e o objetivo é descobrir estrutura (grupos, padrões, anomalias). A distinção define que problema você pode atacar e quanto vai custar montar o dataset — rotular dados é caro.
- **Discriminativo vs. generativo** — dentro do supervisionado, dois estilos de resolver o mesmo problema. Um modelo discriminativo (regressão logística, SVM, florestas aleatórias) aprende a mapear dado→rótulo direto, é rápido e é o padrão para classificação. Um modelo generativo (GANs, autoencoders variacionais, ou modelos espectrais como The Cannon e The Payne usados em astronomia) aprende a produzir dado a partir do rótulo — custa mais caro treinar, mas permite comparar um dado observado contra o que o modelo prevê, o que é útil quando gerar a explicação é parte do que você quer entender ([[pt-br/research/anomaly-detection/articles/traven2019|exemplo em espectroscopia estelar]]).
- **Overfitting e generalização** — o pecado capital do ML: o modelo decora o conjunto de treino (ruído incluído) e fracassa em dados novos. Todo o arsenal metodológico — validação cruzada, regularização, conjunto de teste intocado — existe para detectar e combater isso. Um modelo com 99% no treino e 60% no teste não aprendeu: decorou.
- **Viés e variância** — os dois modos de errar: modelo simples demais para o padrão (viés alto, subajuste) ou sensível demais às particularidades do treino (variância alta, sobreajuste). Diagnosticar de que lado está o erro é o que orienta a próxima ação: mais dados? modelo mais complexo? mais regularização?
- **Divisão treino/validação/teste** — treino ajusta parâmetros, validação escolhe hiperparâmetros, teste dá a estimativa final honesta — e só pode ser usado uma vez. Toda decisão tomada olhando o teste vaza informação e infla o resultado; é o erro metodológico mais comum em trabalhos de iniciantes (e em papers ruins).
- **Métricas além da acurácia** — em fraude, com 99,9% de transações legítimas, o modelo que responde "legítima" para tudo tem 99,9% de acurácia e é inútil. Precisão, revocação, F1 e a matriz de confusão capturam os erros que importam; escolher a métrica certa é decisão de negócio, não detalhe técnico.
- **Gradiente descendente** — o motor de treinamento de quase tudo: medir o erro, calcular em que direção cada parâmetro deve mudar para reduzi-lo (o gradiente) e dar um passo pequeno nessa direção, milhões de vezes. Entendido isso, redes neurais deixam de ser mágica: backpropagation é só a forma eficiente de calcular esse gradiente.
- **Engenharia de atributos** — transformar dados brutos em representações que o modelo consegue explorar: extrair dia da semana de uma data, razões entre colunas, estatísticas de janelas de tempo. Na prática clássica, atributos bons com modelo simples ganham de atributos ruins com modelo sofisticado — quase sempre.
- **Detecção de anomalias** — encontrar o que foge do padrão quando exemplos do "anormal" são raros ou inexistentes: fraude, falha de equipamento, objeto astronômico atípico. Técnicas como Isolation Forest e autoencoders aprendem o normal e sinalizam o resto — é a família de métodos da [[pt-br/research/anomaly-detection|minha pesquisa]].

## Erros comuns de quem está começando

- **Pular a matemática e ir direto para os tutoriais.** Sem estatística e álgebra linear, você opera ferramentas sem entender saídas — e a primeira vez que o modelo se comportar de forma estranha (sempre acontece), não terá como diagnosticar.
- **Avaliar o modelo nos mesmos dados do treino.** O erro metodológico número um: produz números maravilhosos e modelos inúteis. Separe o conjunto de teste no primeiro dia e finja que ele não existe até o fim.
- **Vazamento de dados (data leakage).** Deixar escapar para o treino informação que não existiria no momento da previsão — normalizar antes de dividir os dados, incluir uma coluna derivada do rótulo. O sintoma é resultado bom demais; a lição é desconfiar sempre de resultados bons demais.
- **Começar por deep learning.** Redes neurais brilham em imagem, áudio e texto com dados abundantes; em dados tabulares pequenos — a maioria dos problemas reais — modelos clássicos empatam ou ganham, custando uma fração. Domine o clássico primeiro: é também o que dá a base conceitual.
- **Gastar 90% do tempo no modelo e 10% nos dados.** A proporção real do trabalho é inversa. Entender, limpar e representar bem os dados rende mais que qualquer troca de algoritmo — quem ignora isso otimiza hiperparâmetros de um modelo alimentado com lixo.

## 📚 Materiais recomendados

Não há livro aberto em português no acervo local para este tópico — a boa notícia é que os melhores materiais da área são gratuitos e estão listados abaixo. O guia oficial do [scikit-learn](https://scikit-learn.org/) funciona, na prática, como um livro-texto de ML clássico com código executável.

> [!tip] Complemento local: a página de [[pt-br/research/anomaly-detection|pesquisa em detecção de anomalias]] traz artigos e sínteses em português sobre a aplicação de ML a dados astronômicos — material real de pesquisa para quem quer ver a teoria em uso. O artigo [[pt-br/research/anomaly-detection/articles/traven2019|Traven et al. (2019)]], citado nos exemplos acima, é um bom ponto de partida: revisa a taxonomia de ML (supervisionado/não supervisionado, discriminativo/generativo) e aplica t-SNE, DBSCAN e modelos generativos à detecção de estrelas binárias.

## 🔗 Referências externas

- [Roadmap: Machine Learning](https://roadmap.sh/machine-learning) — a trilha estruturada da área: matemática, algoritmos, ferramentas e MLOps. Use como espinha dorsal do autoestudo.
- [Roadmap: AI and Data Scientist](https://roadmap.sh/ai-data-scientist) — a variante orientada a ciência de dados, com mais ênfase em estatística e análise. Compare os dois e escolha o perfil que combina com você.
- [scikit-learn](https://scikit-learn.org/) — a biblioteca padrão de ML clássico em Python. O guia do usuário explica a teoria de cada algoritmo junto com o código — estude por ele, não só consulte.
- [Kaggle](https://www.kaggle.com/) — datasets, competições e notebooks públicos. O modo certo de usar: refazer notebooks bem votados linha a linha, depois competir em desafios encerrados e estudar as soluções vencedoras.
- [Coursera](https://www.coursera.org/) — os cursos clássicos de ML (o do Andrew Ng é o ponto de partida canônico da área) podem ser auditados gratuitamente.
- [arXiv](https://arxiv.org/) — o repositório de preprints onde a pesquisa em ML acontece de fato. Relevante a partir da etapa 4, quando você escolher uma especialização e quiser acompanhar o estado da arte.
- [Astronomy 162 Podcast](https://www.astronomy.ohio-state.edu/~pogge/Ast162/Audio/) (Richard Pogge, Ohio State University) — série de aulas em áudio sobre astronomia introdutória; não é sobre ML, mas cobre a base observacional (classificação espectral, evolução estelar, populações estelares) por trás dos exemplos astronômicos usados nesta página.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/eletivas/inteligencia-artificial|Inteligência Artificial]] — a eletiva que cobre os fundamentos de IA e aprendizado de máquina dentro da grade.
- [[pt-br/research/anomaly-detection|Pesquisa: Detecção de Anomalias]] — a aplicação real: ML para encontrar objetos atípicos em levantamentos astronômicos, com os artigos e métodos que uso na pesquisa.
