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
      <a href={`${basePath}/en/`} title="English" data-lang="en" data-router-ignore onclick="event.preventDefault(); window.goLang('en')"><img class="nav-lang-flag" src={`${basePath}/static/flags/flag-us.svg`} alt="English" width="24" height="16" loading="lazy" /><span class="nav-lang-label">EN</span></a>

      <script dangerouslySetInnerHTML={{
        __html: `
          if (!window.goLang) {
            // Sem traducao ainda: vai para o index do idioma com ?untranslated=1,
            // que revela o callout "untranslated" da nota de index.
            window.goLang = function(target) {
              const dest = window.translatePath(window.location.pathname, target);
              if (target === 'pt-br') { window.location.href = dest; return; }
              const root = dest.replace(/^(.*\\/(?:en|es|fr)\\/).*$/, '$1');
              if (dest === root) { window.location.href = dest; return; }
              const key = dest.replace(/^\\/|\\/$/g, '').toLowerCase();
              (window.fetchData || Promise.resolve({})).then(function(idx) {
                const found = idx[key] != null || idx[key + '/index'] != null;
                window.location.href = found ? dest : root + '?untranslated=1';
              }).catch(function() { window.location.href = root + '?untranslated=1'; });
            };
          }
          if (new URLSearchParams(window.location.search).has('untranslated')) {
            document.documentElement.classList.add('show-untranslated');
          }
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
