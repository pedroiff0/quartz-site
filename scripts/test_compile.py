import os, sys, tempfile, shutil, subprocess, re
sys.path.append('.')
from scripts.gerar_slides_e_notas import gerar_tex_slides_52_frames, generate_qr_transparent

tex = gerar_tex_slides_52_frames(9, 'Aula 9', 'Sub', False)
cls_dir = '/home/pedro/Repositorios/latex/modelos/slide-mostra'
with tempfile.TemporaryDirectory() as tmp_dir:
    tex_path = os.path.join(tmp_dir, "documento.tex")
    with open(tex_path, "w", encoding='utf-8') as f: f.write(tex)
    for item in os.listdir(cls_dir):
        s = os.path.join(cls_dir, item)
        d = os.path.join(tmp_dir, item)
        if os.path.isdir(s): shutil.copytree(s, d, dirs_exist_ok=True)
        else: shutil.copy2(s, d)
    img_dir = os.path.join(tmp_dir, "img")
    os.makedirs(img_dir, exist_ok=True)
    generate_qr_transparent('https://pedroiff0.github.io/page/pt-br/academic/courses/latex', os.path.join(img_dir, "qrcode_transparente.png"), is_dark_theme=False)
    shutil.copy2("/home/pedro/Downloads/_cosmic_assets/iff/iff_bji_light.png", os.path.join(img_dir, "logoiff.png"))
    
    cmd = ["pdflatex", "-interaction=nonstopmode", "documento.tex"]
    subprocess.run(cmd, cwd=tmp_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    log_path = os.path.join(tmp_dir, "documento.log")
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='latin-1') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith('! '):
                    print('ERROR STARTING AT LINE', i)
                    print(''.join(lines[max(0, i-5):min(len(lines), i+15)]))
                    break
            else:
                print('NO ERRORS FOUND IN LOG!')
