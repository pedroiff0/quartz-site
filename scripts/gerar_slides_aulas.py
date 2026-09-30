#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Gerador Institucional de Aulas e Slides (.tex -> PDF Protegido -> PPTX Protegido -> Thumbs).
Desenvolvido para o ecossistema ReLaTeX - IFF Campus Bom Jesus do Itabapoana.
Professor Responsável: Prof. Dr. Pedro Henrique Rocha de Andrade

Funcionamento:
1. Varre os arquivos de aula (aula-*.md) do curso.
2. Extrai ou gera o código LaTeX institucional ('if-beamer.cls').
3. Compila o '.tex' para PDF no diretório '/resource/areas/academico/biblioteca/<slug>/slides-latex/'.
4. APLICA AUTOMATICAMENTE A SENHA PADRÃO ('escritaiff2026') em todos os PDFs gerados!
5. Gera versão Widescreen PPTX em '/resource/areas/academico/biblioteca/<slug>/slides-pptx/' (com senha padrão).
6. Gera imagem de capa PNG (thumbnail) em '/resource/areas/academico/biblioteca/<slug>/thumbs/'.
7. Aciona 'generate_course_table.py' para sincronizar a tabela e carrossel no 'index.md'.

Uso:
  python3 scripts/gerar_slides_aulas.py --slug latex-escrita --senha escritaiff2026
  python3 scripts/gerar_slides_aulas.py --dir content/templates/ModeloCurso --slug modelo-curso
"""

import os
import re
import sys
import glob
import shutil
import argparse
import subprocess
import tempfile
from pypdf import PdfReader, PdfWriter

def encrypt_pdf(pdf_path, password="escritaiff2026"):
    """Criptografa um arquivo PDF existente usando a senha padrão institucional."""
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        writer.append_pages_from_reader(reader)
        writer.encrypt(password)
        with open(pdf_path, "wb") as f_out:
            writer.write(f_out)
        return True
    except Exception as e:
        print(f"[ERRO] Falha ao proteger PDF com senha em '{pdf_path}': {e}")
        return False

def generate_pdf_from_tex(tex_code, output_pdf_path, cls_src_dir=None, password="escritaiff2026"):
    """Compila uma string ou código .tex em PDF e APLICA A SENHA PADRÃO INSTITUCIONAL."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tex_file = os.path.join(tmp_dir, "apresentacao.tex")
        with open(tex_file, "w", encoding="utf-8") as f:
            f.write(tex_code)

        # Copiar classe institucional if-beamer.cls e pasta figuras se existirem
        if cls_src_dir and os.path.exists(cls_src_dir):
            cls_file = os.path.join(cls_src_dir, "if-beamer.cls")
            if os.path.exists(cls_file):
                shutil.copy(cls_file, tmp_dir)
            fig_dir = os.path.join(cls_src_dir, "figuras")
            if os.path.exists(fig_dir):
                shutil.copytree(fig_dir, os.path.join(tmp_dir, "figuras"), dirs_exist_ok=True)

        cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "apresentacao.tex"]
        for p in range(2):
            subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        tmp_pdf = os.path.join(tmp_dir, "apresentacao.pdf")
        if not os.path.exists(tmp_pdf):
            return False

        # Copiar para o caminho de destino
        os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
        shutil.copy(tmp_pdf, output_pdf_path)

        # Aplicar criptografia com a senha padrão no arquivo PDF final
        return encrypt_pdf(output_pdf_path, password=password)

def extract_latex_from_md(md_path):
    """Extrai bloco de código Beamer LaTeX (```latex ... ```) de um arquivo markdown de aula."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"```(?:latex|tex)\s*\n(.*?\b(?:if-beamer|documentclass)\b.*?)\n```", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def build_default_beamer_code(num_aula, title):
    """Gera código Beamer canônico caso a aula não possua um bloco explícito."""
    return f"""\\documentclass{{if-beamer}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[brazil]{{babel}}

\\title{{Aula {num_aula:02d}: {title}}}
\\author{{Prof. Dr. Pedro Henrique Rocha de Andrade}}
\\institute{{Instituto Federal Fluminense --- Campus Bom Jesus do Itabapoana}}
\\date{{\\today}}

\\begin{{document}}

\\begin{{frame}}
  \\titlepage
\\end{{frame}}

\\begin{{frame}}{{Tópicos Abordados na Aula {num_aula:02d}}}
  \\begin{{itemize}}
    \\item Referencial teórico-metodológico institucional.
    \\item Aplicação estrita das normas ABNT vigentes.
    \\item Automação documental e engenharia com ecossistema ReLaTeX.
  \\end{{itemize}}
\\end{{frame}}

\\begin{{frame}}{{Acesso ao Material Suplementar}}
  \\begin{{block}}{{Aviso Institucional}}
    Todo o material letivo, notas de aula e resoluções de exercícios encontram-se protegidos no repositório institucional do curso.
  \\end{{block}}
\\end{{frame}}

\\end{{document}}
"""

def generate_thumb(pdf_path, thumb_path):
    """Gera miniatura PNG da capa de um PDF."""
    try:
        os.makedirs(os.path.dirname(os.path.abspath(thumb_path)), exist_ok=True)
        prefix = thumb_path[:-4]
        res = subprocess.run(
            ["pdftoppm", "-png", "-r", "150", "-f", "1", "-l", "1", pdf_path, prefix],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        if res.returncode == 0:
            generated = f"{prefix}-1.png"
            if os.path.exists(generated):
                if os.path.exists(thumb_path):
                    os.remove(thumb_path)
                os.rename(generated, thumb_path)
                return True
    except Exception as e:
        print(f"[ERRO] Falha na geração da capa '{thumb_path}': {e}")
    return False

def main():
    parser = argparse.ArgumentParser(description="Gerador de Slides (.tex) com Senha Padrão Automática")
    parser.add_argument("--dir", default="content/pt-br/academic/courses/latex", help="Pasta do curso")
    parser.add_argument("--slug", default="latex-escrita", help="Slug na biblioteca de assets")
    parser.add_argument("--senha", default="escritaiff2026", help="Senha padrão dos PDFs (default: escritaiff2026)")
    args = parser.parse_args()

    root_repo = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    course_dir = os.path.join(root_repo, args.dir)
    base_lib = os.path.join(root_repo, "content/resource/areas/academico/biblioteca", args.slug)
    cls_src_dir = os.path.join(root_repo, "content/assets/modelos_slides/if-beamer") # ou repositório do Pedro se local
    if not os.path.exists(cls_src_dir):
        cls_src_dir = "/home/pedro/Repositorios/academicos/modelos/slides/modelo_slides"

    out_latex = os.path.join(base_lib, "slides-latex")
    out_pptx = os.path.join(base_lib, "slides-pptx")
    out_thumbs = os.path.join(base_lib, "thumbs")

    os.makedirs(out_latex, exist_ok=True)
    os.makedirs(out_pptx, exist_ok=True)
    os.makedirs(out_thumbs, exist_ok=True)

    lesson_files = sorted(glob.glob(os.path.join(course_dir, "aula-*.md")))
    print(f"[{args.slug}] Processando {len(lesson_files)} aulas com proteção automática por senha ('{args.senha}')...")

    sucesso_pdf = 0
    for md_path in lesson_files:
        filename = os.path.basename(md_path)
        match = re.match(r"^aula-(\d+)-(.*?)\.md$", filename)
        if not match:
            continue
        num_aula = int(match.group(1))
        slug_aula = match.group(2).replace("-", " ").title()

        pdf_latex = os.path.join(out_latex, f"aula-{num_aula:02d}.pdf")
        pdf_pptx = os.path.join(out_pptx, f"aula-{num_aula:02d}.pdf")
        png_thumb = os.path.join(out_thumbs, f"aula-{num_aula:02d}.png")

        # 1. Obter código LaTeX da aula
        tex_code = extract_latex_from_md(md_path)
        if not tex_code:
            tex_code = build_default_beamer_code(num_aula, slug_aula)

        print(f"  -> Aula {num_aula:02d}: compilando slides LaTeX com senha padrão '{args.senha}'...")
        if generate_pdf_from_tex(tex_code, pdf_latex, cls_src_dir=cls_src_dir, password=args.senha):
            sucesso_pdf += 1
            # Para PPTX, geramos o Widescreen 16:9 e também aplicamos a senha padrão
            tex_pptx = tex_code.replace("\\documentclass{if-beamer}", "\\documentclass[aspectratio=169]{if-beamer}")
            generate_pdf_from_tex(tex_pptx, pdf_pptx, cls_src_dir=cls_src_dir, password=args.senha)
            generate_thumb(pdf_latex, png_thumb)
        else:
            print(f"     [AVISO] Falha ao compilar slide da aula {num_aula:02d}.")

    print(f"[{args.slug}] Geração concluída: {sucesso_pdf} pares de slides (.pdf) criptografados com senha padrão.")

    # Sincronizar tabela e carrossel do curso automaticamente
    try:
        from generate_course_table import update_course_index
        update_course_index(course_dir, args.slug, root_repo)
    except Exception as e:
        print(f"[AVISO] Não foi possível chamar generate_course_table: {e}")

if __name__ == "__main__":
    main()
