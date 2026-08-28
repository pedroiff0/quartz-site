---
publish: false
title: Aula 21 — Funções de Distribuição de Metalicidade em Galáxias Satélites
created: 2026-07-25 12:36
modified: 2026-08-27 12:36
published: 2026-07-26T11:33:09.987-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - evolucao-quimica
  - galaxias-anas
  - mdf
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula21
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: O Grupo Local como laboratório de evolução química, a função de distribuição de metalicidade (MDF) como registro fóssil de formação estelar e acréscimo, modelos químicos com infall/outflow, e as dificuldades práticas (número de objetos, completeza, fotometria vs. espectroscopia) de medir uma MDF
professor: Hélio Dotto Perottoni
---

# 📊 Aula 21 — Funções de Distribuição de Metalicidade em Galáxias Satélites

> [!note] Resumo
> A função de distribuição de metalicidade (MDF) de uma galáxia — quantas estrelas existem em cada faixa de $[\text{Fe/H}]$ — é um registro fóssil comprimido de toda a sua história de formação estelar, enriquecimento químico e acréscimo. Esta aula usa as galáxias satélites do Grupo Local como laboratório para entender o que molda uma MDF, como modelá-la com equações simples de evolução química, e por que medi-la na prática é mais difícil do que parece.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** slides oficiais da disciplina — "Funções de distribuição de metalicidade"

---

## 🌌 O Grupo Local como laboratório

O **Grupo Local** é dominado por duas espirais massivas — a Via Láctea e Andrômeda (M31) — cada uma acompanhada por dezenas de galáxias satélites de baixa massa, cobrindo quase **seis ordens de grandeza em massa estelar**: de $\sim3\times10^9\,M_\odot$ até sistemas com apenas alguns milhares de massas solares. Essa amplitude enorme de massas, todas observáveis em detalhe por estarem próximas, torna o Grupo Local um laboratório natural para estudar como a formação de galáxias muda com o ambiente e a escala.

## 🧬 O que a forma de uma MDF revela

A **MDF** (_Metallicity Distribution Function_) é definida como a distribuição de frequência das metalicidades estelares de uma galáxia — e sua forma codifica os efeitos cumulativos de vários processos físicos:

- **História de formação estelar:** quão rapidamente a galáxia converteu gás em estrelas.
- **Enriquecimento químico:** com que eficiência as estrelas enriqueceram o meio.
- **Mergers e acréscimos:** **múltiplos picos** na MDF indicam estrelas originárias de populações distintas.
- **Montagem da galáxia (_assembly_):** se múltiplas populações estelares foram acretadas via fusões.

Ou seja: uma MDF bem medida é, em si, um registro comprimido da história completa de uma galáxia — o mesmo espírito por trás de usar o espaço $(E,L_z)$ para achar acréscimos (curso-on Aula 12), mas aplicado à distribuição de metalicidade como um todo, não a estrelas individuais.

## ⚖️ Modelando a MDF: equações de evolução química

Modelos de evolução química preveem a forma esperada de uma MDF a partir de um balanço entre gás que entra, é convertido em estrelas, e é devolvido/perdido:

$\frac{d(\text{gás})}{dt} = \underbrace{\frac{dM_h}{dt}}_{\text{infall}} - \underbrace{(1-R)\,\psi(t)}_{\text{consumo líquido}} - \underbrace{\eta\,\psi(t)}_{\text{ventos}}$

onde $dM_h/dt$ é a taxa de acréscimo (_infall_) de gás, $\psi(t)$ é a taxa de formação estelar (SFR), $\eta$ é o **fator de carregamento** (_mass loading factor_) dos ventos galácticos — quanto gás é ejetado por unidade de massa estelar formada — e $(1-R)$ é o fator de aprisionamento (a fração da massa formada que não retorna ao meio interestelar via perda estelar). Variando esses ingredientes — taxa de infall, eficiência de formação estelar, intensidade dos ventos — os modelos reproduzem formas de MDF bem diferentes, permitindo inferir a história de uma galáxia a partir da MDF observada (o problema inverso).

> [!info] O "problema central" das galáxias anãs
> Reproduzir simultaneamente a MDF observada, a história de formação estelar e a massa total de galáxias anãs com modelos simples de evolução química é uma dificuldade recorrente e bem documentada na literatura — os modelos mais simples (caixa fechada, _closed box_) sistematicamente falham em reproduzir a MDF real sem a inclusão de infall e ventos, cujos parâmetros exatos seguem sendo ativamente ajustados/debatidos.

## ⚠️ Por que medir uma MDF é difícil na prática

- **Número de objetos:** galáxias anãs têm, por definição, poucas estrelas observáveis — amostras de algumas centenas a poucos milhares de estrelas (ex.: Fornax, com contagens de ~1.100 a ~12.700 estrelas dependendo do estudo/critério) tornam a forma da MDF estatisticamente incerta, especialmente nas caudas de metalicidade extrema.
- **Completeza e efeitos de seleção:** quais estrelas entram na amostra (critérios de magnitude, cor, qualidade espectral) afeta diretamente a forma da MDF reconstruída — o mesmo tipo de viés já discutido para catálogos fotométricos em geral (curso-on Aula 15).
- **Fotometria vs. espectroscopia:** MDFs derivadas de metalicidade fotométrica (mais barata, mas menos precisa) e de metalicidade espectroscópica (mais cara, mais precisa) para as mesmas galáxias podem divergir por **0,3-0,4 dex** — uma diferença grande o bastante para mudar substancialmente a interpretação de história química, especialmente perto de picos ou "joelhos" na distribuição.

> [!warning] Uma MDF "errada" conta uma história errada
> Como a forma da MDF é o próprio dado usado para inferir infall, SFR e ventos, qualquer viés de completeza ou discrepância fotometria-espectroscopia não amostrado corretamente se propaga diretamente para conclusões sobre a história de formação da galáxia — reforçando por que a validação cuidadosa da amostra (curso-on Aula 15) é inseparável da própria ciência de evolução química.

---

## 📌 Conceitos-chave

- **MDF (função de distribuição de metalicidade):** a distribuição de $[\text{Fe/H}]$ de uma galáxia — um registro fóssil comprimido de formação estelar, enriquecimento e acréscimo.
- **Múltiplos picos na MDF:** assinatura direta de populações estelares de origens distintas (possível evidência de merger/acréscimo).
- **Modelo com infall + ventos:** $d(\text{gás})/dt = dM_h/dt - (1-R)\psi(t) - \eta\,\psi(t)$ — os ingredientes mínimos para reproduzir MDFs realistas (o modelo de caixa fechada simples não basta).
- **Problema central das galáxias anãs:** dificuldade recorrente em ajustar simultaneamente MDF, SFH e massa total com modelos de evolução química.
- **Discrepância fotometria-espectroscopia (~0,3-0,4 dex):** lembrete de que a MDF observada depende fortemente do método usado para medir metalicidade, não só da física da galáxia.

## 🔗 Referências e correlatos

- Kirby (2013) — MDFs de galáxias anãs via espectroscopia
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-13-nucleossintese-e-enriquecimento-quimico|Aula 13 — Nucleossíntese Estelar e Enriquecimento Químico]] — a origem física dos elementos cuja distribuição a MDF resume estatisticamente
- [[pt-br/resource/curso-on/aula-15-levantamentos-fotometricos-e-espectroscopicos|Aula 15 — Espectroscopia e Fotometria em Grandes Levantamentos]] — completeza e efeitos de seleção, aqui aplicados diretamente ao problema da MDF
- [[pt-br/resource/curso-on/aula-17-gradientes-de-metalicidade-e-amr|Aula 17 — Gradientes de Metalicidade e a Relação Idade-Metalicidade]] — a mesma lógica de evolução química (infall, enriquecimento) aplicada à Via Láctea em vez de galáxias anãs satélites
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula01|Escola de Inverno — Arqueologia Galáctica, Aula 01]] — populações I/II/III como o caso extremo de uma MDF dominada por um único evento de enriquecimento primordial
- [[pt-br/resource/curso-on/aula-22-galaxias-anas-ultrafracas|Aula 22 — Galáxias Anãs Ultrafracas e os Limites da Formação Galáctica]] — aula de encerramento do curso: o mesmo problema de MDF levado ao regime mais extremo de massa estelar
