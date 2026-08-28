---
publish: false
title: Redes
created: 2026-07-18 13:04
modified: 2026-08-27 21:59
published: 2026-07-26T11:33:09.975-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] Redes de computadores é o estudo de como máquinas trocam informação: dos bits no cabo até o navegador carregando uma página. É a infraestrutura invisível de praticamente tudo que você usa — e uma das áreas com mais oferta de trabalho em infraestrutura, cloud e DevOps.

## Por que estudar isso?

Pense no que acontece quando você digita um endereço no navegador e aperta Enter: uma consulta DNS resolve o nome para um IP, uma conexão TCP é aberta com handshake de três vias, uma requisição HTTP viaja encapsulada em pacotes IP que atravessam dezenas de roteadores, e a resposta volta pelo mesmo caminho — tudo em menos de um segundo. Quem não entende essa cadeia enxerga a internet como mágica; quem entende consegue diagnosticar por que "o sistema está lento", configurar um servidor de verdade e projetar sistemas distribuídos que funcionam.

Na prática profissional, redes aparece em todo lugar: o desenvolvedor backend que precisa entender latência e timeouts, o cientista de dados que sobe um serviço na nuvem, o engenheiro que configura a rede industrial de uma planta. No curso, é também uma das sequências mais longas — de Comunicação de Dados no 6º período até as eletivas de interconexão e dimensionamento — então construir uma base sólida cedo rende juros por anos.

## Trilha de estudo

### 1. Fundamentos e modelos de referência (iniciante)

Domine o vocabulário: o que é protocolo, encapsulamento, comutação de pacotes vs. circuitos, e os modelos OSI e TCP/IP como mapas mentais das camadas. Pratique identificando em qual camada cada tecnologia vive (Ethernet? IP? TCP? HTTP?). Instale o [Wireshark](https://www.wireshark.org/) e capture o tráfego da sua própria máquina — ver os pacotes de verdade vale mais que dez diagramas. Tempo típico: 4 a 6 semanas.

### 2. Endereçamento e camada de rede (intermediário)

Aqui mora o IP: endereçamento IPv4 e IPv6, máscaras de sub-rede, CIDR, NAT e o funcionamento de roteadores. Pratique cálculo de sub-redes até virar automático (é presença garantida em provas e entrevistas) e monte topologias em simuladores de rede. Tempo típico: 6 a 8 semanas.

### 3. Transporte, aplicação e serviços (intermediário-avançado)

Entenda TCP a fundo — handshake, controle de congestionamento, retransmissão — e quando UDP é a escolha certa. Estude os protocolos de aplicação que você usa todo dia: DNS, HTTP/HTTPS, DHCP, SMTP. Pratique subindo seus próprios serviços em máquinas virtuais: um servidor web, um DNS local, um DHCP. Tempo típico: 6 a 8 semanas.

### 4. Roteamento dinâmico e projeto de redes (avançado)

Protocolos de roteamento (OSPF, BGP), VLANs, redes sem fio, qualidade de serviço e dimensionamento — quanta banda, quantos equipamentos, qual topologia. É o conteúdo das eletivas e o que separa quem "sabe redes" de quem projeta redes. Tempo típico: 8+ semanas, idealmente com laboratório.

## Conceitos que você precisa dominar

- **Modelo em camadas (OSI e TCP/IP)** — a ideia central de redes: cada camada resolve um problema e oferece serviço à camada de cima, sem precisar conhecer os detalhes das de baixo. É o que permite trocar Wi-Fi por cabo sem reescrever o navegador. Use o modelo como ferramenta de diagnóstico: problema de cabo é camada física, problema de DNS é aplicação.
- **Encapsulamento** — cada camada embrulha os dados da camada superior com seu próprio cabeçalho: a mensagem HTTP vira segmento TCP, que vira pacote IP, que vira quadro Ethernet. Entender isso é o que faz uma captura de Wireshark deixar de ser um amontoado de bytes e virar uma história legível.
- **Endereçamento IP e sub-redes** — como identificar máquinas e dividir redes logicamente. Máscara, CIDR e endereço de broadcast precisam estar na ponta da língua: praticamente toda configuração de rede real começa por "qual é a faixa de IPs?".
- **TCP vs. UDP** — TCP garante entrega ordenada ao custo de latência e overhead; UDP entrega rápido sem garantias. Saber escolher explica por que streaming de vídeo e jogos usam UDP enquanto transferência de arquivos usa TCP.
- **DNS** — o sistema distribuído que traduz nomes em endereços IP, com hierarquia de servidores e cache em vários níveis. Metade dos "problemas de internet" do mundo real são, no fundo, problemas de DNS.
- **Roteamento** — como os pacotes descobrem o caminho entre redes: tabelas de rotas, gateway padrão e os protocolos dinâmicos (OSPF dentro de uma organização, BGP entre organizações — o BGP é literalmente o que mantém a internet inteira de pé).
- **NAT** — a tradução de endereços que permite milhares de dispositivos compartilharem um único IP público. Explica desde por que seu roteador doméstico funciona até por que certas aplicações P2P penam para conectar.

## Erros comuns de quem está começando

- **Decorar as camadas do OSI sem saber usá-las.** Recitar "física, enlace, rede..." não vale nada; o valor do modelo é localizar problemas e tecnologias. Pergunte-se sempre: "isso opera em qual camada, e o que isso implica?"
- **Pular o cálculo de sub-redes por achar "chato".** É a habilidade mais cobrada em prova, certificação e no dia a dia de infraestrutura. Sem fluência aqui, tudo que vem depois (roteamento, VLANs, firewall) fica nebuloso.
- **Estudar só na teoria, sem nunca capturar um pacote.** Redes é disciplina de laboratório. Wireshark, simuladores e máquinas virtuais transformam abstrações em coisas observáveis — e a diferença na retenção é brutal.
- **Tratar "internet lenta" como um problema único.** Latência, banda, perda de pacotes e jitter são coisas diferentes com causas diferentes. Aprender a medir cada uma (ping, traceroute, iperf) é o começo do diagnóstico sério.

## 📚 Materiais recomendados

**Livros abertos (licença pública):**

- **[Redes de Computadores](/assets/biblioteca/computacao/redes-de-computadores-ifro.pdf)** (Rede e-Tec Brasil / IFRO) — apostila introdutória em português, ótima primeira leitura. Disponível no portal [Proedu](https://proedu.rnp.br), repositório público da Rede e-Tec.
- **[Redes de Computadores II](/assets/biblioteca/computacao/redes-de-computadores-2-etec.pdf)** (Rede e-Tec Brasil) — continuação cobrindo roteamento e serviços de rede. Também no [Proedu](https://proedu.rnp.br).
- **[Protocolos e Serviços de Redes](/assets/biblioteca/computacao/protocolos-servicos-redes-etec.pdf)** (Escola Técnica Aberta) — foco na pilha TCP/IP e nos serviços do dia a dia (DNS, DHCP, HTTP). No [Proedu](https://proedu.rnp.br).

**Bibliografia clássica (procure na biblioteca do campus):**

- KUROSE, J.; ROSS, K. _Redes de Computadores e a Internet: uma abordagem top-down_. A referência moderna — começa pela aplicação e desce até o físico, o que torna a leitura muito mais motivadora.
- FOROUZAN, B. _Comunicação de Dados e Redes de Computadores_. Mais detalhista na transmissão e nas camadas baixas; complementa o Kurose.

## 🔗 Referências externas

- [Roadmap: DevOps](https://roadmap.sh/devops) — o módulo de redes deste roadmap mostra exatamente o que o mercado de infraestrutura/cloud espera que você saiba. Use como checklist de empregabilidade.
- [Roadmap: Computer Science](https://roadmap.sh/computer-science) — situa redes dentro do panorama geral de fundamentos de computação; bom para decidir o que estudar antes e depois.
- [Wireshark](https://www.wireshark.org/) — o analisador de pacotes padrão da indústria, gratuito. Use desde a primeira semana: capture seu próprio tráfego e identifique os protocolos que viu na aula.
- [MDN Web Docs](https://developer.mozilla.org/) — a melhor referência gratuita sobre HTTP, cabeçalhos, cache e HTTPS. Consulte quando chegar na camada de aplicação.

## Conexão com as disciplinas do curso

- [[pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados|Comunicação de Dados]] — a base física e de enlace: como os bits realmente viajam.
- [[pt-br/resource/engenharia-de-computação/7-periodo/redes-de-computadores-i|Redes de Computadores I]] — o núcleo: modelos de referência, IP, TCP/UDP e os principais protocolos.
- [[pt-br/resource/engenharia-de-computação/8-periodo/redes-de-computadores-ii|Redes de Computadores II]] — roteamento, serviços e tópicos avançados.
- [[pt-br/resource/engenharia-de-computação/eletivas/interconexao-de-redes-de-computadores|Interconexão de Redes de Computadores]] — eletiva sobre como redes distintas se conectam: roteamento entre domínios e equipamentos de borda.
- [[pt-br/resource/engenharia-de-computação/eletivas/dimensionamento-de-redes-de-computadores|Dimensionamento de Redes de Computadores]] — eletiva de projeto: calcular capacidade e planejar redes que aguentam a carga prometida.
