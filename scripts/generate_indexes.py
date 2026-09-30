import os
import urllib.parse

def main():
    # Use relative paths for GitHub Actions environment
    base_resource = "content/pt-br/academic/engenharia-computacao"
    base_assets = "content/resource/areas/academico/disciplinas"

    if not os.path.exists(base_resource):
        print(f"Directory not found: {base_resource}")
        return

    for period in os.listdir(base_resource):
        period_path = os.path.join(base_resource, period)
        if os.path.isdir(period_path):
            for disc in os.listdir(period_path):
                disc_path = os.path.join(period_path, disc)
                if os.path.isdir(disc_path) and disc != "anotacoes":
                    
                    anotacoes_dir = os.path.join(disc_path, "anotacoes")
                    os.makedirs(anotacoes_dir, exist_ok=True)
                    
                    # 1. Collect notes
                    anotacoes_files = []
                    for root, _, files in os.walk(anotacoes_dir):
                        for file in files:
                            if file.endswith(".md") and file != "index.md":
                                fpath = os.path.join(root, file)
                                rel_path = os.path.relpath(fpath, anotacoes_dir)
                                anotacoes_files.append((file, rel_path))
                    
                    # 2. Collect assets
                    asset_dir = os.path.join(base_assets, period, disc)
                    assets_files = []
                    if os.path.exists(asset_dir):
                        for root, _, files in os.walk(asset_dir):
                            for file in files:
                                if file != "index.md" and file != ".DS_Store":
                                    fpath = os.path.join(root, file)
                                    rel_path = os.path.relpath(fpath, base_assets)
                                    assets_files.append((file, rel_path))
                    
                    # 3. Generate index.md content
                    index_anotacoes = os.path.join(anotacoes_dir, "index.md")
                    
                    md = "---\ntitle: Anotações e Arquivos\npublish: true\npassword: \"engcomp20232\"\n---\n\n"
                    
                    md += "## 📝 Base de Dados de Anotações\n\n"
                    if anotacoes_files:
                        md += "| Nome da Anotação | Acessar |\n"
                        md += "|------------------|---------|\n"
                        for fname, frel in sorted(anotacoes_files):
                            name = frel.replace('.md', '')
                            # Use absolute unique wikilink with escaped pipe for table compatibility
                            wiki_path = f"pt-br/academic/engenharia-computacao/{period}/{disc}/anotacoes/{name}"
                            md += f"| 📄 {name.split('/')[-1]} | [[{wiki_path}\\|Acessar Anotação]] |\n"
                    else:
                        md += "Nenhuma anotação encontrada.\n"
                        
                    md += "\n## 📎 Base de Dados de Arquivos\n\n"
                    if assets_files:
                        md += "| Arquivo / Documento | Link de Acesso |\n"
                        md += "|---------------------|----------------|\n"
                        for fname, frel in sorted(assets_files):
                            full_asset_path = f"/resource/areas/academico/disciplinas/{frel}"
                            encoded_asset_path = urllib.parse.quote(full_asset_path)
                            md += f"| 📦 {fname} | [Baixar / Ver Arquivo]({encoded_asset_path}) |\n"
                    else:
                        md += "Nenhum arquivo encontrado.\n"
                    
                    # Write only if changed to prevent unnecessary git churn (if run locally)
                    # or just overwrite (since it's in CI)
                    with open(index_anotacoes, "w", encoding="utf-8") as f:
                        f.write(md)

    print("Index tables generated successfully.")

if __name__ == "__main__":
    main()
