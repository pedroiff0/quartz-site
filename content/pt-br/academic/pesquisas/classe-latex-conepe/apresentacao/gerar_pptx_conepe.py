#!/usr/bin/env python3
"""
gerar_pptx_conepe.py
Gera a apresentação em PowerPoint (.pptx) para o CONEPE 2026 no formato widescreen 16:9
seguindo estritamente a identidade visual institucional slidesiff e o modelo consolidado
da engenharia para os slides finais.

Características:
- 17 slides espelhando com precisão o documento LaTeX (main.tex).
- Cabeçalho preserva proporção original (512:75) sem deformação horizontal.
- Metadados dinâmicos de seção e tópico no cabeçalho.
- Sumário institucional detalhado no Slide 2.
- Rodapé institucional com link mailto clicável em 'de Andrade, P. H. R., et al.'.
- Slide 16 com fundo temático Via Láctea Blur e card translúcido de agradecimento.
- Slide 17 com wallpaper Via Láctea limpo em tela cheia (sem blur).
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(DIR, "apresentacao-ifftese-conepe2026.pptx")
BANNER_IMG = os.path.join(DIR, "cabecalho-conepe2026.jpg")
QR_IMG = os.path.join(DIR, "qr-code-phrandrade.png")
BG_BLUR = os.path.join(DIR, "vialactea-blur.jpg")
BG_WALLPAPER = os.path.join(DIR, "via-lactea.jpg")

# Paleta Institucional IFF & CONEPE
C_GREEN = RGBColor(30, 130, 60)       # #1E823C (iffprimary)
C_DARK = RGBColor(15, 60, 30)         # #0F3C1E (iffdark)
C_TEXT = RGBColor(20, 20, 20)         # #141414 (ifftext)
C_SUBTEXT = RGBColor(90, 90, 90)      # #5A5A5A (iffsubtext)
C_RED = RGBColor(180, 30, 30)         # #B41E1E (iffred)
C_ALERT_BG = RGBColor(255, 238, 238)  # Fundo alerta claro (iffalertbg)
C_GREEN_BG = RGBColor(238, 252, 240)  # Fundo sucesso claro (iffgreenlight)
C_BLOCK_BG = RGBColor(245, 247, 248)  # Fundo bloco neutro (iffblockbg)
C_TEAL = RGBColor(43, 114, 131)       # CONEPE Teal (conepeteal)
C_TEAL_BG = RGBColor(235, 245, 248)   # Fundo Teal suave
C_WHITE = RGBColor(255, 255, 255)
C_BORDER = RGBColor(200, 205, 200)
C_DARK_CARD = RGBColor(22, 26, 24)    # Fundo card Slide 16

SW = 13.333
SH = 7.5

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(SW)
    prs.slide_height = Inches(SH)
    blank_layout = prs.slide_layouts[6]

    def add_base_decorations(slide, title_text, slide_num, total_slides=17, secao="", topico=""):
        # 1. Top Banner (Mantém proporção 512x75 -> ratio ~6.827:1)
        banner_h = 0.38
        banner_w = banner_h * (512.0 / 75.0)  # ~2.59 in
        if os.path.exists(BANNER_IMG):
            slide.shapes.add_picture(BANNER_IMG, Inches(0.6), Inches(0.12), width=Inches(banner_w), height=Inches(banner_h))

        # 2. Seção dinâmica no cabeçalho
        if secao:
            tb_sec = slide.shapes.add_textbox(Inches(0.6 + banner_w + 0.25), Inches(0.12), Inches(4.5), Inches(banner_h))
            tf_sec = tb_sec.text_frame
            tf_sec.word_wrap = True
            tf_sec.margin_left = tf_sec.margin_top = tf_sec.margin_right = tf_sec.margin_bottom = 0
            p = tf_sec.paragraphs[0]
            r_pipe = p.add_run()
            r_pipe.text = "|   "
            r_pipe.font.name = "Arial"
            r_pipe.font.size = Pt(11)
            r_pipe.font.color.rgb = C_BORDER

            r_sec = p.add_run()
            r_sec.text = secao
            r_sec.font.name = "Arial"
            r_sec.font.size = Pt(10)
            r_sec.font.bold = True
            r_sec.font.color.rgb = C_DARK

        # 3. Topico / Evento à direita
        tb_top = slide.shapes.add_textbox(Inches(6.5), Inches(0.12), Inches(SW - 7.1), Inches(banner_h))
        tf_top = tb_top.text_frame
        tf_top.word_wrap = True
        tf_top.margin_left = tf_top.margin_top = tf_top.margin_right = tf_top.margin_bottom = 0
        p_top = tf_top.paragraphs[0]
        p_top.alignment = PP_ALIGN.RIGHT
        
        r_evt = p_top.add_run()
        r_evt.text = "CONEPE 2026"
        r_evt.font.name = "Arial"
        r_evt.font.size = Pt(9.5)
        r_evt.font.bold = True
        r_evt.font.color.rgb = C_SUBTEXT

        if topico:
            r_p2 = p_top.add_run()
            r_p2.text = "   |   "
            r_p2.font.name = "Arial"
            r_p2.font.size = Pt(9.5)
            r_p2.font.color.rgb = C_BORDER

            r_t = p_top.add_run()
            r_t.text = topico
            r_t.font.name = "Arial"
            r_t.font.size = Pt(9.5)
            r_t.font.bold = True
            r_t.font.color.rgb = C_GREEN

        # 4. Linha verde abaixo do cabeçalho
        rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(0.55), Inches(SW - 1.2), Inches(0.015))
        rule.fill.solid()
        rule.fill.fore_color.rgb = C_GREEN
        rule.line.color.rgb = C_GREEN

        # 5. Título do Slide
        tb_title = slide.shapes.add_textbox(Inches(0.6), Inches(0.66), Inches(SW - 1.2), Inches(0.58))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p = tf_title.paragraphs[0]
        p.text = title_text
        p.font.name = "Arial"
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = C_DARK

        # 6. Linha verde acima do rodapé
        f_rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.6), Inches(7.05), Inches(SW - 1.2), Inches(0.015))
        f_rule.fill.solid()
        f_rule.fill.fore_color.rgb = C_GREEN
        f_rule.line.color.rgb = C_GREEN

        # 7. Rodapé Institucional em 3 colunas
        # Autor (Esquerda com Link Mailto)
        tb_f_left = slide.shapes.add_textbox(Inches(0.6), Inches(7.08), Inches(4.5), Inches(0.35))
        tf_f_left = tb_f_left.text_frame
        tf_f_left.word_wrap = True
        tf_f_left.margin_left = tf_f_left.margin_top = tf_f_left.margin_right = tf_f_left.margin_bottom = 0
        p_fl = tf_f_left.paragraphs[0]
        r_author = p_fl.add_run()
        r_author.text = "de Andrade, P. H. R., et al."
        r_author.font.name = "Arial"
        r_author.font.size = Pt(9.5)
        r_author.font.bold = True
        r_author.font.color.rgb = C_TEXT
        r_author.hyperlink.address = "mailto:pedroiff0@gmail.com"

        # Projeto / Apresentação (Centro)
        tb_f_mid = slide.shapes.add_textbox(Inches(5.0), Inches(7.08), Inches(3.333), Inches(0.35))
        tf_f_mid = tb_f_mid.text_frame
        tf_f_mid.word_wrap = True
        tf_f_mid.margin_left = tf_f_mid.margin_top = tf_f_mid.margin_right = tf_f_mid.margin_bottom = 0
        p_fm = tf_f_mid.paragraphs[0]
        p_fm.alignment = PP_ALIGN.CENTER
        r_proj = p_fm.add_run()
        r_proj.text = "Classe LaTeX — CONEPE 2026"
        r_proj.font.name = "Arial"
        r_proj.font.size = Pt(9.5)
        r_proj.font.bold = True
        r_proj.font.color.rgb = C_DARK
        r_proj.hyperlink.address = "https://phrandrade.com"

        # Paginação (Direita)
        tb_f_right = slide.shapes.add_textbox(Inches(8.5), Inches(7.08), Inches(SW - 9.1), Inches(0.35))
        tf_f_right = tb_f_right.text_frame
        tf_f_right.word_wrap = True
        tf_f_right.margin_left = tf_f_right.margin_top = tf_f_right.margin_right = tf_f_right.margin_bottom = 0
        p_fr = tf_f_right.paragraphs[0]
        p_fr.alignment = PP_ALIGN.RIGHT
        r_num = p_fr.add_run()
        r_num.text = f"{slide_num} / {total_slides}"
        r_num.font.name = "Arial"
        r_num.font.size = Pt(9.5)
        r_num.font.bold = True
        r_num.font.color.rgb = C_SUBTEXT

    def add_card(slide, left, top, width, height, title, items, bg_color=C_WHITE, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=4):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.0)

        tb = slide.shapes.add_textbox(Inches(left + 0.22), Inches(top + 0.16), Inches(width - 0.44), Inches(height - 0.32))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.name = "Arial"
        p0.font.size = Pt(font_size + 1.5)
        p0.font.bold = True
        p0.font.color.rgb = title_color
        p0.space_after = Pt(space_after + 3)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.name = "Arial"
            p.font.size = Pt(font_size)
            p.font.color.rgb = C_TEXT
            p.space_after = Pt(space_after)

    # -------------------------------------------------------------------------
    # SLIDE 1: CAPA OFICIAL (SEM DEFORMAÇÃO)
    # -------------------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    banner_h1 = 0.85
    banner_w1 = banner_h1 * (512.0 / 75.0)  # ~5.80 in
    banner_l1 = (SW - banner_w1) / 2.0
    if os.path.exists(BANNER_IMG):
        s1.shapes.add_picture(BANNER_IMG, Inches(banner_l1), Inches(0.40), width=Inches(banner_w1), height=Inches(banner_h1))

    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(SW - 2.0), Inches(5.6))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "Classe LaTeX: Otimização da Formatação de Trabalhos Acadêmicos"
    r.font.name = "Arial"
    r.font.size = Pt(24)
    r.font.bold = True
    r.font.color.rgb = C_DARK
    p.space_after = Pt(6)

    p = tf1.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "Automação Normativa da ABNT e Abstração Estrutural com ifftese.cls e macros.sty"
    r.font.name = "Arial"
    r.font.size = Pt(14)
    r.font.color.rgb = C_TEAL
    p.space_after = Pt(20)

    p = tf1.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "Pedro Henrique Rocha de Andrade¹*, Ana Cecília Soja¹,\nMaria Luiza Linhares Dantas², Antônio Manoel de Oliveira Figueiredo¹"
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = C_TEXT
    p.space_after = Pt(6)

    p = tf1.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "¹Instituto Federal Fluminense — Campus Bom Jesus do Itabapoana\n²Pontifícia Universidade Católica de Chile (PUC-Chile)"
    r.font.name = "Arial"
    r.font.size = Pt(10.5)
    r.font.color.rgb = C_SUBTEXT
    p.space_after = Pt(4)

    p = tf1.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "*pedroiff0@gmail.com"
    r.font.name = "Arial"
    r.font.size = Pt(10.5)
    r.font.bold = True
    r.font.color.rgb = C_GREEN
    r.hyperlink.address = "mailto:pedroiff0@gmail.com"
    p.space_after = Pt(16)

    p = tf1.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "Apoio Institucional e Financeiro:\nCNPq (Projeto 129985/2025-2)   |   Instituto Federal Fluminense (IFF Bom Jesus)"
    r.font.name = "Arial"
    r.font.size = Pt(10.5)
    r.font.bold = True
    r.font.color.rgb = C_DARK
    p.space_after = Pt(12)

    p = tf1.add_paragraph()
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "CONEPE 2026 — XIII Congresso de Ensino, Pesquisa e Extensão (22 a 24 de Setembro de 2026)"
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = C_SUBTEXT

    # -------------------------------------------------------------------------
    # SLIDE 2: ESTRUTURA DA APRESENTAÇÃO (SUMÁRIO)
    # -------------------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s2, "Estrutura da Apresentação", 2, secao="Sumário", topico="Visão Geral")

    sumario_itens_left = [
        ("01. Contextualização & O Paradoxo do Pesquisador", "A odisseia da formatação no Word, custos operacionais comprovados e a perda de foco na geração de ciência."),
        ("02. O Labirinto Normativo: ABNT & IBGE", "Exigências geométricas da NBR 14724, formatação bibliográfica da NBR 6023, sumário NBR 6027 e regras do IBGE."),
        ("03. Princípio dos Paradigmas: WYSIWYG vs. WYSIWYM", "Análise comparativa algorítmica entre processadores de texto convencionais e o LaTeX (algoritmo de Knuth-Plass).")
    ]
    sumario_itens_right = [
        ("04. A Solução Proposta: ifftese.cls e macros.sty", "Arquitetura da classe institucional oficial, herança do ecossistema abntex2 e biblioteca de abstração em alto nível."),
        ("05. Resultados Práticos e Validação", "Switches de configuração semânticos, geração de pré-texto com comando único e blindagem do pós-texto."),
        ("06. Conclusões e Desdobramentos Futuros", "Ganhos de produtividade acadêmica comprovados e desenvolvimento da interface web para compilação por formulários.")
    ]

    card_y = 1.35
    for title, desc in sumario_itens_left:
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(card_y), Inches(5.85), Inches(1.65))
        c.fill.solid()
        c.fill.fore_color.rgb = C_WHITE
        c.line.color.rgb = C_GREEN
        c.line.width = Pt(1.0)
        tb = s2.shapes.add_textbox(Inches(0.8), Inches(card_y + 0.15), Inches(5.45), Inches(1.35))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_DARK
        p.space_after = Pt(4)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT
        card_y += 1.82

    card_y = 1.35
    for title, desc in sumario_itens_right:
        c = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.85), Inches(card_y), Inches(5.85), Inches(1.65))
        c.fill.solid()
        c.fill.fore_color.rgb = C_WHITE
        c.line.color.rgb = C_TEAL
        c.line.width = Pt(1.0)
        tb = s2.shapes.add_textbox(Inches(7.05), Inches(card_y + 0.15), Inches(5.45), Inches(1.35))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_TEAL
        p.space_after = Pt(4)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT
        card_y += 1.82

    # -------------------------------------------------------------------------
    # SLIDE 3: O PESADELO DA MADRUGADA: A ODISSEIA NO WORD
    # -------------------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s3, "O Pesadelo da Madrugada: A Odisseia da Formatação no Word", 3, secao="Contexto", topico="O Problema")

    # Left Context & Alert Card
    tb3_ctx = s3.shapes.add_textbox(Inches(0.6), Inches(1.35), Inches(5.85), Inches(1.0))
    tf3_ctx = tb3_ctx.text_frame
    tf3_ctx.word_wrap = True
    p = tf3_ctx.paragraphs[0]
    p.text = "Cenário das 23h59 (Véspera de Entrega Final):"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_DARK
    p.space_after = Pt(3)
    p2 = tf3_ctx.add_paragraph()
    p2.text = "• O orientador solicita o acréscimo de 3 linhas pontuais na Introdução.\n• O autor insere o texto e aperta 'Enter'..."
    p2.font.name = "Arial"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_TEXT

    add_card(s3, 0.6, 2.50, 5.85, 4.35, "O Efeito Dominó Catastrófico", [
        "A Figura 4 salta misteriosamente 3 páginas adiante, gerando enorme vazio em branco;",
        "A legenda se desprende da ilustração e fica órfã no topo da folha seguinte;",
        "Surge o clássico erro: 'Erro! Indicador não definido.' nas referências cruzadas;",
        "A lista numérica de citações perde a ordem sequencial [14, 2, 8, 1];",
        "O autor entra em desespero ajustando espaçamentos manuais até o amanhecer."
    ], bg_color=C_ALERT_BG, border_color=C_RED, title_color=C_RED, font_size=10.5, space_after=6)

    # Right Diagnostic Card
    add_card(s3, 6.85, 1.35, 5.85, 5.50, "O Custo Operacional Comprovado", [
        "Quebras de seção corrompem silenciosamente a paginação pré-textual;",
        "Margens oscilam sem intervenção do autor ao colar textos de outras fontes;",
        "O sumário desalinha os números de página em relação aos pontilhados (.....);",
        "Títulos perdem hierarquia e padrão de fontes após salvamento automático;",
        "Diagnóstico Comprovado na Academia:",
        "Até 70% da carga horária de redação científica é desperdiçada corrigindo inconsistências de layout da ferramenta, não gerando ciência."
    ], bg_color=C_BLOCK_BG, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 4: O PARADOXO DO PESQUISADOR ACADÊMICO
    # -------------------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s4, "O Paradoxo do Pesquisador Acadêmico", 4, secao="Contexto", topico="O Paradoxo")

    add_card(s4, 0.6, 1.35, 5.85, 4.10, "O Objetivo Científico Central", [
        "Formulação rigorosa de hipóteses e questionamentos científicos;",
        "Coleta, tratamento e modelagem matemática de dados empíricos;",
        "Redação concisa, precisa e geração de impacto científico relevante;",
        "Contribuição concreta para o avanço da sociedade e da tecnologia."
    ], bg_color=C_GREEN_BG, border_color=C_GREEN, title_color=C_DARK, font_size=11, space_after=8)

    add_card(s4, 6.85, 1.35, 5.85, 4.10, "A Realidade Burocrática Improdutiva", [
        "Medir manualmente margens de 3,0 cm e 2,0 cm na régua visual da tela;",
        "Batalhar horas a fio para ocultar o número de página na capa e resumo;",
        "Repadronizar estilos de títulos corrompidos a cada atualização;",
        "Reformatar espaçamentos verticais manuais a cada ciclo de revisão."
    ], bg_color=C_ALERT_BG, border_color=C_RED, title_color=C_RED, font_size=11, space_after=8)

    # Bottom Question Banner
    card_bot = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.65), Inches(SW - 1.2), Inches(1.20))
    card_bot.fill.solid()
    card_bot.fill.fore_color.rgb = C_DARK
    card_bot.line.color.rgb = C_GREEN
    card_bot.line.width = Pt(1.2)
    tb_bot = s4.shapes.add_textbox(Inches(0.8), Inches(5.80), Inches(SW - 1.6), Inches(0.90))
    tf_bot = tb_bot.text_frame
    tf_bot.word_wrap = True
    p = tf_bot.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r1 = p.add_run()
    r1.text = "Pergunta Norteadora: "
    r1.font.name = "Arial"
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p.add_run()
    r2.text = "Como blindar o pesquisador das armadilhas normativas sem exigir dele conhecimento avançado em programação?"
    r2.font.name = "Arial"
    r2.font.size = Pt(13)
    r2.font.color.rgb = C_WHITE

    # -------------------------------------------------------------------------
    # SLIDE 5: AS NORMAS REGENTES I: ABNT NBR 14724
    # -------------------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s5, "As Normas Regentes I: ABNT NBR 14724", 5, secao="Normas", topico="NBR 14724")

    add_card(s5, 0.6, 1.35, 5.85, 3.60, "Geometria e Margens Estritas", [
        "Anverso: Esquerda e Topo: 3,0 cm  |  Direita e Base: 2,0 cm;",
        "Verso: Margens rigorosamente espelhadas para acomodar encadernação;",
        "Corpo do Trabalho: Fonte tamanho 12 para texto regular;",
        "Citações Longas (> 3 linhas): Recuo obrigatório de 4,0 cm da margem esquerda, fonte tamanho 10 e espaçamento simples entre linhas."
    ], bg_color=C_WHITE, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    # Note below left card
    c_note = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.15), Inches(5.85), Inches(1.70))
    c_note.fill.solid()
    c_note.fill.fore_color.rgb = C_BLOCK_BG
    c_note.line.color.rgb = C_BORDER
    c_note.line.width = Pt(1.0)
    tb_n = s5.shapes.add_textbox(Inches(0.8), Inches(5.30), Inches(5.45), Inches(1.40))
    tf_n = tb_n.text_frame
    tf_n.word_wrap = True
    p = tf_n.paragraphs[0]
    p.text = "Impacto da Geometria no Processo:"
    p.font.name = "Arial"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_DARK
    p.space_after = Pt(3)
    p2 = tf_n.add_paragraph()
    p2.text = "Variações milimétricas em margens alteram o volume de páginas, deslocando finais de seções e provocando refações completas de sumários."
    p2.font.name = "Arial"
    p2.font.size = Pt(10)
    p2.font.color.rgb = C_TEXT

    add_card(s5, 6.85, 1.35, 5.85, 5.50, "A Pegadinha da Paginação Acadêmica", [
        "Contagem Pré-Textual:",
        "As folhas pré-textuais são contadas a partir da Folha de Rosto (folha 2);",
        "Impressão da Numeração Física:",
        "O número da página só é impresso a partir da primeira folha da parte textual (Introdução);",
        "A Fragilidade no Word:",
        "Exige quebras de seção delicadas que corrompem numerações com qualquer exclusão inadvertida;",
        "A Solução na ifftese.cls:",
        "Todo o gerenciamento de paginação e contagem oculta é processado de forma automática e transparente na transição textual."
    ], bg_color=C_ALERT_BG, border_color=C_RED, title_color=C_RED, font_size=10.5, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 6: AS NORMAS REGENTES II: NBR 6023 E NBR 6027
    # -------------------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s6, "As Normas Regentes II: NBR 6023 e NBR 6027", 6, secao="Normas", topico="NBR 6023 & 6027")

    add_card(s6, 0.6, 1.35, 5.85, 5.50, "NBR 6023 (Referências Bibliográficas)", [
        "Alinhamento Estrito à Margem Esquerda:",
        "As referências nunca devem ser justificadas, evitando espaçamentos tipográficos artificiais;",
        "Espaçamento Padronizado:",
        "Espaçamento simples no interior da referência e 1 linha em branco separando as referências;",
        "Destaque Tipográfico Uniforme:",
        "O recurso tipográfico (negrito, itálico ou sublinhado) é aplicado exclusivamente no título da obra;",
        "Sistema de Chamada Consistente:",
        "Adoção homogênea de autor-data ou numérico estrito em todo o corpo do trabalho."
    ], bg_color=C_WHITE, border_color=C_TEAL, title_color=C_TEAL, font_size=10.5, space_after=6)

    add_card(s6, 6.85, 1.35, 5.85, 5.50, "NBR 6027 (Sumário Institucional)", [
        "Identidade Tipográfica Rigorosa:",
        "O sumário deve espelhar com exatidão matemática a grafia das seções no texto:",
        "  • 1 SEÇÃO PRIMÁRIA (CAIXA ALTA NEGRITO)",
        "  • 1.1 Seção Secundária (Caixa Baixa Normal)",
        "  • 1.1.1 Seção Terciária (Caixa Baixa Itálico)",
        "Alinhamento por Linha Pontilhada:",
        "Pontilhados perfeitos conectando cada título à respectiva página física;",
        "Automação na ifftese.cls:",
        "O sumário é compilado de forma autônoma sem risco de divergência de títulos ou de paginação."
    ], bg_color=C_WHITE, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 7: DIFERENCIAÇÃO: TABELAS (IBGE) VS. QUADROS (ABNT)
    # -------------------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s7, "Diferenciação Normativa: Tabelas (IBGE) vs. Quadros (ABNT)", 7, secao="Normas", topico="IBGE vs ABNT")

    add_card(s7, 0.6, 1.35, 5.85, 4.10, "Tabelas (Normas do IBGE)", [
        "Natureza dos Dados: Informações predominantemente numéricas e estatísticas;",
        "Geometria Específica: Laterais abertas (sem bordas verticais nas extremidades externas);",
        "Linhas Horizontais: Presentes no topo superior, cabeçalho e na base inferior;",
        "Lista Pré-Textual: Alimenta automaticamente a Lista de Tabelas institucional."
    ], bg_color=C_GREEN_BG, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    add_card(s7, 6.85, 1.35, 5.85, 4.10, "Quadros (Norma ABNT)", [
        "Natureza dos Dados: Conteúdo conceitual, qualitativo, descritivo ou textual;",
        "Geometria Fechada: Moldura totalmente fechada nos quatro lados;",
        "Grades Internas: Divisórias verticais e horizontais completas entre todas as células;",
        "Lista Pré-Textual: Exige obrigatoriamente a Lista de Quadros separada."
    ], bg_color=C_ALERT_BG, border_color=C_RED, title_color=C_RED, font_size=10.5, space_after=6)

    # Bottom Error Card
    card_bot7 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.65), Inches(SW - 1.2), Inches(1.20))
    card_bot7.fill.solid()
    card_bot7.fill.fore_color.rgb = C_ALERT_BG
    card_bot7.line.color.rgb = C_RED
    card_bot7.line.width = Pt(1.2)
    tb_b7 = s7.shapes.add_textbox(Inches(0.8), Inches(5.75), Inches(SW - 1.6), Inches(0.95))
    tf_b7 = tb_b7.text_frame
    tf_b7.word_wrap = True
    p = tf_b7.paragraphs[0]
    r1 = p.add_run()
    r1.text = "O Erro Crítico na Academia: "
    r1.font.name = "Arial"
    r1.font.size = Pt(11)
    r1.font.bold = True
    r1.font.color.rgb = C_RED
    r2 = p.add_run()
    r2.text = "Tratar tabelas e quadros como sinônimos acarreta penalizações formais em bancas examinadoras. A classe ifftese.cls automatiza a distinção visual e funcional através das macros \\inserirtabela e \\inserirquadro."
    r2.font.name = "Arial"
    r2.font.size = Pt(10)
    r2.font.color.rgb = C_TEXT

    # -------------------------------------------------------------------------
    # SLIDE 8: O PRINCÍPIO DOS PARADIGMAS: WYSIWYG VS. WYSIWYM
    # -------------------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s8, "O Princípio dos Paradigmas: WYSIWYG vs. WYSIWYM", 8, secao="Paradigmas", topico="Knuth-Plass")

    add_card(s8, 0.6, 1.35, 5.85, 5.50, "WYSIWYG: Microsoft Word", [
        "Conceito Operacional: 'What You See Is What You Get';",
        "Renderização Síncrona:",
        "O processador renderiza gráficos e cálculos geométricos simultaneamente à digitação do texto;",
        "Algoritmo Local 'Guloso' (Greedy):",
        "Ajustes pontuais no início do documento propagam instabilidades em cascata pelas centenas de páginas seguintes;",
        "Instabilidade Crítica:",
        "Gargalos severos de desempenho e desconfigurações crônicas em documentos extensos contendo figuras e equações flutuantes."
    ], bg_color=C_ALERT_BG, border_color=C_RED, title_color=C_RED, font_size=10.5, space_after=6)

    add_card(s8, 6.85, 1.35, 5.85, 5.50, "WYSIWYM: O Sistema LaTeX", [
        "Conceito Operacional: 'What You See Is What You Mean';",
        "Fundamentação Histórica:",
        "Criado por Donald Knuth (1977) e expandido por Leslie Lamport (1984);",
        "Separação Estrita de Papéis:",
        "O autor concentra-se na semântica do conteúdo; o compilador projeta o layout global ideal;",
        "Algoritmo Knuth-Plass:",
        "Quebras de parágrafos otimizadas globalmente via programação dinâmica, eliminando rios de espaços em branco e garantindo simetria tipográfica."
    ], bg_color=C_GREEN_BG, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 9: POR QUE O LATEX É A RESPOSTA (E O DILEMA DA CURVA INICIAL)
    # -------------------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s9, "Por Que o LaTeX é a Resposta (e o dilema da curva inicial)", 9, secao="Paradigmas", topico="Curva de Entrada")

    add_card(s9, 0.6, 1.35, 5.85, 4.10, "As Vantagens Inquestionáveis", [
        "Padrão consolidado internacionalmente nas ciências exatas (arXiv, IEEE, ACM, Springer, Nature);",
        "Qualidade tipográfica inigualável em fórmulas matemáticas complexas;",
        "Geração infalível de referências cruzadas através de arquivos auxiliares (.aux);",
        "Separação cristalina entre conteúdo textual e arte-final."
    ], bg_color=C_GREEN_BG, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    add_card(s9, 6.85, 1.35, 5.85, 4.10, "A Barreira de Entrada Institucional", [
        "Curva de aprendizado inicial íngreme para pesquisadores em início de formação;",
        "Configuração de dezenas de pacotes gráficos e de formatação conflitantes;",
        "Mensagens de erro de compilação intimidadoras para não-programadores;",
        "Necessidade recorrente de adequar classes genéricas às normas locais da ABNT."
    ], bg_color=C_ALERT_BG, border_color=C_RED, title_color=C_RED, font_size=10.5, space_after=6)

    # Bottom Solution Card
    card_bot9 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(5.65), Inches(SW - 1.2), Inches(1.20))
    card_bot9.fill.solid()
    card_bot9.fill.fore_color.rgb = C_DARK
    card_bot9.line.color.rgb = C_GREEN
    card_bot9.line.width = Pt(1.2)
    tb_b9 = s9.shapes.add_textbox(Inches(0.8), Inches(5.80), Inches(SW - 1.6), Inches(0.90))
    tf_b9 = tb_b9.text_frame
    tf_b9.word_wrap = True
    p = tf_b9.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r1 = p.add_run()
    r1.text = "A Solução Desenvolvida: "
    r1.font.name = "Arial"
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN
    r2 = p.add_run()
    r2.text = "Uma camada de abstração institucional desenvolvida sob medida que esconde a complexidade e expõe comandos simples e intuitivos."
    r2.font.name = "Arial"
    r2.font.size = Pt(13)
    r2.font.color.rgb = C_WHITE

    # -------------------------------------------------------------------------
    # SLIDE 10: A SOLUÇÃO PROPOSTA: IFFTESE.CLS E MACROS.STY
    # -------------------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s10, "A Solução Proposta: ifftese.cls e macros.sty", 10, secao="Arquitetura", topico="ifftese.cls & macros.sty")

    # Top Objective Box
    c_obj = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.35), Inches(SW - 1.2), Inches(1.40))
    c_obj.fill.solid()
    c_obj.fill.fore_color.rgb = C_BLOCK_BG
    c_obj.line.color.rgb = C_GREEN
    c_obj.line.width = Pt(1.2)
    tb_o = s10.shapes.add_textbox(Inches(0.8), Inches(1.48), Inches(SW - 1.6), Inches(1.15))
    tf_o = tb_o.text_frame
    tf_o.word_wrap = True
    p = tf_o.paragraphs[0]
    p.text = "Objetivo Central do Projeto:"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_DARK
    p.space_after = Pt(3)
    p2 = tf_o.add_paragraph()
    p2.text = "Desenvolver uma classe tipográfica oficial (ifftese.cls) e um pacote de extensão semântica (macros.sty) para a comunidade do Instituto Federal Fluminense, assegurando conformidade estrita às normas ABNT e IBGE com máxima simplicidade para o autor."
    p2.font.name = "Arial"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_TEXT

    add_card(s10, 0.6, 2.95, 5.85, 3.90, "Classe ifftese.cls", [
        "Gerenciamento milimétrico de margens e geometria da página;",
        "Geração automática de capas, lombadas e folhas de aprovação oficiais;",
        "Cabeçalhos institucionais e paginação oculta/visível inteligente;",
        "Construída sobre a base consagrada do ecossistema abntex2."
    ], bg_color=C_WHITE, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    add_card(s10, 6.85, 2.95, 5.85, 3.90, "Extensão macros.sty", [
        "Abstração de comandos complexos em instruções simplificadas de linha única;",
        "Diferenciação nativa automática entre tabelas (IBGE) e quadros (ABNT);",
        "Alimentação automatizada de todas as listas pré-textuais;",
        "Manipulação segura e transparente dos contadores de apêndices e anexos."
    ], bg_color=C_WHITE, border_color=C_TEAL, title_color=C_TEAL, font_size=10.5, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 11: METODOLOGIA DE DESENVOLVIMENTO EM TRÊS ETAPAS
    # -------------------------------------------------------------------------
    s11 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s11, "Metodologia de Desenvolvimento em Três Etapas", 11, secao="Metodologia", topico="3 Etapas")

    # 3 Steps Flow
    steps = [
        ("Etapa 1: Mapeamento Normativo", "Sistematização rigorosa das NBRs 14724, 6023, 6027 e normas tabulares do IBGE em matriz de requisitos formais.", C_GREEN, C_DARK),
        ("Etapa 2: Construção das Macros", "Encapsulamento dos ambientes TeX e desenvolvimento da camada de abstração com validação de parâmetros.", C_TEAL, C_TEAL),
        ("Etapa 3: Template Unificado", "Disponibilização do modelo institucional main.tex pré-configurado, validado em múltiplos compiladores.", C_GREEN, C_DARK)
    ]
    step_x = 0.6
    for title, desc, border_c, title_c in steps:
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(step_x), Inches(1.35), Inches(3.85), Inches(2.20))
        c.fill.solid()
        c.fill.fore_color.rgb = C_WHITE
        c.line.color.rgb = border_c
        c.line.width = Pt(1.2)
        tb = s11.shapes.add_textbox(Inches(step_x + 0.18), Inches(1.50), Inches(3.49), Inches(1.90))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = title_c
        p.space_after = Pt(6)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT
        step_x += 4.14

    # 3 Pillars
    pillars = [
        ("Ambientes de Teste", "Testado e homologado no ecossistema TeX Live com os motores pdflatex e bibtex em Linux, Windows e macOS."),
        ("Acessibilidade Universal", "Compatibilidade total com compiladores em nuvem (Overleaf, TeXPage) e ambientes de desenvolvimento locais."),
        ("Engenharia de Software", "Desenvolvimento centrado na experiência do usuário (UX), eliminando atrito técnico na produção de artigos e teses.")
    ]
    pill_x = 0.6
    for title, desc in pillars:
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(pill_x), Inches(3.85), Inches(3.85), Inches(3.00))
        c.fill.solid()
        c.fill.fore_color.rgb = C_BLOCK_BG
        c.line.color.rgb = C_BORDER
        c.line.width = Pt(1.0)
        tb = s11.shapes.add_textbox(Inches(pill_x + 0.18), Inches(4.00), Inches(3.49), Inches(2.65))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Arial"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_DARK
        p.space_after = Pt(6)
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = "Arial"
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_TEXT
        pill_x += 4.14

    # -------------------------------------------------------------------------
    # SLIDE 12: RESULTADOS: VARIÁVEIS SEMÂNTICAS E PRÉ-TEXTO
    # -------------------------------------------------------------------------
    s12 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s12, "Resultados: Variáveis Semânticas e Pré-Texto", 12, secao="Resultados", topico="Pré-Texto")

    add_card(s12, 0.6, 1.35, 5.85, 5.50, "Switches de Configuração (Flags Booleanas)", [
        "\\frenteVerso: Alterna dinamicamente entre margens simples ou espelhadas para encadernação;",
        "\\capaiff: Aplica o layout institucional padronizado do Instituto Federal Fluminense;",
        "\\corlink: Controle instantâneo de contraste de hiperlinks (azul para tela, preto para impressão oficial);",
        "\\sumarioEscada: Ativa a formatação hierárquica automática conforme a norma ABNT;",
        "Metadados Simples no Preâmbulo:",
        "\\autor{...}, \\titulo{...}, \\orientador{...}, \\local{...}, \\data{...}"
    ], bg_color=C_WHITE, border_color=C_TEAL, title_color=C_TEAL, font_size=10.5, space_after=6)

    # Right Code Box
    c_code12 = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.85), Inches(1.35), Inches(5.85), Inches(5.50))
    c_code12.fill.solid()
    c_code12.fill.fore_color.rgb = C_BLOCK_BG
    c_code12.line.color.rgb = C_DARK
    c_code12.line.width = Pt(1.2)

    tb12_c = s12.shapes.add_textbox(Inches(7.10), Inches(1.55), Inches(5.35), Inches(5.10))
    tf12_c = tb12_c.text_frame
    tf12_c.word_wrap = True
    p = tf12_c.paragraphs[0]
    p.text = "Geração Autônoma com Comandos Únicos"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_DARK
    p.space_after = Pt(8)

    p2 = tf12_c.add_paragraph()
    p2.text = "O autor não formata capas manualmente:"
    p2.font.name = "Arial"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = C_TEXT
    p2.space_after = Pt(6)

    # Code Box Inner
    p_code = tf12_c.add_paragraph()
    p_code.text = "\\capa\n\\contracapa\n\\folhadeaprovacao"
    p_code.font.name = "Courier New"
    p_code.font.size = Pt(12)
    p_code.font.bold = True
    p_code.font.color.rgb = C_GREEN
    p_code.space_after = Pt(14)

    p3 = tf12_c.add_paragraph()
    p3.text = "Garantias Automáticas do Compilador:\n• Espaçamentos milimétricos rigorosos da NBR 14724;\n• Contagem oculta de páginas ativada automaticamente;\n• Zero intervenção manual em arquivos auxiliares."
    p3.font.name = "Arial"
    p3.font.size = Pt(10.5)
    p3.font.color.rgb = C_TEXT

    # -------------------------------------------------------------------------
    # SLIDE 13: RESULTADOS: ELEMENTOS TEXTUAIS (\inserirfigura)
    # -------------------------------------------------------------------------
    s13 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s13, "Resultados: Elementos Textuais (\\inserirfigura)", 13, secao="Resultados", topico="\\inserirfigura")

    # Left: Traditional LaTeX
    c_trad = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.6), Inches(1.35), Inches(5.85), Inches(5.50))
    c_trad.fill.solid()
    c_trad.fill.fore_color.rgb = C_ALERT_BG
    c_trad.line.color.rgb = C_RED
    c_trad.line.width = Pt(1.2)
    tb_tr = s13.shapes.add_textbox(Inches(0.85), Inches(1.55), Inches(5.35), Inches(5.10))
    tf_tr = tb_tr.text_frame
    tf_tr.word_wrap = True
    p = tf_tr.paragraphs[0]
    p.text = "LaTeX Convencional (8 a 10 linhas propensas a erro)"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_RED
    p.space_after = Pt(8)

    p_code_tr = tf_tr.add_paragraph()
    p_code_tr.text = "\\begin{figure}[htbp]\n  \\centering\n  \\caption{Diagrama de Fases}\n  \\includegraphics[width=0.7\\textwidth]{fig.png}\n  \\vspace{0.1cm}\n  {\\footnotesize Fonte: Autor (2026).}\n  \\label{fig:fases}\n\\end{figure}"
    p_code_tr.font.name = "Courier New"
    p_code_tr.font.size = Pt(10)
    p_code_tr.font.bold = True
    p_code_tr.font.color.rgb = C_DARK
    p_code_tr.space_after = Pt(12)

    p_r_tr = tf_tr.add_paragraph()
    p_r_tr.text = "Riscos Crônicos no Modelo Convencional:\n• Esquecimento de centralização;\n• Inversão de posições entre legenda e fonte;\n• Rótulos desacoplados da Lista de Ilustrações."
    p_r_tr.font.name = "Arial"
    p_r_tr.font.size = Pt(10)
    p_r_tr.font.color.rgb = C_TEXT

    # Right: macros.sty
    c_mac = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.85), Inches(1.35), Inches(5.85), Inches(5.50))
    c_mac.fill.solid()
    c_mac.fill.fore_color.rgb = C_GREEN_BG
    c_mac.line.color.rgb = C_GREEN
    c_mac.line.width = Pt(1.2)
    tb_mc = s13.shapes.add_textbox(Inches(7.10), Inches(1.55), Inches(5.35), Inches(5.10))
    tf_mc = tb_mc.text_frame
    tf_mc.word_wrap = True
    p = tf_mc.paragraphs[0]
    p.text = "Com o macros.sty (1 linha expressiva e blindada)"
    p.font.name = "Arial"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_DARK
    p.space_after = Pt(8)

    p_code_mc = tf_mc.add_paragraph()
    p_code_mc.text = "\\inserirfigura[0.7]{fig.png}\n  {Diagrama de Fases}\n  {Autor (2026)}{fig:fases}"
    p_code_mc.font.name = "Courier New"
    p_code_mc.font.size = Pt(11)
    p_code_mc.font.bold = True
    p_code_mc.font.color.rgb = C_GREEN
    p_code_mc.space_after = Pt(14)

    p_g_mc = tf_mc.add_paragraph()
    p_g_mc.text = "Garantias Automáticas Blindadas:\n• Legenda posicionada rigorosamente no topo (norma ABNT);\n• Fonte tipográfica em tamanho menor no rodapé da imagem;\n• Centralização horizontal padronizada;\n• Geração de rótulo e envio imediato à Lista de Ilustrações."
    p_g_mc.font.name = "Arial"
    p_g_mc.font.size = Pt(10)
    p_g_mc.font.color.rgb = C_TEXT

    # -------------------------------------------------------------------------
    # SLIDE 14: RESULTADOS: AUTOMAÇÃO IBGE E PÓS-TEXTO
    # -------------------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s14, "Resultados: Automação IBGE e Blindagem do Pós-Texto", 14, secao="Resultados", topico="Tabelas & Quadros")

    add_card(s14, 0.6, 1.35, 5.85, 5.50, "Tabelas e Quadros Parametrizados", [
        "Macro \\inserirtabela[escala]{arquivo}{legenda}{fonte}{label}:",
        "  • Constrói automaticamente as laterais abertas conforme padrão IBGE;",
        "  • Direciona o metadado para a Lista de Tabelas pré-textual.",
        "Macro \\inserirquadro[escala]{arquivo}{legenda}{fonte}{label}:",
        "  • Constrói moldura totalmente fechada nos quatro lados conforme norma ABNT;",
        "  • Alimenta a Lista de Quadros independente.",
        "Benefício ao Autor:",
        "O autor não precisa lembrar de parâmetros de bordas: a macro aplica as regras."
    ], bg_color=C_WHITE, border_color=C_GREEN, title_color=C_DARK, font_size=10.5, space_after=6)

    add_card(s14, 6.85, 1.35, 5.85, 5.50, "Robustez e Blindagem Pós-Textual", [
        "Apêndices e Anexos:",
        "Transição dinâmica dos contadores numéricos para letras alfabéticas (1, 2 → A, B);",
        "Preservação da Hierarquia do Sumário:",
        "A transição alfabética não desconfigura os níveis hierárquicos do sumário geral;",
        "Listagens Especiais:",
        "Suporte transparente a erratas e listagens dinâmicas de equações;",
        "Conformidade Bibliográfica:",
        "Compatibilidade plena com a biblioteca abntex2cite."
    ], bg_color=C_WHITE, border_color=C_TEAL, title_color=C_TEAL, font_size=10.5, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 15: CONCLUSÕES E DESDOBRAMENTOS FUTUROS
    # -------------------------------------------------------------------------
    s15 = prs.slides.add_slide(blank_layout)
    add_base_decorations(s15, "Conclusões e Desdobramentos Futuros", 15, secao="Conclusão", topico="Interface Web")

    add_card(s15, 0.6, 1.35, SW - 1.2, 2.50, "Conclusões da Pesquisa", [
        "A criação da classe ifftese.cls e do pacote macros.sty cumpriu com pleno êxito o objetivo de abstrair as normas ABNT e IBGE;",
        "Constatou-se uma redução drástica no tempo operacional de formatação e eliminação de inconsistências formais entre usuários;",
        "A solução democratiza o rigor tipográfico do LaTeX em toda a comunidade do Instituto Federal Fluminense."
    ], bg_color=C_WHITE, border_color=C_GREEN, title_color=C_DARK, font_size=11, space_after=6)

    add_card(s15, 0.6, 4.15, SW - 1.2, 2.70, "Trabalho em Andamento: Interface Web por Formulários", [
        "Desenvolvimento de uma plataforma online institucional intuitiva dedicada exclusivamente à ifftese.cls;",
        "O autor preenche apenas formulários web amigáveis com os metadados do trabalho e o texto das seções científicas;",
        "O servidor em nuvem compila a arte-final em PDF com perfeição nos bastidores, eliminando qualquer contato direto com código TeX."
    ], bg_color=C_BLOCK_BG, border_color=C_TEAL, title_color=C_TEAL, font_size=11, space_after=6)

    # -------------------------------------------------------------------------
    # SLIDE 16: SLIDE UNIFICADO DE AGRADECIMENTO (VIA LÁCTEA BLUR)
    # -------------------------------------------------------------------------
    s16 = prs.slides.add_slide(blank_layout)
    if os.path.exists(BG_BLUR):
        s16.shapes.add_picture(BG_BLUR, Inches(0), Inches(0), width=Inches(SW), height=Inches(SH))

    # Centered translucent/dark card
    card_w16 = 9.8
    card_h16 = 6.2
    card_l16 = (SW - card_w16) / 2.0
    card_t16 = 0.65

    c16 = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(card_l16), Inches(card_t16), Inches(card_w16), Inches(card_h16))
    c16.fill.solid()
    c16.fill.fore_color.rgb = C_DARK_CARD
    c16.line.color.rgb = C_GREEN
    c16.line.width = Pt(1.5)

    tb16 = s16.shapes.add_textbox(Inches(card_l16 + 0.4), Inches(card_t16 + 0.30), Inches(card_w16 - 0.8), Inches(2.2))
    tf16 = tb16.text_frame
    tf16.word_wrap = True

    p = tf16.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r1 = p.add_run()
    r1.text = "Muito Obrigado!"
    r1.font.name = "Arial"
    r1.font.size = Pt(26)
    r1.font.bold = True
    r1.font.color.rgb = C_GREEN

    r2 = p.add_run()
    r2.text = "   —   Perguntas & Discussão"
    r2.font.name = "Arial"
    r2.font.size = Pt(18)
    r2.font.bold = True
    r2.font.color.rgb = C_WHITE
    p.space_after = Pt(4)

    p_sub = tf16.add_paragraph()
    p_sub.alignment = PP_ALIGN.CENTER
    r_sub = p_sub.add_run()
    r_sub.text = "CONEPE 2026 — XIII Congresso de Ensino, Pesquisa e Extensão"
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = RGBColor(220, 220, 220)
    p_sub.space_after = Pt(4)

    p_cont = tf16.add_paragraph()
    p_cont.alignment = PP_ALIGN.CENTER
    r_c_lbl = p_cont.add_run()
    r_c_lbl.text = "Contatos: "
    r_c_lbl.font.name = "Arial"
    r_c_lbl.font.size = Pt(11)
    r_c_lbl.font.bold = True
    r_c_lbl.font.color.rgb = RGBColor(200, 200, 200)

    r_c1 = p_cont.add_run()
    r_c1.text = "pedroiff0@gmail.com"
    r_c1.font.name = "Arial"
    r_c1.font.size = Pt(11)
    r_c1.font.bold = True
    r_c1.font.color.rgb = C_GREEN
    r_c1.hyperlink.address = "mailto:pedroiff0@gmail.com"

    r_pipe = p_cont.add_run()
    r_pipe.text = "   |   "
    r_pipe.font.name = "Arial"
    r_pipe.font.size = Pt(11)
    r_pipe.font.color.rgb = RGBColor(160, 160, 160)

    r_c2 = p_cont.add_run()
    r_c2.text = "ana.soja@iff.edu.br"
    r_c2.font.name = "Arial"
    r_c2.font.size = Pt(11)
    r_c2.font.bold = True
    r_c2.font.color.rgb = C_GREEN
    r_c2.hyperlink.address = "mailto:ana.soja@iff.edu.br"

    # Inner White Container for QR Code
    qr_w = 2.7
    qr_h = 2.7
    box_w = 3.1
    box_h = 3.0
    box_l = (SW - box_w) / 2.0
    box_t = card_t16 + 1.85

    c_qr_box = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(box_l), Inches(box_t), Inches(box_w), Inches(box_h))
    c_qr_box.fill.solid()
    c_qr_box.fill.fore_color.rgb = C_WHITE
    c_qr_box.line.color.rgb = C_WHITE

    if os.path.exists(QR_IMG):
        qr_l = (SW - qr_w) / 2.0
        qr_t = box_t + 0.15
        s16.shapes.add_picture(QR_IMG, Inches(qr_l), Inches(qr_t), width=Inches(qr_w), height=Inches(qr_h))

    # Bottom Link and Support
    tb16_bot = s16.shapes.add_textbox(Inches(card_l16 + 0.4), Inches(box_t + box_h + 0.15), Inches(card_w16 - 0.8), Inches(1.1))
    tf16_bot = tb16_bot.text_frame
    tf16_bot.word_wrap = True

    p_link = tf16_bot.paragraphs[0]
    p_link.alignment = PP_ALIGN.CENTER
    r_lk = p_link.add_run()
    r_lk.text = "https://phrandrade.com"
    r_lk.font.name = "Arial"
    r_lk.font.size = Pt(14)
    r_lk.font.bold = True
    r_lk.font.color.rgb = C_WHITE
    r_lk.hyperlink.address = "https://phrandrade.com"
    p_link.space_after = Pt(6)

    p_ack = tf16_bot.add_paragraph()
    p_ack.alignment = PP_ALIGN.CENTER
    r_ak = p_ack.add_run()
    r_ak.text = "Apoio Institucional: CNPq (Projeto 129985/2025-2), IFF Bom Jesus, PUC-Chile e FAPERJ"
    r_ak.font.name = "Arial"
    r_ak.font.size = Pt(9.5)
    r_ak.font.color.rgb = RGBColor(190, 190, 190)

    # -------------------------------------------------------------------------
    # SLIDE 17: SLIDE WALLPAPER FINAL (VIA LÁCTEA SEM BLUR)
    # -------------------------------------------------------------------------
    s17 = prs.slides.add_slide(blank_layout)
    if os.path.exists(BG_WALLPAPER):
        s17.shapes.add_picture(BG_WALLPAPER, Inches(0), Inches(0), width=Inches(SW), height=Inches(SH))

    prs.save(OUTPUT_FILE)
    print(f"✅ Apresentação PPTX gerada com sucesso: {OUTPUT_FILE} ({len(prs.slides)} slides)")

if __name__ == "__main__":
    create_deck()
