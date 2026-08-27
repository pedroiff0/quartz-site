---
publish: true
title: "ENGCOMP"
created: 2026-07-26
modified: 2026-08-01
published: 2026-08-01T20:04:04.327-03:00
cssclasses:
  - page-layout
---

> [!note] Resumen
> Journal club de **Engenharia de Computación** del IFF Campus Bom Jesus do Itabapoana: nosotras elegimos un artículo reciente del arXiv, alguien presenta, y el resto de la conversación es discutir lo que fue leído. Esta página guarda lo que ya se ha discutido; los [[es/research/journal-clubs/engcomp/topicos|tópicos acompañados]] muestran dónde buscar el próximo.

## 👥 Participe

 La organización sucede en el grupo de correo electrónico **[engcompbji](https://groups.google.com/g/engcompbji)** es por ahí que sale la llamada de cada encuentro, el artículo de la semana y quien presenta.

- **Entrar en el grupo** —[inscriba por correo electrónico](mailto:engcompbji+subscribe@googlegroups.com)(basta enviar el mensaje en blanco) o por [grupo en Google Groups](https://groups.google.com/g/engcompbji).
- **Sugerir un artículo** — cualquier persona del grupo puede indicar lectura, no necesita ser quien va a presentar.
- **Mostrar** — 20 minutos bastan. El objetivo es la discusión después, no la clase.


<a class="jc-button" href="mailto:engcompbji@googlegroups.com?subject=Sugest%C3%A3o%20de%20artigo%20%E2%80%94%20Journal%20Club%20ENGCOMP&body=T%C3%ADtulo%3A%0A%0ALink%20do%20arXiv%3A%0A%0AT%C3%B3pico%20%28ex.%3A%20cs.SE%29%3A%0A%0APor%20que%20vale%20discutir%20%28duas%20ou%20tr%C3%AAs%20linhas%29%3A%0A">✉️ Sugerir um artigo para o grupo</a>


## 📚 Artículos ya discutidos

 La tabla se genera a partir del frontmatter de las propias notas de esta carpeta — una nota nueva aparece sola en el siguiente build, sin editar esta página. Ver el [[pt-br/research/journal-clubs#padrão-de-cada-entrada|patrón de cada entrada]].

 ``base
 filters:
 and:
 'file.folder.startsWith("pt-br/research/journal-clubs/engcomp")'
 Sólo notas de artículo tienen `arxiv`; es lo que separa una entrada de las páginas
 de apoyo de esta carpeta (index, topicos, dashboard).
 note.arxiv
 formulaciones:
 artículo: 'link(file.path, note.title)'
 properties:
 formula. artículo:
 displayName: Artículo
 note. presentador:
 displayName: Apresentó
 note. authors:
 displayName: Autor
 note.year:
 displayName: Año
 note. discutido:
 displayName: Discutido en
 La URL arXiv entra como texto y el Quartz la transforma en enlace externo
 solo. No usar enlace() aquí: solo resuelve el camino interno y transforma
 una URL en "../../https/arxiv.org/...". html() tampoco sirve — markup
 se escapa antes de llegar a la célula.
 note. arxiv:
 displayName: arXiv
 vistas:
 -type: table
 name: Artículos discutidos
 order:
 formula. artículo
 note. presentador
 note. authors
 note. year
 note. discutido
 note. arxiv
 sort:
 property: note. discutido
 direction: DESC
 ````

## 📣 Llamada al grupo

 Texto listo para anunciar el próximo encuentro. Copie, rellene las dos lagunas y envíe en el grupo.


<div class="jc-digest">
  <pre id="jc-digest-texto">Pessoal, próximo encontro do Journal Club de Engenharia de Computação.

📅 Quando: \[DIA E HORA]
📄 Artigo: \[TÍTULO + LINK DO ARXIV]

Quem quiser sugerir leitura para as próximas semanas, os tópicos que acompanhamos estão aqui:
https://www.phrandrade.com[[pt-br/research/journal-clubs/engcomp/topicos|Topicos]]

O histórico do que já discutimos fica em:
https://www.phrandrade.com[[pt-br/research/journal-clubs/engcomp|Engcomp]]

Até lá!</pre> <button type="button" class="jc-button" id="jc-digest-copiar">📋 Copiar texto</button>

</div>



<script>
(function () {
  var btn = document.getElementById("jc-digest-copiar");
  var pre = document.getElementById("jc-digest-texto");
  if (!btn || !pre) return;
  btn.addEventListener("click", function () {
    navigator.clipboard.writeText(pre.textContent).then(
      function () {
        btn.textContent = "✅ Copiado!";
        setTimeout(function () { btn.textContent = "📋 Copiar texto"; }, 2000);
      },
      function () {
        btn.textContent = "Não deu — copie manualmente";
      }
    );
  });
})();
</script>


 ---

## 🔗 Referencias y correcciones

- [[es/research/journal-clubs/engcomp/topicos|Temas y dónde buscar]]— las categorías del arXiv que el club acompaña.
- [[es/research/journal-clubs/engcomp/dashboard|Dashboard del club]]— actividad por mes, tópico y presentador.
- [[es/research/journal-clubs|Journal Clubs — visión general]]
- [[es/research/journal-clubs/mwbr|MWBR]]
- [[es/research|Investigación — visión general]]

> [!abstract] Aviso de traducción automática
> Esta página fue traducida automáticamente del portugués utilizando el traductor automático basado en LibreTranslate implementado en `tools/translate_quartz.py` (que preserva wikilinks, embeds y nombres propios mediante división posicional). Es traducción automática y puede contener imprecisiones — la versión original en portugués es la fuente autoritativa.
