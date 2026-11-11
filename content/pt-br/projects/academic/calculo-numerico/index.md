---
publish: true
title: Cálculo Numérico
tags:
- disciplina
- metodos-numericos
repo: https://github.com/pedroiff0/CalculoNumerico
status: público
cssclasses:
  - page-layout
created: '2026-09-14T11:17:03-03:00'
modified: 2026-11-11T16:07:45-03:00
icon: lucide-notebookpen
sitesync: true
resource-sync: false
mirror_of: pedroiff0/calculo-numerico/README.md
---

<div class="academic-nav-container">

<div class="academic-nav-breadcrumb">

<span>Projetos Públicos</span> <span class="academic-nav-sep">/</span> <span class="academic-nav-current-leaf">Cálculo Numérico</span>

</div>

<div class="academic-nav-controls">

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/personal/baton/index|← Baton]]</span>

</div>

<div class="academic-nav-center">

<span class="academic-nav-btn">Hub</span> <span class="academic-nav-counter">(4 de 10)</span>

</div>

<div class="academic-nav-side">

<span class="academic-nav-btn">[[pt-br/projects/personal/devops-guide/index|Guia de DevOps e Infraestrutura →]]</span>

</div>

</div>

</div>

# Cálculo Numérico

[![CI](https://github.com/pedroiff0/calculo-numerico/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroiff0/calculo-numerico/actions/workflows/ci.yml) [![Licença](https://img.shields.io/github/license/pedroiff0/calculo-numerico)](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/LICENSE.md) [![Estrelas](https://img.shields.io/github/stars/pedroiff0/calculo-numerico?style=flat&logo=github)](https://github.com/pedroiff0/calculo-numerico/stargazers) [![Status](https://img.shields.io/badge/status-concluído-informational)](#status)

Implementação em Python dos algoritmos da disciplina de Cálculo Numérico (2025.2, IFF Bom Jesus do Itabapoana), com 96 testes unitários, documentação Sphinx e um guia em LaTeX.

Este projeto faz parte do [portfólio](https://portfolio.phrandrade.com/#calculo-numerico) de Pedro Rocha.

## Sumário

- [Resumo](#resumo)
- [Contexto](#contexto)
- [Tecnologias](#tecnologias)
- [Começando](#começando)
- [Como usar](#como-usar)
- [Reprodução dos resultados](#reprodução-dos-resultados)
- [Metodologia](#metodologia)
- [Dados](#dados)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Trabalhando no projeto](#trabalhando-no-projeto)
- [Status](#status)
- [Como citar](#como-citar)
- [Como contribuir](#como-contribuir)
- [Código de conduta](#código-de-conduta)
- [Segurança](#segurança)
- [Suporte](#suporte)
- [Estrelas e atividade](#estrelas-e-atividade)
- [Autor](#autor)
- [Contribuidores](#contribuidores)
- [Licença](#licença)

## Resumo

Os métodos numéricos da disciplina costumam ser vistos em planilhas e códigos soltos, difíceis de comparar e de testar. Este repositório implementa os tópicos da ementa como biblioteca Python, com testes que verificam cada método contra soluções conhecidas e documentação técnica gerada com Sphinx. Os métodos cobrem erros de ponto flutuante, raízes de equações, interpolação, ajuste de curvas, integração, sistemas lineares e equações diferenciais ordinárias. Limitação: o foco é didático, sem otimização de desempenho.

## Contexto

Projeto da disciplina de Cálculo Numérico, semestre 2025.2, curso de Engenharia de Computação, Instituto Federal Fluminense, campus Bom Jesus do Itabapoana, com o professor Rodrigo Lacerda da Silva.

### Objetivos

- Implementar os algoritmos numéricos fundamentais em Python.
- Manter uma biblioteca testada e documentada.
- Demonstrar aplicações práticas dos métodos.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat&logo=scipy&logoColor=white) ![SymPy](https://img.shields.io/badge/SymPy-3B5526?style=flat&logo=sympy&logoColor=white) ![Sphinx](https://img.shields.io/badge/Sphinx-000000?style=flat&logo=sphinx&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) ![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)

## Começando

### Pré-requisitos

- Python 3.8 ou superior.
- NumPy, SymPy, Matplotlib e SciPy (instalados pelo `pip`).
- Opcional: TeX Live para o guia em `guia/`.

### Instalação

```bash
git clone https://github.com/pedroiff0/calculo-numerico.git
cd calculo-numerico
make install
```

### Conferindo que funcionou

```bash
make test
```

Saída esperada: 96 testes aprovados.

## Como usar

### Exemplo 1: método da bisseção

```python
from codigos.raizes import bissecao

raiz, iteracoes = bissecao("x**2 - 2", 1, 2, 1e-8, 100)
print(raiz)
```

Saída esperada: aproximadamente `1.41421356`.

### Opções principais

| Comando | Efeito |
| :--- | :--- |
| `make test` | Roda a suíte pytest |
| `make docs` | Gera a documentação Sphinx em HTML |
| `make lint` | Verifica a sintaxe Python |
| `make clean` | Remove caches e builds temporários |

## Reprodução dos resultados

| Resultado | Comando |
| :--- | :--- |
| Testes unitários | `pytest tests/ -v` |
| Documentação HTML | `make docs` |
| Guia em PDF | `cd guia && make book` |

Versões fixadas em `pyproject.toml`.

## Metodologia

Cada tópico da ementa é um módulo em `codigos/`, com testes em `tests/` que comparam o resultado com soluções analíticas ou valores de referência.

```mermaid
flowchart LR
    A[codigos/ métodos] --> B[tests/ pytest]
    A --> C[docs/ Sphinx]
    A --> D[guia/ LaTeX]
```

## Dados

Não há conjuntos de dados externos: os exemplos usam funções e sistemas definidos nos próprios testes e na documentação.

## Estrutura do repositório

```text
calculo-numerico/
├── codigos/       implementação dos métodos
├── tests/         suíte pytest
├── docs/          documentação Sphinx
├── guia/          guia em LaTeX
└── pyproject.toml pacote e dependências
```

## Trabalhando no projeto

### Ambiente de desenvolvimento

```bash
make install
make test
```

### Fluxo de trabalho

1. Crie uma branch a partir de `main`: `git checkout -b feat/<assunto-curto>`.
2. Commits no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
3. Rode `make test` antes de abrir o pull request.
4. Registre a mudança na seção `Unreleased` de [CHANGELOG.md](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/CHANGELOG.md).

### Convenções

Funções documentadas com docstring, um teste por método e nomes em português.

## Status

Estado atual: **concluído** para a disciplina; mantido para consulta e correções.

- [x] Todos os tópicos da ementa implementados e testados
- [x] Documentação Sphinx e guia em LaTeX
- [ ] Publicar o pacote no PyPI

## Como citar

Use o arquivo [CITATION.cff](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/CITATION.cff) (botão "Cite this repository" do GitHub).

## Como contribuir

Contribuições são bem-vindas. Antes de começar, leia o [guia de contribuição](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/CONTRIBUTING.md).

1. Abra uma issue descrevendo o problema ou a ideia.
2. Crie uma branch a partir de `main`: `git checkout -b feat/<assunto-curto>`.
3. Faça commits no padrão [Conventional Commits](https://www.conventionalcommits.org/pt-br/).
4. Abra o pull request e registre a mudança em [CHANGELOG.md](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/CHANGELOG.md).

## Código de conduta

Este projeto adota o [Código de Conduta](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/CODE_OF_CONDUCT.md). Ao participar, você concorda em segui-lo.

## Segurança

Não abra issue pública para vulnerabilidades. Siga o procedimento de [SECURITY.md](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/SECURITY.md) para reportar de forma confidencial.

## Suporte

Dúvidas e pedidos de ajuda: veja [SUPPORT.md](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/SUPPORT.md).

## Estrelas e atividade

[![Histórico de estrelas](https://api.star-history.com/svg?repos=pedroiff0/calculo-numerico&type=Date)](https://star-history.com/#pedroiff0/calculo-numerico&Date)

[![Commits por mês](https://img.shields.io/github/commit-activity/m/pedroiff0/calculo-numerico?logo=github)](https://github.com/pedroiff0/calculo-numerico/graphs/commit-activity) [![Último commit](https://img.shields.io/github/last-commit/pedroiff0/calculo-numerico?logo=git&logoColor=white)](https://github.com/pedroiff0/calculo-numerico/commits) [![Issues](https://img.shields.io/github/issues/pedroiff0/calculo-numerico)](https://github.com/pedroiff0/calculo-numerico/issues) [![Pull requests](https://img.shields.io/github/issues-pr/pedroiff0/calculo-numerico)](https://github.com/pedroiff0/calculo-numerico/pulls)

<div align="center">

## Autor

<table>
  <tr>
    <td align="center"><a href="https://github.com/pedroiff0"><img src="https://github.com/pedroiff0.png?size=120" width="96" height="96" alt="Pedro Henrique Rocha de Andrade" /><br /><sub><b>Pedro Henrique Rocha de Andrade</b></sub></a><br />Autor e mantenedor</td>
  </tr>
</table>

## Contribuidores

[![Contribuidores](https://contrib.rocks/image?repo=pedroiff0/calculo-numerico)](https://github.com/pedroiff0/calculo-numerico/graphs/contributors)

</div>

## Licença

Distribuído sob a licença MIT. Texto completo do arquivo [LICENSE](https://github.com/pedroiff0/calculo-numerico/blob/HEAD/LICENSE.md):

```txt
MIT License

Copyright (c) <2025> <Pedro Henrique Rocha de Andrade>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT license text omitted here for brevity — include the standard MIT text in the file before publishing.]
```

---

<div align="center">

<img src="https://api.iconify.design/mdi/star-shooting.svg?color=%23c678dd" width="20" valign="middle" /> *"Keep looking up."*

<img src="https://raw.githubusercontent.com/pedroiff0/pedroiff0/main/assets/pedroiff0.gif" width="480" alt="pedroiff0" />

<br>

<sub>© 2026 Pedro Rocha — Computer Engineering & Computational Astrophysics · IFF / PIBIC-CNPq, made with ☕, code and ☄️ by Pedro Henrique Rocha de Andrade</sub>

</div>
