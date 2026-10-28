---
publish: true
title: Spectral Anomaly Detection in Stars of the Solar Neighbourhood
created: 2026-09-19T13:18:29-03:00
modified: 2026-10-28T09:53:15-03:00
tags:
  - pesquisa
  - academico
  - en
cssclasses:
  - page-layout
icon: lucide-book-open
sitesync: true
resource-sync: true
lang: en
translation-of: "[[pt-br/research/deteccao-de-anomalias-iff-2025/index]]"
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>[[pt-br/research/index|Research]]</span> <span class="academic-nav-sep">/</span> <span>Deteccao De Anomalias Iff 2025</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Spectral Anomaly Detection in Stars of the Solar Neighbourhood</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">← Start</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">[[pt-br/research/index|Hub]]</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">→</span>

</div>

</div>

</div>

# Spectral Anomaly Detection in Stars of the Solar Neighbourhood

> [!warning] Under construction
> This page is under construction and subject to change.

> [!abstract] Research Fact Sheet
> - **Project:** look for stars that differ from the others by examining the spectrum of each one, using data from GALAH DR4 and the Gaia Catalogue of Nearby Stars
> - **Team:** Pedro Henrique Rocha de Andrade, [Dr. Maria Luiza Linhares Dantas](https://www.mlldantas.com) and [Dr. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja)
> - **Institutions:** Instituto Federal Fluminense (IFF) and Pontificia Universidad Católica de Chile, with support from CNPq
> - **Status:** in progress

---

## Research Summary

The spectrum of a star is its light split into colours, like a rainbow full of dark and bright lines. Every star has its own, and it tells what the star is made of, how hot it is and whether anything strange is going on. This research uses machine-learning methods that are given no ready-made answers: they only look at the spectra and group the similar ones. The question is what shows up when we let the spectra organise themselves, and which stars fall outside the pattern.

It is worth stressing that I do this research while studying for a bachelor's degree in computer engineering, at a campus in the countryside, at the Instituto Federal Fluminense!

---

## The story so far

This research has a story of two conferences. At RASAB 2025 I showed what the catalogue numbers say about the stars near the Sun. At RASAB 2026 I return with a bigger question: what if we look at the whole spectrum of each star, what shows up that those numbers do not reveal? Between one conference and the other, the project stopped, resumed, changed method and gained a web panel.

| Phase | When | What happened |
| :--- | :--- | :--- |
| Start | 2025 | A question about the stars near the Sun, answered with catalogue numbers and taken to SAB 2025 |
| Transition | Late 2025 | First machine-learning tests and the first attempt to read the spectra |
| Middle | 2026 | Many method tests, a first draft of the thesis (TCC) and a pause |
| Resumption | 2026 | The decision to use the spectrum as it comes and the extraction of the spectra of all of GALAH |
| Now | SAB 2026 | The mind-map poster and the web panel to explore the map |
| Next step | Coming years | The map with the full GALAH and the thesis |

### The start: what the catalogue says

It all began with a simple question: how varied are the stars within 100 parsecs of the Sun (about 326 light-years)? To answer it, I cross-matched two catalogues. The Gaia Catalogue of Nearby Stars (GCNS) tells which stars are the closest, and GALAH DR4 tells what they are like inside. 6,198 stars appear in both. In this phase I used only what the catalogue already provides, such as temperature, surface gravity, amount of metals, age and velocity, without opening a single spectrum.

It was a period of heavy work: visualising the chemical composition, the ages and the metallicity, building the diagrams that separate stars by type and by motion, and finishing the poster I took to SAB 2025, in Caxambu. Soon after, I also did the Gaia photometry, which shows the brightness and colour of each star.

### The middle: from numbers to the spectrum

After the conference I started testing methods that draw maps from many data at once, such as t-SNE and UMAP, and made the first attempt to read the spectra. Many variations of these methods followed, some good, others that led nowhere, and a first draft of the thesis text. Then the project stood still for a few months.

The resumption came with a series of meetings with the team, and from them came the decision that changed the work: use the GALAH spectrum exactly as it comes, without adjusting or inventing a single point. I reorganised the project, set aside the methods that were not helping and extracted the spectra of all the GALAH DR4 stars, a data volume of about 54 GB. From that effort came the path that became the 2026 poster: maps made with the whole spectrum of each star.

### Where I am now

The work is now at SAB 2026, in Natal, with a new poster and a web panel where the sample maps can be explored. The next step is to apply the same method to all the GALAH stars, described further below.

---

## SAB 2025: the poster in detail

RASAB 2025 was held in Caxambu (MG) and was my first participation in a national conference. The event note is at [[en/media/2025/sab|SAB 2025]]. The poster is titled *Stellar properties and chemical features of the Gaia Catalogue of Nearby Stars observed by GALAH DR4* and was made with [Dr. Maria Luiza Linhares Dantas](https://www.mlldantas.com) and [Dr. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja). The full poster is at [[resource/meta/banners/bannersab25.pdf|Banner SAB25.pdf]].

The idea of the poster was to describe the Sun's neighbourhood using only the catalogue numbers. The figures below are in the order in which I would use them to explain.

**Metals.** The histogram shows how much iron the stars have compared with the Sun ([Fe/H]). The median is -0.19, that is, the stars around here have a little less metal than the Sun.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig2-feh.png|560]]

**Magnesium relative to iron.** This measure ([Mg/Fe]) helps separate the two parts of the Galactic disc: the thin disc, younger, and the thick disc, older. The median is 0.12 and the distribution is tightly concentrated, which already suggests that most of the stars belong to the thin disc.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig3-mgfe.png|560]]

**Age.** The peak near zero may be a limit of the method that computes the ages, an error or genuinely young stars, and I did not try to separate these on the poster. The peak around 3 billion years is the main population, and the median of the sample is 1.5 billion years.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig4-idade.png|560]]

**Kiel diagram.** It places each star by its temperature and its surface gravity. The sample (red dots) lies almost entirely on the cool main sequence, the phase in which stars spend most of their lives, over the whole of GALAH DR4 in yellow. The lines are models of stars 1.5 billion years old, close to the median age.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig5-kiel.png|620]]

**Toomre diagram.** It separates stars by the way they move in the Galaxy. Those that rotate along with the disc sit near the Sun in the plot, and those that move very differently, above 100 km/s, are halo candidates. There are 5,970 disc stars and 228 halo stars: the overwhelming majority is disc.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig6-toomre.png|700]]

**Thin and thick disc.** This plot crosses magnesium and iron, and the curve of Recio-Blanco et al. (2014) divides the stars: above it, thick disc; below, thin disc. The stars well above the curve are 22.51% of the sample. Part of this metal-rich thick disc probably comes from the way the two catalogues selected the stars, and not from the Galaxy itself.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab25-fig7-tinsley.png|700]]

The result in a few lines: about 6,000 stars, most of them similar to the Sun (with a few hotter ones), temperatures between 3000 K and 8000 K, a median age of 1.5 billion years, a bit less metal than the Sun and almost all in the disc. The gap that remained is that all of this came from the catalogue. The spectra were left out, and that is where the 2026 work comes from.

### SAB 2025 poster

![[resource/meta/site-static/banners/bannersab25.pdf]]

## SAB 2026: the continuation

RASAB 2026 takes place in Natal (RN). The event note is at [[en/media/2026/sab/index|SAB 2026]]. The work is titled *How varied are stellar populations in the Solar vicinity? Exploring GCNS and GALAH DR4 with t-SNE* and is done with [Dr. Maria Luiza Linhares Dantas](https://www.mlldantas.com) and [Dr. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja). The posters are in the [[resource/meta/banners/bannersab26-mapa-mental.pdf|mind-map version]] and the [[resource/meta/banners/bannersab26-base-v3.pdf|base version]].

The stars are the same 6,198, but now I look at the whole spectrum of each one, point by point: there are 14,245 points per star, coming from the four cameras of the instrument, one for each colour band. I use the spectrum as it comes, without adjustments. 5,304 stars enter the map. The other 894 are left out because the piece from one of the cameras is missing, and I never invent what is missing. On the mind-map poster, the map sits in the centre and each surrounding panel is a question about it.

**The map.** Each point is a star. Stars with similar spectra sit close together. The colour is the temperature, and the symbols mark stars with emission lines (orange), signs that they are shining beyond normal, and stars that are actually binaries (diamond and circle). The map never saw the temperature or any other number: only the spectrum.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig1-mapa-tsne.png|760]]

**Colours.** Painting the same map by temperature, gravity and metals, an ordering by temperature appears, along with a smooth variation of gravity and metals. None of this was given to the method. It found it on its own.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig2-coloracoes.png|760]]

**GALAH flags.** GALAH itself flags the stars in which it saw a problem or a special feature. Here I separate the stars with no flag, with a flag and with emission only, to see where they fall on the map. These filters only change what is shown on screen, they do not redo the map. More than half of the stars on the map (52%) carry the low-signal flag.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig3-flags.png|760]]

**Emission stars.** There are 286 stars, and they split into five smaller groups within the map. The largest is made of cool stars with metals similar to the Sun's, and two others are made of metal-poor stars.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig4-emissao-subclusters.png|760]]

In the Kiel diagram, the emission stars lie on the cool main sequence, on top of the red dwarfs. One of the groups, near 4500 K, is the hottest.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig5-kiel-subclusters.png|620]]

**Other settings.** The same map made with other t-SNE settings and with UMAP, with the emission highlighted. The organisation of the stars is still there when I change the method and the settings, which is exactly what I wanted to test.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig6-outras-projecoes.png|760]]

**Spectra.** An emission star and an ordinary star side by side, with the hydrogen (Hα), lithium and potassium lines. It is the check that the difference the map showed really appears in the light of the stars.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/sab26-fig7-espectros.png|760]]

What remains from the poster: the ordering by temperature appears on its own, without anyone telling the method what temperature is, in every version I tested, and the emission stars split into five groups. For now these groups are candidates, not definitive classes: it still remains to test carefully whether they hold when I change the settings.

### SAB 2026 posters

The mind-map version is the one that will be presented: the central map and, around it, the questions about it. The base version follows the linear layout of the SAB 2025 poster.

#### Mind-map version

![[resource/meta/site-static/banners/bannersab26-mapa-mental.pdf]]

#### Base version

![[resource/meta/site-static/banners/bannersab26-base-v3.pdf]]

## Future work: the full GALAH

The next step is to take the same method from the sample near the Sun to the whole of GALAH DR4, with more than 900 thousand stars. The spectra are already extracted. What is missing is drawing the map with all of them.

The figure below is a trial run. On the left are the red dwarfs of the local sample and, on the right, 30 thousand stars drawn at random from the full GALAH, both coloured by temperature. It shows that the method keeps ordering the stars by temperature when the sample grows and becomes more varied. It is not yet the result with the full GALAH.

![[resource/areas/academico/pesquisas/deteccao-de-anomalias-iff-2025/arquivos/futuro-galah-completo-subamostra.png|760]]

What is ready and what is missing:

- **Program to run everything:** it already exists and has been tested with 10 thousand real spectra. It still has to be run on the hundreds of thousands of stars.
- **Computation:** the whole of GALAH needs hours of processing on powerful graphics cards for each version of the map.
- **Web panel:** the public version shows the sample near the Sun. The full-GALAH part exists, but for now it is for internal use.
- **After the map:** confirm whether the groups hold and look at the spectra of the candidate stars, one by one.
- **Writing:** the thesis, with the analysis of the full GALAH as its central part.
