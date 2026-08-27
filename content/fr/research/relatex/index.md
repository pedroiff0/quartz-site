---
publish: true
title: "\"ReLaTeX: LaTeX Class for IFF Academic Work\""
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

# 📄 ReLaTeX: Classe LaTeX pour le travail académique IFF

> [!note] Résumé
> Développement de la classe typographique' iftese. cls' et le paquet d'extension 'macros.sty' pour LaTeX, dans le but d'automatiser la conformité aux normes ABNT (NBR 14724, NBR 6027) dans les travaux académiques de l'Institut fédéral de la lumière - réduire considérablement le temps passé manuellement à former des couches, des tableaux, des figures et des éléments pré / positionnels. Présentation au CONNEPE 2026 (Campos Guarus, RJ, 21-23 septembre), en co-auteur [Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja),[Maria Luiza Linhares Dantas](https://www.mlldantas.com) et [Ana Mara Figueiredo de Oliveira](https://integra.iff.edu.br/ecossistema/pessoas/ana-mara-de-oliveira-figueiredo/colaboradora)


<div class="media-carousel">
  <a href="/pt-br/research/relatex" class="carousel-slide">
    <img src="/assets/illustrations/toolkit.svg" alt="ReLaTeX" />
    <div class="slide-caption">Classe LaTeX ifftase. cls</div>
  </a>
</div>


## 🌌 Le problème

 La rédaction de documents académiques selon les lignes directrices de l'ABNT (NBR 14724 pour les travaux académiques, NBR 6023 pour les références, NBR 6027 pour les résumés) impose une structure rigide, mais LaTeX - l'outil le plus techniquement indiqué pour cela, pour son contrôle typographique et son environnement d'équations supérieures aux processeurs visuels tels que Word - a une courbe d'apprentissage élevée. La différence de paradigme explique pourquoi: Les processeurs WYSIWYG ("ce que vous voyez c'est ce que vous avez") sont faciles à démarrer mais difficiles à schématiser sans casser la conception; LaTeX est WYSIWYM ("ce que vous voyez c'est ce que vous voulez dire") - l'initiateur s'éteint beaucoup et dépend d'une consultation constante, mais, au-delà de la courbe d'apprentissage, il gagne un processus d'écriture beaucoup plus fiable et normalisé.

## 🎯 Objectif

 Développer une classe typographique pour LaTeX pour l'utilisateur IFF typique, qui respecte les lignes directrices ABNT et les particularités locales (logos et symboles institutionnels), atténuant la courbe d'apprentissage de ceux qui n'ont jamais utilisé LaTeX et accélérant le travail de ceux qui l'utilisent déjà.

## 🔧 Méthodologie

 Le projet a utilisé comme base les classes 'abntex2 'et' article ', avec le paquet bibliographique' abntex2cite '(Compatibilité ABNT), compilé via TeX Live (' pdflatex '/' bibtex '), supporté par TeXPage, CUN et Overleaf comme environnements en ligne. Le travail a été divisé en trois étapes:

1. *Normes* * - cartographie des restrictions visuelles et structurelles du NBR 14724 et du NBR 6027, traduites en classe «ifftese». Oui.
2. **Commandes auxiliaires** - le paquet 'macros.sty', créé pour éviter la syntaxe primitive de LaTeX et réduire les erreurs de compilation.
3. *Fichier principal* * - consolidation dans un seul 'main.tex', avec tous les environnements NBR 14724 déjà remplis comme commandes prêtes.

## 📊 Résultats

 L'architecture suit la structure normative de l'ABNT (éléments prétextuels, textuels et posttextuels), éliminant la nécessité pour l'utilisateur de manipuler directement les paquets graphiques ou le formatage complexe:

- *Variables de contrôle* * ('\ FrenteVerso', '\ corlink', '\ sumarioEscada', '\ numeraoPorSecao', '\ capiff', '\ legendacurta', '\ en-tête') - hors oui / non qui génèrent automatiquement des marges, en-têtes, liens et numérotation correctes.
- *Eléments prétextuels* * - variables sémantiques ('\ auteur', '\ title', '\ orientalador', '\ local', '\ instituicao', '\ data') flux macros telles que '\ layer 'and'\ contracapa ', qui donnent des pages complètes déjà formatées selon la norme.
- *Eléments textuels* * - la macro '\ insert' encapsula, en une seule ligne, le dimensionnement, l'alignement, les sous-titres, la source et l'étiquette ('label') pour la référence croisée d'une figure. '\ insert tabela 'and'\ insert frame 'automation la distinction standard de IBGE entre tableaux et tableaux, en envoyant les métadonnées directement aux listes de prétextes.
- **Éléments posttextuels** - les macros propres convertissent la numérotation des appendices / annexes numériques pour l'alphabet sans corrompre la numérotation des chapitres, et uniformisent l'appel des glossaires et des indices rémisifs.

## 🧾 Conclusion

 L'encapsulation de ces routines dans les macros paramétrées a atteint l'objectif : réduire le temps de fonctionnement de la formation et démocratiser la rigueur typographique de LaTeX dans la production technico-scientifique d'IFF, armure l'utilisateur contre les erreurs de syntaxe et les références croisées. En tant que découplage, une interface web optionnelle est en phase de test, dans le style Overleaf, axée exclusivement sur cette classe, conçue pour ceux qui préfèrent remplir des formulaires pour modifier directement le code source.

## 🏆 Afficher

 Ce projet sera présenté en **CONNEPE 2026** (Congrès d'éducation, de recherche et d'extension du campus de Guarus) du 21 au 23 septembre 2026.

## 🔗 Références et corrections

- CONTEXTE ASSOCIATION DES RÈGLES TECHNIQUES. NBR 14724: Information et documentation - Travaux académiques - Présentation. Rio de Janeiro, 2011.
- CONTEXTE ASSOCIATION DES RÈGLES TECHNIQUES. NBR 6027: Information et documentation - Résumé - Présentation. Rio de Janeiro, 2012.
- KNUTH, D.E. Le TeXbook. Lecture, Massachusetts: Addison-Wesley, 1986.
- LAMPORT, L. LaTeX: Système de préparation des documents. 2e éd. Reading, Massachusetts: Addison-Wesley, 1994.
- EQUIPE ABNTEX2 -[la classe abntex2](https://github.com/abntex/abntex2), base de compatibilité ABNT utilisée dans ce projet.
- COEPE 2026 - la couverture de la présentation entre ici après l'événement (septembre 2026).
- [[pt-br/resource/latex|LaTeX et les Écritures académiques]]- le cours construit sur ce projet; les classes 06 à 08 documentent 'ifftese. cls', 'macros.sty' et 'metadata. la ligne de sty à la ligne.
- [[pt-br/resource/latex/modelos-corporativos|Modèles d'entreprise]]- la même architecture de classe appliquée en dehors de l'académie, avec un manuel de marque sur le site ABNT.

> [!abstract] Avis de traduction automatique
> Cette page a été traduite automatiquement du portugais à l'aide du traducteur automatique basé sur LibreTranslate implémenté dans `tools/translate_quartz.py` (qui préserve les wikilinks, les embeds et les noms propres par découpage positionnel). Il s'agit d'une traduction automatique pouvant contenir des inexactitudes — la version portugaise originale fait foi.
