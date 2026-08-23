#!/usr/bin/env python3
import re
from pathlib import Path

"""Extract and normalize disciplines from the Resolução text export.

This script assumes the Resolução PDF has been converted to text at /tmp/resolucao.txt
(e.g., via `pdftotext -layout`).

It produces a single normalized output file with:
- EMENTA on one line
- OBJETIVOS with • bullets
- CONTEÚDOS PROGRAMÁTICOS using numbered headings (1., 2., ...) and '-' bullets
- Bibliography items enumerated (1., 2., ...)

Usage:
  python3 generate_disciplinas_2_periodo_completos.py [PERIOD]

If PERIOD is not provided, it defaults to 2.
"""

import sys

RESOL_TXT = Path('/tmp/resolucao.txt')

# Accept either a numeric period (1..10) or special keyword 'eletivas'.
period_arg = sys.argv[1] if len(sys.argv) > 1 else '2'
if period_arg.isdigit():
    period = int(period_arg)
    mode = 'period'
else:
    period = period_arg.lower()
    mode = 'eletivas' if period in ('eletivas', 'eletiva', 'optativas', 'optativo') else 'period'

if mode == 'period':
    OUT_TXT = Path(__file__).resolve().parent / f'disciplinas_{period}_periodo_completos.txt'
else:
    OUT_TXT = Path(__file__).resolve().parent / f'disciplinas_{period}_completos.txt'

text = RESOL_TXT.read_text(encoding='utf-8').splitlines()

if mode == 'period':
    # Find the section boundaries for Nº PERÍODO based on the explicit 'Nº PERÍODO' marker.
    # Use exact match to avoid TOC entries.
    idx_start = [i for i, l in enumerate(text) if l.strip() == f'{period}º PERÍODO']
    idx_next = [i for i, l in enumerate(text) if l.strip() == f'{period+1}º PERÍODO']
    if not idx_start:
        raise SystemExit(f'Could not find {period}º PERÍODO marker in resolucao text')

    start_idx = max(idx_start)
    # find first (period+1)º marker after the (period)º marker
    candidates = [i for i in idx_next if i > start_idx]
    if candidates:
        end_idx = min(candidates)
    else:
        # If there is no next period marker, use end of document
        end_idx = len(text)
else:
    # Eletivas section: find the *real* section marker (not TOC).
    # Prefer the '4.7.2. COMPONENTES CURRICULARES ELETIVOS OU OPTATIVOS' heading.
    start_idx = next(
        (i for i, l in enumerate(text) if '4.7.2.' in l and 'COMPONENTES CURRICULARES ELETIVOS' in l.upper()),
        None,
    )
    if start_idx is None:
        start_idx = next((i for i, l in enumerate(text) if 'COMPONENTES CURRICULARES ELETIVOS' in l.upper()), None)
    if start_idx is None:
        raise SystemExit('Could not find COMPONENTES CURRICULARES ELETIVOS section in resolucao text')

    # End at the next major section marker (e.g., FLEXIBILIZAÇÃO CURRICULAR)
    end_idx = next(
        (i for i, l in enumerate(text[start_idx + 1:], start_idx + 1) if '4.8.' in l or 'FLEXIBILIZAÇÃO' in l.upper()),
        None,
    )
    if end_idx is None:
        end_idx = len(text)

section = text[start_idx:end_idx]

section = text[start_idx:end_idx]

# Filter out page footers / headers
filtered = []
for line in section:
    if line.strip().startswith('RESOLUÇÃO CONSUP'):
        continue
    if re.match(r'^\s*\d+\s*$', line):
        continue
    if line.strip().upper().startswith('PÁGINA'):
        continue
    filtered.append(line)

# Split into blocks by COMPONENTE CURRICULAR:
blocks = []
current = []
for line in filtered:
    if line.strip().startswith('COMPONENTE CURRICULAR:'):
        if current:
            blocks.append(current)
        current = [line]
    else:
        if current:
            current.append(line)
if current:
    blocks.append(current)

# Helpers
code_re = re.compile(r'CSECBJ[I]?\.(\d+)')


def find_field(block, label):
    for i, l in enumerate(block):
        if l.strip().upper().startswith(label.upper()):
            return i
    return None


def tidy_paragraphs(lines: list[str]) -> list[str]:
    """Join lines broken by PDF line wrapping into paragraphs and remove empty list markers."""
    out: list[str] = []
    for line in lines:
        stripped = line.rstrip()
        if not stripped:
            out.append('')
            continue
        # drop pure numbering placeholders (e.g., '1.', '2.', '•')
        if re.match(r'^(\d+\.|•|•\s*)$', stripped.strip()):
            continue
        if out and out[-1] and not out[-1].endswith(('.', '!', '?', ';', ':')) and not stripped.lstrip().startswith(('•', 'o', '-', '1.', '2.', '3.', 'a.', 'b.', 'c.', 'd.', 'e.', 'f.')):
            out[-1] = out[-1] + ' ' + stripped.lstrip()
        else:
            out.append(stripped)
    # remove consecutive blank lines
    collapsed: list[str] = []
    for line in out:
        if not line.strip():
            if collapsed and not collapsed[-1].strip():
                continue
            collapsed.append('')
        else:
            if line.strip() in ('-', '•'):
                continue
            collapsed.append(line)
    return collapsed


# --- Normalization helpers --------------------------------------------------

def normalize_ementa(lines: list[str]) -> list[str]:
    """Flatten EMENTA into a single line and remove PDF layout noise."""
    joined = ' '.join(l.strip() for l in lines if l.strip())

    # Drop leading PDF layout artifacts such as carga horária fields.
    # Often the ementa begins with a word like "Conceitos" while the preceding junk is
    # "Extensão – 0h/a" or "Prática (X)".
    joined = joined.strip()
    joined = re.sub(
        r'^(?:\s*(?:Extensão|Específica|Pesquisa|Teórica|Prática|Laboratorial|Carga|Aulas|Período|Série)[^A-ZÀ-Ú]*)+',
        '',
        joined,
    ).strip()

    # If the result still begins with an unlikely token (e.g., a lone word followed by dash),
    # keep the first capitalized phrase with at least two words.
    m = re.search(r'([A-ZÀ-Ú][a-zà-ú]{2,}(?:\s+[a-zà-ú]{2,})+.*)', joined)
    if m:
        joined = m.group(1).strip()

    return [joined] if joined else []


def normalize_objetivos(lines: list[str]) -> list[str]:
    """Normalize OBJETIVOS to use bullet '•' and collapse blank lines."""
    out: list[str] = []
    for l in lines:
        stripped = l.strip()
        if not stripped:
            if out and out[-1].strip():
                out.append('')
            continue
        # remove existing bullets
        cleaned = re.sub(r'^[\-•oO]\s*', '', stripped)
        out.append(f'• {cleaned}')
    return out


def normalize_conteudos(lines: list[str]) -> list[str]:
    """Normalize CONTEÚDOS PROGRAMÁTICOS to use numbered headings and '-' bullets."""
    out: list[str] = []
    heading_counter = 0
    for l in lines:
        stripped = l.strip()
        if not stripped:
            # Preserve a single blank line between sections
            if out and out[-1].strip():
                out.append('')
            continue

        # Remove existing bullet markers so we don't double-prefix.
        clean = re.sub(r'^[\-•oO]\s*', '', stripped)

        # Fix cases like '4. g. ...' (drop the lettered sub-item)
        m = re.match(r'^\s*\d+\.\s*[a-zA-Z]\.\s*(.*)$', clean)
        if m:
            out.append(f'- {m.group(1).strip()}')
            continue

        # If already a numbered heading like '1. ...', keep the numbering and update counter.
        m = re.match(r'^(\d+)\.\s*(.*)$', clean)
        if m:
            heading_counter = int(m.group(1))
            out.append(f"{heading_counter}. {m.group(2).strip()}")
            continue

        # If looks like a section heading ending in ':' and not already numbered
        if clean.endswith(':') and not clean.startswith('-'):
            heading_counter += 1
            out.append(f"{heading_counter}. {clean}")
            continue

        # If it's a lettered list like 'a. ...'
        m = re.match(r'^[a-zA-Z]\.\s*(.*)$', clean)
        if m:
            out.append(f"- {m.group(1).strip()}")
            continue

        # Otherwise treat as a bullet item.
        out.append(f"- {clean}")

    return out


def _split_bibliography_line(line: str) -> list[str]:
    """Split a bibliography line into multiple entries if it contains more than one."""
    # common split point: a period followed by whitespace and then a new entry starting with an author name.
    # Author names in the PDF can be all caps (e.g., MENDHAM) or mixed case.
    parts = re.split(r"(?<=\.)\s+(?=[A-ZÀ-Ú][A-Za-zÀ-Úà-ú]+,\s+[A-ZÀ-Ú])", line)
    # if we didn't split, try splitting on ' 3. ' style (numbered entries concatenated)
    if len(parts) == 1:
        parts = re.split(r"(?<=\.)\s+(?=\d+\.)", line)
    return [p.strip() for p in parts if p.strip()]


def normalize_bibliografia(lines: list[str]) -> list[str]:
    """Ensure bibliography items are enumerated and clean up existing bullets."""
    out: list[str] = []
    num = 1
    for l in lines:
        stripped = l.strip()
        if not stripped:
            # preserve blank lines
            if out and out[-1].strip():
                out.append('')
            continue
        # split into multiple entries if needed
        for piece in _split_bibliography_line(stripped):
            # remove existing bullets / numbering
            cleaned = re.sub(r'^[\-•oO]\s*', '', piece)
            cleaned = re.sub(r'^\d+\.\s*', '', cleaned)
            cleaned = cleaned.strip()
            if not cleaned:
                continue
            out.append(f"{num}. {cleaned}")
            num += 1

    # Merge broken bibliography lines that start with lower-case or edition fragments
    merged: list[str] = []
    for line in out:
        m = re.match(r'^(\d+)\.\s*(.*)$', line)
        if not m:
            merged.append(line)
            continue
        line_num = int(m.group(1))
        text = m.group(2)
        if merged and re.match(r'^(?:\d+\s+ed\.|ed\.|[a-zçáéíóúãõâêô]+)', text):
            merged[-1] = merged[-1].rstrip() + ' ' + text
        else:
            merged.append(line)
    return merged


def extract_section(block, label, stop_labels=None, strip_metadata=None, strip_contains=None):
    idx = find_field(block, label)
    if idx is None:
        return []
    out: list[str] = []
    for l in block[idx + 1:]:
        if stop_labels and any(l.strip().upper().startswith(s.upper()) for s in stop_labels):
            break
        out.append(l)
    # strip leading/trailing blanks
    while out and not out[0].strip():
        out.pop(0)
    while out and not out[-1].strip():
        out.pop()

    if strip_metadata:
        # drop leading metadata lines
        while out and any(out[0].strip().startswith(p) for p in strip_metadata):
            out.pop(0)

    if strip_contains:
        filtered: list[str] = []
        for l in out:
            if any(s.lower() in l.lower() for s in strip_contains):
                continue
            filtered.append(l)
        out = filtered

    return tidy_paragraphs(out)


def detect_discipline_name(block):
    # after COMPONENTE CURRICULAR:, next non-empty non-label line is likely name
    seen_cc = False
    for l in block:
        if not seen_cc:
            if l.strip().startswith('COMPONENTE CURRICULAR:'):
                seen_cc = True
            continue
        line = l.strip()
        if not line:
            continue
        # skip known labels
        if any(line.startswith(p) for p in ['ANO DE IMPLANTAÇÃO', '(X)']):
            continue
        if ':' in line and line.upper().split(':')[0].strip() in ['CÁLCULO', 'CARGA', 'CÓDIGO', 'PRÉ-REQUISITO', 'CORREQUISITO', 'PERÍODO', 'NATUREZA', 'CAMPUS', 'CURSO', 'ESPECIFICAÇÃO', 'ATIVIDADE', 'NATUREZA', 'CARGA', 'ECTS']:
            continue
        # likely name
        return line
    return None


def get_code(block):
    for l in block:
        m = code_re.search(l)
        if m:
            return f'CSECBJI.{m.group(1)}'
    return None


def get_period(block):
    """Extract the curriculum period (e.g., 2º) from various label formats.

    The raw PDF text can use either:
    - 'Período: 2º'
    - 'Série e/ou Período: 2º'
    - 'Período: 2°' (degree sign)
    """

    # Search for any line mentioning "período" (case-insensitive) and capture a trailing ordinal number.
    for l in block:
        if 'período' in l.lower():
            m = re.search(r'(\d+)\s*[º°]', l)
            if m:
                return int(m.group(1))

    # Fallback: search entire block for an ordinal number (e.g., '2º' or '2°')
    for l in block:
        m = re.search(r'(\d+)\s*[º°]', l)
        if m:
            return int(m.group(1))

    return None


out: list[str] = []
sep = '=' * 131

for block in blocks:
    block_period = get_period(block)

    if mode == 'period' and block_period != period:
        continue

    code = get_code(block)
    name = detect_discipline_name(block) or f'Código {code or "?"}'

    ementa = normalize_ementa(extract_section(
        block,
        'EMENTA:',
        stop_labels=['OBJETIVOS:', 'REFERÊNCIAS:', 'COMPETÊNCIAS'],
        strip_metadata=[
            'Carga horária',
            'Código:',
            'Período:',
            '(X)',
            'Natureza',
            'Especificação',
            'Carga horária presencial',
            'Carga horária prática',
            'Carga horária teórica',
            'Carga horária a distância',
            'Carga horária de extensão',
        ],
        strip_contains=[
            'carga horária',
            'código:',
            'período:',
            'carga horária presencial',
            'carga horária prática',
            'carga horária teórica',
            'carga horária a distância',
            'carga horária de extensão',
            'período:',
        ],
    ))
    objetivos = normalize_objetivos(extract_section(block, 'OBJETIVOS:', stop_labels=['CONTEÚDOS PROGRAMÁTICOS:', 'REFERÊNCIAS:', 'COMPETÊNCIAS']))
    conteudos = normalize_conteudos(extract_section(block, 'CONTEÚDOS PROGRAMÁTICOS:', stop_labels=['REFERÊNCIAS:', 'COMPETÊNCIAS']))

    # References split into básica/complementar (stop at CAMPUS / CURSO markers)
    referencias_raw = extract_section(block, 'REFERÊNCIAS:', stop_labels=['CAMPUS:', 'CURSO:', '4.7.1.', '4.8.', 'FLEXIBILIZAÇÃO'])
    bib_basica: list[str] = []
    bib_compl: list[str] = []

    # find BIBLIOGRAFIA BÁSICA / COMPLEMENTAR within references
    if referencias_raw:
        try:
            idx_basica = next(i for i, l in enumerate(referencias_raw) if l.strip().upper().startswith('BIBLIOGRAFIA BÁSICA'))
        except StopIteration:
            idx_basica = None
        try:
            idx_compl = next(i for i, l in enumerate(referencias_raw) if l.strip().upper().startswith('BIBLIOGRAFIA COMPLEMENTAR'))
        except StopIteration:
            idx_compl = None

        if idx_basica is not None:
            end = idx_compl if idx_compl is not None and idx_compl > idx_basica else len(referencias_raw)
            bib_basica = referencias_raw[idx_basica + 1:end]
        if idx_compl is not None:
            bib_compl = referencias_raw[idx_compl + 1:]

    bib_basica = normalize_bibliografia(tidy_paragraphs(bib_basica))
    bib_compl = normalize_bibliografia(tidy_paragraphs(bib_compl))

    out.append(sep)
    out.append('')
    out.append(f'EMENTA DE {name}')
    out.append('')
    out.append('EMENTA:')
    out.extend(ementa)
    out.append('')
    out.append('OBJETIVOS:')
    out.extend(objetivos)
    out.append('')
    out.append('CONTEÚDOS PROGRAMÁTICOS:')
    out.extend(conteudos)
    out.append('')
    out.append('REFERÊNCIAS:')
    if bib_basica:
        out.append('BIBLIOGRAFIA BÁSICA:')
        out.extend(bib_basica)
        out.append('')
    if bib_compl:
        out.append('BIBLIOGRAFIA COMPLEMENTAR:')
        out.extend(bib_compl)
        out.append('')

# Add fallback placeholders for disciplines that appear in the period curriculum list but are not present in the detailed blocks.
# These are only needed for 2º período, where the PDF does not contain some discipline details.
if mode == 'period' and period == 2:
    existing_names = {line[len('EMENTA DE '):] for line in out if line.startswith('EMENTA DE ')}
    for fallback in [
        'Algoritmos e Técnicas de Programação',
        'Matemática Discreta',
        'Química',
    ]:
        if not any(fallback in name for name in existing_names):
            out.append(sep)
            out.append('')
            out.append(f'EMENTA DE {fallback}')
            out.append('')
            out.append('EMENTA:')
            out.append('Sem ementa disponível no PDF.')
            out.append('')

OUT_TXT.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')
print(f'Wrote {OUT_TXT} with {len(out)} lines (approx).')
