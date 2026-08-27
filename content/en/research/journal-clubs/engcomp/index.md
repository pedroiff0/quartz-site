---
publish: true
title: "ENGCOMP"
created: 2026-07-26
modified: 2026-08-01
published: 2026-08-01T20:04:04.327-03:00
cssclasses:
  - page-layout
---

> [!note] Summary
> Journal club de **Computer Engineering** of the IFF Campus Bom Jesus do Itabapoana: we choose a recent article from the arXiv, someone presents, and the rest of the conversation is to discuss what was read. This page saves what has already been discussed [[en/research/journal-clubs/engcomp/topicos|topics followed]] show you where to look for the next one.

## 👥 Join

 The whole organization happens in the email group **[engcompbji](https://groups.google.com/g/engcompbji)** — that's where the call comes from each meeting, the article of the week and who presents it.

- **Enter the group** —[subscribe by email](mailto:engcompbji+subscribe@googlegroups.com)(just send blank message) or [group on Google Groups](https://groups.google.com/g/engcompbji).
- **Suggesting an article** — anyone in the group can indicate reading, does not need to be the one to present.
- **Present** — 20 minutes are enough. The point is the discussion later, not the class.


<a class="jc-button" href="mailto:engcompbji@googlegroups.com?subject=Sugest%C3%A3o%20de%20artigo%20%E2%80%94%20Journal%20Club%20ENGCOMP&body=T%C3%ADtulo%3A%0A%0ALink%20do%20arXiv%3A%0A%0AT%C3%B3pico%20%28ex.%3A%20cs.SE%29%3A%0A%0APor%20que%20vale%20discutir%20%28duas%20ou%20tr%C3%AAs%20linhas%29%3A%0A">✉️ Sugerir um artigo para o grupo</a>


## 📚 Articles already discussed

 The table is generated from the frontmatter of the notes themselves in this folder — a new note appears on the next build alone without editing this page. View [[pt-br/research/journal-clubs#padrão-de-cada-entrada|default of each input]].

 '`base
 filters:
 and:
 'file.folder.startsWith("pt-br/research/journal-clubs/engcomp")'
 Only article notes have `arxiv`; it is what separates an entry from the pages
 support of this folder (index, topics, dashboard).
 note.arxiv
 formulas:
 article: 'link(file.path, note.title)'
 properties:
 formula. article:
 displayName: Article
 note. presenter:
 displayName: Presented
 note. authors:
 displayName: Author
 note.year:
 displayName: Year
 note. discussed:
 displayName: Discussion in
 It's okay The URL of arXiv enters as text and the Quartz turns it into external link
 Alone. Do not use link() here: it only solves internal path and transforms
 a URL in "../../https/arxiv.org/...". html() also does not serve — markup
 is escaped before reaching the cell.
 note. arxiv:
 displayName: arXiv
 views:
 type: table
 name: Articles discussed
 order:
 formula. article
 notice. host
 notice. authors
 notice. year
 notice. discussed
 notice. arxiv
 sort:
 property: note. discussed
 direction:
 '``

## 📣 Call for group

 Text ready to announce the next meeting. Copy, fill in the two gaps and send them to the group.


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

## 🔗 References and correlations

- [[en/research/journal-clubs/engcomp/topicos|Topics and where to look]]— the categories of the arXiv which the club accompanies.
- [[en/research/journal-clubs/engcomp/dashboard|Club Dashboard]]— activity per month, topic and presenter.
- [[en/research/journal-clubs|Journal Clubs — Overview]]
- [[en/research/journal-clubs/mwbr|MWBR]]
- [[en/research|Research — Overview]]

> [!abstract] Automatic translation notice
> This page was automatically translated from Portuguese using the LibreTranslate-based automated translator implemented in `tools/translate_quartz.py` (it preserves wikilinks, embeds and proper names via positional splitting). Machine translation may contain inaccuracies — the original Portuguese version is the authoritative source.
