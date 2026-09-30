#!/usr/bin/env python3
"""Adiciona ao git (add -f) as imagens de content/resource referenciadas por notas de content/pt-br. Bloqueia documentos/curriculo/pessoal/chaves."""
import re, subprocess, sys, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
BLOCK = ("/documentos/", "/curriculo/", "/areas/pessoal/", "/chaves", "/certificad")
REF = re.compile(r"""(?:!\[\[|\]\(|src=["'])/?(resource/[^\]|)"'#]+?\.(?:png|jpe?g|gif|svg|webp))""", re.I)
files = set()
for md in (CONTENT / "pt-br").rglob("*.md"):
    for m in REF.finditer(md.read_text(encoding="utf-8", errors="ignore")):
        rel = urllib.parse.unquote(m.group(1))
        p = CONTENT / rel
        if p.is_file() and not any(b in "/" + rel.lower() for b in BLOCK):
            files.add(p)
for f in sorted(files):
    subprocess.run(["git", "add", "-f", "--", str(f)], cwd=ROOT, check=True)
print(f"{len(files)} imagens referenciadas adicionadas")
