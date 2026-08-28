---
publish: false
title: Aula 10 — Integração de Órbitas com galpy
created: 2026-07-25 12:36
modified: 2026-08-27 21:54
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
titulo: CursoON-Aula10
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: Aula prática (Google Colab/galpy) — construir potenciais galácticos, obter dados do Gaia via SQL/TAP, integrar órbitas estelares com incertezas por Monte Carlo, e simular o efeito de fricção dinâmica de um satélite (Sagitário) sobre o disco
professor: Hélio Dotto Perottoni
---

# 🛰️ Aula 10 — Integração de Órbitas com galpy

> [!note] Resumo
> Aula prática que aplica a teoria da Aula 09 (potenciais, integrais de movimento) em código real: construir e comparar potenciais da Via Láctea com [galpy](https://docs.galpy.org/), obter dados astrométricos do Gaia via consultas SQL/TAP, integrar a órbita 6D de uma estrela (posição + velocidade) propagando corretamente as incertezas observacionais, e simular como a galáxia anã de Sagitário, ao cair no disco por fricção dinâmica, perturba as órbitas de estrelas do disco.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** notebook oficial da disciplina (Google Colab, biblioteca [galpy](https://docs.galpy.org/))

---

## 🎯 Visão geral

Esta é a contrapartida prática da Aula 09: em vez de derivar o formalismo da dinâmica estelar, o notebook usa a biblioteca Python **galpy** para (1) construir e visualizar potenciais gravitacionais da Via Láctea, (2) obter dados observacionais reais do Gaia, (3) integrar órbitas estelares — propagando corretamente as incertezas astrométricas — e (4) simular o efeito dinâmico de uma galáxia satélite (Sagitário) caindo no potencial da Galáxia via fricção dinâmica.

## ⚙️ Construindo e comparando potenciais galácticos

O galpy já vem com potenciais pré-definidos para a Via Láctea, como `MWPotential2014` e `McMillan17`, cada um decomposto em componentes (bojo, disco, halo) que podem ser avaliados e plotados separadamente com `plotRotcurve` — reproduzindo diretamente a lógica de $v_c(r)=\sqrt{GM(<r)/r}$ vista na Aula 09.

> [!warning] galpy trabalha com unidades adimensionais
> Internamente, o galpy normaliza posição e velocidade por escalas características ($R\to R/r_o$, $v\to v/v_o$), tipicamente $r_o=8\,$kpc e $v_o=220\,$km/s (o mesmo $\Theta_0$ do LSR, Aula 08). É preciso manter esse sistema de unidades consistente ao longo de toda a análise, ou os resultados saem sem sentido físico.

É possível também **construir um potencial próprio**, combinando componentes analíticos (`MiyamotoNagaiPotential` para o disco, `NFWPotential` para o halo, `HernquistPotential` para o bojo) com pesos normalizados que somem 1 — o mesmo espírito dos "exemplos de potenciais esféricos" (esfera homogênea, Plummer, leis de potência) mencionados na Aula 09.

## 📡 Obtendo dados do Gaia via SQL/TAP

Consultas ao catálogo Gaia DR3 são feitas por **SQL**, enviadas através do pacote `pyvo` a um serviço **TAP** (_Table Access Protocol_, ex.: `gaia.ari.uni-heidelberg.de/tap`). Uma consulta típica busca estrelas numa posição e raio (em graus):

```sql
SELECT * FROM gaiadr3.gaia_source AS gaia
WHERE 1=CONTAINS(POINT('ICRS', gaia.ra, gaia.dec), CIRCLE('ICRS', RA, DEC, search_rad))
```

O resultado (uma `VOTable`) é convertido para `astropy.Table` e depois para `pandas.DataFrame`, de onde se extraem os observáveis 6D necessários para uma órbita: posição (`ra`, `dec`, distância — aqui obtida por um catálogo de RR Lyrae, não só por paralaxe simples) e velocidade (`pmra`, `pmdec`, velocidade radial).

## 🌀 Integrando a órbita de uma estrela

Com os 6 observáveis (`ra, dec, dist, pmra, pmdec, vrad`), a classe `Orbit` do galpy integra a trajetória da estrela para frente e para trás no tempo, num potencial escolhido (ex.: `MWPotential2014`):

```python
orbit = Orbit([ra, dec, dist, pmra, pmdec, vrad], radec=True)
orbit.integrate(ts, MWPotential2014)
```

As projeções $X$–$Y$ (vista de cima do disco) e $R$–$Z$ (vista de perfil) mostram a trajetória resultante, e o galpy oferece ainda animações 2D e 3D da órbita ao longo do tempo (`orbit.animate()`, `orbit.animate3d()`).

### Propagando incertezas por Monte Carlo

> [!warning] As incertezas do Gaia são correlacionadas
> Os parâmetros astrométricos do Gaia não são medidos de forma independente — resultam de um ajuste simultâneo de um modelo astrométrico aos dados. Se as incertezas de `pmra` e `pmdec` são correlacionadas (o Gaia fornece essa covariância, `pmra_pmdec_corr`), é preciso levar a **matriz de covariância completa** em conta ao gerar amostras aleatórias, não apenas as incertezas individuais.

O procedimento: (1) montar a matriz de covariância 4×4 (velocidade radial, distância, `pmra`, `pmdec`); (2) amostrar $N$ realizações de uma gaussiana multivariada com essa covariância; (3) integrar $N$ órbitas independentes, uma por realização; (4) tomar percentis (16/50/84) das grandezas de interesse — energia $E$, momento angular $L_z$, pericentro $r_{peri}$, apocentro $r_{apo}$, excentricidade — para obter a incerteza orbital final. Um estudo citado na aula (Feliciano-Souza, em prep.) usa exatamente essa abordagem para determinar quantas realizações de Monte Carlo (testado de 50 a 1000) são estatisticamente suficientes, usando uma amostra de 50 mil estrelas do levantamento SEGUE.

## 🐕 Fricção dinâmica: a queda de Sagitário na Via Láctea

A segunda metade da aula integra a órbita da **galáxia anã de Sagitário** (usando condições iniciais de Vasiliev 2020, ou obtidas diretamente do Simbad via `Orbit.from_name("SDG")`) voltando ~4 bilhões de anos no passado — mas um satélite real perde energia orbital por **fricção dinâmica**, um efeito ausente de uma integração de órbita simples num potencial estático.

O galpy implementa a fricção dinâmica de Chandrasekhar (`ChandrasekharDynamicalFrictionForce`), que requer conhecer a massa e o perfil de densidade tanto do satélite quanto da galáxia hospedeira:

$F_{DF} \propto M_{sat}^2$

> [!tip] Por que $F\propto M^2$ importa
> Uma galáxia satélite **mais massiva** perde energia rapidamente por fricção dinâmica — sua órbita espirala para dentro e os pericentros sucessivos diminuem. Uma satélite **menos massiva** perde energia devagar e sua órbita muda pouco. É por isso que só satélites suficientemente massivos (como as Nuvens de Magalhães ou o próprio Sagitário) afundam visivelmente no potencial da Galáxia numa escala de tempo hubbliana.

A aula também mostra que o potencial de halo padrão do `MWPotential2014` está no limite inferior das estimativas atuais de massa — aumentá-lo em 50% (`MWPotential2014_heavy`) o torna mais consistente com medidas recentes, e muda visivelmente a órbita reconstruída de Sagitário.

### O satélite como potencial "vivo": perturbando o disco

Por fim, o notebook combina os dois efeitos: usa `MovingObjectPotential` para transformar a órbita integrada de Sagitário (modelada como uma esfera de Plummer de massa $5\times10^9\,M_\odot$) num **componente adicional, dependente do tempo**, do potencial total. Um pequeno conjunto de órbitas estelares do disco, integrado nesse potencial combinado (`MWPotential2014_heavy + satpot`), mostra trajetórias visivelmente perturbadas em comparação às mesmas órbitas no potencial estático original — uma demonstração direta e computacional de como um satélite em queda deixa impressa uma assinatura dinâmica no disco (o mesmo tipo de mecanismo por trás de fenômenos como o _phase spiral_ do Gaia, e de correntes estelares de maré).

> [!warning] Limitações reconhecidas no próprio notebook
> A simulação não leva em conta a **perda de massa** do satélite ao longo da queda (que mudaria a intensidade da fricção dinâmica com o tempo), nem testa a sensibilidade a diferentes potenciais hospedeiros. O próprio material da aula é honesto sobre isso: dado tudo isso, o quanto se pode confiar nos detalhes finos dessas órbitas reconstruídas é uma pergunta em aberto — a escolha de uma "órbita fiducial" é sempre uma simplificação.

---

## 📌 Conceitos-chave

- **galpy:** biblioteca Python para dinâmica galáctica — potenciais pré-definidos e customizados, integração de órbitas, coordenadas ação-ângulo, tudo em unidades internas adimensionais ($r_o=8\,$kpc, $v_o=220\,$km/s por convenção).
- **TAP/SQL:** protocolo padrão para consultar catálogos astronômicos públicos (Gaia, entre outros) via consultas estruturadas.
- **Covariância das incertezas do Gaia:** `pmra` e `pmdec` têm erros correlacionados; ignorar essa correlação ao propagar incertezas (Monte Carlo) produz estimativas erradas dos parâmetros orbitais.
- **Fricção dinâmica (Chandrasekhar, $F\propto M^2$):** mecanismo pelo qual um satélite massivo perde energia orbital e espirala para dentro da galáxia hospedeira — depende da massa e do perfil de densidade de ambos os sistemas.
- **`MovingObjectPotential`:** técnica para simular o efeito gravitacional, dependente do tempo, de um satélite em queda sobre as órbitas de estrelas do disco — a base computacional para estudar perturbações como as atribuídas a Sagitário.

## 🔗 Referências e correlatos

- Documentação do [galpy](https://docs.galpy.org/) — biblioteca usada em toda a aula
- Vasiliev (2020) — condições iniciais da órbita de Sagitário
- Feliciano-Souza et al. (em prep.) — número de realizações de Monte Carlo necessárias para parâmetros orbitais robustos (amostra SEGUE)
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-09-orbitas-potenciais-e-integrais-de-movimento|Aula 09 — Órbitas, Potenciais e Integrais de Movimento]] — o formalismo teórico (Poisson, $v_c(r)$, integrais de movimento) que este notebook implementa em código
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula02|Escola de Inverno — Arqueologia Galáctica, Aula 02]] — Omega Centauri e a Gaia-Sausage-Enceladus como outros exemplos de galáxias satélites incorporadas à Via Láctea
- [[pt-br/resource/curso-on/aula-11-satelites-lmc-e-barra-galactica|Aula 11 — Órbitas de Satélites, a LMC e a Barra Galáctica]] — continuação direta: pericentro/apocentro, a LMC em referencial não inercial, e ressonâncias de barra
