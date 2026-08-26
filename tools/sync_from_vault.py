#!/usr/bin/env python3
import os
import shutil

hl_eng = '/home/pedro/hardcore-life/02 - Áreas/Acadêmico/IFF - Engenharia de Computação'
hl_materiais = os.path.join(hl_eng, '_materiais')
qs_eng = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/Engenharia de Computação'
qs_disciplinas = '/home/pedro/Repositorios/pessoal/quartz-site/content/assets/disciplinas'

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
        # Filtrar diretórios ignorados (in-place modification de dirs para impedir descida)
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
    print('✅ Notas acadêmicas sincronizadas com sucesso (sem esboço e com arquivos reais)!')

    print('\n=== 🔄 SINCRONIZANDO ASSETS (_materiais) PARA CONTENT/ASSETS/DISCIPLINAS ===')
    if os.path.exists(hl_materiais):
        print(f"Origem: {hl_materiais}")
        print(f"Destino: {qs_disciplinas}")
        sync_dirs(
            hl_materiais,
            qs_disciplinas,
            exclude_dir_fn=lambda d: d.lower() in {'.git', '.obsidian', '.stfolder', '.stignore'} or d.startswith('.'),
            exclude_file_fn=is_excluded_file
        )
        print('✅ Materiais e slides sincronizados com sucesso!')
