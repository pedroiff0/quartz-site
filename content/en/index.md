---
publish: true
title: About Me
created: 2026-07-18
modified: 2026-07-26T12:36:37.259-03:00
published: 2026-07-26T12:36:37.259-03:00
cssclasses:
  - page-layout
---

> [!info] Welcome!
> This is your starting page! Here you will find everything you need to know about my journey, research, and work. Read in the suggested order to have the best possible experience. 😊

> [!abstract] Also check out my portfolio
> If you came from my **[projects portfolio](https://pedroiff0.github.io/webpage/)** (or just want a quick overview of everything I've built), it lists all my GitHub repositories — public and private — each with a *short brief*, plus my research grants and all contacts on a single page. This site here is the full content (research, classes, media and blog).

## 📚 Where to start?

### 1️⃣ First step: About me

<img src="..[Profilepic.Jpe](/assets/profilepic.jpe)g" alt="Pedro Henrique" width="160" height="160" style="border-radius: 50%; aspect-ratio: 1 / 1; object-fit: cover; float: right; margin-left: 1rem; margin-bottom: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">

I am Pedro Henrique, an undergraduate Computer Engineering student at the [Fluminense Federal Institute](https://portal1.iff.edu.br/), in Rio de Janeiro, Brazil. Since 2022, I have been building a bridge between **computer science** and **astronomy**, working on research projects that explore stellar populations and the structure of the Milky Way.

My passion lies at the intersection of **computational methods** and **astrophysical problems**. I believe that open-source tools and reproducible workflows are essential to advancing science and making it more accessible to everyone.

### 🌐 Social Media

If you'd like to get in touch, send an email!

- 🎓 [**Currículo Lattes**](http://lattes.cnpq.br/6818168089966785)
- 💻 [GitHub](https://github.com/pedroiff0)
- 💼 [LinkedIn](https://www.linkedin.com/in/pedroiff0/)
- 📸 [Instagram](https://instagram.com/ra.pedroh)
- 🔬 [ORCID](https://orcid.org/0009-0003-6724-4640)
- ✉️ [Email](mailto:pedroiff0@gmail.com)

### 📄 Curriculum Vitae

Below my CV in this page's language and the (multilingual LaTeX) repository that generates it:

<div class="cv-cards-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.25rem; margin: 1.75rem 0;">

  <a href="/assets/curriculo/englishCV.pdf" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit; display: flex;">
    <div style="background: var(--light); border: 1px solid var(--lightgray); border-radius: 10px; padding: 1.25rem 1.5rem; width: 100%; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.25s ease; box-shadow: 0 2px 6px rgba(0,0,0,0.04);" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 6px rgba(0,0,0,0.04)';">
      <div>
        <div style="font-size: 1.6rem; margin-bottom: 0.75rem; line-height: 1;">🇬🇧</div>
        <div style="font-weight: 700; font-size: 1.05rem; margin-bottom: 0.35rem; color: var(--dark);">CV in English</div>
        <div style="font-size: 0.85rem; color: var(--gray); line-height: 1.4;">Two-column PDF version</div>
      </div>
      <div style="margin-top: 1.25rem; font-weight: 600; font-size: 0.85rem; color: var(--tertiary); display: flex; align-items: center; gap: 0.35rem;">
        <span>Download / View PDF</span> <span>↗</span>
      </div>
    </div>
  </a>

  <a href="https://github.com/pedroiff0/curriculo" target="_blank" rel="noopener noreferrer" style="text-decoration: none; color: inherit; display: flex;">
    <div style="background: var(--light); border: 1px solid var(--lightgray); border-radius: 10px; padding: 1.25rem 1.5rem; width: 100%; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.25s ease; box-shadow: 0 2px 6px rgba(0,0,0,0.04);" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 6px 16px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='0 2px 6px rgba(0,0,0,0.04)';">
      <div>
        <div style="font-size: 1.6rem; margin-bottom: 0.75rem; line-height: 1;">📄</div>
        <div style="font-weight: 700; font-size: 1.05rem; margin-bottom: 0.35rem; color: var(--dark);">CV Repository</div>
        <div style="font-size: 0.85rem; color: var(--gray); line-height: 1.4;">LaTeX source (PT/EN/ES/FR)</div>
      </div>
      <div style="margin-top: 1.25rem; font-weight: 600; font-size: 0.85rem; color: var(--tertiary); display: flex; align-items: center; gap: 0.35rem;">
        <span>View on GitHub</span> <span>↗</span>
      </div>
    </div>
  </a>

</div>

### 📬 Get in touch

Prefer not to open your email client? Fill in the fields below and the message lands straight in my inbox.

<form id="contact-form" class="contact-form">
  <input type="text" name="from_name" placeholder="Your name" required>
  <input type="email" name="reply_to" placeholder="Your email" required>
  <textarea name="message" placeholder="Your message" rows="5" required></textarea>
  <button type="submit">Send</button>
  <p id="contact-form-status"></p>
</form>

<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>

<script>
(function() {
  // TODO(Pedro): replace with your credentials from https://dashboard.emailjs.com
  // (create a free account, an Email Service and an Email Template using the
  // from_name / reply_to / message variables from the form above).
  var EMAILJS_PUBLIC_KEY = "fh5Z3HcsBAXFKJ-Jd";
  var EMAILJS_SERVICE_ID = "service_myxxjn7";
  var EMAILJS_TEMPLATE_ID = "template_1baqk12";

  var form = document.getElementById("contact-form");
  var status = document.getElementById("contact-form-status");
  if (!form) return;
  if (window.emailjs === undefined) {
    status.textContent = "The send service didn't load (an ad/privacy blocker or proxy may be blocking cdn.jsdelivr.net). Please email me directly for now.";
    return;
  }
  emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });

  form.addEventListener("submit", function(e) {
    e.preventDefault();
    if (EMAILJS_PUBLIC_KEY.indexOf("HERE") !== -1) {
      status.textContent = "Form not configured yet — please email me directly for now.";
      return;
    }
    status.textContent = "Sending…";
    emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form).then(
      function() {
        status.textContent = "Message sent — thanks for reaching out! If it doesn't arrive in a few minutes, check your Spam/Junk folder.";
        form.reset();
      },
      function(err) {
        status.textContent = "Couldn't send it right now (error " + (err && err.status ? err.status : "?") + "). Try again or email me directly.";
      }
    );
  });
})();
</script>

### 2️⃣ Second step: Areas of Interest

- **Astrophysics**: Galactic archaeology, stellar populations, Milky Way structure and chemical evolution, large-scale astronomical data analysis.
- **Computer Science**: Scientific computing, data pipelines, machine learning applications in astronomy, open-source development.
- **Psychoanalysis**:

### 3️⃣ Third step: Explore the content

To navigate my work, explore the sections of this site:

<div class="media-carousel">
  <a href="/en/research" class="carousel-slide">
    <img src="/assets/illustrations/research.svg" alt="Research" />
    <div class="slide-caption">Research</div>
  </a>
  <a href="/en/resource" class="carousel-slide">
    <img src="/assets/illustrations/resource.svg" alt="Resources" />
    <div class="slide-caption">Resources</div>
  </a>
  <a href="/en/resource/engenharia-de-computação" class="carousel-slide">
    <img src="/assets/illustrations/classes.svg" alt="Classes" />
    <div class="slide-caption">Classes</div>
  </a>
  <a href="/en/media" class="carousel-slide">
    <img src="/assets/photos/febic2024/febic.jpeg" alt="Media" />
    <div class="slide-caption">Media</div>
  </a>
</div>

The links below are currently available only in Portuguese:

- [[pt-br/research/|Research]] — Learn about my current projects and publications.
- [[pt-br/resource/|Resources]] — Materials, scripts, and useful tools I've developed or use.
- [[pt-br/media/|Media]] — Participations in events, fairs, and presentations.

This site is written in two languages: all content is first written in **Portuguese (Brazil)** and translated to English as time allows — so not every page has an English version yet. If you noticed something missing or outdated in translation, feel free to open an [issue in the repository](https://github.com/pedroiff0/quartz-site/issues), or [click here to open one pre-filled from the translation template](https://github.com/pedroiff0/quartz-site/issues/new?template=traducao.yml).
