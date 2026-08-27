---
publish: false
title: Simulating the Impact of Satellites on Astronomical Observations
created: 2024-03-06
modified: 2026-07-25T23:58:08.065-03:00
published: 2026-07-25T23:58:08.065-03:00
tags:
  - light-pollution
  - artificial-satellites
  - image-processing
  - undergraduate-research
cssclasses:
  - page-layout
---

# 🛰️ Simulating the Impact of Satellites on Astronomical Observations

> [!note] Summary
> Research project (IFF Bom Jesus do Itabapoana, advised by [Prof. Ana Cecília Soja](https://integra.iff.edu.br/p/ana-cecilia-soja)) on how the proliferation of artificial satellites contaminates astronomical images with light trails — and how to computationally treat that contamination. Working with [Maycon Jorge Deláqua da Silva](https://mayconjdelaqua.vercel.app/) and Arthur Miguelito Lopes, the project evolved from 3rd place at FEBIC 2024 to an algorithm recovering 99.7% of the lost information, winning 1st place at MCTIA 2025.

<div class="media-carousel">
  <a href="/en/research/satellite-trail-removal" class="carousel-slide">
    <img src="/assets/illustrations/informatica.svg" alt="Satellite trail removal from astronomical images" />
    <div class="slide-caption">Satellite Light Pollution</div>
  </a>
</div>

## 🌠 The problem

The 2020s–2030s bring a new generation of telescopes (Vera Rubin, GMT, Euclid) that will multiply the volume and quality of available astronomical data more than a thousandfold. At the same time, however, the rise of **commercial satellite constellations** is populating Earth orbit with thousands of bright objects that get between telescopes and starlight — contaminating images with light trails and threatening to degrade precisely the new generation of large-volume astronomical surveys.

Unlike the two historical barriers to astronomical observation (weather and instrumental limitations), this is an **artificial** contamination, still poorly quantified: each satellite's brightness depends on position, altitude, and wavelength in complex ways, and the international community (astronomers, engineers, dark-sky advocates) has been mobilizing to develop open-source image-treatment tools.

## 🎯 Objectives

- Develop an image-treatment method capable of **identifying satellite contamination** in astronomical observations.
- Test that method on **simulated astronomical objects**, with controlled contamination, evaluating applicability and efficiency.
- Contribute to the international movement toward open-source solutions for the orbital light-pollution problem.

## 🔧 Methodology

The project was planned in 5 phases: (1) systematic review of the problem and existing codes; (2) building a simulated astronomical object (preferably a galaxy); (3) building an image analysis/treatment code; (4) applying the code to the simulated object, with controlled light pollution (simulated satellite trails); (5) analyzing the results.

## 📈 Evolution and results

| Stage | Event | Result |
|---|---|---|
| Initial proposal | Junior research grant call, IFF (2023) | Project approved |
| **FEBIC 2024**(Pomerode, Brazil) | With Maycon Jorge Deláqua da Silva |**3rd place — Undergraduate category**, even with the project still incomplete, competing against already-patented applications — a result that qualified the team for MCTIA 2025 |
| **MCTIA 2025**(Belém, Brazil) | With Maycon Jorge Deláqua da Silva and Arthur Miguelito Lopes |**1st place — Higher Education Exact Sciences category**, with an AI algorithm capable of**removing satellite trails from astronomical data, recovering 99.7% of the information that would otherwise be lost** — a result that qualified the team for the national Ciência Jovem event (Recife, Brazil, 2026) |

> [!note] Note on this text
> This page combines the formal research proposal (submitted to IFF in 2023, with full introduction, rationale, and methodology) with the results publicly announced at the FEBIC 2024 and MCTIA 2025 awards. Technical details of the 99.7%-recovery algorithm haven't been documented on this page yet — to be updated as the work moves toward publication.

## 🔗 References and related

- Milazzo et al. (2021) — _The Growing Digital Divide and its Negative Impacts on NASA's Future Workforce_, BAAS 53, 436
- Rawls et al. (2020) — _Satellite Constellation Internet Affordability and Need_, RNAAS 4, 189
- Venkatesan et al. (2020) — _The Impact of Satellite Constellations on Space as an Ancestral Global Commons_, Nature Astronomy 4, 1043
- [[pt-br/media/2024/febic-2024|FEBIC 2024]] — coverage of the presentation and 3rd place (Portuguese only)
- [[pt-br/media/2025/mctia-2025|MCTIA 2025]] — coverage of the presentation and 1st place (Portuguese only)
- [[en/research/dark-matter-shocks|Understanding Dark Matter through Extragalactic Shocks]] — earlier project, same advisor
- [[en/research/anomaly-detection|Anomaly Detection in Gaia Data]] — another project focused on machine learning applied to astronomical data
