---
publish: false
title: Aula 01 - Introdução
created: 2026-08-26 14:49
modified: 2026-09-22 22:41
encrypted: true
tags:
- aula
- engenharia-de-computacao
cssclasses:
- page-layout
icon: lucide-book-open
---

<div class="progress-bar-container" style="background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 8px; padding: 12px 16px; margin: 1.5rem 0;">
  <div style="font-weight: 600; font-size: 0.85rem; color: var(--dark, #334155); margin-bottom: 6px;">Progresso das Aulas da Disciplina</div>
  <div style="background: var(--lightgray, #e2e8f0); border-radius: 4px; overflow: hidden; height: 8px;">
    <div style="background: var(--secondary, #6d28d9); width: 10%; height: 100%;"></div>
  </div>
</div>

# Aula 01 - Introdução

> [!info]- Informações & Checklist da Aula
> - **Docente:** Anderson Veiga
> - **Data da Aula:** 26/08/2026
> - **Status de Revisão:**
>   - [x] Anotações em sala de aula
>   - [x] Revisão e fixação de conceitos
>   - [x] Resolução de exercícios recomendados
>   - [ ] Destilação para [[07-permanente/notas-permanentes|Notas Permanentes]]

---

## Anotações do Quadro & Conteúdo

### Paradigma Orientado a Objetos
1. Introdução:
2. Descrevendo Objetos
	1. Conceito de Abstração
> 📖 *[Referência: Introdução à Programação Orientada a Objetos, p.2]*
3. Estrutura Formal
	1. Atributos
	2. Operações ou Métodos (Ações: Funções)
4. Objetos
	1. Mesmas caracteristicas (atributos);
	2. Valores diferentes (Estado interno diferente);
	3. Mesmas Operações = Mesmo tipo = Mesma classe
5. Classe
	1. Blueprint
> 📖 *[Referência: Introdução à Programação Orientada a Objetos, p.7]*
6. Paradigma:
> [!important] **Introdução à Programação Orientada a Objetos, p.10**
> > É um paradigma de programação que organiza o software em torno de objetos, que representam entidades do mundo real ou conceitual, agrupando dados e comportamentos dentro de uma entidade.
> 
> 
7. Linguagem: JAVA
> 📖 *[Referência: Introdução à Programação Orientada a Objetos, p.12]*
8. Compilar e Executar
	1. javac
	2. java
9. 

### Código Java

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


> [!important] **Introdução à Programação Orientada a Objetos, p.22**
> > A classe define, o objeto possui.

### Tarefa Prática:
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


---

## Esquemas & Anotações Visuais (excalidraw)
<!-- No iPad: insira desenhos com 'excalidraw: Create and embed new drawing' para desenhar com Apple Pencil -->

---

> [!question]- Dúvidas & Exercícios Recomendados
> - [ ] Como pede informação ao usuário?
