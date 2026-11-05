---
publish: true
title: Baton
created: '2026-11-04T12:00:00-03:00'
modified: 2026-11-04T20:13:52-03:00
published: '2026-11-04T12:00:00-03:00'
tags:
- projeto
- publico
- pessoal
- apresentacao
- codigo-aberto
cssclasses:
  - page-layout
icon: lucide-presentation
repo: https://github.com/pedroiff0/baton
status: ativo
license: MIT
author: Pedro Henrique Rocha de Andrade
sitesync: true
resource-sync: false
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>Projetos Públicos</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Baton</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/academic/anomaly-viewer/index|← Painel interativo de Detecção de Anomal…]]</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">Hub</span> <span class="academic-nav-counter">(2 de 2)</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn is-disabled">Fim →</span>

</div>

</div>

</div>

- Origem: Site Público

# Baton

Controle remoto de apresentações pelo iPhone, via Tailscale, no estilo do clicker Logitech Spotlight. Roda no macOS, Windows e Linux, aceita iPhone ou Android como controle, não exige instalar nada no celular e funciona com qualquer aplicativo de apresentação.

## Modos

- **Externo:** controla PowerPoint, Keynote, leitores de PDF e navegador por teclas e mouse; uma camada nativa em Swift fica acima do modo apresentação, com laser, foco com desfoque, caneta e marca-texto.
- **Tela:** abre um PDF no navegador do Mac com transições, notas do apresentador, passos dentro do slide, zoom e prévia do próximo slide.

## Recursos

- Laser, foco com desfoque ajustável, caneta, marca-texto e zoom.
- Notas do apresentador visíveis no iPhone (arquivo Markdown ao lado do PDF).
- Cronômetro com meta, "Ir para" por número ou miniaturas.
- Personalização salva em disco (tamanho e cor do laser, raio e desfoque do foco, espessuras).
- QR code, token persistente, app na tela de início, instalação no login (`--instalar`).
- Conexão estável: batimento, reconexão e comandos idempotentes.

## Segundo plano

Instalado (`install.sh` ou `install.ps1`), o Baton roda em segundo plano, detecta uma apresentação em tela cheia e pergunta no celular se deve controlar. Dá para pausar a qualquer momento (`baton --pausar` ou painel local).

## Stack

Python 3 (somente biblioteca padrão), Swift/AppKit, Tk, Gtk, pdf.js, PWA, Tailscale.

## Uso

```bash
git clone https://github.com/pedroiff0/baton
cd baton
python3 baton.py slides.pdf
```

Ler o QR code do terminal com o iPhone. Código, instruções completas e licença MIT: [pedroiff0/baton](https://github.com/pedroiff0/baton).
