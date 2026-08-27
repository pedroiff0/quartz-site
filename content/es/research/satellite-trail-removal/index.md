---
publish: true
title: "Simulando el Impacto de Satélites en Observaciones Astronómicas"
created: 2024-03-06
modified: 2026-07-26T10:19:39.079-03:00
published: 2026-07-26T10:19:39.079-03:00
tags:
  - poluicao-luminosa
  - satelites-artificiais
  - processamento-de-imagens
  - iniciacao-cientifica
cssclasses:
  - page-layout
---

# 🛰️ Simulando el Impacto de Satélites en Observaciones Astronómicas

> [!note] Resumen
> Proyecto de investigación (IFF Bom Jesus do Itabapoana, orientación de [Prof.a Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja)) sobre cómo la proliferación de satélites artificiales contamina imágenes astronómicas con rastros luminosos — y cómo tratar esa contaminación computacionalmente. En equipo con [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) y Arthur Miguelito Lopes, el proyecto evolucionó de un 3o lugar en [[es/media/2024/febic-2024|FEBIC 2024]] incluso un algoritmo capaz de recuperar el 99,7% de la información perdida, galardonado en 1o lugar en [[es/media/2025/mctia-2025|MCTIA 2025]].


<div class="media-carousel">
  <a href="/pt-br/research/satellite-trail-removal" class="carousel-slide">
    <img src="/assets/illustrations/informatica.svg" alt="Eliminación de rastros de satélite en imágenes astronómicas" />
    <div class="slide-caption">Contaminación Luminosa por Satélites</div>
  </a>
</div>


## 🌠 El problema

 La década de 2020-2030 trae una nueva generación de telescopios (Vera Rubin, GMT, Euclid) que multiplicará por más de mil el volumen y la calidad de los datos astronómicos disponibles. En paralelo, sin embargo, la popularización de **constelaciones de satélites comerciales** está pobladando la órbita terrestre de miles de objetos brillantes, que se interponen entre los telescopios y la luz de las estrellas — contaminando imágenes con rastros luminosos y amenazando degradando justamente la nueva generación de levantamientos astronómicos de gran volumen.

 A diferencia de las dos barreras históricas de la observación astronómica (clima y limitación instrumental), esta es una contaminación **artificial**, aún mal cuantificada: el brillo de cada satélite depende de posición, altitud y longitud de onda de forma compleja, y la comunidad internacional (astrónomos, ingenieros, defensores del cielo oscuro) se ha movilizado para desarrollar herramientas open source de tratamiento de imagen.

## 🎯 Objetivos

- Desarrollar un método de tratamiento de imagen capaz de **identificar contaminación por satélite** en observaciones astronómicas.
- Prueba ese método en **objetos astronómicos simulados**, con contaminación controlada, evaluando aplicabilidad y eficiencia.
- Sumando esfuerzos al movimiento internacional por soluciones open source para el problema de la contaminación luminosa orbital.

## 🔧 Metodología

 El proyecto fue planificado en 5 fases: (1) revisión sistemática del problema y de códigos ya existentes; (2) elaboración de un objeto astronómico simulado (preferencialmente una galaxia); (3) construcción de un código de análisis/tratamiento de imagen; (4) aplicación del código al objeto simulado, con contaminación luminosa controlada (simulación de rastros de satélite); (5) análisis de los resultados.

## 📈 Evolución y resultados

| Paso | Evento | Salida |
|---|---|---|
| Propuesta inicial | Edital de preiniciación científica, IFF (2023) | Aprobación del proyecto |
| **[[es/media/2024/febic-2024|FEBIC 2024]]**(Pomerode, SC) | Com [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/)  |**3o lugar — categoría Grado**, incluso con el proyecto todavía incompleto, compitiendo con aplicaciones ya patentadas — resultado que clasificó el equipo para el [[es/media/2025/mctia-2025|MCTIA 2025]]  |
| **[[es/media/2025/mctia-2025|MCTIA 2025]]**(Belém, PA) | Com [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) arthur Miguelito Lopes |**1o lugar — categoría Ciencias Exatas de Enseñanza Superior**, con un algoritmo de IA capaz de**remover rastros de satélite de datos astronómicos, recuperando 99,7% de la información que sería perdida** — resultado que clasificó el equipo para el evento nacional Ciencia Joven (Recife, PE, 2026) |

> [!note] Nota sobre este texto
> Esta página combina la propuesta formal de investigación (submetida al IFF en 2023, con introducción, justificación y metodología completas) con los resultados divulgados públicamente en las premiaciones de la FEBIC 2024 y del MCTIA 2025. Detalles técnicos del algoritmo de recuperación del 99,7% todavía no han sido documentados en esta página — actualizar según el trabajo avanza para publicación.

## 🔗 Referencias y correcciones

- Milazzo et al. (2021) —  The Growing Digital Divide and its Negative Impacts on NASA's Future Workforce , BAAS 53, 436
- Rawls et al. (2020) —  Satellite Constellation Internet Affordability and Need , RNAAS 4, 189
- Venkatesan et al. (2020) —  The Impact of Satellite Constellations on Space as an Ancestral Global Commons , Nature Astronomy 4, 1043
- [[es/media/2024/febic-2024|FEBIC 2024]]— cobertura de la presentación y del 3o lugar
- [[es/media/2025/mctia-2025|MCTIA 2025]]— cobertura de la presentación y del primer lugar
- [[es/research/dark-matter-shocks|Entendiendo la materia Escura a partir de Choques Extragalácticos]]— proyecto anterior, mismo orientadora
- [[es/research/anomaly-detection|Detección de Anomalías en Datos de Gaia]]— otro proyecto centrado en el aprendizaje de máquina aplicado a datos astronómicos

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
