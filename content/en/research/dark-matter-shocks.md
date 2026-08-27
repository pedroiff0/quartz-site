---
publish: false
title: Understanding Dark Matter through Extragalactic Shocks
created: 2023-03-01
modified: 2026-07-25T23:58:08.065-03:00
published: 2026-07-25T23:58:08.065-03:00
tags:
  - dark-matter
  - galaxy-clusters
  - undergraduate-research
cssclasses:
  - page-layout
---

# 💥 Understanding Dark Matter through Extragalactic Shocks

> [!note] Summary
> Junior Undergraduate Research project (CNPq/PIBIC-EM, Call 94/2022), advised by [Prof. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja) at IFF Bom Jesus do Itabapoana. I tested the accuracy of Dawson et al.'s (2013) code — which estimates the elapsed time since two galaxy clusters collided, via Monte Carlo — against ZuHone et al.'s (2018) dynamical simulations, as an indirect way to study dark matter's behavior during extreme collisions.

<div class="media-carousel">
  <a href="/en/research/dark-matter-shocks" class="carousel-slide">
    <img src="/assets/illustrations/cosmologia.svg" alt="Galaxy cluster shocks" />
    <div class="slide-caption">Galaxy Cluster Shocks</div>
  </a>
</div>

## 🌌 The problem: how do you "see" dark matter?

Galaxy clusters are the largest gravitationally-bound structures in the Universe — and when two of them collide, the event is among the most energetic known. During a collision, a cluster's three components (galaxies, intracluster gas, and dark matter) behave very differently: galaxies, made of ordinary matter but very sparse relative to each other, pass through each other with barely any interaction; gas, also ordinary matter, collides and is slowed by friction; and dark matter appears to follow the galaxies, but not exactly — indirect evidence that it interacts little (or not at all) through channels beyond gravity. The most famous example is the **Bullet Cluster**, whose gravitational-lensing maps show exactly this spatial separation between the three components.

Since dark matter can't be observed directly, nor can a cluster collision be repeated in a lab, the strategy is indirect: compare **dynamical simulations**against**statistical estimation methods** for observational parameters (relative masses, redshift, projected separation), and check whether they agree.

## 🎯 Objective

Assess the **accuracy**of**Dawson's (2013)** code — which uses a Monte Carlo method to estimate the elapsed time since a pair of clusters first collided, based on relatively simple-to-obtain observational parameters — by comparing its results against the known "ground truth" of ZuHone et al.'s (2018) high-resolution dynamical simulations.

## 🔧 Methodology

The work followed four stages:

1. **Familiarization** with fundamental Astronomy concepts (parallax, OBAFGKM spectral classification, stellar evolution, Hubble's morphological galaxy classification — elliptical, spiral, irregular) and with the physics of colliding clusters.
2. **Compiling and understanding Dawson's code** — first validated against the Bullet Cluster's own reference case (masses $1.5\times10^{14}$ and $1.5\times10^{15}\,M_\odot$, projected separation of 720 kpc), reproducing the original result. The core function, `MCEngine`, takes both clusters' masses, redshift, and projected distance, generating $10^4$ Monte Carlo samples (convergence already observed from $10^3$ iterations onward).
3. **Obtaining ZuHone et al.'s (2018) data** — the _Galaxy Cluster Merger Catalog_, a repository of hydrodynamical cluster-merger simulations organized by mass ratio (1:1, 1:3, 1:10) and impact parameter (0, 500, 1000 kpc). The work focused on the 3 simulations with zero impact parameter (collision in the plane of the sky).
4. **Applying Dawson's method** to each ZuHone simulation, comparing the code's estimated post-collision time against the simulation's known ground truth, with uncertainty estimated via `np.quantile` over the $10^4$ Monte Carlo samples.

## 📊 Results

ZuHone's simulation reveals an oscillatory pattern: clusters start at maximum separation, collide (black line, first collision), separate again to a new maximum — smaller than the first, due to energy lost in the collision — and so on.

| Mass ratio | 1st collision time (Gyr) |
|---|---|
| 1:1 | 1.32 |
| 1:3 | 1.20 |
| 1:10 | 1.04 |

Comparing Dawson's code against ZuHone's data in the window between the first collision and the following maximum separation — the only window where Dawson's method applies — the code's results **agree, within uncertainties, with the simulation for all three tested mass ratios (1:1, 1:3, and 1:10)**.

> [!warning] Systematic bias found
> Despite the good overall agreement, Dawson's code's central estimates showed a **systematic tendency to underestimate** the simulation's true time — a bias that needs deeper investigation in future work, though it doesn't invalidate the method's overall viability.

## 🧾 Conclusion

Dawson's (2013) method proved **reliable within uncertainties** for estimating the elapsed time since a cluster collision, within the method's own stated range of validity — but with a systematic underestimation bias deserving future investigation. The natural next step is extending the analysis to ZuHone's non-zero impact-parameter scenarios (off-sky-plane collisions), not yet tested in this work.

## 🏆 Presentations and awards

This project was presented at **FEBRACE 2023**and**MOSTRATEC 2023** (Novo Hamburgo, Brazil) — see the [[pt-br/media/2023/mostratec-2023|MOSTRATEC coverage]] (Portuguese only).

## 🔗 References and related

- Dawson, W. A. (2013) — _The Dynamics of Merging Clusters: A Monte Carlo Solution Applied to the Bullet and Musket Ball Clusters_, ApJ 772, 131. [MCMAC code](https://github.com/MCTwo/MCMAC).
- ZuHone, J. et al. (2018) — _The Galaxy Cluster Merger Catalog: An Online Repository of Mock Observations from Simulated Galaxy Cluster Mergers_, ApJS 234, 4.
- Clowe, D. et al. — the Bullet Cluster, the classic evidence for spatial separation between dark matter and gas.
- [[pt-br/media/2023/mostratec-2023|MOSTRATEC 2023]] — coverage of this project's presentation (Portuguese only)
- [[en/research/anomaly-detection|Anomaly Detection in Gaia Data]] — another Astronomy research project, also grounded in the dynamics/kinematics of gravitational systems
- [[en/research/satellite-trail-removal|Simulating the Impact of Satellites on Astronomical Observations]] — following project, also computationally focused on astronomical data
- [[pt-br/resource/curso-on/aula-05-avermelhamento-extincao-e-imf|CursoON — Lecture 05]] — another context for non-luminous mass/dark matter within the Galaxy (Portuguese only)
