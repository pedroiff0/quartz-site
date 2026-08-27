---
publish: false
title: "Machine Learning para Binarias"
created: 2026-07-18
modified: 2026-07-25T23:58:08.057-03:00
published: 2026-07-25T23:58:08.057-03:00
tags:
  - artigo
  - pesquisa
cssclasses:
  - page-layout
---

> [!note] En resumen
> Revisión que organiza la taxonomía de machine learning (supervisionado/no supervisado, discriminativo/generativo) y aplica ese herramiental al descubrimiento y caracterización de estrellas binarias espectroscópicas en medio millón de espectros del levantamiento GALAH.

 Traven, G. et al. (2019) 

## Síntesis

 Revisión que organiza el "zoológico" de técnicas de ML en dos ejes: supervisado vs. no supervisado y, dentro del supervisado, discriminativo (mapeia dado→rótulo directamente — regresión logística, SVM, bosques aleatorios) vs. generativo (produz dado a partir de la etiqueta — GANs, autoencoders variacionales). El artículo aplica este instrumento a un problema concreto: encontrar estrellas binarias espectroscópicas (SB2/SB3) en ~587 mil espectros del levantamiento GALAH.

 En la parte no supervisada, los autores testan un autoencoder para reducir la dimensionalidad de los espectros a un mapa 2D — el resultado no separa las clases de forma útil. Cambian a t-SNE, que revela una estructura rica: aglomerados que corresponden, sin ninguna etiqueta previa, a binarias, gigantes pobres en metales, estrellas calientes de rotación rápida y bandas moleculares. El algoritmo de clúster DBSCAN aisla cada grupo automáticamente desde el mapa. Comparando esta detección no supervisada con el método clásico (función de correlación cruzada, CCF), muestran que los dos son complementarios, cada uno encuentra binarias que el otro pierde.

 En la parte generativa (supervisionada), usan The Cannon y The Payne para construir, a partir de etiquetas conocidas (temperatura, gravedad, metalicidad), un modelo data-driven del espectro de una estrella soltera; sumando dos de esos espectros-modelo, generan una plantilla de binaria y lo ajustan a los datos observados — lo que permite identificar hasta binarias espectroscopicamente no resueltas, cuya velocidad orbital no separa las líneas. La conclusión central del artículo, y tal vez la más importante para quien está aprendiendo ML: intervención humana sigue siendo indispensable, porque efectos instrumentales y de reducción de datos pueden imitar la firma de una binaria y engañar el algoritmo. Es la base metodológica del proyecto de detección de anomalías de este sitio web (aprendizado de patrones en datos estelares) y también un buen material introductorio de ML aplicado, referenciado en la página de [[pt-br/resource/computacao/machine-learning|Machine Learning]].

 [Véase el artículo original](https://ui.adsabs.harvard.edu/abs/2019MmSAI..90..327T)

## Citación

 `bibtex
 @ARTICLE{Traven2019,
 author = {{Traven}, G. and {{\v{C}}otar}, K. and {Merle}, T. and {Van der Swaelmen}, M. and {Ting}, Y.-S. and {GALAH Team}},
 title = "{Machine learning techniques meet binaries}",
 journal = {\memsai},
 keywords = {Stars: binaries: close, Stars: binaries: spectroscopic, methods: data analysis, methods: numerical, techniques: radial velocities, techniques: spectroscopic},
 year = 2019,
 month = jan,
 volumen = {90},
 pages = {327},
 adsurl = {https://ui.adsabs.harvard.edu/abs/2019MmSAI..90..327T},
 adsnote = {Provided by the SAO/NASA Astrophysics Data System}
 }
 ````

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
