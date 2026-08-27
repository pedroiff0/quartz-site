---
publish: false
title: Aula 11 — Órbitas de Satélites, a LMC e a Barra Galáctica
created: 2026-07-25
modified: 2026-08-27
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - dinamica-estelar
  - galpy
  - pratica
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula11
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: Aula prática (galpy) — pericentro/apocentro de galáxias satélites, comparação entre potenciais, a Grande Nuvem de Magalhães como perturbador em referencial não inercial, e ressonâncias orbitais na barra galáctica (corrotação e OLR)
professor: Hélio Dotto Perottoni
---

# 🪐 Aula 11 — Órbitas de Satélites, a LMC e a Barra Galáctica

> [!note] Resumo
> Continuação prática da Aula 10: como calcular pericentro/apocentro de uma galáxia satélite e comparar potenciais diferentes, como incluir a Grande Nuvem de Magalhães (LMC) como um perturbador massivo que também puxa a própria Via Láctea (exigindo um referencial não inercial), e como a barra galáctica introduz ressonâncias orbitais — corrotação e a Ressonância Externa de Lindblad (OLR) — que moldam a cinemática estelar local.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** notebook oficial da disciplina (Google Colab, biblioteca [galpy](https://docs.galpy.org/))

---

## 🎯 Visão geral

Esta aula segue direto da Aula 10, aprofundando três ideias: (1) como extrair pericentro e apocentro de uma órbita integrada, e como isso muda dependendo do potencial escolhido; (2) como simular corretamente o efeito da LMC — massiva o bastante para também mover a Via Láctea, exigindo um referencial não inercial; e (3) como a barra galáctica gera ressonâncias que capturam órbitas estelares em padrões específicos.

## 🛰️ Pericentro e apocentro de uma galáxia anã

O galpy conhece as órbitas de **50 galáxias satélites** da Via Láctea prontas via `Orbit.from_name('MW satellite galaxies')` (LMC, SMC, Sagittarius, Fornax, Draco, Sculptor, entre outras). Para uma órbita já integrada, o **apocentro** e o **pericentro** são simplesmente o máximo e o mínimo da distância galactocêntrica $r(t)$ ao longo do tempo — o notebook verifica isso explicitamente: encontrar o `argmax`/`argmin` de $r(t)$ dá o mesmo resultado que os métodos prontos `orbit.rap()` e `orbit.rperi()` do galpy. Usando `scipy.signal.argrelextrema`, é possível extrair **todos** os pericentros/apocentros sucessivos de uma órbita de longo prazo — úteis para checar se a órbita é razoavelmente periódica (os valores sucessivos de pericentro/apocentro do exemplo variam por menos de 1%, indicando uma órbita estável no potencial estático adotado).

> [!tip] O potencial escolhido muda a órbita reconstruída
> Integrar a mesma galáxia satélite (Bootes III, no exemplo) em `MWPotential2014` e em `McMillan17` produz trajetórias visivelmente diferentes no plano $Y$-$Z$ — um lembrete direto de que qualquer órbita reconstruída (incluindo pericentros/apocentros) é sempre condicional ao modelo de potencial galáctico assumido, nunca uma medida "livre de modelo".

## 🌌 A LMC como perturbador: referencial não inercial

A Grande Nuvem de Magalhães (LMC) tem massa suficiente ($\sim1{,}38\times10^{11}\,M_\odot$) para não apenas sofrer a gravidade da Via Láctea, mas também **puxar a própria Galáxia** de volta — o centro da Via Láctea não é, portanto, um referencial verdadeiramente inercial quando a LMC está por perto. Simular esse efeito corretamente exige três ingredientes combinados:

1. **Fricção dinâmica** (`ChandrasekharDynamicalFrictionForce`, já vista na Aula 10) — a LMC perde energia orbital ao interagir com o halo da Via Láctea.
2. **Um potencial "vivo"** (`MovingObjectPotential`, modelando a LMC como uma esfera de Hernquist) — a massa da LMC, na posição orbital correta a cada instante, soma-se ao potencial total.
3. **Uma força de referencial não inercial** (`NonInertialFrameForce`) — a aceleração que a própria Via Láctea sofre por causa da LMC (calculada a partir das forças que a LMC exerce na origem do sistema) precisa ser subtraída do movimento de qualquer outra órbita calculada nesse referencial, senão o resultado é fisicamente inconsistente.

O mesmo procedimento é repetido tanto para `MWPotential2014` quanto para `McMillan17`, reforçando que a escolha do potencial de base continua importando mesmo depois de incluída a LMC.

> [!warning] Múltiplas órbitas de uma vez, sem laço `for`
> O galpy aceita um array de condições iniciais (ex.: 100 amostras de incerteza gaussianas em torno de Bootes III) e integra todas simultaneamente — mas o notebook faz questão de avisar: nesse exemplo específico, as incertezas de movimento próprio foram amostradas **sem** covariância (diferente do procedimento cuidadoso da Aula 10). O objetivo ali é só ilustrar a mecânica de integrar um ensemble de órbitas de uma vez, não produzir uma incerteza estatisticamente correta.

## 〰️ A barra galáctica e suas ressonâncias

A Via Láctea tem uma **barra** no seu centro, modelada aqui com o `DehnenBarPotential` — um potencial parametrizado por velocidade angular de padrão ($\Omega_b$), comprimento, intensidade, e um período de "aquecimento" gradual ($t_{form}$, $t_{steady}$) para evitar choques numéricos ao ligar a barra.

Uma órbita simples, sem barra, é regular e previsível. A mesma órbita, com a barra ligada, deixa de ser regular no referencial inercial — mas revela estrutura ao ser vista no **referencial que gira junto com a barra** (subtraindo a rotação $\Omega_b t$ das coordenadas):

- **Barra longa e lenta** (parâmetros ao estilo Pérez-Villegas et al. 2017): uma órbita inicializada perto da **ressonância de corrotação** fica "capturada", librando em torno de um dos pontos de Lagrange da barra em vez de percorrer todos os ângulos — o tipo de ressonância cuja proximidade à vizinhança solar pode gerar subestrutura observável na cinemática local.
- **Barra curta e rápida** (ao estilo Dehnen 2000): a ressonância relevante mais próxima do Sol passa a ser a **OLR** (_Outer Lindblad Resonance_, Ressonância Externa de Lindblad). Órbitas próximas a essa ressonância mostram, no referencial da barra, uma morfologia característica **2:1** — a estrela entra e sai duas vezes do centro orbital a cada volta completa em torno da Galáxia, formando os padrões de órbita alinhados/anti-alinhados com o eixo maior da barra clássicos da dinâmica de barras.

> [!info] Por que isso importa para arqueologia galáctica
> Ressonâncias de barra (corrotação, OLR, e outras) são um dos mecanismos "seculares" (lentos, internos) capazes de gerar sobredensidades, lacunas de velocidade e outras assinaturas cinemáticas no disco — uma fonte de estrutura que **não** vem de fusões ou acréscimo externo, e que precisa ser distinguida de sinais genuinamente extragalácticos (como a Gaia-Sausage-Enceladus) ao interpretar dados de levantamentos como o Gaia.

---

## 📌 Conceitos-chave

- **Pericentro/apocentro:** mínimo/máximo de $r(t)$ ao longo de uma órbita integrada — dependem do potencial assumido, não são medidas livres de modelo.
- **Referencial não inercial:** necessário sempre que um perturbador (como a LMC) é massivo o bastante para também acelerar o corpo central do sistema de referência — implementado no galpy somando uma `NonInertialFrameForce` calculada a partir da força que o perturbador exerce na origem.
- **`DehnenBarPotential`:** modelo parametrizado de barra galáctica rotativa, com velocidade de padrão, comprimento e intensidade ajustáveis.
- **Corrotação vs. OLR:** duas ressonâncias de barra relevantes para a vizinhança solar, dependendo se a barra é longa/lenta ou curta/rápida — cada uma produz uma assinatura orbital característica (libração em torno de pontos de Lagrange vs. morfologia 2:1).
- **Estrutura secular vs. acretada:** ressonâncias de barra são um mecanismo interno de gerar subestrutura cinemática, distinto (mas potencialmente confundível) com assinaturas de fusões como a GSE.

## 🔗 Referências e correlatos

- Documentação do [galpy](https://docs.galpy.org/) — `DehnenBarPotential`, `NonInertialFrameForce`
- Pérez-Villegas et al. (2017) — modelo de barra longa e lenta, ressonância de corrotação
- Dehnen (2000) — modelo de barra curta e rápida, Ressonância Externa de Lindblad
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-10-integracao-de-orbitas-com-galpy|Aula 10 — Integração de Órbitas com galpy]] — pré-requisito direto: fricção dinâmica e potenciais "vivos" (`MovingObjectPotential`), aqui estendidos à LMC
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula03|Escola de Inverno — Arqueologia Galáctica, Aula 03]] — Gaia-Sausage-Enceladus como o tipo de assinatura extragaláctica que precisa ser distinguida de estrutura secular gerada pela barra
- [[pt-br/resource/curso-on/aula-12-espaco-de-acoes-apogee|Aula 12 — Espaço de Ações e Diagramas de Arqueologia Galáctica]] — as mesmas integrais de movimento aplicadas a mais de um milhão de estrelas reais (APOGEE DR19)
