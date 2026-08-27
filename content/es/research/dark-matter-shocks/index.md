---
publish: true
title: "Entendiendo la materia Escura a partir de Choques Extragalácticos"
created: 2023-03-01
modified: 2026-07-26T10:19:47.462-03:00
published: 2026-07-26T10:19:47.462-03:00
tags:
  - materia-escura
  - aglomerados-de-galaxias
  - iniciacao-cientifica
cssclasses:
  - page-layout
---

# 💥 Entendiendo la materia Escura a partir de Choques Extragalácticos

> [!note] Resumen
> Proyecto de Iniciación Científica Junior (CNPq/PIBIC-EM, Edital 94/2022), orientado por [Prof.a Ana Cecília Soja ](https://integra.iff.edu.br/p/ana-cecilia-soja) en el IFF Bom Jesus do Itabapoana. Testi la exactitud del código de Dawson et al. (2013) —que estima el tiempo transcurrido desde la colisión de dos cúmulos de galaxias vía Monte Carlo— contra las simulaciones dinámicas de ZuHone et al. (2018), como forma indirecta de estudiar el comportamiento de la materia oscura durante colisiones extremas.


<div class="media-carousel">
  <a href="/pt-br/research/dark-matter-shocks" class="carousel-slide">
    <img src="/assets/illustrations/cosmologia.svg" alt="Choques de cúmulos de galaxias" />
    <div class="slide-caption">Choques de Aglomerados</div>
  </a>
</div>


## 🌌 El problema: ¿cómo "ver" la materia oscura?

 Aglomerados de galaxias son las mayores estructuras gravitacionalmente ligadas del universo, y, cuando dos de ellos coliden, el evento es uno de los más energéticos conocidos. En una colisión, los tres componentes de un cúmulo (galáxias, gas intraaglomerado y materia oscura) se comportan de formas diferentes: las galaxias, hechas de materia normal pero muy esparsas entre sí, se cruzan casi sin interactuar; el gas, también materia normal, colide y es freado por fricción; y la materia oscura parece acompañar las galaxias, pero no exactamente — evidencia indirecta de que interactúa poco (o nada) por vías más allá de la gravedad. El ejemplo más famoso es el **Aglomerado de Bala**, cuyas mapas de lentes gravitacionales muestran exactamente esa separación espacial entre los tres componentes.

 Como no es posible observar directamente la materia oscura, ni repetir una colisión de cúmulos en laboratorio, la estrategia adoptada es indirecta: comparar **simulaciones dinámicas**con**métodos estadísticos de estimación de parámetros observacionales** (masas relativas, redshift, separación proyectada) y verificar si están de acuerdo.

## 🎯 Objetivo

 Evaluar la **acurácia**del código de**Dawson (2013)**— que utiliza el método de Monte Carlo para estimar el tiempo transcurrido desde la primera colisión de un par de cúmulos, a partir de parámetros observacionales relativamente simples de obtener — comparando sus resultados con el "gabarito" conocido de las simulaciones dinámicas de alta resolución de**ZuHone et al. (2018)**.

## 🔧 Metodología

 El trabajo siguió cuatro etapas:

1. **Familiarización** con conceptos fundamentales de Astronomía (paralaxe, clasificación espectral OBAFGKM, evolución estelar, clasificación morfológica de galaxias de Hubble — elípticas, espirales, irregulares) y con el problema físico de aglomerados en colisión.
2. *Compilación y entendimiento del código de Dawson** — validado primero contra el caso de referencia del propio Aglomerado de Bala (masas $1{,}5\times10^{14}$ y $1{,}5\times10^{15}\,M \odot$, separación proyectada de 720 kpc), reproduciendo el resultado original. La función central, `MCEngine`, recibe masas de los dos cúmulos, redshift y distancia proyectada, y genera $10^4$ muestras vía Monte Carlo (convergencia ya observada a partir de $10^3$ iteraciones).
3. *Obtención de los datos de ZuHone et al. (2018)** — o  Galaxy Cluster Merger Catalog , un repositorio de simulaciones hidrodinámicas de fusiones de cúmulos, organizado por razón de masa (1:1, 1:3, 1:10) y parámetro de impacto (0,500, 1000 kpc). El trabajo se centró en las 3 simulaciones con parámetro de impacto 0 kpc (cosión en el plano del cielo).
4. **Aplicación del método de Dawson** a cada una de las simulaciones de ZuHone, comparando el tiempo post-cosión estimado por el código con el tiempo real conocido de la simulación, con incertidumbre estimada vía `np.quantile` sobre las $10^4$ muestras de Monte Carlo.

## 📊 Resultados

 La simulación de ZuHone revela un patrón oscilatorio: los cúmulos parten de separación máxima, coliden (línea negra, primera colisión), vuelven a alejarse hasta un nuevo máximo — menor que el primero, por pérdida de energía en la colisión— y así sucesivamente.

| Razón de masas | Instante de la 1a colisión (Ganos) |
|---|---|
| 1:1 | 1,32 |
| 1:3 | 1,20 |
| 1:10 | 1,04 |

 Comparando el código de Dawson con los datos de ZuHone en el intervalo entre la primera colisión y el alejamiento máximo siguiente — la única ventana en la que se aplica el método de Dawson — los resultados del código **concordam, dentro de las incertidumbres, con la simulación para las tres razones de masa comprobadas (1:1, 1:3 y 1:10)**.

> [!warning] Viés sistemático encontrado
> A pesar de la buena concordancia general, los valores centrales estimados por el código de Dawson mostraron una **tendencia sistemática a subestimar** el tiempo real de la simulación — un sesgo que necesita ser investigado con más profundidad en trabajos futuros, y que no invalida la viabilidad general del método.

## 🧾 Conclusión

 El método de Dawson (2013) se mostró **confiable dentro de las incertidumbres** para estimar el tiempo transcurrido desde la colisión de cúmulos de galaxias, en el intervalo de validez propuesto por el propio método, pero con una tendencia sistemática de subestimación que merece investigación futura. La perspectiva natural es ampliar el análisis para los escenarios de ZuHone con parámetro de impacto nonulo (cosiones fuera del plano del cielo), aún no probados en este trabajo.

## 🏆 Presentaciones y premios

 Este proyecto fue presentado en la **[[es/media/2023/febrace-2023|FEBRACE 2023]]**y**[[es/media/2023/mostratec-2023|MOSTRATEC 2023]]** (Novo Hamburgo, RS).

## 🔗 Referencias y correcciones

- Dawson, W. A. (2013) —  The Dynamics of Merging Clusters: La Monte Carlo Solution Applied to the Bullet and Musket Ball Clusters , ApJ 772, 131.[Anuncio Artículo completo (arXiv)](/assets/articles/Dawson2013.pdf)·[Código MCMAC](https://github.com/MCTwo/MCMAC).
- ZuHone, J. et al. (2018) —  The Galaxy Cluster Merger Catalog: An Online Repository of Mock Observations from Simulated Galaxy Cluster Mergers , ApJS 234, 4.[Anuncio Artículo completo (arXiv)](/assets/articles/ZuHone2018.pdf).
- Clowe, D. et al. — Aglomerado de Bala, evidencia clásica de separación espacial entre materia oscura y gas.
- [[es/media/2023/mostratec-2023|MOSTRATEC 2023]]— cobertura de la presentación de este proyecto
- [[es/research/anomaly-detection|Detección de Anomalías en Datos de Gaia]]— otro proyecto de investigación en Astronomía, también orientado por dinámica/cinemática de sistemas gravitacionales
- [[es/research/satellite-trail-removal|Simulando el Impacto de Satélites en Observaciones Astronómicas]]— proyecto siguiente, también con enfoque computacional aplicado a datos astronómicos
- [[pt-br/resource/curso-on/aula-05-avermelhamento-extincao-e-imf|Curso ON — Clase 05]]— otro contexto de masa no-luminosa/materia oscura en la Galaxia

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
