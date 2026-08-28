import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

const CustomFooter: QuartzComponent = ({ displayClass, fileData }: QuartzComponentProps) => {
  const year = new Date().getFullYear()
  const isEn = fileData.slug?.startsWith("en") ?? false
  
  const content = {
    fullName: "Pedro Henrique Rocha de Andrade",
    subtitle: isEn 
      ? "Computer Engineering Student · Instituto Federal Fluminense" 
      : "Estudante de Engenharia de Computação · Instituto Federal Fluminense",
    builtWith: isEn ? "Built with" : "Construído com"
  }

  return (
    <footer class={classNames(displayClass, "custom-footer")} style={{ marginTop: "3rem", textAlign: "center", padding: "2rem 1rem" }}>
      <hr style={{ borderColor: "var(--lightgray)", marginBottom: "1.5rem" }} />
      
      <div class="footer-profile" style={{ marginBottom: "1.2rem" }}>
        <h3 style={{ margin: "0 0 0.25rem 0", fontSize: "1.15rem", color: "var(--dark)", fontWeight: 700 }}>
          {content.fullName}
        </h3>
        <p style={{ margin: 0, fontSize: "0.88rem", color: "var(--gray)" }}>
          {content.subtitle}
        </p>
      </div>

      <div class="footer-social-links" style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: "1.25rem", margin: "1.2rem 0", flexWrap: "wrap" }}>
        {/* GitHub */}
        <a 
          href="https://github.com/pedroiff0" 
          target="_blank" 
          rel="noopener noreferrer" 
          aria-label="GitHub"
          title="GitHub"
          class="social-icon-link"
          style={{ color: "var(--darkgray)", display: "inline-flex", alignItems: "center", justifyContent: "center", transition: "color 0.2s ease, transform 0.2s ease" }}
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4" />
            <path d="M9 18c-4.51 2-5-2-7-2" />
          </svg>
        </a>

        {/* LinkedIn */}
        <a 
          href="https://www.linkedin.com/in/pedroiff0/" 
          target="_blank" 
          rel="noopener noreferrer" 
          aria-label="LinkedIn"
          title="LinkedIn"
          class="social-icon-link"
          style={{ color: "var(--darkgray)", display: "inline-flex", alignItems: "center", justifyContent: "center", transition: "color 0.2s ease, transform 0.2s ease" }}
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" />
            <rect width="4" height="12" x="2" y="9" />
            <circle cx="4" cy="4" r="2" />
          </svg>
        </a>

        {/* Instagram */}
        <a 
          href="https://instagram.com/ra.pedroh" 
          target="_blank" 
          rel="noopener noreferrer" 
          aria-label="Instagram"
          title="Instagram"
          class="social-icon-link"
          style={{ color: "var(--darkgray)", display: "inline-flex", alignItems: "center", justifyContent: "center", transition: "color 0.2s ease, transform 0.2s ease" }}
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect width="20" height="20" x="2" y="2" rx="5" ry="5" />
            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
            <line x1="17.5" x2="17.51" y1="6.5" y2="6.5" />
          </svg>
        </a>

        {/* Email */}
        <a 
          href="mailto:pedroiff0@gmail.com" 
          aria-label="Email"
          title="Email"
          class="social-icon-link"
          style={{ color: "var(--darkgray)", display: "inline-flex", alignItems: "center", justifyContent: "center", transition: "color 0.2s ease, transform 0.2s ease" }}
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect width="20" height="16" x="2" y="4" rx="2" />
            <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7" />
          </svg>
        </a>

        {/* Portfólio / Website */}
        <a 
          href="https://www.phrandrade.com" 
          target="_blank" 
          rel="noopener noreferrer" 
          aria-label="Portfólio / Website"
          title="Portfólio / Website"
          class="social-icon-link"
          style={{ color: "var(--darkgray)", display: "inline-flex", alignItems: "center", justifyContent: "center", transition: "color 0.2s ease, transform 0.2s ease" }}
        >
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10" />
            <line x1="2" x2="22" y1="12" y2="12" />
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
          </svg>
        </a>
      </div>

      <p style={{ margin: "1rem 0 0 0", fontSize: "0.82rem", color: "var(--gray)" }}>
        © {year} <strong>{content.fullName}</strong> · {content.builtWith} <a href="https://quartz.jzhao.xyz/" target="_blank" rel="noopener noreferrer" style={{ color: "var(--secondary)", textDecoration: "none" }}>Quartz</a>
      </p>
    </footer>
  )
}

CustomFooter.afterDOMLoaded = `
function initMermaid() {
  const isDark = document.documentElement.getAttribute("saved-theme") === "dark" || 
                 document.documentElement.dataset.theme === "dark" ||
                 document.documentElement.getAttribute("data-theme") === "dark";
  const theme = isDark ? "dark" : "default";

  const codeBlocks = Array.from(document.querySelectorAll("pre > code.language-mermaid, pre.mermaid, div.mermaid, .language-mermaid"));
  if (codeBlocks.length === 0) return;

  function run() {
    if (window.mermaid) {
      window.mermaid.initialize({
        startOnLoad: false,
        theme: theme,
        securityLevel: 'loose',
        fontFamily: 'inherit'
      });
      
      codeBlocks.forEach((block, index) => {
        const pre = block.closest("pre") || block;
        if (pre.dataset.mermaidRendered) return;
        const code = (block.tagName === "CODE" ? block.textContent : block.querySelector("code")?.textContent || block.textContent).trim();
        const container = document.createElement("div");
        container.className = "mermaid-diagram";
        container.style.display = "flex";
        container.style.justifyContent = "center";
        container.style.margin = "1.5rem 0";
        container.style.overflowX = "auto";
        pre.dataset.mermaidRendered = "true";
        pre.parentNode.insertBefore(container, pre);
        pre.style.display = "none";
        
        const renderId = "mermaid-" + index + "-" + Math.random().toString(36).substring(2, 7);
        window.mermaid.render(renderId, code).then(result => {
          container.innerHTML = result.svg;
        }).catch(err => {
          console.warn("Mermaid render fallback:", err);
          pre.style.display = "block";
          container.remove();
        });
      });
    }
  }

  if (!window.mermaid) {
    const script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js";
    script.onload = run;
    document.head.appendChild(script);
  } else {
    run();
  }
}

document.addEventListener("nav", initMermaid);
document.addEventListener("render", initMermaid);
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initMermaid);
} else {
  initMermaid();
}
`;

export default (() => CustomFooter) satisfies QuartzComponentConstructor
