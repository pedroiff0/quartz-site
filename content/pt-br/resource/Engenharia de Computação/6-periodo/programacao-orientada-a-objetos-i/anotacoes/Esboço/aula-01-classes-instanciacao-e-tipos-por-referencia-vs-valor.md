---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-01-classes-instanciacao-e-tipos-por-referencia-vs-valor
title: "Aula 01: Classes, Instanciação e Tipos por Referência vs Valor — Programação Orientada a Objetos I"
created: 2026-09-02T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-01
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Programação Orientada a Objetos I"
professor: "Sérgio / Bruno"
conteudo: "Declaração de classes, alocação no Heap vs Stack, ciclo de vida de objetos e Garbage Collection básico."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-00-apresentacao-da-disciplina-configuracao-da-jdk-e-ambiente">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-02-encapsulamento-modificadores-de-acesso-e-construtores">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Programação Orientada a Objetos I (CSECBJI.45)
> - **Professor:** Sérgio / Bruno
> - **Data Realizada:** 02/09/2026
> - **Tópico Principal:** Classes, Instanciação e Tipos por Referência vs Valor
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-01-programacao-orientada-a-objetos-i|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-01-programacao-orientada-a-objetos-i|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Classes, Instanciação e Tipos por Referência vs Valor](#-anotações-do-quadro-classes,-instanciação-e-tipos-por-referência-vs-valor)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Classes, Instanciação e Tipos por Referência vs Valor

### 1.1 Classes e Objetos
- **Classe:** O molde, especificação ou modelo abstrato que define a estrutura de dados (atributos/campos) e os comportamentos (métodos) de uma entidade.
- **Objeto:** Uma instância concreta e independente da classe alocada na memória em tempo de execução via operador `new`.

### 1.2 Gerenciamento de Memória: Stack vs Heap
1. **Pilha de Execução (*Stack*):**
   - Armazena variáveis locais de métodos e variáveis de tipos primitivos (`int`, `double`, `boolean`, `char`).
   - Gerenciamento automático rápido em formato LIFO (alocado na chamada do método, liberado no retorno).
2. **Memória Dinâmica (*Heap*):**
   - Todos os objetos e instâncias de classes residem **obrigatoriamente no Heap**.
   - As variáveis do tipo classe na Stack armazenam apenas **endereços/referências** que apontam para o objeto no Heap.
   - A desalocação de objetos não mais referenciados é feita de forma assíncrona pelo **Garbage Collector (GC)**.

### 1.3 Passagem de Parâmetros: Java é SEMPRE Passagem por Valor!
- Para tipos primitivos, copia-se o valor numérico literal.
- Para tipos por referência (objetos), **copia-se o valor da referência (o endereço de memória)**. Modificações nos atributos do objeto referenciado persistem; reatribuir a variável de referência dentro do método não altera a referência externa.

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Simulação de Alocação de Objetos na Memória

```java
public class Ponto2D {
    public double x;
    public double y;

    public void mover(double dx, double dy) {
        this.x += dx;
        this.y += dy;
    }
}

public class TesteMemoria {
    public static void main(String[] args) {
        int a = 10;                     // Alocado na Stack (valor 10)
        Ponto2D p1 = new Ponto2D();      // p1 na Stack aponta para objeto no Heap @0x100
        p1.x = 2.0; p1.y = 3.0;
        
        Ponto2D p2 = p1;                 // p2 na Stack recebe a MESMA referência @0x100
        p2.mover(1.0, 1.0);             // Altera o objeto compartilhado no Heap!
        
        System.out.println("p1.x: " + p1.x); // Imprime 3.0!
    }
}
```

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart LR
    subgraph Stack [Memória Stack (Pilha)]
        V_a["int a = 10"]
        V_p1["p1: Referência @0x100"]
        V_p2["p2: Referência @0x100"]
    end
    subgraph Heap [Memória Heap (Dinâmica)]
        Obj["Objeto Ponto2D (@0x100)
        x = 3.0
        y = 4.0"]
    end
    V_p1 --> Obj
    V_p2 --> Obj
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Comparação de Objetos com `==` vs `.equals()`** | O operador `==` compara os endereços de referência na Stack! Dois objetos com os mesmos atributos retornarão `false` em `p1 == p2` se forem instâncias distintas criadas com `new`. | Sempre use o método `.equals()` para comparar conteúdo de objetos e Strings! |
| **NullPointerException** | Ocorre quando tentamos invocar um método ou acessar um atributo através de uma referência que aponta para `null` (nenhum endereço no Heap). | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Desenhe o diagrama de memória (Stack e Heap) após a execução do código de teste com 3 instâncias de `Ponto2D`.
2. Explique por que passar uma `String` para um método e modificá-la dentro do método não altera a String original (imutabilidade de Strings em Java).

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-00-apresentacao-da-disciplina-configuracao-da-jdk-e-ambiente">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-02-encapsulamento-modificadores-de-acesso-e-construtores">Próxima Aula</a></b></div>
</div>
