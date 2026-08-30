---
publish: true
title: "Trabalho - Normalização e Dependências Funcionais"
subtitle: "Fundamentação Matemática das Dependências Funcionais e Decomposição em 1FN, 2FN e 3FN (Caso Centro de Memória)"
discipline: "Banco de Dados"
period: "6-periodo"
professor: "Pablo Manhães"
date: 02/09/2026
status: planejando
authors:
  - Pedro Henrique Rocha de Andrade
  - Breno Luiz
  - Isaac Salles
corresponding_author: "Pedro Henrique Rocha de Andrade <pedroiff0@gmail.com>"
presenter: "Pedro Henrique Rocha de Andrade"
short_title: "Normalização & DFs"
encrypted: true
password: "eng232"

# 🔗 Links e Materiais do Trabalho & Slides (LaTeX / Quartz)
disciplina_url: "https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/banco-de-dados/"
trabalho_url: "https://www.phrandrade.com/pt-br/resource/engenharia-de-computacao/6-periodo/banco-de-dados/anotacoes/atividades/trabalho---normalizacao-e-dependencias-funcionais/"
roteiro_pdf: "roteiro_iff_disciplina.pdf"
slides_latex_claro: "slides_iff_disciplina.pdf"
slides_latex_escuro: "slides_iff_disciplina_preto.pdf"
portal_institucional: "https://portal1.iff.edu.br/"

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
cssclasses:
  - page-layout
modified: 2026-08-30T15:58:00-03:00
---

# 🎓 Trabalho - Normalização e Dependências Funcionais em Banco de Dados

> [!abstract] Resumo Executivo da Apresentação
> Este trabalho apresenta o estudo formal e aplicado do processo de **Normalização de Esquemas Relacionais**, utilizando a teoria das **Dependências Funcionais (DFs)** como alicerce matemático. Demonstra-se, a partir de um cenário não-normalizado do **Sistema de Gestão de Acervo, Digitalização e Exposições de um Centro de Memória**, a transição sistemática da **Forma Não-Normalizada (0FN)** para a **1FN**, **2FN** e **3FN**, eliminando anomalias de inserção, atualização e exclusão, com garantia formal de *Junção sem Perdas (Lossless Join)* e *Preservação de Dependências*.

> [!info] 📌 Informações & Checklist do Trabalho
> - **Docente:** Pablo Manhães
> - **Data Prevista:** 02/09/2026
> - **Apresentador:** Pedro Henrique Rocha de Andrade
> - **Autores / Equipe:** Pedro Henrique Rocha de Andrade, Breno Luiz e Isaac Salles
> - **Status da Atividade:** 🟡 `Planejando` *(Status no frontmatter: `status: planejando`)*
> - [ ] 🎯 Apresentar Trabalho: Normalização e Dependências Funcionais

> [!important] 🔒 Acesso e Senha dos Arquivos
> Os materiais gerados na pasta `_materiais/` e espelhados no Quartz Site são protegidos pela senha canônica:
> **`eng232`**

---

## 📂 Recursos & Materiais da Disciplina

> [!tip] 🔗 Links e Materiais Vinculados (Banco de Dados)
> - 📑 **Roteiro & Documento Técnico (PDF):** [[02 - Áreas/Acadêmico/IFF - Engenharia de Computação/_materiais/6-periodo/banco-de-dados/roteiro_iff_disciplina.pdf|roteiro_iff_disciplina.pdf]] *(Documento formatado em LaTeX institucional)*
> - 📊 **Slides Beamer Institucionais (PDF Claro):** [[02 - Áreas/Acadêmico/IFF - Engenharia de Computação/_materiais/6-periodo/banco-de-dados/slides_iff_disciplina.pdf|slides_iff_disciplina.pdf]] *(Apresentação Institucional IFF - Modo Claro)*
> - 📊 **Slides Beamer Institucionais (PDF Escuro):** [[02 - Áreas/Acadêmico/IFF - Engenharia de Computação/_materiais/6-periodo/banco-de-dados/slides_iff_disciplina_preto.pdf|slides_iff_disciplina_preto.pdf]] *(Apresentação Institucional IFF - Modo Noturno)*
> - 💻 **Apresentação em PowerPoint (PPTX Claro):** `slides_iff_disciplina.pptx`
> - 💻 **Apresentação em PowerPoint (PPTX Escuro):** `slides_iff_disciplina_preto.pptx`
> - 🌐 **Hub da Disciplina no Quartz:** [Acessar Hub de Banco de Dados](https://www.phrandrade.com/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados/)
> - 🏛️ **Portal Institucional IFF:** [portal1.iff.edu.br](https://portal1.iff.edu.br/)

> [!info] 🛠️ Guia das Propriedades de Links e Apresentação
> - **`disciplina_url`**: URL aberta ao clicar no **Nome da Disciplina** no cabeçalho superior dos slides.
> - **`trabalho_url`**: URL aberta ao clicar no **"Seminário \| `short_title`"** ou no **título do rodapé** dos slides, levando ao endereço público deste `.md` no Quartz.
> - **`short_title`**: Título curto exibido no cabeçalho dos slides (ao lado de `Nome da Disciplina | ...`).
> - **`roteiro_pdf`**: Nome do PDF do relatório em `_materiais/`, linkado no rodapé do card de figura lateral nos slides.
> - **`slides_latex_claro` & `slides_latex_escuro`**: Nomes dos PDFs dos slides Beamer (claro e noturno).
> - **QR Code (Encerramento):** Redireciona para o portal principal de **Engenharia de Computação** (`phrandrade.com/disciplinas`).

---

## Anotações & Links de Referência

- **IBM Think:** [Normalização de Banco de Dados](https://www.ibm.com/br-pt/think/topics/database-normalization)
- **Medium (Célio Normando):** [Dependências Funcionais e Normalização](https://medium.com/@celionormando/depend%C3%AAncias-funcionais-e-normaliza%C3%A7%C3%A3o-9098c3ac9c33)
- **DataCamp:** [Tutorial de Normalização em SGBD](https://www.datacamp.com/pt/tutorial/normalization-in-dbms)

---

## 🎯 1. Fundamentos & Motivação Teórica

### 1.1 O Papel da Teoria Relacional
O modelo relacional clássico proposto por **Edgar F. Codd (1970)** fundamenta o armazenamento e a recuperação de dados em conceitos matemáticos de conjuntos e lógica de predicados de primeira ordem. Em um ambiente operacional, esquemas relacionais mal projetados sofrem de três patologias graves decorrentes da **redundância de dados**:

```
                  ┌───────────────────────────────────────────┐
                  │          PATOLOGIAS DE ESQUEMA            │
                  ├───────────────────────────────────────────┤
                  │ 1. Anomalia de Inserção                   │
                  │    Impossibilidade de inserir dados de    │
                  │    uma entidade sem criar dados de outra  │
                  │ ───────────────────────────────────────── │
                  │ 2. Anomalia de Exclusão                   │
                  │    A exclusão de uma tupla acarreta a     │
                  │    perda colateral de informações vitais  │
                  │ ───────────────────────────────────────── │
                  │ 3. Anomalia de Atualização                │
                  │    Alteração de um dado exige múltiplos   │
                  │    updates em tuplas redundantes; falha   │
                  │    gera inconsistência interna do SGBD    │
                  └───────────────────────────────────────────┘
```

### 1.2 O Conceito Central: Dependência Funcional (DF)
Uma **Dependência Funcional** é uma restrição formal entre dois conjuntos de atributos $X$ e $Y$ pertencentes a uma relação $R$, denotada por:

$$X \to Y \quad \text{("X determina funcionalmente Y")}$$

Formalmente, diz-se que $X \to Y$ se e somente se, para quaisquer duas tuplas $t_1, t_2 \in R$:

$$t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$

- **Determinante ($X$):** O conjunto de atributos do lado esquerdo.
- **Determinado ($Y$):** O conjunto de atributos do lado direito.
- **Superchave:** Um conjunto de atributos $K \subseteq R$ tal que $K \to R$.
- **Chave Candidata ($CK$):** Uma superchave mínima (nenhum subconjunto próprio de $CK$ é superchave).
- **Atributo Primo:** Qualquer atributo que componha pelo menos uma chave candidata.
- **Atributo Não-Primo:** Atributo que não participa de nenhuma chave candidata.

---

## 🔍 2. O Cenário Não-Normalizado: Centro de Memória

Para ilustrar o processo completo de forma direta e compreensível, examinamos o sistema de **Gestão de Acervo, Doações, Digitalização e Exposições de um Centro de Memória**:

### 2.1 A Relação Universal Não-Normalizada (0FN)
Suponha uma tabela única `REGISTRO_CENTRO_MEMORIA` que agrupa dados do acervo, palavras-chave, doações, digitalizações e eventos expositivos:

$$\text{REGISTRO\_CENTRO\_MEMORIA}( \underline{\text{cod\_exposicao}}, \underline{\text{cod\_tombo}}, \text{titulo\_item}, \text{data\_aprox}, \text{palavras\_chave}, \text{cod\_doacao}, \text{data\_doacao}, \text{id\_doador}, \text{nome\_doador}, \text{posicao\_secao}, \text{txt\_legenda} )$$

| cod_exposicao | cod_tombo | titulo_item | data_aprox | palavras_chave | cod_doacao | data_doacao | id_doador | nome_doador | posicao_secao | txt_legenda |
| :---: | :---: | :--- | :---: | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **EXP01** | **T101** | Foto Fundadores | 1950 | Fotografia, Memória, IFF | D01 | 15/03/2026 | P01 | Carlos Silva | Vitrine A1 | Foto original dos fundadores |
| **EXP01** | **T102** | Ata Inaugural | 1952 | Documento, Ata, História | D01 | 15/03/2026 | P01 | Carlos Silva | Vitrine A2 | Primeira ata do conselho |
| **EXP02** | **T101** | Foto Fundadores | 1950 | Fotografia, Memória, IFF | D01 | 15/03/2026 | P01 | Carlos Silva | Painel B | Cópia histórica restaurada |
| **EXP02** | **T103** | Teodolito Antigo | 1960 | Instrumento, Topografia | D02 | 20/04/2026 | P02 | Ana Souza | Suporte C1 | Usado nas medições do campus |

### 2.2 Diagnóstico das Anomalias Práticas
1. **Anomalia de Inserção:** Impossível cadastrar uma nova doação ou um novo doador sem vincular imediatamente a um item do acervo e a uma exposição.
2. **Anomalia de Exclusão:** Se a exposição `EXP02` for cancelada e suas linhas apagadas, o item `T103` (**Teodolito Antigo**) é apagado do banco de dados se não constar em nenhuma outra exposição!
3. **Anomalia de Atualização:** O nome do doador `Carlos Silva` (`P01`) e a data da doação `D01` estão repetidos em 3 tuplas. Se o doador corrigir seu nome, todas as tuplas precisam de atualização simultânea.

---

## 📐 3. Dependências Funcionais & O Processo de Normalização Passo a Passo

```
       [ 0FN: Relação Universal com Palavras-Chave Multivaloradas ]
                                  │
                                  ▼ (Eliminar Atributos Multivalorados)
       [ 1ª Forma Normal (1FN): Valores Estritamente Atômicos ]
                                  │
                                  ▼ (Eliminar Dependências Parciais da Chave Composta)
       [ 2ª Forma Normal (2FN): Total Dependência da Chave Primária ]
                                  │
                                  ▼ (Eliminar Dependências Transitivas entre Não-Chaves)
       [ 3ª Forma Normal (3FN): Sem Dependências Transitivas ]
```

### 3.1 Mapeamento Formal das Dependências Funcionais
Analisando as regras de negócio do domínio do Centro de Memória:

1. **$\text{DF}_1$ (Chave Composta $\to$ Atributos da Exibição):**
   $$\{ \text{cod\_exposicao}, \text{cod\_tombo} \} \to \{ \text{posicao\_secao}, \text{txt\_legenda} \}$$
2. **$\text{DF}_2$ (Dependência Parcial do Item do Acervo):**
   $$\text{cod\_tombo} \to \{ \text{titulo\_item}, \text{data\_aprox}, \text{cod\_doacao} \}$$
3. **$\text{DF}_3$ (Dependência Parcial da Exposição):**
   $$\text{cod\_exposicao} \to \{ \text{titulo\_exposicao}, \text{tema}, \text{data\_inicio}, \text{local\_realizacao} \}$$
4. **$\text{DF}_4$ (Dependência Transitiva da Doação):**
   $$\text{cod\_doacao} \to \{ \text{data\_doacao}, \text{id\_doador}, \text{termo\_assinado} \}$$
5. **$\text{DF}_5$ (Dependência Transitiva da Pessoa Doadora):**
   $$\text{id\_doador} \to \{ \text{nome\_doador}, \text{cpf}, \text{email} \}$$

---

### 3.2 Passo 1: Transição para a 1ª Forma Normal (1FN)

> [!tip] Regra da 1FN
> Uma relação $R$ está na **1FN** se e somente se todos os atributos contêm apenas **valores atômicos (indivisíveis)** e não existem atributos multivalorados ou grupos repetitivos.

#### Problema Identificado:
O atributo `palavras_chave` contém múltiplos valores concatenados na mesma célula (ex: `"Fotografia, Memória, IFF"`).

#### Solução:
Isolar o atributo multivalorado em uma tabela associativa atômica `Item_PalavraChave`:

$$\text{Item\_PalavraChave}( \underline{\text{cod\_tombo}}, \underline{\text{palavra\_chave}} )$$

A relação de itens em exposições mantém apenas atributos atômicos:

$$\text{R\_1FN}( \underline{\text{cod\_exposicao}}, \underline{\text{cod\_tombo}}, \text{titulo\_item}, \text{data\_aprox}, \text{cod\_doacao}, \text{data\_doacao}, \text{id\_doador}, \text{nome\_doador}, \text{posicao\_secao}, \text{txt\_legenda} )$$

---

### 3.3 Passo 2: Transição para a 2ª Forma Normal (2FN)

> [!tip] Regra da 2FN
> Uma relação $R$ está na **2FN** se e somente se:
> 1. Está na **1FN**;
> 2. **Nenhum atributo não-primo é dependente parcial de qualquer chave candidata composta de $R$**. Todo atributo não-primo deve depender da totalidade da chave primária.

#### Problema Identificado:
A chave primária é composta por $\{ \text{cod\_exposicao}, \text{cod\_tombo} \}$.
- $\text{DF}_2: \text{cod\_tombo} \to \{ \text{titulo\_item}, \text{data\_aprox}, \text{cod\_doacao}, \text{data\_doacao}, \text{id\_doador}, \text{nome\_doador} \}$ $\implies$ Dependência Parcial!
- $\text{DF}_3: \text{cod\_exposicao} \to \{ \text{titulo\_exposicao}, \text{tema}, \text{data\_inicio} \}$ $\implies$ Dependência Parcial!

#### Solução (Decomposição em 2FN):
Criamos relações separadas para cada determinante parcial:

1. **`Exposicao`** (elimina a dependência de `cod_exposicao`):
   $$\text{Exposicao}( \underline{\text{codigo\_exposicao}}, \text{titulo}, \text{tema}, \text{data\_inicio}, \text{data\_termino}, \text{modalidade}, \text{local\_realizacao} )$$

2. **`Item_Acervo_Temp`** (elimina a dependência de `cod_tombo`):
   $$\text{Item\_Acervo\_Temp}( \underline{\text{cod\_tombo}}, \text{titulo}, \text{data\_aprox}, \text{estado\_conservacao}, \text{procedencia}, \text{cod\_doacao}, \text{data\_doacao}, \text{id\_doador}, \text{nome\_doador} )$$

3. **`Item_Exposicao`** (mantém apenas atributos totalmente dependentes da chave composta):
   $$\text{Item\_Exposicao}( \underline{\text{codigo\_exposicao}}, \underline{\text{cod\_tombo}}, \text{posicao\_secao}, \text{txt\_legenda}, \text{cond\_exibicao}, \text{autoriz\_especifica} )$$

---

### 3.4 Passo 3: Transição para a 3ª Forma Normal (3FN)

> [!tip] Regra da 3FN
> Uma relação $R$ está na **3FN** se e somente se:
> 1. Está na **2FN**;
> 2. **Nenhum atributo não-primo depende transitivamente da chave primária**.
>
> Para toda dependência funcional não-trivial $X \to A$, deve ocorrer:
> - $X$ é uma superchave de $R$; **OU**
> - $A$ é um atributo primo (membro de uma chave candidata).

#### Problema Identificado:
Na tabela `Item_Acervo_Temp`, a chave primária é $\text{cod\_tombo}$.
Existe a cadeia transitiva:

$$\text{cod\_tombo} \xrightarrow{\text{DF}_2} \text{cod\_doacao} \xrightarrow{\text{DF}_4} \{ \text{data\_doacao}, \text{id\_doador} \} \xrightarrow{\text{DF}_5} \text{nome\_doador}$$

Como $\text{cod\_doacao}$ **não é chave primária** de `Item_Acervo_Temp`, temos violação direta da 3FN.

#### Solução (Decomposição em 3FN):
Extraímos as entidades independentes de doação e pessoa:

1. **`Pessoa`:**
   $$\text{Pessoa}( \underline{\text{id\_pessoa}}, \text{nome\_completo}, \text{cpf}, \text{email\_principal}, \text{data\_nascimento} )$$

2. **`Doacao`:**
   $$\text{Doacao}( \underline{\text{codigo\_doacao}}, \text{data\_recebimento}, \text{termo\_assinado}, \text{observacoes}, \text{situacao}, \text{id\_pessoa\_doador} )$$
   *Chave Estrangeira:* `id_pessoa_doador REFERENCES Pessoa(id_pessoa)`

3. **`Item_Acervo`:**
   $$\text{Item\_Acervo}( \underline{\text{cod\_tombo}}, \text{titulo}, \text{data\_aprox}, \text{estado\_conservacao}, \text{procedencia}, \text{codigo\_doacao} )$$
   *Chave Estrangeira:* `codigo_doacao REFERENCES Doacao(codigo_doacao)`

---

## 📈 4. Comparativo de Esquemas, Garantias Formais & Conclusões

### 4.1 O Esquema Relacional Final Normalizado (3FN / BCNF)

O banco de dados final do Centro de Memória é estruturado de forma desacoplada e coesa:

```
 ┌────────────────────────┐             ┌────────────────────────┐
 │       Exposicao        │             │         Doacao         │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 codigo_exposicao    │             │ 🔑 codigo_doacao       │
 │    titulo              │             │    data_recebimento    │
 │    tema                │             │    termo_assinado      │
 │    data_inicio         │             │ 🔗 id_pessoa_doador    │
 └───────────┬────────────┘             └───────────▲────────────┘
             │ (1:N)                                │ (1:N)
             │                                      │
 ┌───────────▼────────────┐             ┌───────────┴────────────┐
 │     Item_Exposicao     │             │       Item_Acervo      │
 ├────────────────────────┤             ├────────────────────────┤
 │ 🔑 codigo_exposicao(FK)│ (N:1)       │ 🔑 cod_tombo           │
 │ 🔑 cod_tombo (FK)      ├─────────────►    titulo              │
 │    posicao_secao       │             │    data_aprox          │
 │    txt_legenda         │             │ 🔗 codigo_doacao (FK)  │
 └────────────────────────┘             └───────────┬────────────┘
                                                    │ (1:N)
                                        ┌───────────┴────────────┐
                                        │   Item_PalavraChave    │
                                        ├────────────────────────┤
                                        │ 🔑 cod_tombo (PK, FK)  │
                                        │ 🔑 palavra_chave (PK)  │
                                        └────────────────────────┘
```

### 4.2 Garantias Matemáticas da Decomposição

1. **Decomposição sem Perdas (*Lossless-Join Decomposition*):**
   Garante que o `NATURAL JOIN` das tabelas normalizadas reconstitui exatamente a relação universal original, sem geração de tuplas espúrias:
   $$\Pi_{R_1}(R) \bowtie \Pi_{R_2}(R) = R \iff (R_1 \cap R_2 \to R_1) \lor (R_1 \cap R_2 \to R_2)$$

2. **Preservação de Dependências (*Dependency Preservation*):**
   Todas as dependências funcionais originais podem ser fiscalizadas dentro das relações individuais por meio de chaves primárias e *Foreign Keys*.

### 4.3 Tabela Comparativa de Avaliação

| Métrica / Critério | Esquema 0FN (Tabela Única) | Esquema 3FN (Normalizado) |
| :--- | :---: | :---: |
| **Redundância de Dados** | Crítica (dados de doadores e exposições duplicados) | Nula (cada fato registrado em uma única tabela) |
| **Anomalias de Inserção/Exclusão** | Constantes (impossível cadastrar doador avulso) | Inexistentes (entidades independentes com FKs) |
| **Integridade Relacional** | Frágil (risco de grafias divergentes) | Máxima (garantida por restrições de integridade) |
| **Desempenho de Atualização** | Lento (múltiplas linhas alteradas) | Instantâneo (modificação atômica em tupla única) |

---

## 📚 5. Referências Bibliográficas e Materiais de Apoio
- 1. ELMASRI, Ramez; NAVATHE, Shamkant B. *Sistemas de Banco de Dados*. 7. ed. São Paulo: Pearson, 2018. (Capítulo 14: Teoria de Projeto de Bancos de Dados Relacionais e Dependências Funcionais; Capítulo 15: Algoritmos de Projeto de Bancos de Dados Relacionais).
- 2. SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. *Sistema de Banco de Dados*. 6. ed. Rio de Janeiro: Elsevier, 2012. (Capítulo 8: Projeto de Banco de Dados Relacional).
- 3. CODD, Edgar F. *A Relational Model of Data for Large Shared Data Banks*. Communications of the ACM, v. 13, n. 6, p. 377-387, 1970.
- 4. DATE, C. J. *Introdução a Sistemas de Bancos de Dados*. 8. ed. Rio de Janeiro: Elsevier, 2004.
- 5. IBM. *Database Normalization: Guia Prático de Normalização*. IBM Think Topics. Disponível em: <https://www.ibm.com/br-pt/think/topics/database-normalization>.
- 6. NORMANDO, Célio. *Dependências Funcionais e Normalização de Dados*. Medium. Disponível em: <https://medium.com/@celionormando/depend%C3%AAncias-funcionais-e-normaliza%C3%A7%C3%A3o-9098c3ac9c33>.
- 7. DATACAMP. *Normalization in DBMS Tutorial*. Disponível em: <https://www.datacamp.com/pt/tutorial/normalization-in-dbms>.
