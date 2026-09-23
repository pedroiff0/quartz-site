import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
import { pathToRoot } from "../util/path"

const AuthorProfile: QuartzComponent = ({ displayClass, fileData }: QuartzComponentProps) => {
  // Translate based on path
  const isEn = fileData.slug?.startsWith("en") ?? false
  const baseDir = pathToRoot(fileData.slug!)
  
  const content = {
    location: isEn ? "Bom Jesus do Itabapoana, RJ - Brazil" : "Bom Jesus do Itabapoana, RJ - Brasil",
    institution: "Instituto Federal Fluminense",
    bio: isEn ? "I am an undergraduate student in Computer Engineering at the Fluminense Federal Institute, in Rio de Janeiro, Brazil. I have been working with astronomy since 2022." : "Sou estudante de Engenharia de Computação no Instituto Federal Fluminense, no Rio de Janeiro, Brasil. Trabalho com astronomia desde 2022.",
    email: "pedroiff0@gmail.com",
    cv: isEn ? "View CV" : "Ver CV",
    cvLink: "/cv.pdf",
    timezone: isEn ? "Time: " : "Hora: "
  }

  const iconStyle = { verticalAlign: "-2px", marginRight: "6px" }

  return (
    <div class={classNames(displayClass, "author-profile")}>
      <details class="author-details">
        <summary class="author-summary">
          <img src={baseDir + "assets/profilepic.jpeg"} alt="Pedro H. R. de Andrade" class="author-avatar-small" />
          <span>Pedro H. R. de Andrade</span>
        </summary>
        <div class="author-info">
          <img src={baseDir + "assets/profilepic.jpeg"} alt="Pedro H. R. de Andrade" class="author-avatar" />
          <p class="author-bio">{content.bio}</p>
          <p class="author-detail">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style={iconStyle}><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
            {content.institution}
          </p>
          <p class="author-detail">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style={iconStyle}><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
            {content.location}
          </p>
          <p class="author-detail">
            <a href={"mailto:" + content.email}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style={iconStyle}><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
              {content.email}
            </a>
          </p>
          <p class="author-detail">
            <a href={baseDir + content.cvLink.replace(/^\//, '')} target="_blank">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style={iconStyle}><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>
              {content.cv}
            </a>
          </p>
          <p class="author-detail" id="author-time">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style={iconStyle}><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            {content.timezone} <span></span>
          </p>
        </div>
      </details>
      <script dangerouslySetInnerHTML={{
        __html: `
          function updateTime() {
            const timeSpan = document.querySelector('#author-time span');
            if (!timeSpan) return;
            const now = new Date();
            timeSpan.textContent = now.toLocaleTimeString('pt-BR', { timeZone: 'America/Sao_Paulo', hour: '2-digit', minute: '2-digit' });
          }
          updateTime();
          setInterval(updateTime, 10000);
        `
      }} />
    </div>
  )
}



export default (() => AuthorProfile) satisfies QuartzComponentConstructor
