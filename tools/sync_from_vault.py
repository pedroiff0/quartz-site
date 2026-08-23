import os
import shutil

hl_eng = '/home/pedro/hardcore-life/02 - Áreas/Acadêmico/IFF - Engenharia de Computação'
hl_materiais = os.path.join(hl_eng, '_materiais')
qs_eng = '/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/resource/Engenharia de Computação'
qs_disciplinas = '/home/pedro/Repositorios/pessoal/quartz-site/content/assets/disciplinas'

def sync_dirs(src, dst, exclude_names=None):
    if exclude_names is None:
        exclude_names = set()
    
    if os.path.islink(dst):
        os.remove(dst)
    os.makedirs(dst, exist_ok=True)
    
    # Copiar ou atualizar arquivos de src para dst
    for root, dirs, files in os.walk(src):
        # Excluir pastas ignoradas
        dirs[:] = [d for d in dirs if d not in exclude_names and not d.startswith('.')]
        
        rel = os.path.relpath(root, src)
        target_dir = os.path.join(dst, rel) if rel != '.' else dst
        os.makedirs(target_dir, exist_ok=True)
        
        for f in files:
            if f in exclude_names or f.startswith('.'):
                continue
            src_file = os.path.join(root, f)
            dst_file = os.path.join(target_dir, f)
            
            # Copiar se não existe ou se o tamanho/data difere
            if not os.path.exists(dst_file) or os.path.getmtime(src_file) > os.path.getmtime(dst_file) or os.path.getsize(src_file) != os.path.getsize(dst_file):
                shutil.copy2(src_file, dst_file)
                
    # Remover arquivos em dst que não existem mais em src
    for root, dirs, files in os.walk(dst):
        rel = os.path.relpath(root, dst)
        src_dir = os.path.join(src, rel) if rel != '.' else src
        
        for f in files:
            src_file = os.path.join(src_dir, f)
            if not os.path.exists(src_file):
                dst_file = os.path.join(root, f)
                os.remove(dst_file)
                
        for d in list(dirs):
            src_sub = os.path.join(src_dir, d)
            if not os.path.exists(src_sub):
                dst_sub = os.path.join(root, d)
                shutil.rmtree(dst_sub, ignore_errors=True)
                dirs.remove(d)

print('=== 🔄 SINCRONIZANDO NOTAS DO COFRE PARA O QUARTZ-SITE ===')
sync_dirs(hl_eng, qs_eng, exclude_names={'_materiais'})
print('✅ Notas acadêmicas sincronizadas com sucesso!')

print('\n=== 🔄 SINCRONIZANDO ASSETS (_materiais) PARA CONTENT/ASSETS/DISCIPLINAS ===')
if os.path.exists(hl_materiais):
    sync_dirs(hl_materiais, qs_disciplinas)
    print('✅ Materiais e slides sincronizados com sucesso!')
