import json, os, re

def canvas_to_markdown(canvas_path, output_md_paths, obsidian_md_path=None):
    svg_str = generate_canvas_svg(canvas_path)
    return svg_str

def generate_canvas_svg(canvas_path):
    if not os.path.exists(canvas_path):
        return ""

    with open(canvas_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = data.get("nodes", [])
    edges = data.get("edges", [])

    if not nodes:
        return ""

    min_x = min(n["x"] for n in nodes) - 50
    min_y = min(n["y"] for n in nodes) - 50
    max_x = max(n["x"] + n["width"] for n in nodes) + 50
    max_y = max(n["y"] + n["height"] for n in nodes) + 50

    svg_w = max_x - min_x
    svg_h = max_y - min_y

    color_map = {
        "1": "#f43f5e", # red
        "2": "#f97316", # orange
        "3": "#eab308", # yellow
        "4": "#10b981", # green
        "5": "#06b6d4", # cyan
        "6": "#8b5cf6"  # purple
    }

    node_dict = {n["id"]: n for n in nodes}

    svg_lines = []
    for edge in edges:
        fn = node_dict.get(edge.get("fromNode"))
        tn = node_dict.get(edge.get("toNode"))
        if not fn or not tn: continue

        fx = fn["x"] + fn["width"] / 2 - min_x
        fy = fn["y"] + fn["height"] / 2 - min_y
        tx = tn["x"] + tn["width"] / 2 - min_x
        ty = tn["y"] + tn["height"] / 2 - min_y

        svg_lines.append(
            f'<line x1="{fx}" y1="{fy}" x2="{tx}" y2="{ty}" stroke="var(--gray)" stroke-width="2.5" stroke-dasharray="6,4" opacity="0.6" marker-end="url(#arrow)"/>'
        )

    svg_cards = []
    for n in nodes:
        nx = n["x"] - min_x
        ny = n["y"] - min_y
        nw = n["width"]
        nh = n["height"]
        color_code = color_map.get(str(n.get("color", "")), "#8b5cf6")

        raw_text = n.get("text", "")
        # Clean Wikilinks into purely informative text without broken links
        clean_raw = re.sub(r"\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) if m.group(2) else m.group(1).split("/")[-1], raw_text)
        
        lines = [l.strip() for l in clean_raw.splitlines() if l.strip()]

        text_svg_elements = []
        curr_y = ny + 28

        for line in lines:
            if line.startswith("#"):
                clean_l = re.sub(r"^#+\s*", "", line).strip()
                text_svg_elements.append(
                    f'<text x="{nx + 16}" y="{curr_y}" font-family="sans-serif" font-size="15" font-weight="700" fill="{color_code}">{clean_l}</text>'
                )
                curr_y += 24
            elif line.startswith("*") or line.startswith("-"):
                clean_l = line.strip("* -").strip()
                clean_l = clean_l.replace("**", "")
                text_svg_elements.append(
                    f'<text x="{nx + 20}" y="{curr_y}" font-family="sans-serif" font-size="13" fill="var(--dark)">• {clean_l}</text>'
                )
                curr_y += 20
            else:
                clean_l = line.replace("**", "").strip()
                text_svg_elements.append(
                    f'<text x="{nx + 16}" y="{curr_y}" font-family="sans-serif" font-size="13" font-weight="600" fill="var(--dark)">{clean_l}</text>'
                )
                curr_y += 20

        node_box_svg = f'''
  <g class="canvas-node">
    <rect x="{nx}" y="{ny}" width="{nw}" height="{nh}" rx="12" ry="12" fill="var(--light)" stroke="{color_code}" stroke-width="2.5"/>
    <rect x="{nx}" y="{ny}" width="{nw}" height="7" rx="3" ry="3" fill="{color_code}"/>
    {"".join(text_svg_elements)}
  </g>'''
        svg_cards.append(node_box_svg)

    lines_str = "\n".join(svg_lines)
    cards_str = "\n".join(svg_cards)

    return f'''<svg viewBox="0 0 {svg_w} {svg_h}" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; border-radius: 12px; background: var(--light); padding: 12px; border: 1px solid var(--lightgray); box-sizing: border-box;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--gray)"/>
    </marker>
  </defs>
  {lines_str}
  {cards_str}
</svg>'''

if __name__ == '__main__':
    canvas_p = "/home/pedro/hardcore-life/00 - Mapa/Mapa Geral.canvas"
    svg_res = generate_canvas_svg(canvas_p)
    print("SVG Canvas generated successfully. Length:", len(svg_res))
