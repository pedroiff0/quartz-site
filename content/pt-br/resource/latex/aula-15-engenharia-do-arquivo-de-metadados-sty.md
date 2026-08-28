---
title: "Aula 15: Engenharia de Metadados: Estrutura de metadados.sty, Escopo e Flexão de Gênero"
created: 2026-08-04 13:34
modified: 2026-08-27 13:34
publish: true
notas: "[📄 Notas (PDF)](/assets/biblioteca/latex-escrita/notes-latex/aula-15.pdf)"
slide: "[📄 Slide (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-15-branco.pdf)"
tags:
  - latex
  - escrita-academica
  - abnt
  - ifftese
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty">Próxima Aula</a></b></div>
</div>

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material da Aula
> - 📄 **[Slides LaTeX — Modelo Branco (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-15-branco.pdf)** — *Apresentação visual institucional em tema claro.*
> - 📄 **[Slides LaTeX — Modelo Preto (PDF)](/assets/biblioteca/latex-escrita/slides-latex/aula-15-preto.pdf)** — *Apresentação visual institucional em tema escuro.*
> - 📝 **[Notas de Aula Institucionais (PDF)](/assets/biblioteca/latex-escrita/notes-latex/aula-15.pdf)** — *Apostila técnica completa em LaTeX.*
> 
> ### 🌐 Links Externos de Apoio
> - **[CTAN (Comprehensive TeX Archive Network)](https://ctan.org/)** — *Repositório mundial de pacotes TeX.*
> - **[ABNT — Catálogo de Normas Técnicas](https://www.abnt.org.br/)** — *Portal oficial de normas NBR 14724, 10520 e 6023.*
> - **[Overleaf Documentation](https://www.overleaf.com/learn)** — *Guias interativos de compilação TeX.*

## 📋 Sumário Interativo
- [📍 1. Fundamentos e Contextualização](#-1-fundamentos-e-contextualização)
- [📍 2. Conceitos-Chave e Normas ABNT](#-2-conceitos-chave-e-normas-abnt)
- [📍 3. Aplicação Prática no Ecossistema ReLaTeX](#-3-aplicação-prática-no-ecossistema-relatex)
- [🔗 Aulas Correlatas & Conexões](#-aulas-correlatas--conexões)
- [📚 Referências Bibliográficas](#-referências-bibliográficas)

## 📖 Conteúdo da Aula

Engenharia e desenvolvimento do arquivo de metadados centralizado (`metadados.sty`). Abordagem de desativação de dados sensíveis, flexão dinâmica de gênero para cargos (Orientador/Orientadora, Coordenador/Coordenadora) e padronização institucional IFF.

### 📍 1. Conceito de Fonte Única da Verdade (*Single Source of Truth*)

Centralização de todos os metadados da pesquisa (Título, Autor, Orientador, Banca, Data, Campus) em um único arquivo de configuração `.sty` desacoplado da estrutura da monografia.

### 📍 2. Lógica Condicional e Flexão Dinâmica de Gênero

Implementação de macros TeX condicionais (`\ifdefined`, `\equal`) para alternância automática de rótulos institucionais de acordo com o gênero dos docentes (ex: *Orientadora*, *Examinadora*).

### 📍 3. Higienização de Dados Sensíveis e Versão Pública

Criação de chaves de controle no metadados para anonimização de dados discentes na versão de submissão para bancas cegas (*blind review*).

### 📊 Fluxograma Metodológico da Aula (Mermaid)
```mermaid
flowchart TD
    A[Fundamentação Teórica] --> B[Normalização ABNT Vigente]
    B --> C[Implementação em LaTeX/ReLaTeX]
    C --> D[Compilação e Validação de Resultados]
```

## 🔗 Aulas Correlatas & Conexões

Esta aula conecta-se transversalmente aos seguintes tópicos da formação em LaTeX & Escrita Acadêmica:

- 🔗 **[[pt-br/resource/latex/aula-11-arquitetura-latex-motores-tex-e-preambulo-tex|Aula 11: Arquitetura do Kernel LaTeX2e, Motores PDFLaTeX/LuaLaTeX/XeLaTeX e Estrutura do Preâmbulo .tex]]**
- 🔗 **[[pt-br/resource/latex/aula-17-engenharia-da-classe-ifftese-cls|Aula 17: Engenharia de Classes .cls - Anatomia da ifftese e abntex2]]**

## 📚 Referências Bibliográficas

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 14724**: Informação e documentação — Trabalhos acadêmicos — Apresentação. Rio de Janeiro: ABNT, 2011.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 10520**: Informação e documentação — Citações em documentos — Apresentação. Rio de Janeiro: ABNT, 2023.
- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6023**: Informação e documentação — Referências — Elaboração. Rio de Janeiro: ABNT, 2018.

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/latex/aula-14-graficos-vetoriais-tikz-e-pgfplots">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/latex/aula-16-desenvolvimento-de-pacotes-e-macros-sty">Próxima Aula</a></b></div>
</div>
