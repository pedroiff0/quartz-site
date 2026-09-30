export const REQUIRED_CLASS = "page-layout"

const ALIASES = { "center-title": "center-titles", "center-image": "center-images", "card": "cards" }

export function normalizeCssClasses(value) {
  let list = []
  if (Array.isArray(value)) list = value
  else if (typeof value === "string") list = value.split(/[\s,]+/)
  const out = [REQUIRED_CLASS]
  for (const raw of list) {
    if (raw === null || raw === undefined) continue
    let c = String(raw).trim().toLowerCase()
    if (!c || c === "none" || c === "null" || c === "~") continue
    c = c.replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "")
    c = ALIASES[c] ?? c
    if (c && !out.includes(c)) out.push(c)
  }
  return out
}

export const CssClasses = () => ({
  name: "CssClasses",
  htmlPlugins() {
    return [
      () => (_tree, file) => {
        const fm = file.data.frontmatter ?? (file.data.frontmatter = {})
        fm.cssclasses = normalizeCssClasses(fm.cssclasses ?? fm.cssclass)
      },
    ]
  },
})

export default CssClasses
