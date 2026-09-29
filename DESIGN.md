# DESIGN — Quartz Site Architecture & Design Rules

## 1. Arquitetura do Digital Garden

```mermaid
graph TD
    Vault["Obsidian Vault (hardcore-life)"] -->|scripts/sync_vault.py (Filtro publish: true)| Content["content/ (Markdown Curado)"]
    Content --> QuartzEngine["Quartz v4 Engine (TypeScript / Remark)"]
    Plugins["local-plugins/ (Plugins Customizados)"] --> QuartzEngine
    Config["quartz.config.yaml"] --> QuartzEngine
    QuartzEngine --> Static["public/ (HTML/CSS/JS Estático)"]
    Static --> GHPages["GitHub Pages Deployment"]
```

---

## 2. Princípios de Design e Curadoria

1. **Filtro Estrito de Publicação:**
   - Nenhuma nota deve ser publicada sem `publish: true` explícito no frontmatter.
   - Notas diárias, metadados internos e pastas privadas são bloqueadas permanentemente.
2. **Navegação & Grafo de Conhecimento:**
   - Backlinks e visualizador de grafo interativo habilitados para explorar conexões temáticas entre conceitos acadêmicos, técnicos e de engenharia.
