---
publish: true
title: "\"ReLaTeX: Clase LaTeX para Trabajos Académicos del IFF\""
created: 2026-06-18
modified: 2026-07-31T23:45:03.282-03:00
published: 2026-07-31T23:45:03.282-03:00
tags:
  - latex
  - engenharia-de-software
  - automacao
cssclasses:
  - page-layout
---

# 📄 ReLaTeX: Clase LaTeX para Trabajos Académicos de IFF

> [!note] Resumen
> Desarrollo de la clase tipográfica `ifftese. cls` y el paquete de extensión `macros.sty` para LaTeX, con el objetivo de automatizar el cumplimiento de las normas ABNT (NBR 14724, NBR 6027) en trabajos académicos del Instituto Federal Fluminense — reduciendo drásticamente el tiempo gastado formando manualmente capas, tablas, figuras y elementos pre/posituales. A ser presentado en el CONEPE 2026 (Campos Guarus, RJ, 21 al 23 de septiembre), en coautoría con [Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja),[Maria Luiza Linhares Dantas](https://www.mlldantas.com) y [Ana Mara Figueiredo de Oliveira](https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora)


<div class="media-carousel">
  <a href="/pt-br/research/relatex" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="ReLaTeX" />
    <div class="slide-caption">Clase LaTeX ifftese. cls</div>
  </a>
</div>


## 🌌 El problema

 La redacción de documentos académicos bajo las directrices de la ABNT (NBR 14724 para trabajos académicos, NBR 6023 para referencias, NBR 6027 para resúmenes) impone una estructura rígida, pero LaTeX — la herramienta más indicada técnicamente para eso, por su control tipográfico y ambiente de ecuaciones superior a procesadores visuales como Word— tiene una curva de aprendizaje alta. La diferencia de paradigma explica por qué: procesadores WYSIWYG ("lo que ves es lo que tienes") son fáciles de empezar pero difíciles de diagramar sin romper el diseño; LaTeX es WYSIWYM ("lo que ves es lo que quieres decir") — el iniciante erra bastante y depende de consulta constante, pero, superada la curva de aprendizaje, gana un proceso de escritura mucho más confiable y alineado a las normas.

## 🎯 Objetivo

 Desarrollar una clase tipográfica para LaTeX dirigida al usuario típico del IFF, que respete las directrices de la ABNT y las particularidades locales (logos y símbolos institucionales), atenuando la curva de aprendizaje de quien nunca usó LaTeX y agilizando el trabajo de quien ya usa.

## 🔧 Metodología

 El proyecto utilizó como base las clases `abntex2` y `article`, con el paquete bibliográfico `abntex2cite` (compatibilidad ABNT), compilado vía TeX Live (`pdflatex`/`bibtex`), con apoyo de TeXPage, CTAN y Overleaf como ambientes online. El trabajo fue dividido en tres etapas:

1. **Normas** — mapeo de las restricciones visuales y estructurales de la NBR 14724 y NBR 6027, traducidas en la clase `ifftese. cls`.
2. **Comandos auxiliares** — el paquete `macros.sty`, creado para evitar la sintaxis primitiva de LaTeX y reducir errores de compilación.
3. **Archivo principal** — consolidación en un único `main.tex`, con todos los ambientes de la NBR 14724 ya llenados como comandos listos.

## 📊 Resultados

 La arquitectura sigue la estructura normativa de ABNT (elementos pretextuales, textuales y posttextuales), eliminando la necesidad de que el usuario manipule paquetes gráficos o formateo complejo directamente:

- **Variables de control** (`\frenteVerso`, `\corlink`, `\sumarioEscada`, `\numeracaoPorSecao`, `\capaiff`, `\legendacurta`, `\cabecalho`) — flags sí/no que generan automáticamente márgenes, cabeceras, enlaces y numeración correctos.
- *Elementos pretextuales ** — variables semánticas (`\autor`, `\titulo`, `\orientador`, `\local`, `\instituicao`, `\data`) alimentan macros como `\capa` y `\contracapa`, que rinden páginas completas ya formatadas conforme a la norma.
- *Elementos textuales** — la macro `\inserirfigura` encapsula, en una sola línea, el dimensionamiento, alineación, subtítulos, fuente y etiqueta (`label`) para referencia cruzada de una figura. `\inserirtabela` y `\inserir marco` automatización la distinción normativa del IBGE entre tablas y cuadros, enviando los metadatos directamente a las listas de pretexto.
- *Elementos posttextuales ** — macros propias convierten la numeración de apéndices/anexos de numérica para alfabético sin corromper la numeración de los capítulos, y estandarizaron la llamada de glosarios e índices remisivos.

## 🧾 Conclusión

 El encapsulamiento de esas rutinas en macros parametrizadas cumplió el objetivo: reducir el tiempo operativo de formatación y democratizar el rigor tipográfico de LaTeX en la producción técnico-científica del IFF, blindando al usuario contra errores de sintaxis y referencias cruzadas. Como desdoblamiento, está en fase de pruebas una interfaz web opcional, en el estilo de Overleaf, centrada exclusivamente en esta clase, pensada para quien prefiere rellenar formularios a editar código fuente directamente.

## 🏆 Mostrar

 Este proyecto será presentado en el **CONEPE 2026** (Congreso de Enseñanza, Investigación y Extensión del IFF  Campus  Guarus), del 21 al 23 de septiembre de 2026.

## 🔗 Referencias y correcciones

- ASOCIACIÓN BRASILERA DE NORMAS TÉCNICAS. NBR 14724: Información y documentación — Trabajos académicos — Presentación. Río de Janeiro, 2011.
- ASOCIACIÓN BRASILERA DE NORMAS TÉCNICAS. NBR 6027: Información y documentación — Resumen — Presentación. Río de Janeiro, 2012.
- KNUTH, D. E.  The TeXbook . Reading, Massachusetts: Addison-Wesley, 1986.
- LAMPORT, L.  LaTeX: Document Preparation System . 2a ed. Reading, Massachusetts: Addison-Wesley, 1994.
- EQUIPE ABNTEX2 —[la clase abntex2](https://github.com/abntex/abntex2), base de compatibilidad ABNT usada en este proyecto.
- CONEPE 2026 — la cobertura de la presentación entra aquí después del evento (septiembre de 2026).
- [[pt-br/resource/latex|LaTeX y Escritura Académica]]— el curso construido sobre este proyecto; las clases 06 a 08 documentan `ifftese. cls`, `macros.sty` y `metadados. sty` línea a línea.
- [[pt-br/resource/latex/modelos-corporativos|Modelos Corporativos]]— la misma arquitectura de clase aplicada fuera de la academia, con manual de marca en el lugar de la ABNT.

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
