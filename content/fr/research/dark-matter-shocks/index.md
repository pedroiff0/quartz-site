---
publish: true
title: "Comprendre la matière noire des chocs extragalactiques"
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

# 💥 Comprendre la matière noire des chocs extragalactiques

> [!note] Résumé
> Projet d'initiation scientifique junior (CNPq / PIBIC-EM, édition 94 / 2022), orienté par [Professeur Ana Cecília Soja ](https://integra.iff.edu.br/p/ana-cecilia-soja) à l'IFF Bom Jésus do Itabapoana. J'ai testé la précision du code Dawson et al. (2013) - qui estime le temps passé depuis la collision de deux amas de galaxies via Monte Carlo - contre les simulations dynamiques de ZuHone et al. (2018), comme moyen indirect d'étudier le comportement de la matière noire lors de collisions extrêmes.


<div class="media-carousel">
  <a href="/pt-br/research/dark-matter-shocks" class="carousel-slide">
    <img src="/assets/illustrations/cosmologia.svg" alt="Chocs des amas de galaxies" />
    <div class="slide-caption">Chocs en groupe</div>
  </a>
</div>


## 🌌 Le problème : comment "voir" la matière noire ?

 Les galaxies en grappe sont les plus grandes structures gravitationnelles de l'univers et, lorsque deux d'entre elles entrent en collision, l'événement est l'une des plus énergétiques connues. Dans une collision, les trois composantes d'un amas (galaxie, gaz intragloméré et matière noire) se comportent de différentes manières : les galaxies, faites de matière normale mais très fallacieuses l'une envers l'autre, se croisent presque sans interagir; le gaz, aussi la matière normale, se heurte et est sans frottement; et la matière noire semble accompagner les galaxies, mais pas exactement - preuve indirecte qu'elle interagit peu (ou rien) par des voies au-delà de la gravité. L'exemple le plus célèbre est le ** Bala cluster*, dont les cartes gravitationnelles montrent exactement la séparation spatiale entre les trois composantes.

 Comme il n'est pas possible d'observer directement la matière noire, ni de répéter une collision en grappe en laboratoire, la stratégie adoptée est indirecte: comparer **simulations dynamiques**avec**méthodes statistiques d'estimation des paramètres d'observation** (masses relatives, changement de rouge, séparation projetée) et vérifier s'ils sont d'accord.

## 🎯 Objectif

 Évaluer le **acuracia**du *Dawson (2013)* code - qui utilise la méthode Monte Carlo pour estimer le temps passé depuis la première collision d'un couple de clusters, à partir de paramètres d'observation relativement simples à obtenir - en comparant ses résultats avec le "gabarito" connu des simulations dynamiques à haute résolution de**ZuHone et al. (2018)**.

## 🔧 Méthodologie

 Les travaux ont suivi quatre étapes :

1. *Familiarisation* * avec des concepts fondamentaux d'astronomie (parax, classification spectrale OBAFGKM, évolution stellaire, classification morphologique des galaxies Hubble - elliptiques, spirales, irrégulières) et avec le problème physique des agglomérés de collision.
2. **Compilation et compréhension du code Dawson** - validé d'abord par rapport au cas de référence de l'Aggloméré Bala lui-même (masses 1 $ {,} 5\ fois10 ^ {14} $ et 1 $ {,} 5\ fois10 ^ {15}\, M\ odot $, séparation projetée de 720 kpc), reproduisant le résultat original. La fonction centrale, 'MCEngine', reçoit des masses des deux clusters, Redshift et la distance projetée, et génère 10 ^ 4 $ d'échantillons via Monte Carlo (convergence déjà observée à partir de 10 ^ 3 $ d'itérations).
3. *ZuHone et al. (2018)* * - ou Galaxy Cluster Fusion Catalog, un dépôt de simulations hydrodynamiques de fusions de clusters, organisé par masse (1: 1, 1: 3, 1: 10) et par paramètre d'impact (0.500, 1000 kpc). Le travail s'est concentré sur les 3 simulations avec le paramètre d'impact 0 kpc (cosion dans le plan du ciel).
4. *Application de la méthode Dawson* * à chacune des simulations de ZuHone, comparant le temps estimé post-cousion par le code avec le temps réel connu de la simulation, avec une incertitude estimée via 'np.quantile' sur les échantillons de 10 ^ 4 $ Monte Carlo.

## 📊 Résultats

 La simulation de ZuHone révèle un modèle oscillatoire : les grappes partent de la séparation maximale, du coliden (ligne noire, première collision), elles reviennent à un nouveau maximum - inférieur au premier, en raison de la perte d'énergie dans la collision - et ainsi de suite.

| Raison de masse | Instant de la 1ère collision (Gains) |
|---|---|
| 1 : 1 | 1,32 |
| 1 : 3 | 1.20 |
| 1 : 10 | 1.04 |

 Comparaison du code Dawson avec les données de ZuHone dans l'intervalle entre la première collision et la distance maximale suivante - la seule fenêtre dans laquelle la méthode Dawson est appliquée - les résultats de la concordance du code *, dans les incertitudes, avec la simulation pour les trois raisons de masse prouvées (1: 1, 1: 3 et 1: 10) * *.

> [!warning] Visites systématiques trouvées
> Malgré le bon accord général, les valeurs centrales estimées par le code Dawson ont montré une tendance systématique à sous-estimer * * le temps réel de la simulation - un biais qui doit être étudié plus en détail dans les travaux futurs, et qui n'invalide pas la viabilité générale de la méthode.

## 🧾 Conclusion

 La méthode Dawson (2013) était fiable **dans les incertitudes** pour estimer le temps passé depuis la compilation des amas de galaxies, dans l'intervalle de validité proposé par la méthode elle-même, mais avec une tendance systématique de sous-estimation qui mérite des recherches futures. La perspective naturelle est d'étendre l'analyse pour les scénarios ZuHone avec un paramètre d'impact nonulo (cossions en dehors du plan du ciel), pas encore testé dans ce travail.

## 🏆 Présentations et prix

 Ce projet a été présenté dans le **[[fr/media/2023/febrace-2023|FECURE 2023]]♪ et ♪[[fr/media/2023/mostratec-2023|MOSTRATEC 2023]]** (Novo Hamburg, RS).

## 🔗 Références et corrections

- Dawson, W. A. (2013) - The Dynamics of Melling Clusters: La Monte Carlo Solution appliquée aux clusters à balles et à balles, ApJ 772, 131.[Annonce complète de l'article (arXiv)](/assets/articles/Dawson2013.pdf)·[Code MCMAC](https://github.com/MCTwo/MCMAC).
- ZuHone, J. et al. (2018) - Le catalogue de fusions de clusters Galaxy : un dépôt en ligne d'observations Mock de fusions de clusters Galaxy simulées, ApJS 234, 4.[Annonce complète de l'article (arXiv)](/assets/articles/ZuHone2018.pdf).
- Clowe, D. et al. - Bala cluster, preuve classique de la séparation spatiale entre la matière noire et le gaz.
- [[fr/media/2023/mostratec-2023|MOSTRATEC 2023]]- couverture de la présentation de ce projet
- [[fr/research/anomaly-detection|Détection d'anomalies dans les données de Gaia]]- un autre projet de recherche en astronomie, également orienté par la dynamique / cinématique des systèmes gravitationnels
- [[fr/research/satellite-trail-removal|Simulation de l'impact des satellites sur les observations astronomiques]]- prochain projet, également avec une approche computationnelle appliquée aux données astronomiques
- [[pt-br/resource/curso-on/aula-05-avermelhamento-extincao-e-imf|Cours ON - Classe 05]]- un autre contexte de masse non-claire / matière noire dans la galaxie

> [!abstract] Avis de traduction automatique
> Cette page a été traduite automatiquement du portugais à l'aide du traducteur automatique basé sur LibreTranslate implémenté dans `tools/translate_quartz.py` (qui préserve les wikilinks, les embeds et les noms propres par découpage positionnel). Il s'agit d'une traduction automatique pouvant contenir des inexactitudes — la version portugaise originale fait foi.
