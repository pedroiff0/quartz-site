---
publish: false
title: "Articles"
created: 2026-07-23
modified: 2026-07-25T23:58:08.061-03:00
published: 2026-07-25T23:58:08.061-03:00
order: 1
cssclasses:
  - page-layout
---

> [!note] Résumé
> Lecture Annotation sur 28 articles scientifiques relatifs au projet [[fr/research/anomaly-detection|Détection d'anomalies dans les données de Gaia]], par thème.


<div class="media-carousel">
  <a href="/pt-br/research/anomaly-detection/articles/collaboration2016" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="La mission Gaia" />
    <div class="slide-caption">La mission Gaia</div>
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
    <img src="/assets/illustrations/articles.svg" alt="GALAH - Classement par t-SNE" />
    <div class="slide-caption">GALAH - Classement par t-SNE</div>
  </a>
  <a href="/pt-br/research/anomaly-detection/articles/lochner2021" class="carousel-slide">
    <img src="/assets/illustrations/articles.svg" alt="ASTRONOMIQUE ET" />
    <div class="slide-caption">ASTRONOMIQUE ET</div>
  </a>
</div>


 Lire l'annotation d'articles scientifiques pertinents à ma recherche dans la détection d'anomalies dans les populations stellaires - sa synthèse, pas les articles complets (le droit d'auteur des éditoriaux / arXiv restent avec les auteurs originaux). Groupe par papier dans le projet: les soulèvements et les données que j'utilise, les méthodes d'apprentissage automatique que j'applique, les modèles stellaires qui étalonnent mes âges / isocrates, et le contexte de la chimie dynamique / galactique qui interprète les résultats.

## 🛰️ Revenus et catalogues ( dés)

- [[fr/research/anomaly-detection/articles/collaboration2016|La mission Gaia]]- 1 milliard d'étoiles d'astrométrie; source des coordonnées cinématiques du projet.
- [[fr/research/anomaly-detection/articles/collaboration2021|Gaia EDR3 - Gaia Catalogue des étoiles à proximité]]- catalogue propre à 100 cc du Soleil, base de l'échantillon GCNS.
- [[fr/research/anomaly-detection/articles/deandrade2025|GCNS × GALAH DR4]]- mon propre article, l'analyse conjointe qui sous-tend l'étape 1.
- [[fr/research/anomaly-detection/articles/buder2025|GALAH DR4]]- 4ème sortie de GALAH : jusqu'à 32 éléments par étoile via des réseaux neuronaux.
- [[fr/research/anomaly-detection/articles/kos2017|GALAH - Pipeline pour la réduction des données]]- comme les spectres bruts d'HERMES ont vu les paramètres du catalogue.
- [[fr/research/anomaly-detection/articles/majewski2017|APOGEE]]- relevé infrarouge haute résolution, utilisé comme comparaison / contexte.
- [[fr/research/anomaly-detection/articles/xiang2019|LAMOST DR5 - Abondances de 16 éléments]]- une autre enquête spectroscopique de grande envergure, fondée sur des données (DD-Payne).
- [[fr/research/anomaly-detection/articles/quispehuaynasi2025|S-PLUS DR4 - Amortisseurs SED]]- détection d'anomalies photométriques dans différentes enquêtes, parallèle méthodologique.

## 🤖 Apprentis machine et détection d'anomalies

- [[fr/research/anomaly-detection/articles/traven2017|GALAH - Classement par t-SNE]]- méthodologie de base de l'étape 2 (t-SNE sur les spectres bruts).
- [[fr/research/anomaly-detection/articles/dasilva2023|silva & Smiljanic (2023) - T-SNE Chimiodynamique]]- base de comparaison entre les colonnes de catalogue et les pixels de spectre.
- [[fr/research/anomaly-detection/articles/lochner2021|ASTRONOMIQUE ET]]- motivation à l'échelle : pourquoi les grandes données astronomiques nécessitent une détection automatique des anomalies.
- [[fr/research/anomaly-detection/articles/ishida2021|Détection d'anomalies actives (Domaine du temps)]]- apprentissage actif appliqué à la découverte d'objets inhabituels.
- [[fr/research/anomaly-detection/articles/traven2019|Machine Learning pour Binary]]- examen des méthodes de ML dans les grands soulèvements.
- [[fr/research/anomaly-detection/articles/otar2021|GALAH - Emission Line Stars]]- codeur automatique qui reconspire les spectres pour trouver des émissions anormales - même famille de la méthode de la phase 2.
- [[fr/research/anomaly-detection/articles/hughes2022|GALAH - Des étoiles extrêmement pauvres à Metais]]- ML supervisé pour trouver 54 candidats EMP dans GALAH.
- [[fr/research/anomaly-detection/articles/vogrini2023|GALAH - Différents groupes interstellaires]]- un autre exemple d'exploitation spectroscopique de mégadonnées GALAH.

## ⭐ Modèles et âges Stellar

- [[fr/research/anomaly-detection/articles/bressan2012|PARSEC - Stellar Isocrates]]- code d'évolution des étoiles généré par les isocrons utilisés dans le diagramme de Kiel.
- [[fr/research/anomaly-detection/articles/marigo2017|PARSEC-COLIBRI - Isocrates avec la phase TP- AGB]]- plus récente génération d'isocrates, avec la phase détaillée TP- AGB.
- [[fr/research/anomaly-detection/articles/hayden2022|GALAH - Montres chimiques]]- vieillir par XGBoost de la seule métallicité / abondance.
- [[fr/research/anomaly-detection/articles/traven2020|GALAH - binaire FGK]]- échantillon de binaire spectroscopique, utile pour le nettoyage des polluants de l'échantillon.
- [[fr/research/anomaly-detection/articles/thomas2024|SpectroTraducteur]]- réseau neuronal pour convertir les paramètres entre différentes enquêtes.

## 🌌 Dynamique galactique et chimie (interprétation)

- [[fr/research/anomaly-detection/articles/bovy2015|- oui]]- paquet utilisé pour calculer les orbites et les actions, base de la cinétique du projet.
- [[fr/research/anomaly-detection/articles/mcmillan2017|Masse et distribution potentielle de la Voie lactée]]- le potentiel galactique utilisé dans la galpie pour intégrer les orbites.
- [[fr/research/anomaly-detection/articles/hayden2020|GALAH - Chimiodynamique du quartier solaire]]- structure chimiodynamique de référence pour comparaison avec l'échantillon croisé.
- [[fr/research/anomaly-detection/articles/recioblanco2014|Gaia-ESO - Transmittal Disco Fino / Espesso]]- le contexte des populations stellaires et de la migration radiale.
- [[fr/research/anomaly-detection/articles/borbolato2025|Coformation de disques fins/épais (z > 2)]]- scénario d'entraînement pour la dichotomie fine/épais.
- [[fr/research/anomaly-detection/articles/tinsley1979|Stellar temps de vie et raisons de l'abondance]]- article classique de l'évolution chimique, base théorique de la nucléosis.
- [[fr/research/anomaly-detection/articles/wallerstein1962|Abondances en Anãs G VI]]- article historique, une des premières déterminations systématiques de l'abondance stellaire.

> [!abstract] Avis de traduction automatique
> Cette page a été traduite automatiquement du portugais à l'aide du traducteur automatique basé sur LibreTranslate implémenté dans `tools/translate_quartz.py` (qui préserve les wikilinks, les embeds et les noms propres par découpage positionnel). Il s'agit d'une traduction automatique pouvant contenir des inexactitudes — la version portugaise originale fait foi.
