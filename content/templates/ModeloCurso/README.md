---
cssclasses:
  - page-layout
---

# 🏛️ Template Oficial de Cursos para o Quartz

Este diretório contém o **modelo padrão oficial** para criação e estruturação de novos cursos no site Quartz do **Prof. Pedro Henrique Rocha de Andrade (IFF — Campus Bom Jesus do Itabapoana)**.

---

## 🚀 Como Utilizar para Criar um Novo Curso

1. **Copiar esta pasta**:
   Copie a pasta `content/templates/ModeloCurso` para a localização desejada dentro de `content[[pt-br/resource|Resource]]/` (exemplo: `content[[pt-br/resource/Engenharia%20de%20Computa%C3%A7%C3%A3o/3-periodo/programacao-orientada-a-objeto|Programacao Orientada A Objeto]]s`).

2. **Editar o `index.md`**:
   - Atualize os metadados do frontmatter (`title`, `tags`).
   - Modifique a introdução, articulação curricular e critérios de avaliação.
   - Ajuste o filtro `file.folder.startsWith(...)` no bloco ````base```` para apontar para a pasta do novo curso.

3. **Criar os Arquivos de Aula (`aula-01-*.md`)**:
   - Utilize a estrutura de `aula-01-exemplo.md` como base.
   - Preencha o frontmatter (`title`, `publish`, `notas`, `slide`).
   - Atualize a tabela de **Material Didático** com os links correspondentes aos PDFs/recursos da aula em `/assets/biblioteca/<slug-do-curso>/`.

4. **Publicar**:
   - Realize o `git add .`, `git commit` e `git push`. A tabela dinamica ````base```` e o Quartz construirão a página do curso automaticamente no build!
