---
title: "The GALAH survey: Data Release 4 — Análise Espectral, Produtos e Decisões Metodológicas"
first_author: Buder, Sven et al.
year: "2025"
tags:
  - paper
  - pesquisa
  - galah_dr4
  - espectroscopia
  - machine_learning
  - t-sne
  - umap
status: Lido
pdf_link: "**Buder2025**"
created: 2026-03-06 13:34
modified: 2026-09-14 20:12
cssclasses:
  - page-layout
---

# 📑 Notas Metodológicas — Buder et al. (2025) & Aplicação em Machine Learning (Traven 2017, 2019, 2020)

> [!abstract] Referência Principal
> **Artigo:** Buder, S., Kos, J., Wang, E. X., et al. (2025). *The GALAH Survey: Data Release 4*. **Publications of the Astronomical Society of Australia (PASA)**, 42, e051. arXiv:2409.19858.
> **PDF Local:** **Buder2025**
> **Artigos Metodológicos Conexos:**
> - Traven, G. et al. (2017). *The GALAH survey: classification and diagnostics with t-SNE reduction of spectral information*. **Traven2017**.
> - Traven, G. et al. (2020). *The GALAH survey: Double-lined spectroscopic binaries with t-SNE and machine learning*. **Traven2020**.

---

## 1. Arquitetura dos Produtos Espectrais do GALAH DR4 (Seção 7.3)

O GALAH DR4 disponibiliza dois formatos primários para acesso aos dados observacionais de cada estrela (`sobject_id`):

### A. Espectros Reduzidos por CCD (`com/*.fits` / `obs/`) **Buder2025, p. 26**
- **Estrutura:** 4 arquivos FITS independentes por exposição, correspondentes aos 4 braços ópticos do espectrógrafo HERMES no telescópio AAT (3.9 m).
- **Características:**
  - Fluxo bruto em elétrons/pixel (não normalizado).
  - Wavelength parametrizado no cabeçalho FITS ($\text{CRVAL1}, \text{CDELT1}, \text{NAXIS1}$).
  - Referencial do observador (velocidade radial $v_{\mathrm{rad}}$ **não** corrigida).
- **Uso Recomendado:** Reduções fotométricas customizadas, calibrações instrumentais do zero e análise de CCDs isolados.

### B. Espectro Único de Ajuste Espectral (`*_single_fit_spectrum.fits` / `allspec`) **Buder2025, p. 26**
- **Estrutura:** Arquivo FITS único com tabela binária (`HDU 1`) contendo $15.102$ pixels ordenados.
- **Colunas Fundamentais:**
  1. `wave`: Comprimento de onda em repouso ($\lambda_{\mathrm{rest}}$ em $\text{\AA}$), corrigido para o referencial de repouso estelar pelo deslocamento Doppler ($v_{\mathrm{rad}}$).
  2. `sob`: Fluxo observado **normalizado pelo contínuo** ($s_{\mathrm{ob}} \approx 1.0$).
  3. `smod`: **Modelo espectral sintético** ($s_{\mathrm{mod}}$) calculado a partir das atmosferas modelo 1D LTE do pipeline de otimização estelar.
  4. `uob`: Incerteza observacional por pixel ($u_{\mathrm{ob}} = 1/\sigma$).
  5. `mob`: Máscara de pixels com problemas (`mob == 0` são pixels válidos; `mob > 0` indica linhas telúricas, raios cósmicos ou bordas de detector).
- **Vantagem para Machine Learning:** As feições espectrais e linhas atômicas alinham-se rigorosamente nas mesmas posições de comprimento de onda para todas as estrelas, eliminando distorções de velocidade radial antes do t-SNE/UMAP.

---

## 2. Relação Sinal-Ruído ($\text{S/N}$) e Diagnóstico Físico

$$\text{SNR}_{\mathrm{pixel}} = \frac{\text{Fluxo Estelar Medido}}{\sigma_{\mathrm{Poisson}} + \sigma_{\mathrm{leitura}}}$$

### A. Dependência Espectral do $\text{S/N}$ em Estrelas Frias (Anãs M)
Em estrelas de baixa temperatura ($T_{\mathrm{eff}} \le 4000\,\text{K}$), a curva de radiação de corpo negro (Lei de Planck) tem seu pico deslocado para comprimentos de onda mais longos ($> 7000\,\text{\AA}$):
- $\text{S/N}_{\mathrm{CCD1}}$ (Azul: $4713\text{--}4900\,\text{\AA}$): Frequentemente baixo ($\le 10$) devido ao fluxo intrinsecamente fraco.
- $\text{S/N}_{\mathrm{CCD3}}$ (Vermelho: $6479\text{--}6735\,\text{\AA}$) e $\text{S/N}_{\mathrm{CCD4}}$ (Infravermelho: $7680\text{--}7885\,\text{\AA}$): Relação sinal-ruído alta ($> 30\text{--}100$), sendo os balizadores reais da qualidade física da observação.

### B. Critérios de Qualidade Adotados
- `flag_sp == 0`: Ajuste canônico confiável.
- `snr_px_ccd3 >= 15`: Limiar mínimo recomendado para que anomalias em $H\alpha$ representem física real e não artefatos de ruído.

---

## 3. Decisões Metodológicas de Machine Learning (Traven et al. 2017, 2019, 2020)

### A. Grade Comum Unificada e Concatenação dos 4 CCDs
Como o espectrógrafo HERMES possui 4 janelas ópticas com vazios (*gaps*) entre si, a matriz de entrada para algoritmos de manifold learning é construída por:

$$\mathbf{X} = \begin{bmatrix} \vec{s}_{\mathrm{CCD1}} & \vec{s}_{\mathrm{CCD2}} & \vec{s}_{\mathrm{CCD3}} & \vec{s}_{\mathrm{CCD4}} \end{bmatrix} \in \mathbb{R}^{N_{\mathrm{stars}} \times 14800}$$

1. **CCD 1 (Azul):** $4713.0 - 4900.0\,\text{\AA}$ (4.000 pixels) $\to$ Linha $H\beta$ ($4861.3\,\text{\AA}$), Fe I, Ti I.
2. **CCD 2 (Verde):** $5649.0 - 5872.0\,\text{\AA}$ (4.000 pixels) $\to$ Tripleto $\mathrm{Mg\,I\,b}$ ($5183.6\,\text{\AA}$), Dubleto $\mathrm{Na\,I\,D}$ ($5889.9, 5895.9\,\text{\AA}$).
3. **CCD 3 (Vermelho):** $6479.0 - 6735.0\,\text{\AA}$ (4.000 pixels) $\to$ **$H\alpha$ ($6562.8\,\text{\AA}$)**, $\mathrm{Li\,I}$ ($6707.8\,\text{\AA}$).
4. **CCD 4 (IR):** $7680.0 - 7885.0\,\text{\AA}$ (2.800 pixels) $\to$ $\mathrm{K\,I}$ ($7664.9, 7698.9\,\text{\AA}$), Bandas moleculares de $\mathrm{TiO}$ ($7050\text{--}7800\,\text{\AA}$).

### B. PCA como Filtro de Ruído e Redução Intermediária
- Padronização z-score pixel a pixel: $z_{ij} = \frac{x_{ij} - \mu_j}{\sigma_j}$.
- Projeção em $K=50$ componentes principais:
  $$\mathbf{Z} = \mathbf{X}_{\mathrm{scaled}} \mathbf{W}_{K}$$
- **Fundamentação teórica:** Retém $>84\%$ da variância explicada total, compactando correlações de linhas físicas e eliminando o ruído de alta frequência gaussiano pixel a pixel.

### C. Aprendizado de Variedades Não-Lineares: t-SNE vs UMAP
- **t-SNE (Traven et al. 2017):**
  - Otimiza a divergência de Kullback-Leibler $KL(P || Q)$ entre probabilidades de vizinhança em alta dimensão e no espaço 2D:
    $$p_{j|i} = \frac{\exp(-\|\mathbf{z}_i - \mathbf{z}_j\|^2 / 2\sigma_i^2)}{\sum_{k \ne i} \exp(-\|\mathbf{z}_i - \mathbf{z}_k\|^2 / 2\sigma_i^2)}, \quad q_{ij} = \frac{(1 + \|\mathbf{y}_i - \mathbf{y}_j\|^2)^{-1}}{\sum_{k \ne l} (1 + \|\mathbf{y}_k - \mathbf{y}_l\|^2)^{-1}}$$
  - **Sensibilidade:** Excelente para isolar ilhas pontuais de estrelas peculiares com linhas de emissão ou binárias SB2.
- **UMAP (McInnes et al. 2018):**
  - Preserva tanto a geometria local quanto as distâncias topológicas globais da sequência principal.
  - O gradiente contínuo ao longo do manifold 2D correlaciona-se monotonicamente com $T_{\mathrm{eff}}$ e $[\mathrm{Fe/H}]$.

---

## 4. Diagnóstico Físico dos Resíduos Espectrais ($\Delta s = s_{\mathrm{ob}} - s_{\mathrm{mod}}$)

O resíduo espectral isola os fenômenos não contemplados pelos modelos de atmosfera estelar padrão 1D LTE:

| Assinatura no Resíduo | Feição Espectral | Causa Física / Fenomenologia |
| :--- | :--- | :--- |
| **Pico Positivo Estrito** ($\Delta s > +0.3$) | $\lambda = 6562.8\,\text{\AA}$ ($H\alpha$) | **Atividade Magnética Cromosférica / Erupções (Flares)** |
| **Perfil em "W" ou Linhas Desdobradas** | Múltiplos dubletos de Fe/Mg | **Binária Espectroscópica de Linhas Duplas (SB2)** (Traven et al. 2020) |
| **Depressões Moleculares Largas** | $\lambda > 7680\,\text{\AA}$ | **Anã M Ultratardia ($T_{\mathrm{eff}} < 3200\,\text{K}$)** com opacidade de $\mathrm{TiO}$ incompleta no modelo sintético |
| **Degrau no Contínuo** | Transição de CCDs | Imperfeição no fitting do contínuo spline durante a redução preliminar |

---

## 5. Sumário de Diretrizes para o Projeto de Detecção de Anomalias
1. **Entrada Canônica:** Adotar prioritariamente os espectros `_single_fit_spectrum.fits` pelo alinhamento Doppler exato em repouso e normalização homogênea.
2. **Espaço de Busca:** Projetar em 50 componentes PCA e mapear via UMAP / t-SNE.
3. **Métrica de Anomalia:** Combinar **LOF (Local Outlier Factor)** no espaço de alta dimensão com **GLOSH (HDBSCAN)** na densidade latente.
4. **Validação Espectral:** Inspecionar visualmente o resíduo $\Delta s$ em $H\alpha$ e nas bandas de $\mathrm{TiO}$ para classificar a anomalia em física real vs artefato observacional.
