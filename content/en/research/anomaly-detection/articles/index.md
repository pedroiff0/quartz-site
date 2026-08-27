---
publish: false
title: "Articles"
created: 2026-07-23
modified: 2026-07-25T23:58:08.061-03:00
published: 2026-07-25T23:58:08.061-03:00
order: 1
cssclasses:
  - page-layout
---

> [!note] Summary
> Reading notes on 28 scientific articles relevant to the project [[en/research/anomaly-detection|Gaia Data Anomalies Detection]], organized by theme.


<div class="media-carousel">
  <a href="/pt-br/research/anomaly-detection/articles/collaboration2016" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="The Gaia Mission" />
    <div class="slide-caption">The Gaia Mission</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/buder2025" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GALAH DR4" />
    <div class="slide-caption">GALAH DR4</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/majewski2017" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="APOGEE" />
    <div class="slide-caption">APOGEE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/deandrade2025" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GCNS × GALAH DR4" />
    <div class="slide-caption">GCNS × GALAH DR4</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/traven2017" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="GALAH — Classification via t-SNE" />
    <div class="slide-caption">GALAH — Classification via t-SNE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/lochner2021" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="ASTRONOMALY" />
    <div class="slide-caption">ASTRONOMALY</div>
  </a>
</div>


 Reading notes on scientific articles relevant to my research in detecting anomalies in stellar populations — own syntheses, not complete articles (editors/arXiv copyrights remain with the original authors). Grouped by role in the project: the surveys and data I use, the machine learning methods I apply, the stellar models that calibrate my ages/isochrons, and the context of galactic dynamics/chemistry that interprets the results.

## 🛰️ Surveys and catalogues (data)

- [[en/research/anomaly-detection/articles/collaboration2016|The Gaia Mission]]— astrometry of billions of stars; source of the project's kinematic coordinates.
- [[en/research/anomaly-detection/articles/collaboration2021|Gaia EDR3 — Gaia Catalog of Nearby Stars]]— clear catalogue at 100 ch of the Sun, basis of sample GCNS.
- [[en/research/anomaly-detection/articles/deandrade2025|GCNS × GALAH DR4]]— my own article, the joint analysis under Step 1.
- [[en/research/anomaly-detection/articles/buder2025|GALAH DR4]]— GALAH 4th release: up to 32 elements per star via neural networks.
- [[en/research/anomaly-detection/articles/kos2017|GALAH — Data Reduction Pipeline]]— how the raw spectra of HERMES saw the parameters of the catalogue.
- [[en/research/anomaly-detection/articles/majewski2017|APOGEE]]— high-resolution infrared survey, used as comparison/context.
- [[en/research/anomaly-detection/articles/xiang2019|LAMOST DR5 — Abundances of 16 Elements]]— another large-volume spectroscopic survey, date-driving approach (DD-Payne).
- [[en/research/anomaly-detection/articles/quispehuaynasi2025|S-PLUS DR4 — SED Outliers]]— detection of photometric anomalies in different survey, methodological parallel.

## 🤖 Machine learning and anomaly detection

- [[en/research/anomaly-detection/articles/traven2017|GALAH — Classification via t-SNE]]— Stage 2 basic methodology (t-SNE on crude spectra).
- [[en/research/anomaly-detection/articles/dasilva2023|da Silva & Smiljanic (2023) — t-SNE Chemodynamics]]— the basis of the comparison between catalogue columns and spectrum pixels.
- [[en/research/anomaly-detection/articles/lochner2021|ASTRONOMALY]]— motivation of scale: why big astronomical data requires automatic detection of anomalies.
- [[en/research/anomaly-detection/articles/ishida2021|Active Detection of Anomalies (Time-Domain)]]—  active learning  applied to the discovery of unusual objects.
- [[en/research/anomaly-detection/articles/traven2019|Machine Learning for Binary]]— revision of LM methods in large surveys.
- [[en/research/anomaly-detection/articles/otar2021|GALAH — Emission Line Stars]]— self-encoder that rebuilds spectra to find abnormal emissions — same family of Step 2 method.
- [[en/research/anomaly-detection/articles/hughes2022|GALAH — Extremely Poor Stars in Metals]]— LM supervised to find 54 EMP candidates at GALAH.
- [[en/research/anomaly-detection/articles/vogrini2023|GALAH — Diffuse Interstellar Bands]]— another example of GALAH  big data  spectroscopic mining.

## ⭐ Star models and ages

- [[en/research/anomaly-detection/articles/bressan2012|PARSEC — Star Isochrons]]— stellar evolution code generating isochrons used in the Kiel diagram.
- [[en/research/anomaly-detection/articles/marigo2017|PARSEC-COLIBRI — TP-AGB Phase Isochrons]]— the latest generation of isochrons, with a detailed TP-AGB phase.
- [[en/research/anomaly-detection/articles/hayden2022|GALAH — Chemical clocks]]— age via XGBoost from metalicity only/abundances.
- [[en/research/anomaly-detection/articles/traven2020|GALAH — FGK Binaries]]— sample of spectroscopic binaries, relevant for cleaning contaminants from the sample.
- [[en/research/anomaly-detection/articles/thomas2024|SpectroTranslator]]— neural network to convert parameters between different surveys.

## 🌌 Dynamics and galactic chemistry (interpretation)

- [[en/research/anomaly-detection/articles/bovy2015|galpy]]— package used to calculate orbits and actions, base of the project kinematics.
- [[en/research/anomaly-detection/articles/mcmillan2017|Milky Way Mass and Potential Distribution]]— the galactic potential used in galpy to integrate orbits.
- [[en/research/anomaly-detection/articles/hayden2020|GALAH — Chemical Dynamics of Solar Neighborhood]]— reference chemodynamic structure for comparison with cross-sample.
- [[en/research/anomaly-detection/articles/recioblanco2014|Gaia-ESO — Fine/Spense Disk Transition]]— the context of star populations and radial migration.
- [[en/research/anomaly-detection/articles/borbolato2025|Co-formation of Fine/Spense Discs (z>2)]]— training scenario for fine disc dichotomy/expenditure.
- [[en/research/anomaly-detection/articles/tinsley1979|Star Life Times and Abundance Reasons]]— classical article of chemical evolution, theoretical basis of nucleosynthesis.
- [[en/research/anomaly-detection/articles/wallerstein1962|Abundances in Dwarfs G VI]]— historical article, one of the first systematic determinations of stellar abundance.

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
