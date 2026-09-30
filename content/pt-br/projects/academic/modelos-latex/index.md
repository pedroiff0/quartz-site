---
publish: true
title: Modelos LaTeX
tags:
- template
repo: https://github.com/pedroiff0/modelos
status: privado
cssclasses:
  - page-layout
created: 2026-09-14 11:17:03-03:00
modified: 2026-09-30T13:05:50-03:00
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[pt-br/projects/site-publico-hub|Site Público]]

# Ecossistema de Modelos e Classes Institucionais \LaTeX{} — IFFlu

Repositório central de classes tipográficas e modelos acadêmicos oficiais do **Instituto Federal de Educação, Ciência e Tecnologia Fluminense (IFFlu)**.

Desenvolvido para assegurar o cumprimento rigoroso e automatizado das normas da **ABNT** (NBR 14724, NBR 6022, NBR 6023, NBR 6028) e normas tabulares do **IBGE**, permitindo que o pesquisador, docente ou discente concentre seus esforços exclusivamente no conteúdo científico sob o paradigma **WYSIWYM** (*What You See Is What You Mean*).

---

## Estrutura do Repositório

```text
modelos/
 Makefile                     # Compilação e limpeza global de todos os modelos
 README.md                    # Guia geral do ecossistema e instruções de uso
 classes-iff/                 # FONTE ÚNICA DA VERDADE (Classes e Estilos)
    ifftese.cls              # Classe para TCC, Teses, Dissertações e Relatórios
    iffslides.cls            # Classe Beamer para Apresentações (Padrão CONEPE 2026)
    iffartigo.cls            # Classe para Artigos Científicos (2 colunas, ABNT NBR 6022)
    iffposter.cls            # Classe para Pôsteres e Banners (70x100cm / 90x120cm)
    macros.sty               # Núcleo semântico de comandos, caixas e ilustrações
    metadados.sty            # Folha de preenchimento de variáveis e metadados

 modelo-tcc/                  # Modelo Canônico de TCC / Monografia (ABNT NBR 14724)
 modelo-relatorio/            # Modelo de Relatório Técnico (Manual do Usuário Oficial)
 modelo-slides/               # Modelo de Apresentação de Slides (Widescreen 16:9)
 modelo-artigo/               # Modelo de Artigo Científico (Duas Colunas)
 modelo-banner/               # Modelo de Pôster / Banner para Mostras Científicas
```

---

## Modelos Prontos para Uso (*Copy-Paste Workflow*)

Cada pasta de modelo é totalmente **autocontida**. Para iniciar um novo trabalho acadêmico:

```bash
# 1. Clone o repositório
git clone https://github.com/pedroiff0/modelos.git
cd modelos

# 2. Copie o modelo desejado para sua pasta de trabalho
cp -r modelo-tcc ~/meu-tcc
cd ~/meu-tcc

# 3. Compile com um único comando
make
```

### Resumo dos Modelos

| Diretório | Classe Base | Finalidade | Principais Recursos |
|---|---|---|---|
| `modelo-tcc/` | `ifftese.cls` (`tipo=tcc`) | TCC, Dissertações e Teses | Pré-textuais completos (capa, folha de rosto, aprovação, dedicatória, agradecimentos, epígrafe, resumo, abstract), capítulos modulares e 7 listas de ToC independentes. |
| `modelo-relatorio/` | `ifftese.cls` (`tipo=relatorio`) | Relatórios Técnicos e Acadêmicos | Contém o **Manual do Usuário Oficial** do ecossistema em 21 páginas explicativas com dados de catalogação e convênio. |
| `modelo-slides/` | `iffslides.cls` (Beamer) | Apresentações e Defesas | Formato 16:9 widescreen, régua verde institucional, rodapé `autor \| título \| X/Y`, capa automática, frame wallpaper e encerramento com QR Code. |
| `modelo-artigo/` | `iffartigo.cls` | Artigos de Periódicos e Congressos | Formato em duas colunas com cabeçalho de título e resumo em largura total (*full-width top header*), cabeçalhos `fancyhdr` e ABNT NBR 6022. |
| `modelo-banner/` | `iffposter.cls` | Pôsteres e Banners Científicos | Formato 70\,cm $\times$ 100\,cm (ou 90\,cm $\times$ 120\,cm com opção `maior`), caixas de seção em `tcolorbox`, logos de agências (CNPq, FAPERJ) e legendas inteligentes. |

---

## Diferenciação e Listas de Ilustrações Técnicas

O ecossistema implementa separação taxonômica e catalográfica estrita para cada modalidade de elemento visual, garantindo a geração de listas sumárias (**ToC**) dedicadas e condicionais (impressas automaticamente apenas quando o elemento existe no trabalho):

| Elemento | Macro de Inserção | Lista Gerada no Sumário | Norma / Regra de Diagramação |
|---|---|---|---|
| **Figura** | `\inserirfigura[opc]{arq}{legenda}{curta}{fonte}{label}` | `\listoffigures` (Lista de Figuras) | Fotografias, capturas e ilustrações gerais. |
| **Gráfico** | `\inserirgrafico[opc]{arq}{legenda}{curta}{fonte}{label}` | `\listofgraficos` (Lista de Gráficos) | Séries estatísticas, curvas analíticas e histogramas. |
| **Fluxograma** | `\inserirfluxograma[opc]{arq}{legenda}{curta}{fonte}{label}` | `\listoffluxogramas` (Lista de Fluxogramas) | Encadeamentos lógicos e processos operacionais. |
| **Diagrama** | `\inserirdiagrama[opc]{arq}{legenda}{curta}{fonte}{label}` | `\listofdiagramas` (Lista de Diagramas) | Arquiteturas conceituais e diagramas de blocos. |
| **Esquema** | `\inseriresquema[opc]{arq}{legenda}{curta}{fonte}{label}` | `\listofesquemas` (Lista de Esquemas) | Topologias físicas, hardware e circuitos. |
| **Tabela** | `\inserirtabela{legenda}{curta}{label}{conteudo}{fonte}` | `\listoftables` (Lista de Tabelas) | Séries numéricas puras (**sem linhas verticais laterais**, padrão IBGE). |
| **Quadro** | `\inserirquadro{legenda}{curta}{label}{conteudo}{fonte}` | `\listofquadros` (Lista de Quadros) | Dados prioritariamente textuais e conceituais (**bordas fechadas**, padrão ABNT). |

> [!TIP]
> O comando unificado `\imprimirListas` avalia o documento e imprime apenas as listas que de fato contêm ilustrações, evitando páginas em branco ou listas vazias.

---

## Automação com Makefile

Todos os modelos e a raiz do repositório contam com scripts de compilação rápida:

- `make`: Compila o trabalho completo (`latexmk -pdf`), resolvendo automaticamente citações bibliográficas (BibTeX), índices remissivos e referências cruzadas.
- `make watch`: Modo interativo de desenvolvimento (*live-reload* contínuo a cada salvamento).
- `make clean`: Remove arquivos auxiliares temporários (`.aux`, `.log`, `.toc`, `.lof`, `.bbl`, etc.), preservando o PDF final.
- `make distclean`: Remove todos os arquivos gerados, inclusive os arquivos `.pdf`.

---

## Opções Comportamentais das Classes

As classes preservam flexibilidade total através de opções configuráveis tanto na declaração `\documentclass` quanto em `metadados.sty`:

- `corlink={sim|nao}`: Ativa hiperlinks com a paleta de cores institucional verde IFFlu (`#1E823C`) ou mantém preto para impressão oficial.
- `sumarioescada={sim|nao}`: Alterna entre sumário hierárquico com recuo progressivo (*escada*) ou sumário alinhado tradicional.
- `noheader`: Suprime cabeçalhos superiores para diagramações minimalistas.
- `nofooter`: Suprime números de página e rodapés.
- `frenteVerso={sim|nao}`: Formatação de margens alternadas (espelhadas) e início de capítulos em páginas ímpares (recto) para impressão gráfica frente e verso.

---

## Autoria e Licença

Desenvolvido por **Pedro Henrique Rocha de Andrade** no âmbito do **Instituto Federal Fluminense (IFFlu)**, Campus Bom Jesus do Itabapoana.

Distribuído sob licença livre para a comunidade acadêmica e científica.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/modelos-latex](https://github.com/pedroiff0/modelos-latex)
- **Índice de Projetos:** [[pt-br/projects/projetos-publicos|Projetos Públicos]]

---

<p align=center>
  <a href="https://github.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://linkedin.com/in/pedro-andrade-iff" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="https://instagram.com/pedroiff0" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white" alt="Instagram" /></a>
  <a href="mailto:pedro.andrade@iff.edu.br"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <a href="https://pedroiff.com" target="_blank"><img src="https://img.shields.io/badge/Website-000000?style=flat-square&logo=googlechrome&logoColor=white" alt="Website" /></a>
</p>

<p align=center>
  <sub>© 2026 <b><a href="https://pedroiff.com">Pedro Rocha</a></b> — Computer Engineering &amp; Computational Astrophysics</sub><br />
  <sub>Made with <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M10 2v2'/><path d='M14 2v2'/><path d='M16 8a1 1 0 0 1 1 1v8a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1h14a4 4 0 1 1 0 8h-1'/><path d='M6 2v2'/></svg>" width="16" height="16" valign="middle" alt="coffee" />, <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='m16 18 6-6-6-6'/><path d='m8 6-6 6 6 6'/></svg>" width="16" height="16" valign="middle" alt="code" /> and <img src="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%23888888' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='3'/><path d='M3 12a9 9 0 0 1 9-9 9 9 0 0 1 9 9 9 9 0 0 1-9 9 9 9 0 0 1-9-9'/><path d='M5.5 5.5a13 13 0 0 0 13 13'/><path d='M18.5 5.5a13 13 0 0 1-13 13'/></svg>" width="16" height="16" valign="middle" alt="astrophysics" /> by <b><a href="https://github.com/pedroiff0">Pedro Henrique Rocha de Andrade</a></b></sub>
</p>
