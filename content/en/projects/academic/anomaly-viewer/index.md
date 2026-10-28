---
publish: true
title: Interactive Anomaly Detection Panel (Anomaly Viewer)
created: 2026-10-28T08:20:00-03:00
modified: 2026-10-28T09:19:58-03:00
published: 2026-10-28T08:20:00-03:00
tags:
  - projeto
  - streamlit
  - galah-dr4
  - espectroscopia
  - en
status: online, temporary
cssclasses:
  - page-layout
icon: lucide-layout-dashboard
sitesync: true
resource-sync: false
lang: en
translation-of: "[[pt-br/projects/academic/anomaly-viewer/index]]"
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>Public Projects</span> <span class="academic-nav-sep">/</span> <span>Anomaly Viewer</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Interactive Anomaly Detection Panel (Anomaly Viewer)</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">← Start</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">Hub</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">End →</span>

</div>

</div>

</div>

# Interactive Anomaly Detection Panel (Anomaly Viewer)

> [!warning] Under construction
> This page is under construction and subject to change.

> [!abstract] Summary
> A web panel to explore the maps of stellar spectra from the research [[en/research/deteccao-de-anomalias-iff-2025/index|Spectral Anomaly Detection in Stars (GALAH DR4)]]. It is a Python (Streamlit) application running on a server of mine, at [anomaly.phrandrade.com](https://anomaly.phrandrade.com), and it was built for SAB 2026: anyone looking at the poster can open the QR code and play with the same maps.

> [!warning] Temporary panel
> The panel is temporary and will be shut down after SAB 2026. For more information, please get in touch: [pedroiff0@gmail.com](mailto:pedroiff0@gmail.com).

## What you can do in the panel

The panel has three pages, in Portuguese and English (language selector at the top, which starts from the browser language), with a light, dark or OLED theme and a layout that adjusts to phones.

- **Overview:** a quick context of the work, the main results from SAB 2025 and SAB 2026, the references with a link to each paper (arXiv, NASA ADS, IOPscience) and the poster PDF to view and download.
- **SAB 2025, basic analyses:** the figures of the 2025 poster redone interactively, with zoom and hover tooltips: histograms of metals, magnesium and age, the Kiel diagram with isochrones, the Toomre diagram and the split between thin and thick disc.
- **Sample and projections:** the sample of 6,198 stars near the Sun and the t-SNE and UMAP maps made from the spectrum, which can be coloured by temperature, gravity and metals, inspected through the GALAH flags, compared side by side, and used to open the data of a single star.

## Behind the panel: the computing side

The panel is the visible tip of a data and software engineering project. The research needs hundreds of thousands of spectra (each with about 14 thousand points) to become a map that a person can explore in the browser, without freezing the machine or the phone of whoever is looking. The main decisions:

- **Stack:** Python 3.11, Streamlit for the interface, Plotly for the charts (with WebGL, to draw thousands of points without choking), pandas and NumPy for the data, Astropy to read the FITS files of the spectra, and scikit-learn, UMAP, HDBSCAN and openTSNE for the maps. The environment is managed with uv.
- **One app, several pages:** there is a single navigation (`st.navigation`) and each page is a separate file. Before, there were six independent applications, each in its own process, because a single process reached 17 GiB of memory and froze the machine.
- **Memory under control:** the spectra matrix (about 1 GB) sits in a shared cache, with no copy on every click, and is loaded only when a page asks for it. If free memory drops below 1.5 GB, the panel refuses to load instead of bringing the server down.
- **Read-only public version:** the public instance has no GPU button and no editing, and only reads data that has already been prepared. The part that uses the whole of GALAH exists, but is for internal use.
- **Translation and theme:** all texts live in a Portuguese and English dictionary, and the theme follows the browser's choice, with an adjustment for small screens (columns stack below 768 px).
- **Going live:** a systemd user service, which starts with the machine and restarts if it crashes, listening only on the local address. Outside access goes through a Cloudflare tunnel, so the server opens no port to the internet.
- **Verification:** the pages are verified without a browser with Streamlit's AppTest, in both languages, and the repository checks the syntax of its modules on every push through an automatic check on GitHub.

## The pipeline that feeds the panel

The maps in the panel come from a separate processing program, designed to run in batches, unattended and without risk to the original data. It has five stages: choose the spectra, extract each one into a matrix, find the nearest neighbours of each star, draw the maps and package the result.

- **Neighbours without PCA:** the program computes the exact neighbours by cosine similarity directly on the pixels, in blocks, never loading everything into memory. For the whole of GALAH DR4 that is 905,415 spectra and a matrix of about 54 GB.
- **Safe execution:** a configurable memory ceiling (12 GB by default), automatic stop if free memory drops too low, resuming from where it left off and no change to the source files.
- **Measured times (GTX 1660 GPU):** the 5 thousand M dwarfs of the local sample take about 25 seconds with all the projections, and the 21,817 M dwarfs of GALAH take about 2.8 minutes.
- **Estimate for the whole of GALAH:** about 2.4 x 10^16 operations for the neighbours alone, something like 4.5 hours on a GTX 1660 card and close to 40 minutes on an A100. It is an estimate, and the real bottleneck is reading the 54 GB from disk several times. It has not been run yet.

## Limits and next steps

- The public panel shows the sample near the Sun, with 6,198 stars. The full-GALAH map is still internal.
- The groups of stars that appear in the maps are candidates, not definitive classes, and that applies to what the panel shows.
- After SAB 2026 the panel goes offline. What remains is the code, the poster and the research notes.

## References and related

- [[en/research/deteccao-de-anomalias-iff-2025/index|Spectral Anomaly Detection in Stars (GALAH DR4)]]: the research behind the panel
- [[en/media/2026/sab/index|XLIX RASAB (2026)]]: the event where the panel was presented
- SpectraViewer: another GALAH DR4 spectrum viewer
- Origin: Public Site
