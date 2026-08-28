---
publish: true
title: ENGCOMP
created: 2026-07-26 13:33
modified: 2026-08-27 13:33
published: 2026-08-01T20:04:04.327-03:00
cssclasses:
  - page-layout
---

> [!note] Resumo
> Journal club de **Engenharia de Computação** do IFF Campus Bom Jesus do Itabapoana: a gente escolhe um artigo recente do arXiv, alguém apresenta, e o resto da conversa é discutir o que foi lido. Esta página guarda o que já foi discutido; os [[pt-br/research/journal-clubs/engcomp/topicos|tópicos acompanhados]] mostram onde procurar o próximo.

## 👥 Participe

A organização acontece toda no grupo de e-mail **[engcompbji](https://groups.google.com/g/engcompbji)** — é por lá que sai a chamada de cada encontro, o artigo da semana e quem apresenta.

- **Entrar no grupo** — [inscreva-se por e-mail](mailto:engcompbji+subscribe@googlegroups.com) (basta enviar a mensagem em branco) ou pelo [grupo no Google Groups](https://groups.google.com/g/engcompbji).
- **Sugerir um artigo** — qualquer pessoa do grupo pode indicar leitura, não precisa ser quem vai apresentar.
- **Apresentar** — 20 minutos bastam. O objetivo é a discussão depois, não a aula.

<a class="jc-button" href="mailto:engcompbji@googlegroups.com?subject=Sugest%C3%A3o%20de%20artigo%20%E2%80%94%20Journal%20Club%20ENGCOMP&body=T%C3%ADtulo%3A%0A%0ALink%20do%20arXiv%3A%0A%0AT%C3%B3pico%20%28ex.%3A%20cs.SE%29%3A%0A%0APor%20que%20vale%20discutir%20%28duas%20ou%20tr%C3%AAs%20linhas%29%3A%0A">✉️ Sugerir um artigo para o grupo</a>

## 📚 Artigos já discutidos

A tabela é gerada a partir do frontmatter das próprias notas desta pasta — uma nota nova aparece sozinha no próximo build, sem editar esta página. Ver o [[pt-br/research/journal-clubs#padrão-de-cada-entrada|padrão de cada entrada]].

```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/research/journal-clubs/engcomp")'
    # Só notas de artigo têm `arxiv`; é o que separa uma entrada das páginas
    # de apoio desta pasta (index, topicos, dashboard).
    - 'note.arxiv'
formulas:
  artigo: 'link(file.path, note.title)'
properties:
  formula.artigo:
    displayName: Artigo
  note.apresentador:
    displayName: Apresentou
  note.authors:
    displayName: Autoria
  note.year:
    displayName: Ano
  note.discutido:
    displayName: Discutido em
  # A URL do arXiv entra como texto e o Quartz a transforma em link externo
  # sozinho. Não usar link() aqui: ele só resolve caminho interno e transforma
  # uma URL em "../../https/arxiv.org/...". html() também não serve — o markup
  # é escapado antes de chegar na célula.
  note.arxiv:
    displayName: arXiv
views:
  - type: table
    name: Artigos discutidos
    order:
      - formula.artigo
      - note.apresentador
      - note.authors
      - note.year
      - note.discutido
      - note.arxiv
    sort:
      - property: note.discutido
        direction: DESC
```

## 📣 Chamada para o grupo

Texto pronto para anunciar o próximo encontro. Copie, preencha as duas lacunas e mande no grupo.

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

## 🔗 Referências e correlatos

- [[pt-br/research/journal-clubs/engcomp/topicos|Tópicos e onde procurar]] — as categorias do arXiv que o clube acompanha.
- [[pt-br/research/journal-clubs/engcomp/dashboard|Dashboard do clube]] — atividade por mês, tópico e apresentador.
- [[pt-br/research/journal-clubs|Journal Clubs — visão geral]]
- [[pt-br/research/journal-clubs/mwbr|MWBR]]
- [[pt-br/research|Pesquisa — visão geral]]
