---
publish: false
title: '20260926 - Sessão Dev - CCD missing, projeções sem PCA e SAB26'
created: 2026-09-26 20:00
modified: 2026-09-26 21:20
tags:
- projeto
- devlog
- anotacao
- anomaly_detection
- sab26
- ccd-missing
- projecoes
icon: lucide-folder
cssclasses:
  - page-layout
---

# Sessão de Dev: CCD missing, projeções sem PCA e SAB26 — 26/09/2026

[[README|⬅️ Voltar ao Hub do Projeto]]

> [!abstract] Resumo da Sessão
> - **Foco da Sessão:** Fechar pendências SAB26; parar PCA pesado; implementar CCD missing; reescrever projeções GPU sem PCA; validar params.
> - **Status:** ✓ Concluído (job params em background; sem commit ainda)

---

## 📋 Referência da Sessão do Agente

[[09-agentes/20260926/20260926 - CLAUDE - anomaly_detection - CCD missing, projeções sem PCA e SAB26|Sessão do Agente Claude Sonnet 5 (26/09/2026)]]

---

## ✓ Entregas Principais

### Job Pesado: Diagnosticado e Parado
- **run_galah_full_chain.sh:** PCA-50 em 905k espectros interrompido
  - Medido: 11,7 min fit + 11,5 min proj (CPU); RAM ~6GB
  - Variância: 49,45% (insuficiente para o custo)
- **Decisão:** PCA agora opt-in (`--pca N` flag); padrão é direto no espectro

### CCD Missing Filtrado
- Nova função `filter_ccd_missing()` em `src/analysis/sample_filters.py`
- Listas geradas: `sobject_ids_<tipo>_{sem,so}_ccd_missing.txt`
- Relatório: `data/ccd_missing_report.csv`
  - GALAH: 4,9% CCD missing
  - Anãs M GALAH: 25,9% CCD missing
  - Anãs M locais: 18,4% CCD missing
- Scripts com `--ccd all|exclude|only` option

### run_projections_gpu.py Reescrito
- **t-SNE/UMAP direto em 14.800 px** (sem PCA padrão)
- **CCD filtering:** 3 modos (all, exclude, only)
- **Rodadas executadas:**
  - Anãs M GALAH: 21.817 estrelas em 2,8 min (GTX 1660)
  - Figuras: `figuras/TCC/profile_galah_m_dwarfs_direto*`
  - Script: `run_m_dwarfs_gpu.sh`

### run_projections_params.py (4 Tipos)
- **Atm:** Teff, logg, [Fe/H]
- **Abund:** 18 elementos (cobertura ≥70%)
- **Kin:** U, V, W, |V|
- **Atm_age:** BASTA (idades)
- **Status:** Validado com 50k; 906k rodando em background via `run_params_all.sh`
- **Output:** `data/allstar_<tipo>_results.csv`

### Documentação Criada
- `docs/estimativa_computacional.md` (medido vs. estimado; A100 benchmark)
- `docs/tutorial_projecoes_ccd_params.md` (guide de flags)

### SAB26 Finalizado
- **Banner:** F13, F14, flag_bitmap inclusos; texto corrigido; cabe em 1 página
- **TCC:** 05-espectros-projecoes.tex com tabela flag_sp e "Binárias e rastreio"
- **Quartz:** Nota criada (publish: false; ⚠️ force_publish=True no script)
- **Streamlit:** AppTest 5 abas, 0 warnings
- **TASKS.md:** Atualizado

---

## 🐛 Bugs & Achados

### Resolvidos
1. **PCA pesado:** Diagnosticado e pausado (trade-off ruim)
2. **CCD missing:** 25,9% das anãs M GALAH—requer filtragem

### Abertos / Alertas
1. **Quartz force_publish=True:** Próximo sync publicaria nota automaticamente
2. **LaTeX errors (05.tex):** `\teff` math mode, figuras com espaço no caminho (não corrigido esta sessão)
3. **run_params_all.sh rodando:** Check `/tmp/params_all.log` para status

---

## 💡 Próximos Passos

- [ ] Verificar conclusão params_all.sh (~70–85s/config em 898k)
- [ ] Decidir Quartz publish (manual ou auto via force_publish)
- [ ] LaTeX fixes em 05 (math mode, file paths)
- [ ] Visual test Streamlit (stage_sab26.py + navegador)
- [ ] Validar `allstar_<tipo>_results.csv`
- [ ] Integração banner/LaTeX para apresentação
- [ ] First commit quando tudo passar

---

**Última atualização:** 2026-09-26 20:45 -03:00

## Adendo (21h) — histórico completo e rodada de parâmetros

- Rodada completa `--ccd all` dos 4 tipos por parâmetros do allstar concluída (`atm` 898.029, `abund` 447.784, `kin` 906.679, `atm_age` 848.032 estrelas; ~4,6 a 13 min por tipo na GTX 1660).
- Pedido do Pedro: guardar tudo (o que deu certo e errado) desde o início para reuniões e TCC (2027.2 e 2028.1). Escrito em `02-areas/academico/pesquisas/deteccao-de-anomalias-em-estrelas-da-via-lactea-2025/arquivos/`: [[esboco-historico-01-linha-do-tempo]], [[esboco-historico-02-licoes-acertos-e-erros]], [[esboco-historico-03-catalogo-de-experimentos]], [[esboco-historico-04-pendencias-e-perguntas-abertas]].
- Banner SAB26: será refeito no `relatex` (decisão do Pedro, para depois).
