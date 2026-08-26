---
publish: true
permalink: pt-br/resource/engenharia-de-computação/6-periodo
title: "6º Período"
created: 2026-07-21
modified: 2026-08-22
---

> [!info] 🎓 Visão Geral e Carga Horária do Período
> - **Carga Horária Total do Bloco:** `500h` (340h teóricas + 160h práticas / projetos)
> - **Semestre Letivo:** `2026-2` (24 de Agosto de 2026 a 18 de Dezembro de 2026 · 20 Semanas / 100 Dias Letivos)
> - **Resumo Pedagógico:** Análise e engenharia orientada a objetos, bancos de dados relacionais e avançados, circuitos lógicos digitais, teoria e construção de compiladores, telecomunicações e redes físicas, reflexão epistemológica e viabilidade técnica/econômica de projetos de engenharia.

```dataviewjs
const allPages = dv.pages('"02 - Áreas/Acadêmico/IFF - Engenharia de Computação/6-periodo"');
const disciplines = [
    { name: "Análise de Software OO", path: "analise-de-software-orientada-a-objetos" },
    { name: "Banco de Dados", path: "banco-de-dados" },
    { name: "Compiladores", path: "compiladores" },
    { name: "Comunicação de Dados", path: "comunicacao-de-dados" },
    { name: "Eletrônica Digital", path: "eletronica-digital" },
    { name: "Filosofia da Ciência e Tecnologia", path: "filosofia-da-ciencia-e-tecnologia" },
    { name: "Gestão de Projetos", path: "gestao-de-projetos" },
    { name: "Programação Orientada a Objetos I", path: "programacao-orientada-a-objetos-i" }
];

let html = `<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin: 1.5rem 0;">`;

disciplines.forEach(d => {
    const dPages = allPages.filter(p => p.file.folder.includes(d.path));
    
    const completedAulas = dPages.filter(p => {
        const folder = (p.file.folder || "").toLowerCase();
        const path = (p.file.path || "").toLowerCase();
        const name = (p.file.name || "").toLowerCase();
        
        const isEsboco = folder.includes("esboço") || folder.includes("esboco") || path.includes("esboço") || path.includes("esboco") || folder.includes("draft");
        const isAula = /^aula[\s_-]+\d+/i.test(name);
        
        return isAula && !isEsboco;
    });

    const completed = completedAulas.length;
    const total = 20;
    const pct = Math.min(100, Math.round((completed / total) * 100));
    
    html += `
    <div style="padding: 1rem; background: var(--background-secondary, #f4f4f5); border-radius: 8px; border: 1px solid var(--border-color, #e4e4e7);">
      <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 0.4rem; color: var(--text-normal, #18181b);">${d.name}</div>
      <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: var(--text-muted, #71717a); margin-bottom: 0.3rem;">
        <span>${completed} / ${total} Aulas</span>
        <span>${pct}%</span>
      </div>
      <div style="width: 100%; height: 6px; background-color: var(--background-modifier-border, #e4e4e7); border-radius: 3px; overflow: hidden;">
        <div style="width: ${pct}%; height: 100%; background: linear-gradient(90deg, #2563eb, #3b82f6); border-radius: 3px;"></div>
      </div>
    </div>`;
});

html += `</div>`;
dv.el("div", html);
```

> [!note] 📚 Grade Curricular e Disciplinas Integrantes
> - 📘 **[Análise de Software Orientada a Objetos](/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos)** (`60h` · Prof. Pablo · Quarta 13:40–16:30)
> - 📘 **[Filosofia da Ciência e Tecnologia](/pt-br/resource/engenharia-de-computação/6-periodo/filosofia-da-ciencia-e-tecnologia)** (`60h` · Prof. Dr. Rafel Tardin · Quarta 19:20–22:00)
> - 📘 **[Banco de Dados](/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados)** (`60h` · Prof. Pablo · Terça 13:40–16:30)
> - 📘 **[Programação Orientada a Objetos I](/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i)** (`60h` · Prof. Me. Andeson Veiga · Quarta 16:40–19:20)
> - 📘 **[Eletrônica Digital](/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital)** (`60h` · Prof. Dr. Fabrício Barros Gonçalves · Segunda 16:40–19:20)
> - 📘 **[Comunicação de Dados](/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados)** (`60h` · Prof. Me. Luiz Carlos Ferreira Garcez· Terça 16:40–19:20)
> - 📘 **[Compiladores](/pt-br/resource/engenharia-de-computação/6-periodo/compiladores)** (`60h` · Prof.  Dr. Fabrício Barros Gonçalves · Sexta 13:40–16:30)

---

## 🕒 Quadro de Horários Semanal (2026-2)

<div style="display: flex; gap: 12px; margin-bottom: 1.5rem; flex-wrap: wrap;" class="schedule-actions-bar">
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/cronograma-6-periodo.json" download="cronograma-6-periodo.json" class="btn-action" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; background: #2563eb; color: #ffffff; text-decoration: none; border-radius: 8px; font-weight: 600; font-size: 0.9rem; box-shadow: 0 2px 4px rgba(37,99,235,0.2);">
    📥 Exportar Cronograma (JSON)
  </a>
  <button onclick="window.print()" class="btn-action" style="display: inline-flex; align-items: center; gap: 8px; padding: 10px 18px; background: #059669; color: #ffffff; border: none; border-radius: 8px; font-weight: 600; font-size: 0.9rem; cursor: pointer; box-shadow: 0 2px 4px rgba(5,150,105,0.2);">
    🖨️ Imprimir / Salvar em PDF
  </a>
</div>

<style>
@media print {
  body { background: white !important; color: black !important; font-size: 10pt; }
  .schedule-actions-bar, nav, header, footer, .sidebar, .explorer, .toc { display: none !important; }
  .schedule-table-wrapper { width: 100% !important; margin: 0 !important; }
}
.schedule-badge {
  display: block;
  padding: 4px 6px;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 600;
  text-decoration: none;
  line-height: 1.2;
}
.badge-bd { background: #e0f2fe; color: #0369a1; border-left: 3px solid #0284c7; }
.badge-asoo { background: #fef3c7; color: #92400e; border-left: 3px solid #f59e0b; }
.badge-comp { background: #f3e8ff; color: #6b21a8; border-left: 3px solid #9333ea; }
.badge-ed { background: #dcfce7; color: #166534; border-left: 3px solid #16a34a; }
.badge-cd { background: #ffedd5; color: #9a3412; border-left: 3px solid #ea580c; }
.badge-poo { background: #fee2e2; color: #991b1b; border-left: 3px solid #dc2626; }
.badge-gp { background: #e0e7ff; color: #3730a3; border-left: 3px solid #4f46e5; }
.badge-filo { background: #f1f5f9; color: #334155; border-left: 3px solid #64748b; }
.intervalo-row { background: var(--light, #f8fafc); color: var(--gray, #94a3b8); font-size: 0.7rem; text-align: center; font-style: italic; }
</style>

| ⏰ Horário       | Segunda (SEG)                                                                                                                                                                                      | Terça (TER)                                                                                                                                                                                              | Quarta (QUA)                                                                                                                                                                                                  | Quinta (QUI)                                                                                                                                                                           | Sexta (SEX)                                                                                                                                                                              |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **13:40–14:30** | —                                                                                                                                                                                                  | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados" class="schedule-badge badge-bd"><b>CSECBJI.44</b><br>Banco de Dados<br>Prof. Pablo</a>                                       | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos" class="schedule-badge badge-asoo"><b>CSECBJI.42</b><br>Análise de Software OO<br>Prof. Pablo</a>         | —                                                                                                                                                                                      | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores" class="schedule-badge badge-comp"><b>CSECBJI.48</b><br>Compiladores<br>Prof. Dr. Fabrício Barros Gonçalves</a> |
| **14:30–14:50** | *Intervalo (20m)*                                                                                                                                                                                  | *Intervalo (20m)*                                                                                                                                                                                        | *Intervalo (20m)*                                                                                                                                                                                             | *Intervalo (20m)*                                                                                                                                                                      | *Intervalo (20m)*                                                                                                                                                                        |
| **14:50–15:40** | —                                                                                                                                                                                                  | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados" class="schedule-badge badge-bd"><b>CSECBJI.44</b><br>Banco de Dados<br>Prof. Pablo</a>                                       | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos" class="schedule-badge badge-asoo"><b>CSECBJI.42</b><br>Análise de Software OO<br>Prof. Pablo</a>         | —                                                                                                                                                                                      | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores" class="schedule-badge badge-comp"><b>CSECBJI.48</b><br>Compiladores<br>Prof. Dr. Fabrício Barros Gonçalves</a> |
| **15:40–16:30** | —                                                                                                                                                                                                  | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados" class="schedule-badge badge-bd"><b>CSECBJI.44</b><br>Banco de Dados<br>Prof. Pablo</a>                                       | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos" class="schedule-badge badge-asoo"><b>CSECBJI.42</b><br>Análise de Software OO<br>Prof. Pablo</a>         | —                                                                                                                                                                                      | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores" class="schedule-badge badge-comp"><b>CSECBJI.48</b><br>Compiladores<br>Prof. Dr. Fabrício Barros Gonçalves</a> |
| **16:30–16:40** | *Intervalo (10m)*                                                                                                                                                                                  | *Intervalo (10m)*                                                                                                                                                                                        | *Intervalo (10m)*                                                                                                                                                                                             | *Intervalo (10m)*                                                                                                                                                                      | *Intervalo (10m)*                                                                                                                                                                        |
| **16:40–17:30** | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital" class="schedule-badge badge-ed"><b>CSECBJI.46</b><br>Eletrônica Digital<br>Prof. Dr. Fabrício Barros Gonçalves</a> | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados" class="schedule-badge badge-cd"><b>CSECBJI.47</b><br>Comunicação de Dados<br>Prof. Me. Luiz Carlos Ferreira Garcez</a> | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i" class="schedule-badge badge-poo"><b>CSECBJI.45</b><br>Programação OO I<br>Prof. Me. Anderson Veiga</a>         | <!-- <a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos" class="schedule-badge badge-gp"><b>CSECBJI.49</b><br>Gestão de Projetos<br>Prof. [Nome]</a> --> — | —                                                                                                                                                                                        |
| **17:30–18:20** | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital" class="schedule-badge badge-ed"><b>CSECBJI.46</b><br>Eletrônica Digital<br>Prof. Dr. Fabrício Barros Gonçalves</a> | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados" class="schedule-badge badge-cd"><b>CSECBJI.47</b><br>Comunicação de Dados<br>Prof. Me. Luiz Carlos Ferreira Garcez</a> | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i" class="schedule-badge badge-poo"><b>CSECBJI.45</b><br>Programação OO I<br>Prof. Me. Anderson Veiga</a>         | <!-- <a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos" class="schedule-badge badge-gp"><b>CSECBJI.49</b><br>Gestão de Projetos<br>Prof. [Nome]</a> --> — | —                                                                                                                                                                                        |
| **18:20–18:30** | *Intervalo (10m)*                                                                                                                                                                                  | *Intervalo (10m)*                                                                                                                                                                                        | *Intervalo (10m)*                                                                                                                                                                                             | *Intervalo (10m)*                                                                                                                                                                      | *Intervalo (10m)*                                                                                                                                                                        |
| **18:30–19:20** | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital" class="schedule-badge badge-ed"><b>CSECBJI.46</b><br>Eletrônica Digital<br>Prof. Dr. Fabrício Barros Gonçalves</a> | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados" class="schedule-badge badge-cd"><b>CSECBJI.47</b><br>Comunicação de Dados<br>Prof. Me. Luiz Carlos Ferreira Garcez</a> | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i" class="schedule-badge badge-poo"><b>CSECBJI.45</b><br>Programação OO I<br>Prof. Me. Anderson Veiga</a>         | <!-- <a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos" class="schedule-badge badge-gp"><b>CSECBJI.49</b><br>Gestão de Projetos<br>Prof. [Nome]</a> --> — | —                                                                                                                                                                                        |
| **19:20–20:10** | —                                                                                                                                                                                                  | —                                                                                                                                                                                                        | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/filosofia-da-ciencia-e-tecnologia" class="schedule-badge badge-filo"><b>CSECBJI.43</b><br>Filosofia Ciência & Tec.<br>Prof. Dr. Rafael Tardin</a> | <!-- <a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos" class="schedule-badge badge-gp"><b>CSECBJI.49</b><br>Gestão de Projetos<br>Prof. [Nome]</a> --> — | —                                                                                                                                                                                        |
| **20:10–20:20** | *Intervalo (10m)*                                                                                                                                                                                  | *Intervalo (10m)*                                                                                                                                                                                        | *Intervalo (10m)*                                                                                                                                                                                             | *Intervalo (10m)*                                                                                                                                                                      | *Intervalo (10m)*                                                                                                                                                                        |
| **20:20–21:10** | —                                                                                                                                                                                                  | —                                                                                                                                                                                                        | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/filosofia-da-ciencia-e-tecnologia" class="schedule-badge badge-filo"><b>CSECBJI.43</b><br>Filosofia Ciência & Tec.<br>Prof. Dr. Rafael Tardin</a> | —                                                                                                                                                                                      | —                                                                                                                                                                                        |
| **21:10–22:00** | —                                                                                                                                                                                                  | —                                                                                                                                                                                                        | <a href="/pt-br/resource/engenharia-de-computação/6-periodo/filosofia-da-ciencia-e-tecnologia" class="schedule-badge badge-filo"><b>CSECBJI.43</b><br>Filosofia Ciência & Tec.<br>Prof. Dr. Rafael Tardin</a> | —                                                                                                                                                                                      | —                                                                                                                                                                                        |

---

## 🎨 Carrossel de Disciplinas do Período

Navegue interativamente pelas disciplinas deste bloco letivo:

<div class="media-carousel">
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/analise-de-software-orientada-a-objetos" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Análise de Software Orientada a Objetos" />
    <div class="slide-caption">Análise de Software OO</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/filosofia-da-ciencia-e-tecnologia" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Filosofia da Ciência e Tecnologia" />
    <div class="slide-caption">Filosofia da Ciência e Tecnologia</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/banco-de-dados" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Banco de Dados" />
    <div class="slide-caption">Banco de Dados</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/programacao-orientada-a-objetos-i" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Programação Orientada a Objetos I" />
    <div class="slide-caption">POO I</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/eletronica-digital" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Eletrônica Digital" />
    <div class="slide-caption">Eletrônica Digital</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/comunicacao-de-dados" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Comunicação de Dados" />
    <div class="slide-caption">Comunicação de Dados</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/compiladores" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Compiladores" />
    <div class="slide-caption">Compiladores</div>
  </a>
  <a href="/pt-br/resource/engenharia-de-computação/6-periodo/gestao-de-projetos" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Gestão de Projetos" />
    <div class="slide-caption">Gestão de Projetos</div>
  </a>
</div>
