---
publish: true
title: "Simulation de l'impact des satellites sur les observations astronomiques"
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

# 🛰️ Simulation de l'impact des satellites sur les observations astronomiques

> [!note] Résumé
> Projet de recherche (IFF Bom Jesus do Itabapoana, orientation de [Professeur Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja)) sur la façon dont la prolifération des satellites artificiels contamine les images astronomiques avec des traces lumineuses - et comment traiter cette pollution par calcul. En équipe avec [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) et Arthur Miguelito Lopes, le projet a évolué d'une troisième place dans [[fr/media/2024/febic-2024|FÉBIC 2024]] même un algorithme capable de récupérer 99,7% de l'information perdue, décerné en 1ère place dans [[fr/media/2025/mctia-2025|MCTIA 2025]].


<div class="media-carousel">
  <a href="/pt-br/research/satellite-trail-removal" class="carousel-slide">
    <img src="/assets/illustrations/informatica.svg" alt="Élimination des traces de satellites dans les images astronomiques" />
    <div class="slide-caption">Pollution lumineuse par satellite</div>
  </a>
</div>


## 🌠 Le problème

 La décennie 2020-2030 apporte une nouvelle génération de télescopes (Vera Rubin, GMT, Euclid) qui augmentera le volume et la qualité des données astronomiques disponibles de plus de mille. En parallèle, cependant, la popularisation de **constellations de satellites commerciaux** peuple l'orbite terrestre de milliers d'objets lumineux, qui se tiennent entre les télescopes et la lumière des étoiles - contaminant des images avec des traces lumineuses et menaçant simplement de dégrader la nouvelle génération de soulèvements astronomiques en grand volume.

 Contrairement aux deux barrières historiques de l'observation astronomique (climat et limitation instrumentale), il s'agit d'une pollution **artificielle**, encore mal quantifiée: la luminosité de chaque satellite dépend de la position, de l'altitude et de la longueur d'onde de manière complexe, et la communauté internationale (astronomes, ingénieurs, défenseurs du ciel sombre) a été mobilisée pour développer des outils de traitement d'images open source.

## 🎯 Objectifs

- Élaborer une méthode de traitement de l'image capable de **identifier la pollution par satellite** dans les observations astronomiques.
- Testez cette méthode en **objets astronomiques simulés**, avec contamination contrôlée, en évaluant l'applicabilité et l'efficacité.
- Redoubler d'efforts pour résoudre le problème de la pollution par la lumière orbitale.

## 🔧 Méthodologie

 Le projet a été planifié en 5 phases : 1) examen systématique du problème et des codes existants; 2) développement d'un objet astronomique simulé (de préférence une galaxie); 3) construction d'un code d'analyse/de traitement de l'image; 4) application du code à l'objet simulé, avec pollution lumineuse contrôlée (simulation de trace satellitaire); 5) analyse des résultats.

## 📈 Faits nouveaux et résultats

| Étape | Événement | Sortie |
|---|---|---|
| Proposition initiale | Éditorial de pré-initiation scientifique, IFF (2023) | Adoption du projet |
| *[[fr/media/2024/febic-2024|FÉBIC 2024]]* (Pomérode, SC) | Communauté [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/)  | ***3ème place - Catégorie de grade**, même si le projet est encore incomplet, en concurrence avec des applications déjà brevetées - résultat qui a classé l'équipement pour le [[fr/media/2025/mctia-2025|MCTIA 2025]]  |
| *[[fr/media/2025/mctia-2025|MCTIA 2025]]**(Belém, AP) | Communauté [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) arthur Miguelito Lopes |***1ère place - catégorie Exate Sciences of Higher Education * *, avec un algorithme IA capable de**enlevant les traces satellite de données astronomiques, en récupérant 99,7 % des informations qui seraient perdues** - résultat qui classait l'équipement pour l'événement national Young Science (Recife, PE, 2026) |

> [!note] Note sur ce texte
> Cette page combine la proposition de recherche officielle (sous-traitée à la FIF en 2023, avec l'introduction complète, la justification et la méthodologie) avec les résultats publiés publiquement dans les prix de la FABIC 2024 et de la MCTIA 2025. Les détails techniques de l'algorithme de récupération de 99,7% n'ont pas encore été documentés sur cette page - mise à jour à mesure que les travaux avancent pour publication.

## 🔗 Références et corrections

- Milazzo et al. (2021) - La fracture numérique croissante et ses répercussions négatives sur l'effectif futur de la NASA, BAAS 53, 436
- Rawls et al. (2020) - Constellation par satellite sur l'accessibilité et les besoins Internet, RNAAS 4, 189
- Venkatesan et al. (2020) - L'impact des constellations satellitaires sur l'espace en tant qu'ancêtre mondial, astronomie de la nature 4, 1043
- [[fr/media/2024/febic-2024|FÉBIC 2024]]- couverture de la présentation et troisième place
- [[fr/media/2025/mctia-2025|MCTIA 2025]]- couverture de la présentation et première place
- [[fr/research/dark-matter-shocks|Comprendre la matière noire des chocs extragalactiques]]- projet précédent, même orientation
- [[fr/research/anomaly-detection|Détection d'anomalies dans les données de Gaia]]- un autre projet axé sur l'apprentissage automatique appliqué aux données astronomiques

> [!abstract] Avis de traduction automatique
> Cette page a été traduite automatiquement du portugais à l'aide du traducteur automatique basé sur LibreTranslate implémenté dans `tools/translate_quartz.py` (qui préserve les wikilinks, les embeds et les noms propres par découpage positionnel). Il s'agit d'une traduction automatique pouvant contenir des inexactitudes — la version portugaise originale fait foi.
