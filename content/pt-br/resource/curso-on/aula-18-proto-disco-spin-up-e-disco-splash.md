---
publish: false
title: Aula 18 — Proto-Disco, Spin-Up e o Disco Splash
created: 2026-07-25 12:36
modified: 2026-08-27 21:59
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - historia-da-via-lactea
  - gaia-sausage-enceladus
cssclasses:
  - page-grid
  - center-images
encrypted: true
discipline: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
content: Cronologia da evolução galáctica (parte 1) — do pipeline observacional aos parâmetros orbitais, a Via Láctea proto-galáctica (Kraken, Heracles, Aurora e outras candidatas), o disco primordial em z~3, o spin-up do disco e o disco "splash" aquecido pela fusão GSE
professor: Hélio Dotto Perottoni
---

# 🌅 Aula 18 — Proto-Disco, Spin-Up e o Disco Splash

> [!note] Resumo
> Primeira metade da aula de síntese do curso: como ir de observações brutas (astrometria, fotometria, espectroscopia) a parâmetros orbitais completos, e como isso reconstrói a cronologia mais antiga da Via Láctea — desde as candidatas a "proto-galáxia" (Kraken, Heracles, Aurora, entre outras), passando pela evidência de um disco já presente em $z\sim3$, o "spin-up" do disco em rotação, até o disco "splash" — estrelas do disco primordial aquecidas e lançadas para órbitas quase-halo pela fusão Gaia-Sausage-Enceladus.

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni
> **Fonte:** slides oficiais da disciplina — "Cronologia da evolução galáctica" (primeira metade)

---

## 🎯 Por que a Via Láctea é um "laboratório" único

Arqueologia galáctica é o uso de informação sobre populações estelares para reconstruir a sequência de eventos que formou a estrutura atual da Galáxia. A Via Láctea é a **única** galáxia onde é possível ter informação detalhada, estrela a estrela, para amostras de milhões de objetos — por isso, o que se aprende sobre ela funciona como modelo (_template_) para a formação de galáxias em geral.

## 🧮 Do dado bruto aos parâmetros orbitais

Reconstruir a órbita completa de uma estrela combina várias camadas de informação: **astrometria** (paralaxes), **fotometria multibanda**, **espectroscopia** (parâmetros estelares) e **modelos/isócronas estelares**, tudo combinado por um código Bayesiano espectrofotométrico como o **StarHorse** (já mencionado na Escola de Inverno) para produzir a distribuição estelar 3D da Galáxia.

O mesmo tipo de pipeline se estende aos **parâmetros orbitais**: partindo de quantidades observadas (RA, Dec, distância, movimentos próprios, velocidade radial), assumindo um potencial axissimétrico $\Phi(x,y,z)$ e parâmetros galácticos fundamentais, gera-se $N$ realizações de Monte Carlo (propagando incertezas, como visto no curso-on Aula 10) para obter as integrais de movimento $(E, J_R, J_\phi, J_z)$ a partir da informação de espaço de fase $(X,Y,Z,v_x,v_y,v_z)$.

> [!tip] Por que isso funciona mesmo para debris completamente disperso
> Uma animação clássica (créditos: Ana Bonaca) mostra várias galáxias anãs "jogadas" no potencial de um modelo da Via Láctea: por mais que se disrompam espacialmente ao longo do tempo, **conservam** quantidades cinemáticas como energia orbital total e momento angular — o mesmo princípio (Helmi et al. 1999, curso-on Aula 12) que permite reconhecer debris de fusões antigas no espaço $(E, L_z)$ muito depois de qualquer coerência espacial ter desaparecido.

## 🕰️ A cronologia da Via Láctea, em uma figura

Um resumo recorrente ao longo desta aula organiza a história galáctica em quatro estágios aproximados (o mesmo roteiro já introduzido no curso-on Aula 01):

| Estágio | Época | O que acontece |
|---|---|---|
| Formação do disco | $z\sim7$, $>11$ Gyr | Proto-Via Láctea + _spin-up_ (Semenov+2024; Xiao+2025) |
| Gaia-Sausage-Enceladus | $z>2$, $\sim$11-9 Gyr | Disco aquecido/_splash_ + _starburst_ + halo interno + possível _warp_ (Naidu+2021) |
| Sagittarius dSph | $2>z>0{,}3$, $\sim$5 Gyr | Sobredensidades estelares no disco + aumento da taxa de formação estelar (Ruiz-Lara+2020) |
| Nuvens de Magalhães | $z<0{,}3$, $>{\sim}3{,}5$ Gyr | Halo "desperta" com a primeira aproximação (Lucchini+2020) |

## 👶 A proto-Via Láctea: candidatas em debate

Diversos trabalhos recentes (2019-2025) propõem estruturas antigas e massivas, possivelmente formadas ainda antes ou durante a fase mais primitiva da Galáxia, com nomes distintos conforme o grupo que as identificou — **Kraken**, **Koala**, **Heracles**, **Aurora**, **"Poor Old Heart"**, **Pangu** (Kruijssen+2019/2020; Forbes 2020; Horta+2021; Rix+2022; Belokurov & Kravtsov 2022; Xiang+2025). Não há ainda consenso sobre quantas dessas estruturas são de fato distintas entre si (ou do próprio _in situ_ mais antigo da Galáxia) — um dos debates mais ativos da área hoje.

## 🌀 O disco primordial e o "spin-up"

Evidências recentes (Sestito+2019/2020/2021; Di Matteo+2020; Cordoni+2021; Re Fiorentin+2021; Carollo+2023; Bellazzini+2024; Xiang+2025; Borbolato+2025, entre muitos outros) sugerem que discos finos já estavam presentes em redshifts tão altos quanto $z\sim3$ — um **disco primordial** anterior a qualquer fusão importante. A transição desse material proto-galáctico, dominado por movimento aleatório/dispersão, para um disco genuinamente rotacional é o **spin-up** (Chandra+2024; Semenov+2024) — o próprio mecanismo listado como primeiro estágio na tabela acima.

## 💦 O disco "splash": estrelas de disco lançadas ao halo

Um dos resultados mais marcantes é a identificação de um componente **metal-rico mas cinematicamente parecido com halo** — o disco **"splash"** (Belokurov+2020; ver também Amarante+2020) — interpretado como estrelas do disco primordial que existiam **antes** da fusão GSE e foram dinamicamente **aquecidas e "chacoalhadas"** (_kicked out_) pelo próprio impacto do merger, ficando com órbitas quentes/excêntricas apesar de reter a química de disco (metal-rica). É uma peça chave para entender por que nem toda estrela halo-like é necessariamente acretada.

## ⚖️ Disco fino vs. disco espesso: co-formação, não sequência simples

O quadro clássico do **Two-Infall Model** (curso-on Aula 17) supõe duas épocas de queda de gás separadas, formando primeiro o disco espesso e depois o fino. Trabalhos mais recentes revisitam essa separação:

- **Co-formação** de disco fino e espesso (Silva Aguirre+2018; Beraldo e Silva+2021; Nepal+2024; Gent+2024; Borbolato+2026) — a transição entre os dois pode não exigir um evento distinto de fusão rica em gás para mediá-la.
- Modelos _two-infall_ **não reproduzem com precisão** a bimodalidade observada (Spitoni+2019).
- A bimodalidade química fino/espesso **não é causada por migração radial** (Amarante+2026) — descartando uma explicação puramente dinâmica que competiria com a explicação química (curso-on Aula 17).
- Um **disco fino "splash"** também foi proposto (Nepal+2024; Borbolato+2026/submetido): mesmo a formação do disco fino pode ter uma componente aquecida por interação, e a própria **GSE não seria essencial** para a formação do disco fino como um todo.

> [!warning] Um campo em movimento rápido
> Note que boa parte das referências desta aula é de 2024-2026 — muitas dessas conclusões (co-formação sem merger mediador, bimodalidade não causada por migração, GSE não essencial ao disco fino) são resultados recentes e ainda sendo debatidos ativamente pela comunidade, não fatos estabelecidos há décadas como a classificação OBAFGKM ou a nucleossíntese estelar.

---

## 📌 Conceitos-chave

- **Pipeline observacional → orbital:** astrometria + fotometria + espectroscopia + isócronas (via StarHorse) → parâmetros estelares → integração de órbitas → integrais de movimento $(E, J_R, J_\phi, J_z)$.
- **Cronologia em 4 estágios:** formação do disco/spin-up ($>11$ Gyr) → GSE (~11-9 Gyr) → Sagitário (~5 Gyr) → Nuvens de Magalhães (>~3,5 Gyr).
- **Candidatas de proto-Via Láctea:** Kraken, Koala, Heracles, Aurora, "Poor Old Heart", Pangu — estruturas antigas propostas, ainda sem consenso sobre distinção entre si.
- **Disco primordial em $z\sim3$:** evidência de que discos finos já existiam antes de qualquer fusão relevante.
- **Spin-up:** transição de um proto-disco dominado por dispersão para um disco genuinamente rotacional.
- **Disco splash:** componente metal-rico, cinematicamente quente, interpretado como disco primordial aquecido pelo impacto da fusão GSE.
- **Co-formação disco fino/espesso:** evidência recente de que a separação fino/espesso pode não exigir um merger mediador distinto, nem ser explicada por migração radial.

## 🔗 Referências e correlatos

- Helmi et al. (1999) — conservação de $E$, $L_z$ em debris, já citada no curso-on Aula 12
- Kruijssen et al. (2019, 2020); Belokurov & Kravtsov (2022) — candidatas de proto-Via Láctea
- Sestito et al. (2019, 2020, 2021) — disco primordial em alto redshift
- Belokurov et al. (2020); Amarante et al. (2020) — disco splash
- Borbolato et al. (2026, submetido); Amarante et al. (2026); Spitoni et al. (2019) — revisão recente da co-formação disco fino/espesso
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-10-integracao-de-orbitas-com-galpy|Aula 10 — Integração de Órbitas com galpy]] — o mesmo pipeline de Monte Carlo para parâmetros orbitais, aqui aplicado à cronologia galáctica
- [[pt-br/resource/curso-on/aula-17-gradientes-de-metalicidade-e-amr|Aula 17 — Gradientes de Metalicidade e a Relação Idade-Metalicidade]] — o Two-Infall Model revisitado aqui à luz de evidências mais recentes
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula02|Escola de Inverno — Arqueologia Galáctica, Aula 02]] — a mesma cronologia em 4 estágios já introduzida ali, com Omega Centauri como um dos casos discutidos
- [[pt-br/resource/curso-on/aula-19-gse-e-subestruturas-do-halo|Aula 19 — O Merger Gaia-Sausage-Enceladus e as Subestruturas do Halo]] — continuação direta: o mecanismo detalhado da fusão que produziu o disco splash
