---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-05-modelagem-comportamental-diagramas-de-sequencia
title: "Aula 05: Modelagem Comportamental: Diagramas de Sequência — Análise de Software Orientada a Objetos"
created: 2026-09-30T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-05
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Análise de Software Orientada a Objetos"
professor: "Bruno"
conteudo: "Troca de mensagens síncronas/assíncronas, linhas de vida, fragmentos combinados (loop, alt, opt) e diagrama de comunicação."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-04-modelagem-estrutural-diagramas-de-classes-e-pacotes">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-06-diagramas-de-atividades-e-maquinas-de-estados">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Análise de Software Orientada a Objetos (CSECBJI.42)
> - **Professor:** Bruno
> - **Data Realizada:** 30/09/2026
> - **Tópico Principal:** Modelagem Comportamental: Diagramas de Sequência
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-05-analise-de-software-orientada-a-objetos|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-05-analise-de-software-orientada-a-objetos|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Modelagem Comportamental: Diagramas de Sequência](#-anotações-do-quadro-modelagem-comportamental-diagramas-de-sequência)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Modelagem Comportamental: Diagramas de Sequência

### 5.1 Diagramas de Sequência (UML)
O Diagrama de Sequência é um modelo comportamental dinâmico que descreve a troca ordenada de mensagens entre objetos ao longo do tempo para realizar um caso de uso específico.

### 5.2 Elementos Fundamentais
- **Linha de Vida (*Lifeline*):** Linha vertical tracejada representando a existência temporal do objeto.
- **Barra de Ativação (*Focus of Control*):** Retângulo sobre a linha de vida indicando quando o objeto está processando uma operação.
- **Mensagem Síncrona:** Seta com ponta preenchida ($\longrightarrow$). O emissor bloqueia aguardando o retorno.
- **Mensagem Assíncrona:** Seta com ponta aberta ($\longrightarrow$). O emissor continua a execução sem esperar.
- **Mensagem de Retorno:** Linha tracejada com seta aberta ($\dashrightarrow$).
- **Criação e Destruição de Objetos:** Mensagem `<<create>>` apontando para a caixa do objeto e 'X' no final da linha de vida para destruição.

### 5.3 Fragmentos Combinados de Controle
- `alt` (Alternativa): Representa blocos `if-then-else` mutuamente exclusivos.
- `opt` (Opcional): Representa um bloco condicional simples `if` sem `else`.
- `loop`: Representa uma repetição `for` / `while` sobre uma coleção.
- `par`: Execução paralela simultânea de mensagens.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Diagrama de Sequência: Realização do Processamento de Pedido

1. O `ClienteUI` envia `finalizarPedido(itens)` para o `PedidoController`.
2. O `PedidoController` cria uma nova instância de `Pedido`.
3. O `Pedido` itera em um `loop` sobre os itens calculando o total.
4. O `PedidoController` invoca `processar(total)` no `GatewayPagamento`.
5. Em fragmento `alt`:
   - Se aprovado: O `PedidoController` chama `salvar(pedido)` no `Repositorio` e retorna confirmação.
   - Se recusado: Retorna mensagem de erro de pagamento.

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
sequenceDiagram
    autonumber
    actor Cliente
    participant UI as PedidoUI
    participant Ctrl as PedidoController
    participant Ped as novoPedido : Pedido
    participant Gate as GatewayPagamento

    Cliente->>UI: Clicar "Pagar"
    UI->>Ctrl: finalizarPedido(dados)
    Ctrl->>Ped: <<create>>(itens)
    loop Para cada item
        Ped->>Ped: calcularSubtotal()
    end
    Ctrl->>Gate: cobrar(total)
    alt Pagamento Aprovado
        Gate-->>Ctrl: Sucesso (TransacaoID)
        Ctrl-->>UI: Exibir "Pedido Confirmado"
    else Pagamento Recusado
        Gate-->>Ctrl: Erro (Saldo Insuficiente)
        Ctrl-->>UI: Exibir "Falha no Pagamento"
    end
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Diagrama de Sequência de Sistema (DSS) vs de Projeto** | O DSS trata o sistema inteiro como uma **caixa preta única** interagindo com o ator; o Diagrama de Sequência de Projeto detalha as chamadas internas entre as classes Controller, Model e Repositorio. | Não confunda os dois níveis de abstração! |
| **Ordem Top-to-Bottom** | O tempo flui estritamente de cima para baixo no diagrama de sequência. | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Desenhe o Diagrama de Sequência de Projeto para o caso de uso de autenticação de usuário com verificação de senha criptografada e token JWT.
2. Modele um fragmento `par` representando a emissão simultânea de nota fiscal e envio de e-mail de confirmação.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-04-modelagem-estrutural-diagramas-de-classes-e-pacotes">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos/anotacoes/aula-06-diagramas-de-atividades-e-maquinas-de-estados">Próxima Aula</a></b></div>
</div>
