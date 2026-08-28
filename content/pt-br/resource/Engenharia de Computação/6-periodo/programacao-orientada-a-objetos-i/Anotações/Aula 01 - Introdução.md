---
publish: true
title: Aula 01 - Introdução
created: 2026-08-26 14:49
modified: 2026-08-27 21:54
encrypted: true
tags:
  - aula
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: Programação Orientada a Objetos I
professor: Anderson Veiga
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>

| Aula / Conteúdo | Data | Docente |
| :--- | :---: | :--- |
| [[02\|02]] | 27/08/2026 | — |
| [[Aula 01 - Introdução\|Aula 01 - Introdução]] | 26/08/2026 | Anderson Veiga |

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Tópico Central:** Introdução a POO
> - **Status das Anotações:** 
> - [ ] 🟡 Planejando
> - [ ] 🟠 Em Andamento
> - [ ] 🟢 Concluído

> [!note] 📦 Material Didático & Recursos da Aula
> - 📄 **[[Aula 01 - Introdução]]**
> - 📖 **[[../short-lecture|Short Lecture da Disciplina]]**

## 📋 Sumário Interativo
- [📍 Anotações](#-anotações)
- [🧠 Resumo](#-resumo)
- [📝 Dúvida](#-dúvida)

---

## 📍 Anotações

#### 26/08
1. Introdução:
2. Descrevendo Objetos
	1. Conceito de Abstração
![[Introdução à Programação Orientada a Objetos.pdf#page=2&rect=160,68,571,298|Introdução à Programação Orientada a Objetos, p.2]]
3. Estrutura Formal
	1. Atributos
	2. Operações ou Métodos (Ações: Funções)
4. Objetos
	1. Mesmas caracteristicas (atributos);
	2. Valores diferentes (Estado interno diferente);
	3. Mesmas Operações = Mesmo tipo = Mesma classe
5. Classe
	1. Blueprint
![[Introdução à Programação Orientada a Objetos.pdf#page=7&rect=43,16,684,252|Introdução à Programação Orientada a Objetos, p.7]]
6. Paradigma:
> [!PDF|important] [[Introdução à Programação Orientada a Objetos.pdf#page=10&selection=2,0,4,38&color=important|Introdução à Programação Orientada a Objetos, p.10]]
> > É um paradigma de programação que organiza o software em torno de objetos, que representam entidades do mundo real ou conceitual, agrupando dados e comportamentos dentro de uma entidade.
> 
> 
7. Linguagem: JAVA
![[Introdução à Programação Orientada a Objetos.pdf#page=12&rect=110,113,606,230&color=important|Introdução à Programação Orientada a Objetos, p.12]]
8. Compilar e Executar
	1. javac
	2. java
9. 

##### Código Java

Estrutura base
Classe.java
```
class Carro {
	String fabricante;
	String modelo;
	int anoFabricacao;
	double velocidade;
	
	void acelerar(){
		velocidade += 10;
		System.out.println("Acelerando...");
	}

	void frear() {
		velocidade -= 10;
		System.out.println("Freando...");
	}
}
```
App.java

```
public class App {
	public static void main () {
		Carro carro1 = new Carro(); 
		Carro carro2 = new Carro();
		
		carro1.modelo = "F40"; 
		carro2.modelo = "Countach"; 
		
		carro1.acelerar(); 
		carro1.acelerar(); 
		carro2.acelerar(); 
		
		System.out.println(carro1.velocidade);
		System.out.println(carro2.velocidade);
	}	
}
```

Blueprint: 
```
class Carro {
	String fabricante;
	String modelo;
	int anoFabricacao;
	double velocidade;
	
	void acelerar(){
		velocidade += 10;
		System.out.println("Acelerando...");
	}

	void frear() {
		velocidade -= 10;
		System.out.println("Freando...");
	}
}
```

New = construtor, carro = “ponteiro”


> [!PDF|important] [[Introdução à Programação Orientada a Objetos.pdf#page=22&selection=0,0,0,34&color=important|Introdução à Programação Orientada a Objetos, p.22]]
> > A classe define, o objeto possui.

#### Tarefa Prática:
- [x] Implementar classe Lâmpada;
- [ ] Implementar classe Conta Bancária;

Tarefa 1:
```
class Lampada {
	String estado;
	String cor;
	
	void acender(){
		System.out.println("Acendendo...");
		estado = "Acesa";
	}
	
	void apagar(){
		System.out.println("Apagando...");
		estado = "Apagada";
	}
	
	void alternar(){

	}
}
```

Tarefa 2:
```
class Conta {
	String numero;
	String nome_titular;
	double saldo;
	
	void sacar(){
		System.out.println("Acendendo...");
		estado = "Acesa";
	}
	
	void depositar(){
		System.out.println("Apagando...");
		estado = "Apagada";
	}
	
	void transferir(){

	}
}
```

---

## 🧠 Resumo

| Tópico    | Princípio Central | Atenção Especial / Pegadinha |
| :-------- | :---------------- | :--------------------------- |
| Classe    |                   |                              |
| Objeto    |                   |                              |
| Atributos |                   |                              |

> [!tip] 💡 Dica de Prova do Professor
> 

---

## 📝 Dúvida

- [ ] Como pede informação ao usuário?

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>
