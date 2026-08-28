---
publish: false
title: Computação Gráfica
created: 2026-07-26 13:04
modified: 2026-08-27 21:59
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] O que é este tópico
> Computação Gráfica é a disciplina que transforma descrições matemáticas de objetos — pontos, triângulos, texturas, luzes — em imagens 2D que aparecem numa tela. É onde Álgebra Linear (matrizes, vetores, transformações) deixa de ser exercício abstrato e vira a ferramenta que posiciona uma câmera, gira um objeto 3D ou projeta uma cena inteira num plano.

## Por que estudar isso?

Todo jogo, toda simulação, toda ferramenta de visualização científica passa pelo mesmo pipeline: representar objetos, transformá-los (mover, girar, escalar), projetá-los numa câmera e decidir quais pixels acendem com qual cor. Mesmo fora de jogos, os mesmos princípios aparecem sempre que dados viram gráfico — os sistemas de coordenadas e transformações que esta disciplina ensina são exatamente os que sustentam bibliotecas de plotagem científica (o tipo de gráfico que uso direto na minha pesquisa em astrofísica: projeções, diagramas de dispersão coloridos por parâmetro físico, mapas 2D de dados de alta dimensão).

É também a disciplina que constrói a base matemática (transformações, projeções, sistemas de coordenadas) necessária pra Processamento de Imagens, sua tranca direta na grade.

## Trilha de estudo

### 1. Dispositivos gráficos e o pipeline gráfico (2 semanas)

O que dominar: como imagens são apresentadas em monitores (varredura de pixels), espaços de cor (RGB para exibição, HSV para manipulação intuitiva de matiz/saturação/brilho), e uma visão geral do **pipeline gráfico**: a sequência de estágios que transforma vértices 3D em pixels coloridos na tela (transformação de vértices → rasterização → sombreamento de fragmentos → saída). O que praticar: identificar, num jogo ou render qualquer, em que estágio do pipeline aconteceria cada efeito visual que você observa (iluminação, textura, sombra).

![O pipeline de renderização do Direct3D 11: cada estágio processa a geometria e produz a entrada do próximo, do vértice bruto ao pixel final na tela.](https://commons.wikimedia.org/wiki/Special:FilePath/Direct3D_11_Render_Pipeline.svg)

### 2. Primitivas gráficas e modelagem geométrica (2–3 semanas)

O que dominar: como primitivas simples (ponto, reta, circunferência, polígono) são rasterizadas — o algoritmo de Bresenham para retas é o exemplo clássico de "como desenhar uma linha reta usando só aritmética inteira"; e como objetos mais complexos são modelados via triangulação de polígonos, vetores normais (essenciais pra iluminação) e operações de conjuntos (união, interseção, diferença entre sólidos — CSG). O que praticar: triangular manualmente um polígono não convexo simples e calcular o vetor normal de cada triângulo resultante.

### 3. Sistemas de coordenadas e transformações 2D/3D (2–3 semanas)

O que dominar: coordenadas homogêneas (adicionar uma dimensão extra pra representar translação como multiplicação de matriz, não soma), as matrizes de escala, translação e rotação, e como compor várias transformações numa única matriz; a cadeia de sistemas de coordenadas que todo objeto atravessa — espaço do objeto → espaço do mundo → espaço da câmera → espaço da tela. O que praticar: compor manualmente a matriz de "rotacionar 90° e depois transladar" e verificar que a ordem das multiplicações importa (transformações não comutam).

### 4. Algoritmos de projeção, recorte e visibilidade (3 semanas)

O que dominar: projeção paralela vs. projeção em perspectiva (a diferença entre "sem distorção de distância" e "objetos distantes parecem menores", como o olho humano vê); o algoritmo de **Z-buffer** para decidir qual objeto está na frente quando vários se sobrepõem; uma visão geral de **ray tracing** (traçar raios de luz da câmera até os objetos, ao invés de rasterizar triângulos) — mais realista, mais caro computacionalmente, e por isso historicamente reservado a renderização offline (cinema) até GPUs recentes viabilizarem ray tracing em tempo real. O que praticar: para uma cena com dois objetos sobrepostos, simular manualmente o teste de Z-buffer pixel a pixel.

### 5. Iluminação e shading (2 semanas)

O que dominar: o modelo de iluminação de Phong (componentes ambiente, difusa e especular — a soma que faz uma esfera 3D parecer ter volume e brilho), mapeamento de textura (colar uma imagem 2D sobre uma superfície 3D), e uma introdução a sombras e reflexão. O que praticar: para uma esfera iluminada por uma única fonte de luz, esboçar como cada componente do modelo de Phong contribui separadamente para o resultado final.

## Conceitos que você precisa dominar

- **Pipeline gráfico** — a sequência de estágios (vértice → geometria → rasterização → fragmento/pixel) que todo sistema de renderização moderno segue, seja em uma GPU de jogo ou em uma biblioteca de plotagem científica.
- **Coordenadas homogêneas** — o truque matemático (adicionar uma quarta coordenada `w`) que permite representar translação, rotação e escala com a mesma operação (multiplicação de matriz), o que torna possível compor várias transformações numa única matriz.
- **Matriz de transformação** — cada transformação geométrica (escala, rotação, translação) é uma matriz; aplicar várias transformações em sequência é multiplicar as matrizes, na ordem certa (a ordem importa: rotação seguida de translação ≠ translação seguida de rotação).
- **Z-buffer** — uma "segunda imagem", do mesmo tamanho da tela, que guarda a profundidade de cada pixel; ao desenhar um novo objeto, só se atualiza o pixel se o novo objeto estiver mais perto da câmera do que o que já estava lá.
- **Rasterização vs. ray tracing** — rasterização projeta triângulos na tela e testa quais pixels cada um cobre (rápido, é o que jogos em tempo real usam); ray tracing traça o caminho da luz de trás para frente, da câmera até a cena (mais fisicamente realista, tradicionalmente mais caro).
- **Modelo de iluminação de Phong** — decompõe a luz que chega ao olho em três componentes somadas: ambiente (luz difusa constante, simula iluminação indireta), difusa (depende do ângulo entre luz e superfície) e especular (o brilho concentrado, depende também do ângulo de visão).

## Erros comuns de quem está começando

- **Confundir espaço do objeto, do mundo e da câmera** — aplicar uma transformação no espaço errado é a causa mais comum de "meu objeto girou em torno do ponto errado" ou "minha câmera não olha pra onde eu esperava".
- **Esquecer de normalizar coordenadas homogêneas** — depois de certas transformações (como projeção em perspectiva), é preciso dividir todas as coordenadas por `w`; esquecer esse passo produz resultados visualmente distorcidos e difíceis de depurar.
- **Achar que ray tracing é sempre "melhor" que rasterização** — ray tracing é mais caro computacionalmente; a escolha entre as duas técnicas é uma decisão de engenharia (tempo real vs. qualidade), não uma hierarquia de "melhor e pior".
- **Ignorar aliasing (serrilhado)** — rasterizar bordas diagonais sem qualquer técnica de anti-aliasing produz o efeito clássico de "escada" nas bordas; é um problema de amostragem, não um bug.

## 📚 Materiais recomendados

### Cursos e tutoriais gratuitos

- **[Scratchapixel](https://www.scratchapixel.com/)** — tutorial gratuito e extremamente detalhado, cobrindo desde transformações e projeções até ray tracing do zero, com o rigor matemático completo por trás de cada técnica.
- **[LearnOpenGL](https://learnopengl.com/)** — tutorial prático e gratuito de OpenGL moderno; ótimo para ver o pipeline gráfico desta trilha implementado em código real.
- **[CS184 — UC Berkeley (Foundations of Computer Graphics)](https://cs184.eecs.berkeley.edu/)** — curso universitário com slides e material aberto, cobrindo a disciplina inteira em profundidade acadêmica.

### Bibliografia clássica (consultar na biblioteca)

- AZEVEDO, E., CONCI, A., VASCONCELOS, C. _Computação Gráfica: Teoria e Prática_ — a referência-base da própria ementa da disciplina, em português.

## 🔗 Referências externas

- [The Book of Shaders](https://thebookofshaders.com/) — introdução gratuita e visual a shaders (o código que roda por pixel na GPU), útil pra quem quer ver iluminação e cor "ao vivo" enquanto edita o código.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/eletivas/computacao-grafica|Computação Gráfica]] — a eletiva que cobre exatamente esta trilha; tem como pré-requisitos Álgebra Linear e Geometria Analítica II e Algoritmos e Estruturas de Dados II.
- [[pt-br/resource/computacao/processamento-de-imagens|Processamento de Imagens]] — a tranca direta: uma vez que uma imagem é gerada (ou capturada), processá-la usa as mesmas noções de matriz, pixel e espaço de cor apresentadas aqui.
