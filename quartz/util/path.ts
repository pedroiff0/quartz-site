import {
  slugifyFilePath as defaultSlugifyFilePath,
  getFileExtension,
} from "@quartz-community/utils"
import type { FilePath, FullSlug } from "@quartz-community/utils"

export {
  isFilePath,
  isFullSlug,
  isSimpleSlug,
  isRelativeURL,
  isAbsoluteURL,
  getFullSlug,
  simplifySlug,
  joinSegments,
  endsWith,
  trimSuffix,
  stripSlashes,
  getFileExtension,
  isFolderPath,
  getAllSegmentPrefixes,
  pathToRoot,
  resolveRelative,
  splitAnchor,
  slugTag,
  transformInternalLink,
  transformLink,
  normalizeHastElement,
} from "@quartz-community/utils"

function normalizeForComparison(s: string): string {
  return s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
}

function isFolderNoteMatch(parentSeg: string, fileSeg: string): boolean {
  if (parentSeg === "index" || fileSeg === "index") return false

  const pNorm = normalizeForComparison(parentSeg)
  const fNorm = normalizeForComparison(fileSeg)

  // 1. Direct match or normalized diacritic-insensitive match
  // (e.g. "introducao-a-engenharia" vs "introdução-à-engenharia", "1-periodo" vs "1º-período")
  if (pNorm === fNorm) return true

  // 2. Hub / Disciplinas prefix
  // (e.g. "Hub — Fundamentos Da Computacao" in "fundamentos-da-computacao", "Disciplinas Eletivas" in "eletivas")
  const fClean = normalizeForComparison(fileSeg.replace(/^(?:hub\s*[-—]\s*|disciplinas\s*)/i, ""))
  if (pNorm === fClean) return true

  // 3. Anotações / Atividades
  // (e.g. "Anotações — Introducao A Engenharia" in "Anotações", "Atividades — ..." in "Atividades")
  if (
    (pNorm === "anotacoes" && fNorm.startsWith("anotacoes-")) ||
    (pNorm === "atividades" && fNorm.startsWith("atividades-"))
  ) {
    return true
  }

  return false
}

export function slugifyFilePath(fp: FilePath, excludeExt?: boolean): FullSlug {
  const slug = defaultSlugifyFilePath(fp, excludeExt)

  const ext = excludeExt ? "" : (getFileExtension(slug) ?? "")
  const withoutExt = ext ? slug.slice(0, -ext.length) : slug

  const segments = withoutExt.split("/")
  if (segments.length >= 2) {
    const parentSeg = segments[segments.length - 2]
    const fileSeg = segments[segments.length - 1]

    if (isFolderNoteMatch(parentSeg, fileSeg)) {
      segments[segments.length - 1] = "index"
      return (segments.join("/") + ext) as FullSlug
    }
  }

  return slug
}

export type {
  FilePath,
  FullSlug,
  SimpleSlug,
  RelativeURL,
  TransformOptions,
} from "@quartz-community/utils"

// --- v5-specific exports below ---

export const QUARTZ = "quartz"

// from micromorph/src/utils.ts
// https://github.com/natemoo-re/micromorph/blob/main/src/utils.ts#L5
const _rebaseHtmlElement = (el: Element, attr: string, newBase: string | URL) => {
  const rebased = new URL(el.getAttribute(attr)!, newBase)
  el.setAttribute(attr, rebased.pathname + rebased.hash)
}
export function normalizeRelativeURLs(el: Element | Document, destination: string | URL) {
  el.querySelectorAll('[href=""], [href^="./"], [href^="../"]').forEach((item) => {
    _rebaseHtmlElement(item, "href", destination)
  })
  el.querySelectorAll('[src=""], [src^="./"], [src^="../"]').forEach((item) => {
    _rebaseHtmlElement(item, "src", destination)
  })
}
