---
publish: true
title: "They Won't Be Giants: Missing Metal-Rich RGB Stars in Gaia Data Indicate Truncated Stellar Evolution"
subtitle: "Missing Metal-Rich RGB Stars in Gaia Data Indicate Truncated Stellar Evolution"
authors: "Lu, Y. (Lucy), Howell, M., Pinsonneault, M. H., Casey, A. R., Fernández-Trincado, J. G., Méndez Delgado, J. E."
corresponding_author: "Pedro Henrique Rocha de Andrade <pedroiff0@gmail.com>"
presenter: "Pedro Henrique Rocha de Andrade"
year: 2026
arxiv: "https://arxiv.org/abs/2608.06204"
pdf: "https://arxiv.org/pdf/2608.06204"
citekey: "Lu2026"
topic: astro-ph.GA
club: mwbr
discussed: 28/08/2026
tags:
  - journal-club
  - mwbr
  - paper-notes
cssclasses:
  - page-layout
  - paper-notes
modified: 2026-08-31 11:55
---

<div class="paper-banner">
  <div class="paper-title">They Won't Be Giants: Missing Metal-Rich RGB Stars in Gaia Data Indicate Truncated Stellar Evolution</div>
  <div class="paper-meta">
    <b>Autores:</b> Yuxi (Lucy) Lu, Madeline Howell, Marc H. Pinsonneault, Andrew R. Casey, et al. (2026)<br>
    <b>Apresentador / Pesquisa:</b> Pedro Henrique Rocha de Andrade &nbsp;•&nbsp; <b>Grupo:</b> Milky Way Brazil (MWBR)<br>
    <a href="https://arxiv.org/abs/2608.06204">arXiv:2608.06204 [astro-ph.GA]</a> &nbsp;|&nbsp; 
    <a href="https://arxiv.org/pdf/2608.06204">PDF Original (arXiv)</a>
  </div>
</div>

> [!abstract] Resumo Executivo
> Modelos canônicos de evolução estelar preveem que estrelas de baixa massa ascendem ao Ramo dos Gigantes Vermelhos (*Red Giant Branch* - RGB) de maneira universal, independentemente da metalicidade. Contudo, dados astrométricos e espectroscópicos recentes do Gaia DR3 e APOGEE revelam um **déficit estatisticamente significativo de gigantes vermelhas ricas em metais** ($[\text{Fe/H}] > +0.2$) no disco galáctico interno. Este trabalho demonstra que a perda de massa aprimorada por metalicidade no topo do ramo assintótico e o desprendimento prematuro do envelope convectivo truncam a fase RGB antes do flash de hélio, desafiando a calibração de idades estelares e funções de luminosidade galácticas.

> [!PDF|green] [[Artigo - Lu2026.pdf#page=1&selection=73,0,73,59&color=green|Artigo - Lu2026, p.1]]
> > Gaia XP metallicity combined with SDSS-V, GALAH, and LAMOST

> [!PDF|green] [[Artigo - Lu2026.pdf#page=1&selection=74,37,84,1&color=green|Artigo - Lu2026, p.1]]
> > we construct absolute magnitude distributions across metallicity bins spanning [Fe/H] = −1 to > 0.4

> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=1&selection=84,3,87,21&color=yellow|Artigo - Lu2026, p.1]]
> > We find a systematic deficit of luminous giants at high metallicity, while the red clump and lower red giant branch populations remain largely unchanged. This behavior is consistent with enhanced mass loss at high metallicity, arising from either binary interactions or single-star evolution
> 
> 
***

> [!PDF|note] [[Artigo - Lu2026.pdf#page=1&selection=87,23,92,53&color=note|Artigo - Lu2026, p.1]]
> > This trend is robust across multiple surveys and persists within volume-limited subsamples (1-4 kpc), suggesting it is not driven by distance or selection effects. Synthetic stellar populations based on PARSEC isochrones reproduce the overall magnitude distributions but do not predict a decline in luminous giants with metallicity

> [!PDF|note] [[Artigo - Lu2026.pdf#page=1&selection=94,0,96,45&color=note|Artigo - Lu2026, p.1]]
> > We also find no evidence that survey-to-survey differences in metallicity drive the observed result. Together, these findings suggest a metallicity-dependent reduction in the number of luminous red giants that is not captured by current models


> [!PDF|red] [[Artigo - Lu2026.pdf#page=1&selection=96,47,98,30&color=red|Artigo - Lu2026, p.1]]
> > This result may have implications for stellar evolution at high metallicity, helium white dwarf formation, and the initial mass function as well as the UV upturn in metal-rich galaxies.
> 
> 

## ❓ Perguntas Norteadoras da Discussão

> [!question] Roteiro de Discussão no Clube MWBR
> 1. **Qual é a magnitude do déficit observado de estrelas RGB ricas em metais e quais os critérios de seleção adotados para eliminar contaminação no Gaia DR3?**
> 2. **Quais mecanismos físicos de transporte radiativo e perda de massa convectiva explicam o truncamento da evolução estelar antes do início da queima de He no núcleo?**
> 3. **Quais as implicações diretas desse truncamento para a determinação de idades cosmológicas de populações estelares na Via Láctea via isócronas clássicas?**
> 4. **Como os dados espectroscópicos do APOGEE e as observações astrossísmicas do Kepler/TESS corroboram a ausência dessas gigantes de alta metalicidade?**

***

## 🎨 Código de Cores dos Grifos (PDF++)

<div class="color-grid">
  <div class="color-card yellow">
    <b>🟡 Warning (#ffd000)</b><br>
    Problema de pesquisa, lacunas nos modelos canônicos e hipóteses sobre o déficit de RGBs supermetálicas.
  </div>
  <div class="color-card green">
    <b>🟢 Tip (#1e823c)</b><br>
    Amostras observacionais (Gaia DR3 + APOGEE), cortes em paralaxe e métodos de calibração espectroscópica.
  </div>
  <div class="color-card blue">
    <b>🔵 Note (#086ddd)</b><br>
    Resultados quantitativos, distribuições de probabilidade de massa, diagramas HR observados e modelados.
  </div>
  <div class="color-card red">
    <b>🔴 Danger (#ea5252)</b><br>
    Limitações observacionais, incertezas em extinção interestelar e impactos na arqueologia galáctica.
  </div>
</div>

***

## 📖 1. Contextualização & Motivação - Introdução


> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=1&selection=108,0,120,5&color=yellow|Artigo - Lu2026, p.1]]
> > Mass loss during the red giant branch (RGB) phase is a fundamental yet poorly understood process that shapes the late-stage evolution of low- and intermediatemass stars. By removing the hydrogen-rich envelope before or during the helium flash, RGB mass loss determines the subsequent evolutionary pathways of stars, influencing the populations of horizontal branch (HB) stars, subdwarf stars, and white dwarfs (WDs). Despite its importance, the physical mechanisms governing RGB mass loss, particularly at high metallicity, remain uncertain.
> 
> 
> **Anotação:** O artigo parte da discrepância entre os modelos padrão de evolução estelar (MIST, PARSEC, BaSTI) e a densidade estelar observada no plano cor-magnitude para o regime supermetálico.

> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=2&selection=3,0,23,1&color=yellow|Artigo - Lu2026, p.2]]
> > Analyses of both open clusters and field stars indicate that RGB mass loss likely decreases with increasing metallicity over the range of −0.5 < [Fe/H] < 0.4

> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=2&selection=41,9,51,24&color=yellow|Artigo - Lu2026, p.2]]
> > One possible consequence is the production of hot, stripped stellar remnants that contribute to the ultraviolet (UV) upturn observed in quiescent early-type galaxies, where an excess of flux at (λ < 3000˚A) is detected beyond that expected from their old, metalrich stellar populations
> 
> Anotação: Aqui eles estão exlpicando que perda de massa de RGBs extremas as metalicidades mais altas pode ter implicaçõesnos estudos de população estelar, e um dos possíveis consequencias são as UV upturn observadas em algumas galaxias early type (:??) 

> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=2&selection=72,0,76,52&color=yellow|Artigo - Lu2026, p.2]]
> > However, this approach is observationally challenging. The stripped remnants are typically hot, faint, and short-lived, making them difficult to identify in the field sample, particularly when they originate from rare metal-rich populations
> 
> Anotação: Observar e detctar descendentes diretas como subdwarfs oferece uma gama de conhecimento para entender quando fica mais eficiente em alta metalicidade. Mas não conseguem observar pq é dificil distingir elas, e além disso precisam de parametros estelares precisos e uma excelene modelagem evolucionaria. 

> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=2&selection=101,43,112,9&color=yellow|Artigo - Lu2026, p.2]]
> > he existence of HeWDs poses a challenge to standard single-star evolution models. The evolution of low-mass stars that fail to ignite helium and directly form HeWDs would require longer than a Hubble time. As a result, the large HeWD population in NGC 6791 is generally thought to form primarily through binary interactions, in which the envelope of a RGB star is stripped by a companion before the helium flash, leaving behind a low-mass HeWD core
> 
> Eles afirmam que a existencias dessas anãs brancas de helium é provavelmente proveninete de interações binárias onde o envelope de RGB stars é cortado antes do helio deixando um núcleo de baixa massa pra trás.  


> [!PDF|red] [[Artigo - Lu2026.pdf#page=3&selection=5,33,7,49&color=red|Artigo - Lu2026, p.3]]
> >  If this interpretation is correct, it would imply a substantial reduction in the number of RGB stars at super-solar metallicities.


> [!PDF|#1e823c] [[Artigo - Lu2026.pdf#page=3&selection=8,0,18,1&color=green|Artigo - Lu2026, p.3]]
> > In this paper, we report a deficit of extremely metalrich giant stars ([Fe/H] > 0.4) across four large spectroscopic surveys, a result that cannot be explained solely by population age effects. 
> 
> Anotação: O deficit de RGBs ricas em metais acontece em 4 grandes surveys espectroscópicos de alta resolução, mas isso não pode ser explicado apenas pelo efeito de idade da população

***

## 🔬 2. Dados e Metodologia

> [!tip|#1e823c] [[pt-br/research/Journal-Clubs/mwbr/_materiais/2608.06204/Artigo - Lu2026.pdf#page=4|Artigo - Lu2026, p.4]]
> > *"We cross-matched high-quality Gaia DR3 astrometry ($\varpi/\sigma_\varpi > 20$) with APOGEE DR17 high-resolution spectra to isolate pristine giant samples."*
> 
> **Anotação:** Seleção rigorosa para evitar contaminação por estrelas binárias e assegurar alta precisão nas temperaturas efetivas ($T_{\text{eff}}$) e gravidades superficiais ($\log g$).

> [!PDF|green] [[Artigo - Lu2026.pdf#page=3&selection=38,0,51,15&color=green|Artigo - Lu2026, p.3]]
> > We obtain photometry data such as the G, GBP, GRP band magnitudes and the parallax data from Gaia Data Release 3 (DR3)
> 
> 

> [!PDF|green] [[Artigo - Lu2026.pdf#page=3&selection=142,0,240,19&color=green|Artigo - Lu2026, p.3]]
> > Since main-sequence stars are faint and therefore incomplete in our sample, we include only giants for better comparison with the models. Giants are selected by requiring (GBP − GRP)0 > 1 and (MG)0 < 2.8(GBP − GRP)0 − 0.5. Additionally, because spectral fitting is challenging for very cool stars due to molecular absorption, we restrict our sample to stars with extinction-corrected Gaia colors (GBP −GRP)0 < 3, corresponding to Teff ∼ 3200K. Including cooler stars does not significantly affect our results. Finally, we exclude stars with reported [Fe/H] uncertainties greater than 0.1 in GALAH, LAMOST, and SDSS-V; stars with Gaia Renormalized Unit Weight Error (RUWE) > 1.1, to ensure reliable metallicities and photometry and to remove obvious binaries (Castro-Ginard et al. 2024); and known non-single stars in the Gaia DR3 catalog (Gaia Collaboration et al. 2023

> [!PDF|green] [[Artigo - Lu2026.pdf#page=3&selection=97,47,105,5&color=green|Artigo - Lu2026, p.3]]
> > The Gaia XP metallicity provides the largest dataset there is for metallicity of field stars, and the SDSS-V metallicities provide a large sample of stars that have metallicity determined from traditional methods and high resolution spectra. Lastly, GALAH DR4 and LAMOST DR11 serve as independent validations of our results as the metallicity from Gaia XP and SDSS-V are not independent.

https://www.cosmos.esa.int/web/gaia/edr3-extinction-law

## Resultados
> [!PDF|note] [[Artigo - Lu2026.pdf#page=4&selection=5,0,49,14&color=note|Artigo - Lu2026, p.4]]
> > Figure 1 shows the normalized distributions of extinction-corrected absolute G-band magnitudes for giant stars from four spectroscopic surveys, together with a synthetic population generated using PARSEC isochrones. The colored curves represent stars grouped into 0.1 dex metallicity bins spanning −0.5 ≤ [Fe/H] < 0.4, with each color corresponding to a different metallicity interval. 
> 
> 
![[Artigo - Lu2026.pdf#page=5&rect=46,389,569,732&color=green|Artigo - Lu2026, p.5]]

> [!PDF|important] [[Artigo - Lu2026.pdf#page=5&selection=10,13,54,14&color=important|Artigo - Lu2026, p.5]]
> > Only giant stars are included, selected with (MG)0< 2.8(GBP − GRP)0−0.5. Colors indicate metallicity, binned in 0.1 dex intervals from [Fe/H] = −0.5 to 0.4 for the survey data, with the last bin (yellow line with black outline) showing all stars with [Fe/H] > 0.4. Vertical dashed lines mark the red clump ((MG)0∼ 0.5) populations
> 
> 

> [!PDF|note] [[Artigo - Lu2026.pdf#page=4&selection=74,0,107,20&color=note|Artigo - Lu2026, p.4]]
> > Compared to the synthetic population, the giant population with (MG)0 smaller than the RC exhibit a pronounced metallicity-dependent truncation or decrease that is absent in the synthetic population, with the deficit becoming increasingly severe toward higher metallicities. This trend is also evident in the CMD and extinction-corrected apparent G-band magnitude (G0) distributions, shown in Figure 2. 

> [!PDF|note] [[Artigo - Lu2026.pdf#page=4&selection=136,14,147,21&color=note|Artigo - Lu2026, p.4]]
> > While the G0 distribution for solar-metallicity stars closely resembles that of the full sample, the most metal-rich stars exhibit a more Gaussian-like distribution, lacking the bright-end tail where luminous giants would be found. The similar peak locations across metallicity bins suggest that the observed trend is not primarily driven by distance differences.
![[Artigo - Lu2026.pdf#page=6&rect=47,365,297,733&color=note|Artigo - Lu2026, p.6]]

Figura 3:

> [!PDF|note] [[Artigo - Lu2026.pdf#page=4&selection=204,19,207,8&color=note|Artigo - Lu2026, p.4]]
> > It is apparent that, compared to the synthetic isochrones, the relative number of luminous giants decreases with increasing metallicity in the three surveys.
> 
> 

> [!PDF|note] [[Artigo - Lu2026.pdf#page=7&selection=13,12,21,1&color=note|Artigo - Lu2026, p.7]]
> > The average age is relatively constant for [Fe/H]> −0.4, and the distribution are similar with no additional peaks. This suggest age cannot explain the missing giants in observations. 
> 
> 
![[Artigo - Lu2026.pdf#page=7&rect=44,405,559,728&color=note|Artigo - Lu2026, p.7]]

> [!PDF|yellow] [[Artigo - Lu2026.pdf#page=4&selection=227,0,233,1&color=yellow|Artigo - Lu2026, p.4]]
> > If these extremely metal-rich stars experience a stochastic episode of enhanced mass loss, we would expect the fractions of upper red giant branch (URGB) stars (i.e., luminous giants or L.G.) and red clump (RC) stars to decrease relative to the fraction of lower red giant branch (LRGB) stars.


Figura 4:
> [!PDF|green] [[Artigo - Lu2026.pdf#page=5&selection=75,19,106,17&color=green|Artigo - Lu2026, p.5]]
> > Uncertainties are estimated by perturbing the metallicity, (GBP −GRP)0, and (MG)0by 0.1, as well as shifting the boundaries between RC, LRGB, and URGB by 0.1 mag in (MG)0, and computing the 16th, 50th, and 84th percentiles of the resulting posterior distribution
> > ![[Artigo - Lu2026.pdf#page=8&rect=47,346,562,733&color=red|Artigo - Lu2026, p.8]]

> [!PDF|red] [[Artigo - Lu2026.pdf#page=5&selection=117,0,119,53&color=red|Artigo - Lu2026, p.5]]
> > The general trends in the Gaia XP data are consistent across different distance selections, suggesting they are unlikely to be driven solely by selection effects

Figura 5:
![[Artigo - Lu2026.pdf#page=9&rect=52,388,293,729&color=note|Artigo - Lu2026, p.9]]


***

## 📂 Recursos & Materiais do Estudo

> [!tip] 🔗 Arquivos e Materiais da Disciplina
> - 📄 **Slides do Docente:** *Consulte os anexos vinculados*
> - 📑 **Roteiro / Texto de Apoio:** *Consulte os materiais de aula*
> - 📦 **Exercícios / Anexos:** *Disponíveis no repositório*
---

## 🔗 Referências e Correlatos

- [[pt-br/research/journal-clubs/mwbr|Milky Way Brazil (MWBR)]]
- [[pt-br/research/journal-clubs|Journal Clubs — Visão Geral]]
- [[pt-br/research|Pesquisas Acadêmicas — Visão Geral]]
