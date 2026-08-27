---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i/anotacoes/aula-01-introdução
title: "Aula 01 - Introdução"
created: '2026-08-26'
modified: '2026-08-26'
encrypted: true
tags:
  - aula
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: 
professor: 
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>

```dataviewjs
const currentPath = dv.current()?.file?.path || "";
const parts = currentPath.split("/");
const periodIndex = parts.findIndex(p => p.toLowerCase().includes("periodo") || p.toLowerCase().includes("período"));
const disciplineFolder = periodIndex !== -1 && parts.length > periodIndex + 1 ? parts[periodIndex + 1] : "";

const allPages = dv.pages();
const completedAulas = allPages.filter(p => {
    const path = (p.file?.path || "").toLowerCase();
    const name = (p.file?.name || "").toLowerCase();
    
    const isInDiscipline = disciplineFolder ? path.includes(disciplineFolder.toLowerCase()) : true;
    const isEsboco = path.includes("esboço") || path.includes("esboco") || path.includes("draft");
    const isAula = /^aula[\s_-]+\d+/i.test(name);
    
    return isInDiscipline && isAula && !isEsboco;
});

const totalAulas = 20;
const completedCount = completedAulas.length;
const percentage = Math.min(100, Math.round((completedCount / totalAulas) * 100));

dv.container.innerHTML = `
<div style="margin: 1.5rem 0; padding: 1.2rem; background: var(--background-secondary, #f4f4f5); border-radius: 8px; border: 1px solid var(--border-color, #e4e4e7); box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem;">
    <span style="font-weight: 700; font-size: 0.95rem; color: var(--text-normal, #18181b); display: inline-flex; align-items: center; gap: 6px;">
      📖 Progresso da Disciplina
    </span>
    <span style="font-size: 0.85rem; font-weight: 700; color: var(--text-muted, #71717a);">
      ${completedCount} / ${totalAulas} Aulas (${percentage}%)
    </span>
  </div>
  <div style="width: 100%; height: 12px; background-color: var(--background-modifier-border, #e4e4e7); border-radius: 6px; overflow: hidden;">
    <div style="width: ${percentage}%; height: 100%; background: linear-gradient(90deg, #10b981, #059669); border-radius: 6px; transition: width 0.3s ease;"></div>
  </div>
</div>`;
```

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Tópico Central:** Introdução a POO
> - **Status das Anotações:** 🟡 Planejando | 🟠 Em Andamento | 🟢 Concluído

> [!note] 📦 Material Didático & Recursos da Aula
> - 📄 **[[Aula 01 - Introdução]]**
> - 📖 **[Short Lecture da Disciplina](../short-lecture)**

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
8. 

##### Código Java

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
- [ ] Implementar classe Lâmpada;
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


---

## 🧠 Resumo

| Tópico | Princípio Central | Atenção Especial / Pegadinha |
| :--- | :--- | :--- |
| | | |

> [!tip] 💡 Dica de Prova do Professor
> 

---

## 📝 Dúvida

- [ ] 

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>
