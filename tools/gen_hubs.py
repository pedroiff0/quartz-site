#!/usr/bin/env python3
"""Gera as notas hub (index.md) de content/<idioma>/projects e subpastas, listando as páginas filhas.

Uso: python3 tools/gen_hubs.py   (rode depois do sync do cofre)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "content"
L = {
    "pt-br": {"projects": ("Projetos", "Ferramentas, aplicações e material didático que construo fora da pesquisa."), "personal": ("Pessoais", "Projetos pessoais e ferramentas de uso próprio."),
              "academic": ("Acadêmicos", "Projetos ligados ao curso e à pesquisa."), "professional": ("Profissionais", "Templates e projetos de uso profissional."),
              "col": ("Projeto", "Descrição"), "sub": ("Categoria", "Projetos"), "vazio": "Ainda sem projetos publicados."},
    "en": {"projects": ("Projects", "Tools, applications and teaching material built outside research."), "personal": ("Personal", "Personal projects and tools for my own use."),
           "academic": ("Academic", "Projects tied to the degree and to research."), "professional": ("Professional", "Templates and projects for professional use."),
           "col": ("Project", "Description"), "sub": ("Category", "Projects"), "vazio": "No published projects yet."},
    "es": {"projects": ("Proyectos", "Herramientas, aplicaciones y material didáctico fuera de la investigación."), "personal": ("Personales", "Proyectos personales y herramientas de uso propio."),
           "academic": ("Académicos", "Proyectos ligados a la carrera y a la investigación."), "professional": ("Profesionales", "Plantillas y proyectos de uso profesional."),
           "col": ("Proyecto", "Descripción"), "sub": ("Categoría", "Proyectos"), "vazio": "Aún sin proyectos publicados."},
    "fr": {"projects": ("Projets", "Outils, applications et matériel pédagogique hors recherche."), "personal": ("Personnels", "Projets personnels et outils à usage propre."),
           "academic": ("Académiques", "Projets liés au cursus et à la recherche."), "professional": ("Professionnels", "Modèles et projets à usage professionnel."),
           "col": ("Projet", "Description"), "sub": ("Catégorie", "Projets"), "vazio": "Pas encore de projets publiés."},
}


def meta(p: Path):
    s = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)", s, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ("", s)
    t = re.search(r"^title:\s*[\"']?(.*?)[\"']?\s*$", fm, re.M)
    title = t.group(1) if t else p.parent.name
    desc = ""
    for line in body.splitlines():
        l = line.strip()
        if not l or l[0] in "#<>|`-!" or l.startswith(("[![", "Este projeto", "```", "---", "(")) or "dv." in l:
            continue
        desc = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", l)
        desc = re.sub(r"[*_`]", "", desc)
        break
    if len(desc) > 180:
        desc = desc[:177].rsplit(" ", 1)[0] + "..."
    return title, desc.replace("|", "/")


def hub(lang, rel, nome):
    d = ROOT / lang / rel
    t = L[lang]
    titulo, intro = t[nome]
    filhos = sorted(c for c in d.iterdir() if c.is_dir() and (c / "index.md").exists())
    if nome == "projects":
        linhas = [f"| {t['sub'][0]} | {t['sub'][1]} |", "| :--- | :--- |"]
        for c in filhos:
            n = len(list(x for x in c.iterdir() if x.is_dir() and (x / "index.md").exists()))
            lbl = t.get(c.name, (c.name,))[0]
            linhas.append(f"| [[{lang}/{rel}/{c.name}/index\\|{lbl}]] | {n} |")
    else:
        linhas = [f"| {t['col'][0]} | {t['col'][1]} |", "| :--- | :--- |"]
        for c in filhos:
            ti, de = meta(c / "index.md")
            linhas.append(f"| [[{lang}/{rel}/{c.name}/index\\|{ti}]] | {de} |")
    corpo = "\n".join(linhas) if filhos else t["vazio"]
    (d / "index.md").write_text(f'---\ntitle: "{titulo}"\npublish: true\ncssclasses:\n  - page-layout\ntags: []\n---\n\n{intro}\n\n{corpo}\n', encoding="utf-8")
    print("hub", lang, rel, len(filhos))


for lang in L:
    base = ROOT / lang / "projects"
    if not base.exists():
        continue
    hub(lang, "projects", "projects")
    for c in sorted(x for x in base.iterdir() if x.is_dir()):
        if c.name in L[lang]:
            hub(lang, f"projects/{c.name}", c.name)
