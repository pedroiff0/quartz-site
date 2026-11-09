export function parseLevels(value) {
  const raw = Array.isArray(value) ? value : value === undefined || value === null ? [] : String(value).split(/[\s,]+/)
  const out = []
  for (const r of raw) {
    const n = parseInt(String(r).replace(/^h/i, ""), 10)
    if (n >= 1 && n <= 6 && !out.includes(n)) out.push(n)
  }
  return out
}

const level = (n) => (n && n.type === "element" && /^h[1-6]$/.test(n.tagName) ? Number(n.tagName[1]) : 0)

export function wrap(children, levels) {
  const out = []
  for (let i = 0; i < children.length; i++) {
    const node = children[i]
    const lv = level(node)
    if (!levels.includes(lv)) {
      out.push(node)
      continue
    }
    let j = i + 1
    while (j < children.length && !(level(children[j]) && level(children[j]) <= lv)) j++
    const body = wrap(children.slice(i + 1, j), levels)
    out.push({
      type: "element",
      tagName: "details",
      properties: { className: ["collapsible-heading", `collapsible-heading-h${lv}`] },
      children: [
        { type: "element", tagName: "summary", properties: {}, children: [node] },
        { type: "element", tagName: "div", properties: { className: ["collapsible-heading-body"] }, children: body },
      ],
    })
    i = j - 1
  }
  return out
}

export const CollapsibleHeadings = () => ({
  name: "CollapsibleHeadings",
  htmlPlugins() {
    return [
      () => (tree, file) => {
        const levels = parseLevels(file.data.frontmatter?.collapse)
        if (levels.length && tree.children) tree.children = wrap(tree.children, levels)
      },
    ]
  },
})

export default CollapsibleHeadings
