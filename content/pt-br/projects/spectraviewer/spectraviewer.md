---
publish: true
title: SpectraViewer
tags:
- espectroscopia
- galah-dr4
- open-source
repo: https://github.com/pedroiff0/spectraviewer
status: público
cssclasses:
- page-layout
created: 2026-09-14 11:17
modified: 2026-09-30 13:05
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]

# SpectraViewer - GALAH DR4 Spectra Viewer

An interactive viewer for spectra from the GALAH DR4 catalog (Galactic Archeology with Hermes Data Release 4). The application allows you to explore stellar spectra intuitively, with support for multiple bands, reference spectral lines, and automatic spectral classification.

## Features

- **Interactive Visualization**: Plotting of 4 spectral bands (Blue, Green, Red, IR) with interactive interface
- **Spectral Lines**: Overlay of reference spectral lines from GALAH DR4 with groups (CNO, Alpha-process, Iron-peak, etc.)
- **Local Data**: Direct reading of FITS files from the local dataset
- **Stellar Metadata**: Display of information such as Teff, log(g), [Fe/H] and other abundances

## Requirements

- Python 3.8+
- GALAH DR4 Datasets (FITS files)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/pedroiff0/spectraviewer.git
cd spectraviewer
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Run locally

```bash
streamlit run spectraviewer.py
```

The application will open at `http://localhost:8501`.

### Using the application

1. **Search**: Select a star from the dropdown menu
2. **View Spectrum**: The 4-band spectrum will be loaded and displayed
3. **Spectral Lines**: Select groups of spectral lines to overlay on the spectrum
4. **Labels**: Enable the "Show line labels" option to display line identifications

## Data Structure

### FITS Spectra
- Location: `spectra/galah/dr4/spectra/hermes/com/{YYMMDD}/`
- File: `{sobject_id}{CCD}.fits`
- Bands:
  - CCD 1: Blue (~4713 Å)
  - CCD 2: Green (~5648 Å)  
  - CCD 3: Red (~6478 Å)
  - CCD 4: IR (~7585 Å)

### FITS Metadata
- TEFF_R: Effective temperature
- LOGG_R: log(g) - surface gravity
- FE_H_R: Metallicity [Fe/H]
- A_FE_R: Abundance [α/Fe]
- SNR_AA: Signal-to-noise ratio in Ångströms
- RV: Radial velocity
- E_RV: Error in radial velocity

## References

- [GALAH DR4 Survey](https://www.galah-survey.org/)
- [Gaia-ESO Spectroscopic Survey](http://www.gaia-eso.eu/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)
- [Astropy FITS](https://docs.astropy.org/en/stable/io/fits/)

## Development

### Project Structure
```
spectraviewer/
 spectraviewer.py          # Main application
 requirements.txt          # Python dependencies
 class.txt                 # Spectral classification catalog
 spectra/                  # Data (included with samples)
    galah/
        dr4/
            spectra/      # FITS spectrum files
 venv/                     # Virtual environment
 README.md                 # This file
```

### Adding New Features

1. Modify `spectraviewer.py`
2. Test locally: `streamlit run spectraviewer.py`
3. Commit and push to GitHub

## Troubleshooting

### "File not found" for spectra
- Verify that FITS files exist in `spectra/galah/dr4/spectra/hermes/com/`
- Confirm that the `sobject_id` is correct (15 digits)

### Spectral lines do not appear
- Verify that the line list file exists
- Confirm that the wavelengths of the lines are within the spectral coverage range

### Slow performance
- Resize the plots
- Reduce the number of selected line groups
- Check disk read speed for FITS files

## License

This project uses data from the GALAH DR4 Survey. Respect the terms of use of the data.

## Contributions

Contributions are welcome! Please:

1. Fork the repository
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support

For questions, bug reports or suggestions, open an issue in the repository.

---

**Last update**: May 2026  
**Version**: 1.0.0

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/spectraviewer](https://github.com/pedroiff0/spectraviewer)
- **Índice de Projetos:** [[01-projetos/site-publico/projetos-publicos|Projetos Públicos]]

---

<p align=center>
  <a href="https://github.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://linkedin.com/in/pedro-andrade-iff" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://instagram.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="mailto:pedro.andrade@iff.edu.br"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://pedroiff.com" target="_blank"><img src="https://img.shields.io/badge/Website-000000?style=flat-square&logo=googlechrome&logoColor=white" alt="Website" /></a>
</p>

<p align=center>
  <sub>© 2026 <b><a href="https://pedroiff.com">Pedro Rocha</a></b> — Computer Engineering &amp; Computational Astrophysics</sub><br />
  <sub>Made with <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M10 2v2'/><path d='M14 2v2'/><path d='M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1'/><path d='M6 2v2'/></svg>" width="16" height="16" valign="middle" alt="coffee" />, <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='m16 18 6-6-6-6'/><path d='m8 6-6 6 6 6'/></svg>" width="16" height="16" valign="middle" alt="code" /> and <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='3'/><path d='M3 12a9 9 0 0 1 9-9 9 9 0 0 1 9 9 9 9 0 0 1-9 9 9 9 0 0 1-9-9'/><path d='M5.5 5.5a13 13 0 0 0 13 13'/><path d='M18.5 5.5a13 13 0 0 1-13 13'/></svg>" width="16" height="16" valign="middle" alt="astrophysics" /> by <b><a href="https://github.com/pedroiff0">Pedro Henrique Rocha de Andrade</a></b></sub>
</p>
