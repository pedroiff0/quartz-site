import { ValidLocale } from "../i18n"
import { QuartzPluginData } from "../plugins/vfile"

interface Props {
  date: Date
  locale?: ValidLocale
}

export type ValidDateType = keyof Required<QuartzPluginData>["dates"]

export function getDate(data: QuartzPluginData): Date | undefined {
  if (!data.defaultDateType) {
    throw new Error(
      `Field 'defaultDateType' was not set. Ensure the CreatedModifiedDate plugin is configured with a 'defaultDateType' option. See https://quartz.jzhao.xyz/plugins/CreatedModifiedDate for more details.`,
    )
  }
  return data.dates?.[data.defaultDateType]
}

export function formatDate(d: Date, locale: ValidLocale = "en-US"): string {
  const day = d.getDate()
  const year = d.getFullYear()
  const rawHours = d.getHours()
  const rawMins = d.getMinutes()
  const minsStr = String(rawMins).padStart(2, "0")
  const hasTime = rawHours !== 0 || rawMins !== 0

  const isEn = locale === "en-US" || locale === "en-GB" || locale.startsWith("en")
  const isEs = locale.startsWith("es")
  const isFr = locale.startsWith("fr")

  if (isEn) {
    const enMonths = [
      "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"
    ]
    const monthName = enMonths[d.getMonth()]
    const hours12 = rawHours % 12 || 12
    const ampm = rawHours >= 12 ? "PM" : "AM"
    const timeStr = hasTime ? ` ${hours12}:${minsStr} ${ampm}` : ""
    return `${monthName} ${day}, ${year}${timeStr}`
  }

  if (isEs) {
    const esMonths = [
      "enero", "febrero", "marzo", "abril", "mayo", "junio",
      "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    const monthName = esMonths[d.getMonth()]
    const timeStr = hasTime ? ` ${String(rawHours).padStart(2, "0")}:${minsStr}` : ""
    return `${day} de ${monthName} de ${year}${timeStr}`
  }

  if (isFr) {
    const frMonths = [
      "janvier", "février", "mars", "avril", "mai", "juin",
      "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    const monthName = frMonths[d.getMonth()]
    const timeStr = hasTime ? ` ${String(rawHours).padStart(2, "0")}:${minsStr}` : ""
    return `${day} ${monthName} ${year}${timeStr}`
  }

  // Padrão: Português (pt-BR) com mês por extenso
  const ptMonths = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
  ]
  const monthName = ptMonths[d.getMonth()]
  const timeStr = hasTime ? ` ${String(rawHours).padStart(2, "0")}:${minsStr}` : ""
  return `${day} de ${monthName} de ${year}${timeStr}`
}

export function Date({ date, locale }: Props) {
  return <time datetime={date.toISOString()}>{formatDate(date, locale)}</time>
}
