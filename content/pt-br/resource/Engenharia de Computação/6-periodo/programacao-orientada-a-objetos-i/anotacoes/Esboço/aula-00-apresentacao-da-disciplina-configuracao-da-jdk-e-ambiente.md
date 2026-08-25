---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-00-apresentacao-da-disciplina-configuracao-da-jdk-e-ambiente
title: "Aula 00: Apresentação da Disciplina, Configuração da JDK e Ambiente — Programação Orientada a Objetos I"
created: 2026-08-26T14:00:00-03:00
modified: 2026-08-23T14:00:00-03:00
encrypted: true
tags:
  - aula
  - aula-00
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: "Programação Orientada a Objetos I"
professor: "Sérgio / Bruno"
conteudo: "Apresentação do curso, fundamentos da JVM/Bytecode, instalação de JDK/IDE e convenções de código."
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <span style="color: gray;">Primeira Aula</span></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-01-classes-instanciacao-e-tipos-por-referencia-vs-valor">Próxima Aula</a></b></div>
</div>

> [!info] 📅 Informações da Aula
> - **Disciplina:** Programação Orientada a Objetos I (CSECBJI.45)
> - **Professor:** Sérgio / Bruno
> - **Data Realizada:** 26/08/2026
> - **Tópico Principal:** Apresentação da Disciplina, Configuração da JDK e Ambiente
> - **Status:** Concluída e Revisada

> [!note] 📂 Material Complementar & Slides
> - 📄 **Slides Oficiais:** [[slide-00-programacao-orientada-a-objetos-i|Acessar Apresentação em PDF]]
> - 🎥 **Short Lecture / Gravação:** [[video-00-programacao-orientada-a-objetos-i|Assistir Síntese da Aula (Vídeo)]]

---

### 📑 Resumo das Seções
- [📌 1. Anotações do Quadro: Apresentação da Disciplina, Configuração da JDK e Ambiente](#-anotações-do-quadro-apresentação-da-disciplina,-configuração-da-jdk-e-ambiente)
- [🧮 2. Formulação & Exemplo Prático Resolvido](#-formulação--exemplo-prático-resolvido)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-dúvidas--exercícios-recomendados-para-casa)

---

## 📌 Anotações do Quadro: Apresentação da Disciplina, Configuração da JDK e Ambiente

### 1.1 O Ecossistema Java e a Máquina Virtual (JVM)
A plataforma Java baseia-se no princípio *Write Once, Run Anywhere* (WORA):
- **Código Fonte (`.java`):** Texto escrito pelo programador em alto nível.
- **Compilador (`javac`):** Compila o código fonte em um formato intermediário binário e independente de hardware chamado **Bytecode** (`.class`).
- **Máquina Virtual Java (JVM):** Traduz o Bytecode em instruções de máquina nativas da CPU hospedeira através de interpretação e compilação JIT (*Just-In-Time*).
- **JDK vs JRE:**
  - **JRE (*Java Runtime Environment*):** Contém a JVM e as bibliotecas essenciais para executar programas Java.
  - **JDK (*Java Development Kit*):** Contém a JRE mais os utilitários de desenvolvimento (`javac`, `jar`, `javadoc`, `jdb`).

### 1.2 Instalação e Configuração do Ambiente
- Instalação do OpenJDK 21 LTS e configuração das variáveis de ambiente:
  - `JAVA_HOME=/usr/lib/jvm/java-21-openjdk`
  - `PATH=$JAVA_HOME/bin:$PATH`
- Convenções Oficiais de Nomenclatura (Java Code Conventions):
  - Classes e Interfaces: `PascalCase` (ex: `ContaBancaria`, `RepositorioUsuario`).
  - Métodos e Variáveis: `camelCase` (ex: `calcularSalarioLiquido()`, `saldoDisponivel`).
  - Constantes: `UPPER_SNAKE_CASE` (ex: `TAXA_JUROS_PADRAO`).
  - Pacotes: letras minúsculas (ex: `br.edu.iff.engcomp.sistema`).

---

## 🧮 Formulação & Exemplo Prático Resolvido

### ✏️ Primeiro Programa em Java e Compilação Manual no Terminal

```java
package br.edu.iff.engcomp.aula00;

public class OlaMundo {
    public static void main(String[] args) {
        System.out.println("=== Bem-vindo a POO I - Engenharia de Computação (IFF) ===");
        System.out.printf("Versão do Java: %s\n", System.getProperty("java.version"));
    }
}
```

**Comandos de Terminal:**
```bash
# Compilação gerando arquivo .class
javac -d bin src/br/edu/iff/engcomp/aula00/OlaMundo.java

# Execução na JVM
java -cp bin br.edu.iff.engcomp.aula00.OlaMundo
```

---

## 📊 Esquema Visual & Fluxograma (Mermaid)

```mermaid
flowchart LR
    Src[OlaMundo.java] -->|javac| Byte[OlaMundo.class: Bytecode]
    Byte --> JVM[Java Virtual Machine: JVM]
    JVM -->|JIT Compiler| Nat[Código Máquina Nativo: x86 / ARM]
```

---

## 🧠 Resumo Pessoal & Macetes do Professor

| Conceito-Chave | *Takeaway* do Professor | Dicas de Prova / Atenção |
| :--- | :--- | :--- |
| **Assinatura do Método main** | `public static void main(String[] args)` é o único ponto de entrada reconhecido pela JVM para iniciar a aplicação. | Qualquer alteração na assinatura impedirá a execução do programa. |
| **Nome do Arquivo vs Nome da Classe Pública** | Um arquivo `.java` só pode conter no máximo UMA classe pública (`public class`), e o nome do arquivo DEVE ser rigorosamente idêntico ao nome dessa classe (respeitando maiúsculas e minúsculas). | Aplicação prática direta |

---

## 📝 Dúvidas & Exercícios Recomendados para Casa

1. Configure o OpenJDK 21 em seu ambiente e verifique a instalação executando `java -version`.
2. Escreva e execute um programa Java que imprima todas as propriedades do sistema operacional através de `System.getProperties()`.

---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <span style="color: gray;">Primeira Aula</span></div>
  <div>🏠 <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-01-classes-instanciacao-e-tipos-por-referencia-vs-valor">Próxima Aula</a></b></div>
</div>
