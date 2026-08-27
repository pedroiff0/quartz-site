---
publish: true
title: "ENGCOMP"
created: 2026-07-26
modified: 2026-08-01
published: 2026-08-01T20:04:04.327-03:00
cssclasses:
  - page-layout
---

> [!note] Résumé
> Journal club de **Engenharia ordinateur** de IFF Campus Bom Jesus do Itabapoana: nous avons choisi un article récent de l'arXiv, quelqu'un présente, et le reste de la conversation est de discuter de ce qui a été lu. Cette page conserve ce qui a déjà été discuté [[fr/research/journal-clubs/engcomp/topicos|sujets accompagnés]] montrez où chercher le prochain.

## 👥 Participation

 L'organisation se produit dans le groupe de courriels **[engcompbji](https://groups.google.com/g/engcompbji)** c'est là que l'appel de chaque réunion, l'article de la semaine et qui présente.

- *Entrez dans le groupe* * -[inscription par courriel](mailto:engcompbji+subscribe@googlegroups.com)(il suffit d'envoyer le message vide) ou par [groupe Google](https://groups.google.com/g/engcompbji).
- *Proposez un article* * - toute personne du groupe peut indiquer la lecture, n'a pas besoin d'être celle à présenter.
- *Montrer* * - 20 minutes assez. L'objectif est la discussion plus tard, pas la classe.


<a class="jc-button" href="mailto:engcompbji@googlegroups.com?subject=Sugest%C3%A3o%20de%20artigo%20%E2%80%94%20Journal%20Club%20ENGCOMP&body=T%C3%ADtulo%3A%0A%0ALink%20do%20arXiv%3A%0A%0AT%C3%B3pico%20%28ex.%3A%20cs.SE%29%3A%0A%0APor%20que%20vale%20discutir%20%28duas%20ou%20tr%C3%AAs%20linhas%29%3A%0A">✉️ Sugerir um artigo para o grupo</a>


## 📚 Articles déjà examinés

 La table est générée à partir de la matière première des notes de ce dossier lui-même - une nouvelle note apparaît seule dans la prochaine construction, sans modifier cette page. Voir [[pt-br/research/journal-clubs#padrão-de-cada-entrada|modèle de chaque entrée]].

 "base
 filtres:
 et:
 'file.folder.startsWith ("pt-br / research / journal-clubs / engcomp")'
 ♪ Seules les notes d'article ont 'arxiv' ; c'est ce qui sépare une entrée des pages
 prise en charge de ce dossier (index, sujets, tableau de bord).
 note.arxiv
 formulations:
 article: 'lien (file.path, note.title)'
 propriétés:
 formule. objet:
 nom d'affichage : article
 remarque :
 nom d'affichage & #160;:
 note autorisée:
 displayName: Auteur
 note: année:
 nom d'affichage: Année
 note examinée:
 displayName : discuté dans
 L'URL arXiv entre comme texte et le quartz le transforme en lien externe
 Seul. Ne pas utiliser le lien () ici : résout seulement le chemin intérieur et transforme
 une URL dans.. "/.. / https / arxiv.org /..." html () ne sert pas non plus - balisage
 il s'en va avant d'arriver au portable.
 note:
 nom d'affichage : arXiv
 vues:
 type: tableau
 nom: articles discutés
 ordre:
 formule. le président
 remarque
 note : autorisée
 note : année
 remarque
 remarque. arxiv
 tri:
 propriété: note. discutée
 direction: DEC
 ""

## 📣 Appel au groupe

 Texte prêt à annoncer la prochaine réunion. Recopiez, remplissez les deux lagunes et envoyez le groupe.


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

## 🔗 Références et corrections

- [[fr/research/journal-clubs/engcomp/topicos|Sujets et où regarder]]- les catégories de l'arXiv que le club accompagne.
- [[fr/research/journal-clubs/engcomp/dashboard|Tableau de bord du club]]- activité par mois, sujet et présentateur.
- [[fr/research/journal-clubs|Clubs de Journal - aperçu]]
- [[fr/research/journal-clubs/mwbr|MWBR]]
- [[fr/research|Recherche - aperçu]]

> [!abstract] Avis de traduction automatique
> Cette page a été traduite automatiquement du portugais à l'aide du traducteur automatique basé sur LibreTranslate implémenté dans `tools/translate_quartz.py` (qui préserve les wikilinks, les embeds et les noms propres par découpage positionnel). Il s'agit d'une traduction automatique pouvant contenir des inexactitudes — la version portugaise originale fait foi.
