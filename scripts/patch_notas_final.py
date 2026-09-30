import re

with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    code = f.read()

funcs = """def md_to_latex_notes(md_text):
    md_text = re.sub(r'^---.*?---\n', '', md_text, flags=re.DOTALL)
    md_text = re.sub(r'\\| Material Didático.*?\\(Ajuste aula.*?\\.pdf\\)\\*', '', md_text, flags=re.DOTALL)
    
    math_blocks = []
    def math_repl(m):
        math_blocks.append(m.group(0))
        return f"@@MATH{len(math_blocks)-1}@@"
    md_text = re.sub(r'\\$.*?\\$', math_repl, md_text)
    
    def mermaid_repl(m):
        code = m.group(1).strip()
        return f"\\n\\\\begin{{tcolorbox}}[title=Diagrama (Mermaid)]\\n\\\\begin{{verbatim}}\\n{code}\\n\\\\end{{verbatim}}\\n\\\\end{{tcolorbox}}\\n"
    md_text = re.sub(r'```mermaid\\n(.*?)\\n```', mermaid_repl, md_text, flags=re.DOTALL)
    
    code_blocks = []
    def code_repl(m):
        code_blocks.append(m.group(1))
        return f"@@CODE{len(code_blocks)-1}@@"
    md_text = re.sub(r'`(.*?)`', code_repl, md_text)
    
    md_text = md_text.replace('\\\\', '@@BACKSLASH@@')
    md_text = md_text.replace('{', r'\\{').replace('}', r'\\}')
    md_text = md_text.replace('@@BACKSLASH@@', r'\\textbackslash{}')
    md_text = md_text.replace('%', r'\\%').replace('&', r'\\&').replace('#', r'\\#').replace('_', r'\\_').replace('"', "''")
    md_text = md_text.replace('^', r'\\textasciicircum{}').replace('~', r'\\textasciitilde{}')
    
    for i, cod in enumerate(code_blocks):
        code_esc = cod.replace('\\\\', r'\\textbackslash{}').replace('{', r'\\{').replace('}', r'\\}')
        code_esc = code_esc.replace('%', r'\\%').replace('&', r'\\&').replace('#', r'\\#').replace('_', r'\\_')
        md_text = md_text.replace(f"@@CODE{i}@@", f"\\\\texttt{{{code_esc}}}")
        
    md_text = re.sub(r'\\*\\*(.*?)\\*\\*', r'\\\\textbf{\\1}', md_text)
    md_text = re.sub(r'\\*(.*?)\\*', r'\\\\textit{\\1}', md_text)
    
    md_text = re.sub(r'^### (.*?)$', r'\\\\subsection{\\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.*?)$', r'\\\\section{\\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^# (.*?)$', r'\\\\section{\\1}', md_text, flags=re.MULTILINE)
    
    lines = md_text.split('\\n')
    out_lines = []
    in_list = False
    for line in lines:
        if re.match(r'^(\\*|-|\\d+\\.)\\s', line.strip()):
            if not in_list:
                out_lines.append(r'\\begin{itemize}')
                in_list = True
            item_text = re.sub(r'^(\\*|-|\\d+\\.)\\s+', '', line.strip())
            out_lines.append(f'  \\\\item {item_text}')
        else:
            if in_list and line.strip() == '':
                continue
            elif in_list:
                out_lines.append(r'\\end{itemize}')
                in_list = False
            
            if line.strip() == '':
                out_lines.append(r'\\vspace{0.2cm}')
            else:
                out_lines.append(line)
    if in_list:
        out_lines.append(r'\\end{itemize}')
        
    md_text = '\\n'.join(out_lines)
    for i, m in enumerate(math_blocks):
        md_text = md_text.replace(f"@@MATH{i}@@", m)
        
    return md_text

def gerar_tex_notas_institucionais"""
code = code.replace("def gerar_tex_notas_institucionais", funcs)

old_notas_body = r"""    lines.append(r"\vspace{0.8cm}")
    
    lines.append(r"\section{Introdução e Fundamentação Metodológica}")
    lines.append(r"Estas notas de aula documentam o referencial teórico-metodológico e técnico da \textbf{Aula " + num_str + r": " + titulo + r"}. A produção acadêmica e a redação científica exigem a harmonização entre a coerência argumentativa epistemológica e a observância rigorosa da normalização estabelecida pelas diretrizes da Associação Brasileira de Normas Técnicas (ABNT).")
    
    lines.append(r"\section{Normalização ABNT NBR 14724 e NBR 10520:2023}")
    lines.append(r"A estruturação de trabalhos acadêmicos no Instituto Federal Fluminense baseia-se na conformidade à NBR 14724:2011, que regulamenta a hierarquia dos elementos pré-textuais, textuais e pós-textuais. O controle tipográfico com margens canônicas e citações no formato autor-data estipulado pela NBR 10520:2023 confere credibilidade e padronização aos documentos.")
    
    lines.append(r"\subsection{Diagrama Estrutural do Documento Acadêmico (TikZ)}")
    lines.append(r"\begin{figure}[h!]")
    lines.append(r"\centering")
    lines.append(r"\begin{tikzpicture}[node distance=2.2cm, auto,")
    lines.append(r"  boxpre/.style={rectangle, draw=iffgreen, thick, fill=iffgreen!12!white, text width=3.8cm, align=center, rounded corners, minimum height=1.1cm},")
    lines.append(r"  boxtex/.style={rectangle, draw=iffgold, thick, fill=iffgold!12!white, text width=3.8cm, align=center, rounded corners, minimum height=1.1cm},")
    lines.append(r"  boxpos/.style={rectangle, draw=iffviolet, thick, fill=iffviolet!12!white, text width=3.8cm, align=center, rounded corners, minimum height=1.1cm},")
    lines.append(r"  arrow/.style={->, >=stealth, thick, color=iffred}")
    lines.append(r"]")
    lines.append(r"  \node[boxpre] (pre) {\textbf{1. Elementos Pré-textuais}\\ \small Capa, Rosto, Resumo};")
    lines.append(r"  \node[boxtex, right of=pre, xshift=3.2cm] (tex) {\textbf{2. Elementos Textuais}\\ \small Introdução, Desenvolvimento};")
    lines.append(r"  \node[boxpos, right of=tex, xshift=3.2cm] (pos) {\textbf{3. Elementos Pós-textuais}\\ \small Referências, Apêndices};")
    lines.append(r"  \draw[arrow] (pre) -- (tex);")
    lines.append(r"  \draw[arrow] (tex) -- (pos);")
    lines.append(r"\end{tikzpicture}")
    lines.append(r"\caption{Fluxo de informação normatizado de acordo com a ABNT NBR 14724.}")
    lines.append(r"\label{fig:fluxo_abnt}")
    lines.append(r"\end{figure}")
    
    lines.append(r"\section{Arquitetura Computacional e Prática no Ecossistema ReLaTeX}")
    lines.append(r"A diagramação via motor PDFLaTeX ou LuaLaTeX garante uma separação clara entre a lógica do texto (\texttt{.tex}) e as instruções tipográficas da classe (\texttt{ifftese.cls}). A utilização dos pacotes \texttt{metadados.sty} e \texttt{macros.sty} simplifica a governança de variáveis institucionais e a reprodutibilidade dos relatórios e monografias.")
    
    lines.append(r"\subsection{Comparativo Normativo em Tabela \texttt{booktabs}}")
    lines.append(r"\begin{table}[h!]")
    lines.append(r"\centering")
    lines.append(r"\caption{Correlação entre Diretrizes Normativas e Implementação TeX}")
    lines.append(r"\begin{tabular}{lll}")
    lines.append(r"\toprule")
    lines.append(r"\textbf{Componente Acadêmico} & \textbf{Norma ABNT Aplicável} & \textbf{Comando no Ecossistema ReLaTeX} \\")
    lines.append(r"\midrule")
    lines.append(r"Resumo e Palavras-Chave & ABNT NBR 6028:2021 & \texttt{\textbackslash begin\{resumo\}} \\")
    lines.append(r"Citações e Paráfrases & ABNT NBR 10520:2023 & \texttt{\textbackslash cite}, \texttt{\textbackslash citeonline} \\")
    lines.append(r"Apresentação Tabular & IBGE (1993) / NBR 14724 & \texttt{\textbackslash begin\{tabular\}} com \texttt{booktabs} \\")
    lines.append(r"Lista de Referências & ABNT NBR 6023:2018/2020 & \texttt{\textbackslash printbibliography} \\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    
    lines.append(r"\section{Aplicação Prática e Resolução de Inconsistências Comuns}")
    lines.append(r"Durante a redação acadêmica, problemas frequentes incluem o emprego inadequado de tabelas providas de linhas verticais em desacordo com a norma IBGE (1993), citações sem identificação de página em transcrições diretas e ausência de vetorização em ilustrações técnicas. O cumprimento da normalização elimina essas irregularidades.")
    
    lines.append(r"\section{Síntese Crítica e Autonomia Científica}")
    lines.append(r"A proficiência técnica no uso da normalização ABNT em convergência com a precisão tipográfica do LaTeX consolida a autonomia do pesquisador, valorizando a qualidade e a reprodutibilidade dos trabalhos publicados no Instituto Federal Fluminense.")"""

new_notas_body = r"""    lines.append(r"\vspace{0.8cm}")
    
    import glob
    md_files = glob.glob(f"content/pt-br/academic/courses/latex/aula-{num_str}-*.md")
    if md_files:
        with open(md_files[0], 'r', encoding='utf-8') as f:
            md_content = f.read()
        lines.append(md_to_latex_notes(md_content))
    else:
        lines.append(r"Conteúdo da aula não encontrado.")"""
code = code.replace(old_notas_body, new_notas_body)

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(code)
