import re

with open('scripts/gerar_slides_e_notas.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Add extract_slides_from_md above gerar_tex_slides_52_frames
extract_func = """
import glob
def extract_slides_from_md(num_str):
    pattern = f"/home/pedro/Repositorios/pessoal/quartz-site/content/pt-br/academic/courses/latex/aula-{num_str}-*.md"
    files = glob.glob(pattern)
    if not files: return [{"title": "Conteúdo indisponível", "items": ["Arquivo MD não encontrado."]}]
    with open(files[0], 'r', encoding='utf-8') as f: content = f.read()
    sections = re.split(r'\\n##\\s+', content)
    slides_data = []
    for sec in sections[1:]:
        lines = sec.split('\\n')
        title = lines[0].strip()
        if 'Recursos Adicionais' in title or 'Sumário' in title or 'Referências' in title or 'Material Didático' in title: continue
        bullets = []
        for line in lines[1:]:
            line = line.strip()
            if not line or line.startswith('```') or line.startswith('|') or line.startswith('<'): continue
            if line.startswith('- ') or line.startswith('* '): bullets.append(line[2:])
            elif line.startswith('### '): bullets.append('[AZUL] ' + line[4:])
            else:
                if len(line) > 10: bullets.append(line)
        chunk_size = 4
        for i in range(0, len(bullets), chunk_size):
            slides_data.append({'title': title + (f' (Cont.)' if i > 0 else ''), 'items': bullets[i:i+chunk_size]})
    return slides_data

def gerar_tex_slides_52_frames"""

code = code.replace("def gerar_tex_slides_52_frames", extract_func)

# 2. Update popule_pptx_institucional
new_popule = """def popule_pptx_institucional(template_path, output_pptx_path, num_str, titulo, subtitulo, is_dark=False, url_qr="https://www.phrandrade.com/pt-br/academic/courses/latex"):
    prs = pptx.Presentation(template_path)
    
    obrigado_idx = -1
    for i, slide in enumerate(prs.slides):
        for shape in slide.shapes:
            if shape.has_text_frame and "Obrigado" in shape.text_frame.text:
                obrigado_idx = i
                break
        if obrigado_idx != -1: break
    if obrigado_idx == -1: obrigado_idx = len(prs.slides) - 1
    
    for i in range(len(prs.slides)-1, 0, -1):
        if i != obrigado_idx:
            rId = prs.slides._sldIdLst[i].rId
            prs.part.drop_rel(rId)
            del prs.slides._sldIdLst[i]
            
    slide_capa = prs.slides[0]
    for shape in slide_capa.shapes:
        if shape.has_text_frame:
            text_val = shape.text_frame.text
            if "Apresentador:" in text_val or "Pedro" in text_val:
                shape.text_frame.clear()
                p = shape.text_frame.paragraphs[0]
                p.text = "Pedro Henrique Rocha de Andrade"
                p.font.size = Pt(14)
                p.font.bold = True
                p.font.color.rgb = RGBColor(245, 158, 11) if is_dark else RGBColor(180, 83, 9)
                
                p2 = shape.text_frame.add_paragraph()
                p2.text = "Instituto Federal Fluminense (IFF) — Campus Bom Jesus do Itabapoana\\nCurso: LaTeX e Escrita Acadêmica"
                p2.font.size = Pt(12)
                p2.font.color.rgb = RGBColor(167, 139, 250) if is_dark else RGBColor(109, 40, 217)
            elif "Reconciliação" in text_val or "Abundâncias" in text_val or len(text_val) > 15:
                shape.text_frame.clear()
                p = shape.text_frame.paragraphs[0]
                p.text = f"AULA {num_str}: {titulo.upper()}"
                p.font.size = Pt(26)
                p.font.bold = True
                p.font.color.rgb = RGBColor(245, 158, 11) if is_dark else RGBColor(180, 83, 9)
                
                p2 = shape.text_frame.add_paragraph()
                p2.text = f"{subtitulo}\\nCurso: LaTeX e Escrita Acadêmica — Normas ABNT"
                p2.font.size = Pt(16)
                p2.font.color.rgb = RGBColor(34, 197, 94) if is_dark else RGBColor(21, 128, 61)
                
    slides_data = extract_slides_from_md(num_str)
    logo_path = "/home/pedro/Downloads/_cosmic_assets/iff/iff_bji_dark.png" if is_dark else "/home/pedro/Downloads/_cosmic_assets/iff/iff_bji_light.png"
    if not os.path.exists(logo_path): logo_path = "/home/pedro/Downloads/_cosmic_assets/iff/iffbomjesusvert-1.png"
    
    for idx_topic, sdata in enumerate(slides_data):
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        if os.path.exists(logo_path):
            slide.shapes.add_picture(logo_path, Inches(0.5), Inches(0.08), Inches(2.3), Inches(0.85))
            
        txBox = slide.shapes.add_textbox(Inches(12.0), Inches(7.0), Inches(1.0), Inches(0.5))
        tf_num = txBox.text_frame
        tf_num.text = str(idx_topic + 2)
        tf_num.paragraphs[0].font.size = Pt(12)
        tf_num.paragraphs[0].font.color.rgb = RGBColor(167, 139, 250) if is_dark else RGBColor(109, 40, 217)
        
        if slide.shapes.title:
            title_shape = slide.shapes.title
            title_shape.text = sdata['title']
            p = title_shape.text_frame.paragraphs[0]
            p.font.size = Pt(36)
            p.font.bold = True
            p.font.color.rgb = RGBColor(245, 158, 11) if is_dark else RGBColor(180, 83, 9)
            
        if len(slide.placeholders) > 1:
            body_shape = slide.placeholders[1]
            tf = body_shape.text_frame
            tf.clear()
            for j, item in enumerate(sdata['items']):
                p = tf.add_paragraph()
                if '[AZUL]' in item:
                    item_text = item.replace('[AZUL]', '').strip()
                    p.text = f"[Vale Lembrar] {item_text}"
                    p.font.color.rgb = RGBColor(96, 165, 250) if is_dark else RGBColor(37, 99, 235)
                elif j % 3 == 0:
                    p.text = f"[Importante] {item}"
                    p.font.color.rgb = RGBColor(34, 197, 94) if is_dark else RGBColor(21, 128, 61)
                elif j % 3 == 1:
                    p.text = f"[Prova/Trabalho] {item}"
                    p.font.color.rgb = RGBColor(167, 139, 250) if is_dark else RGBColor(109, 40, 217)
                else:
                    p.text = item
                    p.font.color.rgb = RGBColor(255, 255, 255) if is_dark else RGBColor(15, 23, 42)
                p.font.size = Pt(20)
                p.level = 0

    sldIdLst = prs.slides._sldIdLst
    obrigado_sld = sldIdLst[1]
    sldIdLst.remove(obrigado_sld)
    sldIdLst.append(obrigado_sld)
    
    with tempfile.TemporaryDirectory() as tmp_qr_dir:
        qr_path = os.path.join(tmp_qr_dir, "qrcode_transparente.png")
        generate_qr_transparent(url_qr, qr_path, is_dark_theme=is_dark)
        slide_capa.shapes.add_picture(qr_path, Inches(10.5), Inches(1.5), Inches(2.0), Inches(2.0))
        slide_final = prs.slides[-1]
        slide_final.shapes.add_picture(qr_path, Inches(10.2), Inches(4.3), Inches(2.4), Inches(2.4))

    os.makedirs(os.path.dirname(output_pptx_path), exist_ok=True)
    prs.save(output_pptx_path)
    return True"""
code = re.sub(r'def popule_pptx_institucional.*?return True', new_popule, code, flags=re.DOTALL)

with open('scripts/gerar_slides_e_notas.py', 'w', encoding='utf-8') as f:
    f.write(code)
