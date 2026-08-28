---
publish: true
title: "LaTeX & Escrita Acadêmica"
created: 2026-08-04 13:34
modified: 2026-08-27 13:34
tags:
  - latex
  - escrita-academica
  - abnt
  - ifftese
  - relatex
cssclasses:
  - page-layout
---

Bem-vindo ao repositório oficial da formação em **LaTeX & Escrita Acadêmica** do **Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana**, ministrada pelo **Prof. Pedro Henrique Rocha de Andrade**.

Esta plataforma centraliza o referencial teórico-metodológico e a arquitetura de automação documental **ReLaTeX**, promovendo o alinhamento integral entre rigor científico (**ABNT NBR 14724, NBR 10520, NBR 6023, NBR 6027, NBR 6028 e IBGE 1993**) e excelência tipográfica.

---

## 🎓 Articulação Curricular na Engenharia de Computação

A formação em **LaTeX & Escrita Acadêmica** integra-se transversalmente à matriz curricular do curso de **Bacharelado em Engenharia de Computação** do IFF — Campus Bom Jesus do Itabapoana, fornecendo a instrumentação técnica, a automação tipográfica e a fundamentação epistêmica indispensáveis para a elaboração de trabalhos acadêmicos de alta complexidade:

- ✍️ **[[pt-br/resource/Engenharia%20de%20Computa%C3%A7%C3%A3o/1-periodo/expressao-oral-e-escrita|Expressão Oral e Escrita (1º Período)]]** — *Desenvolvimento da comunicação científica, sobriedade vocabular, coesão textual e estrutura argumentativa.*
- 📊 **[[pt-br/resource/Engenharia%20de%20Computa%C3%A7%C3%A3o/5-periodo/engenharia-de-software|Gestão de Projetos e Engenharia de Software (5º Período)]]** — *Planejamento, matrizes de análise, gerenciamento de requisitos e especificação formal de sistemas.*
- 🔬 **[[pt-br/resource/Engenharia%20de%20Computa%C3%A7%C3%A3o/8-periodo/metodologia-cientifica-e-tecnologica|Metodologia Científica e Tecnológica (8º Período)]]** — *Problematização, formulação de hipóteses, revisão sistemática da literatura (PRISMA 2020) e conformidade ABNT NBR 14724.*
- 🚀 **[[pt-br/resource/Engenharia%20de%20Computa%C3%A7%C3%A3o/9-periodo/projeto-final-de-curso-i|Projeto Final de Curso I — PFC 1 (9º Período)]]** — *Elaboração da proposta de monografia, elementos pré-textuais, referencial teórico e projeto de pesquisa na classe `ifftese.cls`.*
- 🏆 **[[pt-br/resource/Engenharia%20de%20Computa%C3%A7%C3%A3o/10-periodo/projeto-final-de-curso-ii|Projeto Final de Curso II — PFC 2 (10º Período)]]** — *Defesa final, consolidação do trabalho de conclusão de curso (TCC), apresentações com `slidesiffmodelo.cls` e depósito na biblioteca.*

---

## 🎨 Carrossel de Aulas (Acesso Rápido Interativo)

Navegue diretamente pelas notas de aula e apresentações através do carrossel interativo:

<style>
.course-carousel-wrapper {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  gap: 1.5rem;
  padding: 1.5rem 0.5rem;
  scrollbar-width: thin;
  scrollbar-color: var(--secondary, #0077b6) transparent;
  -webkit-overflow-scrolling: touch;
}
.course-carousel-card {
  flex: 0 0 280px;
  scroll-snap-align: start;
  border: 1px solid var(--lightgray, #e2e8f0);
  border-radius: 14px;
  overflow: hidden;
  background: var(--light, #ffffff);
  box-shadow: 0 4px 15px rgba(0,0,0,0.06);
  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
  display: flex;
  flex-direction: column;
  text-decoration: none;
  position: relative;
}
.course-carousel-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 14px 28px rgba(0,0,0,0.14);
  border-color: var(--secondary, #0077b6);
}
.course-carousel-thumb-box {
  position: relative;
  width: 100%;
  height: 160px;
  overflow: hidden;
  background: #1e293b;
}
.course-carousel-thumb {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: blur(3.5px) brightness(0.85);
  transform: scale(1.08);
  transition: filter 0.4s ease, transform 0.4s ease, brightness 0.4s ease;
}
.course-carousel-card:hover .course-carousel-thumb {
  filter: blur(0px) brightness(1);
  transform: scale(1.0);
}
.course-carousel-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(0, 0, 0, 0.75);
  color: #fff;
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 700;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255,255,255,0.2);
  z-index: 2;
}
.course-carousel-body {
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
}
.course-carousel-title {
  font-size: 0.98rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--dark, #0f172a);
  line-height: 1.35;
}
.course-carousel-desc {
  font-size: 0.82rem;
  color: var(--gray, #64748b);
  line-height: 1.45;
  margin: 0;
}
</style>

<div class="course-carousel-wrapper">
  <a href="/pt-br/resource/latex/aula-01-epistemologia-problematizacao-e-hipoteses" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 01</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-01.png" alt="Capa Aula 01" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Epistemologia, Problematização e Hipóteses</div>
      <p class="course-carousel-desc">ABNT NBR 14724 / CEP/CONEP</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-02-objetivos-taxonomia-de-bloom-e-justificativa" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 02</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-02.png" alt="Capa Aula 02" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Objetivos, Taxonomia de Bloom e Justificativa</div>
      <p class="course-carousel-desc">ABNT NBR 14724:2011</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-03-resumo-abstract-e-palavras-chave-nbr-6028" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 03</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-03.png" alt="Capa Aula 03" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Resumo, Abstract e Palavras-Chave (NBR 6028:2021)</div>
      <p class="course-carousel-desc">ABNT NBR 6028:2021</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-04-elementos-pre-textuais-nbr-14724" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 04</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-04.png" alt="Capa Aula 04" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Elementos Pré-Textuais NBR 14724</div>
      <p class="course-carousel-desc">ABNT NBR 14724 / ABNT NBR 6027</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-05-introducao-contextualizacao-e-lacuna-de-pesquisa" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 05</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-05.png" alt="Capa Aula 05" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Introdução e Lacuna de Pesquisa (*Research Gap*)</div>
      <p class="course-carousel-desc">ABNT NBR 14724:2011</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-06-revisao-sistematica-da-literatura-e-protocolo-prisma" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 06</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-06.png" alt="Capa Aula 06" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Revisão Sistemática da Literatura e Protocolo PRISMA 2020</div>
      <p class="course-carousel-desc">Protocolo PRISMA 2020 / ABNT NBR 14724</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-07-metodologia-materiais-e-reprodutibilidade" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 07</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-07.png" alt="Capa Aula 07" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Metodologia, Materiais e Reprodutibilidade na ABNT</div>
      <p class="course-carousel-desc">ABNT NBR 14724:2011</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-08-etica-plataforma-brasil-e-uso-de-ia" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 08</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-08.png" alt="Capa Aula 08" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Ética na Pesquisa (Plataforma Brasil) e IA</div>
      <p class="course-carousel-desc">Resolução CNS 466/12 / CEP/CONEP / ABNT NBR 6023</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-09-resultados-tabelas-ibge-vs-quadros-abnt" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 09</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-09.png" alt="Capa Aula 09" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Resultados: Tabelas IBGE vs. Quadros ABNT</div>
      <p class="course-carousel-desc">IBGE 1993 / ABNT NBR 14724</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-10-discussao-citacoes-nbr-10520-e-referencias-nbr-6023" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 10</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-10.png" alt="Capa Aula 10" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Discussão, Citações (10520) e Referências (6023)</div>
      <p class="course-carousel-desc">ABNT NBR 10520:2023 / ABNT NBR 6023:2018</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-11-arquitetura-latex-motores-tex-e-preambulo-tex" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 11</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-11.png" alt="Capa Aula 11" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Arquitetura do Kernel LaTeX2e, Motores PDFLaTeX/LuaLaTeX/XeLaTeX e Estrutura do Preâmbulo .tex</div>
      <p class="course-carousel-desc">Kernel LaTeX2e / TeX Live 2026</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-12-sintaxe-matematica-amsmath-e-tabelas-booktabs" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 12</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-12.png" alt="Capa Aula 12" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Sintaxe Canônica, Ambientes Matemáticos Avançados (amsmath) e Tabelas (booktabs)</div>
      <p class="course-carousel-desc">Pacotes `amsmath`, `mathtools` e `booktabs`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-13-modularizacao-multi-arquivo-e-biblatex-biber" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 13</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-13.png" alt="Capa Aula 13" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Modularização Multi-arquivo e Gestão Bibliográfica com biblatex-biber</div>
      <p class="course-carousel-desc">Pacote `biblatex` (estilo `abnt`) / Engine `biber`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 14</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-14.png" alt="Capa Aula 14" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Computação Gráfica Vetorial Programável com TikZ e Gráficos PGFPlots</div>
      <p class="course-carousel-desc">Pacotes `tikz` e `pgfplots`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-15-engenharia-do-arquivo-de-metadados-sty" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 15</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-15.png" alt="Capa Aula 15" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Engenharia de Metadados: Estrutura de metadados.sty, Escopo e Flexão de Gênero</div>
      <p class="course-carousel-desc">Arquitetura ReLaTeX / Pacote `metadados.sty`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 16</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-16.png" alt="Capa Aula 16" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Desenvolvimento de Pacotes .sty - Programação TeX e Macros</div>
      <p class="course-carousel-desc">Linguagem TeX / Pacote `macros.sty`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-17-engenharia-da-classe-ifftese-cls" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 17</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-17.png" alt="Capa Aula 17" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Engenharia de Classes .cls - Anatomia da ifftese e abntex2</div>
      <p class="course-carousel-desc">Classe `ifftese.cls` / `abntex2.cls`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-18-customizacao-de-floats-fancyhdr-e-nbr-6027" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 18</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-18.png" alt="Capa Aula 18" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Controle Avançado de Floats e NBR 6027</div>
      <p class="course-carousel-desc">ABNT NBR 6027 / Pacote `fancyhdr`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-19-classes-especializadas-if-beamer-iffposter-relatoriocorp" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 19</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-19.png" alt="Capa Aula 19" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Classes Especializadas (Beamer, Poster e Relatório)</div>
      <p class="course-carousel-desc">Classes `slidesiffmodelo.cls`, `iffposter.cls` e `relatoriocorp.cls`</p>
    </div>
  </a>
  <a href="/pt-br/resource/latex/aula-20-automacao-latexmkrc-git-e-integracao-continua" class="course-carousel-card">
    <div class="course-carousel-thumb-box">
      <span class="course-carousel-badge">AULA 20</span>
      <img src="/assets/biblioteca/latex-escrita/thumbs/aula-20.png" alt="Capa Aula 20" class="course-carousel-thumb" />
    </div>
    <div class="course-carousel-body">
      <div class="course-carousel-title">Automação LaTeX, Git e Integração Contínua CI/CD</div>
      <p class="course-carousel-desc">LaTeXmk / Git / GitHub Actions CI/CD</p>
    </div>
  </a>
</div>

---

## 📚 Material Suplementar e Documentos Oficiais

> [!note] Guia Rápido e Documentos Institucionais
> - **[[pt-br/resource/latex/planejamento-e-cronograma|📅 Planejamento Letivo e Cronograma de Atividades]]** — *Planejamento analítico das 20 aulas, divisão em 5 módulos didáticos, matriz de competências e referencial normativo ABNT.*
> - **[[pt-br/resource/latex/codigo-de-conduta-e-diretrizes|📜 Código de Conduta, Ética na Pesquisa e Diretrizes Acadêmicas]]** — *Código de ética científica, política institucional de integridade contra plágio/autoplágio, regimento de uso de IA (LLMs) e boas práticas de laboratório.*
> - **[[pt-br/resource/latex/modelos-de-documento|🏛️ Guia Oficial de Modelos, Classes e Pacotes ReLaTeX]]** — *Referência técnica unificada com documentação canônica das classes `ifftese.cls`, `iffposter.cls`, `relatoriocorp.cls` e pacotes `metadados.sty` e `macros.sty`.*

---

## 📖 Biblioteca Digital de Manuais, Apostilas e Modelos (.pdf & .zip)

> [!note] 📅 Documentos Oficiais da Disciplina
> - 📅 **[Cronograma e Ementa Analítica da Formação (PDF)](/assets/biblioteca/latex-escrita/documentos/cronograma-e-ementa.pdf)** — *Documento em PDF com o detalhamento das 80h de curso.*
> - 📜 **[Guia Institucional de Diretrizes e Integridade (PDF)](/assets/biblioteca/latex-escrita/documentos/guia-e-diretrizes.pdf)** — *Normativo ético e conduta discente em laboratório.*

> [!info] 📑 Manuais, Apostilas e Guias de Normalização (PDF)
> - 📘 **[Apostila Completa de LaTeX — UFES (PDF)](/assets/biblioteca/latex-escrita/apostila-latex-ufes.pdf)** — *Guia prático e abrangente de introdução, ambientes e tópicos avançados em LaTeX.*
> - 📕 **[Manual Oficial do Pacote biblatex-abnt (PDF)](/assets/biblioteca/latex-escrita/biblatex-abnt-manual.pdf)** — *Documentação canônica para gestão de citações e referências bibliográficas ABNT no Biber.*
> - 📄 **[Guia Rápido / Cheatsheet BibLaTeX (PDF)](/assets/biblioteca/latex-escrita/biblatex-cheatsheet.pdf)** — *Folha de consulta rápida para tipos de entrada e comandos de citação.*
> - 🎨 **[Figuras e Diagramas Vetoriais em TikZ — UFPB (PDF)](/assets/biblioteca/latex-escrita/figuras-diagramas-tikz-ufpb.pdf)** — *Manual de construção gráfica de esquemas, circuitos e diagramas vetoriais programáveis.*
> - 📑 **[Guia Ilustrado de Normalização ABNT — PUC Minas (PDF)](/assets/biblioteca/latex-escrita/guia-abnt-puc-minas.pdf)** — *Manual prático e exemplificado de formatação de trabalhos acadêmicos.*
> - 📙 **[Manual Complementar de Normalização — UNIP (PDF)](/assets/biblioteca/latex-escrita/guia-abnt-unip.pdf)** — *Diretrizes complementares de elementos pré-textuais, citações e referências.*

> [!tip] 📦 Modelos de Código-Fonte e Templates Institucionais (.zip)
> - 📦 **[Modelo de TCC e Monografia — ifftese.cls (.zip)](/assets/biblioteca/latex-escrita/modelo-ifftese-tcc.zip)** — *Pacote zip com classe, preâmbulo, metadados e estrutura completa para TCC.*
> - 📦 **[Modelo de Pôster / Banner A0 — iffposter.cls (.zip)](/assets/biblioteca/latex-escrita/modelo-iffposter-banner.zip)** — *Pacote zip para confecção de banners e pôsteres acadêmicos.*
> - 📦 **[Modelo de Slides Institucionais — slidesiffmodelo.cls (.zip)](/assets/biblioteca/latex-escrita/modelo-slide-iffbji.zip)** — *Template zip 16:9 em Branco e Preto para apresentações de TCC.*

---

## 📊 Sistema Resumido de Avaliação e Cronograma

> [!tip] Distribuição de Pesos nos Bimestres
> - **📅 Período Letivo:** 24/08/2026 a 20/12/2026 | **⏰ Terças-feiras, 14h30 - 17h30** (IFF — Campus Bom Jesus do Itabapoana)
> - **🔹 1º Bimestre (Metodologia e Normalização ABNT — Aulas 01 a 10):**  
>   - **60%** — Trabalho Prático de Escrita (Lacuna de Pesquisa, PRISMA 2020 e Estrutura ABNT NBR 14724).  
>   - **40%** — Avaliação Prática em Laboratório (Citações NBR 10520:2023, Referências NBR 6023 e Tabelas IBGE 1993).
> - **🔹 2º Bimestre (Engenharia TeX e Automação ReLaTeX — Aulas 11 a 20):**  
>   - **80%** — Projeto Customizado em LaTeX (Monografia/Projeto em `ifftese.cls`, macros `.sty`, `booktabs` e `TikZ`).  
>   - **20%** — Avaliação Prática em Laboratório (Resolução de erros de compilação e gestão bibliográfica com Biber).

---

## 🗺️ Tabela de Aulas



```base
filters:
  and:
    - 'file.folder.startsWith("pt-br/resource/latex")'
    - 'note.publish'
    - 'note.notas'
formulas:
  aula: 'link(file.path, note.title)'
properties:
  formula.aula:
    displayName: Aula & Título da Aula
  note.notas:
    displayName: Notas de Aula (PDF)
  note.slide:
    displayName: Slide Institucional (PDF)
views:
  - type: table
    name: Aulas do Curso de LaTeX & Escrita Acadêmica
    order:
      - formula.aula
      - note.notas
      - note.slide
    sort:
      - property: file.name
        direction: ASC
```

---

## 🏛️ Material de Referência Externa e Normalização Mundial

> [!important] Fontes Canônicas e Portais Oficiais
> ### 🌐 Normalização, Repositórios TeX e Comunidade Científica
> - **[ABNT — Associação Brasileira de Normas Técnicas](https://www.abnt.org.br/)** — *Portal oficial de consulta às normas ABNT NBR 14724, NBR 10520 e NBR 6023.*
> - **[CTAN (Comprehensive TeX Archive Network)](https://ctan.org/)** — *O repositório mundial canônico de pacotes, documentações e classes LaTeX2e/LaTeX3.*
> - **[Overleaf Documentation & TeX Live Guide](https://www.overleaf.com/learn)** — *Guias interativos, documentação de pacotes e tutoriais da linguagem LaTeX.*
> - **[TUG (TeX Users Group) & TUGboat Journal](https://www.tug.org/)** — *Organização mundial de usuários TeX e publicação científica de engenharia tipográfica.*
> - **[TikZ & PGF Manual Online (CTAN)](https://tikz.dev/)** — *Documentação técnica oficial para programação gráfica vetorial em LaTeX.*
> - **[Plataforma Brasil & CEP/CONEP](https://plataformabrasil.saude.gov.br/)** — *Base nacional e unificada dos registros de pesquisas envolvendo seres humanos.*
> - **[PRISMA 2020 Statement](http://www.prisma-statement.org/)** — *Diretrizes internacionais e fluxogramas recomendados para revisões sistemáticas da literatura.*
> - **[IBGE — Normas de Apresentação Tabular (1993)](https://biblioteca.ibge.gov.br/)** — *Manual técnico oficial para elaboração e padronização de tabelas estatísticas brasileiras.*
