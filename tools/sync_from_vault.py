#!/usr/bin/env python3
import os
import shutil
import re

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

    # 3. Sanitizar permalinks, formatar criacao/modificacao e garantir cssclasses no frontmatter
    import datetime
    mtime_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')

    if not content.startswith('---'):
        content = f"---\ncreated: {mtime_date}\nmodified: {mtime_date}\ncssclasses:\n  - page-layout\n---\n\n" + content
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
                        new_lines.append(f'modified: {mtime_date}')
                    if not has_cssclasses:
                        new_lines.append('cssclasses:')
                        new_lines.append('  - page-layout')
            
            if in_frontmatter:
                l = line.strip()
                if l.startswith('permalink:'):
                    continue
                if l.startswith('modified:') or l.startswith('modificado:'):
                    has_modified = True
                    new_lines.append(f'modified: {mtime_date}')
                    continue
                if l.startswith('created:') or l.startswith('criado:'):
                    raw_val = l.split(':', 1)[1].strip().strip("'\"")
                    m = re.search(r"(\d\d)/(\d\d)/(\d\d\d\d)", raw_val)
                    if m:
                        clean_val = f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
                    elif re.match(r"^\d{4}-\d{2}-\d{2}", raw_val):
                        clean_val = raw_val[:10]
                    else:
                        clean_val = mtime_date
                    new_lines.append(f'created: {clean_val}')
                    continue
                if l.startswith('cssclasses:'):
                    has_cssclasses = True
                    
            new_lines.append(line)
            
        content = '\n'.join(new_lines)
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
