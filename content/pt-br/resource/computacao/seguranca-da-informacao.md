---
publish: false
title: Segurança da Informação
created: 2026-07-18 13:04
modified: 2026-08-27 21:54
published: 2026-07-26T11:33:09.979-03:00
tags:
  - recursos
  - computacao
cssclasses:
  - page-layout
---

> [!info] Segurança da informação é a disciplina de proteger sistemas e dados contra acesso, alteração e destruição indevidos — da criptografia que protege sua senha ao pentest que encontra a falha antes do atacante. Hoje é responsabilidade de todo desenvolvedor, não só de especialistas.

> [!warning] O curso não tem uma disciplina dedicada a segurança — o tema aparece diluído nas disciplinas de redes. Isso é mais um motivo, não menos, para estudar por conta própria: o mercado cobra esse conhecimento de qualquer profissional, e a lacuna curricular é sua chance de se diferenciar.

## Por que estudar isso?

Em 2021, vazamentos expuseram dados de mais de 220 milhões de brasileiros — CPF, endereço, renda. Casos assim raramente envolvem técnicas sofisticadas: a porta de entrada costuma ser uma injeção de SQL trivial, uma senha padrão esquecida, um servidor sem atualização. Ou seja: falhas que o _desenvolvedor_ comum cometeu e que o _desenvolvedor_ com formação em segurança teria evitado. Com a LGPD em vigor, essas falhas também viram multa e processo — segurança deixou de ser opcional para virar requisito legal.

Para quem gosta da área, a carreira é das mais aquecidas da computação, com déficit global crônico de profissionais. E mesmo para quem não vai se especializar, pensar como atacante ("como eu quebraria isso?") muda permanentemente a qualidade do código que você escreve.

## Trilha de estudo

### 1. Fundamentos e mentalidade (iniciante)

Comece pela tríade CIA (confidencialidade, integridade, disponibilidade), os tipos de ameaça e o vocabulário: vulnerabilidade, exploit, vetor de ataque, superfície de ataque. Pré-requisito real: redes (TCP/IP, portas, DNS) e um mínimo de Linux e linha de comando. As trilhas iniciais do [TryHackMe](https://tryhackme.com/) ensinam exatamente essa base de forma guiada e legal. Tempo típico: 4 a 6 semanas.

### 2. Segurança de aplicações web (intermediário)

O terreno mais prático e empregável: estude o OWASP Top 10 — injeção de SQL, XSS, quebra de autenticação, configurações inseguras — entendendo o mecanismo de cada ataque e a defesa correspondente. Pratique nos laboratórios deliberadamente vulneráveis (o projeto Juice Shop, da própria [OWASP](https://owasp.org/), é o padrão). Nunca em sistemas de terceiros sem autorização. Tempo típico: 6 a 8 semanas.

### 3. Criptografia aplicada e segurança de redes (intermediário-avançado)

Entenda o que cada primitiva garante: criptografia simétrica vs. assimétrica, hashes, assinaturas digitais, certificados e TLS — o suficiente para _usar_ criptografia corretamente, que é o que 99% dos profissionais precisa. Do lado de redes: firewalls, segmentação, VPNs, e análise de tráfego com [Wireshark](https://www.wireshark.org/). Tempo típico: 6 a 8 semanas.

### 4. Prática ofensiva e CTFs (avançado)

Consolide atacando (legalmente): capture-the-flag no [picoCTF](https://picoctf.org/) e máquinas do [TryHackMe](https://tryhackme.com/), cobrindo reconhecimento, exploração e escalada de privilégios. CTF é o equivalente da maratona de programação para segurança: viciante, formativo e ótimo no currículo. Tempo típico: contínuo — a área exige atualização permanente.

## Conceitos que você precisa dominar

- **Tríade CIA** — confidencialidade (só quem deve vê), integridade (ninguém altera sem autorização) e disponibilidade (o serviço está de pé quando precisam). Todo controle de segurança existe para proteger uma dessas três propriedades, e todo ataque viola pelo menos uma — é o quadro de referência para analisar qualquer incidente.
- **Autenticação vs. autorização** — autenticação prova quem você é (senha, biometria, segundo fator); autorização decide o que você pode fazer. Confundir as duas gera a clássica falha de sistemas que verificam o login mas não checam se _aquele_ usuário pode acessar _aquele_ recurso — o IDOR do OWASP Top 10.
- **Injeção (SQL injection e parentes)** — o ataque nasce quando dado do usuário é interpretado como código: um campo de formulário que vira comando SQL. A defesa (consultas parametrizadas) é trivial, e mesmo assim injeção segue entre as falhas mais exploradas do mundo — porque a cada geração, desenvolvedores novos repetem o erro.
- **Cross-Site Scripting (XSS)** — injeção de JavaScript em páginas vistas por outros usuários, permitindo roubar sessões e agir em nome da vítima. Ensina a lição mais geral da segurança web: toda entrada é hostil até que se prove o contrário, e a sanitização depende do contexto onde o dado será usado.
- **Criptografia simétrica vs. assimétrica** — na simétrica (AES), a mesma chave cifra e decifra: rápida, mas exige combinar a chave antes. Na assimétrica (RSA, curvas elípticas), a chave pública cifra e só a privada decifra — resolvendo a distribuição de chaves. TLS usa as duas: assimétrica para o aperto de mãos, simétrica para o volume de dados.
- **Hash e sal (salt)** — funções de mão única que transformam qualquer dado numa impressão digital de tamanho fixo. Senhas jamais se armazenam: armazena-se o hash, com sal único por usuário e algoritmo lento de propósito (bcrypt, Argon2) — para que um vazamento do banco não entregue as senhas de bandeja.
- **Superfície de ataque e defesa em profundidade** — a superfície é tudo que está exposto (portas, endpoints, formulários, dependências); reduzi-la é a primeira defesa. A segunda é assumir que qualquer camada pode falhar e empilhar controles independentes — firewall E autenticação E validação E monitoramento, não apenas um deles.
- **Engenharia social** — o ataque ao humano em vez da máquina: phishing, pretexting, o "suporte técnico" que liga pedindo a senha. A maioria dos grandes incidentes começa assim, e nenhum firewall resolve — por isso segurança é também processo e cultura, não só tecnologia.

## Erros comuns de quem está começando

- **Querer "aprender a hackear" sem a base de redes e sistemas.** Rodar ferramenta pronta sem entender o que ela faz forma script kiddies, não profissionais. O caminho real é: redes → Linux → web → e então segurança faz sentido.
- **Testar em sistemas reais sem autorização.** Além de crime (Lei Carolina Dieckmann, art. 154-A do Código Penal), é desnecessário: TryHackMe, picoCTF e laboratórios locais oferecem alvos legais idênticos aos reais. Pentest profissional se faz com contrato e escopo assinado.
- **Inventar a própria criptografia.** A regra de ouro da área: use bibliotecas estabelecidas e auditadas. Todo esquema caseiro de cifrar dados que já apareceu em código de iniciante estava quebrado — sem exceção conhecida.
- **Tratar segurança como etapa final do projeto.** "Depois a gente adiciona segurança" produz retrabalho e brechas estruturais. Validação de entrada, controle de acesso e tratamento de segredos são decisões de arquitetura, não verniz.
- **Achar que o firewall (ou o antivírus, ou o HTTPS) resolve tudo.** Cada controle protege contra uma classe específica de ataque. HTTPS protege o dado em trânsito e não faz nada contra SQL injection; o firewall não impede phishing. Segurança é o conjunto, nunca uma bala de prata.

## 📚 Materiais recomendados

**Livros abertos (licença pública):**

- **[Segurança da Informação](/assets/biblioteca/computacao/seguranca-da-informacao-ifro.pdf)** (Rede e-Tec Brasil / IFRO) — apostila em português cobrindo fundamentos, políticas de segurança e proteção de sistemas; boa porta de entrada no vocabulário da área. Disponível no portal [Proedu](https://proedu.rnp.br), repositório público da Rede e-Tec.

## 🔗 Referências externas

- [Roadmap: Cyber Security](https://roadmap.sh/cyber-security) — o mapa completo da carreira em segurança, dos fundamentos às especializações (ofensiva, defensiva, GRC). Use para se orientar e escolher um ramo.
- [OWASP](https://owasp.org/) — a fundação que define os padrões de segurança de aplicações: o Top 10, cheat sheets de defesa e o Juice Shop para praticar. Referência obrigatória para qualquer desenvolvedor web.
- [TryHackMe](https://tryhackme.com/) — laboratórios guiados no navegador, do zero absoluto ao pentest. A porta de entrada mais didática da área; as trilhas iniciais são gratuitas.
- [picoCTF](https://picoctf.org/) — CTF educacional gratuito da Carnegie Mellon, com desafios permanentes de criptografia, web, forense e engenharia reversa. Ideal para transformar estudo em jogo.
- [Wireshark](https://www.wireshark.org/) — análise de tráfego de rede: indispensável para o lado defensivo (detectar o estranho no fio) e para entender como os ataques aparecem na prática.

## Conexão com as disciplinas do curso

Não há disciplina dedicada de segurança na grade — o tema aparece dentro das disciplinas de redes, e o restante é por sua conta (use este guia como trilha):

- [[pt-br/resource/engenharia-de-computação/7-periodo/redes-de-computadores-i|Redes de Computadores I]] — a base indispensável: TCP/IP, portas e serviços são o alfabeto de qualquer análise de segurança.
- [[pt-br/resource/engenharia-de-computação/8-periodo/redes-de-computadores-ii|Redes de Computadores II]] — onde aparecem os tópicos de segurança de redes: firewalls, VPNs e proteção de perímetro.
