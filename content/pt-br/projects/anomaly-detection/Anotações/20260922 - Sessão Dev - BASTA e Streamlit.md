---
publish: false
title: '20260922 - Sessão Dev - BASTA e Streamlit'
created: 2026-09-22 14:30
modified: 2026-09-22 22:41
tags:
- projeto
- devlog
- anotacao
- anomaly_detection
- basta
- streamlit
icon: lucide-folder
cssclasses:
  - page-layout
---

# Sessão de Dev: BASTA e Streamlit — 22/09/2026

[[README|⬅️ Voltar ao Hub do Projeto]]

> [!abstract] Resumo da Sessão
> - **Foco da Sessão:** Preparação BASTA venv, refatoração Streamlit (t-SNE/UMAP), limpeza data/, validação de nota anterior
> - **Status:** ✓ Concluído

---

## 📋 Referência da Sessão do Agente

[[09-agentes/20260922/20260922 - CLAUDE - anomaly_detection - Preparação BASTA e Streamlit viewer|Sessão do Agente Claude Sonnet 5 (22/09/2026)]]

---

## ✓ Entregas Principais

### Limpeza e Ambiente
- Data directory: ~2.5GB de arquivos órfãos movidos para `_archive/`
- HD GALAH externo montado e integrado
- Verificação de nota AGY: erros em distâncias confirmados (Gaia vs GALAH calibration)
- `.gitignore` e `.stignore` atualizados (Syncthing issue)

### Scripts Refatorados (6)
Todos os paths corrigidos para relative paths com `Path(__file__).parent`:
- `src/download/download_single_df5.py`
- `src/download/download_single_spectra.py`
- `src/download/download_spectra.py`
- `src/analysis/inspect_and_compare_spectra.py`
- `src/analysis/run_tsne_umap_m_dwarfs.py`
- `src/notebook_gen/create_comparison_notebook.py`

### Novo Script: `src/analysis/tsne_umap_isolation_score.py`
Calcula anomaly score diretamente em embeddings 2D (t-SNE/UMAP), atalho para exploração visual rápida.

### Streamlit Viewer (Completo)
4 páginas modulares:
- **Sample:** exploração de amostras individuais
- **GAIA:** histogramas e estatísticas GAIA
- **GALAH:** histogramas e estatísticas GALAH
- **Anomaly Visualization:** plot t-SNE/UMAP com anomalias destacadas

Arquivos criados:
- `viewer/app.py` (main Streamlit app)
- `viewer/common.py` (cached loaders, utilities)
- `viewer/stage_sample.py`, `stage_gaia.py`, `stage_galah.py`, `stage_anomaly.py`
- `viewer/README.md` (instruções de uso)

**Otimizações:**
- `@st.cache_data` em loaders (~5-10s initial, <1s reloads)
- Queries e filtros eficientes
- RAM-conscious com lazy loading

### BASTA Pipeline (Validado)
- venv isolado criado: `basta_venv/`
- BaSTI grid (~34GB) integrado
- 2 scripts validation testados com sucesso:
  - `src/validation/build_basta_input.py`: prepara dados para BASTA
  - `src/validation/run_basta_fit.py`: executa fits
- Bug astropy-iers-data em pyproject.toml corrigido

### Documentação Atualizada
- `TASKS.md`: roadmap revisto
- `SETUP.md`: instruções BASTA+venv
- `viewer/README.md`: guide de uso
- `pyproject.toml`: dependências validadas

---

## 🐛 Bugs, Errors & Troubleshooting

### Resolvidos
1. **pyproject.toml astropy-iers-data:** removido de deps (gerado automaticamente)
2. **Path issues:** 6 scripts migrando hardcoded paths → Path(__file__).parent
3. **Data orphans:** ~2.5GB de .pkl antigos identificados e arquivados

### Aberto (Syncthing Issue) ⚠️
- Arquivo `syncthing.Academicos.zip.tmp` (9.9GB) presente no repo root
- Sinc contínua sincronizando pasta "Academicos" (fora de escopo)
- Adicionado a .gitignore e .stignore, mas precisa de debug:
  - Desabilitar Syncthing no repo?
  - Config residual deixada?
  - Limpar `.stfolder/` e relogs?

### Notas Técnicas
- GALAH distances (nota AGY): confirmado mismatch com Gaia → precisa calibração
- BASTA validation testado com 100-star subset → pronto para full run
- Streamlit cache testado com dataset ~5k estrelas → 50MB RAM

---

## 🔗 Links & Referências Úteis

- **BASTA:** http://www.brera.inaf.it/basta/
- **BaSTI:** isochrones grid, docs in `basta_venv/lib/.../basti/`
- **t-SNE/UMAP:** sklearn, umap-learn (já em pyproject.toml)
- **Streamlit:** https://streamlit.io/

---

## 🎯 Decisões Técnicas (ADR) & Respostas de IA

### ADR-1: Modularização Streamlit
**Decisão:** 4 stages independentes (sample, gaia, galah, anomaly) em arquivos separados.
**Rationale:** Clarity, maintainability, fácil adicionar novas páginas.
**Implementação:** `common.py` expõe loaders+utilities, cada stage é um módulo.

### ADR-2: BASTA venv Isolado
**Decisão:** venv separado em `basta_venv/`, não integrado ao projeto principal.
**Rationale:** BASTA é pesado (~34GB grid), isolamento evita conflitos de deps.
**Setup:** `python -m venv basta_venv && source basta_venv/bin/activate && pip install -e .`

### ADR-3: Cache Strategy (Streamlit)
**Decisão:** `@st.cache_data` em `load_data()`, load_embeddings()`, minimal invalidation.
**Rationale:** ~5-10s initial load, <1s reloads, melhor UX.
**Trade-off:** RAM usage (~50MB para 5k stars), aceitável no dev.

---

## 💡 Ideias, Refatoração & Próximos Passos

### Próximas Ações
- [ ] Resolver Syncthing (debugar config ou desabilitar)
- [ ] Executar BASTA full pipeline end-to-end
- [ ] Testes Streamlit com dataset completo (>100k stars)
- [ ] Otimizar RAM para large datasets
- [ ] Documentar troubleshooting BASTA+venv setup
- [ ] Validar calibração GALAH distances

### Ideias Futuras
- Dashboard consolidado (Streamlit + BASTA results)
- Batch processing UI (upload CSVs, run pipeline)
- API REST wrapper (FastAPI) para automation
- Caching de embeddings (DuckDB, Parquet)

---

**Última atualização:** 2026-09-22 16:45 -03:00
