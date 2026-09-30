import glob, re

for filepath in glob.glob('content/pt-br/academic/courses/latex/aula-*.md'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Matches the PPTX row in the table
    # Example: | 📊 **Slides PPTX (.zip)** | [Acessar Slide PPTX](/resource/areas/academico/biblioteca/latex-escrita/slides-pptx/aula-13.zip) |
    new_content = re.sub(r'\|\s*(?:📊|.*?)\s*\*\*Slides PPTX.*?\n', '', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed PPTX link from {filepath}")
