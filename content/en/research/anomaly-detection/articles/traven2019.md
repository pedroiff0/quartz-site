---
publish: false
title: Machine Learning para Binárias
created: 2026-07-18
modified: 2026-07-25T23:58:08.057-03:00
published: 2026-07-25T23:58:08.057-03:00
tags:
  - artigo
  - pesquisa
cssclasses:
  - page-layout
---

> [!note] In short
> Review that organizes the machine learning taxonomy (supervised/unsupervised, discriminative/generative) and applies this tool to the discovery and characterization of spectroscopic binary stars in half a million spectra of the GALAH survey.

 Traven, G. et al. (2019) 

## Summary

 Review that organizes the "zoological" of LM techniques in two axes: supervised vs. unsupervised and, within the supervised, discriminative (data map→network directly — logistic regression, S.V.M., random forests) vs. generative (produces from the label — GANs, variational autoencoders). The article applies this tool to a concrete problem: finding spectroscopic binary stars (SB2/SB3) in ~587 thousand spectra of the GALAH survey.

 In the unsupervised part, the authors test a self-encoder to reduce the dimensionality of the spectra to a 2D map — the result does not separate the classes in a useful way. They switch to t-SNE, which reveals a rich structure: clusters that correspond, without any prior label, to binary, metal-poor giants, fast-rotating hot stars and molecular bands. The clustering algorithm DBSCAN then isolates each group automatically from the map. Comparing this unsupervised detection with the classical method (cross-correlation function, CCF), they show that the two are complementary — each finds binary that the other loses.

 In the generative (supervised) part, they use The Cannon and The Payne to build, from known labels (temperature, gravity, metallicity), a single star spectrum data-driven model; by adding two of these model spectra, they generate a binary template and adjust it to the observed data—which allows us to identify even unresolved spectroscopic binary, whose orbital velocity does not separate the lines. The central conclusion of the article, and perhaps the most important for those who are learning ML: human intervention remains indispensable, because instrumental effects and data reduction can mimic the signature of a binary and deceive the algorithm. It is the methodological basis of the anomaly detection project of this site (learning patterns in stellar data) and also a good introductory material of applied ML, referenced on the page of [[pt-br/resource/computacao/machine-learning|Machine Learning]].

 [See original article](https://ui.adsabs.harvard.edu/abs/2019MmSAI..90..327T)

## Quotation

 ``bibtex
 @ARTICLE{Traven2019,
 author = {{Traven}, G. and {{\v{C}}}, K. and {Merle}, T. and {Van der Swaelmen}, M. and {Ting}, Y.-S. and {GALAH Team},
 title = "{Machine learning techniques meet binaries}",
 journal = {\memsai},
 keywords = {Stars: binaries: close, Stars: binaries: spectroscopic, methods: data analysis, methods: numerical, techniques: radial speeds, techniques: spectroscopic},
 year = 2019,
 month = jan,
 volume = {90},
 pages = {327},
 adsurl = {https://ui.adsabs.harvard.edu/abs/2019MmSAI..90..327T},
 adsnote = {Provided by the SAO/NASA Astrophysics Data System}
 }
 '``

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
