---
publish: false
draft: true
title: "Aula 01: Teorema Fundamental do Cálculo e Integração por Substituição"
created: 2026-08-06
modified: '2026-08-06'
encrypted: true
tags:
  - calculo-i
  - anotaçoes-de-quadro
  - engenharia
cssclasses:
  - page-layout
---

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/templates">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/templates">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/templates/modelocurso/aula-01-introducao-exemplo">Próxima Aula</a></b></div>
</div>

> [!info] 📌 Informações da Aula & Contexto do Quadro
> - **Data da Aula:** 06/08/2026 | **Docente:** Prof. Dr. Gustavo Stênio
> - **Tópico Principal do Quadro:** Teorema Fundamental do Cálculo (Parte 1 e 2) & Técnica da Substituição $u$
> - **Capítulo do Livro-Texto:** Leithold Vol. 1, Cap. 5 (pp. 320-345) / Guidorizzi Vol. 1, Cap. 8
> - **Status das Anotações:** 🟢 Completo (Copiado do Quadro + Revisão Pessoal)

> [!note] 📦 Material Didático e Recursos da Aula
> ### 📑 Material da Aula
> - 📄 **[Slides da Aula — Modelo Branco (PDF)](/assets/biblioteca/matematica/slides-calculo-aula01-branco.pdf)** — *Apresentação em tema claro.*
> - 📄 **[Slides da Aula — Modelo Preto (PDF)](/assets/biblioteca/matematica/slides-calculo-aula01-preto.pdf)** — *Apresentação em tema escuro.*
> - 📝 **[Notas de Aula em PDF (Apostila Institucional)](/assets/biblioteca/matematica/notes-calculo-aula01.pdf)** — *Material de apoio oficial.*
> 
> ### 🌐 Links Externos de Apoio
> - **[Symbolab Integral Calculator](https://www.symbolab.com/)** — *Validador de passos de integração.*
> - **[3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/)** — *Visualização geométrica das integrais.*

## 📋 Sumário Interativo
- [📍 1. Anotações do Quadro: Definições & Teoremas](#-1-anotações-do-quadro-definições--teoremas)
- [🧮 2. Exemplo do Quadro Resolvido Passo a Passo](#-2-exemplo-do-quadro-resolvido-passo-a-passo)
- [📊 3. Esquema Visual & Fluxograma (Mermaid)](#-3-esquema-visual--fluxograma-mermaid)
- [🧠 4. Resumo Pessoal & Macetes do Professor](#-4-resumo-pessoal--macetes-do-professor)
- [📝 5. Dúvidas & Exercícios Recomendados para Casa](#-5-dúvidas--exercícios-recomendados-para-casa)
- [🔗 Aulas Correlatas & Conexões](#-aulas-correlatas--conexões)

---

## 📌 1. Anotações do Quadro: Definições & Teoremas

### 📐 Teorema Fundamental do Cálculo (Parte 1)
Se $f$ for contínua em $[a, b]$, então a função $F(x)$ definida por:
$$F(x) = \int_{a}^{x} f(t) \, dt \quad 	ext{para } x \in [a, b]$$
é contínua em $[a, b]$, derivável em $(a, b)$, e sua derivada é dada por:
$$F'(x) = rac{d}{dx} \left( \int_{a}^{x} f(t) \, dt 
ight) = f(x)$$

### 📐 Teorema Fundamental do Cálculo (Parte 2)
Se $f$ for contínua em $[a, b]$ e $F$ for qualquer primitiva de $f$ em $[a, b]$ (isto é, $F'(x) = f(x)$), então:
$$\int_{a}^{b} f(x) \, dx = F(b) - F(a) = \left[ F(x) 
ight]_{a}^{b}$$

---

## 🧮 2. Exemplo do Quadro Resolvido Passo a Passo

### ✏️ Problema Copiado do Quadro
Calcule a integral definida:
$$I = \int_{0}^{2} x \cdot \sqrt{x^2 + 1} \, dx$$

#### 🔹 Passo 1: Escolha da Variável de Substituição $u$
Escolhemos a expressão interna do radical para ser $u$:
$$u = x^2 + 1 \implies rac{du}{dx} = 2x \implies du = 2x \, dx \implies x \, dx = rac{du}{2}$$

#### 🔹 Passo 2: Mudança dos Limites de Integração
- Quando $x = 0 \implies u = (0)^2 + 1 = 1$
- Quando $x = 2 \implies u = (2)^2 + 1 = 5$

#### 🔹 Passo 3: Substituição e Integração
$$\int_{0}^{2} x \sqrt{x^2 + 1} \, dx = \int_{1}^{5} \sqrt{u} \cdot rac{du}{2} = rac{1}{2} \int_{1}^{5} u^{1/2} \, du$$
$$rac{1}{2} \left[ rac{u^{3/2}}{3/2} 
ight]_{1}^{5} = rac{1}{2} \cdot rac{2}{3} \left[ u^{3/2} 
ight]_{1}^{5} = rac{1}{3} \left( 5^{3/2} - 1^{3/2} 
ight) = rac{5\sqrt{5} - 1}{3}$$

> [!tip] 💡 Macete do Professor (Dica do Quadro)
> Sempre que alterar a variável para $u$, recalcule imediatamente os **limites de integração** para não precisar voltar para a variável $x$ no final!

> [!warning] ⚠️ Erro Comum em Provas (Pegadinha)
> Esquecer de multiplicar o fator $rac{1}{2}$ decorrente do $du = 2x \, dx$. Sempre isole o termo $x \, dx$ antes de substituir!

---

## 📊 3. Esquema Visual & Fluxograma (Mermaid)

Representação esquemática do algoritmo de decisão desenhado no quadro para escolher o método de integração:

```mermaid
flowchart TD
    A[Integral Identificada: ∫ f(x) dx] --> B{Forma u' * g(u)?}
    B -- Sim --> C[Aplicar Substituição u = g(x)]
    B -- Não --> D{Produto de Polinômio e Exponencial/Trig?}
    D -- Sim --> E[Aplicar Integração por Partes: ∫ u dv]
    D -- Não --> F[Verificar Substituição Trigonométrica ou Frações Parciais]
    C --> G[Recalcular Limites de Integração se for Definida]
    E --> H[Avaliar Limites e Simplificar]
    G --> I[Resultado Final]
    F --> I
```

---

## 🧠 4. Resumo Pessoal & Macetes do Professor

| Conceito do Quadro | Aplicação Prática | Atenção Especial |
| :--- | :--- | :--- |
| **TFC Parte 1** | Derivar integrais com limite variável | Substitua $t$ por $x$ diretamente se limite for $x$ |
| **TFC Parte 2** | Calcular a área sob a curva | Encontrar a antiderivada $F(x)$ primeiro |
| **Substituição $u$** | Simplificar integrandos com composta | $du$ deve cobrir o restante da expressão original |

---

## 📝 5. Dúvidas & Exercícios Recomendados para Casa

### ❓ Minhas Dúvidas da Aula
- [ ] Rever a demonstração da Regra da Cadeia aplicada ao TFC Parte 1 quando o limite superior é uma função $g(x)$.

### 📝 Lista de Exercícios Passada no Quadro
- [ ] Leithold Cap. 5.3: Exercícios 1, 5, 12, 18, 25.
- [ ] Leithold Cap. 5.4: Exercícios 3, 7, 15, 22.

---

## 🔗 Aulas Correlatas & Conexões
- 🔗 **[[nota-02|Aula 02: Aplicações Práticas e Resolução de Problemas]]** — *Próxima aula: Áreas entre curvas e volume de sólidos de revolução.*

<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="/templates">Aula Anterior</a></b></div>
  <div>🏠 <b><a href="/templates">Anotações da Disciplina</a></b></div>
  <div>➡️ <b><a href="/templates/modelocurso/aula-01-introducao-exemplo">Próxima Aula</a></b></div>
</div>
