---
publish: false
title: Aula 08 — Velocidades e Movimento Próprio
created: 2026-07-23
modified: 2026-08-27
published: 2026-07-26T11:33:09.983-03:00
tags:
  - curso-on
  - arqueologia-galactica
  - populacoes-estelares
  - cinematica-estelar
cssclasses:
  - page-grid
  - center-images
encrypted: true
titulo: CursoON-Aula08
disciplina: Arqueologia Galáctica e Populações Estelares (Observatório Nacional)
conteudo: Velocidade radial e tangencial, o Padrão Local de Repouso e o movimento próprio das estrelas
professor: Hélio Dotto Perottoni
---

# 🚀 Aula 08 — Velocidades e Movimento Próprio

> [!note] Resumo
> A última peça do quebra-cabeça (posição, química, idade e agora cinemática): como decompor a velocidade espacial de uma estrela em componentes radial e tangencial, e como referenciá-las ao Padrão Local de Repouso da Galáxia — a base observacional para qualquer estudo de dinâmica estelar (Unidade 3 da ementa).

> [!info] Informações da aula
> **Disciplina:** Arqueologia Galáctica e Populações Estelares
> **Instituição:** Observatório Nacional (ON)
> **Professor:** Hélio Dotto Perottoni

---

## 🎯 Velocidade radial e tangencial

A velocidade espacial de uma estrela, com respeito ao Sol, decompõe-se em dois vetores:

- **Velocidade radial ($v_R$):** ao longo da linha de visada, medida pelo **desvio Doppler** de linhas espectrais.
- **Velocidade tangencial:** perpendicular à linha de visada, medida por técnicas **astrométricas** (movimento próprio + distância).

$v_R = c\,\frac{\Delta\lambda}{\lambda_0}$

onde $\Delta\lambda$ é o deslocamento Doppler e $\lambda_0$ o comprimento de onda de repouso da transição. O que é medido diretamente ao telescópio é a $v_R$ **topocêntrica**, que precisa ser corrigida sucessivamente para o centro da Terra ($v_R$ geocêntrica) e depois para o centro do Sol ($v_R$ heliocêntrica).

## 🗺️ Referencial das velocidades espaciais

O referencial de velocidades na Galáxia baseia-se no sistema de coordenadas galácticas cartesianas (Aula 07), com as mesmas ambiguidades de convenção quanto à direção do eixo radial. As componentes cartesianas de velocidade chamam-se $(U,V,W)$; quando reduzidas ao **Referencial de Repouso da Galáxia**, usam-se as componentes cilíndricas $(\Pi,\Theta,Z)$ que, na vizinhança solar, coincidem numericamente com $(U,V,W)$.

## 🧭 Padrão Local de Repouso (LSR)

O **LSR** é definido pela velocidade **média** das estrelas na vizinhança solar. Como o único movimento global dessa vizinhança é rotacional, o LSR corresponde à velocidade circular na posição do Sol:

$(\Pi_{LSR}, \Theta_{LSR}, Z_{LSR}) = (0, \Theta_0, 0)$

O valor de $\Theta_0$ ainda é mal conhecido — a literatura usa valores entre 180 e 250 km/s, sendo **220 km/s** o mais comumente adotado. A velocidade **peculiar** de uma estrela em relação ao LSR é a diferença entre sua velocidade e $\Theta_0$.

O próprio **Sol** tem uma velocidade peculiar em relação ao LSR — geralmente adotada como $(u,v,w)_\odot = (-9, 11, 6)\,$km/s \[ver Mihalas & Binney 1980, Cap. 6, para os métodos de medida]. Ou seja, o **Sol se move um pouco mais rápido** do que o LSR estritamente definido. A velocidade heliocêntrica de qualquer estrela próxima é, portanto, a diferença entre as velocidades peculiares da estrela e do Sol.

### Velocidade radial em outros referenciais

Para estudos de dinâmica galáctica, é mais apropriado remover a contribuição da velocidade solar projetada na linha de visada:

- **Com respeito ao LSR:** velocidade radial que um observador movendo-se junto ao LSR mediria.
- **Com respeito ao Padrão Galáctico de Repouso (adotando $\Theta_0=220\,$km/s):** velocidade radial que um observador **estacionário** no referencial de repouso da Galáxia, na posição atual do Sol, mediria. Este é o referencial mais adequado para estudar a distribuição de velocidades de estrelas em diferentes direções do céu.

## 🎯 Movimento próprio

O deslocamento aparente de uma estrela na esfera celeste, causado pela sua velocidade **tangencial**, chama-se **movimento próprio**. É medido em arcosegundos percorridos por unidade de tempo — tipicamente **miliarcossegundos/ano (mas/yr)**.

Para converter movimento próprio ($\mu$) em velocidade tangencial, é necessário conhecer a **distância** $d$ ao objeto (ver Aula 07):

$v_{tan} = 4{,}74\,\mu\,[''/\text{yr}]\; \cdot\; d\,[\text{pc}] \quad \text{km/s}$

O movimento próprio observado será **grande** quando:

1. A distância ao objeto for **pequena**, ou
2. O objeto tiver **grande** velocidade tangencial em relação ao Sol.

Movimentos próprios típicos são $< 0{,}1''$/ano; poucas estrelas têm $\mu > 1{,}0''$/ano. O movimento próprio pode ser decomposto nas direções dos eixos de coordenadas usados — por exemplo, $\mu_\alpha$ e $\mu_\delta$ em coordenadas equatoriais.

---

## 📌 Conceitos-chave

- **Velocidade radial (Doppler) + velocidade tangencial (movimento próprio + distância) = velocidade espacial completa.**
- **LSR:** velocidade circular média na posição do Sol, $\Theta_0\approx220\,$km/s; o Sol tem velocidade peculiar própria em relação a ele, $(u,v,w)_\odot=(-9,11,6)\,$km/s.
- **Movimento próprio depende de distância:** um mesmo $v_{tan}$ produz $\mu$ maior quanto mais próxima a estrela — cuidado ao comparar $\mu$ entre populações a distâncias muito diferentes.

## 🔗 Referências e correlatos

- Mihalas & Binney (1980), Cap. 6 — determinação do movimento solar em relação ao LSR
- [[pt-br/resource/curso-on|Curso ON — visão geral]]
- [[pt-br/resource/curso-on/aula-07-distancias-e-coordenadas|Aula 07 — Distâncias, Escala de Distância e Sistemas de Coordenadas]] — pré-requisito direto (distância entra na conversão $\mu \to v_{tan}$)
- [[pt-br/resource/curso-on/aula-09-orbitas-potenciais-e-integrais-de-movimento|Aula 09 — Órbitas, Potenciais e Integrais de Movimento]] — $(U,V,W)$ e o LSR desta aula tornam-se condições iniciais para integração de órbitas
- [[pt-br/research/anomaly-detection|Detecção de Anomalias em Dados do Gaia]] — cinemática LSR é um dos filtros de pré-processamento usados na minha pesquisa
- [[pt-br/resource/escolainverno/arqgal/arqueologiagalactica-aula03|Escola de Inverno — Arqueologia Galáctica, Aula 03]] — LSR e velocidade peculiar aplicadas na prática para separar disco fino/espesso/halo via diagrama de Toomre
