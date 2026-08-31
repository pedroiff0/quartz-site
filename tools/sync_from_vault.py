#!/usr/bin/env python3
import os
import shutil
import re
import datetime

hl_eng = '/home/pedro/hardcore-life/02 - Áreas/Acadêmico/IFF - Engenharia de Computação'
hl_materiais = os.path.join(hl_eng, '_materiais')
qs_eng = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/Engenharia de Computação'
qs_disciplinas = '/home/pedro/Repositorios/pessoal/quartz-site/content/assets/disciplinas'

hl_escola = '/home/pedro/hardcore-life/05 - Recursos/Cursos/Escola de Inverno - ON'
qs_escola = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/escolainverno'

EXCLUDED_DIR_NAMES = {
    '_materiais',
    'esboço',
    'esboco',
    '.git',
    '.obsidian',
    '.stfolder',
    '.stignore',
    '.trash',
}

def is_excluded_dir(name: str) -> bool:
    name_lower = name.lower()
    return name_lower in EXCLUDED_DIR_NAMES or name_lower.startswith('.')

def is_excluded_file(name: str) -> bool:
    name_lower = name.lower()
    if name_lower.startswith('.') or '.sync-conflict-' in name_lower:
        return True
    return False

def clean_symlinks_in_dir(dir_path: str):
    if not os.path.exists(dir_path):
        return
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.islink(item_path):
            print(f"  🔗 Removendo link simbólico antigo: {item}")
            os.unlink(item_path)

LINK_REWRITES = [
    ("00 - Mapa", "pt-br/mapa"),
    ("02 - Áreas/Acadêmico/IFF - Engenharia de Computação", "pt-br/resource/Engenharia de Computação"),
    ("02 - Áreas/Acadêmico/Pesquisas/Escola de Inverno - ON", "pt-br/resource/escolainverno"),
    ("04 - Recursos/Cursos/Escola de Inverno - ON", "pt-br/resource/escolainverno"),
    ("05 - Recursos/Cursos/Escola de Inverno - ON", "pt-br/resource/escolainverno"),
    ("02 - Áreas/Acadêmico/Cursos/Curso ON", "pt-br/resource/curso-on"),
    ("02 - Áreas/Acadêmico/Cursos/LaTeX e Escrita Cientifica", "pt-br/resource/latex"),
    ("04 - Recursos/Cursos/Curso ON", "pt-br/resource/curso-on"),
    ("04 - Recursos/Cursos/LaTeX e Escrita Cientifica", "pt-br/resource/latex"),
    ("04 - Recursos/Computação", "pt-br/resource/computacao"),
    ("02 - Áreas/Acadêmico/Idiomas", "pt-br/resource/idiomas"),
    ("02 - Áreas/Acadêmico/Pesquisas", "pt-br/research"),
    ("01 - Projetos", "pt-br/projects"),
    ("03 - Mídia", "pt-br/media"),
    ("04 - Mídia", "pt-br/media"),
    ("07 - Diário", "pt-br/media"),
]

def convert_md_links_in_str(text: str) -> str:
    pattern = re.compile(r"(?<!\!)\[([^\]]+)\]\(([^)]+)\)")
    def replacer(match):
        label = match.group(1)
        target = match.group(2).strip()
        if target.startswith(("http://", "https://", "mailto:", "ftp://", "#", "tel:", "/")):
            return match.group(0)
        target_path = target.split("#")[0]
        anchor = ("#" + target.split("#")[1]) if "#" in target else ""
        if target_path.endswith(".md") or not "." in os.path.basename(target_path):
            clean_target = target_path.replace(".md", "").rstrip("/")
            if clean_target.startswith("/"):
                clean_target = clean_target[1:]
            target_str = f"{clean_target}{anchor}" if anchor else clean_target
            if label == clean_target or label == os.path.basename(clean_target):
                return f"[[{target_str}]]"
            else:
                return f"[[{target_str}|{label}]]"
        return match.group(0)
    return pattern.sub(replacer, text)

def parse_note_metadata(file_path: str):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    basename = os.path.basename(file_path).replace('.md', '')
    title = basename
    created = ""
    professor = "—"
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            for line in fm.splitlines():
                l = line.strip()
                if l.startswith(('title:', 'titulo:')):
                    val = l.split(':', 1)[1].strip().strip("'\"")
                    if val and val.lower() != 'anotações':
                        if re.match(r"^Aula\s+\d+$", val, re.IGNORECASE) and len(basename) > len(val):
                            title = basename
                        else:
                            title = val
                elif l.startswith(('created:', 'criado:')):
                    val = l.split(':', 1)[1].strip().strip("'\"")
                    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", val)
                    if m:
                        created = f"{m.group(3)}/{m.group(2)}/{m.group(1)}"
                    else:
                        m2 = re.search(r"(\d{2})/(\d{2})/(\d{4})", val)
                        if m2:
                            created = f"{m2.group(1)}/{m2.group(2)}/{m2.group(3)}"
                elif l.startswith(('professor:', 'docente:')):
                    val = l.split(':', 1)[1].strip().strip("'\"")
                    if val:
                        professor = val

    if title == basename:
        m_h1 = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if m_h1:
            title = m_h1.group(1).strip()
            title = title.replace('Notas de Aula - ', 'Aula: ').replace('Notas de Aula: ', 'Aula: ')

    if not created:
        m_date = re.match(r"^(\d{2})(\d{2})(\d{2})", basename)
        if m_date:
            yy, mm, dd = m_date.groups()
            created = f"{dd}/{mm}/20{yy}"
        else:
            mtime = os.path.getmtime(file_path)
            created = datetime.datetime.fromtimestamp(mtime).strftime('%d/%m/%Y')

    return {
        'basename': basename,
        'title': title,
        'created': created,
        'professor': professor,
        'path': file_path
    }

def generate_anotacoes_table(anotacoes_dir: str, prefix_link="") -> str:
    if not os.path.exists(anotacoes_dir):
        return "> [!info] Sem anotações registradas\n> As notas de aula desta disciplina serão disponibilizadas aqui conforme forem ministradas."
    
    notes = []
    for f in os.listdir(anotacoes_dir):
        if not f.endswith('.md'):
            continue
        f_lower = f.lower()
        if f_lower.startswith('index') or 'esboço' in f_lower or 'esboco' in f_lower or 'draft' in f_lower or '.sync-conflict' in f_lower:
            continue
        fp = os.path.join(anotacoes_dir, f)
        notes.append(parse_note_metadata(fp))
        
    if not notes:
        return "> [!info] Sem anotações registradas\n> As notas de aula desta disciplina serão disponibilizadas aqui conforme forem ministradas."
    
    notes.sort(key=lambda x: x['basename'])
    
    has_prof = any(n['professor'] != '—' for n in notes)
    
    lines = []
    if has_prof:
        lines.append("| Aula / Conteúdo | Data | Docente |")
        lines.append("| :--- | :---: | :--- |")
        for n in notes:
            link = f"{prefix_link}{n['basename']}"
            lines.append(f"| [[{link}\\|{n['title']}]] | {n['created']} | {n['professor']} |")
    else:
        lines.append("| Aula / Conteúdo | Data |")
        lines.append("| :--- | :---: |")
        for n in notes:
            link = f"{prefix_link}{n['basename']}"
            lines.append(f"| [[{link}\\|{n['title']}]] | {n['created']} |")
            
    return '\n'.join(lines)

def parse_journal_club_notes(jc_dir: str):
    if not os.path.exists(jc_dir):
        return []
    
    notes = []
    for f in os.listdir(jc_dir):
        if not f.endswith('.md'):
            continue
        f_lower = f.lower()
        if f_lower.startswith('index') or f_lower.startswith('dashboard') or f_lower.startswith('topicos') or f_lower.startswith('readme') or 'esboço' in f_lower or 'esboco' in f_lower or 'draft' in f_lower or '.sync-conflict' in f_lower:
            continue
        
        fp = os.path.join(jc_dir, f)
        with open(fp, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        basename = f.replace('.md', '')
        title = basename
        authors = "—"
        presenter = "—"
        year = "—"
        arxiv = ""
        discussed = ""
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = parts[1]
                for line in fm.splitlines():
                    l = line.strip()
                    if l.startswith('title:'):
                        val = l.split(':', 1)[1].strip().strip("'\"")
                        if val:
                            title = val
                    elif l.startswith('authors:'):
                        authors = l.split(':', 1)[1].strip().strip("'\"")
                    elif l.startswith(('presenter:', 'apresentador:')):
                        presenter = l.split(':', 1)[1].strip().strip("'\"")
                    elif l.startswith('year:'):
                        year = l.split(':', 1)[1].strip().strip("'\"")
                    elif l.startswith('arxiv:'):
                        arxiv = l.split(':', 1)[1].strip().strip("'\"")
                    elif l.startswith(('discussed:', 'discutido:')):
                        raw_date = l.split(':', 1)[1].strip().strip("'\"")
                        m = re.search(r"(\d{4})-(\d{2})-(\d{2})", raw_date)
                        if m:
                            discussed = f"{m.group(3)}/{m.group(2)}/{m.group(1)}"
                        else:
                            discussed = raw_date
                            
        # Se não tem arxiv, não é artigo de Journal Club
        if not arxiv:
            continue
            
        notes.append({
            'basename': basename,
            'title': title,
            'authors': authors,
            'presenter': presenter,
            'year': str(year),
            'arxiv': arxiv,
            'discussed': discussed,
            'path': fp
        })
        
    return notes

def generate_journal_club_table(jc_dir: str, query_text: str) -> str:
    notes = parse_journal_club_notes(jc_dir)
    if not notes:
        return "> [!info] Nenhum artigo registrado\n> Os artigos discutidos neste Journal Club serão listados aqui."
    
    query_lower = query_text.lower()
    
    # 1. Filtro: Se a query pede apenas os artigos apresentados por Pedro
    if "contains(presenter, \"pedro\")" in query_lower and not "!contains" in query_lower and not "not contains" in query_lower:
        filtered = [n for n in notes if "pedro" in n['presenter'].lower()]
        if not filtered:
            return "> [!info] Nenhum artigo apresentado até o momento."
        
        filtered.sort(key=lambda x: x['discussed'], reverse=True)
        
        lines = [
            "| Artigo | Autoria | Ano | Data | arXiv / Link |",
            "| :--- | :--- | :---: | :---: | :---: |"
        ]
        for n in filtered:
            arxiv_link = f"[{n['arxiv'].split('/')[-1]}]({n['arxiv']})" if n['arxiv'].startswith("http") else n['arxiv']
            lines.append(f"| [[{n['basename']}\\|{n['title']}]] | {n['authors']} | {n['year']} | {n['discussed']} | {arxiv_link} |")
        return '\n'.join(lines)
        
    # 2. Filtro: Se a query pede artigos apresentados por colegas (!contains(presenter, "Pedro"))
    elif "!contains(presenter, \"pedro\")" in query_lower or "not contains(presenter, \"pedro\")" in query_lower:
        filtered = [n for n in notes if "pedro" not in n['presenter'].lower()]
        if not filtered:
            return "> [!info] Nenhum artigo recomendado registrado no momento."
            
        filtered.sort(key=lambda x: x['discussed'], reverse=True)
        
        lines = [
            "| Artigo | Apresentado por | Autoria | Ano | Data | arXiv / Link |",
            "| :--- | :--- | :--- | :---: | :---: | :---: |"
        ]
        for n in filtered:
            arxiv_link = f"[{n['arxiv'].split('/')[-1]}]({n['arxiv']})" if n['arxiv'].startswith("http") else n['arxiv']
            lines.append(f"| [[{n['basename']}\\|{n['title']}]] | {n['presenter']} | {n['authors']} | {n['year']} | {n['discussed']} | {arxiv_link} |")
        return '\n'.join(lines)
        
    # 3. Tabela Geral (Ex: ENGCOMP ou visão ampla)
    else:
        notes.sort(key=lambda x: x['discussed'], reverse=True)
        lines = [
            "| Artigo | Apresentou | Autoria | Ano | Discutido em | arXiv |",
            "| :--- | :--- | :--- | :---: | :---: | :---: |"
        ]
        for n in notes:
            arxiv_link = f"[{n['arxiv'].split('/')[-1]}]({n['arxiv']})" if n['arxiv'].startswith("http") else n['arxiv']
            lines.append(f"| [[{n['basename']}\\|{n['title']}]] | {n['presenter']} | {n['authors']} | {n['year']} | {n['discussed']} | {arxiv_link} |")
        return '\n'.join(lines)

def transform_markdown_file(file_path: str):
    if not file_path.endswith('.md'):
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Reescrever caminhos de links internos de pastas do vault para slugs do site
    for old_prefix, new_prefix in LINK_REWRITES:
        content = content.replace(old_prefix, new_prefix)
    
    # 2. Converter links markdown no formato [label](path) para Wikilinks [[path|label]]
    content = convert_md_links_in_str(content)

    # 2.1 Em tabelas Markdown (| col1 | col2 |), converter Wikilinks para links markdown padrão [Label](Target)
    # Isso evita que o parser GFM/Remark quebre colunas devido ao pipe '|' interno do wikilink.
    lines_tmp = content.splitlines()
    table_lines = []
    for line in lines_tmp:
        if line.strip().startswith('|'):
            def table_link_converter(match):
                inner = match.group(1).strip()
                if '\\|' in inner:
                    parts = inner.split('\\|', 1)
                    target, label = parts[0].strip(), parts[1].strip()
                elif '|' in inner:
                    parts = inner.split('|', 1)
                    target, label = parts[0].strip(), parts[1].strip()
                else:
                    target = inner
                    label = os.path.basename(inner)
                
                formatted_target = f"<{target}>" if ' ' in target else target
                return f"[{label}]({formatted_target})"

            line = re.sub(r'\[\[(.*?)\]\]', table_link_converter, line)
        table_lines.append(line)
    content = '\n'.join(table_lines)

    # 3. Sanitizar permalinks, formatar criacao/modificacao e garantir cssclasses no frontmatter
    import datetime
    mtime_dt = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    mtime_str = mtime_dt.strftime('%Y-%m-%d %H:%M')

    parent_dir = os.path.dirname(file_path)
    parent_name = os.path.basename(parent_dir).lower()

    if not content.startswith('---'):
        content = f"---\ncreated: {mtime_str}\nmodified: {mtime_str}\ncssclasses:\n  - page-layout\n---\n\n" + content
    else:
        lines = content.splitlines()
        new_lines = []
        in_frontmatter = False
        frontmatter_count = 0
        has_cssclasses = False
        has_modified = False
        
        for line in lines:
            if line.strip() == '---':
                frontmatter_count += 1
                in_frontmatter = (frontmatter_count == 1)
                if frontmatter_count == 2:
                    if not has_modified:
                        new_lines.append(f'modified: {mtime_str}')
                    if not has_cssclasses:
                        new_lines.append('cssclasses:')
                        new_lines.append('  - page-layout')
            
            if in_frontmatter:
                l = line.strip()
                if l.startswith('permalink:'):
                    continue
                if l.startswith(('modified:', 'modificado:')):
                    has_modified = True
                    new_lines.append(f'modified: {mtime_str}')
                    continue
                if l.startswith(('created:', 'criado:')):
                    raw_val = l.split(':', 1)[1].strip().strip("'\"")
                    m_full = re.search(r"(\d{4}-\d{2}-\d{2})[T\s](\d{2}:\d{2})", raw_val)
                    if m_full:
                        clean_val = f"{m_full.group(1)} {m_full.group(2)}"
                    else:
                        m_br = re.search(r"(\d{2})/(\d{2})/(\d{4})(?:[T\s](\d{2}:\d{2}))?", raw_val)
                        if m_br:
                            d, m, y, t = m_br.groups()
                            clean_val = f"{y}-{m}-{d} {t}" if t else f"{y}-{m}-{d} {mtime_dt.strftime('%H:%M')}"
                        elif re.match(r"^\d{4}-\d{2}-\d{2}", raw_val):
                            clean_val = f"{raw_val[:10]} {mtime_dt.strftime('%H:%M')}"
                        else:
                            clean_val = mtime_str
                    new_lines.append(f'created: {clean_val}')
                    continue
                if l.startswith(('date:', 'data:')):
                    raw_val = l.split(':', 1)[1].strip().strip("'\"")
                    m_br = re.search(r"(\d{2})/(\d{2})/(\d{4})(?:[T\s](\d{2}:\d{2}))?", raw_val)
                    if m_br:
                        d, m, y, t = m_br.groups()
                        clean_val = f"{y}-{m}-{d} {t}" if t else f"{y}-{m}-{d}"
                    elif re.match(r"^\d{4}-\d{2}-\d{2}", raw_val):
                        clean_val = raw_val
                    else:
                        clean_val = raw_val
                    new_lines.append(f'date: {clean_val}')
                    continue
                if l.startswith('titulo:'):
                    val = l.split(':', 1)[1].strip()
                    new_lines.append(f'title: {val}')
                    continue
                if l.startswith('disciplina:'):
                    val = l.split(':', 1)[1].strip()
                    new_lines.append(f'discipline: {val}')
                    continue
                if l.startswith('cssclasses:'):
                    has_cssclasses = True
                if (parent_name == 'anotações' or parent_name == 'anotacoes') and os.path.basename(file_path) == 'index.md' and l.startswith(('title:', 'titulo:')):
                    new_lines.append('title: "Anotações"')
                    continue
                    
            new_lines.append(line)
            
        content = '\n'.join(new_lines)

    # 4. Avaliar e renderizar blocos Dataview para tabelas estáticas Markdown (sem pegar dataviewjs)
    def dataview_replacer(match):
        block_text = match.group(0)
        is_jc = ('journal-clubs' in file_path.lower() or 
                 'journal-clubs' in block_text.lower() or 
                 'arxiv' in block_text.lower() or
                 'mwbr' in file_path.lower() or
                 'engcomp' in file_path.lower())
        if is_jc:
            return generate_journal_club_table(parent_dir, block_text)
        elif parent_name == 'anotações' or parent_name == 'anotacoes':
            return generate_anotacoes_table(parent_dir)
        elif os.path.exists(os.path.join(parent_dir, 'Anotações')):
            anot_dir = os.path.join(parent_dir, 'Anotações')
            return generate_anotacoes_table(anot_dir, prefix_link="Anotações/")
        else:
            return generate_anotacoes_table(parent_dir)

    content = re.sub(r'```dataview\b[\s\S]*?```', dataview_replacer, content)

    # 5. Avaliar e renderizar blocos DataviewJS
    def dataviewjs_replacer(match):
        block_text = match.group(0)
        if 'interactive-nav-bar' in block_text or 'disciplineAulas' in block_text or 'prevLink' in block_text or 'hubLink' in block_text:
            return '''<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 16px; background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 10px; margin: 1.5rem 0;">
  <div>⬅️ <b><a href="../index">Hub da Disciplina</a></b></div>
  <div>🏠 <b><a href="../index">Visão Geral</a></b></div>
  <div>➡️ <b><a href="../index">Aulas</a></b></div>
</div>'''
        elif '_materiais' in block_text or 'slides_aula' in block_text:
            return '''> [!tip] 🔗 Arquivos e Materiais da Disciplina
> - 📄 **Slides do Docente:** *Consulte os anexos vinculados*
> - 📑 **Roteiro / Texto de Apoio:** *Consulte os materiais de aula*
> - 📦 **Exercícios / Anexos:** *Disponíveis no repositório*'''
        else:
            return '''<div class="progress-bar-container" style="background: var(--light, #f8fafc); border: 1px solid var(--lightgray, #e2e8f0); border-radius: 8px; padding: 12px 16px; margin: 1.5rem 0;">
  <div style="font-weight: 600; font-size: 0.85rem; color: var(--dark, #334155); margin-bottom: 6px;">Progresso das Aulas da Disciplina</div>
  <div style="background: var(--lightgray, #e2e8f0); border-radius: 4px; overflow: hidden; height: 8px;">
    <div style="background: var(--secondary, #6d28d9); width: 10%; height: 100%;"></div>
  </div>
</div>'''

    content = re.sub(r'```dataviewjs\b[\s\S]*?```', dataviewjs_replacer, content)

    if content and not content.endswith('\n'):
        content += '\n'
        
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

def sync_dirs(src: str, dst: str, exclude_dir_fn=is_excluded_dir, exclude_file_fn=is_excluded_file):
    if not os.path.exists(src):
        print(f"⚠️ Diretório de origem não encontrado: {src}")
        return

    if os.path.islink(dst):
        os.unlink(dst)
    os.makedirs(dst, exist_ok=True)

    clean_symlinks_in_dir(dst)

    copied_count = 0
    updated_count = 0
    deleted_count = 0

    # 1. Copiar ou atualizar arquivos de src para dst
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if not exclude_dir_fn(d)]

        rel = os.path.relpath(root, src)
        target_dir = os.path.join(dst, rel) if rel != '.' else dst
        os.makedirs(target_dir, exist_ok=True)

        for f in files:
            if exclude_file_fn(f):
                continue
            src_file = os.path.join(root, f)
            dst_file = os.path.join(target_dir, f)

            if os.path.islink(dst_file):
                os.unlink(dst_file)

            needs_copy = False
            if not os.path.exists(dst_file):
                needs_copy = True
                copied_count += 1
            else:
                src_stat = os.stat(src_file)
                dst_stat = os.stat(dst_file)
                if src_stat.st_mtime > dst_stat.st_mtime or src_stat.st_size != dst_stat.st_size:
                    needs_copy = True
                    updated_count += 1

            if needs_copy:
                shutil.copy2(src_file, dst_file)
                transform_markdown_file(dst_file)
            else:
                # Garantir transformação em arquivos existentes também
                transform_markdown_file(dst_file)

    # 2. Remover arquivos e diretórios em dst que não devem existir (esboço, deletados no vault, etc.)
    for root, dirs, files in os.walk(dst, topdown=False):
        rel = os.path.relpath(root, dst)
        src_dir = os.path.join(src, rel) if rel != '.' else src

        for f in files:
            dst_file = os.path.join(root, f)
            src_file = os.path.join(src_dir, f)
            should_remove = False

            if os.path.islink(dst_file):
                should_remove = True
            elif exclude_file_fn(f):
                should_remove = True
            elif not os.path.exists(src_file):
                should_remove = True

            if should_remove:
                os.remove(dst_file)
                deleted_count += 1

        for d in dirs:
            dst_sub = os.path.join(root, d)
            src_sub = os.path.join(src_dir, d)
            should_remove = False

            if os.path.islink(dst_sub):
                should_remove = True
            elif exclude_dir_fn(d):
                should_remove = True
            elif not os.path.exists(src_sub):
                should_remove = True

            if should_remove:
                shutil.rmtree(dst_sub, ignore_errors=True)
                deleted_count += 1

    print(f"  📊 Resultado: {copied_count} novos, {updated_count} atualizados, {deleted_count} removidos.")

if __name__ == '__main__':
    print('=== 🔄 SINCRONIZANDO NOTAS DO COFRE (IFF - Engenharia) PARA O QUARTZ-SITE ===')
    print(f"Origem: {hl_eng}")
    print(f"Destino: {qs_eng}")
    sync_dirs(hl_eng, qs_eng)
    print('✅ Notas acadêmicas sincronizadas com sucesso!')

    print('\n=== 🔄 SINCRONIZANDO NOTAS DO COFRE (Escola de Inverno) PARA O QUARTZ-SITE ===')
    hl_escola = '/home/pedro/hardcore-life/05 - Recursos/Cursos/Escola de Inverno - ON'
    qs_escola = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/escolainverno'
    sync_dirs(hl_escola, qs_escola)
    print('✅ Notas da Escola de Inverno sincronizadas com sucesso!')

    print('\n=== 🔄 SINCRONIZANDO NOTAS DO COFRE (Mídia) PARA O QUARTZ-SITE ===')
    hl_media = '/home/pedro/hardcore-life/04 - Mídia'
    qs_media = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/media'
    sync_dirs(hl_media, qs_media)

    print('\n=== 🔄 SINCRONIZANDO NOTAS DO COFRE (Projetos) PARA O QUARTZ-SITE ===')
    hl_proj = '/home/pedro/hardcore-life/01 - Projetos/Site-Publico'
    qs_proj = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/projects'
    sync_dirs(hl_proj, qs_proj)

    print('\n=== 🔄 SINCRONIZANDO NOTAS DO COFRE (Pesquisas) PARA O QUARTZ-SITE ===')
    hl_anom = '/home/pedro/hardcore-life/02 - Áreas/Acadêmico/Pesquisas/Anomaly_Detection'
    qs_anom = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/research/anomaly-detection'
    sync_dirs(hl_anom, qs_anom)

    hl_jc = '/home/pedro/hardcore-life/02 - Áreas/Acadêmico/Pesquisas/Journal-Clubs'
    qs_jc = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/research/journal-clubs'
    sync_dirs(hl_jc, qs_jc)

    print('\n=== 🔄 SINCRONIZANDO NOTAS DO COFRE (Cursos & Recursos) PARA O QUARTZ-SITE ===')
    hl_curso_on = '/home/pedro/hardcore-life/05 - Recursos/Cursos/Curso ON'
    qs_curso_on = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/curso-on'
    sync_dirs(hl_curso_on, qs_curso_on)

    hl_latex = '/home/pedro/hardcore-life/05 - Recursos/Cursos/LaTeX e Escrita Cientifica'
    qs_latex = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/latex'
    sync_dirs(hl_latex, qs_latex)

    hl_comp = '/home/pedro/hardcore-life/05 - Recursos/Computação'
    qs_comp = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/computacao'
    sync_dirs(hl_comp, qs_comp)

    hl_idiomas = '/home/pedro/hardcore-life/02 - Áreas/Acadêmico/Idiomas'
    qs_idiomas = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/idiomas'
    sync_dirs(hl_idiomas, qs_idiomas)

    print('\n=== 🔄 SINCRONIZANDO PASTA SOBRE MIM PARA O QUARTZ-SITE ===')
    hl_sobre_dir = '/home/pedro/hardcore-life/00 - Mapa/Sobre Mim'
    qs_sobre_dir = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/sobre-mim'
    if os.path.exists(hl_sobre_dir):
        sync_dirs(hl_sobre_dir, qs_sobre_dir)
        hl_sobre_index = os.path.join(hl_sobre_dir, 'index.md')
        qs_ptbr_index = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/index.md'
        if os.path.exists(hl_sobre_index):
            shutil.copy2(hl_sobre_index, qs_ptbr_index)
            transform_markdown_file(qs_ptbr_index)
            print('✅ Sobre Mim -> content/pt-br/index.md & content/pt-br/sobre-mim/ sincronizados com sucesso!')

    # Clean up unneeded files and directories
    redundant_paths = [
        '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/mapa',
        '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/sobre-mim.md',
        '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/canvas.md',
        '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/canvas'
    ]
    for r_path in redundant_paths:
        if os.path.isdir(r_path):
            shutil.rmtree(r_path, ignore_errors=True)
            print(f"  🧹 Removido diretório redundante: {r_path}")
        elif os.path.isfile(r_path):
            os.remove(r_path)
            print(f"  🧹 Removido arquivo redundante: {r_path}")
