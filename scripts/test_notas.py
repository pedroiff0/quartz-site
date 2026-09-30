import re, glob, os

def md_to_latex_notes(md_text):
    # Remove Frontmatter
    md_text = re.sub(r'^---.*?---\n', '', md_text, flags=re.DOTALL)
    # Remove the table with slides links
    md_text = re.sub(r'\| Material Didático.*?\(Ajuste aula.*?\.pdf\)\*', '', md_text, flags=re.DOTALL)
    
    math_blocks = []
    def math_repl(m):
        math_blocks.append(m.group(0))
        return f"@@MATH{len(math_blocks)-1}@@"
    md_text = re.sub(r'\$.*?\$', math_repl, md_text)
    
    def mermaid_repl(m):
        code = m.group(1).strip()
        # Escape backslashes for verbatim not needed, but verbatim handles everything
        return f"\n\\begin{{tcolorbox}}[title=Diagrama (Mermaid)]\n\\begin{{verbatim}}\n{code}\n\\end{{verbatim}}\n\\end{{tcolorbox}}\n"
    md_text = re.sub(r'```mermaid\n(.*?)\n```', mermaid_repl, md_text, flags=re.DOTALL)
    
    # other code blocks
    code_blocks = []
    def code_repl(m):
        code_blocks.append(m.group(1))
        return f"@@CODE{len(code_blocks)-1}@@"
    md_text = re.sub(r'`(.*?)`', code_repl, md_text)
    
    md_text = md_text.replace('\\', '@@BACKSLASH@@')
    md_text = md_text.replace('{', r'\{').replace('}', r'\}')
    md_text = md_text.replace('@@BACKSLASH@@', r'\textbackslash{}')
    md_text = md_text.replace('%', r'\%').replace('&', r'\&').replace('#', r'\#').replace('_', r'\_').replace('"', "''")
    md_text = md_text.replace('^', r'\textasciicircum{}').replace('~', r'\textasciitilde{}')
    
    for i, code in enumerate(code_blocks):
        code_esc = code.replace('\\', r'\textbackslash{}').replace('{', r'\{').replace('}', r'\}')
        code_esc = code_esc.replace('%', r'\%').replace('&', r'\&').replace('#', r'\#').replace('_', r'\_')
        md_text = md_text.replace(f"@@CODE{i}@@", f"\\texttt{{{code_esc}}}")
        
    md_text = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', md_text)
    md_text = re.sub(r'\*(.*?)\*', r'\\textit{\1}', md_text)
    
    md_text = re.sub(r'^### (.*?)$', r'\\subsection{\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^## (.*?)$', r'\\section{\1}', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'^# (.*?)$', r'\\section{\1}', md_text, flags=re.MULTILINE)
    
    lines = md_text.split('\n')
    out_lines = []
    in_list = False
    for line in lines:
        if re.match(r'^(\*|-|\d+\.)\s', line.strip()):
            if not in_list:
                out_lines.append(r'\begin{itemize}')
                in_list = True
            item_text = re.sub(r'^(\*|-|\d+\.)\s+', '', line.strip())
            out_lines.append(f'  \\item {item_text}')
        else:
            if in_list and line.strip() == '':
                continue
            elif in_list:
                out_lines.append(r'\end{itemize}')
                in_list = False
            
            # paragraph spacing
            if line.strip() == '':
                out_lines.append(r'\vspace{0.2cm}')
            else:
                out_lines.append(line)
    if in_list:
        out_lines.append(r'\end{itemize}')
        
    md_text = '\n'.join(out_lines)
    for i, m in enumerate(math_blocks):
        md_text = md_text.replace(f"@@MATH{i}@@", m)
        
    return md_text

for filepath in glob.glob('content/pt-br/academic/courses/latex/aula-*.md'):
    with open(filepath, 'r') as f:
        print(f"Testing {filepath}")
        md_to_latex_notes(f.read())
print("OK")
