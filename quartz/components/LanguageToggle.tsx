import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const LanguageToggle: QuartzComponent = ({ displayClass, cfg }: QuartzComponentProps) => {
  // pathname already starts with "/" (or is just "/" with nothing after it),
  // so stripping a trailing slash gives "" for a bare-domain baseUrl and
  // "/subpath" for a project-page baseUrl -- either way `${basePath}/en/`
  // below ends up with exactly one slash between them, never "//en/".
  const basePath = cfg.baseUrl
    ? new URL(`https://${cfg.baseUrl}`).pathname.replace(/\/$/, "")
    : ""

  return (
    <div class={classNames(displayClass, "nav-lang")}>
      <a href={`${basePath}/en/`} title="English" data-lang="en" data-router-ignore onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'en')">EN</a>
      <a href={`${basePath}/pt-br/`} title="Português" data-lang="pt-br" data-router-ignore onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'pt-br')">PT</a>
      <a href={`${basePath}/es/`} title="Español" data-lang="es" data-router-ignore onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'es')">ES</a>
      <a href={`${basePath}/fr/`} title="Français" data-lang="fr" data-router-ignore onclick="event.preventDefault(); window.location.href = window.translatePath(window.location.pathname, 'fr')">FR</a>
      <script dangerouslySetInnerHTML={{
        __html: `
          if (!window.translatePath) {
            // Content slugs are identical across locales (content/en/x mirrors
            // content/pt-br/x), so switching language is just swapping that one
            // path segment — no per-folder dictionary to keep in sync.
            window.translatePath = function(path, targetLang) {
              const parts = path.split('/').filter(p => p);
              const langIdx = parts.findIndex(p => p === 'en' || p === 'pt-br' || p === 'es' || p === 'fr');

              // Everything before the language segment is the base path (e.g. GitHub Pages project prefix)
              const prefix = langIdx === -1 ? parts : parts.slice(0, langIdx);
              const rest = langIdx === -1 ? [] : parts.slice(langIdx + 1);

              // Only add a trailing slash if the current URL already has one
              // (folder/index pages) -- leaf pages have no trailing slash and
              // a spurious one 404s instead of resolving.
              const trailingSlash = path.endsWith('/') ? '/' : '';
              return '/' + [...prefix, targetLang, ...rest].join('/') + trailingSlash;
            };
          }
        `
      }} />
    </div>
  )
}



export default (() => LanguageToggle) satisfies QuartzComponentConstructor
