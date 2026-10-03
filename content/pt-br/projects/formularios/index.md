---
publish: true
title: Formulários
tags:
- resumo
- formulas
repo: https://github.com/pedroiff0/formularios
status: público
cssclasses:
  - page-layout
created: 2026-09-14 11:17
modified: 2026-10-01 20:14
icon: lucide-notebookpen
sitesync: true
---

- Origem: [[01-projetos/site-publico/site-publico-hub|Site Público]]


# Formulários — Coleção de folhas de fórmulas 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

---

Breve: coleções de resumos e folhas de fórmulas em LaTeX organizadas por disciplina.

## Sumário

- [Requisitos](#requisitos)
- [Uso rapido](#uso-rapido)
- [Construcoes por capitulo](#construcoes-por-capitulo)
- [Alvo combinado](#alvo-combinado)
- [Integracao continua (CI)](#integracao-continua-ci)
- [Contribuicao](#contribuicao)
- [Licenca](#licenca)

---

## Requisitos

- TeX (pdflatex) — TeX Live ou similar. Observação: o pacote `siunitx` é necessário; no Debian/Ubuntu instale `texlive-science`.
- make

---

## Uso rapido

- Gerar o documento principal:

```bash
make all
```

- Gerar toda a disciplina (PDF dentro da pasta da disciplina):

```bash
make fisicas        # -> fisicas/fisicas.pdf
make calculos       # -> calculos/calculos.pdf
```

- Gerar um capítulo específico (exemplos):

```bash
make fisicaiii cap30                  # forma posicional
```

Observações:

- Arquivos temporários (build_*.tex, .aux, .log, .synctex.gz) são removidos automaticamente após build bem-sucedido.

## Builds rápidos

Para ciclos de desenvolvimento rápidos, há um modo "fast" que compila em modo rascunho e roda pdflatex apenas uma vez:

```bash
make fisicas-fast      # equivalente a: make fisicas FAST=1
# ou
make fisicas FAST=1
```

Útil para checar o layout sem processar imagens pesadas.

## Construcoes por capitulo

Gera um PDF por capítulo (arquivo individual dentro do diretório da disciplina). Use o alvo `disciplinas` (pt) ou `disciplines` (en) com a variável contendo disciplinas separadas por vírgula.

Exemplos:

```bash
# gera um PDF por capítulo em calculos/ e fisicas/
make disciplines="calculos,fisicas"       # ou make disciplinas="calculos,fisicas"

# gerar só calculos
make disciplines="calculos"
```

Comportamento:

- Cria um PDF para cada entrada listada em `CALCULOS_INCLUDES` e `FISICAS_INCLUDES` (por exemplo: `calculos/calculoi/calculoi_calculo_basico.pdf`, `fisicas/fisicaiii/fisicaiii_cap30.pdf`).
- Silencioso por padrão; passe `VERBOSE=1` para ver os passos:

```bash
make disciplines="calculos,fisicas" VERBOSE=1
```

## Alvo combinado

O alvo `combined` gera um único PDF `combined.pdf` contendo as seções de Cálculos e Físicas.

```bash
make combined VERBOSE=1
```

---

## Integracao continua (CI)

Há um workflow GitHub Actions em `.github/workflows/test-builds.yml` que executa em push e em pull requests. O job:

- instala pacotes LaTeX mínimos na runner;
- executa `make disciplines=calculos,fisicas VERBOSE=1` (gera PDFs por capítulo);
- executa `make combined VERBOSE=1` (gera `combined.pdf`);
- publica os PDFs como artifacts para inspeção.

O job falhará caso qualquer build retorne erro — útil como teste automático de regressão.

---

## Testes locais

Para reproduzir o que o CI faz, execute localmente:

```bash
# gerar um PDF por capítulo para calculos e fisicas
make disciplines="calculos,fisicas" VERBOSE=1

# gerar combinado
make combined VERBOSE=1
```

Os arquivos são gerados nas pastas correspondentes (e.g., `calculos/...pdf`, `fisicas/...pdf`) e `combined.pdf` é criado no repositório raiz.

---

## Contribuicao

- Envie PRs para mudanças; inclua uma descrição clara e, quando possível, um teste ou verificação simples.
- Prefira imagens vetoriais (TikZ, PDF) e considere marcar recursos pesados para serem ignorados em builds rápidos (FAST=1).
- Ao alterar `Makefile` ou scripts de build, adicione verificações que possam ser executadas no CI.

## Autoria

- Pedro — mantenedor do repositório

---

## Licenca

MIT — veja `LICENSE`.

---

Se quiser, adiciono um badge do CI (status) no topo do README e/ou um alvo `verify` no `Makefile` que confirme a existência dos PDFs esperados (útil para CI).

---

Obrigado — documentação simplificada e focada nas operações de build está pronta. Se quiser, posso também abrir um PR com essas mudanças, adicionar o badge do workflow e criar um alvo `verify` que o CI utilize para validar os PDFs.

---

## Autor e Contato

- **Autor:** Pedro Henrique Rocha de Andrade
- **GitHub:** [pedroiff0](https://github.com/pedroiff0)
- **LinkedIn:** [Pedro Henrique Rocha de Andrade](https://linkedin.com/in/pedro-andrade-iff)

---

## Links e Referências

- **Repositório no GitHub:** [pedroiff0/formularios](https://github.com/pedroiff0/formularios)
- **Índice de Projetos:** [[01-projetos/site-publico/projetos-publicos|Projetos Públicos]]

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
