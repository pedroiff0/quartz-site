---
publish: false
title: Aula 05 — Avermelhamento, Extinção e IMF
created: 2026-07-23 12:36
modified: 2026-08-27 12:36
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - meio-interestelar
  - extincao-interestelar
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula05
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: O meio interestelar, a extinção e o avermelhamento da luz por poeira, e a função de massa inicial revisitada
professor: Hélio Dotto Perottoni
---

# 🌫️ Aula 05 — Avermelhamento, Extinção e IMF

> [!note] Resumo
> Antes de qualquer estimativa de distância na Galáxia ser confiável, é preciso corrigir a luz estelar do efeito do meio interestelar: gás e poeira absorvem e espalham fótons de forma dependente do comprimento de onda, atenuando (extinção) e avermelhando a luz observada.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni

---

## ☁️ O meio interestelar (ISM)

Gás e poeira ocupam o espaço entre as estrelas: **~99%** da massa do ISM está em forma de gás (HI neutro, HII ionizado, H₂ molecular), e **~1%** em poeira. Da massa de gás, cerca de 70% é hidrogênio, 29% hélio e 1% metais. A distribuição do ISM **não é homogênea** ao longo do disco galáctico.

A massa total de gás + poeira representa apenas 10–20% da massa em estrelas da Galáxia. Estimativas de ordem de grandeza para a Via Láctea: massa total $1$–$1{,}5\times10^{12}\,M_\odot$; massa estelar $\sim5\times10^{10}\,M_\odot$; massa em gás $\sim1\times10^{10}\,M_\odot$ — o restante é matéria escura, cuja distribuição não é diretamente observável (ver [[pt-br/research/dark-matter-shocks|Entendendo a Matéria Escura a partir de Choques Extragalácticos]] para um método alternativo de mapeá-la).

### Poeira interestelar

Grãos com núcleo de ferro, silicatos e grafite, envoltos por materiais congelados (CO₂/H₂O/NH₂) \[Jessberger et al. 2001]. Comparação de escalas: átomos $\sim0{,}1\,$nm, moléculas pequenas $\sim1\,$nm, grãos de poeira $\sim100\,$nm. Sua distribuição é bastante **filamentar** — variações substanciais ocorrem em regiões separadas por poucos minutos de arco \[mapa 3D Argonaut].

### Formas do gás interestelar

- **HII (regiões de hidrogênio ionizado):** visíveis apenas perto de estrelas quentes, cuja luz UV ioniza o gás — pequena fração do gás total.
- **Nuvens de hidrogênio neutro (HI):** não emitem no visível; observadas por absorção de luz estelar atrás delas, ou pela emissão de rádio em **21 cm** do H frio.
- **Gás ultraquente:** temperaturas de milhões de graus, proveniente de explosões de supernova.
- **Nuvens moleculares:** moléculas complexas podem sobreviver quando protegidas da luz UV; berçários de formação estelar.

A poeira não emite no visível, mas **bloqueia** a luz — nebulosas de reflexão são regiões onde a poeira espalha luz estelar, tornando-se visível principalmente em comprimentos de onda azuis.

## 📉 A descoberta observacional do meio interestelar

**Hartmann (1904)** observou o sistema binário **δ Orionis** e notou que, embora a maioria das linhas espectrais se deslocasse de forma consistente com o movimento orbital (variação de velocidade radial esperada para um binário), a linha K do Cálcio **não** compartilhava essa variação. A conclusão correta: havia uma nuvem de gás contendo cálcio estacionária na linha de visada, entre nós e o sistema binário — a primeira evidência direta de matéria difusa no espaço interestelar.

## 🌒 Extinção interestelar

**Trumpler (1930)** obteve evidência da existência de absorção interestelar comparando distâncias de aglomerados abertos calculadas por dois métodos independentes: brilho das estrelas vs. diâmetro angular do aglomerado — a discrepância sistemática revelou que a luz estava sendo atenuada por poeira ao longo do caminho. Trumpler mostrou que a extinção segue aproximadamente uma lei $\propto\lambda^{-1}$: se os grãos fossem muito maiores que $\lambda$, a extinção seria $\propto\lambda^0$; se fossem de tamanho molecular, seria espalhamento Rayleigh ($\propto\lambda^{-4}$). A lei $\lambda^{-1}$ observada implica grãos de tamanho **intermediário**.

### Definições

- **Extinção ($A_\lambda$):** atenuação total da luz (absorção + espalhamento) num dado comprimento de onda, medida em magnitudes. $A_V > 0$ sempre aumenta a magnitude aparente observada.
- **Avermelhamento (excesso de cor):** $E(B-V) = A_B - A_V$ — quantifica a mudança de cor causada pela maior atenuação de comprimentos de onda curtos em relação a longos.
- **Razão de extinção total/seletiva:** $A_V = R_V \cdot E(B-V)$, com $R_V \approx 3{,}1$ típico para o meio interestelar difuso (varia entre 2,7–6 em núcleos de nuvens densas, um regime "anômalo" \[Cardelli, Clayton & Mathis 1989]).

> [!warning] Se você não corrigir a extinção...
> ...vai **subestimar sistematicamente as distâncias**, porque estrelas enfraquecidas pela poeira parecem mais distantes do que realmente estão (via módulo de distância, Aula 03).

A extinção afeta principalmente baixas latitudes galácticas (onde a poeira se concentra), mas não é nula fora do plano — precisa ser considerada sempre que se buscam distâncias precisas.

### Método de aglomerados para determinar $R_V$

Para um aglomerado, o módulo de distância intrínseco $(m_V - M_V)_0$ é constante para todas as estrelas membro. Variações observadas em $(m_V - M_V)$ vêm de diferentes quantidades de extinção ao longo de cada linha de visada:

$m_V - M_V = C + A_V = C + R_V\, E(B-V)$

onde $C$ é constante para o aglomerado (depende só da distância) e $A_V$ varia estrela a estrela.

### Mapas de extinção

Os mapas de **Schlegel et al. (1998)** foram obtidos a partir de dados de infravermelho distante (FIR) da missão COBE, fornecendo $E(B-V)$ para cada direção do céu. Ferramentas modernas: `dustmaps` (Python), o mapa 3D do Argonaut, e a interface IRSA/Caltech por coordenada.

Correção prática básica: $\text{mag}_{x,0} = \text{mag}_x - \text{coef.\ extinção}_x \cdot E(B-V)_{\text{SFD}}$ (ou multiplicado pelo fator de correção de Schlafly, $\times0{,}86$).

## 🧮 IMF — revisitada

A **função de massa inicial** (ver Aula 02) descreve a probabilidade de formação de estrelas de cada massa. Segue sendo um objeto de estudo ativo: incerta no limite de altíssimas massas ($\sim100\,M_\odot$), no valor exato do pico característico, e quanto à sua universalidade entre diferentes ambientes de formação \[Offner et al. 2014]. O formato exato da IMF é crucial para prever escalas de tempo de enriquecimento químico, ocorrência de supernovas e dinâmica do meio interestelar em uma galáxia — conectando diretamente esta aula com o tema central do curso.

---

## 📌 Conceitos-chave

- **Extinção ($A_\lambda$) vs. avermelhamento ($E(B-V)$):** atenuação total vs. mudança de cor diferencial — ambas causadas pela poeira interestelar.
- **$R_V = A_V / E(B-V) \approx 3{,}1$:** razão característica do meio interestelar difuso; usada para converter excesso de cor em extinção total.
- **Corrigir extinção é obrigatório** para qualquer estimativa de distância confiável — senão, distâncias são sistematicamente superestimadas.

## 🔗 Referências e correlatos

- Trumpler (1930) — primeira evidência de extinção interestelar via aglomerados
- Cardelli, Clayton & Mathis (1989) — lei de extinção universal parametrizada por $R_V$
- Schlegel, Finkbeiner & Davis (1998) — mapas de extinção de referência
- Offner et al. (2014) — revisão da IMF
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-02-diagrama-hr-e-aglomerados|Aula 02 — Diagrama HR e Aglomerados Estelares]] — IMF introduzida pela primeira vez
- [[pt-br/resource/curso-on/aula-06-diagrama-hr-e-relacao-massa-luminosidade|Aula 06 — Diagrama HR e Relação Massa-Luminosidade]]
- [[pt-br/research/dark-matter-shocks|Entendendo a Matéria Escura a partir de Choques Extragalácticos]] — outro método (dinâmico) de mapear massa não-luminosa, em escala extragaláctica
