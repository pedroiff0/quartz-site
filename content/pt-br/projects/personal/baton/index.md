---
publish: true
title: Baton
created: '2026-11-04T12:00:00-03:00'
modified: 2026-11-10T13:55:41-03:00
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
mirror_of: pedroiff0/baton/README.md
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

<h3 align="center">Baton — Passador de slides pelo celular</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center">O celular (iPhone ou Android) controla qualquer app de apresentação no macOS, Windows ou Linux, com laser, foco, caneta, marca-texto, cortina, notas e zoom. Somente biblioteca padrão do Python 3.8+.</p>

## 📝 Sumário

- [⚡ Guia Rápido](#guia-rapido)
- [Sobre](#sobre)
- [Instalação](#instalacao)
- [Uso](#uso)
- [Plataformas](#plataformas)
- [Sem internet e Bluetooth](#offline)
- [Segurança](#seguranca)
- [Testes](#testes)
- [Contribuição](#contribuicao)

---

## ⚡ Guia Rápido <a name="guia-rapido"></a>

```bash
python3 baton.py                # celular controla o app em primeiro plano
python3 baton.py slides.pdf     # o Baton exibe o PDF no navegador
python3 baton.py --instalar     # inicia com o sistema (--desinstalar remove)
```

No Windows use `py baton.py ...`. Ao iniciar, uma página local mostra um **QR code**: escaneie com o celular. No iPhone, **Compartilhar > Adicionar à Tela de Início**; no Android, **⋮ > Instalar app**.

---

## 🧐 Sobre <a name="sobre"></a>

- **Modo externo** (padrão, sem PDF): envia setas, Home e End ao app em primeiro plano e desenha laser, foco, caneta e marca-texto numa camada transparente por cima de tudo, inclusive em tela cheia.
- **Modo tela** (com PDF): exibe o PDF no navegador com transições, passos dentro de um slide, notas do apresentador, cronômetro com meta, prévia do próximo slide, "Ir para" e zoom.
- **Cortina e efeitos**: preto, branco, teatro, fim com confete e efeitos sonoros sintetizados.
- **Modo residente**: em segundo plano, detecta apresentação em tela cheia e pergunta no celular antes de enviar qualquer tecla. Clicar no aviso do sistema abre a página local.
- **Zoom** (modo externo): amplia a projeção inteira (1,5x a 5x), centrada onde o dedo ou o apontador está. Usa uma captura do monitor; no Mac precisa da permissão de Gravação de Tela.
- **Ajustes** salvos em disco: cor e tamanho do laser, raio e desfoque do foco, espessura da caneta e do marca-texto.

---

## 🔧 Instalação <a name="instalacao"></a>

Requisitos: Python 3.8+. O celular conecta pelo Wi-Fi do computador (sem VPN) ou, de fora dele, pelo Tailscale (opcional, nos dois aparelhos). A página do QR code mostra um QR para cada caminho e o celular troca sozinho de um para o outro se a conexão cair.

```bash
./install.sh        # macOS e Linux (sem sudo)
.\install.ps1       # Windows (PowerShell, sem administrador)
./uninstall.sh      # ou .\uninstall.ps1
```

**Modo simples (laser por apontamento):** no controle, toque em "modo simples" (ou abra `/simples`): só Anterior, Próximo e um botão Laser. Segure o Laser e aponte o celular para a tela: o ponto acompanha o giro do aparelho (a pose ao apertar é o centro). Os sensores só funcionam em HTTPS: a página oferece o link `https://<ip>:8766` (certificado autoassinado, aceite o aviso uma vez; no iPhone o Safari pede também a permissão de movimento no primeiro toque). Sem HTTPS ou sem sensores, arraste o dedo sobre o botão.

**App no celular (PWA):** abra o modo simples pelo endereço HTTPS e toque em **Instalar** (Android) ou em Compartilhar > Adicionar à Tela de Início (iPhone/iPad). O ícone abre o Baton em tela cheia, sem barra do navegador. Em Ajustes escolha Destro ou Canhoto e o alcance do apontador.

**Pela internet (Cloudflare Tunnel):** aponte um hostname do túnel para `http://127.0.0.1:8765` e inicie o Baton com `--url-publica https://baton.exemplo.com`. O QR passa a oferecer esse endereço HTTPS (os sensores do modo simples funcionam sem aviso de certificado). Só o pareamento por QR de uso único dá acesso; o painel, o QR e o upload do computador ficam bloqueados para quem vem pelo túnel. Pelo túnel, tudo responde 404 exceto `/p/<código>` (o id do QR, de uso único) e as rotas do celular já pareado (com o token dele). `baton --instalar --url-publica https://baton.exemplo.com` grava a URL como padrão do Baton iniciado no login.

**Prévia sem PDF:** sem arquivo carregado o celular mostra uma captura da tela principal do computador (a apresentação em tela cheia) no lugar do slide atual, só para celulares pareados; `--sem-captura` desliga. Para o próximo slide, carregue o PDF no painel. No macOS libere o Baton em Ajustes > Privacidade > Gravação de Tela; no Linux use `grim` (Wayland) ou `import`/`maim`/`scrot` (X11), ou `pip install pillow`.

**Ícone na bandeja (Linux):** o GNOME não tem bandeja; o `install.sh` instala o AppIndicator e a extensão, e é preciso sair e entrar na sessão uma vez. KDE, XFCE e Cinnamon mostram o ícone direto.

**Windows sem instalar (portátil):** `python3 scripts/empacotar-windows.py` gera `dist/Baton-windows.zip` (Python embutido, pdf.js e QR offline, ~11 MB). **Pen-drive multi-sistema (Windows, Mac e Linux):** `python3 scripts/empacotar-pendrive.py --destino /Volumes/PENDRIVE` (pode rodar no Mac) monta `Baton/` com os lançadores portáteis, um Python embutido por sistema (~440 MB; `--so win,mac` reduz) e o repositório completo com `.git` em `repositorio/` (dá para instalar de vez com `install.sh`/`install.ps1` e atualizar com `git pull`, como quem clonou do GitHub); no computador externo abra `Baton.bat` (Windows), `Baton.command` (Mac) ou `Baton.sh` (Linux) direto do pen-drive, sem extrair nem instalar. Para rodar direto do pen-drive, sem extrair: `python3 scripts/empacotar-windows.py --destino /media/SEU_PENDRIVE` copia a pasta `Baton/` pronta; no Windows, abra `Baton\Baton.bat` de dentro do pen-drive (os dados ficam nele; o Windows não tem autoexecução de pen-drive, então é um duplo clique). Ou extraia o zip em qualquer pasta e abra `Baton.bat`: não precisa de Python, de instalação nem de administrador, e tudo fica na pasta `dados/` ao lado (nada no perfil do PC). Sem Tk no Python embutido, só a camada de desenho sobre outros apps fica indisponível; a tela cheia do Baton e o controle pelo celular funcionam normalmente. O Firewall pode pedir permissão para redes privadas.

**Mac, permissão de teclas:** se o Baton não aparecer em Acessibilidade, rode `baton --permissao` (ou use o botão no painel): ele pede a permissão pelo `Baton.app`, mostra o app no Finder e abre os Ajustes; se ainda não listar, clique em **+** e escolha `~/Applications/Baton.app`. `baton --diagnostico` imprime um resumo (Baton.app, assinatura, swiftc, launchd, log) para suporte.

Dependências opcionais:
- macOS: `swiftc` (`xcode-select --install`) para a camada de desenho; `terminal-notifier` para o aviso clicável; liberar o **Baton** em Acessibilidade.
- Linux: `xdotool` e `x11-utils` (teclas e detecção), PyGObject + Gtk 3 + pycairo (camada), `notify-send`.
- Windows: Python do python.org (inclui Tk).

---

## 🧭 Uso <a name="uso"></a>

**Vários celulares:** cada QR code vale para **um** celular: ao ser escaneado, o celular vira um dispositivo próprio (token próprio) e o QR muda na hora, então o segundo celular escaneia o QR novo e também entra, separado. O painel lista os celulares (conectado ou não) e tem **Desconectar** e **Parear novo celular**; o QR expira em 10 min. `baton --novo-token` desfaz o pareamento de todos. Tentativas com código errado são limitadas (8 por minuto por endereço).

**Ícone na bandeja:** instalado (modo residente), o Baton mostra um ícone na barra de menu (macOS), na bandeja (Windows) ou no indicador (Linux; no GNOME precisa da extensão AppIndicator) com: Pausar/Retomar, **Escolher apresentação...** (seletor de arquivo do sistema), Remover apresentação, Mostrar QR code, Abrir painel e Sair. `--sem-tray` desliga; `--tray` liga fora do modo residente.

**Sem terminal:** abra o painel (`http://localhost:8765/painel`, também acessível pelo link da página do QR code), solte o arquivo da apresentação (PDF, PPTX, ODP ou `.md` de notas) na área **Apresentação** e pronto: o celular recarrega sozinho com o slide atual, o próximo e as notas, e as teclas continuam indo para o app em primeiro plano (PowerPoint, Keynote, ReLaTeX em Modo Apresentação...). **Remover apresentação** volta ao modo só-teclas. `.pptx` precisa do LibreOffice para gerar a prévia.

```bash
baton --pausar | --retomar     # sem desinstalar
baton --detectar               # testa a detecção de tela cheia
python3 baton.py slides.pdf --notas slides.notas.md --transicao fade
```

Opções: `--tela N` (monitor do projetor), `--sem-overlay`, `--cursor`, `--proporcao 16:9`, `--novo-token`, `--porta`, `--sem-abrir`.

Painel local (pausar, modo, apps lembrados, início com o sistema, sair): `http://localhost:8765/painel`.

**Visão do apresentador (como no PowerPoint):** passe o arquivo junto com `--externo`. O celular mostra o slide atual, o próximo, o cronômetro e as notas, e continua enviando as teclas ao app em primeiro plano:

```bash
python3 baton.py apresentacao.pptx --externo     # notas lidas do próprio .pptx (converte em PDF com o LibreOffice)
python3 baton.py slides.pdf --externo --notas slides.notas.md
```

A posição é contada pelos toques, então comece a apresentação no slide 1 e use **Ir para** se sair de sincronia (animações dentro do slide contam como avanço). Sem arquivo, o Baton não conhece o conteúdo e não há prévia nem notas.

**Notas de PDF do beamer (`\note{}`):** compile com `\setbeameroption{show notes on second screen=right}`; o PDF sai com páginas largas (slide à esquerda, notas à direita) e o Baton detecta isso sozinho: mostra só o slide na prévia e no modo tela e lê as notas da metade direita (descarta o cabeçalho da página de notas). Funciona só com PDF passado na linha de comando (`baton slides.pdf --externo`); exemplo em `exemplo-notas-beamer.tex`. Notas digitadas no celular têm prioridade sobre as do PDF.

**Notas digitadas no celular (sem arquivo):** no painel de notas, **Editar** grava a nota do slide atual e **Todas** abre um campo para colar as notas inteiras em Markdown. Ficam salvas em `~/.cache/baton/notas-sessao.json` (por apresentação; sem arquivo, numa sessão "livre") e voltam sozinhas quando o Baton reabre. Sem arquivo, o número do slide é a contagem de toques (comece no slide 1). Com arquivo, o que você digita se soma às notas dele.

**Importar notas de um arquivo (sem abrir o arquivo na apresentação):** `baton --importar-notas apresentacao.pptx` (ou `.md`) lê as notas do PowerPoint e as grava na sessão; se o Baton estiver rodando, valem na hora. No painel (`http://localhost:8765/painel`) há o mesmo em "Notas do apresentador > escolher arquivo". A importação substitui as notas da sessão; depois dá para ajustar no celular.

Notas do apresentador em Markdown: `## 5` é o slide 5, `## p12` a página 12 do PDF; aceita `**negrito**`, `*itálico*` e listas. Veja `exemplo.notas.md`.

Atalhos no modo tela: `F` tela cheia, setas/espaço avançam, `B` preto, `W` branco, `T` teatro, `E` fim, `C` limpar, `Q` QR code.

---

## 🖥️ Plataformas <a name="plataformas"></a>

| Sistema | Teclas e mouse | Camada de desenho | Som |
| :-- | :-- | :-- | :-- |
| macOS | CoreGraphics | `overlay.swift` | `afplay` |
| Windows 10/11 | user32 | `overlay_tk.py` | `winsound` |
| Linux (X11/XWayland) | `xdotool` | `overlay_gtk.py` (ou Tk) | `paplay`, `aplay`, `ffplay` |

Wayland nativo não permite enviar teclas: use sessão X11. A camada macOS e o Windows ainda dependem de teste em máquina real.

---

## 📡 Sem internet e Bluetooth <a name="offline"></a>

O Baton não precisa de internet: precisa só de uma rede IP entre o celular e o computador. Funcionam, sem internet: o mesmo Wi-Fi de um roteador sem acesso à internet, o **hotspot do celular** (Wi-Fi, USB ou **Bluetooth**) e o compartilhamento de internet do Mac. A página do QR code lista todos os caminhos encontrados (Wi-Fi, Bluetooth, hotspot, Tailscale), um QR para cada, e o celular troca sozinho entre eles.

**Bluetooth (assistente no painel):** parear só não basta, porque o controle é uma página web e o Bluetooth sozinho não carrega páginas. O cartão **Sem internet (Bluetooth)** do painel mostra o passo a passo para iPhone e Android no seu sistema (macOS, Windows ou Linux) e o status ao vivo ("Aguardando o computador entrar na rede do celular..." e depois "Conectado por Bluetooth"). Em resumo: pareie os dois aparelhos, ative o compartilhamento por Bluetooth no celular (iPhone: Ponto de Acesso Pessoal; Android: Tethering Bluetooth) e conecte o computador a essa rede. Assim que a rede aparece, o QR code passa a usar o endereço dela (ordem: Bluetooth, hotspot, Wi-Fi, Tailscale).

**Modo leve:** o Bluetooth entrega 1 a 2 Mb/s. Quando o celular entra por Bluetooth ou hotspot, o Baton passa a servir o PDF em blocos (`Range`, 64 KB), lê as notas e a prévia só das páginas em uso, não calcula os passos do PDF inteiro e não envia laser e desenho ao celular (só à tela local). Passar slides e ver as notas continua imediato; o primeiro slide demora um pouco mais em PDFs grandes.

**Preparar antes de ficar sem internet:** `baton --preparar-offline` baixa o leitor de PDF e o gerador de QR code (o instalador já faz isso). `--preparar-offline --vendor` grava em `vendor/` ao lado do `baton.py`, que tem prioridade sobre o cache (útil para levar numa pasta ou pendrive).

**Só na primeira vez** o Baton baixa o leitor de PDF e o gerador de QR code (precisa de internet); depois ficam em cache em `~/.cache/baton` e tudo funciona offline.

## 🌐 Várias sessões: relay central <a name="relay"></a>

Uma URL pública (ex.: `https://baton.exemplo.com`, via Cloudflare Tunnel) aponta para um só computador. Para várias apresentações em paralelo, cada uma no seu PC, rode um **relay** no servidor e conecte cada Baton a ele: cada computador mantém sessão, QR e celulares próprios, e as sessões não se enxergam (o roteamento usa o código do QR e o token de cada celular). Mais de um celular pode escanear o mesmo QR e entrar na mesma sessão.

**Padrão: clonar e usar.** O Baton já vem apontando para o relay público (`baton.phrandrade.com`) e se registra sozinho, sem convite nem chave: clone, instale, abra e escaneie o QR (HTTPS e sensores no iPhone funcionam de qualquer rede). Se a internet falhar, o QR segue pela rede local. Para não usar o relay público: `--sem-relay-publico`, `--relay -` ou o cartão "Relay público" do painel (`localhost:8765/painel`). Os comandos dos slides (e o PDF e as notas, se o celular os carregar) passam por ele só em trânsito. Para rodar o seu próprio relay, veja abaixo e troque `RELAY_PADRAO` em `baton.py` (ou use `--relay wss://seu-dominio`). No relay, o painel liga e desliga o registro aberto; fechado, só entra quem tem convite. Limites do registro aberto: 3 conexões simultâneas por IP, 20% das vagas reservadas a convidados, respostas com campo de senha são cortadas e o administrador pode derrubar qualquer sessão.

**Sem login e sem coleta.** O relay não tem contas, não grava IP nem conteúdo e não recebe nome, sistema ou qualquer dado do computador: só repassa o tráfego entre o celular e o PC. Em disco ficam apenas o hash da chave de cada computador autorizado e o rótulo que o administrador deu ao convite; quem está online e quantos celulares estão conectados existem só em memória. Tudo é código aberto neste repositório.

```bash
# no servidor (aponte o túnel para a porta do relay, WebSocket incluído)
[![Estrelas](https://img.shields.io/github/stars/pedroiff0/baton?style=flat&logo=github)](https://github.com/pedroiff0/baton/stargazers)
BATON_RELAY_CHAVE='chave-de-administrador-longa' baton --servir-relay --relay-porta 8780

# convite de uso único (vale 24 h) para cada computador novo
baton --criar-convite "Mac do instituto"        # mostra os comandos prontos
# na máquina da pessoa:
baton --convite baton.exemplo.com/ABCD-EFGH-JKLM
# ou instalando de uma vez:
git clone https://github.com/pedroiff0/baton && cd baton && BATON_CONVITE=baton.exemplo.com/ABCD-EFGH-JKLM ./install.sh
```

O convite é trocado por uma chave própria do computador (guardada só nele); a chave de administrador nunca sai do servidor. Para o Windows portátil, `python3 scripts/empacotar-windows.py --convite baton.exemplo.com/CODIGO` leva um convite no zip e o Baton entra no relay sozinho no primeiro uso: o usuário só abre o app, joga a apresentação (ou põe um slide em tela cheia) e escaneia o QR.

**Painel da central:** `https://baton.exemplo.com/relay/painel` (entra com a chave de administrador; `baton --painel-link` no servidor mostra um link que entra direto, e o convite sai como link `…/relay/convite/CODIGO` com QR, que mostra o comando certo para o sistema de quem abre; `baton --relay-status` e `baton --atualizar-relay` cuidam do servidor): lista os computadores com status online, tempo e celulares conectados agora; cria convites com os comandos prontos para copiar; renomeia, cancela convites e revoga computadores (desconecta na hora). Botões de volume do celular não chegam a nenhuma página web (iOS e Android os consomem); use os controles de mídia do sistema, fones ou um passador de slides Bluetooth.

## 🔒 Segurança <a name="seguranca"></a>

O servidor escuta em todas as interfaces (Wi-Fi e Tailscale) e o Baton nunca o abre na internet. Na rede local o tráfego é HTTP sem criptografia: use só em Wi-Fi de confiança. Tudo que importa (PDF, eventos, comandos, manifesto) exige o token; a página do QR code e o painel só abrem no próprio computador. O celular precisa do token da URL; o computador local não. Quem tem a URL com o token controla o computador: não compartilhe o QR code. Pausado, nenhum comando é aceito.

---

## 🧪 Testes <a name="testes"></a>

```bash
python3 -m unittest discover -s tests -v
BATON_BACKEND=log BATON_OVERLAY=log python3 baton.py --sem-abrir   # sem enviar teclas
```

Estrutura: `baton.py` (servidor, páginas web, modo externo), `residente.py` (modo residente), `overlay*.{swift,py}` (camadas), `launcher.swift` (`Baton.app` e barra de menu no macOS), `tray_win.ps1` e `tray_gtk.py` (bandeja no Windows e Linux), `tests/`.

---

## 🤝 Contribuição <a name="contribuicao"></a>

- Abra issues/pull requests neste repositório.
- Mantenha apenas a biblioteca padrão do Python.
- Adicione testes em `tests/` para novo comportamento.

---

**Licença:** MIT. O pdf.js (Apache-2.0) e o qrcode-generator (MIT) são baixados na primeira execução e não fazem parte do repositório.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-4EAA25?style=flat&logo=gnubash&logoColor=white)
![Swift](https://img.shields.io/badge/Swift-F05138?style=flat&logo=swift&logoColor=white)

## Autores

<table>
  <tr>
    <td align="center"><a href="https://github.com/pedroiff0"><img src="https://github.com/pedroiff0.png?size=120" width="96" height="96" alt="Pedro Henrique Rocha de Andrade" /><br /><sub><b>Pedro Henrique Rocha de Andrade</b></sub></a><br />Autor e mantenedor</td>
  </tr>
</table>

### Contribuidores

[![Contribuidores](https://contrib.rocks/image?repo=pedroiff0/baton)](https://github.com/pedroiff0/baton/graphs/contributors)
