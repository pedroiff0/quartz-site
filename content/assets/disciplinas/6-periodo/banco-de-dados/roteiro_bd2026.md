---
title: "Roteiro - Normalização & Dependências Funcionais"
subtitle: "Apresentação Banco de Dados - 6º Período (Centro de Memória)"
discipline: Banco de Dados
period: 6-periodo
professor: Pablo Manhães
date: 2026-09-02
status: concluido
authors:
  - Arthur de Oliveira Lima Potente
  - Breno Luiz Silva do Carmo
  - Isaac Salles Gonçalves
  - Pedro Henrique Rocha de Andrade
tags:
  - disciplina
  - engenharia-de-computacao
  - trabalho
  - apresentacao
  - atividade
  - banco-de-dados
  - normalizacao
  - dependencias-funcionais
draft: false
---

# Roteiro de Apresentação — Normalização & Dependências Funcionais

> [!info] Dados da Apresentação
> - **Disciplina:** Banco de Dados — 6º Período
> - **Docente:** Pablo Manhães
> - **Data:** 02/09/2026
> - **Tema:** Teoria Relacional e Decomposição em 1FN, 2FN e 3FN (Caso Centro de Memória)
> - **Slides:** 11 slides (LaTeX Beamer)

---

## ⏱️ Tempo Estimado: ~10 minutos

---

## 📋 Roteiro por Slide

### Slide 1 — Capa (15s)
- Título: Normalização & Dependências Funcionais
- Subtítulo: Teoria Relacional e Decomposição em 1FN, 2FN e 3FN (Caso Centro de Memória)
- Apresentar autores e instituição

### Slide 2 — Sumário (15s)
- Roteiro: Conceitos → Cenário 0FN → 1FN → 2FN → 3FN → Conclusões

### Slide 3 — Conceitos (1min30s)
- **Definição de DF:** $X \to Y$ — X determina unicamente Y
- **Determinante vs Determinado:** lado esquerdo determina, lado direito depende
- **Anomalias Clássicas:**
  - Inserção: impossível cadastrar entidade A sem entidade B
  - Exclusão: apagar registro perde informação colateral
  - Alteração: múltiplas linhas precisam de update
- **Objetivo:** Eliminar redundâncias sem perda de dados

### Slide 4 — Cenário 0FN (1min30s)
- **Domínio:** Sistema Centro de Memória — acervo, doações e exposições unificados
- **Tabela única** com todos os dados misturados
- **Anomalia de Inserção:** Impossível cadastrar doador sem item do acervo
- **Anomalia de Exclusão:** Cancelar exposição apaga o item do acervo
- **Anomalia de Alteração:** Atualização repetida de dados do doador

### Slide 5 — 1FN (1min)
- **Regra:** Atributos estritamente atômicos (indivisíveis)
- **Problema:** `palavras_chave` agrupadas na mesma célula ("Python, C++, SQL")
- **Solução:** Extração para tabela associativa
  - `Item_PalavraChave(cod_tombo, palavra_chave)`
- **Benefício:** Atomicidade + facilidade de indexação

### Slide 6 — 2FN (1min30s)
- **Regra:** Estar na 1FN + sem dependências parciais
- **Problema:** Título depende só de `cod_tombo` (chave composta: `cod_tombo + cod_exposicao`)
- **Decomposição:**
  - `Exposicao(codigo_exposicao, titulo, ...)`
  - `Item_Acervo(cod_tombo, titulo, ...)`
  - `Item_Exposicao(cod_exp, cod_tombo, pos)`
- **Garantia:** Atributos dependem da chave primária completa

### Slide 7 — 3FN (1min30s)
- **Regra:** Estar na 2FN + sem dependências transitivas
- **Problema:** `cod_tombo → cod_doacao → dados_doador` (cadeia transitiva)
- **Decomposição:**
  - `Doacao(cod_doacao, data, termo, id_doador)`
  - `Pessoa(id_pessoa, nome, cpf, email, ...)`
- **Vínculo:** `Item_Acervo` mantém apenas FK `cod_doacao`

### Slide 8 — Conclusões (1min)
- **Lossless Join:** Junção natural recompõe dados sem perdas
- **Preservação de DFs:** Regras garantidas localmente por constraints
- **Redundância Nula:** Cada fato registrado em uma única tabela
- **Integridade:** Consistência assegurada por PKs e FKs

### Slide 9 — Comparação (30s)
| Critério | 0FN (Bruto) | 3FN (Normalizado) |
|----------|-------------|-------------------|
| Redundância | Alta | Nula |
| Anomalias | Críticas | Inexistentes |
| Integridade | Frágil | Máxima |
| Update | Lento (múltiplas linhas) | Instantâneo (linha única) |

### Slide 10 — Referências (15s)
- ELMASRI & NAVATHE — Sistemas de Banco de Dados (7ed, Pearson)
- SILBERSCHATZ, KORTH & SUDARSHAN — Sistema de Banco de Dados (6ed, Elsevier)
- CODD — A Relational Model of Data (1970)
- DATE — Introdução a Sistemas de Bancos de Dados (8ed, Elsevier)
- IBM — Database Normalization: Guia Prático (2024)

### Slide 11 — Obrigado! (15s)
- Agradecimento
- Contatos:
  - pedroiff0@gmail.com
  - brenooh7@gmail.com
  - isaacsalles2005@gmail.com
  - arthurpotente16@gmail.com
- Link: phrandrade.com/pt-br/resource/engenharia-de-computação

---

## 🎯 Pontos-chave para Enfatizar

1. **Centro de Memória** é o caso concreto (não abstrair demais)
2. **Cada anomalia** tem exemplo real no domínio
3. **Decomposição** resolve problema específico (não é "mágica")
4. **Garantias formais** (Lossless Join + Preservação de DFs) dão rigor

## ⚠️ Possíveis Perguntas

- "Por que não BCNF?" → BCNF pode não preservar DFs; 3FN é suficiente
- "E a performance?" → JOINs são custosos, mas compensam pela integridade
- "Quando NÃO normalizar?" → Data warehouses, leitura intensiva (denormalização controlada)
