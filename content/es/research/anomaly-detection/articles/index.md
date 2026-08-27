---
publish: false
title: "Artículos"
created: 2026-07-23
modified: 2026-07-25T23:58:08.061-03:00
published: 2026-07-25T23:58:08.061-03:00
order: 1
cssclasses:
  - page-layout
---

> [!note] Resumen
> Anotación de lectura sobre 28 artículos científicos relevantes para el proyecto [[es/research/anomaly-detection|Detección de Anomalías en Datos de Gaia]], organizadas por tema.


<div class="media-carousel">
  <a href="/pt-br/research/anomaly-detection/articles/collaboration2016" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="La Misión Gaia" />
    <div class="slide-caption">La Misión Gaia</div>
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
    <img src="/assets/illustrations/articles.svg" alt="GALAH — Clasificación vía t-SNE" />
    <div class="slide-caption">GALAH — Clasificación vía t-SNE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/lochner2021" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="ASTRONOMALY" />
    <div class="slide-caption">ASTRONOMALY</div>
  </a>
</div>


 Anotación de lectura sobre artículos científicos relevantes para mi investigación en detección de anomalías en poblaciones estelares — síntesis propias, no los artículos completos (derechos de autor de las editoriales/arXiv permanecen con los autores originales). Agrupadas por papel en el proyecto: los levantamientos y datos que uso, los métodos de aprendizaje de máquina que aplico, los modelos estelares que calibran mis edades/isócronas, y el contexto de dinámica/química galáctica que interpreta los resultados.

## 🛰️ Ingresos y catálogos (dados)

- [[es/research/anomaly-detection/articles/collaboration2016|La Misión Gaia]]— astrometría de mil millones de estrellas; fuente de las coordenadas cinemáticas del proyecto.
- [[es/research/anomaly-detection/articles/collaboration2021|Gaia EDR3 — Gaia Catalogue of Nearby Stars]]— catálogo limpio a 100 pc del Sol, base de la muestra GCNS.
- [[es/research/anomaly-detection/articles/deandrade2025|GCNS × GALAH DR4]]— mi propio artículo, el análisis conjunto que fundamenta la Etapa 1.
- [[es/research/anomaly-detection/articles/buder2025|GALAH DR4]]— 4o release de GALAH: hasta 32 elementos por estrella vía redes neuronales.
- [[es/research/anomaly-detection/articles/kos2017|GALAH — Pipeline de Reducción de datos]]— como los espectros brutos de HERMES vieron los parámetros del catálogo.
- [[es/research/anomaly-detection/articles/majewski2017|APOGEE]]— survey infrarrojo de alta resolución, usado como comparación/contexto.
- [[es/research/anomaly-detection/articles/xiang2019|LAMOST DR5 — Abundancias de 16 Elementos]]— otro survey espectroscópico de gran volumen, enfoque  data-driven  (DD-Payne).
- [[es/research/anomaly-detection/articles/quispehuaynasi2025|S-PLUS DR4 — Outliers de SED]]— detección de anomalías fotométricas en survey diferente, paralelo metodológico.

## 🤖 Aprendizado de máquina y detección de anomalías

- [[es/research/anomaly-detection/articles/traven2017|GALAH — Clasificación vía t-SNE]]— metodología base de la Etapa 2 (t-SNE sobre espectros brutos).
- [[es/research/anomaly-detection/articles/dasilva2023|silva & Smiljanic (2023) — t-SNE Quimiodinámico]]— base de la comparación entre columnas de catálogo y píxeles del espectro.
- [[es/research/anomaly-detection/articles/lochner2021|ASTRONOMALY]]— motivación de escala: por qué big data astronómico exige detección automática de anomalías.
- [[es/research/anomaly-detection/articles/ishida2021|Detección Activa de Anomalías (Time-Domain)]]—  active learning  aplicado al descubrimiento de objetos inusuales.
- [[es/research/anomaly-detection/articles/traven2019|Machine Learning para Binarias]]— revisión de métodos de ML en grandes levantamientos.
- [[es/research/anomaly-detection/articles/otar2021|GALAH — Estrellas de Líneas de Emisión]]— autoencoder que reconstró espectros para encontrar emisiones anómalas — misma familia de método de la Etapa 2.
- [[es/research/anomaly-detection/articles/hughes2022|GALAH — Estrellas Extremamente Pobres en Metais]]— ML supervisado para encontrar 54 candidatas EMP en GALAH.
- [[es/research/anomaly-detection/articles/vogrini2023|GALAH — Bandas Interestelares Difusas]]— otro ejemplo de minería de  big data  espectroscópico de GALAH.

## ⭐ Modelos estelares y edades

- [[es/research/anomaly-detection/articles/bressan2012|PARSEC — Isócronas Estelares]]— código de evolución estelar que genera las isócronas usadas en el diagrama de Kiel.
- [[es/research/anomaly-detection/articles/marigo2017|PARSEC-COLIBRI — Isócronas con fase TP-AGB]]— generación más reciente de isócronas, con fase TP-AGB detallada.
- [[es/research/anomaly-detection/articles/hayden2022|GALAH — Relojes Químicos]]— edades vía XGBoost a partir sólo de metalicidad/abundancias.
- [[es/research/anomaly-detection/articles/traven2020|GALAH — Binaria FGK]]— muestra de binarias espectroscópicas, relevante para limpiar contaminantes de la muestra.
- [[es/research/anomaly-detection/articles/thomas2024|SpectroTranslator]]— red neuronal para convertir parámetros entre surveys diferentes.

## 🌌 Dinámica y química galáctica (interpretación)

- [[es/research/anomaly-detection/articles/bovy2015|galpy]]— paquete usado para calcular órbitas y acciones, base de la cinemática del proyecto.
- [[es/research/anomaly-detection/articles/mcmillan2017|Distribución de masa y potencial de la Vía Láctea]]— el potencial galáctico usado en el galpy para integrar órbitas.
- [[es/research/anomaly-detection/articles/hayden2020|GALAH — Quimiodinámica de la vecindad solar]]— estructura quimiodinámica de referencia para comparar con la muestra cruzada.
- [[es/research/anomaly-detection/articles/recioblanco2014|Gaia-ESO — Transición Disco Fino/Espesso]]— contexto de poblaciones estelares y migración radial.
- [[es/research/anomaly-detection/articles/borbolato2025|Coformación de los discos Fino/Espesso (z>2)]]— escenario de formación para la dicotomía disco fino/espesso.
- [[es/research/anomaly-detection/articles/tinsley1979|Tiempos de vida Estelares y Razones de Abundancia]]— artículo clásico de evolución química, base teórica de la nucleósidosis.
- [[es/research/anomaly-detection/articles/wallerstein1962|Abundancias en Anãs G VI]]— artículo histórico, una de las primeras determinaciones sistemáticas de abundancia estelar.

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
