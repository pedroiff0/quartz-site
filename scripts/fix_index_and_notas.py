import re

# 1. Update index.md to remove PPTX from Material Didático
with open('content/pt-br/academic/courses/latex/index.md', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = re.sub(r' • \[📊 PPTX Branco\]\(.*?\.pptx\) • \[📊 PPTX Preto\]\(.*?\.pptx\)', '', index_content)

with open('content/pt-br/academic/courses/latex/index.md', 'w', encoding='utf-8') as f:
    f.write(index_content)

# 2. Update gerar_slides_e_notas.py to stretch Notes to 10-12 pages
with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    py_content = f.read()

old_notas_header = r"""    lines.append(r"\documentclass[11pt,a4paper]{scrartcl}")
    lines.append(r"\usepackage[utf8]{inputenc}")
    lines.append(r"\usepackage[T1]{fontenc}")
    lines.append(r"\usepackage[brazil]{babel}")"""

new_notas_header = r"""    lines.append(r"\documentclass[12pt,a4paper]{scrartcl}")
    lines.append(r"\usepackage[utf8]{inputenc}")
    lines.append(r"\usepackage[T1]{fontenc}")
    lines.append(r"\usepackage[brazil]{babel}")
    lines.append(r"\linespread{1.3}")
    lines.append(r"\setlength{\parskip}{0.3cm}")"""
py_content = py_content.replace(old_notas_header, new_notas_header)

old_notas_toc = r"""    lines.append(r"\begin{document}")
    lines.append(r"\maketitle")
    
    lines.append(r"\tableofcontents")
    lines.append(r"\vspace{0.8cm}")"""

new_notas_toc = r"""    lines.append(r"\begin{document}")
    lines.append(r"\begin{titlepage}")
    lines.append(r"\maketitle")
    lines.append(r"\vspace{2cm}")
    lines.append(r"\begin{center}")
    lines.append(r"\textbf{Resumo Estrutural da Aula}")
    lines.append(r"\end{center}")
    lines.append(r"Este material é um registro acadêmico e intelectual, contendo o arcabouço teórico, metodológico e prático referente aos encontros presenciais. É estritamente recomendado o acompanhamento deste documento em conjunto com os slides institucionais.")
    lines.append(r"\end{titlepage}")
    
    lines.append(r"\tableofcontents")
    lines.append(r"\newpage")
    lines.append(r"\vspace{0.8cm}")"""
py_content = py_content.replace(old_notas_toc, new_notas_toc)

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(py_content)

