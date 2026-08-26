---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital/anotacoes/aula-01-portas-lógicas
title: Aula 01 - Portas Lógicas
created: 2026-08-24
modified: 2026-08-24
encrypted: true
tags:
  - aula
  - engenharia-de-computacao
  - anotacoes-de-quadro
disciplina: Eletrônica Digital
professor: Fabrício Barros Gonçalves
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
    const isAula = /^aula\s+\d+\s*-/.test(name);
    
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
> - **Disciplina:** [[02 - Áreas/Acadêmico/IFF - Engenharia de Computação/6-periodo/eletronica-digital|Eletrônica Digital]]
> - **Docente Responsável:** Fabrício Barros Gonçalves
> - **Tópico Central:** Portas Lógicas
> - **Status das Anotações:** Em andamento

> [!note] 📦 Material Didático & Recursos da Aula
> - 📄 **[Slides da Aula (PDF)](/assets/disciplinas/)**
> - 📖 **[[02 - Áreas/Acadêmico/IFF - Engenharia de Computação/6-periodo/eletronica-digital/short-lecture|Básico da Disciplina]]**

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro & Fundamentação Teórica](#-1-anotações-do-quadro--fundamentação-teórica)
- [🧮 2. Exemplos do Quadro Resolvidos Passo a Passo](#-2-exemplos-do-quadro-resolvidos-passo-a-passo)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes de Prova](#-4-resumo-pessoal--macetes-de-prova)
- [📝 5. Dúvidas & Exercícios Recomendados](#-5-dúvidas--exercícios-recomendados)

---

## 📅 24/08/2026: [Portas Lógicas]

### 📝 Atividades / Cronograma
- [ ] 
### 📐 Revisão [[02 - Áreas/Acadêmico/IFF - Engenharia de Computação/1-periodo/logica-para-computacao/index|Lógica para Computação]] 

### 1. NAO (NOT)

```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*

| A   | S   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---

### 2. E (AND)

```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*

| A   | S   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---

### 3. OU (OR)


```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*

| A   | S   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---

### 4. OU EXCLUSIVO (XOR)

```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*

| A   | S   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---
### 5. NAO E (NAND)

```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*

| A   | S   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |

---
### 6. NAO OU (NOR)

```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*

| A   | S   |
| --- | --- |
| 0   | 1   |
| 1   | 0   |
### 7. Não ou exclusivo (NXOR)

```mermaid
flowchart TD
    A[A] --> B[S]
```

*inserir desenho mermaid*
$$S=\bar{A}$$
*inserir tabela centralizada*


### Min termos

inserir conta tabela e mermaid

### Max termos

inserir conta tabela e mermaid

### Lendo expressões boleanas

***nao necessário para prova***

$$S= (A+B+C) . {B[(A+C) +circular (\bar{B.C})].(\bar{A}.B.\bar{C})}$$
inserir mermaid

$$S= (A+B+C) . {B[(A+C) +circular (\bar{B.C})].(\bar{A}.B.\bar{C})}$$

---
## 🧠 4. Resumo Pessoal & Macetes de Prova

| Tópico        | Princípio Central | Atenção Especial / Pegadinha |
| :------------ | :---------------- | :--------------------------- |
| **mintermos** |                   |                              |
| **maxtermos** |                   |                              |

> [!tip] 💡 Dica de Prova do Professor
> Trabalhar apenas com ***mintermos***
> LogiSim
> 

---

## 📝 5. Dúvidas & Exercícios Recomendados

- [ ] 

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="#">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="../">Hub da Disciplina</a></b></div>
  <div>➡️ <b><a href="#">Próxima Aula</a></b></div>
</div>
