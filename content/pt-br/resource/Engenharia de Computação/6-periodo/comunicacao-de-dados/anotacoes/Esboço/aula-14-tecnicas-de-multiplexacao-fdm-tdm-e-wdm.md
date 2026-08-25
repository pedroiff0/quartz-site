---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-14-tecnicas-de-multiplexacao-fdm-tdm-e-wdm
title: "Aula 14: Técnicas de Multiplexação: FDM, TDM e WDM — Comunicação de Dados"
created: 2026-12-01T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-14
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Comunicação de Dados"
professor: "Rômulo / Paulo"
conteudo: "Multiplexação por Divisão de Frequência, TDM Síncrono/Estatístico, Wavelength Division Multiplexing e hierarquias digitais (PDH/SDH)."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-13-protocolos-de-janela-deslizante-go-back-n-e-selective-repeat">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-15-espalhamento-espectral-dsss-fhss-e-cdma">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Comunicação de Dados (CSECBJI.47)
> - **Professor:** Rômulo / Paulo
> - **Data Realizada:** 01/12/2026
> - **Tópico Principal:** Técnicas de Multiplexação: FDM, TDM e WDM
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-14-comunicacao-de-dados|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-14-comunicacao-de-dados|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Técnicas de Multiplexação: FDM, TDM e WDM](#-anotações-do-quadro-técnicas-de-multiplexação-fdm,-tdm-e-wdm)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Técnicas de Multiplexação: FDM, TDM e WDM

### 14.1 Conceito de Multiplexação
A **Multiplexação** consiste em combinar múltiplos fluxos de comunicação independentes de baixa velocidade para transmissão simultânea através de um único meio físico compartilhado de alta capacidade.

### 14.2 Técnicas Fundamentais de Multiplexação
1. **FDM (Frequency-Division Multiplexing - Analógica):**
   - A largura de banda total do canal é dividida em faixas de frequência não-sobrepostas.
   - Cada canal modula uma portadora distinta.
   - Inserção obrigatória de **Bandas de Guarda (*Guard Bands*)** entre canais adjacentes para evitar diafonia e sobreposição espectral (ex: Rádio FM, TV aberta).
2. **TDM Síncrono (Time-Division Multiplexing - Digital):**
   - O tempo de transmissão é dividido em quadros periódicos e cada canal recebe uma **fatia de tempo (*Time Slot*) fixa e dedicada** em cada quadro, mesmo que não tenha dados para enviar (ex: Linhas telefônicas E1 de 2.048 Mbps com 32 slots de 64 kbps).
3. **TDM Estatístico / Assíncrono (STDM):**
   - Aloca slots dinamicamente sob demanda apenas para canais ativos. Cada slot inclui cabeçalho com o endereço do canal, maximizando a taxa de utilização da linha.
4. **WDM (Wavelength-Division Multiplexing - Óptica):**
   - FDM em frequências de luz: múltiplos sinais laser em comprimentos de onda ligeiramente diferentes ($\lambda_1, \lambda_2, \dots$) são combinados em uma única fibra óptica (ex: DWDM com mais de 80 canais a 100 Gbps por fibra).

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Estrutura do Quadro E1 Padrão Brasileiro e Europeu (TDM Síncrono)

**Parâmetros:**
- Taxa de Amostragem de Voz (Nyquist): $8.000\text{ amostras/s}$ ($T_{\text{amostragem}} = 125\ \mu\text{s}$)
- Quantização: $8\text{ bits por amostra}$ (Lei A) $\implies 64\text{ kbps}$ por canal de voz.
- Quantidade de Canais: $32\text{ Time Slots}$ ($TS_0$ a $TS_{31}$).
  - $TS_0$: Sincronismo de quadro.
  - $TS_1$ a $TS_{15}$: Canais de voz/dados.
  - $TS_{16}$: Sinalização telefônica (CAS/CCS).
  - $TS_{17}$ a $TS_{31}$: Canais de voz/dados.

**Cálculo da Taxa de Dados Total:**
$$\text{Taxa E1} = 32\text{ slots} \times 8\text{ bits/slot} \times 8.000\text{ quadros/s} = 2.048.000\text{ bps} = 2.048\text{ Mbps}$$

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart LR
    C1[Canal 1: 64 kbps] --> Mux[Multiplexador TDM]
    C2[Canal 2: 64 kbps] --> Mux
    C3[Canal 3: 64 kbps] --> Mux
    C4[Canal 4: 64 kbps] --> Mux
    Mux -->|Linha Agregada: Slot 1 | Slot 2 | Slot 3 | Slot 4| Demux[Demultiplexador TDM]
    Demux --> R1[Receptor 1]
    Demux --> R2[Receptor 2]
    Demux --> R3[Receptor 3]
    Demux --> R4[Receptor 4]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **TDM Síncrono vs Estatístico** | No TDM síncrono, se um usuário não transmitir nada, seu slot trafega vazio (desperdício de banda). No TDM estatístico, o slot é atribuído a quem tem dados na fila. | A base das redes de comutação de pacotes modernas. |
| **Padrão T1 vs E1** | O padrão americano T1 possui 24 canais e opera a $1.544	ext{ Mbps}$; o padrão E1 brasileiro/europeu possui 32 canais e opera a $2.048	ext{ Mbps}$. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Calcule a eficiência de uso de banda de um sistema FDM de 10 canais onde cada canal tem banda útil de $4	ext{ kHz}$ e são usadas faixas de guarda de $500	ext{ Hz}$ entre canais vizinhos.
2. Explique a diferença entre WDM convencional (CWDM) e WDM denso (DWDM) em termos de espaçamento entre canais.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-13-protocolos-de-janela-deslizante-go-back-n-e-selective-repeat">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados/anotacoes/aula-15-espalhamento-espectral-dsss-fhss-e-cdma">Próxima Aula</a></b></div>
</div>
